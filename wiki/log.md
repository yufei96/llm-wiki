
---

## 2026-05-06 — 开放架构层次体系扩展：从10种到21种实现

**触发**：用户指出"其他的各种开放系统架构的实现也应该归入这个分类结构"，要求补全美国所有开放架构实现

**操作**：
- 新建13个wiki source pages（AMS GRA, A-GRA, ABMS GRA, NC3 GRA, Sentinel GRA, COARPS, R-EGI, SCARS, CFW ICD, OSMP, NG InSight, DAU Next Gen Acquisition, Senate Hunter Testimony）
- 下载14个.mil/.gov PDF/DOCX到raw/papers/，mutool转换到raw/articles/
- 下载11个web文章到raw/articles/
- 更新层次总览页open-architecture-hierarchy.md：从10种→21种实现
- 更新index.md、交叉引用

**新建source pages**：
- wiki/sources/dau-next-gen-acquisition-2024.md — DAU演示（全GRA清单）
- wiki/sources/senate-defense-hunter-testimony-2024.md — Senate证词（AMS GRA/A-GRA）
- wiki/sources/ng-insight-open-processor.md — NG InSight处理器（AMS-GRA合规）
- wiki/sources/afrc-a-gra-cca-validation-2025.md — A-GRA/CCA验证
- wiki/sources/crs-nc3-if11697.md — NC3 CRS入门
- wiki/sources/dtic-nc3-architecture-ada619949.md — NC3 GAO审查
- wiki/sources/crs-sentinel-icbm-if11681.md — Sentinel CRS入门
- wiki/sources/afgsc-sentinel-gbsd.md — AFGSC Sentinel部署
- wiki/sources/dvids-r-egi-pnt-flight-2024.md — R-EGI飞行演示
- wiki/sources/usaf-coarps-rfi-2021.md — COARPS RFI
- wiki/sources/ntsa-scars-stcf-2025.md — SCARS 2025简报
- wiki/sources/ndia-cfw-icd-wright-2015.md — CFW ICD NDIA演示
- wiki/sources/navair-osmp-guide-v1-2025.md — OSMP实施指南

