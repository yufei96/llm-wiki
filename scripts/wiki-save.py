#!/usr/bin/env python3
"""Preview and confirm one research page, its index entry, and a log entry."""
import argparse
import base64
import ctypes
from contextlib import ExitStack
import difflib
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WIKI = (ROOT / "wiki").resolve()
INDEX = "wiki/索引.md"
LOG = "wiki/日志.md"
ACTIVE = ROOT / ".scratch" / "research-workbench" / "ticket8-active-save.json"
RECOVERY = ROOT / ".scratch" / "research-workbench" / "ticket8-save-recovery.json"
_WINDOWS_API = None


class _FileTime(ctypes.Structure):
    _fields_ = [("low", ctypes.c_uint32), ("high", ctypes.c_uint32)]


class _ByHandleFileInformation(ctypes.Structure):
    _fields_ = [
        ("attributes", ctypes.c_uint32),
        ("creation_time", _FileTime),
        ("access_time", _FileTime),
        ("write_time", _FileTime),
        ("volume_serial", ctypes.c_uint32),
        ("size_high", ctypes.c_uint32),
        ("size_low", ctypes.c_uint32),
        ("number_of_links", ctypes.c_uint32),
        ("file_index_high", ctypes.c_uint32),
        ("file_index_low", ctypes.c_uint32),
    ]


class SaveError(Exception):
    pass


def digest(data):
    return hashlib.sha256(data).hexdigest() if data is not None else None


def checked_path(relative):
    if not isinstance(relative, str):
        raise SaveError("写入路径必须是文本")
    path = Path(relative)
    resolved = (ROOT / path).resolve()
    if path.is_absolute() or path.drive or ".." in path.parts or path.suffix.lower() != ".md" or not resolved.is_relative_to(WIKI):
        raise SaveError(f"写入路径必须是 wiki/ 下的 Markdown 文件：{relative}")
    current = ROOT
    for part in path.parts:
        current /= part
        if current.is_symlink():
            raise SaveError(f"不接受符号链接路径：{relative}")
    if not resolved.parent.is_dir():
        raise SaveError(f"目标目录不存在：{relative}")
    return path.as_posix(), resolved


def read_current(path, relative):
    if not path.exists():
        return None
    if not path.is_file():
        raise SaveError(f"目标不是普通文件：{relative}")
    return path.read_bytes()


def file_entry(relative, path, content):
    before = read_current(path, relative)
    return {
        "path": relative,
        "before": digest(before),
        "before_content": before.decode("utf-8") if before is not None else None,
        "content": content,
        "after": digest(content.encode("utf-8")),
    }


def make_identity(scope, files):
    return {
        "scope": scope,
        "files": [{"path": f["path"], "before": f["before"], "after": f["after"]} for f in files],
    }


