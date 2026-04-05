# LLM Wiki

A persistent, structured knowledge base — automatically generated and maintained by an AI assistant from ingested documents (papers, policy documents, standards, articles).

Different from RAG: knowledge is compiled into structured wiki pages with cross-references, so every query benefits from all prior accumulated context.

## Architecture

```
┌─────────────────────────────────────────────────────┐
│  raw/          ← Immutable source documents         │
│    papers/      → Academic papers, technical reports │
│    articles/    → Articles, blog posts, notes        │
│    repos/       → Reference repositories             │
│                                                     │
│  wiki/         ← LLM-generated structured pages     │
│    sources/     → Summaries of ingested sources      │
│    concepts/    → Concept definitions & relationships│
│    entities/    → People, organizations, programs    │
│    comparisons/ → Cross-source analytical pages      │
│    synthesis/   → Integrated knowledge pages         │
│    index.md     → Content directory                  │
│    log.md       → Activity timeline                  │
│                                                     │
│  output/       ← Delivery artifacts                 │
│                                                     │
│  SCHEMA.md     ← Structure rules & conventions      │
└─────────────────────────────────────────────────────┘
```

## Workflow

1. **Ingest**: Drop a document (PDF, article, note) → AI extracts key information → creates/updates wiki pages
2. **Query**: Ask the AI about any topic → it searches the wiki and synthesizes answers from accumulated knowledge
3. **Lint**: Check structural consistency (broken links, missing references, orphan pages)

## Design

Based on [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

### Key Principles

- **Sources are immutable** — once ingested, raw files never change
- **Wiki pages are living** — updated as new sources add or contradict information
- **Cross-references link everything** — `[[wikilinks]]` connect concepts, entities, and sources
- **Git tracks all changes** — full edit history, no information loss
- **Push mirrors to Gitee → GitHub** for Obsidian sync on other machines

## Current Focus: MOSA (Modular Open Systems Approach)

This wiki started with MOSA research — a DoD acquisition strategy for modular architecture and open interfaces across defense systems.

### Ingested Sources

| # | Source | Pages | Key Finding |
|---|--------|-------|-------------|
| 1 | Shah, "MOSA and US Defense Acquisition" (GWU D.Eng. 2021) | 124 | 5/6 hypotheses supported; no standardized MOSA evaluation metrics |
| 2 | DoDI 5000.02 — Operation of the AAF (2020, Chg1 2022) | 19 | **0 MOSA mentions** — framework document only |
| 3 | DoDI 5000.85 — Major Capability Acquisition (2020, Chg1 2021) | 40 | **MOSA legal mandate** — p.26 §3C.3.a.(5), 11 MOSA mentions |
| 4 | NDIA MOSA White Paper — Top 10 Recommendations (2019) | 16 | Industry+gov alignment; "Make MOSA a requirement, not an option" |
| 5 | MIL-STD-881D — WBS for Defense Materiel Items (2018) | 233 | NDIA Rec #3 reference for MOSA component taxonomy |
| 6 | FACE Technical Standard, Ed. 3.2 (Aug 2023) | 592 | Most mature MOSA practice; only 4 MOSA mentions in spec |

### Core Knowledge Network

- **Concepts**: MOSA, vendor lock-in, AAF, FACE, OMS, defense acquisition overrun trends
- **Entities**: Parth Devang Shah, Ellen M. Lord, The Open Group, FACE Consortium
- **Relationships**: 6 source documents cross-referencing the same gaps from different angles

### Key Insight (Cross-Source Synthesis)

The same MOSA evaluation gap appears in all 6 sources: **no standardized metrics for MOSA compliance or ROI**.
- Shah thesis: "What to measure, how to measure, and with what metrics to measure remain the key challenge."
- NDIA: "Define MOSA metrics for various domains and SoS levels."
- DoDI 5000.85: Requires MOSA "to the maximum extent practicable" but doesn't define what that means.
- FACE: The *only* standard with an actual **conformance testing process** — a model others could follow.

## Repo Structure

```
.
├── README.md          ← This file
├── SCHEMA.md          ← Wiki structure rules and conventions
├── raw/               ← Immutable source documents (PDFs, articles)
├── wiki/              ← LLM-generated markdown pages
├── output/            ← Delivery artifacts (exported documents)
└── .gitignore         ← Excludes .git-credentials
```

## Sync

- **Server → Gitee**: Direct `git push` (this machine)
- **Gitee → GitHub**: Automatic mirror via Gitee repo mirror feature
- **GitHub → Local (Obsidian)**: Pull from GitHub for Obsidian viewing

## Usage

Send documents (PDFs, articles, notes) to the AI assistant — it will ingest them and update the wiki automatically.

---

*Maintained by 虾宝 🦐 — last updated 2026-04-05*