**新增raw/papers/**：
- dau-next-gen-acquisition-2024.pdf, dtic-nc3-architecture-ada619949.pdf, afrc-a-gra-cca-validation-2025.pdf, senate-defense-hunter-testimony-2024.pdf, dvids-r-egi-pnt-flight-2024.pdf, crs-sentinel-icbm-if11681.pdf, crs-nc3-if11697.pdf, ng-insight-open-processor.pdf, navair-osmp-guide-v1-2025.pdf, usaf-coarps-rfi-2021.docx, samgov-uai-rfi.pdf, ntsa-scars-stcf-2025.pdf, afgsc-sentinel-gbsd.pdf, ndia-cfw-icd-wright-2015.pdf

**更新**：
- wiki/comparisons/open-architecture-hierarchy.md — 21种实现四层结构，链接到concept pages
- wiki/index.md — 新增11个concept pages + 3个comparison pages
- wiki/log.md — 本条目

**新建concept pages**：
- wiki/concepts/ams-gra-agile-mission-suite.md — AMS GRA
- wiki/concepts/a-gra-autonomy-reference-architecture.md — A-GRA
- wiki/concepts/abms-gra-advanced-battle-management.md — ABMS GRA
- wiki/concepts/pnt-gra-r-egi.md — PNT GRA/R-EGI
- wiki/concepts/coarps-radar-architecture.md — COARPS
- wiki/concepts/scars-simulator-architecture.md — SCARS
- wiki/concepts/nc3-gra-nuclear-c3.md — NC3 GRA
- wiki/concepts/sentinel-gra-icbm.md — Sentinel GRA

**Mission Planning GRA**：公开信息极少（仅Garrett演示一行），待后续补充

**POST-INGEST分析**：
- 新建8个entity pages：CAE USA、General Atomics、Anduril、Shield AI、Collins Aerospace、IS4S、AFGSC、STRATCOM
- 新建1个topic page：gra-ecosystem-evolution（GRA生态演进：从单一标准到四层架构体系）
- 更新overview.md：新增第4节"GRA生态：21种开放架构的四层体系"
- 更新index.md：新增entity pages和topic page

---

## 2026-04-29 — 软件定义能力+数字生态系统平台+OMS/CCA扩展

**新增概念页面（2个）**：
- `software-defined-capabilities.md` — 软件定义能力：CCA和ABMS的核心设计理念（硬件标准化+软件可替换+能力通过软件配置），与OMS/FACE/MOSA的关系
- `digital-ecosystem-platforms.md` — 数字生态系统四大平台对比：PLM（数据管理）、FENCES（网络安全）、CLOUDONE（云基础设施）、PLATFORMONE（DevSecOps）

**扩展页面（4个）**：
- `open-mission-systems.md` — 大幅扩展：新增GRA目标架构中OMS作为"抽象服务总线（ASB）隔离器"角色、CCA关联、FACE TIM 2021集成实践、Chris Garrett演示数据
- `speed-vs-modularity.md` — 新增CCA作为最新案例（2028 MTA时间线 vs MOSA合规）、SAB ToR隐含审查、平衡策略（GRA复用、标准堆栈预集成）
- `c5isr-standards-convergence.md` — 新增FACE TIM 2021实证数据（20公司×29产品×8 TSS集成规模、多版本FACE互操作、TSS桥接机制、遗留系统融入、容器适航性差距）
- `digital-engineering-practice.md` — 新增NASA三层DE实施体系（HDBK-1004采办框架217页 + HDBK-1009A系统建模88页 + HDBK-7009A M&S质量157页）、实施数据（692用户/1100+模型）、与DoD体系对比

**来源**：
- Chris Garrett AFMC演示 (2024.9, 19页)
- FY2024 SAB S&T审查ToR (6页)
- PEO Aviation FACE TIM 2021 (56页)

**更新index.md**：+2 concepts, +1 comparison

---

## 2026-04-26 — 数字工程×MOSA交叉领域补充

**新增source页面**：
- `nist-sp-800-160-v2-cyber-resilience.md` — NIST赛博弹性系统开发（310页，含11项结构性设计原则，与MOSA模块化高度对齐）
- `sysml-v2-specification.md` — SysML v2规范（2025年6月OMG正式采纳，MOSA接口建模的下一代语言基础）
- `ousd-sysml-v2-transition-guidance.md` — OUSD(R&E) SysML v1→v2 过渡指导（官方规划大纲）
- `ndia-sysml-v2-transition-2023.md` — NDIA 2023 SysML v2 过渡指南项目简报（Daniel Hettema）
- `nasa-se-handbook-rev2.md` — NASA系统工程手册 Rev 2（接口管理体系，MOSA工程实践参考）
- `incose-se-handbook-v5.md` — INCOSE SE Handbook V5（系统工程权威参考，与ISO 15288对齐）

**新增实体**：
- `daniel-hetzema.md` — Daniel Hettema（DEM&S 主任，SysML v2 过渡推动者）
- `ousd-re.md` — OUSD(R&E) 研究与工程副部长办公室
- `dems.md` — DEM&S 数字工程、建模与仿真团队

**新增对比页**：
- `three-se-handbooks-detailed-comparison.md` — 三本SE手册逐维度对比（NASA/INCOSE/ISO）

**交叉引用修复**（14个页面）：
- `digital-engineering-ecosystem` — +INCOSE/NASA/NIST
- `three-se-handbooks-detailed-comparison` — +NIST
- `three-se-handbooks-complement` — +NIST
- `iso-15288-2023` — +INCOSE
- `digital-engineering-mosa-convergence` — +INCOSE
- `incose-mbse-methodology-survey` — +INCOSE/NASA
- `sysml-v2-specification` — +INCOSE
- `nist-sp-800-160-v2-cyber-resilience` — +NASA
- `incose-se-handbook-v5` — +INCOSE entity
- `ppi` / `ppi-business-case-se` / `ppi-integrating-pm-se` / `ppi-did-templates` — +INCOSE
- `ppi-requirements-quality-metrics` — +NASA

**概念/主题页修复**（12个页面）：
- 概念 高密度 6个: `requirements-quality-mosa` / `mosa-five-pillars` / `mosa-defense-acquisition` / `modular-architecture-patterns` / `mosa-brownfield-vs-greenfield` / `dews-mosa-reference-architecture` — +接口演进
- 概念 中密度 4个: `mosa-digital-engineering` / `mosa-five-pillars-assessment` / `host-hardware-open-systems` / `ucs-control-station` — +接口演进
- 主题 2个: `digital-engineering-ecosystem` +SysML / `three-se-handbooks-complement` +SysML

**洞察综合（5+新source后执行）**：
- `interface-engineering-evolution.md` — 接口工程三层演进（NASA ICD → MOSA标准化 → SysML v2模型驱动）
- `nist-cyber-resilience-mosa-security.md` — NIST赛博弹性设计原则作为MOSA安全性架构框架（7/11项原则直接映射）
- `sysml-v2-transition-bottleneck.md` — SysML v1→v2过渡作为MOSA数字工程落地的基础设施瓶颈（15,000+模型迁移）
- `incose-resilience-vs-nist-cyber-resilience.md` — INCOSE韧性 vs NIST赛博弹性（通用框架与赛博特化的关系）
- `three-se-handbooks-complement.md` — 三本SE手册互补（NASA/INCOSE/ISO三层参考体系）

**更新页面**：
- `cybersecurity-vs-mosa-openness.md` — 新增NIST赛博弹性框架作为MOSA安全性的解决方案
- `digital-engineering-tools-comparison.md` — 新增SysML v2引用
- `digital-engineering-ecosystem.md` — 新增NIST和SysML v2来源
- `incose.md` — 新增SysML v2标准化活动
- `mosa-digital-engineering.md` — 新增NIST和SysML v2引用

**已下载原始资料**：
- `NIST.SP.800-160v2r1.pdf` (5.0M, 42273行) — 赛博弹性工程
- `SysML-v2-Basics-2024.pdf` (1.5M, 974行) — SysML v2概述
- `raw/repo/sysml-v2-release/` — SysML v2官方repo（含KerML 454页、SysML v2 691页、API 107页、v1→v2转换 661页、图形表示法 123页，共5个规范PDF + BNF语法定义）
- `SysML-Info-Sheet-Jan2025.pdf` (893K, 2页) — OUSD(R&E) SysML v2 技术亮点
- `SysML-v2-TransitionOutline-1.1.pdf` (360K) — OUSD(R&E) SysML v1→v2 过渡规划大纲 v1.1
- `Thurs_1560710_Stirk.pdf` (2.0M) — NDIA 2023 SysML v2 过渡指南项目简报
- `NASA-SP-2016-6105-Rev2.pdf` (4.0M, 21030行) — NASA系统工程手册 Rev 2
- `INCOSE-SE-Handbook-V5.pdf` (8.8M, 22329行) — INCOSE SE Handbook V5

**待手动下载**（服务器不可达）：
- ~~INCOSE SE Handbook V5（付费书）~~ ✅ 已由用户手动下载

---
## 2026-04-20 — 知识库全面质量检查与修复

**操作**：扫描77个内容页面，发现47个有问题，全部修复

**修复内容**：
1. **37个页面**补充frontmatter created/updated字段
2. **15个页面**补充## 相关内容章节
3. **dfars-part-227**用PDF原文重写（从17行扩展到100+行，含Subpart 227.71全文摘要）
4. **karpathy-vs-implementation**更新为当前状态（含post-ingest checklist、topics/）
5. **mosaic-modular-open-systems-approach**补充frontmatter title
6. 修复1处断链（SCHEMA.md wikilink）

**验证**：77个页面，0 frontmatter缺失，0 缺少相关内容，0断链

---

## 2026-04-20 — source文件名去掉日期前缀

**操作**：批量重命名sources/下43个文件，去掉YYYY-MM-DD-前缀

**改名规则**：`2026-04-19-dodi-5000-75-business-systems.md` → `dodi-5000-75-business-systems.md`

**原因**：
- 日期前缀与YAML frontmatter的created字段冗余
- wikilink引用时容易漏前缀导致断链
- 文件名更简洁易记

**处理**：
- 43个source文件改名
- 60个wiki文件更新wikilink引用
- 验证：0断链

---

## 2026-04-20 上午 — 知识库机制改进

**问题**：摄取文章后entities/topics/comparisons经常不更新，Karpathy原版overview.md缺失

**修复内容**：

1. **修复7处断链**：
   - `dodi-5000.97-digital-engineering` → `2026-04-19-dodi-5000-97-digital-engineering`（6处）
   - `ppi-integrating-pm-se` → `2026-04-19-ppi-integrating-pm-se`（1处）
   - `ppi-requirements-analysis` → `2026-04-19-ppi-requirements-analysis`（1处）

2. **更新llm-wiki skill**：
   - 新增⑦ **POST-INGEST MANDATORY CHECKLIST**：每次ingest后必须检查5个下游文件夹
   - 新增overview.md章节：定义了overview.md的定位、更新时机、结构
   - 更新架构图：加入overview.md
   - 更新orientation步骤：加入读取overview.md

3. **更新SCHEMA.md**：
   - 目录结构加入overview.md、topics/
   - Ingest操作加入post-ingest checklist
   - Red Flags加入"未检查下游文件夹"和"未更新overview.md"

4. **创建overview.md**：
   - 知识库"我现在知道什么"总览
   - 5条核心故事线：MOSA演化、DEE、C5ISR标准、合同框架、国际化
   - 待填补空白清单

**统计数据**：76个wiki页面，7条断链已修复，0孤儿页面待处理（17个中大部分是新增entities/topics，自然状态）

**补充操作**：
- 删除 `~/wiki/wiki/synthesis/` 空目录（方案A已合并到topics）
- 合并两个SCHEMA.md：根目录`~/wiki/SCHEMA.md`改为项目说明指针，权威版在`~/wiki/wiki/SCHEMA.md`
- 权威SCHEMA.md加入post-ingest checklist、overview.md定义、updated Red Flags

---

## 2026-04-20 上午 — 补充entities和topics

**操作**：根据新摄取内容补充entities和topics，理顺synthesis/topics关系

**决策**：采用方案A，保留topics，明确定位：
- concepts：定义层（What）
- topics：实践层（How）— 跨来源主题综合
- comparisons：分析层（Comparison）

**新建entities（4个）**：
- `omb` — 管理和预算办公室（OMB Circular A-130发布机构）
- `incose` — 国际系统工程委员会（MBSE方法论调查发布组织）
- `dsb` — 国防科学委员会（数字工程报告发布机构）
- `ppi` — 国际项目绩效公司（DID模板、SE/RE投资回报研究）

**新建topics（1个）**：
- `digital-engineering-ecosystem` — 数字工程生态系统（DEE）概述（综合5个来源）

**更新index.md**：
- 新增4个entities条目
- 新增1个topics条目
- 删除Synthesis部分（已合并到topics）

---

## 2026-04-20 早晨 — 新增2个结构性comparison

**操作**：基于用户需求，创建2个新的对比分析页面

**新建comparison页（2个）**：
- `cybersecurity-vs-mosa-openness` — 赛博安全与MOSA开放接口的政策张力
  - 分析OMB A-130信息安全要求与MOSA开放接口的矛盾
  - 提出分级开放、零信任架构、DevSecOps等平衡策略
- `digital-engineering-mosa-convergence` — 数字工程与MOSA融合
  - 分析MOSA从采办策略到DEE技术基础的第二次质变
  - 整合DoD数字工程战略2018、DoDI 5000.97、INCOSE MBSE调查、DSB报告

**更新index.md**：Comparisons部分新增2个条目

**最终状态**：9个comparison页面

---

## 2026-04-20 早晨 — 补充遗漏PDF：OMB Circular A-130

**操作**：检查昨天发送的PDF文件，发现2个遗漏，处理入知识库

**检查结果**：
- `500002p.PDF` (497 KB) — 与已处理的`dodi-5000.02-adaptive-acquisition-framework-2020.pdf`完全相同（文件大小509233 bytes），删除重复文件
- `a130revised.pdf` (537 KB) — OMB Circular A-130 "Managing Information as a Strategic Resource"，未处理

**新建source页（1个）**：
  - 联邦信息资源管理顶层政策（信息安全、隐私保护、IT投资管理）
  - 与MOSA知识库关联：开放接口的隐私风险、数据权利、IT投资框架

**更新index.md**：新增OMB Circular A-130条目

**处理工具**：使用mutool提取PDF文本（比markitdown更稳定）

**最终状态**：68个wiki页面

---

## 2026-04-19 深夜 — 数字工程核心材料补充

**操作**：用户上传3个关键PDF，处理入知识库

**新建source页（3个）**：
- `dod-de-strategy-2018` — DoD数字工程战略2018（纲领文件，5大目标：权威数据源/数字线程/MBSE/文化变革/基础设施）
- `incose-mbse-methodology-survey` — INCOSE MBSE方法论调查（JPL Estefan 2008，覆盖OOSEM/Harmony-SE/Vitech/JPL State Analysis等方法）
- `iso-15288-2023` — ISO/IEC/IEEE 15288:2023 系统生命周期过程（第二版，4类过程组）

**更新concept页**：
- `mosa-digital-engineering` — "待补充材料"更新为"已补充+仍待补充"，相关链接增加3个

**最终状态**：67个wiki页面，327条wikilink，100%交叉引用完整性

---

---

## 2026-04-19 深夜 — PPI洞察深挖

**操作**：从12个PPI系统工程文件中提炼3个结构性洞察，创建wiki页面

**新建concept页（1个）**：
- `requirements-quality-mosa` — 需求质量：MOSA的技术基础（接口定义质量=MOSA成败关键）

**新建comparison页（2个）**：
- `mosa-implementation-stack` — MOSA实施全栈：从法律到合同执行的五层架构
- `pm-se-integration-mosa` — PM-SE整合：MOSA实施的组织瓶颈（赋能环境支柱的深层分析）

**补交叉引用（5处）**：mosa-defense-acquisition、mosa-five-pillars、wosa-architecture-tools、speed-vs-modularity、ppi-integrating-pm-se

**最终状态**：64个wiki页面，305条wikilink，100%交叉引用完整性

---

---

## 2026-04-19 晚间 — PPI系统工程资源ingest

**操作**：下载并处理12个PPI系统工程PDF，创建5个source页

**下载（12个，7.9 MB）**：
- DID模板7个：CONOPS/OSD、SEP、SOW、SSDD、SyRS、SEM Definitions、Requirements Quality Metrics
- 通用SE 5个：SE投资回报、RE投资回报、需求分析×2、PM-SE整合

**新建source页（5个）**：
- `ppi-did-templates` — 7个DID模板合集（合同执行层，MOSA→合同的转化工具）
- `ppi-business-case-se` — SE投资回报论证（ROI 10:1-100:1）
- `ppi-business-case-re` — RE投资回报论证（需求缺陷是成本超支首要原因）
- `ppi-requirements-analysis` — 需求分析方法论（PPI流程+概览）
- `ppi-integrating-pm-se` — PM与SE整合方法

**补交叉引用（4处）**：mosa-defense-acquisition、wosa-architecture-tools、speed-vs-modularity、peo-aviation-impl-guide

**最终状态**：61个wiki页面，266条wikilink，99.6%完整度（1处已修复）

---

---

## 2026-04-19 晚间 — Synthesize：结构性洞察提炼

**操作**：回顾已有55个wiki页面，提炼5个跨source结构性洞察

**新增comparison/topic页（5个）**：
- `mosa-five-principles-to-pillars` — MOSA五原则→五大支柱12年演化对比
- `c5isr-standards-convergence` — C5ISR标准生态趋同（CMOSS/SOSA/OMS/VICTORY/MORA）
- `mosa-internationalization` — MOSA从美国DoD到NATO联盟的国际化扩展
- `speed-vs-modularity` — MTA快速路径中MOSA不强制的政策张力分析

**新增concept页（1个）**：
- `mosa-digital-engineering` — MOSA与数字工程融合（DEE九大要素之一）

**更新SCHEMA.md**：
- Lint操作扩展为"健康检查+模式发现"，引入Zettelkasten emergent structure理念

**最终状态**：56个wiki页面，236条wikilink，100%交叉引用完整性

---

---

## 2026-04-19 晚间 — 概念层完善

**操作**：基于用户"concepts等页面有没有应当增加的"指令，完善知识库概念层

**新增concept页（2个）**：
- `ucs-control-station` — 无人系统指挥控制标准接口（UCS），9次引用
- `middle-tier-acquisition` — 中间采办层级（MTA），9次引用

**修复YAML头部（2个）**：
- `mosa-five-pillars` — 添加created/updated/tags/sources字段
- `mosa-implementation-guidebook`（topic页）— 添加YAML头部

**补交叉引用（约25处）**：
- 6个source页补mosa-defense-acquisition链接
- 4个source页补face-technical-standard链接
- 2个source页补vendor-lock-in链接
- 各1处补open-mission-systems、adaptive-acquisition-framework、modular-architecture-patterns
- 5个concept页补新source/新concept链接
- 修复mosa-five-pillars重复链接

**更新index.md**：添加2个新concept页，Standards补SCA

**最终状态**：57个wiki页面，38个raw PDF

# Wiki Log

## [2026-04-19 14:17] ingest | 用户补充缺口文档：MORA + OSA指南 + DoDI 5000.97 + UCS + ARSENL
   - MORA (8页): 射频架构标准，CMOSS的RF组件，从VICTORY衍生，v2.3
   - OSA Contract Guidebook v1.1 (223页): **MOSA五原则原始定义文档**，2013年USD(AT&L)发布
   - DoDI 5000.97 (数字工程指令): MOSA列为数字工程九大要素之一
   - STANAG 4586 (14页): NATO UAV控制系统标准接口，UCS标准
   - ARSENL (4页): USAF MOSA使能标准官方清单，发现SCA/REDHAWK/CoPaIS三个新标准领域
   - IRENE (297页): AFRL辐射环境模型，与MOSA无关，未创建source页


## [2026-04-19 11:49] ingest | 第二/三梯队补充：DSP Journal + PEO Aviation + DSB
   - DSP Journal MOSA专刊 (40页): MOSA/CMOSS/VICTORY/MORA/SOSA综述，标准生态最佳入门
   - PEO Aviation Industry Day 2022 (79 slides): 9条MOSA工作线、EAF框架、行业协作
   - PEO Aviation MOSA实施指南 (23页): 合同模板(SOW/PWS/SPS/TEMP)、软件检查清单、BCA模板
   - DSB数字工程报告 (66页): MOSA作为数字工程生态系统(DEE)的技术基础
   - 第二梯队完成: 4/4 ✅（CMOSS/SOSA/VICTORY/OMS-PEO Aviation替代）
   - 第三梯队完成: 3/4 ✅（PEO Aviation×2/DSB/DSP Journal），WOSA原始标准待补充


## [2026-04-19 11:17] ingest | 第二梯队技术标准：CMOSS + SOSA + VICTORY
   - CMOSS: 32页，DEVCOM C5ISR Center，Universal A-Kit + 共享资源 + 共享服务
   - SOSA: 214页，The Open Group联盟，传感器开放系统架构Edition 1.0 V2 Snapshot
   - VICTORY: 案例研究+GVA对比，车辆C4ISR/EW互操作性
   - OMS 2024概述: PDF损坏无法提取（19页）
   - PEO Aviation FACE TIM: PDF损坏无法提取
   - 第二梯队完成3/4（OMS待用户提供可用PDF）


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
---

## 2026-04-19 — 最后一篇：PPI需求质量度量

**操作**：处理知识库最后一个未处理PDF

**新建source页（1个）**：
- `ppi-requirements-quality-metrics` — Halligan需求质量度量体系（1993/2017，6页）
  - 十大质量因子：正确性/完整性/一致性/清晰性/无歧义性/连通性/单一性/可测试性/可修改性/可行性
  - 需求结构模板：7元素解析法（主体/条件/动作/对象/约束/精化）
  - 产品度量：IRQ + IQF1-10 + RQ
  - 过程度量：RSTA/RTBD/RCOM/RAPP/RALL
  - 三种完整性估计法 + 历史基准需求量（商务机2500-4500、客机8000-10000等）

**更新cross-reference（1处）**：
- `requirements-quality-mosa` — 添加对新source页的wikilink

**最终状态**：raw/papers 全部55个PDF处理完成，0个待处理

---

## 2026-04-23 — 补充topics和entities

**操作**：根据overview.md待填补清单，创建3个topic和4个entity

**新增Topics**：
1. [[mosa-software-acquisition]] — DoDI 5000.87路径下MOSA在软件采办中的实施（DevSecOps、开放接口、数据权利）
2. [[middle-tier-acquisition-mosa-tension]] — MTA与MOSA的速度vs模块化政策张力（GAO数据、两种观点、解决方案）
3. [[digital-engineering-tools-comparison]] — MBSE工具和数字孪生平台对比（MagicDraw/Capella/Rhapsody、AFSIM/Ansys）

**新增Entities**：
1. [[dod-department-of-defense]] — DoD在MOSA中的三重角色（政策制定者/最大客户/标准推动者）
2. [[the-open-group]] — SOSA/FACE标准联盟（商业标准vs政府标准、争议）
3. [[nato]] — 联盟互操作标准（STANAG体系、与DoD MOSA的核心差异）
4. [[gao]] — 国会监察机构（年度武器评估、MOSA合规审计建议）

**更新**：
- index.md：添加7个新页面链接
- overview.md：更新待填补清单、统计数字（76→83页）

**未执行**（用户要求）：不更新README，不推送Gitee

---

## [2026-04-26] ingest | MOSA国防应用案例批量摄取
- 原始资料下载: 9份（GAO-25-106931, NDAA 2020/2021, CRS IF12094, DFARS RFI, NDIA白皮书, ABA文章, Curtiss-Wright, MITRE DEWS）
- Source页创建: 9个
- Entity页创建: 3个（Northrop Grumman, Lockheed Martin, SDA）
- Concept页创建: 3个（DEWS RA, Brownfield挑战, 五大支柱评估）
- Comparison页创建: 2个（SiAW vs AARGM-ER, 实施状态矩阵）
- 来源: GAO-25-106931深度调研14个JSON结果

## [2026-04-26] update | GAO-25-106931 PDF全文摄取
- 用户提供GAO-25-106931 PDF原文（6.2MB, 74页）
- mutool转换为文本（155KB, 4165行）
- 原始PDF保存: raw/papers/gao-25-106931-mosa-review.pdf
- 转换文本保存: raw/articles/gao-25-106931-mosa-review-full.txt
- 更新: sources/gaor-25-106931-mosa-review.md — 补充完整Table 1数据（20项目状态）和14条建议全文
- 更新: comparisons/mosa-implementation-status-matrix.md — 修正sources引用和日期

## [2026-04-26] fix | 断链修复 + 补充资料 + SCHEMA更新
- 断链修复: 6个raw文章从JSON创建, 1个引用路径修正(.md→.pdf)
- 补充资料: sosa-updated-standards-afcea.md, sosa-2025-special-edition.md, f35-tr3-lockheed-update.md
- .mil域名拦截: NAVAIR/DOT&E/AFMC/SAM.gov均不可达, ABMS/JADC2暂时无法获取
- SCHEMA.md: 洞察综合步骤增加原始资料缺口分析(断链检查+知识空白+可补充vs政策空白)

## [2026-04-26] ingest | 用户提供5份.mil域名PDF补充资料
- 来源: 用户手动下载的被拦截.mil/.gov页面PDF
- PDF保存: raw/papers/ (navair-mosa-overview, dote-fy2024-abms, afmc-abms-article, sam-abms-baa, mitre-dews-mosa-ra)
- 新增raw文章: 5个
- 新增source页: 5个 (navair-mosa-overview, dote-fy2024-abms, afmc-abms-distributed-connectivity, sam-abms-baa, mitre-dews-mosa-ra-full)
- 更新concept页: dews-mosa-reference-architecture.md (从幻灯片升级为完整文档)
- 洞察: ABMS核心问题是CBC2软件不成熟而非架构问题; 海军有MOSA战略但无正式指南; DEWS RA全文含完整数据模型

## [2026-04-26] ingest | NAVAIR MOSA生态补充（5个来源 + 3个PDF OCR）

**新增来源：**
- 三军联合备忘录 (2024.12) — Nickolas Guertin等三军部长联合签署，MOSA强制化标志
- 海军MOSA实施指南V1.0 — 海军定制版，含网络安全集成和企业推广策略
- NAVAIR HOST 5.0发布新闻 (2023.2) — HOST标准官方发布
- Defense News评论文章 (2024.12) — Guertin署名，MOSA→作战能力叙事转变
- Military Embedded报道 (2025.8) — 海军OSMP内生化

**新增页面：**
- entities: nickolas-guertin, pma-209
- concepts: host-hardware-open-systems
- comparisons: six-validated-mosa-standards
- sources: 5个新source页

**洞察：**
1. 三军备忘录首次在最高政策层面确认6大标准（OMS/UCI, SOSA, AMS GRA, WOSA, FACE, VICTORY），AMS GRA此前wiki未覆盖
2. WOSA在备忘录中被定义为武器系统接口标准（非工具），需更新现有概念页
3. 海军OSMP内生化是MOSA从"外包文档"到"内生能力"的标志性转变
4. HOST是NAVAIR自研硬件标准，与6大标准互补而非重叠

**待补：**
- WOSA概念页需更新（从工具描述改为标准描述）
- AMS GRA可考虑新建概念页

---

## [2026-04-29] ingest | PEO Aviation PDF替换：Industry Day 2022 + FACE TIM 2021

**操作**：处理2个PEO Aviation PDF（替换此前损坏的版本）

**更新source页（1个）**：
- `peo-aviation-mosa-industry-2022.md` — 更新sources引用指向正确PDF（`PEO_Aviation_MOSA_TO_Industry_Days_2022.pdf`），大幅扩展摘要内容（新增EAF/EPA/CSM/MCC/EPS/AMCE/CDC详细描述），补充交叉引用

**新建source页（1个）**：
- `peo-aviation-face-tim-2021.md` — PEO Aviation FACE TIM 2021开放系统演示（56页，20家公司+9个DoD组织+29个软件产品+8个TSS产品的大规模FACE集成演示）

**更新index.md**：
- 新增 `peo-aviation-face-tim-2021` 条目
- 更新 `peo-aviation-mosa-industry-2022` 描述

**POST-INGEST检查清单**：
- [x] entities/ — 无新核心实体（PEO Aviation已在多个页面中引用，无需独立实体页）
- [x] concepts/ — FACE TIM 2021暴露的概念（TSS桥接、容器适航性、多版本FACE互操作）已由现有`face-technical-standard`概念覆盖
- [x] comparisons/ — 无新张力/演化需要创建（现有`c5isr-standards-convergence`已覆盖CMOSS/SOSA/CMOSS互操作主题）
- [x] topics/ — 无新跨来源综合需要（2个source均为PEO Aviation内部演示，已由现有主题覆盖）
- [x] overview.md — 非基础性文件，不改变大局观

**关键发现**：
- Industry Day 2022新PDF比旧版内容更完整：新增EPS CSM、AMCE架构、通信模块化路线图、CSM开发挑战详细反馈
- FACE TIM 2021是FACE生态最大规模集成演示的完整技术文档，此前因PDF损坏无法处理
- 两个PDF互为补充：Industry Day侧重业务/治理/框架，FACE TIM侧重技术集成/实现

## [2026-04-29] ingest | 数字工程补充材料：NASA手册×4 + FY24 S&T + Chris Garrett

**操作**：处理6个新增PDF（用户"补充资料.zip"），覆盖NASA数字工程框架、空军数字化转型

**新建source页（6个）**：
- `nasa-hdbk-7009a.md` — NASA建模与仿真手册HDBK-7009A（157页，M&S全生命周期管理、V&V体系、置信度评估框架）
- `nasa-hdbk-1004.md` — NASA数字工程采办框架HDBK-1004（217页，DRD模板、合同语言、MBE计划、互操作性要求）
- `nasa-hdbk-1009a.md` — NASA系统建模手册HDBK-1009A Rev A（88页，SysML元模型、SE引擎对齐、MBSE Grid架构）
- `ieee-nasa-de-journey-2024.md` — IEEE NASA数字工程转型之旅（18页，MBSE部署692用户、工具链集成经验）
- `fy24-st-terms-of-reference.md` — FY2024 DAF SAB S&T审查职权范围（6页，CCA/定向能/频谱战主导权）
- `chris-garrett-presentation-2024.md` — Chris Garrett AFMC数字化转型演示（19页，DMM/GRA/MBSE模型库/数字生态系统）

**更新index.md**：新增6个条目

**POST-INGEST检查清单**：
- [x] entities/ — Chris Garrett (AFMC数字化转型主任) 可考虑创建实体页，但目前仅1个来源提及，不满足阈值
- [x] concepts/ — NASA数字工程框架(7009A/1004/1009A)形成完整体系，可考虑创建综合概念页，但需更多来源支撑
- [x] comparisons/ — NASA vs DoD数字工程路径对比有潜力（NASA HDBK 1004 vs DoDI 5000.97），待后续综合
- [x] topics/ — 4个NASA手册可扩展 `digital-engineering-ecosystem` 主题，但需人工审阅后决定
- [x] overview.md — NASA数字工程体系的补充填补了"系统韧性量化"部分空白，待整体review后更新

**关键发现**：
- NASA HDBK 7009A/1004/1009A 形成完整的数字工程三层体系：M&S管理→采办框架→建模语言
- Chris Garrett演示揭示AFMC正在建立"数字生态系统"（Digital Ecosystem），与MOSA数字工程融合路径一致
- FY24 S&T Terms of Reference 聚焦CCA任务系统/定向能/频谱战，是MOSA在下一代武器系统中的应用场景
