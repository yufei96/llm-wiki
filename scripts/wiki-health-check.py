#!/usr/bin/env python3
"""Wiki Health Check Script - Checks for broken links, orphans, index gaps."""

import re
import importlib.util
import sys
from pathlib import Path
from collections import defaultdict

spec = importlib.util.spec_from_file_location(
    'link_converter', Path(__file__).resolve().parent.parent / 'site' / 'link_converter.py'
)
link_converter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(link_converter)

def check_wiki(wiki_root):
    wiki_path = Path(wiki_root) / "wiki"
    issues = {
        "broken_links": [],
        "orphan_pages": [],
        "missing_from_index": [],
        "missing_frontmatter": [],
    }
    
    # Collect all pages (separate pass so incoming_links works correctly)
    pages = sorted(f for f in wiki_path.rglob('*.md') if not f.name.startswith('.'))
    all_pages = {f.relative_to(wiki_path).as_posix() for f in pages}
    page_index = link_converter.build_page_index(wiki_path, Path(wiki_root) / 'raw')

    # Second pass: track incoming links and check broken links
    incoming_links = defaultdict(set)
    for f in pages:
        page_name = f.relative_to(wiki_path).as_posix()
        content = f.read_text(encoding='utf-8', errors='ignore')
        links = re.findall(r'\[\[([^\]]+?)(?:\|[^\]]+)?\]\]', content)
        for link in links:
            if not link_converter.normalize_link(link):
                continue
            link_target = link_converter.resolve_link(link, page_index)
            if link_target is not None:
                incoming_links[link_target].add(page_name)
            else:
                issues["broken_links"].append((page_name, link.strip()))
    
    # Check orphan pages (excluding raw/ files)
    system_pages = {'索引.md', '日志.md', '待处理问题.md', '日志-监控列表.md', '概述.md'}
    for page in sorted(all_pages):
        if page not in system_pages and len(incoming_links[page]) == 0:
            issues["orphan_pages"].append(page)
    
    # Check index completeness
    index_file = wiki_path / "索引.md"
    if index_file.exists():
        index_content = index_file.read_text(encoding='utf-8')
        indexed = {
            link_converter.resolve_link(target, page_index)
            for target in re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]', index_content)
        }
        issues["missing_from_index"] = sorted(all_pages - indexed - system_pages)
    
    # Check frontmatter
    for f in pages:
        content = f.read_text(encoding='utf-8', errors='ignore')
        if not content.startswith('---'):
            issues["missing_frontmatter"].append(f.relative_to(wiki_path).as_posix())
    
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
