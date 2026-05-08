#!/usr/bin/env python3
"""
Convert Obsidian [[wiki-links]] to standard Markdown links for MkDocs.
Handles:
  - [[page-name]] → [page-name](page-name.md)
  - [[page-name|display text]] → [display text](page-name.md)
  - Resolves paths across wiki subdirectories
"""
import re
import os
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent / "wiki"

def build_page_index(wiki_root: Path) -> dict:
    """Build a map of page-name → relative path from wiki/."""
    index = {}
    for md_file in wiki_root.rglob("*.md"):
        rel = md_file.relative_to(wiki_root)
        name = md_file.stem  # filename without .md
        index[name] = str(rel)
        # Also index with parent dir for disambiguation
        parent = rel.parent
        if parent != Path('.'):
            index[f"{parent}/{name}"] = str(rel)
    return index

def convert_wiki_links(content: str, current_file: Path, page_index: dict, wiki_root: Path) -> str:
    """Convert [[wiki-links]] to relative markdown links."""
    current_dir = current_file.parent

    def replace_link(match):
        full = match.group(1)
        # Handle [[page|display]]
        if '|' in full:
            target, display = full.split('|', 1)
        else:
            target = full
            display = full

        target = target.strip()
        display = display.strip()

        # Skip if it looks like an image or external link
        if target.startswith(('http://', 'https://', '#', '!')):
            return match.group(0)

        # Try to resolve the target
        resolved_path = page_index.get(target)
        if resolved_path:
            # Compute relative path from current file to target
            target_path = wiki_root / resolved_path
            try:
                rel = os.path.relpath(target_path, current_dir)
            except ValueError:
                rel = resolved_path
            return f"[{display}]({rel})"
        else:
            # If not found, create a link anyway (page might be created later)
            # Try common locations
            for subdir in ['', 'sources/', 'concepts/', 'entities/', 'topics/', 'comparisons/']:
                candidate = f"{subdir}{target}.md"
                if (wiki_root / candidate).exists():
                    target_path = wiki_root / candidate
                    try:
                        rel = os.path.relpath(target_path, current_dir)
                    except ValueError:
                        rel = candidate
                    return f"[{display}]({rel})"
            # Fallback: link as-is
            return f"[{display}]({target}.md)"

    # Match [[...]] but not inside code blocks
    pattern = r'\[\[([^\]]+)\]\]'
    return re.sub(pattern, replace_link, content)

def process_wiki(wiki_root: Path, dry_run: bool = False):
    """Process all markdown files in the wiki."""
    page_index = build_page_index(wiki_root)
    print(f"Built index with {len(page_index)} pages")

    converted = 0
    for md_file in sorted(wiki_root.rglob("*.md")):
        content = md_file.read_text(encoding='utf-8')
        if '[[' not in content:
            continue

        new_content = convert_wiki_links(content, md_file, page_index, wiki_root)
        if new_content != content:
            converted += 1
            link_count = content.count('[[') 
            print(f"  [{converted}] {md_file.relative_to(wiki_root)} ({link_count} links)")
            if not dry_run:
                md_file.write_text(new_content, encoding='utf-8')

    print(f"\nConverted {converted} files")

if __name__ == '__main__':
    dry_run = '--dry-run' in sys.argv
    process_wiki(WIKI_ROOT, dry_run=dry_run)
