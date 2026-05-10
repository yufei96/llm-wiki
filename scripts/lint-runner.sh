#!/bin/bash
# Wiki Lint Runner - Comprehensive health check
set -e

WIKI_ROOT="${1:-$(dirname "$0")/..}"
WIKI_DIR="$WIKI_ROOT/wiki"

echo "=== Wiki Lint Runner ==="
echo "Root: $WIKI_ROOT"

# 1. Health check
echo ""
echo "--- Phase 1: Health Check ---"
python3 "$WIKI_ROOT/scripts/wiki-health-check.py" "$WIKI_ROOT"

# 2. Raw file integrity
echo ""
echo "--- Phase 2: Raw File Integrity ---"
PAPERS_DIR="$WIKI_ROOT/raw/papers"
ARTICLES_DIR="$WIKI_ROOT/raw/articles"

if [ -d "$PAPERS_DIR" ] && [ -d "$ARTICLES_DIR" ]; then
    PAPER_COUNT=$(ls "$PAPERS_DIR"/*.pdf 2>/dev/null | wc -l)
    ARTICLE_COUNT=$(ls "$ARTICLES_DIR"/*.md 2>/dev/null | wc -l)
    echo "Papers: $PAPER_COUNT PDFs"
    echo "Articles: $ARTICLE_COUNT MDs"
    
    # Check for PDFs without articles
    NO_ARTICLE=0
    for pdf in "$PAPERS_DIR"/*.pdf; do
        base=$(basename "$pdf" .pdf)
        if [ ! -f "$ARTICLES_DIR/$base.md" ]; then
            NO_ARTICLE=$((NO_ARTICLE + 1))
        fi
    done
    echo "PDFs without articles: $NO_ARTICLE"
fi

# 3. Frontmatter check
echo ""
echo "--- Phase 3: Frontmatter Check ---"
NO_FM=0
for f in "$WIKI_DIR"/**/*.md; do
    if head -1 "$f" | grep -qv "^---"; then
        NO_FM=$((NO_FM + 1))
    fi
done
echo "Pages without frontmatter: $NO_FM"

# 4. Large pages
echo ""
echo "--- Phase 4: Large Pages (>200 lines) ---"
LARGE=0
for f in "$WIKI_DIR"/**/*.md; do
    lines=$(wc -l < "$f")
    if [ "$lines" -gt 200 ]; then
        echo "  $(basename "$f"): $lines lines"
        LARGE=$((LARGE + 1))
    fi
done
echo "Large pages: $LARGE"

echo ""
echo "=== Lint Complete ==="
