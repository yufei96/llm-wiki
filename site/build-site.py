#!/usr/bin/env python3
"""
Build MkDocs site from Obsidian wiki.
1. Copy wiki/ to site/content/
2. Convert [[wiki-links]] to standard markdown
3. Run mkdocs build
"""
import shutil
import re
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI_SRC = ROOT / "wiki"
BUILD_DIR = ROOT / "site" / "content"
SITE_OUT = ROOT / "site" / "build"
MKDOCS_YML = ROOT / "mkdocs.yml"
MKDOCS_BUILD_YML = ROOT / "site" / "mkdocs.yml"

def build_page_index(wiki_root: Path) -> dict:
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

        if target.startswith(('http://', 'https://', '#', '!')):
            return match.group(0)

        resolved_path = page_index.get(target)
        if not resolved_path:
            # Try partial matches
            for subdir in ['sources', 'concepts', 'entities', 'topics', 'comparisons']:
                key = f"{subdir}/{target}"
                if key in page_index:
                    resolved_path = page_index[key]
                    break

        if resolved_path:
            target_path = wiki_root / resolved_path
            try:
                rel = os.path.relpath(target_path, current_dir)
            except ValueError:
                rel = resolved_path
            return f"[{display}]({rel})"
        else:
            return f"[{display}]({target}.md)"

    pattern = r'\[\[([^\]]+)\]\]'
    return re.sub(pattern, replace_link, content)

def extract_title(md_file: Path) -> str:
    """Extract title from YAML frontmatter or first heading."""
    try:
        content = md_file.read_text(encoding='utf-8')
    except Exception:
        return md_file.stem

    # Try YAML frontmatter
    fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm_match.group(1), re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()

    # Try first heading
    heading_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    if heading_match:
        return heading_match.group(1).strip()

    return md_file.stem


def generate_section_indexes(content_dir: Path):
    """Auto-generate index.md for each section directory."""
    sections = ['topics', 'concepts', 'comparisons', 'entities', 'sources']
    section_titles = {
        'topics': '主题',
        'concepts': '概念',
        'comparisons': '对比',
        'entities': '实体',
        'sources': '来源',
    }
    section_descs = {
        'topics': '综合多来源的主题深度文章',
        'concepts': '独立概念释义',
        'comparisons': '跨领域对比分析',
        'entities': '人物、组织与政策实体',
        'sources': '原始来源摘要与引用',
    }

    for section in sections:
        section_dir = content_dir / section
        if not section_dir.is_dir():
            continue

        # Collect articles (exclude index.md itself)
        articles = []
        for md_file in sorted(section_dir.glob("*.md")):
            if md_file.name == "index.md":
                continue
            title = extract_title(md_file)
            articles.append((md_file.stem, title))

        if not articles:
            continue

        # Generate index.md
        title = section_titles.get(section, section.title())
        desc = section_descs.get(section, '')
        lines = [
            f'---',
            f'title: "{title}"',
            f'---',
            f'',
            f'# {title}',
            f'',
        ]
        if desc:
            lines.append(f'> {desc}')
            lines.append(f'')

        for stem, article_title in articles:
            lines.append(f'- [{article_title}]({stem}.md)')

        index_path = section_dir / "index.md"
        index_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
        print(f"  Generated {section}/index.md ({len(articles)} articles)")


def main():
    # Clean
    for d in [BUILD_DIR, SITE_OUT]:
        if d.exists():
            shutil.rmtree(d)

    # Copy wiki → content
    shutil.copytree(WIKI_SRC, BUILD_DIR)
    print(f"Copied wiki/ → site/content/")

    # Generate section index pages
    print("Generating section indexes...")
    generate_section_indexes(BUILD_DIR)

    # Build index and convert
    page_index = build_page_index(BUILD_DIR)
    print(f"Index: {len(page_index)} pages")

    converted = 0
    total_links = 0
    unresolved = []

    for md_file in sorted(BUILD_DIR.rglob("*.md")):
        content = md_file.read_text(encoding='utf-8')
        if '[[' not in content:
            continue

        link_count = content.count('[[')
        new_content = convert_wiki_links(content, md_file, page_index, BUILD_DIR)

        # Track unresolved links
        remaining = re.findall(r'\[\[([^\]]+)\]\]', new_content)
        for r in remaining:
            unresolved.append((md_file.relative_to(BUILD_DIR), r))

        if new_content != content:
            converted += 1
            total_links += link_count
            md_file.write_text(new_content, encoding='utf-8')

    print(f"Converted {converted} files, {total_links} links")
    if unresolved:
        print(f"Unresolved: {len(unresolved)} links (will be plain links)")

    # Create mkdocs.yml for build (paths relative to site/ cwd)
    mkdocs_content = MKDOCS_YML.read_text(encoding='utf-8')
    mkdocs_content = mkdocs_content.replace('docs_dir: site/content', 'docs_dir: content')
    mkdocs_content = mkdocs_content.replace('site_dir: site/build', 'site_dir: build')
    MKDOCS_BUILD_YML.write_text(mkdocs_content, encoding='utf-8')

    # Build
    print("\nBuilding MkDocs site...")
    result = subprocess.run(
        ["mkdocs", "build", "-f", str(MKDOCS_BUILD_YML)],
        capture_output=True, text=True, cwd=str(ROOT / "site")
    )

    if result.returncode != 0:
        print("BUILD FAILED:")
        print(result.stderr[-2000:] if len(result.stderr) > 2000 else result.stderr)
        sys.exit(1)

    # Copy static root files (e.g. WeChat verification) to build output
    for f in ROOT.glob("*.txt"):
        if f.name.startswith(".") or f.name == "requirements.txt":
            continue
        shutil.copy2(f, SITE_OUT / f.name)
        print(f"  Copied root file: {f.name}")

    # Count output
    if SITE_OUT.exists():
        file_count = sum(1 for _ in SITE_OUT.rglob("*") if _.is_file())
        size_mb = sum(f.stat().st_size for f in SITE_OUT.rglob("*") if _.is_file()) / 1024 / 1024
        print(f"✓ Site built: {SITE_OUT}")
        print(f"  {file_count} files, {size_mb:.1f} MB")
    else:
        print("ERROR: Build directory not created")
        sys.exit(1)

if __name__ == '__main__':
    main()
