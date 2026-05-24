#!/usr/bin/env python3
"""Verify all raw/ references in wiki/ source/topic/entity pages resolve to actual files.

Usage:
  python3 scripts/verify-refs.py            # check wiki/ → raw/ references
  python3 scripts/verify-refs.py --release   # also check release asset names match
"""

import os
import re
import sys
import argparse
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = WIKI_ROOT / "wiki"
RAW_ARTICLES = WIKI_ROOT / "raw" / "articles"
RAW_PAPERS = WIKI_ROOT / "raw" / "papers"

parser = argparse.ArgumentParser()
parser.add_argument("--release", action="store_true", help="Also check Release asset alignment")
args = parser.parse_args()

all_articles = set(os.listdir(RAW_ARTICLES)) if RAW_ARTICLES.exists() else set()
all_papers = set(os.listdir(RAW_PAPERS)) if RAW_PAPERS.exists() else set()

broken_articles = []
broken_papers = []

for section in ["sources", "topics", "entities", "concepts"]:
    section_dir = WIKI_DIR / section
    if not section_dir.exists():
        continue
    for fn in sorted(os.listdir(section_dir)):
        if not fn.endswith(".md"):
            continue
        path = section_dir / fn
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract raw/articles/xxx and raw/papers/xxx references
        for m in re.finditer(r"raw/(articles|papers)/([^\s\)\]\"\'\]\[,]+)", content):
            ref_type = m.group(1)
            ref = m.group(2).rstrip("`").rstrip("\u3002").rstrip("\uff0c").rstrip("\uff09")
            target = all_articles if ref_type == "articles" else all_papers

            if ref not in target:
                # Try prefix match (filenames with spaces)
                matched = [t for t in target if t.startswith(ref + " ") or t.startswith(ref + ".")]
                if not matched:
                    (broken_articles if ref_type == "articles" else broken_papers).append(
                        (section, fn, ref, ref_type)
                    )

exit_code = 0

if broken_articles or broken_papers:
    print("✗ Broken references found:")
    for section, fn, ref, rtype in sorted(broken_articles + broken_papers):
        print(f"  {section}/{fn}: raw/{rtype}/{ref}")
    exit_code = 1
else:
    print(f"✓ All references valid (scanned {section}: {len(all_articles)} articles, {len(all_papers)} papers)")

if args.release:
    # Check that all papers have a mapping in release-map.tsv
    map_path = WIKI_ROOT / "raw" / "release-map.tsv"
    if not map_path.exists():
        print("✗ raw/release-map.tsv not found — run release alignment first")
        exit_code = 1
    else:
        mapped = set()
        for line in map_path.read_text(encoding='utf-8').strip().split('\n')[1:]:
            parts = line.split('\t')
            if len(parts) == 2:
                mapped.add(parts[0])
        unmapped = sorted(f for f in os.listdir(RAW_PAPERS) if f not in mapped and f.endswith('.pdf'))
        if unmapped:
            print(f"✗ Unmapped papers in Release: {len(unmapped)}")
            for f in unmapped[:10]:
                print(f"  {f}")
            exit_code = 1
        else:
            print(f"✓ All {len(mapped)} papers mapped in raw/release-map.tsv")

sys.exit(exit_code)
