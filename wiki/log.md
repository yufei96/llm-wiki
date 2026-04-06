# Wiki Log

Append-only record of all wiki activity.

## [2026-04-05 15:35] wiki structure | Aligned with Karpathy original
- Restructured: raw → wiki → output (3 layers per Karpathy gist:442a6bf)
- Added wiki/comparisons/ for analytical pages
- Pages: 7

## [2026-04-05 15:50] ingest | MOSA and US Defense Acquisition (Shah D.Eng. Praxis, 2021)
- Ingested: modular open systems approach thesis from GWU
- Created: 6 wiki pages (1 source, 2 concepts, 1 entity, 1 synthesis, 1 comparison)
- Topics: MOSA, vendor lock-in, Better Buying Power 3.0, FACE standard

## [2026-04-05 16:05] restructure + full ingest | Karpathy alignment + 124-page complete extract
- **Structure fixes**:
  - SCHEMA.md: moved from wiki/ to project root (Karpathy style: CLAUDE.md-level)
  - raw/: added papers/, articles/, repos/ subdirectories
  - MOSA files moved to raw/papers/
- **Full text extraction**: PyMuPDF extracted all 124 pages (187KB text)
  - Default pdf tool only reads first 10 pages — PyMuPDF solves this (pip install pymupdf --break-system-packages)
- **Hypothesis results** (complete):
  - H1 (cost/schedule): Not Supported — data can't isolate MOSA effect
  - H2 (gov claims success): Supported — 15+ programs cited
  - H3 (US depts require MOSA): Supported — Army, Navy, Air Force
  - H4 (non-US gov): Supported — UK MoD, Australia, Canada
  - H5 (commercial adoption): Supported — Airbus HForce
  - H6 (commercial success): Supported — H125M/H145M/H225M helicopters
- **New pages**: concepts/open-mission-systems.md
- **Updated**: sources/mosa-shah-thesis.md (full 124-page results), concepts/mosa-defense-acquisition.md (complete), index.md
- Total wiki pages: 12

## [2026-04-05 17:18] ingest | DoDI 5000.02 — Operation of the Adaptive Acquisition Framework (2020, Chg1 2022)
- Source: raw/papers/dodi-5000.02-adaptive-acquisition-framework-2020.pdf (19 pages, 33KB)
- **Key finding**: MOSA NOT mentioned anywhere in this document. The 2020 version was restructured; MOSA policy was in the 2015 version, but all content moved to separate child DoDIs (5000.85, 5000.80, 5000.88, 5000.89, 5000.91, 5000.95).
- AAF has 6 pathways: Urgent (<2yr), MTA (≤5yr), Major Capability (structured), Software (agile), DBS, Services
- MOSA search must pivot to **DoDI 5000.85** (Major Capability Acquisition) or other child instructions
- Pages created:
  - sources/2026-04-05-dodi-5000-02-2020.md
  - concepts/adaptive-acquisition-framework.md
- Total wiki pages: 14

## [2026-04-05 18:50] batch ingest: 4 new sources, all commits + pushed
Committed as e7a41f8, pushed to Gitee → GitHub.

### Source: MIL-STD-881D (2018) — Work Breakdown Structures
- 233 pages, 12 appendices, superseded 881C
- NDIA Recommendation #3 references this for MOSA component taxonomy
- Key 2018 additions: Data Rights, Cybersecurity, Software Engineering elements in Appendix K
- **Pages**: sources/2026-04-05-mil-std-881d-wbs-defense-materiel.md

### Source: FACE Technical Standard 3.2 (Aug 2023) — The Open Group
- 592 pages, only 4x MOSA mentions (p29, p588 glossary) — significant finding
- 5 segments: OS, I/O Services, Platform-Specific Services, Portable Components, Transport Services
- 3 "KEY" Standardized Interfaces (MOSA open interfaces)
- 70+ organizations, 900+ contributors, 20+ deployments
- UoC (Unit of Conformance) model — the actual mechanism for portability
- Conformance testing process exists — model for MOSA evaluation
- **Pages**: sources/2026-04-05-face-technical-standard-3.2-2023.md

### Source: DoDI 5000.85 (2020, Chg1 2021) — Major Capability Acquisition
- 40 pages — the MOSA legal mandate source we'd been searching for
- Page 26, §3C.3.a.(5): Full MOSA requirements
  - MDAPs after 1/1/2019 "must" design/develop with MOSA to max extent practicable
  - Acquisition strategy must describe: architecture, interfaces, IP, TDP, future evolution
  - RFP must specify MOSA implementation and minimum component set
- 6 acquisition pathways under AAF
- **Pages**: sources/2026-04-05-dodi-5000-85-2020.md

### Source: NDIA MOSA White Paper Recommendations (2019, Rev. D)
- 16 pages, 38 industry + 14 gov + 5 academia members
- Top 10 recommendations align perfectly with Shah thesis findings
- Key: "Make MOSA a requirement — not an option — for all procurements"
- OSMP = Open Systems Management Plan (as common as SEMP)
- **Pages**: sources/2026-04-05-ndia-mosa-white-paper-2019.md

### Key Synthesis (cross-source findings):
1. **DoDI 5000.02 has 0 MOSA mentions** vs **DoDI 5000.85 has 11** — framework vs. mandate
2. **FACE 3.2 barely mentions MOSA** (4x in 592 pages) — it's a spec, not a policy document
3. **MOSA legal basis** = USC 10 §2446a + DoDI 5000.85 §3C.3.a.(5) — both say "max extent practicable"
4. **NDIA + Shah align** on every gap: no metrics, no certification, no standardized metrics
5. **FACE is the only MOSA standard with conformance testing** — model for others

Total wiki pages: 20

## [2026-04-06 20:40] compile | First topic compilation — MOSA
- Adopted llm-wiki-compiler improvements: topic-based articles + standard structure + coverage tags
- Created: `wiki/topics/mosaic-modular-open-systems-approach.md`
- Merged: 12 sources into one topic article (all MOSA-related content)
- Standard sections: Summary, Timeline, Current State, Key Decisions, Experiments & Results, Gotchas, Open Questions, Sources
- Coverage tagging: `[coverage: high/medium/low]` to guide when to read raw
- Updated: index.md with new Topics section
- Total wiki pages: 21