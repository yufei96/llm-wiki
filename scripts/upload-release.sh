#!/bin/bash
# Upload all PDFs to draft release with English names, then publish
set -e
cd "$(dirname "$0")/.."

RELEASE_ID=$(cat /tmp/rvid.txt)
MAP="raw/release-map.tsv"
PAPERS_DIR="raw/papers"
UPLOAD_URL="https://uploads.github.com/repos/yufei96/llm-wiki/releases/$RELEASE_ID/assets"
export GH_TOKEN="$(grep -A1 "oauth_token" ~/.config/gh/hosts.yml | grep "token:" | head -1 | awk '{print $2}')"

# Step 1: Copy PDFs to temp dir with English names
TMPDIR=$(mktemp -d)
echo "Temp dir: $TMPDIR"
total=$(tail -n +2 "$MAP" | wc -l)
count=0

tail -n +2 "$MAP" | while IFS=$'\t' read -r cn en; do
  src="$PAPERS_DIR/$cn"
  if [ ! -f "$src" ]; then
    echo "SKIP: $cn"
    continue
  fi
  cp "$src" "$TMPDIR/$en"
  count=$((count + 1))
  if [ $((count % 20)) -eq 0 ]; then
    echo "  Copied $count/$total"
  fi
done
echo "All $count PDFs copied to $TMPDIR"

# Step 2: Upload each English-named file via curl directly (gh CLI is unreliable)
count=0
for f in "$TMPDIR"/*.pdf; do
  en_name=$(basename "$f")
  size=$(stat -c%s "$f" 2>/dev/null || stat -f%z "$f" 2>/dev/null)
  
  # URL-encode the filename for the API
  encoded=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$en_name', safe=''))")
  
  result=$(curl -s -X POST \
    -H "Authorization: token $GH_TOKEN" \
    -H "Content-Type: application/pdf" \
    --data-binary "@$f" \
    "${UPLOAD_URL}?name=${encoded}" 2>/dev/null)
  
  name=$(echo "$result" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('name','FAIL'))" 2>/dev/null)
  count=$((count + 1))
  
  if [ "$name" = "$en_name" ]; then
    printf "\r  [%3d/%d] ✅ %s (%dKB)" "$count" "$total" "$en_name" "$((size/1024))"
  else
    printf "\r  [%3d/%d] ❌ %s -> %s" "$count" "$total" "$en_name" "$name"
  fi
done

echo ""
echo "=== Upload done: $count/$total ==="

# Step 3: Publish
curl -s -X PATCH \
  -H "Authorization: token $GH_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  "https://api.github.com/repos/yufei96/llm-wiki/releases/$RELEASE_ID" \
  -d '{"draft":false}' > /dev/null
echo "Release published!"

# Cleanup
rm -rf "$TMPDIR"
echo "Done"
