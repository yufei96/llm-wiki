#!/usr/bin/env python3
"""Wiki Link Fix Script - Fixes broken wikilinks."""

import re
import sys
from pathlib import Path

def fix_links(wiki_root, apply=False):
    wiki_path = Path(wiki_root) / "wiki"
    
    # Build page name mapping
    all_pages = set()
    for f in wiki_path.glob("**/*.md"):
        if not f.name.startswith('.'):
            all_pages.add(f.stem)
    
    # Define common fixes
    fixes = {
        "NASA手册7009A-有限元分析": "NASA手册7009A",
        "国防部指令5000.81": "DODI 5000.81紧急能力",
        "Defense News-开放标准报道2024": "防务新闻-开放标准2024",
        "国防部指令5000.75": "DODI 5000.75-业务系统",
        "国防部指令5000.74": "DODI 5000.74-服务",
        "国防部指令5000.87": "DODI 5000.87软件采办",
        "军事嵌入式-海军OSMP 2025": "军事嵌入-海军OSMP 2025",
        "PPI需求质量指标": "PPI需求质量度量",
    }
    
    fixed = 0
    for f in wiki_path.glob("**/*.md"):
        if f.name.startswith('.'):
            continue
        
        content = f.read_text(encoding='utf-8', errors='ignore')
        original = content
        
        for old, new in fixes.items():
            content = re.sub(
                rf'\[\[{re.escape(old)}\]\]',
                f'[[{new}]]',
                content
            )
        
        if content != original:
            if apply:
                f.write_text(content, encoding='utf-8')
            fixed += 1
    
    return fixed

def main():
    wiki_root = sys.argv[1] if len(sys.argv) > 1 else str(Path.home() / "wiki")
    apply = "--apply" in sys.argv
    
    fixed = fix_links(wiki_root, apply)
    mode = "Applied" if apply else "Found"
    print(f"{mode} {fixed} link fixes")

if __name__ == "__main__":
    main()
