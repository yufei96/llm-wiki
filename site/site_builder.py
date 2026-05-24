#!/usr/bin/env python3
"""Build MkDocs site from Obsidian wiki — orchestrator.

Responsibilities:
1. YAML integrity pre-check
2. Copy wiki/ → site/content/
3. Generate section index pages (tag-grouped)
4. Convert [[wikilinks]] to markdown links
5. Auto-generate mkdocs nav
6. Run mkdocs build
7. Symlink raw/ files into build output
"""
from __future__ import annotations
import os
import re
import shutil
import subprocess
import sys

import yaml
from pathlib import Path

# Import sibling modules (works when run as `python3 site/site_builder.py` from wiki root)
import importlib.util
spec_dc = importlib.util.spec_from_file_location("doc_config", Path(__file__).parent / "doc_config.py")
doc_config = importlib.util.module_from_spec(spec_dc)
spec_lc = importlib.util.spec_from_file_location("link_converter", Path(__file__).parent / "link_converter.py")
link_converter = importlib.util.module_from_spec(spec_lc)
spec_dc.loader.exec_module(doc_config)
spec_lc.loader.exec_module(link_converter)

generate_section_indexes = doc_config.generate_section_indexes
generate_nav = doc_config.generate_nav
_SECTION_CFG = doc_config._SECTION_CFG
build_page_index = link_converter.build_page_index
convert_wiki_links = link_converter.convert_wiki_links
quote_path = link_converter.quote_path

ROOT = Path(__file__).parent.parent
WIKI_SRC = ROOT / "wiki"
BUILD_DIR = ROOT / "site" / "content"
SITE_OUT = ROOT / "site" / "build"
MKDOCS_YML = ROOT / "mkdocs.yml"
MKDOCS_BUILD_YML = ROOT / "site" / "mkdocs.yml"
SECTIONS = ['topics', 'concepts', 'comparisons', 'entities', 'sources']


def main():
    # ── YAML integrity pre-check (fail early) ──
    yaml_check = subprocess.run(
        [sys.executable, str(ROOT / "site" / "check-yaml.py")],
        capture_output=True, text=True
    )
    if yaml_check.returncode != 0:
        print("YAML INTEGRITY CHECK FAILED:")
        print(yaml_check.stdout)
        print(yaml_check.stderr)
        sys.exit(1)
    print("YAML integrity check: OK")

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

    # Use overview.md as homepage
    overview = BUILD_DIR / "概述.md"
    if not overview.exists():
        overview = BUILD_DIR / "overview.md"
    if overview.exists():
        shutil.copy2(overview, BUILD_DIR / "index.md")
        print("Copied overview.md → index.md (homepage)")

    # Build index and convert
    page_index = build_page_index(BUILD_DIR)

    # Also index raw/ files
    RAW_SRC = ROOT / "raw"
    if RAW_SRC.exists():
        raw_files = 0
        for md_file in RAW_SRC.rglob("*.md"):
            rel = f"raw/{md_file.relative_to(RAW_SRC)}"
            name = md_file.stem
            page_index[name] = rel
            parent = md_file.relative_to(RAW_SRC).parent
            if parent != Path('.'):
                page_index[f"{parent.as_posix()}/{name}"] = rel
            page_index[f"raw/{md_file.relative_to(RAW_SRC).with_suffix('')}"] = rel
            raw_files += 1
        print(f"Indexed {raw_files} raw/ files")
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

    # ── Health check: run wiki-health-check on source ──
    print("\nRunning health check...")
    health_check = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "wiki-health-check.py"), str(ROOT)],
        capture_output=True, text=True
    )
    print(health_check.stdout.strip())
    if health_check.returncode != 0:
        print(health_check.stderr.strip())

    # Strip .md from regular markdown links (MkDocs compatibility)
    md_stripped = 0
    for md_file in BUILD_DIR.rglob("*.md"):
        orig = md_file.read_text(encoding='utf-8')
        new = orig
        for m in re.finditer(r'\[([^\]]+)\]\(([^)]+\.md)\)', orig):
            path = m.group(2)[:-3]
            if (BUILD_DIR / path).with_suffix('.md').exists():
                new = new.replace(m.group(0), f'[{m.group(1)}]({path})')
                md_stripped += 1
        if new != orig:
            md_file.write_text(new, encoding='utf-8')
    if md_stripped:
        print(f"Stripped .md from {md_stripped} regular markdown links")

    # URL-encode Chinese paths
    encoded_links = 0
    for md_file in BUILD_DIR.rglob("*.md"):
        orig = md_file.read_text(encoding='utf-8')
        new = re.sub(
            r'(\[[^\]]*\]\()([^)]*[\u4e00-\u9fff][^)]*)(\))',
            lambda m: m.group(1) + quote_path(m.group(2)) + m.group(3),
            orig
        )
        if new != orig:
            md_file.write_text(new, encoding='utf-8')
            encoded_links += 1
    if encoded_links:
        print(f"URL-encoded Chinese paths in {encoded_links} files")

    # ── Auto-generate nav from filesystem ──
    nav = generate_nav(BUILD_DIR, _SECTION_CFG)
    print(f"Generated nav: {len(nav)} sections")

    # Build mkdocs.yml for build (paths relative to site/ cwd)
    mkdocs_content = MKDOCS_YML.read_text(encoding='utf-8')
    mkdocs_content = mkdocs_content.replace('docs_dir: site/content', 'docs_dir: content')
    mkdocs_content = mkdocs_content.replace('site_dir: site/build', 'site_dir: build')

    config = yaml.safe_load(mkdocs_content)
    config['nav'] = nav
    mkdocs_content = yaml.dump(config, allow_unicode=True, default_flow_style=False, sort_keys=False)

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

    # Symlink individual raw/ .md files
    raw_link_root = SITE_OUT / "raw"
    if RAW_SRC.exists():
        if raw_link_root.exists() or raw_link_root.is_symlink():
            if raw_link_root.is_symlink():
                raw_link_root.unlink()
            else:
                shutil.rmtree(raw_link_root)
        raw_linked = 0
        for md_file in RAW_SRC.rglob("*.md"):
            dst = raw_link_root / md_file.relative_to(RAW_SRC)
            dst.parent.mkdir(parents=True, exist_ok=True)
            if not dst.exists():
                dst.symlink_to(os.path.relpath(md_file, dst.parent))
                raw_linked += 1
        print(f"  Symlinked {raw_linked} raw/*.md files to build output")

    # Count output
    if SITE_OUT.exists():
        file_count = sum(1 for _ in SITE_OUT.rglob("*") if _.is_file())
        size_mb = sum(f.stat().st_size for f in SITE_OUT.rglob("*") if f.is_file()) / 1024 / 1024
        print(f"✓ Site built: {SITE_OUT}")
        print(f"  {file_count} files, {size_mb:.1f} MB")
    else:
        print("ERROR: Build directory not created")
        sys.exit(1)


if __name__ == '__main__':
    main()
