#!/bin/bash
# Wiki Graph HTML - Generate interactive visualization
set -e

WIKI_ROOT="${1:-$(dirname "$0")/..}"
OUTPUT="$WIKI_ROOT/site/build/graph"

# Build graph data first
bash "$WIKI_ROOT/scripts/graph-build.sh" "$WIKI_ROOT"

echo "=== Generating Graph HTML ==="

cat > "$OUTPUT/index.html" << 'HTMLEOF'
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Wiki Knowledge Graph</title>
<style>
body { margin: 0; background: #1a1a2e; color: #eee; font-family: sans-serif; }
#graph { width: 100vw; height: 100vh; }
.node circle { stroke: #fff; stroke-width: 1.5px; }
.node text { font-size: 10px; fill: #eee; }
.link { stroke: #555; stroke-opacity: 0.6; }
</style>
</head>
<body>
<div id="graph"></div>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
fetch('graph.json').then(r=>r.json()).then(data=>{
const width=window.innerWidth,height=window.innerHeight;
const svg=d3.select('#graph').append('svg').attr('width',width).attr('height',height);
const color=d3.scaleOrdinal(['#e6194b','#3cb44b','#4363d8','#f58231','#911eb4','#42d4f4','#f032e6','#bfef45']);
const sim=d3.forceSimulation(data.nodes)
.force('link',d3.forceLink(data.edges).id(d=>d.id).distance(50))
.force('charge',d3.forceManyBody().strength(-100))
.force('center',d3.forceCenter(width/2,height/2));
const link=svg.append('g').selectAll('line').data(data.edges).join('line').attr('class','link');
const node=svg.append('g').selectAll('g').data(data.nodes).join('g').attr('class','node');
node.append('circle').attr('r',5).attr('fill',d=>color(d.group));
node.append('text').text(d=>d.id).attr('x',8).attr('y',3);
sim.on('tick',()=>{link.attr('x1',d=>d.source.x).attr('y1',d=>d.source.y).attr('x2',d=>d.target.x).attr('y2',d=>d.target.y);node.attr('transform',d=>`translate(${d.x},${d.y})`);});
});
</script>
</body>
</html>
HTMLEOF

echo "✓ Graph HTML saved to $OUTPUT/index.html"
