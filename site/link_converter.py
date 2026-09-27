"""Wiki link converter — build page index, convert [[wikilinks]] to markdown links."""
from __future__ import annotations

import os
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote


def quote_path(path: str) -> str:
    """URL-encode non-ASCII characters in a path, preserving / separators."""
    parts = path.split('/')
    return '/'.join(quote(p, safe='') for p in parts)


def build_page_index(wiki_root: Path, raw_root: Path | None = None) -> dict:
    """Index full paths and unique names; wiki names take precedence over raw names."""
    index = {}
    for prefix, root in [('', wiki_root), ('raw/', raw_root)]:
        if root is None:
            continue
        names = defaultdict(list)
        for md_file in sorted(root.rglob('*.md')):
            if md_file.name.startswith('.'):
                continue
            rel = md_file.relative_to(root)
            path = prefix + rel.as_posix()
            key = rel.with_suffix('').as_posix()
            index[prefix + key] = path
            if prefix:
                index.setdefault(key, path)
            names[md_file.stem].append(path)
        for name, paths in names.items():
            index.setdefault(name, paths[0] if len(paths) == 1 else None)
    return index


def normalize_link(target: str) -> str:
    """Normalize a local page target without discarding its directory or version dots."""
    target = target.strip()
    if target.startswith(('http://', 'https://', '#', '!')):
        return ''
    if target.endswith('.md'):
        target = target[:-3]
    if target.startswith('wiki/'):
        target = target[5:]
    return target


def resolve_link(target: str, page_index: dict) -> str | None:
    return page_index.get(normalize_link(target))


def convert_wiki_links(content: str, current_file: Path, page_index: dict, wiki_root: Path,
                       unresolved: list[str] | None = None) -> str:
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
        if not normalize_link(target):
            return match.group(0)
        resolved_path = resolve_link(target, page_index)

        if resolved_path:
            # Make relative to current file
            try:
                rel_path = Path(os.path.relpath(
                    (wiki_root / resolved_path).resolve(),
                    current_dir.resolve()
                ))
            except (ValueError, OSError):
                rel_path = Path(resolved_path)
            link_path = rel_path.as_posix()
            return f"[{display}]({link_path})"
        # Unresolved → plain text (preserve display name)
        if unresolved is not None:
            unresolved.append(target)
        return display

    return re.sub(r'\[\[([^\]]+)\]\]', replace_link, content)
