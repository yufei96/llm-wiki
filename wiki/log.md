# Wiki Log

## [2026-04-19 10:58] ingest | DoDI 5000.80 — 中间采办层级（MTA）
   - Created: wiki/sources/2026-04-19-dodi-5000-80-middle-tier-acquisition.md
   - Source: raw/papers/dodi-5000.80-middle-tier-acquisition.pdf (19 pages, Chg1 2024, 用户提供)
   - MOSA提及: 0次。MTA路径以速度优先，5年内完成快速原型/部署。
   - 旧文件raw/papers/dodi_5000.80.pdf（内容实际为5000.81）已重命名为dodi_5000.80-MISNAMED-actually-5000.81.pdf
   - AAF六条路径补全完成：5000.02/5000.74/5000.75/5000.80/5000.81/5000.85/5000.87


## [2026-04-19 10:48] ingest | Better Buying Power 3.0 实施指令
   - Created: wiki/sources/2026-04-19-bbp-3-0-implementation-directive.md
   - Source: raw/papers/bbp-3-implementation-directive.pdf (35 pages, 用户提供)
   - MOSA提及: **关键** — BBP 3.0首次将MOSA写入DoD政策（"Use Modular Open Systems Architecture to stimulate innovation"）
   - 关键发现：MOSA五原则（赋能环境/模块化设计/指定接口/开放标准/一致性认证）直接演变为2025年五大支柱

## [2026-04-19 10:48] ingest | GAO-24-106831 武器系统年度评估
   - Created: wiki/sources/2026-04-19-gao-24-106831-weapon-systems.md
   - Source: raw/papers/gao-24-106831-weapon-systems-assessment.pdf (261 pages, 用户提供)
   - MOSA提及: 若干（MK 54鱼雷、Sentinel、F-22开放系统架构演示）
   - 关键数据：MDAP未交付项目平均>10年、MTA项目多数未实施领先实践


## [2026-04-19 09:44] ingest | DoDI 5000.75 — 业务系统需求与采办
   - Created: wiki/sources/2026-04-19-dodi-5000-75-business-systems.md
   - Updated: wiki/index.md
   - Source: raw/papers/dodi_5000.75.pdf (39 pages)
   - MOSA提及: 0次。业务系统独立采办流程（BCAC），不适用MOSA法定要求。
   - 已纳入知识库作为AAF框架补充文档。

## [2026-04-19 09:44] ingest | DoDI 5000.81 — 紧急能力采办
   - Created: wiki/sources/2026-04-19-dodi-5000-81-urgent-capability.md
   - Updated: wiki/index.md
   - Source: raw/papers/dodi_5000.81.pdf (21 pages)
   - MOSA提及: 0次。紧急采办路径（<2年部署）明确将速度优先于模块化设计。
   - ⚠️ raw/papers/dodi_5000.80.pdf 内容与dodi_5000.81.pdf完全相同（命名错误）。

## [2026-04-19 09:44] ingest | DFARS Part 252 — 征询条款与合同条款
   - Created: wiki/sources/2026-04-19-dfars-part-252-contract-clauses.md
   - Updated: wiki/index.md
   - Source: raw/papers/dfars_part-252---solicitation-provisions-and-contract-clauses.pdf (607 pages)
   - MOSA提及: 0次直接提及。DFARS 252.227条款群（数据权利）是MOSA合同执行机制的基础。
   - 关键条款：252.227-7013（技术数据权利）、252.227-7014（软件权利）、252.227-7037（权利限制验证）。

## [2026-04-19 09:44] ingest | HASC Report 114-102 — FY2016 NDAA 委员会报告
   - Created: wiki/sources/2026-04-19-hasc-report-114-102-fy2016-ndaa.md
   - Updated: wiki/index.md
   - Source: raw/papers/hasc_report_114-102.pdf (358 pages)
   - MOSA提及: 0次。本报告的Section 805与FY2017 NDAA Section 805（MOSA法定来源）是不同条款。
   - 作为MOSA立法前夕的采办改革背景文档。


## [2026-04-19 09:35] fix | 断链修复与知识库整理
- 删除4个重复source页面：10us-code-4401/4402/4403、dfars-part-207-acquisition-planning
- 统一wikilink命名：better-buying-power-3→-3-0、dodi-5000-85→2026-04-05版、wosa-chain→wosa
- 修复~50处断链：实体链接转纯文本、PDF引用转wikilink、名称不匹配修正
- 创建2个缺失概念页面：defense-acquisition-overrun-trends（4处引用）、modular-architecture-patterns（3处引用）
- index.md同步：删除幻影链接、补充孤立页面
- 验证：全部wikilink通过（0断链）
- Total wiki pages: 30 (excluding index/log)


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

## [2026-04-10] migration | Migrated from OpenClaw to Hermes Agent
- Full repository migration: all raw/, wiki/, and structure preserved
- Updated git remote: Gitee → GitHub (public mirror)
- LLM Wiki 存量迁移总结：
  - 21 original pages, migrated 30 pages total (added new sources from OpenClaw ingest)
  - 9 new source documents added: DFARS 207/227, 10 USC §4401-4403, DoDI 5000.74, DoDI 5000.87, FY2017 NDAA §805, 2025 MOSA Implementation Guidebook
  - 2 new concepts: `mosa-five-pillars`, `topics/mosa-implementation-guidebook`
  - All files retained full git history
- Lint pass done: orphan pages and broken links documented, no critical issues

Total wiki pages: 30
## [2026-04-13] ingest | WOSA架构工具链分析
   - Created: wiki/concepts/wosa-architecture-tools.md
   - Updated: wiki/index.md
   - Source: raw/articles/wosa-architecture-tools-analysis.md
## [2026-04-13] ingest | 75195d4e-741e-4cee-8e1e-72ec9bc966ab.pdf
   - Created: wiki/concepts/unknown-tech-report-75195d4e.md
   - Updated: wiki/index.md
   - Source: raw/papers/75195d4e-741e-4cee-8e1e-72ec9bc966ab.pdf
   - Note: PDF转换超时，创建了占位概念页面
## [2026-04-13] process | PDF处理完成：75195d4e-741e-4cee-8e1e-72ec9bc966ab.pdf
   - 已使用 mutool 提取文本内容 (1322 字符)
   - 原始PDF保持未修改
   - 已更新markdown文件用于LLM处理
   - 已更新概念页面和索引
   - 所有处理严格遵循llm-wiki原则
## [2026-04-13] ingest | MIL-HDBK-1211(MI): Missile Flight Simulation Handbook
   - Created: wiki/sources/mil-hdbk-1211-mi-missile-flight-simulation.md
   - Updated: wiki/index.md
   - Source: raw/papers/75195d4e-741e-4cee-8e1e-72ec9bc966ab.pdf
   - Text content extracted via mutool (847,337 characters)
   - Original PDF preserved in raw/papers/
   - Added source entry to index and concept cross-references