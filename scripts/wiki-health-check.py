#!/usr/bin/env python3
"""Wiki Health Check Script - Checks for broken links, orphans, index gaps."""

import re
import sys
from pathlib import Path
from collections import defaultdict

def check_wiki(wiki_root):
    wiki_path = Path(wiki_root) / "wiki"
    issues = {
        "broken_links": [],
        "orphan_pages": [],
        "missing_from_index": [],
        "missing_frontmatter": [],
    }
    
    # Collect all pages
    all_pages = set()
    incoming_links = defaultdict(set)
    
    for f in wiki_path.glob("**/*.md"):
        if f.name.startswith('.'):
            continue
        page_name = f.stem
        all_pages.add(page_name)
        
        content = f.read_text(encoding='utf-8', errors='ignore')
        links = re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]', content)
        for link in links:
            link_target = link.strip()
            if link_target in all_pages:
                incoming_links[link_target].add(page_name)
    
    # Check broken links
    for f in wiki_path.glob("**/*.md"):
        if f.name.startswith('.'):
            continue
        content = f.read_text(encoding='utf-8', errors='ignore')
        links = re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]', content)
        for link in links:
            if link.strip() not in all_pages:
                issues["broken_links"].append((f.stem, link.strip()))
    
    # Check orphan pages
    system_pages = {'索引', '日志', '待处理问题', '日志-监控列表', '概述'}
    for page in all_pages:
        if page not in system_pages and len(incoming_links[page]) == 0:
            issues["orphan_pages"].append(page)
    
    # Check index completeness
    index_file = wiki_path / "索引.md"
    if index_file.exists():
        index_content = index_file.read_text(encoding='utf-8')
        indexed = set(re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]', index_content))
        missing = all_pages - indexed - system_pages
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
        for src, target in issues['broken_links'][:10]:
            print(f"  [[{target}]] in {src}")
    
    if issues['orphan_pages']:
        print("\n--- Orphan Pages ---")
        for p in sorted(issues['orphan_pages'])[:10]:
            print(f"  - {p}")

if __name__ == "__main__":
    main()
