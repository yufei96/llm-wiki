#!/bin/bash
# Wiki Lint Fix - Auto-fix low-risk issues
set -e

WIKI_ROOT="${1:-$(dirname "$0")/..}"
DRY_RUN=true

if [ "$1" = "--apply" ] || [ "$2" = "--apply" ]; then
    DRY_RUN=false
fi

echo "=== Wiki Lint Fix ==="
echo "Mode: $([ "$DRY_RUN" = true ] && echo "DRY RUN" || echo "APPLY")"

# Fix broken links
echo ""
echo "--- Fixing Broken Links ---"
python3 "$WIKI_ROOT/scripts/wiki-fix-links.py" "$WIKI_ROOT" $([ "$DRY_RUN" = false ] && echo "--apply")

echo ""
echo "=== Lint Fix Complete ==="
