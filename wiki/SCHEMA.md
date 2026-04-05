# Wiki Schema

## Overview

持久化 LLM Wiki — 结构化、互联的 Markdown 知识库，由 LLM 自主维护和更新。

## Directory Structure

```
wiki/
├── SCHEMA.md          # ← 你正在读的这个文件
├── index.md           # ← 内容目录（每页一条记录，分类列出）
├── log.md             # ← 时间线日志（append-only，格式：## [YYYY-MM-DD] op | 标题）
├── concepts/          # ← 概念/主题页面
├── entities/          # ← 实体页面（人物/组织/产品等）
├── synthesis/         # ← 综合分析、交叉对比、洞察
├── sources/           # ← 原始来源记录（摘要引用，不动原文）
│   ├── articles/
│   ├── papers/
│   └── notes/
└── topics/            # ← 按主题组织的二级目录（按需创建）
```

## Naming Conventions

- 文件名：kebab-case，如 `machine-learning-bias`、`openai-strategy`
- 标题：使用英文或中文（保持一致即可，推荐中文以方便阅读）
- 每个文件顶部有 YAML frontmatter（可选但推荐）

## Page Format

```markdown
---
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
source: [来源引用或 URL]
---

# [标题]

## Summary
一段话概述。

## Key Points
- ...

## Related
- [[related-page-1]]
- [[related-page-2]]

## Notes
自由笔记。
```

## Operations

### Ingest（摄入新来源）

1. 把来源放到 `wiki/sources/` 下（可以是文件、笔记、或引用链接）
2. 阅读来源，提取关键信息
3. 在对应分类下创建/更新 wiki 页面
4. 更新 `index.md`
5. 追加一条记录到 `log.md`：`## [YYYY-MM-DD] ingest | 来源标题`

### Query（查询知识库）

1. 先读 `index.md` 找到相关页面
2. 读取相关页面内容
3. 合成回答
4. 如果查询产生了有价值的分析，存为新页面到 `wiki/synthesis/`

### Lint（健康检查）

定期检查：
- 页面间的矛盾
- 过时声明（被新来源推翻）
- 孤立页面（无入链）
- 有提及但无专页的重要概念
- 缺失的交叉引用

## Output Formats

根据查询需求，回答可以保存为：
- Markdown 页面（默认）
- 对比表格
- 综合分析

## Tips

- 每次 ingest 后可以更新多个页面（10-15 个是正常的）
- 保持 index.md 和 log.md 最新
- 发现矛盾时，在相关页面记录并标记 "CONTRADICTION"
