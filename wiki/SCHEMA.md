# LLM Wiki Schema

## Overview
Persistent, structured, interlinked Markdown knowledge base maintained incrementally by the LLM. Not RAG — knowledge is compiled once and kept current, accumulated over time.

## Architecture (Karpathy, 2025)
Three layers:

| Layer | Role | Rule |
|-------|------|------|
| **raw/** | Immutable source documents (articles, papers, images, data) | LLM reads only, never writes here. Source of truth. |
| **wiki/** | LLM-generated Markdown pages (summaries, concepts, entities, comparisons) | LLM owns this layer entirely. Read only. |
| **output/** | Derived deliverables (Marp slides, charts, reports) | Generated from wiki, can be filed back into wiki. |

## Directory Structure
```
wiki-project/
├── raw/                      # Immutable source documents
│   ├── articles/
│   ├── papers/
│   ├── assets/               # Downloaded images, attachments
│   └── repos/
├── wiki/                     # LLM-owned wiki layer
│   ├── SCHEMA.md             # This file — conventions and workflow
│   ├── index.md              # Content catalog (all pages, by category)
│   ├── log.md                # Chronological, append-only activity log
│   ├── concepts/             # Topic/concept pages
│   ├── entities/             # Entity pages (people, organizations, products)
│   ├── comparisons/          # Comparison and synthesis pages
│   └── sources/              # Summaries/indexes of raw documents
└── output/                   # Derived deliverables
    ├── slides/
    ├── charts/
    └── reports/
```

## Language Convention

- **内容语言**：所有wiki页面正文使用**简体中文**
- **保留原文**：文件名保持英文，代码块保留原文，关键英文缩写（MOSA、DoDI、AAF等）保留不翻译
- **Source页摘要**：即使原文是英文，摘要用中文撰写

## Naming Conventions

- **Filenames**: kebab-case, e.g., `mosa-defense-acquisition`, `vendor-lock-in`
- **Titles**: 使用简体中文标题，英文缩写保留（如"模块化开放系统方法（MOSA）"）
- **YAML frontmatter** on every wiki page: `created`, `updated`, `tags`, `source`

## Page Format

```markdown
---
title: "Page Title"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
source: [raw/source-file.md]
---

# [Title]

## Summary
One-paragraph overview.

## Key Points
- ...

## Related
- [[related-page-1]]
- [[related-page-2]]

## Notes
Free-form notes, contradictions, caveats.
```

## Operations

### Ingest

Drop a new source into `raw/`, tell the LLM to process it:

1. Read the source and discuss key takeaways with the user
2. Write a summary page in `wiki/sources/`（含完整YAML front matter）
3. Create/update concept pages in `wiki/concepts/`（新概念若被3+处引用则建独立页）
4. Create/update entity pages in `wiki/entities/`
5. **补双向交叉引用**：source页加`## 相关内容`链接相关concept，concept页加对应source链接
6. Update `wiki/index.md`（content catalog）
7. Append entry to `wiki/log.md`: `## [YYYY-MM-DD] ingest | Source Title`
8. **验证完整性**：跑一次wikilink断链检查，确保新增链接目标存在

A single source might touch 10-15 wiki pages. Stay involved — read summaries and guide emphasis.

### Query

Ask questions against the wiki:

1. Read `wiki/index.md` to find relevant pages
2. Read the relevant pages in detail
3. Synthesize an answer with citations
4. If the query produces valuable analysis (comparisons, connections), save it as a new page in `wiki/comparisons/` or `wiki/synthesis/`

Good answers should be filed back into the wiki as new pages — explorations compound just like ingested sources.

### Lint

Periodically review the wiki for both health and emergent structure:

**Health检查：**

1. Read `wiki/log.md` for last Lint timestamp
2. Scan all wiki pages for:
   - Contradictions between pages
   - Stale claims superseded by newer sources
   - Orphan pages with no inbound links
   - Missing cross-references
3. Run wikilink integrity check (all `[[page]]` targets exist)

**模式发现（Synthesize）：**

4. After accumulating 5+ new sources, review the corpus as a whole:
   - What patterns emerge across sources that no single page captures?
   - What connections exist between standards/policies/concepts?
   - What concepts are evolving (policy versions, expanding scope)?
   - What tensions or contradictions exist in the material?
5. Save emergent insights as new pages in `wiki/comparisons/` or `wiki/topics/`
6. Report findings and suggest new questions to investigate

This is the Zettelkasten "emergent structure" step — knowledge isn't planned, it surfaces when accumulated density reaches a threshold.

## Index and Log

**index.md** — Content-oriented catalog. Every wiki page listed with link, one-line summary, and category. Organized by type (entities, concepts, sources, etc.). Updated on every ingest. At moderate scale (~100 sources, ~hundreds of pages) this works well instead of embedding-based RAG.

**log.md** — Chronological, append-only record. Each entry: `## [YYYY-MM-DD] operation | Title`. Parseable with Unix tools: `grep "^## \[" wiki/log.md | tail -5`.

## Output Formats

Query answers can take different forms, all filed back into the wiki:
- **Markdown page** (default) — for concepts, entities, notes
- **Comparison table** — for side-by-side analysis
- **Marp slides** — for presentations (markdown-based)
- **Matplotlib chart** — for data visualization

## Tips

- Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase
- Download images to `raw/assets/` so the LLM can view them directly
- Obsidian graph view shows wiki shape — connections, hubs, orphans
- The wiki is just a git repo — version history, branching, collaboration
- Good questions to investigate are as valuable as the answers

## Red Flags

- Ingest without updating `index.md`
- Ingest without appending to `log.md`
- Source files modified by the LLM (raw should be immutable)
- Query results discarded after chat instead of saved as wiki pages
- Contradictions between pages left unmarked
- Orphan pages growing without review
