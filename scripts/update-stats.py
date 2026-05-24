#!/usr/bin/env python3
"""Update 概述.md and README.md with current wiki stats.

Run before build/deploy to ensure homepage and README reflect reality.
Integrates into Makefile as a pre-requisite for 'make build'.
"""
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI = ROOT / "wiki"
README = ROOT / "README.md"


def count_section(section: str) -> int:
    """Count non-index .md files in a wiki section."""
    d = WIKI / section
    if not d.is_dir():
        return 0
    return sum(1 for f in d.glob("*.md") if f.name != "index.md")


def count_raw() -> int:
    """Count .md files in raw/ directory."""
    raw = ROOT / "raw"
    if not raw.exists():
        return 0
    return sum(1 for f in raw.rglob("*.md") if not f.name.startswith("."))


def count_total() -> int:
    """Count all wiki pages excluding _meta and index files."""
    total = 0
    for d in WIKI.iterdir():
        if d.is_dir() and d.name != "_meta":
            total += count_section(d.name)
    return total


def count_wikilinks() -> int:
    """Count total [[wikilinks]] across all wiki pages."""
    total = 0
    for f in WIKI.rglob("*.md"):
        if f.name.startswith(".") or f.name == "index.md":
            continue
        total += f.read_text(encoding="utf-8", errors="ignore").count("[[")
    return total


def update_overview(sources: int, concepts: int, entities: int,
                    topics: int, comparisons: int, total: int):
    """Update the knowledge map table and stats line in 概述.md."""
    path = WIKI / "概述.md"
    content = path.read_text(encoding="utf-8")
    today = date.today().strftime("%Y-%m-%d")

    # 1. Update the quote block stats line
    content = re.sub(
        r'> 共\d+个知识页面，覆盖\d+个一手来源.*',
        f'> 共{total}个知识页面，覆盖{sources}个一手来源，含{count_wikilinks():,}+交叉引用和8张Mermaid架构图。',
        content,
    )

    # 2. Update the knowledge map table
    # The table looks like:
    # 2. Update the knowledge map table
    table_lines = [
        "| 层 | 文件夹 | 数量 | 功能 |",
        "|----|--------|------|------|",
        f"| 来源 | sources/ | {sources} | 一手文档摘要 |",
        f"| 概念 | concepts/ | {concepts} | 单一概念定义（含Mermaid架构图） |",
        f"| 实体 | entities/ | {entities} | 组织/人物/政策 |",
        f"| 主题 | topics/ | {topics} | 跨来源综合 |",
        f"| 对比 | comparisons/ | {comparisons} | 演化/张力/趋同分析 |",
        f"| **合计** | | **{total}** | |",
    ]

    # Find the table in the content and replace it
    table_start = content.find("| 层 | 文件夹 | 数量 | 功能 |")
    if table_start == -1:
        # Try the double-pipe variant
        table_start = content.find("|| 层 | 文件夹 | 数量 | 功能 ||")
        while table_start > 0 and content[table_start] != '\n':
            table_start -= 1
        if table_start > 0:
            table_start += 1  # past newline

    if table_start >= 0:
        # Find end of table (next blank line or section header)
        table_end = content.find("\n\n", table_start)
        if table_end == -1:
            table_end = len(content)
        content = content[:table_start] + '\n'.join(table_lines) + '\n\n' + content[table_end:]

    # 3. Update last-updated date
    content = re.sub(
        r'最后更新：\d{4}-\d{2}-\d{2}',
        f'最后更新：{today}',
        content,
    )

    path.write_text(content, encoding="utf-8")
    print(f"  Updated {path.relative_to(ROOT)}")


def update_readme(sources: int, concepts: int, entities: int,
                  topics: int, comparisons: int, total: int, raw: int):
    """Update stats line in README.md."""
    content = README.read_text(encoding="utf-8")
    today = date.today().strftime("%Y-%m-%d")

    # 1. Update the stats line under the title
    content = re.sub(
        r'📊 当前规模：\*\*\d+ 篇知识页面\*\* · \*\*\d+ 篇原始文档\*\* · .*',
        f'📊 当前规模：**{total} 篇知识页面** · **{raw} 篇原始文档** · **{count_wikilinks():,}+ 交叉引用**',
        content,
    )

    # 2. Update last-updated date
    content = re.sub(
        r'\*\*最后更新\*\*：\d{4}-\d{2}-\d{2}',
        f'**最后更新**：{today}',
        content,
    )

    README.write_text(content, encoding="utf-8")
    print(f"  Updated {README.relative_to(ROOT)}")


def main():
    print("Updating wiki stats...")
    sources = count_section("sources")
    concepts = count_section("concepts")
    entities = count_section("entities")
    topics = count_section("topics")
    comparisons = count_section("comparisons")
    total = count_total()
    raw = count_raw()

    print(f"  sources: {sources}, concepts: {concepts}, entities: {entities}, "
          f"topics: {topics}, comparisons: {comparisons}")
    print(f"  total: {total}, raw files: {raw}, wikilinks: {count_wikilinks()}")

    update_overview(sources, concepts, entities, topics, comparisons, total)
    update_readme(sources, concepts, entities, topics, comparisons, total, raw)
    print("✓ Stats updated")


if __name__ == "__main__":
    main()
