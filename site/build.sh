#!/bin/bash
# Cloudflare Pages 构建脚本
set -e

cd /root/wiki

# 0. 硬约束：首页必须是概述.md（防回退）
HOMEPAGE=$(grep -oP '^\s*-\s*首页:\s*\K\S+' site/mkdocs.yml)
if [ "$HOMEPAGE" != "概述.md" ]; then
    echo "❌ mkdocs.yml 首页错误: '$HOMEPAGE'，必须是 '概述.md'"
    echo "   修复: 将 nav 第一项的 '首页' 改回 '概述.md'"
    exit 1
fi

# 1. 转换 [[wikilinks]]（不修改源文件）
python site/convert-wikilinks.py

# 2. 构建 MkDocs 网站
mkdocs build -f mkdocs.yml

# 3. 根路径重定向 → 概述/（mkdocs 不会为 概述.md 生成根 index.html）
cat > site/build/index.html << 'HTMLEOF'
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="refresh" content="0; url=/概述/">
<title>MOSA 知识库</title>
</head>
<body>
<p>正在跳转到 <a href="/概述/">MOSA 知识库首页</a>...</p>
</body>
</html>
HTMLEOF

echo "✓ Build complete. Output in site/build"
