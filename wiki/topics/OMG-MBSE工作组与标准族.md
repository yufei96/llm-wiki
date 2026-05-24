---
title: "OMG MBSE 倡议：工作组与标准族"
type: topic
date: 2026-05-18
sources:
  - raw/articles/OMG-MBSE体系.md
  - raw/articles/OMG-MBSE体系.md
  - raw/articles/OMG-MBSE体系.md
  - raw/articles/OMG-MBSE体系.md
  - raw/articles/OMG-MBSE体系.md
  - raw/articles/OMG-MBSE体系.md
tags: [MBSE, systems-engineering, OMG, INCOSE, SysML]
---

# OMG MBSE 倡议：工作组与标准族

## 倡议概述

基于模型的系统工程（MBSE）是"建模的正式化应用，以支持系统需求、设计、分析、验证和确认活动，从概念设计阶段开始，贯穿开发和后续生命周期阶段"。

- **发起方**: INCOSE（国际系统工程委员会）+ OMG 系统工程 DSIG
- **主席**: Mark Sampson | **副主席**: Troy Peterson
- **始于**: 2007 年 INCOSE 国际研讨会

MBSE Initiative 通过 Challenge/Activity Teams 推进特定领域的 MBSE 实践。许多团队后来发展为 INCOSE 正式工作组。

## 工作组体系

MBSE Initiative 下设多个活动团队，覆盖 MBSE 实践的不同维度：

### 模型管理

关注模型的生命周期管理，后发展为 INCOSE Tool Integration and Model Lifecycle Management Working Group。

核心议题：
- 模型版本控制与配置管理
- 模型基线与变更管理
- 多工具环境下的模型一致性
- 模型库（Model Repository）架构

### 方法论与度量

关注 MBSE 实践中的方法学框架和效果度量，为组织采用 MBSE 提供指导。

核心议题：
- MBSE 方法论评估与比较
- MBSE 实践的量化度量指标
- 最佳实践的提炼与传播
- MBSE 成熟度模型

方法论为模型管理提供实践框架，度量为管理决策提供数据支撑——两者共同构成 MBSE 实践的"方法+管理"基础。

### 建模标准与互操作

关注系统工程领域建模语言和工具的标准化工作，主要成果：

- **SysML v1/v2** 规范
- **UPDM**（统一 Profile for DoDAF/MODAF）
- **Modelica** 物理建模语言
- **HLA**（高层架构）仿真互操作标准

建模仿真互操作挑战团队后发展为 [[DECO数字生态系统挑战团队]]，关注不同建模工具间的数据交换、异构模型集成与供应链模型互操作。

SysML v2 的 API & Services 规范直接解决了建模互操作问题——通过标准化接口实现工具间的模型导航、查询和更新。

### OMG-MBSE工作组与标准族（MBE）

MBE 宣言是 MBSE 理念在工程实践中的具体化表达，强调以模型作为工程活动的中心而非文档，为组织从文档驱动向模型驱动转型提供理论基础和行动指南。

## 标准族关系

```
MBSE Initiative (INCOSE + OMG)
├── SysML v1/v2 ──────── 系统建模语言
├── UPDM ─────────────── DoDAF/MODAF 建模规范
├── Modelica ─────────── 物理建模
├── HLA ──────────────── 仿真互操作
├── DECO ─────────────── 数字生态系统互操作
└── Tool Integration WG ─ 模型生命周期管理
```

## 价值主张

相比文档驱动方法，MBSE 预期提供：
- 提高生产力和质量
- 降低风险
- 改善开发团队间沟通


## MBSE实践大会来源

- [[MBSynergy场景化MBSE改进方法]]
- [[主动式网络安全威胁架构分析]]
- [[基于模型的安全关键系统保障]]
- [[MBSE定义DevSecOps能力成熟度]]
- [[初始架构分析]]
## 相关页面

- [[SysML过渡指南]] — SysML v1 到 v2 过渡路线
- [[DECO数字生态系统挑战团队]] — 数字生态系统互操作
- [[MBSE安全架构分析方法]] — 安全性与架构分析
- [[MBSE数字化转型路径]] — 组织转型实践
