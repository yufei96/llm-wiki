#!/usr/bin/env python3
"""
Pre-build: Convert [[wiki-links]] to standard markdown links.
Copies wiki/ → site/content/, converts, then mkdocs builds from site/content/.
Source files are NOT modified.
"""
import re
import os
import shutil
from pathlib import Path

WIKI_SRC = Path("/root/wiki/wiki")
BUILD_CONTENT = Path("/root/wiki/site/content")

# Section index pages
SECTION_INDEXES = {
    "concepts": "概念",
    "sources": "来源",
    "entities": "实体",
    "topics": "主题",
    "comparisons": "对比",
}

def build_page_index(wiki_dir):
    """Build index: stem → relative path (without .md)"""
    index = {}
    for md_file in wiki_dir.rglob("*.md"):
        rel = md_file.relative_to(wiki_dir)
        stem = md_file.stem
        path_no_ext = str(rel.with_suffix(''))
        index[stem] = path_no_ext
        index[path_no_ext] = path_no_ext
    return index

def convert_wikilinks(content, page_rel, page_index):
    """Convert [[target]] and [[target|display]] to [display](relative_path)"""
    
    def replacer(match):
        full = match.group(1)
        if '|' in full:
            target, display = full.split('|', 1)
        else:
            target = full
            display = full
        
        target = target.strip()
        display = display.strip()
        
        # Handle [[page#section]]
        if '#' in target:
            page_part, section = target.split('#', 1)
        else:
            page_part = target
            section = None
        
        # Look up target
        target_path = page_index.get(page_part)
        if not target_path:
            target_path = page_index.get(page_part.lower())
        if not target_path:
            return f'`[[{full}]]`'  # Unresolved
        
        # Calculate relative path
        current_dir = Path(page_rel).parent
        try:
            rel = os.path.relpath(target_path, current_dir)
        except ValueError:
            rel = target_path
        
        if section:
            rel += f"#{section}"
        
        return f'[{display}]({rel})'
    
    # Only convert outside code blocks
    parts = re.split(r'(```[\s\S]*?```|`[^`]+`)', content)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 0:  # Not inside code block
            part = re.sub(r'\[\[([^\]]+)\]\]', replacer, part)
        result.append(part)
    
    return ''.join(result)

def create_section_indexes(content_dir):
    """Create index.md for each section directory"""
    for dir_name, title in SECTION_INDEXES.items():
        index_path = content_dir / dir_name / "index.md"
        if not index_path.exists():
            index_path.parent.mkdir(parents=True, exist_ok=True)
            index_path.write_text(f"---\ntitle: {title}\n---\n\n# {title}\n", encoding='utf-8')

def main():
    if BUILD_CONTENT.exists():
        shutil.rmtree(BUILD_CONTENT)
    
    shutil.copytree(WIKI_SRC, BUILD_CONTENT)
    page_index = build_page_index(BUILD_CONTENT)
    
    # Create section index pages
    create_section_indexes(BUILD_CONTENT)
    
    converted = 0
    unresolved = 0
    for md_file in BUILD_CONTENT.rglob("*.md"):
        content = md_file.read_text('utf-8')
        rel = str(md_file.relative_to(BUILD_CONTENT))
        new_content = convert_wikilinks(content, rel, page_index)
        
        if new_content != content:
            old = len(re.findall(r'\[\[[^\]]+\]\]', content))
            new = len(re.findall(r'\[\[[^\]]+\]\]', new_content))
            converted += (old - new)
            unresolved += new
            md_file.write_text(new_content, 'utf-8')
    
    print(f"✓ {converted} wikilinks converted, {unresolved} unresolved")

if __name__ == "__main__":
    main()
