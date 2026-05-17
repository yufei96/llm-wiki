#!/usr/bin/env python3
"""
wiki-ingest: 自动化 wiki 入库管道

用法:
  python3 scripts/wiki-ingest.py <PDF路径或URL> [--title "中文标题"] [--tag MOSA] [--tag 空军]
  python3 scripts/wiki-ingest.py raw/papers/some.pdf --title "某文档标题"
  python3 scripts/wiki-ingest.py https://example.com/paper.pdf --title "某论文"

流程:
  1. 下载/复制 PDF → raw/papers/
  2. pymupdf 提取文本 → raw/articles/
  3. 生成 source 页骨架 → wiki/sources/ (需 agent 填充摘要)
  4. 更新 wiki/日志.md
"""

import argparse
import os
import re
import sys
import urllib.parse
from datetime import datetime
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
RAW_PAPERS = WIKI_ROOT / "raw" / "papers"
RAW_ARTICLES = WIKI_ROOT / "raw" / "articles"
WIKI_SOURCES = WIKI_ROOT / "wiki" / "sources"
WIKI_LOG = WIKI_ROOT / "wiki" / "日志.md"


def sanitize_filename(name: str) -> str:
    """转为 kebab-case 文件名，去除中文标点和特殊字符"""
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'[\s]+', '-', name.strip())
    name = re.sub(r'-+', '-', name)
    return name.strip('-').lower()


def download_pdf(url: str, dest: Path) -> Path:
    """下载 PDF 到目标路径"""
    import subprocess
    print(f"[1/4] 下载: {url}")
    result = subprocess.run(
        ["curl", "-fsSL", "-o", str(dest), url],
        capture_output=True, text=True, timeout=120
    )
    if result.returncode != 0:
        print(f"  ✗ 下载失败: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    print(f"  ✓ 已保存: {dest.name}")
    return dest


def copy_pdf(src: Path, dest: Path) -> Path:
    """复制本地 PDF"""
    import shutil
    print(f"[1/4] 复制: {src}")
    shutil.copy2(src, dest)
    print(f"  ✓ 已复制: {dest.name}")
    return dest


def extract_text(pdf_path: Path) -> str:
    """用 pymupdf 提取 PDF 文本"""
    print(f"[2/4] 提取文本: {pdf_path.name}")
    try:
        import fitz  # pymupdf
    except ImportError:
        print("  ✗ pymupdf 未安装，运行: pip install pymupdf", file=sys.stderr)
        sys.exit(1)

    doc = fitz.open(str(pdf_path))
    pages = []
    for i in range(len(doc)):
        page = doc[i]
        text = str(page.get_text("text") or "")
        if text.strip():
            pages.append(f"<!-- Page {i + 1} -->\n{text}")
    doc.close()

    full_text = "\n\n".join(pages)
    print(f"  ✓ 提取 {len(pages)} 页，{len(full_text)} 字符")
    return full_text


def write_article(text: str, filename: str) -> Path:
    """写入 raw/articles/"""
    article_path = RAW_ARTICLES / f"{filename}.md"
    article_path.write_text(text, encoding="utf-8")
    print(f"  ✓ 已保存: raw/articles/{article_path.name}")
    return article_path


def create_source_skeleton(title: str, filename: str, tags: list, has_pdf: bool) -> Path:
    """生成 wiki/sources/ 骨架页"""
    today = datetime.now().strftime("%Y-%m-%d")
    source_ref = f"raw/articles/{filename}.md"
    if has_pdf:
        source_ref = f"[raw/papers/{filename}.pdf, raw/articles/{filename}.md]"

    tags_str = ", ".join(tags) if tags else "待分类"

    content = f"""---
title: "{title}"
created: {today}
updated: {today}
type: source
tags: [{tags_str}]
sources: {source_ref}
confidence: PENDING
evidence: "自动生成，待人工审阅"
---

# {title}

## 摘要

<!-- TODO: 由 agent 或人工填写摘要 -->

## 关键要点

<!-- TODO: 提取关键要点 -->

## 目录

<!-- TODO: 从原文提取目录结构 -->

## 相关内容

<!-- TODO: 链接相关 wiki 页面 -->
"""

    source_path = WIKI_SOURCES / f"{title}.md"
    # 避免文件名冲突
    if source_path.exists():
        source_path = WIKI_SOURCES / f"{title}-{today}.md"

    source_path.write_text(content, encoding="utf-8")
    print(f"  ✓ 已生成: wiki/sources/{source_path.name}")
    return source_path


def update_log(title: str, action: str = "ingest"):
    """追加到 wiki/log.md"""
    today = datetime.now().strftime("%Y-%m-%d")
    entry = f"## {today} — {action} | {title}\n\n- 自动入库\n"

    if WIKI_LOG.exists():
        content = WIKI_LOG.read_text(encoding="utf-8")
        content = content.rstrip() + f"\n\n{entry}"
    else:
        content = f"# Wiki 活动日志\n\n{entry}"

    WIKI_LOG.write_text(content, encoding="utf-8")
    print(f"  ✓ 已更新 wiki/log.md")


def main():
    parser = argparse.ArgumentParser(description="Wiki 自动入库管道")
    parser.add_argument("source", help="PDF 文件路径或 URL")
    parser.add_argument("--title", "-t", help="文档中文标题（用于 source 页和文件名）")
    parser.add_argument("--tag", action="append", default=[], help="标签（可多次指定）")
    parser.add_argument("--skip-download", action="store_true", help="跳过下载，直接用已有文件")
    args = parser.parse_args()

    # 确保目录存在
    RAW_PAPERS.mkdir(parents=True, exist_ok=True)
    RAW_ARTICLES.mkdir(parents=True, exist_ok=True)
    WIKI_SOURCES.mkdir(parents=True, exist_ok=True)

    source = args.source
    is_url = source.startswith("http://") or source.startswith("https://")

    # 确定文件名
    if args.title:
        filename = sanitize_filename(args.title)
    elif is_url:
        url_name = urllib.parse.unquote(source.split("/")[-1])
        filename = sanitize_filename(Path(url_name).stem)
    else:
        filename = sanitize_filename(Path(source).stem)

    title = args.title or filename

    # Step 1: 获取 PDF
    pdf_path = RAW_PAPERS / f"{filename}.pdf"
    if is_url and not args.skip_download:
        download_pdf(source, pdf_path)
    elif not is_url:
        src = Path(source).resolve()
        if not src.exists():
            print(f"  ✗ 文件不存在: {src}", file=sys.stderr)
            sys.exit(1)
        copy_pdf(src, pdf_path)
    elif pdf_path.exists():
        print(f"[1/4] 已有 PDF: {pdf_path.name}")
    else:
        print(f"  ✗ PDF 不存在且未指定下载 URL", file=sys.stderr)
        sys.exit(1)

    # Step 2: 提取文本
    text = extract_text(pdf_path)

    # Step 3: 写入 article
    print(f"[3/4] 写入文本")
    write_article(text, filename)

    # Step 4: 生成 source 页骨架
    print(f"[4/4] 生成 source 页")
    create_source_skeleton(title, filename, args.tag, has_pdf=True)

    # 更新日志
    update_log(title)

    print(f"\n✅ 入库完成: {title}")
    print(f"   PDF:  raw/papers/{filename}.pdf")
    print(f"   文本: raw/articles/{filename}.md")
    print(f"   摘要: wiki/sources/{title}.md")
    print(f"\n⚠  source 页摘要待填充——运行 agent 处理或手动编辑")


if __name__ == "__main__":
    main()