def fingerprint(scope, files):
    encoded = json.dumps(make_identity(scope, files), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return digest(encoded.encode("utf-8"))


def preview(plan_path):
    plan = json.loads(Path(plan_path).read_text(encoding="utf-8"))
    if not isinstance(plan, dict) or not isinstance(plan.get("scope"), str) or not plan["scope"].strip():
        raise SaveError("计划必须包含非空 scope")
    page = plan.get("page")
    if not isinstance(page, dict) or not isinstance(page.get("content"), str):
        raise SaveError("计划必须包含 page.path 和 page.content")
    if not isinstance(plan.get("index"), str) or not isinstance(plan.get("log_entry"), str):
        raise SaveError("计划必须包含 index 全文和 log_entry 追加内容")

    page_rel, page_path = checked_path(page.get("path"))
    if page_rel in (INDEX, LOG):
        raise SaveError("page.path 必须是知识页面，不能是索引或日志")
    index_rel, index_path = checked_path(INDEX)
    log_rel, log_path = checked_path(LOG)
    if len({str(p).casefold() for p in (page_path, index_path, log_path)}) != 3:
        raise SaveError("目标页面、索引和日志必须是三个不同文件")

    index = file_entry(index_rel, index_path, plan["index"])
    old_log = read_current(log_path, log_rel)
    if old_log is None:
        raise SaveError("wiki/日志.md 不存在，无法保证只追加")
    entry = plan["log_entry"].strip("\r\n")
    if not entry.startswith("## "):
        raise SaveError("log_entry 必须以 ## 标题开头")
    newline = "\r\n" if b"\r\n" in old_log else "\n"
    separator = "" if old_log.endswith((b"\n\n", b"\r\n\r\n")) else newline
    log_content = old_log.decode("utf-8") + separator + entry.replace("\r\n", "\n").replace("\n", newline) + newline
    log = {
        "path": log_rel,
        "before": digest(old_log),
        "before_content": old_log.decode("utf-8"),
        "content": log_content,
        "after": digest(log_content.encode("utf-8")),
    }
    files = [file_entry(page_rel, page_path, page["content"]), index, log]
    token = fingerprint(plan["scope"], files)
    manifest = {"scope": plan["scope"], "files": files, "token": token}

    ACTIVE.parent.mkdir(parents=True, exist_ok=True)
    temp = write_temp(ACTIVE, (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    try:
        os.replace(temp, ACTIVE)
    finally:
        if temp.exists():
            temp.unlink()
    for item in files:
        print("".join(difflib.unified_diff(
            (item["before_content"] or "").splitlines(keepends=True),
            item["content"].splitlines(keepends=True),
            fromfile=item["path"], tofile=item["path"],
        )), end="")
    print(f"PREVIEW {token}")


def validate_manifest(manifest, supplied_token):
    scope, files = manifest.get("scope"), manifest.get("files")
    if not isinstance(scope, str) or not scope.strip() or not isinstance(files, list) or len(files) != 3:
        raise SaveError("预览清单结构无效")
    paths = [item.get("path") for item in files if isinstance(item, dict)]
    if len(paths) != 3 or any(not isinstance(path, str) for path in paths):
        raise SaveError("预览清单必须包含一个目标页面、索引和日志")
    if paths.count(INDEX) != 1 or paths.count(LOG) != 1 or len({p.casefold() for p in paths}) != 3:
        raise SaveError("预览清单必须包含一个目标页面、索引和日志")
    page_paths = [path for path in paths if path not in (INDEX, LOG)]
    if len(page_paths) != 1 or len(set(paths)) != 3:
        raise SaveError("预览清单中的目标路径无效")
    for item in files:
        if not isinstance(item.get("content"), str):
            raise SaveError("预览清单缺少目标文本")
        relative, _ = checked_path(item["path"])
        before = item.get("before_content")
        if before is not None and not isinstance(before, str):
            raise SaveError("预览清单中的原文件内容无效")
        if digest(before.encode("utf-8") if before is not None else None) != item.get("before"):
            raise SaveError(f"预览清单中的原文件指纹无效：{relative}")
        if digest(item["content"].encode("utf-8")) != item.get("after"):
            raise SaveError(f"预览清单中的新文件指纹无效：{relative}")
    log = next(item for item in files if item["path"] == LOG)
    old_log = log["before_content"]
    addition = log["content"][len(old_log):] if old_log is not None else ""
    if old_log is None or not log["content"].startswith(old_log) or not addition.lstrip("\r\n").startswith("## "):
        raise SaveError("预览清单的日志变更不是追加记录")
    computed = fingerprint(scope, files)
    if computed != manifest.get("token") or computed != supplied_token:
        raise SaveError("预览指纹与已展示内容不匹配；请重新预览")


def write_temp(path, data):
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temp = Path(name)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        return temp
    except BaseException:
        try:
            os.close(fd)
        except OSError:
            pass
        if temp.exists():
            temp.unlink()
        raise


def windows_api():
    global _WINDOWS_API
    if os.name != "nt":
        raise SaveError("confirm 和 recover 目前仅支持 Windows；preview 可跨平台运行")
    if _WINDOWS_API is None:
        from ctypes import wintypes

        kernel = ctypes.WinDLL("kernel32", use_last_error=True)
        create = kernel.CreateFileW
        create.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID,
                           wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE]
        create.restype = wintypes.HANDLE
        set_information = kernel.SetFileInformationByHandle
        set_information.argtypes = [wintypes.HANDLE, wintypes.DWORD, ctypes.c_void_p, wintypes.DWORD]
        set_information.restype = wintypes.BOOL
        get_information = kernel.GetFileInformationByHandle
        get_information.argtypes = [wintypes.HANDLE, ctypes.POINTER(_ByHandleFileInformation)]
        get_information.restype = wintypes.BOOL
        close = kernel.CloseHandle
        close.argtypes = [wintypes.HANDLE]
        close.restype = wintypes.BOOL
        _WINDOWS_API = kernel, create, set_information, get_information, close
    return _WINDOWS_API


def open_locked(path, relative, *, create_new=False, delete=False):
    kernel, create, _, _, close = windows_api()
    import msvcrt

    access = 0x80000000 | 0x40000000  # GENERIC_READ | GENERIC_WRITE
    if delete:
        access |= 0x00010000  # DELETE, used only for a page created by this save
    disposition = 1 if create_new else 3  # CREATE_NEW or OPEN_EXISTING
    handle = create(str(path), access, 0x00000001, None, disposition, 0x00000080, None)
    if handle == ctypes.c_void_p(-1).value:
        code = ctypes.get_last_error()
        raise ctypes.WinError(code)
    fd = None
    stream = None
    try:
        fd = msvcrt.open_osfhandle(handle, os.O_RDWR | os.O_BINARY)
        stream = os.fdopen(fd, "r+b", buffering=0)
        check_single_link(stream, relative)
        return stream
    except BaseException:
        if stream is not None:
            stream.close()
        elif fd is None:
            close(handle)
        else:
            os.close(fd)
        raise


def read_locked(stream):
    stream.seek(0)
    return stream.read()


def write_locked(stream, path, data):
    stream.seek(0)
    stream.truncate(0)
    remaining = memoryview(data)
    while remaining:
        written = stream.write(remaining)
        if not written:
            raise OSError(f"写入没有前进：{path}")
        remaining = remaining[written:]
    os.fsync(stream.fileno())


def mark_for_delete(stream):
    _, _, set_information, _, _ = windows_api()
    import msvcrt

    delete_file = ctypes.c_ubyte(1)  # FILE_DISPOSITION_INFO.DeleteFile is BOOLEAN
    handle = msvcrt.get_osfhandle(stream.fileno())
    if not set_information(handle, 4, ctypes.byref(delete_file), ctypes.sizeof(delete_file)):
        raise ctypes.WinError(ctypes.get_last_error())


def check_single_link(stream, relative):
    _, _, _, get_information, _ = windows_api()
    import msvcrt

    info = _ByHandleFileInformation()
    handle = msvcrt.get_osfhandle(stream.fileno())
    if not get_information(handle, ctypes.byref(info)):
        raise ctypes.WinError(ctypes.get_last_error())
    if info.number_of_links != 1:
        raise SaveError(f"拒绝操作硬链接目标（链接数 {info.number_of_links}）：{relative}")


def recovery_bytes(data):
    return base64.b64encode(data).decode("ascii") if data is not None else None


def persist_recovery(states):
    if RECOVERY.exists():
        raise SaveError(f"存在未完成保存的恢复副本：{RECOVERY.relative_to(ROOT)}；先运行 recover")
    RECOVERY.parent.mkdir(parents=True, exist_ok=True)
    files = []
    for state in states:
        item = state["item"]
        before = state["data"]
        after = item["content"].encode("utf-8")
        files.append({
            "path": item["path"],
            "before_base64": recovery_bytes(before),
            "before_sha256": digest(before),
            "after_base64": recovery_bytes(after),
            "after_sha256": digest(after),
        })
    payload = json.dumps({"version": 1, "files": files}, ensure_ascii=False, indent=2).encode("utf-8") + b"\n"
    temp = write_temp(RECOVERY, payload)
    try:
        if RECOVERY.exists():
            raise SaveError(f"恢复副本已出现：{RECOVERY.relative_to(ROOT)}；先运行 recover")
        os.replace(temp, RECOVERY)
    finally:
        if temp.exists():
            temp.unlink()


def remove_recovery():
    try:
        RECOVERY.unlink()
    except FileNotFoundError:
        pass


def load_recovery():
    if not RECOVERY.is_file() or RECOVERY.is_symlink():
        raise SaveError(f"恢复副本不存在或不是普通文件：{RECOVERY.relative_to(ROOT)}")
    snapshot = RECOVERY.read_bytes()
    document = json.loads(snapshot.decode("utf-8"))
    if not isinstance(document, dict) or document.get("version") != 1:
        raise SaveError("恢复副本格式无效；请保留文件供人工核验")
    files = document.get("files")
    if not isinstance(files, list) or len(files) != 3 or any(not isinstance(item, dict) for item in files):
        raise SaveError("恢复副本必须包含三个目标；请保留文件供人工核验")
    paths = [item.get("path") for item in files]
    if (paths.count(INDEX) != 1 or paths.count(LOG) != 1 or
            len({path.casefold() for path in paths if isinstance(path, str)}) != 3):
        raise SaveError("恢复副本目标路径无效；请保留文件供人工核验")

    restored = []
    for item in files:
        relative, path = checked_path(item["path"])
        if relative != item["path"]:
            raise SaveError("恢复副本路径未规范化；请保留文件供人工核验")
        before_encoded, after_encoded = item.get("before_base64"), item.get("after_base64")
        try:
            before = base64.b64decode(before_encoded, validate=True) if before_encoded is not None else None
            after = base64.b64decode(after_encoded, validate=True)
        except (ValueError, TypeError) as exc:
            raise SaveError("恢复副本内容无效；请保留文件供人工核验") from exc
        if ((before is None and relative in (INDEX, LOG)) or
                digest(before) != item.get("before_sha256") or
                digest(after) != item.get("after_sha256")):
            raise SaveError("恢复副本内容指纹无效；请保留文件供人工核验")
        try:
            after.decode("utf-8")
            if before is not None:
                before.decode("utf-8")
        except UnicodeError as exc:
            raise SaveError("恢复副本不是 UTF-8 文本；请保留文件供人工核验") from exc
        restored.append({"path": path, "relative": relative, "before": before, "after": after})
    return restored, snapshot


def confirm(supplied_token):
    windows_api()
    if RECOVERY.exists():
        raise SaveError(f"存在未完成保存的恢复副本：{RECOVERY.relative_to(ROOT)}；先运行 recover")
    if not ACTIVE.is_file():
        raise SaveError("没有待确认的预览，请重新运行 preview")
    manifest = json.loads(ACTIVE.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        raise SaveError("预览清单结构无效")
    validate_manifest(manifest, supplied_token)

    with ExitStack() as stack:
        states = []
        for item in manifest["files"]:
            relative, path = checked_path(item["path"])
            try:
                stream = stack.enter_context(open_locked(path, relative))
                data = read_locked(stream)
            except OSError as exc:
                if item["before"] is None and getattr(exc, "winerror", None) in (2, 3):
                    stream, data = None, None
                else:
                    raise SaveError(f"无法锁定目标文件，可能仍被写入：{relative}：{exc}") from exc
            states.append({"item": item, "path": path, "stream": stream,
                           "data": data, "created": False})

        if all(digest(state["data"]) == state["item"]["after"] for state in states):
            print("已保存，无需重复写入：")
            for state in states:
                print(f"- {state['item']['path']}")
            return
        if not all(digest(state["data"]) == state["item"]["before"] for state in states):
            raise SaveError("目标文件在预览后已变化，预览失效；请重新读取并生成差异")

        changed = [state for state in states
                   if state["item"]["before"] != state["item"]["after"]]
        persist_recovery(states)
        attempted = []
        try:
            for state in states:
                if state["stream"] is None:
                    try:
                        state["stream"] = stack.enter_context(
                            open_locked(state["path"], state["item"]["path"], create_new=True, delete=True))
                        state["created"] = True
                    except OSError as exc:
                        raise SaveError(f"目标页面在预览后已创建，未覆盖：{state['item']['path']}") from exc

            for state in changed:
                attempted.append(state)
                write_locked(state["stream"], state["path"], state["item"]["content"].encode("utf-8"))
        except (OSError, SaveError) as exc:
            failures = []
            touched = {id(state) for state in attempted}
            for state in reversed(attempted):
                try:
                    if state["item"]["before"] is None:
                        mark_for_delete(state["stream"])
                    else:
                        write_locked(state["stream"], state["path"], state["data"])
                except (OSError, SaveError) as rollback_error:
                    failures.append(f"{state['item']['path']}: {rollback_error}")
            for state in states:
                if state["created"] and id(state) not in touched:
                    try:
                        mark_for_delete(state["stream"])
                    except (OSError, SaveError) as rollback_error:
                        failures.append(f"{state['item']['path']}: {rollback_error}")
            if not failures:
                try:
                    remove_recovery()
                except OSError as rollback_error:
                    failures.append(f"恢复副本未能清理：{rollback_error}")
            detail = f"写入失败：{exc}"
            if failures:
                detail += f"；恢复未完成，副本保留在 {RECOVERY.relative_to(ROOT)}：{'；'.join(failures)}"
            else:
                detail += "；已恢复预览前内容"
            raise SaveError(detail) from exc

        try:
            remove_recovery()
        except OSError as exc:
            raise SaveError(f"目标已写入，但恢复副本未能清理：{RECOVERY.relative_to(ROOT)}：{exc}") from exc

    print("已保存：")
    for state in states:
        print(f"- {state['item']['path']}")


def recover():
    windows_api()
    records, snapshot = load_recovery()
    with ExitStack() as stack:
        states = []
        for record in records:
            if record["before"] is None:
                try:
                    stream = stack.enter_context(open_locked(
                        record["path"], record["relative"], delete=True))
                except OSError as exc:
                    if getattr(exc, "winerror", None) not in (2, 3):
                        raise SaveError(f"无法锁定恢复目标 {record['relative']}：{exc}") from exc
                    try:
                        stream = stack.enter_context(open_locked(
                            record["path"], record["relative"], create_new=True, delete=True))
                    except OSError as create_error:
                        raise SaveError(f"恢复期间目标路径发生变化：{record['relative']}；副本保留") from create_error
                    mark_for_delete(stream)
                    states.append({"record": record, "stream": stream, "data": None, "created": True})
                    continue
                data = read_locked(stream)
                states.append({"record": record, "stream": stream, "data": data, "created": False})
                continue
            try:
                stream = stack.enter_context(open_locked(record["path"], record["relative"]))
            except OSError as exc:
                raise SaveError(f"无法锁定恢复目标 {record['relative']}：{exc}；副本保留") from exc
            states.append({"record": record, "stream": stream,
                           "data": read_locked(stream), "created": False})

        try:
            current_snapshot = RECOVERY.read_bytes()
        except OSError as exc:
            raise SaveError("等待目标锁期间恢复副本已清理；拒绝应用旧快照") from exc
        if current_snapshot != snapshot:
            raise SaveError("等待目标锁期间恢复副本已变化；拒绝应用旧快照")

        for state in states:
            record = state["record"]
            if state["created"]:
                continue
            if record["before"] is None:
                if state["data"] != record["after"]:
                    raise SaveError(f"原本不存在的页面包含预期之外或部分写入的内容：{record['relative']}；请人工核验并保留 {RECOVERY.relative_to(ROOT)}")
                continue
            if state["data"] not in (record["before"], record["after"]):
                raise SaveError(f"恢复目标包含预期之外或部分写入的内容：{record['relative']}；请人工核验并保留 {RECOVERY.relative_to(ROOT)}")

        try:
            for state in states:
                record = state["record"]
                if record["before"] is None and not state["created"]:
                    mark_for_delete(state["stream"])
                elif not state["created"] and state["data"] != record["before"]:
                    write_locked(state["stream"], record["path"], record["before"])
            remove_recovery()
        except OSError as exc:
            raise SaveError(f"恢复失败；副本保留在 {RECOVERY.relative_to(ROOT)}：{exc}") from exc

    print(f"已按恢复副本恢复目标；副本已清理：{RECOVERY.relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser(description="预览并确认研究页面、索引和日志变更")
    commands = parser.add_subparsers(dest="command", required=True)
    preview_cmd = commands.add_parser("preview", help="展示保存差异")
    preview_cmd.add_argument("plan", help="包含 scope、page、index 和 log_entry 的 JSON")
    confirm_cmd = commands.add_parser("confirm", help="按预览指纹确认写入")
    confirm_cmd.add_argument("fingerprint")
    commands.add_parser("recover", help="按未完成保存的恢复副本恢复原内容")
    args = parser.parse_args()
    try:
        if args.command == "preview":
            preview(args.plan)
        elif args.command == "confirm":
            confirm(args.fingerprint)
        else:
            recover()
        return 0
    except (OSError, UnicodeError, ValueError, KeyError, TypeError, json.JSONDecodeError, SaveError) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
