---
title: "NAVAIR OSMP Implementation Description Guide v1.0"
source_type: official_guide
source_org: "NAVAIR (Naval Air Systems Command)"
source_url: "https://www.navair.navy.mil/sites/g/files/jejdrs536/files/document/OSMP%20Implementation%20Description%20Guide%20v1.0%202025.pdf"
date: 2025
distro_statement: "SPR-2025-0350, Distribution A"
downloaded: 2026-05-06
tags:
  - OSMP
  - MOSA
  - NAVAIR
  - Navy
  - open-architecture
  - acquisition
  - ICD
  - FACE
  - OMS
  - SOSA
  - WOSA
  - UCI
  - AMS-GRA
related_pages:
  - "[[open-architecture-hierarchy]]"
  - "[[osmp]]"
  - "[[mosa]]"
  - "[[navair]]"
  - "[[face]]"
  - "[[oms]]"
  - "[[sosa]]"
  - "[[wosa]]"
data_quality: high
---

# NAVAIR OSMP Implementation Description Guide v1.0 (2025)

## 核心内容

- **OSMP** = Open Systems Management Plan（开放系统管理计划）
- 本文档是 NAVAIR 面向其武器系统组合推广 MOSA 方法的官方实施指南
- **OSMP 是海军实现 MOSA 的蓝图**，将采购策略与成本优化、增加竞争和长期可持续性目标对齐
- 文档版本：v1.0，基准化后经多轮审查（v.16 → v.18 → v.2）
- DID 参考：DI-MGMT-82099 Rev. A OSMP
- 关联政策：2024年12月 **Navy MOSA Guidebook**（ASN(RDA) 发布）

### OSMP 的定位

- 关键的**项目管理工具**和**合同交付物**
- 政府起草初始 OSMP，覆盖关键业务和技术目标
- 提案阶段：用于源选评估的目标版本
- 合同签订后：承包商在关键里程碑交付更新版本，需政府同意
- 全生命周期的**协作"活文档"**

### NAVAIR MOSA 流程框架（5个阶段）

| 阶段 | 名称 | 内容 |
|------|------|------|
| 1 | Business Model & Architecture Decomposition | 系统分解为模块化、可替换单元 |
| 2 | Key Interfaces | 定义模块间交互点（硬件、软件、数据格式） |
| 3 | Interface Repository & MSI | 中央存储库，存储接口定义、版本历史、使用指南 |
| 4 | Standards Compliance | 使用 OMS, UCI, AMS-GRA, FACE, SOSA, WOSA, POSIX 等标准 |
| 5 | Verification & Validation Testing (VVT) | 独立测试确保模块符合开放标准 |

### 三种设计方法对比

| 方法 | 特点 |
|------|------|
| Extensive MOSA（广泛MOSA） | 完全模块化，最高灵活性、互操作性和可升级性 |
| Selective MOSA（选择性MOSA） | 针对性模块化，平衡灵活性与成本 |
| Proprietary/Non-Modular | 供应商锁定，高生命周期成本，最低灵活性 |

### 缩略词表（精选关键术语）

| 缩略词 | 含义 |
|--------|------|
| AMS-GRA | Agile Mission Suite – Government Reference Architecture |
| FACE | Future Airborne Capability Environment |
| MSI | Modular Systems Interface |
| OMS | Open Mission Systems |
| OSMP | Open Systems Management Plan |
| OSMPA | Open Systems Management Plan Data Item Description |
| SOSA | Sensor Open Systems Architecture |
| UCI | Universal Command and Control Interface |
| WOSA | Weapon Open Systems Architecture |
| BDFD | Business-Driven Functional Decomposition |
| MOSAACQ | Modular Open Systems Approach to Acquisition |
| TRF | Technical Reference Framework |

### 文档结构

1. NAVAIR MOSA Process Framework 简介
2. MOSA 基础与 OSMP 链接
3. OSMP 定义
4. NAVAIR OSMP 流程框架
5. OSMP 与 DoD 5000 框架的战略对齐
6. 提案评估与合同授予指南
7. OSMP 关键业务和技术驱动因素
8. 总结
9. 附录 A：MOSA 实施常见错误
10. 附录 B

## 关键人员

| 姓名 | 职位 |
|------|------|
| Rich Ernst | NAVAIR, 原始创建者 |
| Dr. Steven Davidson | DASN/MITR |
| T. Naugle, M. Beaulieu, F. Ahmad, P. Wingate | NAVAIR |

## 数据质量评估

- **来源**: NAVAIR 官方发布指南，Distribution A（公开）
- **限制**: 完整指南较详细，本文摘要涵盖主要框架；附录 A/B 需参考原文
- **价值**: 海军 MOSA 实施的权威指南，包含完整的 OSMP 流程框架和缩略词表

## 相关页面

- [[open-architecture-hierarchy]] — OSMP 是海军 MOSA 实施的顶层规划文档
- [[osmp]] — Open Systems Management Plan 详情
- [[mosa]] — Modular Open Systems Approach
- [[navair]] — Naval Air Systems Command
- [[face]] — Future Airborne Capability Environment
- [[oms]] — Open Mission Systems
- [[sosa]] — Sensor Open Systems Architecture
- [[wosa]] — Weapon Open Systems Architecture
