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