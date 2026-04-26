---
title: "OUSD(R&E) MOSA五大支柱评估框架"
created: 2025-04-26
updated: 2025-04-26
type: concept
tags: [MOSA, 评估标准, OUSD, 五大支柱, 合规认证, 采办政策]
sources:
  - /root/mosa-defense-applications/results/OUSD_RE_MOSA评估标准.json
  - /root/mosa-defense-applications/results/MOSA实施状态矩阵.json
---

# OUSD(R&E) MOSA五大支柱评估框架

## 概述

OUSD(R&E)（研究与工程副国防部长办公室）系统工程与架构（SE&A）部门于2022年5月建立了MOSA五大支柱评估框架，为评估国防采办项目是否充分实施MOSA提供了结构化标准。2025年2月，DoD发布了最新版MOSA实施指南手册，进一步推进了框架的落地。该框架是目前最权威的MOSA评估方法论，但尚未形成统一的强制性合规评分卡。

## 要点

### 五大支柱定义

1. **模块化架构（Modular Architecture）**
   - 系统分解为高度内聚、松散耦合的模块
   - 支持独立开发、测试和替换
   - 模块可分割，支持竞争性采购

2. **开放接口（Open Interfaces）**
   - 基于广泛接受的共识标准定义
   - 接口可验证合规性
   - 支持即插即用能力

3. **开放标准（Open Standards）**
   - 使用公开可用、共识驱动的标准
   - 促进组件复用和供应商竞争
   - 相关标准包括：[[sosa-reference-architecture-v2]]、[[cmoss-overview-2022]]、[[face-technical-standard]]、OMS、MORA、UCI

4. **使能环境（Enabling Environment）**
   - MBSE工具链支持
   - 配置管理
   - DevSecOps流程
   - 数字工程与MOSA架构设计深度结合

5. **合规认证（Compliance Certification）**
   - 通过验证确保组件满足接口标准规范
   - 各军种实施程度不一
   - **缺乏统一的MOSA合规认证流程**——这是当前最大的系统性缺陷之一

### 框架的局限性

根据 [[gaor-25-106931-mosa-review]] 和框架本身的特点：

- **无统一评分卡** — 五大支柱提供了评估维度，但未形成量化的强制性合规评分方法
- **MTA路径空白** — 中间层采办（MTA）路径的DOD政策未明确涵盖MOSA要求
- **成本效益分析缺失** — 20个受审项目中无一进行正式MOSA成本效益分析，评估标准本身也未包含标准化成本效益分析方法论
- **PEO协调不足** — 9个受审PEO中仅2个有正式跨项目MOSA协调流程
- **资源评估缺失** — 军种未评估MOSA所需资源和专业需求

### 军种实施差异

| 军种 | MOSA实施率 | 指南状况 |
|------|-----------|---------|
| 陆军 | 100%（6/6） | 有全面指南手册 |
| 太空军 | 75%（3/4） | 有部分指南 |
| 海军 | 50%（2/4） | **无MOSA指南手册** |
| 空军 | 40%（2/5） | 有部分指南，未覆盖所有项目 |

### 政策演进时间线

- 2019年1月 — 三军MOSA备忘录（宣布MOSA为作战要素）
- 2022年5月 — OUSD(R&E) MOSA评估标准初版
- 2025年2月 — DoD MOSA实施指南手册
- 2025年11月 — 采办转型战略指示建立PEO级MOSA协调机制

### 与IP数据权利的关系

FY2021 NDAA Sec 804授予政府模块化系统接口数据的政府目的权利（GPR）。IP Cadre提供专业建议。评估标准要求在MOSA架构中明确IP策略，但缺乏标准化评估方法论。参见 [[dodi-5000-85-2020]]。

## 相关内容

- [[gaor-25-106931-mosa-review]] — GAO MOSA专项审查报告（直接评估五大支柱实施状况）
- [[mosaic-modular-open-systems-approach]] — MOSA总体方法论
- [[dodi-5000-85-2020]] — DoDI 5000.85 重大能力采办
- [[mosa-implementation-status-matrix]] — 20项目MOSA实施状态矩阵
- [[siaw-aargm-er-mosa-contrast]] — 军种间MOSA实施不一致的典型案例
- [[dews-mosa-reference-architecture]] — DEWS参考架构的五大愿景目标与五大支柱对应
- [[sosa-reference-architecture-v2]] — 开放标准支柱的具体体现
- [[cmoss-overview-2022]] — 开放标准支柱的具体体现
- [[gao-24-106831-weapon-systems]] — GAO武器系统总体报告

## 笔记

五大支柱评估框架的核心价值在于提供了一个结构化的思考维度，但其最大的问题恰恰在于**缺乏强制执行力**。GAO-25-106931报告的14项建议直接回应了这一缺陷——建议DoD制定统一的MOSA合规认证流程、建立标准化成本效益分析方法论、要求PEO建立跨项目MOSA协调机制。值得注意的是，维护成本约占武器系统全寿命周期成本的70%，五大支柱框架的长期价值在于通过模块化设计降低这一成本，但短期内缺乏量化证据支撑这一假设。
