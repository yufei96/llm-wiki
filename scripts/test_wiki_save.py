"""Run with python -B scripts/test_wiki_save.py; all wiki writes stay temporary."""
import json
import gc
import importlib.util
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import threading
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SAVE_SCRIPT = ROOT / "scripts" / "wiki-save.py"


def prepare(root: Path):
    (root / "scripts").mkdir(parents=True)
    shutil.copy2(SAVE_SCRIPT, root / "scripts" / "wiki-save.py")
    (root / ".scratch" / "research-workbench").mkdir(parents=True)
    (root / "wiki" / "topics").mkdir(parents=True)
    (root / "raw" / "articles").mkdir(parents=True)

    page = root / "wiki" / "topics" / "电芯温度趋势.md"
    index = root / "wiki" / "索引.md"
    log = root / "wiki" / "日志.md"
    source = root / "raw" / "articles" / "热循环测试.md"
    page.write_text(
        "---\ntitle: 电芯温度趋势\nsource: [raw/articles/热循环测试.md]\n---\n"
        "# 电芯温度趋势\n\n## 现有结论\n待复核。\n",
        encoding="utf-8",
    )
    index.write_text(
        "# 知识库索引\n\n## 主题\n\n- [[电芯温度趋势]] — 待复核\n",
        encoding="utf-8",
    )
    log.write_text("# Wiki 活动日志\n", encoding="utf-8")
    source.write_text(
        "热循环测试记录：环境温度为 25 ℃ 时，经过 100 次循环后，容量保持率为 96%。\n",
        encoding="utf-8",
    )
    return page, index, log, source


def make_plan(root: Path, scope="25 ℃ 下 100 次热循环后的容量保持率"):
    return {
        "scope": scope,
        "page": {
            "path": "wiki/topics/电芯温度趋势.md",
            "content": (
                "---\ntitle: 电芯温度趋势\nsource: [raw/articles/热循环测试.md]\n"
                "confidence: SYNTHESIZED\n---\n# 电芯温度趋势\n\n"
                "## 结论\n原文记录 25 ℃ 条件下经过 100 次循环后容量保持率为 96%。\n\n"
                "## 证据\n原文事实：\n> 环境温度为 25 ℃ 时，经过 100 次循环后，容量保持率为 96%。\n"
                "来源：`raw/articles/热循环测试.md`，测试记录首行。\n"
            ),
        },
        "index": (
            "# 知识库索引\n\n## 主题\n\n"
            "- [[电芯温度趋势]] — 25 ℃、100 次热循环后的容量保持率为 96%。\n"
        ),
        "log_entry": (
            "## [2026-09-26] 研究 | 电芯温度趋势\n\n"
            "- 根据热循环测试原文核验容量保持率，并更新主题页和索引。"
        ),
    }


def write_plan(root: Path, plan):
    path = root / "plan.json"
    path.write_text(json.dumps(plan, ensure_ascii=False), encoding="utf-8")
    return path


