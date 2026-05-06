---
title: "MOSA & 数防采办知识库总览"
created: 2026-04-20
updated: 2026-05-06
type: overview
---

# MOSA 与数字工程知识库总览

> 本知识库覆盖模块化开放系统方法（MOSA）在美国国防采办中的演化、数字工程生态系统、以及相关的技术标准和政策框架。
> 共约175个wiki页面，覆盖90+个一手来源。

## 核心故事线

### 1. MOSA：从理念到法律（2013-2025）

MOSA不是一个技术标准，而是一套**采办哲学**：通过模块化架构和开放接口，打破国防承包商锁定，促进竞争和创新。

- **2013**: OSA合同指南v1.1定义了MOSA五原则：[[mosa-five-pillars]]
- **2015**: [[better-buying-power-3-0]]首次将MOSA写入DoD政策
- **2017**: FY2017 NDAA Section 805将MOSA**法定化**
- **2019**: [[adaptive-acquisition-framework]]六条路径建立，MOSA在[[middle-tier-acquisition]]中不强制
- **2025**: MOSA实施指南发布五大支柱，覆盖[[digital-engineering-mosa-convergence]]

关键张力：速度vs模块化（[[speed-vs-modularity]]），紧急/MTA路径将速度优先于MOSA。

### 2. 数字工程生态系统（DEE）

DoD正在从文档驱动转向数据驱动的工程方法：

- **2018**: DoD数字工程战略确立5大目标
- **2023**: [[dodi-5000-97-digital-engineering]]将MOSA列为DEE九大要素之一
- **2024**: DSB报告确认MOSA是DEE的[[mosa-digital-engineering|技术基础]]
- **2024**: AFMC推出DMM框架（[[digital-materiel-management]]），GRA系统实现79个MIL文档→36个系统模型的数字化转换

**NASA三层DE实施体系**（[[nasa-de-implementation-system]]）：HDBK-1004（采办框架，217页）+ HDBK-1009A（系统建模，88页）+ HDBK-7009A（M&S质量管理，157页），构成全球最完整的DE操作框架——DoD有政策（DoDI 5000.97）但缺乏此类操作手册。

**CCA：MOSA的下一代大考**（[[collaborative-combat-aircraft]]）：1000+架无人作战飞机，2028年MTA路径首次列装，使用[[open-mission-systems|OMS]]框架，是MOSA在空中力量中最大规模的应用——极端的2028时间线与完整MOSA合规之间的张力（[[mosa-cca-application]]）将定义未来MOSA实施路径。

核心工具：[[face-technical-standard]]、[[modular-architecture-patterns]]、MBSE方法论。

### 3. C5ISR标准生态

军用电子和传感器领域的模块化标准正在趋同（[[c5isr-standards-convergence]]）：

- **CMOSS**: 通用底盘+共享资源（DEVCOM）
- **SOSA**: 传感器开放系统架构（The Open Group）
- **VICTORY**: 车辆C4ISR互操作性
- **MORA**: 射频组件模块化
- **OMS**: 任务系统互操作性

这些标准独立发展但高度重叠，正在向统一框架演进。

### 4. GRA生态：21种开放架构的四层体系

MOSA的架构层实现已从零散标准发展为完整的四层体系（[[open-architecture-hierarchy]]、[[gra-ecosystem-evolution]]）：

- **平台级**：OMS/UCI、UCS、ABMS GRA — 定义整个平台的任务系统架构
- **分系统级**：WOSA、DEWS RA、NC3 GRA、Sentinel GRA、CFW ICD — 定义功能分系统接口
- **设备级**：SOSA、MORA、CMOSS、VICTORY、AMS GRA、A-GRA、R-EGI、COARPS、SCARS — 定义设备/模块标准
- **部组件级**：FACE、HOST — 定义底层软硬件规范

MOSA已从航空（OMS/FACE）扩展到核力量（NC3/Sentinel）、PNT（R-EGI）、雷达（COARPS）、训练（SCARS）、自主（A-GRA）等6+个领域。CCA项目催生了"架构三件套"（AMS GRA + A-GRA + OMS），实现了跨平台自主算法竞争。

### 5. 合同与法律框架

MOSA的实施落地依赖多层法律和合同工具：

- **法律层**: 10 USC §4401-4403（[[mosa-implementation-stack|全栈]]）
- **政策层**: DoDI 5000.85（MOSA法定要求）
- **合同层**: DFARS Part 252（数据权利条款）
- **执行层**: PPI DID模板（[[requirements-quality-mosa|需求质量]]是MOSA成败关键）

### 6. 国际化

MOSA从美国DoD扩展到联盟体系（[[mosa-internationalization]]）：
- NATO: STANAG 4586（UCS无人系统标准）
- UK/Australia/Canada: 已采纳MOSA原则
- 商业领域: Airbus HForce等案例验证了MOSA可行性

### 7. SysML v2 与数字建模革命

SysML v2 (2024) 是建模语言的范式转换：文本化表示、API原生、8种图类型。OUSD RE 已发布过渡指导（FY2025试点→FY2028强制），NDIA 简报指出过渡是最大瓶颈。这对 MOSA 的意义：标准化建模语言使模块定义可移植、接口可验证。
参考: [[sysml-v2-specification]], [[ousd-sysml-v2-transition-guidance]], [[ndia-sysml-v2-transition-2023]], [[sysml-v2-transition-bottleneck]]

