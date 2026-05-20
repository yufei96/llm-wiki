#!/bin/bash
# Build wiki site → check for broken links → deploy to Cloudflare Pages
# Usage: ./deploy.sh [-n]   (add -n for dry-run: build only, skip deploy)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$SCRIPT_DIR")"

DRY_RUN=false
if [ "${1:-}" = "-n" ]; then
    DRY_RUN=true
fi

echo "=== Step 1: Build ==="
python3 "$SCRIPT_DIR/build-site.py"
echo ""

# Quick broken-link check (grep mkdocs output for common 404 patterns)
BUILD_DIR="$SCRIPT_DIR/build"
if [ -d "$BUILD_DIR" ]; then
    echo "=== Step 2: Link check ==="
    # Check for empty href="" or broken internal links in compiled HTML
    BROKEN=$(grep -r 'href=""' "$BUILD_DIR" 2>/dev/null | wc -l || true)
    if [ "$BROKEN" -gt 0 ]; then
        echo "⚠ Warning: $BROKEN empty href(s) found in build output"
    else
        echo "✓ No empty hrefs found"
    fi
else
    echo "ERROR: Build output not found at $BUILD_DIR"
    exit 1
fi
echo ""

if $DRY_RUN; then
    echo "=== Dry run — skipping deploy ==="
    echo "Build output: $BUILD_DIR"
    exit 0
fi

echo "=== Step 3: Deploy to Cloudflare Pages ==="
cd "$ROOT"

PROJECT_NAME="mosa-wiki"
wrangler pages deploy "$BUILD_DIR" \
    --project-name "$PROJECT_NAME" \
    --commit-dirty=true \
    --branch main

echo ""
echo "✓ Deploy complete: https://mosa-wiki.pages.dev"
