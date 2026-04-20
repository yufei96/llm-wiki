---
title: "MOSA & 数防采办知识库总览"
created: 2026-04-20
updated: 2026-04-20
type: overview
---

# MOSA 与数字工程知识库总览

> 本知识库覆盖模块化开放系统方法（MOSA）在美国国防采办中的演化、数字工程生态系统、以及相关的技术标准和政策框架。
> 共76个wiki页面，覆盖45个一手来源。

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

核心工具：[[face-technical-standard]]、[[modular-architecture-patterns]]、MBSE方法论。

### 3. C5ISR标准生态

军用电子和传感器领域的模块化标准正在趋同（[[c5isr-standards-convergence]]）：

- **CMOSS**: 通用底盘+共享资源（DEVCOM）
- **SOSA**: 传感器开放系统架构（The Open Group）
- **VICTORY**: 车辆C4ISR互操作性
- **MORA**: 射频组件模块化
- **OMS**: 任务系统互操作性

这些标准独立发展但高度重叠，正在向统一框架演进。

### 4. 合同与法律框架

MOSA的实施落地依赖多层法律和合同工具：

- **法律层**: 10 USC §4401-4403（[[mosa-implementation-stack|全栈]]）
- **政策层**: DoDI 5000.85（MOSA法定要求）
- **合同层**: DFARS Part 252（数据权利条款）
- **执行层**: PPI DID模板（[[requirements-quality-mosa|需求质量]]是MOSA成败关键）

### 5. 国际化

MOSA从美国DoD扩展到联盟体系（[[mosa-internationalization]]）：
- NATO: STANAG 4586（UCS无人系统标准）
- UK/Australia/Canada: 已采纳MOSA原则
- 商业领域: Airbus HForce等案例验证了MOSA可行性

## 知识地图

| 层 | 文件夹 | 数量 | 功能 |
|----|--------|------|------|
| 来源 | sources/ | 45 | 一手文档摘要 |
| 概念 | concepts/ | 13 | 单一概念定义 |
| 实体 | entities/ | 6 | 组织/人物/政策 |
| 主题 | topics/ | 3 | 跨来源综合 |
| 对比 | comparisons/ | 9 | 演化/张力/趋同分析 |

## 待填补的空白

- **WOSA原始标准**: 已有工具链分析，缺少WOSA标准本身
- **OMS最新版**: PDF损坏，需可用来源
- **更多NATO标准**: 目前只有STANAG 4586
- **商业MOSA案例**: Airbus HForce之外的案例
- **MOSA成本效益数据**: GAO报告有框架但缺归因数据

## 相关内容

- [[mosa-defense-acquisition]] — MOSA核心概念
- [[mosa-five-pillars]] — MOSA五大支柱
- [[adaptive-acquisition-framework]] — DoD自适应采办框架
- [[digital-engineering-ecosystem]] — 数字工程生态系统概述
- [[c5isr-standards-convergence]] — C5ISR标准生态趋同
- [[mosa-implementation-stack]] — MOSA实施全栈
- [[mosa-internationalization]] — MOSA国际化

---

*本文件是知识库的"我现在知道什么"总览。每次摄取重大来源或发现新模式后更新。*