### 7. 系统工程手册三重奏

INCOSE SE Handbook V5、NASA SE Handbook Rev2、NIST SP 800-160 Vol 2 覆盖互补领域：INCOSE=全生命周期方法论、NASA=航天工程实践、NIST=赛博弹性专项。三者共同定义了系统韧性的完整框架。2026-04-29新增NASA四本手册：[[nasa-hdbk-1004]]（采办框架）、[[nasa-hdbk-1009a]]（SysML建模）、[[nasa-hdbk-7009a]]（M&S质量）、[[ieee-nasa-de-journey-2024]]（DE实施进展），形成NASA从流程→建模→质量管理→采办的完整实践体系。
参考: [[incose-se-handbook-v5]], [[nasa-se-handbook-rev2]], [[nist-sp-800-160-v2-cyber-resilience]], [[three-se-handbooks-complement]], [[three-se-handbooks-detailed-comparison]], [[nasa-hdbk-1004]], [[nasa-hdbk-1009a]], [[nasa-hdbk-7009a]], [[ieee-nasa-de-journey-2024]]

### 8. AFMC数字化转型与DMM

[[afmc|AFMC]]正在推动数字化物资管理（[[digital-materiel-management|DMM]]）框架，通过政府参考架构（[[government-reference-architectures|GRA]]）体系（79个MIL文档→36个系统模型）、MBSE模型库和数字生态系统（PLM/FENCES/CLOUDONE/PLATFORMONE）实现采办数字化。DMM与DoD层面的[[digital-engineering-ecosystem|DEE]]高度趋同但视角不同（[[dmm-vs-dee-convergence|对比分析]]）。DMM是AFMC级的DEE实施，NASA的[[nasa-de-implementation-system|三层DE实施体系]]则提供了另一条自下而上的路径。
参考: [[chris-garrett-presentation-2024]], [[chris-garrett]], [[digital-materiel-management]], [[government-reference-architectures]], [[nasa-de-implementation-system]]

### 9. AFRL S&T前沿：CCA、DEW、SWD

[[daf-sab|DAF SAB]] FY2024审查聚焦三大前沿技术领域：
- [[collaborative-combat-aircraft|协作作战飞机（CCA）]]：无人半自主作战飞机，计划1000+架，2028年列装，使用[[open-mission-systems|OMS]]框架——MOSA在下一代空中力量中最大规模的应用（[[mosa-cca-application|MOSA-CCA应用分析]]），面临速度（2028 MTA路径）vs 模块化（MOSA五大支柱）的极端张力
- 定向能武器（DEW）：高能激光/高功率微波，[[dews-mosa-reference-architecture|DEWS MOSA参考架构]]已有
- 频谱战主导权（SWD）：电磁频谱作战，认知自主性支持
参考: [[fy24-st-terms-of-reference]], [[daf-sab]], [[collaborative-combat-aircraft]], [[mosa-cca-application]]

## 知识地图

| 层 | 文件夹 | 数量 | 功能 |
|----|--------|------|------|
| 来源 | sources/ | 74 | 一手文档摘要 |
| 概念 | concepts/ | 27 | 单一概念定义 |
| 实体 | entities/ | 21 | 组织/人物/政策 |
| 主题 | topics/ | 11 | 跨来源综合 |
| 对比 | comparisons/ | 18 | 演化/张力/趋同分析 |

## 待填补的空白

- **WOSA原始标准**: 已有工具链分析，缺少WOSA标准本身
- **OMS最新版**: PDF损坏，需可用来源
- **更多NATO标准**: 目前只有STANAG 4586，需补充STANAG 4694/5602
- **商业MOSA案例**: Airbus HForce之外的案例（已创建entities框架，待补充PDF）
- **MOSA成本效益数据**: GAO报告有框架但缺归因数据
- **entities完整度**: 需补充主要承包商实体页
- **SysML v2实证数据**: 过渡指导刚发布，需跟踪FY2025试点结果
- **系统韧性量化**: 三本手册提供了框架但缺少可操作的量化指标

## 相关内容

- [[mosa-defense-acquisition]] — MOSA核心概念
- [[mosa-five-pillars]] — MOSA五大支柱
- [[adaptive-acquisition-framework]] — DoD自适应采办框架
- [[digital-engineering-ecosystem]] — 数字工程生态系统概述
- [[c5isr-standards-convergence]] — C5ISR标准生态趋同
- [[mosa-implementation-stack]] — MOSA实施全栈
- [[mosa-internationalization]] — MOSA国际化
- [[model-based-systems-engineering]] — 基于模型的系统工程
- [[system-resilience-engineering]] — 系统韧性工程
- [[digital-engineering-practice]] — 数字工程实践
- [[digital-materiel-management]] — 数字化物资管理（DMM）
- [[collaborative-combat-aircraft]] — 协作作战飞机（CCA）
- [[government-reference-architectures]] — 政府参考架构
- [[dmm-vs-dee-convergence]] — DMM与DEE趋同分析
- [[nasa-de-implementation-system]] — NASA三层DE实施体系
- [[mosa-cca-application]] — MOSA在CCA中的应用
- [[open-mission-systems]] — 开放任务系统（OMS）

---

*本文件是知识库的"我现在知道什么"总览。每次摄取重大来源或发现新模式后更新。*
updated: 2026-04-29
共154个wiki页面，覆盖74个一手来源。
来源 | sources/ | 74 | 一手文档摘要 |
