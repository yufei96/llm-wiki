#!/usr/bin/env python3
"""YAML integrity pre-check for wiki pages.

Scans all wiki/*.md files and reports issues that would break the build
or indicate stale data that needs migration:

  concepts/: confidence: EXTRACTED (should be SYNTHESIZED)
  concepts/: sources referencing raw/ files (should point to wiki/ pages)
  Any page:   fused YAML lines (list item runs into next key without newline)
  Any page:   missing required frontmatter fields (title, type)

Returns non-zero if any issues found — meant to run before build.
"""

import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent / "wiki"


def check_file(md_path: Path) -> list[str]:
    issues = []
    try:
        content = md_path.read_text(encoding="utf-8")
    except Exception:
        return [f"Cannot read: {md_path}"]

    fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return []

    fm = fm_match.group(1)
    rel = md_path.relative_to(WIKI_ROOT)

    # 1. Fused YAML line — ALWAYS check (breaks parsing)
    fm_lines = fm.split("\n")
    for i, line in enumerate(fm_lines):
        stripped = line.lstrip()
        if stripped.startswith("- ") and re.search(
            r"-\s+\S+(confidence|evidence|title|type|tags|sources|created|updated):",
            line,
        ):
            issues.append(
                f"{rel}:{i + 2}: fused YAML line — "
                f"list item runs into next key without newline"
            )

    # 2. Missing required frontmatter fields — ALWAYS check
    # Skip pages that intentionally don't have these (索引.md, 概述.md, _meta/)
    skip_confidence = (
        rel.parts[0] in ("_meta",)
        or md_path.name in ("索引.md", "概述.md", "日志.md", "README.md")
    )
    if not skip_confidence:
        for field in ["title", "type"]:
            if not re.search(rf"^{field}:", fm, re.MULTILINE):
                issues.append(f"{rel}: missing required field '{field}'")

    # 3. concepts/ specific checks
    if rel.parts[0] == "concepts":
        if re.search(r"^confidence:\s*EXTRACTED", fm, re.MULTILINE):
            issues.append(f"{rel}: confidence is EXTRACTED (should be SYNTHESIZED)")

        if re.search(
            r"^\s*-\s*raw/", fm, re.MULTILINE
        ) or re.search(r"sources:\s*\[.*?raw/", fm):
            issues.append(
                f"{rel}: sources references raw/ file (should use wiki/ page name)"
            )

    return issues


def main():
    issues = []
    for md_file in WIKI_ROOT.rglob("*.md"):
        if md_file.name == "index.md":
            continue  # auto-generated
        file_issues = check_file(md_file)
        issues.extend(file_issues)

    if issues:
        print(f"YAML integrity check: {len(issues)} issues found\n")
        for issue in issues:
            print(f"  ✗ {issue}")
        print(f"\nFix {len(issues)} issue(s) before building.")
        sys.exit(1)
    else:
        print("YAML integrity check: OK")
        sys.exit(0)


if __name__ == "__main__":
    main()
