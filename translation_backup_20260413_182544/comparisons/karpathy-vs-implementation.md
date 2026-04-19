---
title: "Karpathy LLM Wiki Original vs Our Implementation"
date: 2026-04-05
type: comparison
tags: [wiki, karpathy, architecture, comparison]
sources: [gist:442a6bf555914893e9891c11519de94f]
---

# Karpathy Original vs Our Implementation

## Structural Differences

| Aspect | Karpathy Original | Our Implementation | Status |
|--------|------------------|-------------------|--------|
| **Three layers** | raw/ (immutable) → wiki/ (LLM-owned) → output (deliverables) | raw/ → wiki/ → output/ | ✅ Aligned |
| **raw/ organization** | articles/, papers/, repos/, assets/ | flat + assets/ | ⚠️ needs subdirs |
| **wiki/ pages** | Concepts, entities, comparisons, overview, synthesis, summaries | concepts/, entities/, comparisons/, synthesis/, sources/ | ✅ Aligned |
| **Schema file** | CLAUDE.md / AGENTS.md (top-level agent instruction) | wiki/SCHEMA.md | ⚠️ should be top-level |
| **index.md** | In wiki/ root; content catalog by category | In wiki/ root; organized by category | ✅ Aligned |
| **log.md** | In wiki/ root; append-only, parseable entries | In wiki/ root; append-only | ✅ Aligned |
| **output/** | Not explicitly a folder; deliverables filed back into wiki | Explicit output/ directory | ⚠️ extra layer |
| **Sources subfolder** | sources are raw/, wiki has source summaries | wiki/sources/ for document summaries | ✅ Aligned |

## Operational Alignment

| Operation | Karpathy | Our SCHEMA.md |
|-----------|----------|---------------|
| **Ingest** | Drop in raw/, LLM processes, updates wiki pages, index, log | Same 3-step flow documented | ✅ |
| **Query** | Search wiki, synthesize, file good answers back as wiki pages | Same flow documented | ✅ |
| **Lint** | Health-check for contradictions, orphans, stale claims | Same checklist documented | ✅ |
| **User involvement** | "I prefer to ingest one at a time and stay involved" | "和宇飞讨论要点" | ✅ |
| **Pages per ingest** | "10-15 wiki pages per source" | Same range expected | ✅ |

## Key Philosophical Points (Karpathy)

1. **"The wiki is a persistent, compounding artifact."** — Cross-references already there, contradictions flagged, synthesis reflects everything read
2. **"You never write the wiki yourself — the LLM writes and maintains all of it"** — User sources, LLM grunts
3. **"Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase"** — Development metaphor
4. **"The tedious part is not the reading or thinking — it's the bookkeeping"** — LLMs don't get bored, don't forget cross-references

## What We're Missing (from Karpathy's tips)

- ✗ **Obsidian Web Clipper** — browser extension → raw/ (宇飞可以用 Obsidian 桌面版)
- ✗ **Image download workflow** — attachments to raw/assets/
- ✗ **Marp** — markdown-to-slides format
- ✗ **Dataview** — Obsidian plugin for frontmatter queries
- ✗ **Graph view** — visualize wiki connections
- ✗ **qmd** — local markdown search engine (BM25 + vector + LLM re-ranking)
- ✗ **CLI tools** — custom tools for LLM wiki operations

## What We Added (beyond Karpathy)

- ✅ **YAML frontmatter** on every page (Karpathy mentions it as optional with Dataview)
- ✅ **Page format template** with Summary/Key Points/Related/Notes structure
- ✅ **Git versioning** via Gitee mirror → GitHub (infrastructure constraint solution)
- ✅ **SCHEMA.md** as explicit wiki instruction file (Karpathy uses CLAUDE.md / AGENTS.md)

---
*Comparison generated 2026-04-05 during initial structuring audit*
