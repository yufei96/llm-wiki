"""Wiki link converter — build page index, convert [[wikilinks]] to markdown links."""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import quote


def quote_path(path: str) -> str:
    """URL-encode non-ASCII characters in a path, preserving / separators."""
    parts = path.split('/')
    return '/'.join(quote(p, safe='') for p in parts)


def build_page_index(wiki_root: Path) -> dict:
    """Build {name: path} index for all .md files."""
    index = {}
    for md_file in wiki_root.rglob("*.md"):
        rel = md_file.relative_to(wiki_root)
        name = md_file.stem
        index[name] = str(rel)
        parent = rel.parent
        if parent != Path('.'):
            index[f"{parent.name}/{name}"] = str(rel)
    return index


def convert_wiki_links(content: str, current_file: Path, page_index: dict, wiki_root: Path) -> str:
    """Convert [[wiki-link]] syntax to standard markdown links.

    Falls back to plain text for unresolvable links.
    """
    current_dir = current_file.parent

    def replace_link(match):
        full = match.group(1)
        if '|' in full:
            target, display = full.split('|', 1)
        else:
            target = full
            display = full

        target = target.strip()
        display = display.strip()
        # Strip .md extension for lookup
        lookup_target = target[:-3] if target.endswith('.md') else target
        # Strip wiki/ prefix (Obsidian cross-vault links)
        if lookup_target.startswith('wiki/'):
            lookup_target = lookup_target[5:]

        if target.startswith(('http://', 'https://', '#', '!')):
            return match.group(0)
        resolved_path = page_index.get(lookup_target)
        if not resolved_path:
            # Try partial matches
            for subdir in ['sources', 'concepts', 'entities', 'topics', 'comparisons',
                           'raw/articles', 'raw/papers', 'raw/archive-2026-05-17', 'raw/repo']:
                key = f"{subdir}/{lookup_target}"
                if key in page_index:
                    resolved_path = page_index[key]
                    break

        if resolved_path:
            # Make relative to current file
            try:
                rel_path = Path(os.path.relpath(
                    (wiki_root / resolved_path).resolve(),
                    current_dir.resolve()
                ))
            except (ValueError, OSError):
                rel_path = Path(resolved_path)
            link_path = str(rel_path)
            return f"[{display}]({link_path})"
        # Unresolved → plain text (preserve display name)
        return display

    import os  # imported here to avoid top-level collision with pathlib
    return re.sub(r'\[\[([^\]]+)\]\]', replace_link, content)
