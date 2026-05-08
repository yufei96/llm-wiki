#!/bin/bash
# Cloudflare Pages 构建脚本
set -e

cd /root/wiki

# 1. 转换 [[wikilinks]]（不修改源文件）
python site/convert-wikilinks.py

# 2. 构建 MkDocs 网站
mkdocs build -f mkdocs.yml

echo "✓ Build complete. Output in site/build"