def run(root: Path, *args):
    return subprocess.run(
        [sys.executable, str(root / "scripts" / "wiki-save.py"), *map(str, args)],
        cwd=root,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def preview(root: Path, plan):
    result = run(root, "preview", write_plan(root, plan))
    assert result.returncode == 0, result.stderr
    match = re.search(r"^PREVIEW ([0-9a-f]{64})$", result.stdout, re.MULTILINE)
    assert match, result.stdout
    return match.group(1), result.stdout


def load_save_module(root: Path, name="wiki_save_test"):
    script = root / "scripts" / "wiki-save.py"
    spec = importlib.util.spec_from_file_location(name, script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_save_and_duplicate_confirmation(root: Path):
    page, index, log, source = prepare(root)
    before = {p: p.read_bytes() for p in (page, index, log, source)}
    files = subprocess.run(
        ["rg", "--files", "wiki", "raw"], cwd=root, capture_output=True, text=True, encoding="utf-8"
    )
    indexed = subprocess.run(
        ["rg", "-n", "电芯温度趋势", "wiki/索引.md"], cwd=root, capture_output=True, text=True, encoding="utf-8"
    )
    evidence = subprocess.run(
        ["rg", "-n", "容量保持率为 96%", "raw"], cwd=root, capture_output=True, text=True, encoding="utf-8"
    )
    assert files.returncode == 0 and "wiki/topics/电芯温度趋势.md" in files.stdout.replace("\\", "/")
    assert indexed.returncode == 0 and "电芯温度趋势" in indexed.stdout
    assert evidence.returncode == 0 and "raw/articles/热循环测试.md:1:" in evidence.stdout.replace("\\", "/") and "96%" in evidence.stdout
    token, output = preview(root, make_plan(root))
    assert "电芯温度趋势.md" in output and "索引.md" in output and "日志.md" in output
    assert {p: p.read_bytes() for p in before} == before

    saved = run(root, "confirm", token)
    assert saved.returncode == 0, saved.stderr
    assert "已保存" in saved.stdout, saved.stdout
    assert "96%" in page.read_text(encoding="utf-8")
    assert "96%" in index.read_text(encoding="utf-8")
    assert log.read_bytes().startswith(before[log])
    assert source.read_bytes() == before[source]
    search = subprocess.run(
        ["rg", "-n", "96%", "wiki/索引.md", "wiki/topics"],
        cwd=root,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert search.returncode == 0 and "电芯温度趋势" in search.stdout, search.stdout

    mtimes = {p: p.stat().st_mtime_ns for p in (page, index, log)}
    duplicate = run(root, "confirm", token)
    assert duplicate.returncode == 0, duplicate.stderr
    assert "无需重复写入" in duplicate.stdout, duplicate.stdout
    assert {p: p.stat().st_mtime_ns for p in mtimes} == mtimes


def test_stale_target_is_preserved(root: Path):
    page, index, log, _ = prepare(root)
    token, _ = preview(root, make_plan(root))
    page.write_text(page.read_text(encoding="utf-8") + "\n## 并发修改\n保留此内容。\n", encoding="utf-8")
    concurrent = page.read_bytes()
    result = run(root, "confirm", token)
    assert result.returncode != 0 and "失效" in result.stderr, result
    assert page.read_bytes() == concurrent
    assert "待复核" in index.read_text(encoding="utf-8")
    assert log.read_text(encoding="utf-8") == "# Wiki 活动日志\n"


def test_concurrent_write_and_replace_are_blocked_while_saving(root: Path):
    page, _, _, _ = prepare(root)
    plan = make_plan(root)
    token, _ = preview(root, plan)
    save = load_save_module(root, "wiki_save_race")
    original_write = save.write_locked
    blocked = {}

    def inject_competing_edits(stream, path, data):
        if path == page and not blocked:
            write_probe = subprocess.run(
                [sys.executable, "-B", "-c",
                 "from pathlib import Path; import sys; "
                 "exec(\"try:\\n Path(sys.argv[1]).write_text('CONCURRENT EDIT\\\\n', encoding='utf-8')\\n"
                 "except OSError:\\n print('blocked')\\nelse:\\n print('written')\")",
                 str(page)],
                cwd=root, capture_output=True, text=True, encoding="utf-8",
            )
            blocked["write"] = write_probe.returncode == 0 and write_probe.stdout.strip() == "blocked"
            replacement = root / "replacement.tmp"
            replacement.write_text("REPLACEMENT THAT MUST SURVIVE\n", encoding="utf-8")
            replace_probe = subprocess.run(
                [sys.executable, "-B", "-c",
                 "import os,sys; "
                 "exec(\"try:\\n os.replace(sys.argv[1], sys.argv[2])\\n"
                 "except OSError:\\n print('blocked')\\nelse:\\n print('replaced')\")",
                 str(replacement), str(page)],
                cwd=root, capture_output=True, text=True, encoding="utf-8",
            )
            blocked["replace"] = replace_probe.returncode == 0 and replace_probe.stdout.strip() == "blocked"
        return original_write(stream, path, data)

    save.write_locked = inject_competing_edits
    save.confirm(token)

    assert blocked == {"write": True, "replace": True}, blocked
    assert page.read_text(encoding="utf-8") == plan["page"]["content"]
    assert not (root / ".scratch" / "research-workbench" / "ticket8-save-recovery.json").exists()


def test_hardlinked_raw_file_is_never_modified(root: Path):
    page, index, log, source = prepare(root)
    page.unlink()
    os.link(source, page)
    raw_before = source.read_bytes()
    index_before, log_before = index.read_bytes(), log.read_bytes()
    plan = make_plan(root)
    token, _ = preview(root, plan)

    rejected = run(root, "confirm", token)
    assert rejected.returncode != 0 and "硬链接" in rejected.stderr, rejected
    assert source.read_bytes() == raw_before and page.read_bytes() == raw_before
    assert index.read_bytes() == index_before and log.read_bytes() == log_before

    save = load_save_module(root, "wiki_save_hardlink")
    planned = {
        page: plan["page"]["content"].encode("utf-8"),
        index: plan["index"].encode("utf-8"),
        log: log_before,
    }
    records = []
    for path, after in planned.items():
        before = path.read_bytes()
        records.append({
            "path": path.relative_to(root).as_posix(),
            "before_base64": save.recovery_bytes(before),
            "before_sha256": save.digest(before),
            "after_base64": save.recovery_bytes(after),
            "after_sha256": save.digest(after),
        })
    recovery = root / ".scratch" / "research-workbench" / "ticket8-save-recovery.json"
    recovery.write_text(json.dumps({"version": 1, "files": records}), encoding="utf-8")
    rejected_recovery = run(root, "recover")
    assert rejected_recovery.returncode != 0 and "硬链接" in rejected_recovery.stderr, rejected_recovery
    assert recovery.is_file()
    assert source.read_bytes() == raw_before and page.read_bytes() == raw_before
    assert index.read_bytes() == index_before and log.read_bytes() == log_before


def test_new_page_is_created_when_no_target_exists(root: Path):
    _, index, log, source = prepare(root)
    plan = make_plan(root)
    page_path = "wiki/topics/热循环结果.md"
    plan["page"]["path"] = page_path
    plan["page"]["content"] = plan["page"]["content"].replace("电芯温度趋势", "热循环结果")
    plan["index"] = plan["index"].replace("电芯温度趋势", "热循环结果")
    plan["log_entry"] = plan["log_entry"].replace("电芯温度趋势", "热循环结果")
    token, _ = preview(root, plan)
    saved = run(root, "confirm", token)
    assert saved.returncode == 0, saved.stderr
    assert (root / page_path).is_file()
    assert "96%" in (root / page_path).read_text(encoding="utf-8")
    assert "热循环结果" in index.read_text(encoding="utf-8")
    assert "热循环结果" in log.read_text(encoding="utf-8")
    assert source.read_text(encoding="utf-8").startswith("热循环测试记录")


def test_new_preview_invalidates_old_scope(root: Path):
    page, index, log, _ = prepare(root)
    old_token, _ = preview(root, make_plan(root))
    new_token, _ = preview(root, make_plan(root, "仅比较其他温度条件"))
    assert old_token != new_token
    old = run(root, "confirm", old_token)
    assert old.returncode != 0 and "指纹" in old.stderr, old
    assert "待复核" in page.read_text(encoding="utf-8")
    assert "待复核" in index.read_text(encoding="utf-8")
    assert log.read_text(encoding="utf-8") == "# Wiki 活动日志\n"


def test_write_failure_rolls_back_prior_files(root: Path):
    page, index, log, _ = prepare(root)
    plan = make_plan(root)
    before = {p: p.read_bytes() for p in (page, index, log)}
    token, _ = preview(root, plan)
    save = load_save_module(root, "wiki_save_write_failure")
    original_write = save.write_locked
    injected = False

    def fail_during_log_write(stream, path, data):
        nonlocal injected
        if path == log and not injected:
            injected = True
            stream.seek(0)
            stream.truncate(0)
            stream.write(data[: max(1, len(data) // 2)])
            os.fsync(stream.fileno())
            raise OSError("injected partial write failure")
        return original_write(stream, path, data)

    save.write_locked = fail_during_log_write
    try:
        save.confirm(token)
        raise AssertionError("injected write failure was not raised")
    except save.SaveError as failed:
        assert "已恢复预览前内容" in str(failed), failed
    assert injected
    assert {p: p.read_bytes() for p in before} == before
    assert not (root / ".scratch" / "research-workbench" / "ticket8-save-recovery.json").exists()


def test_interrupted_save_keeps_recovery_copy_and_restores_complete_writes(root: Path):
    page, index, log, _ = prepare(root)
    before = {path: path.read_bytes() for path in (page, index, log)}
    token, _ = preview(root, make_plan(root))
    save = load_save_module(root, "wiki_save_interrupted")
    original_write = save.write_locked
    interrupted = False

    def interrupt_after_page_write(stream, path, data):
        nonlocal interrupted
        original_write(stream, path, data)
        if path == page and not interrupted:
            interrupted = True
            raise KeyboardInterrupt

    save.write_locked = interrupt_after_page_write
    try:
        save.confirm(token)
    except KeyboardInterrupt:
        pass
    else:
        raise AssertionError("the interruption was not injected")

    recovery = root / ".scratch" / "research-workbench" / "ticket8-save-recovery.json"
    assert recovery.is_file()
    assert page.read_bytes() != before[page]
    assert index.read_bytes() == before[index] and log.read_bytes() == before[log]
    result = run(root, "recover")
    assert result.returncode == 0, result.stderr
    assert {path: path.read_bytes() for path in before} == before
    assert not recovery.exists()


def test_interrupted_new_page_is_removed_from_complete_after_state(root: Path):
    original_page, index, log, _ = prepare(root)
    before = {path: path.read_bytes() for path in (original_page, index, log)}
    plan = make_plan(root)
    new_page_rel = "wiki/topics/中断后可恢复.md"
    new_page = root / new_page_rel
    plan["page"]["path"] = new_page_rel
    plan["page"]["content"] = plan["page"]["content"].replace("电芯温度趋势", "中断后可恢复")
    plan["index"] = plan["index"].replace("电芯温度趋势", "中断后可恢复")
    plan["log_entry"] = plan["log_entry"].replace("电芯温度趋势", "中断后可恢复")
    token, _ = preview(root, plan)
    save = load_save_module(root, "wiki_save_new_page_interrupted")
    original_write = save.write_locked
    interrupted = False

    def interrupt_after_new_page_write(stream, path, data):
        nonlocal interrupted
        original_write(stream, path, data)
        if path == new_page and not interrupted:
            interrupted = True
            raise KeyboardInterrupt

    save.write_locked = interrupt_after_new_page_write
    try:
        save.confirm(token)
    except KeyboardInterrupt:
        pass
    else:
        raise AssertionError("the interruption was not injected")

    recovery = root / ".scratch" / "research-workbench" / "ticket8-save-recovery.json"
    assert recovery.is_file() and new_page.read_bytes() == plan["page"]["content"].encode("utf-8")
    assert index.read_bytes() == before[index] and log.read_bytes() == before[log]
    result = run(root, "recover")
    assert result.returncode == 0, result.stderr
    assert not new_page.exists()
    assert {path: path.read_bytes() for path in before} == before
    assert not recovery.exists()


def test_recover_rechecks_snapshot_after_waiting_for_target_locks(root: Path):
    page, index, log, _ = prepare(root)
    plan = make_plan(root)
    token, _ = preview(root, plan)
    save = load_save_module(root, "wiki_save_recovery_race")
    original_write, original_open = save.write_locked, save.open_locked
    page_written = threading.Event()
    allow_confirm = threading.Event()
    recovery_loaded = threading.Event()
    allow_recover = threading.Event()
    errors = []

    def gated_write(stream, path, data):
        result = original_write(stream, path, data)
        if threading.current_thread().name == "confirm" and path == page:
            page_written.set()
            assert allow_confirm.wait(10)
        return result

    def gated_open(path, relative, **kwargs):
        if (threading.current_thread().name == "recover" and
                not recovery_loaded.is_set()):
            recovery_loaded.set()
            assert allow_recover.wait(10)
        return original_open(path, relative, **kwargs)

    def capture_error(operation):
        try:
            operation()
        except BaseException as exc:
            errors.append((threading.current_thread().name, exc))

    save.write_locked, save.open_locked = gated_write, gated_open
    confirm_thread = threading.Thread(
        target=capture_error, args=(lambda: save.confirm(token),), name="confirm")
    recover_thread = threading.Thread(
        target=capture_error, args=(save.recover,), name="recover")
    confirm_thread.start()
    assert page_written.wait(10), "confirm did not pause after its first write"
    recover_thread.start()
    try:
        assert recovery_loaded.wait(10), "recover did not load the initial snapshot"
    finally:
        allow_confirm.set()
        confirm_thread.join(10)
        allow_recover.set()
        recover_thread.join(10)
        save.write_locked, save.open_locked = original_write, original_open

    assert not confirm_thread.is_alive() and not recover_thread.is_alive()
    assert [(name, type(error)) for name, error in errors] == [("recover", save.SaveError)], errors
    assert "恢复副本已清理" in str(errors[0][1])
    assert page.read_text(encoding="utf-8") == plan["page"]["content"]
    assert index.read_text(encoding="utf-8") == plan["index"]
    assert not (root / ".scratch" / "research-workbench" / "ticket8-save-recovery.json").exists()


def test_recovery_refuses_unknown_partial_content(root: Path):
    page, index, log, _ = prepare(root)
    before = {path: path.read_bytes() for path in (page, index, log)}
    plan = make_plan(root)
    token, _ = preview(root, plan)
    save = load_save_module(root, "wiki_save_partial_interruption")
    original_write = save.write_locked

    def interrupt_mid_page_write(stream, path, data):
        if path == page:
            stream.seek(0)
            stream.truncate(0)
            stream.write(data[: max(1, len(data) // 2)])
            os.fsync(stream.fileno())
            raise KeyboardInterrupt
        return original_write(stream, path, data)

    save.write_locked = interrupt_mid_page_write
    try:
        save.confirm(token)
    except KeyboardInterrupt:
        pass
    else:
        raise AssertionError("the interruption was not injected")

    partial = page.read_bytes()
    assert partial not in (before[page], plan["page"]["content"].encode("utf-8"))
    recovery = root / ".scratch" / "research-workbench" / "ticket8-save-recovery.json"
    result = run(root, "recover")
    assert result.returncode != 0 and "部分写入" in result.stderr, result
    assert recovery.is_file()
    assert page.read_bytes() == partial
    assert index.read_bytes() == before[index] and log.read_bytes() == before[log]


def test_modified_preview_content_and_target_role_are_rejected(root: Path):
    page, index, log, _ = prepare(root)
    token, _ = preview(root, make_plan(root))
    active = root / ".scratch" / "research-workbench" / "ticket8-active-save.json"
    manifest = json.loads(active.read_text(encoding="utf-8"))
    manifest["files"][0]["content"] = "# 未展示的内容\n"
    active.write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
    result = run(root, "confirm", token)
    assert result.returncode != 0 and "指纹" in result.stderr, result
    assert "待复核" in page.read_text(encoding="utf-8")
    assert "待复核" in index.read_text(encoding="utf-8")
    assert log.read_text(encoding="utf-8") == "# Wiki 活动日志\n"

    token, _ = preview(root, make_plan(root))
    manifest = json.loads(active.read_text(encoding="utf-8"))
    manifest["files"][0]["path"] = "wiki/日志.md"
    active.write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
    result = run(root, "confirm", token)
    assert result.returncode != 0 and "索引和日志" in result.stderr, result
    assert "待复核" in page.read_text(encoding="utf-8")
    assert "待复核" in index.read_text(encoding="utf-8")
    assert log.read_text(encoding="utf-8") == "# Wiki 活动日志\n"


def test_rejected_handle_does_not_close_reused_descriptor(root: Path):
    page, _, _, _ = prepare(root)
    os.link(page, root / "alias.md")
    save = load_save_module(root, "wiki_save_descriptor")
    caught = None
    try:
        save.open_locked(page, page.name)
    except save.SaveError as exc:
        caught = exc
    assert caught is not None
    other = open(root / "other.txt", "wb", buffering=0)
    try:
        caught = None
        gc.collect()
        other.write(b"still open")
    finally:
        try:
            other.close()
        except OSError:
            pass
    assert (root / "other.txt").read_bytes() == b"still open"


def test_preview_marks_missing_final_newlines(root: Path):
    page, index, _, _ = prepare(root)
    page.write_bytes(b"old page")
    index.write_bytes(b"old index")
    plan = make_plan(root)
    plan["page"]["content"] = "new page"
    plan["index"] = "new index"
    token, output = preview(root, plan)
    marker = "\\ No newline at end of file\n"
    for line in ("-old page", "+new page", "-old index", "+new index"):
        assert line + "\n" + marker in output, output
    assert "\n--- wiki/索引.md\n" in output
    assert "\n--- wiki/日志.md\n" in output
    saved = run(root, "confirm", token)
    assert saved.returncode == 0, saved.stderr
    assert page.read_bytes() == b"new page"
    assert index.read_bytes() == b"new index"


if __name__ == "__main__":
    tests = (
        test_preview_marks_missing_final_newlines,
        test_rejected_handle_does_not_close_reused_descriptor,
        test_save_and_duplicate_confirmation,
        test_stale_target_is_preserved,
        test_concurrent_write_and_replace_are_blocked_while_saving,
        test_hardlinked_raw_file_is_never_modified,
        test_new_page_is_created_when_no_target_exists,
        test_new_preview_invalidates_old_scope,
        test_write_failure_rolls_back_prior_files,
        test_interrupted_save_keeps_recovery_copy_and_restores_complete_writes,
        test_interrupted_new_page_is_removed_from_complete_after_state,
        test_recover_rechecks_snapshot_after_waiting_for_target_locks,
        test_recovery_refuses_unknown_partial_content,
        test_modified_preview_content_and_target_role_are_rejected,
    )
    for test in tests:
        with tempfile.TemporaryDirectory(prefix="llm-wiki-save-") as directory:
            test(Path(directory))
        print(f"PASS: {test.__name__}")
