#!/usr/bin/env python3
"""Wiki Health Check Script - Checks for broken links, orphans, index gaps."""

import re
import sys
from pathlib import Path
from collections import defaultdict

def normalize_link(target: str) -> str:
    """Normalize a wikilink target to a page stem for lookup.

    Mirrors the normalization in build-site.py/link_converter.py.
    Cannot use Path.stem here because it strips trailing dots (V1.0 → V1).
    """
    # Strip .md extension
    if target.endswith('.md'):
        target = target[:-3]
    # Strip wiki/ prefix (Obsidian cross-vault links)
    if target.startswith('wiki/'):
        target = target[5:]
    # Extract page name from paths like raw/articles/xxx → xxx
    # Use rsplit on '/' instead of Path.stem to preserve dots in names like V1.0
    if '/' in target:
        return target.rsplit('/', 1)[-1]
    return target



def check_wiki(wiki_root):
    wiki_path = Path(wiki_root) / "wiki"
    issues = {
        "broken_links": [],
        "orphan_pages": [],
        "missing_from_index": [],
        "missing_frontmatter": [],
    }
    
    # Collect all pages (separate pass so incoming_links works correctly)
    all_pages = set()
    for f in wiki_path.glob("**/*.md"):
        if f.name.startswith('.'):
            continue
        all_pages.add(f.stem)

    # Also index raw/ files so [[raw/articles/xxx]] links resolve
    raw_path = Path(wiki_root) / "raw"
    raw_stems = set()
    if raw_path.exists():
        for f in raw_path.rglob("*.md"):
            if not f.name.startswith('.'):
                all_pages.add(f.stem)
                raw_stems.add(f.stem)

    # Second pass: track incoming links and check broken links
    incoming_links = defaultdict(set)
    for f in wiki_path.glob("**/*.md"):
        if f.name.startswith('.'):
            continue
        page_name = f.stem
        content = f.read_text(encoding='utf-8', errors='ignore')
        links = re.findall(r'\[\[([^\]]+?)(?:\|[^\]]+)?\]\]', content)
        for link in links:
            link_target = normalize_link(link.strip())
            if link_target in all_pages:
                incoming_links[link_target].add(page_name)
            else:
                issues["broken_links"].append((page_name, link.strip()))
    
    # Check orphan pages (excluding raw/ files)
    system_pages = {'索引', '日志', '待处理问题', '日志-监控列表', '概述'}
    for page in all_pages:
        if page in raw_stems:
            continue
        if page not in system_pages and len(incoming_links[page]) == 0:
            issues["orphan_pages"].append(page)
    
    # Check index completeness
    index_file = wiki_path / "索引.md"
    if index_file.exists():
        index_content = index_file.read_text(encoding='utf-8')
        indexed = set(re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]', index_content))
        missing = all_pages - indexed - system_pages - raw_stems
        issues["missing_from_index"] = list(missing)
    
    # Check frontmatter
    for f in wiki_path.glob("**/*.md"):
        if f.name.startswith('.'):
            continue
        content = f.read_text(encoding='utf-8', errors='ignore')
        if not content.startswith('---'):
            issues["missing_frontmatter"].append(f.stem)
    
    return issues

def main():
    wiki_root = sys.argv[1] if len(sys.argv) > 1 else str(Path.home() / "wiki")
    issues = check_wiki(wiki_root)
    
    print("=== Wiki Health Check ===")
    print(f"Broken links: {len(issues['broken_links'])}")
    print(f"Orphan pages: {len(issues['orphan_pages'])}")
    print(f"Missing from index: {len(issues['missing_from_index'])}")
    print(f"Missing frontmatter: {len(issues['missing_frontmatter'])}")
    
    if issues['broken_links']:
        print("\n--- Broken Links ---")
        for src, target in issues['broken_links']:
            print(f"  [[{target}]] in {src}")

    if issues['orphan_pages']:
        print("\n--- Orphan Pages ---")
        for p in sorted(issues['orphan_pages']):
            print(f"  - {p}")

if __name__ == "__main__":
    main()
