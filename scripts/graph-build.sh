#!/bin/bash
# Wiki Graph Builder - Generate graph data from wikilinks
set -e

WIKI_ROOT="${1:-$(dirname "$0")/..}"
WIKI_DIR="$WIKI_ROOT/wiki"
OUTPUT="$WIKI_ROOT/site/build/graph"

mkdir -p "$OUTPUT"

echo "=== Building Wiki Graph ==="

python3 -c "
import re
import json
from pathlib import Path
from collections import defaultdict

wiki_root = Path('$WIKI_DIR')
nodes = []
edges = []

# Collect all pages
page_types = {}
for f in wiki_root.glob('**/*.md'):
    if f.name.startswith('.'):
        continue
    rel = f.relative_to(wiki_root)
    category = rel.parts[0] if len(rel.parts) > 1 else 'root'
    page_types[f.stem] = category

# Build nodes and edges
for f in wiki_root.glob('**/*.md'):
    if f.name.startswith('.'):
        continue
    
    page_name = f.stem
    category = page_types.get(page_name, 'root')
    
    nodes.append({
        'id': page_name,
        'group': category,
        'size': f.stat().st_size
    })
    
    content = f.read_text(encoding='utf-8', errors='ignore')
    links = re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]', content)
    for link in links:
        link_target = link.strip()
        if link_target in page_types:
            edges.append({
                'source': page_name,
                'target': link_target
            })

graph = {'nodes': nodes, 'edges': edges}
output_path = Path('$OUTPUT/graph.json')
output_path.write_text(json.dumps(graph, indent=2, ensure_ascii=False))
print(f'Nodes: {len(nodes)}, Edges: {len(edges)}')
"

echo "✓ Graph data saved to $OUTPUT/graph.json"
