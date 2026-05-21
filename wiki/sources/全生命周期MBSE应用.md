---
title: "全生命周期MBSE应用 — SPEC Innovations 30年实践"
created: 2026-05-20
updated: 2026-05-21
type: source
tags: [MBSE, 系统工程, 方法论, LML, INCOSE, MBSE in Practice 2025, 语义本体, SysML, Innoslate, MOSA]
sources: [MBSE in Practice Conference 2025, SEI]
confidence: VERIFIED
evidence: "从SPEC Innovations Steven Dam博士演讲原文深度提取"
---

# 全生命周期MBSE应用 — SPEC Innovations 30年实践

## 摘要

SPEC Innovations创始人Steven H. Dam博士回顾30年MBSE工程实践的演讲。核心主张：**MBSE ≠ SysML**——MBSE概念可追溯至1960年代，第一个真正的MBSE方法论来自TRW的SREM（1969）。2007年INCOSE正式定义MBSE后，工具从RDD-100 → Vitech Core/Genesys → 云原生Innoslate演进。Dam提出：MBSE需要一个基于**系统工程语义的数据库工具**才能有效，为此创建了LML（Lifecycle Modeling Language）——一套简化的语义本体。

## 来源

- **作者:** Steven H. Dam, Ph.D., ESEP — SPEC Innovations创始人
- **会议:** MBSE in Practice Conference 2025, August 21, SEI
- **机构:** SPEC Innovations — 1993年成立，参与NCES、陆军未来作战系统（FCS）等重大国防项目

## 核心论点：MBSE ≠ SysML

Dam提出了一系列颠覆性观点，挑战了将MBSE等同于SysML的普遍认知：

### MBSE的历史远早于SysML

- **MBSE概念可追溯至1960年代**，远在OMG定义SysML之前
- 第一个真正的MBSE方法论来自TRW的**SREM（Software Requirements Engineering Methodology, 1969年）**
- SREM证明：在没有图形建模语言的时代，基于数据库的工程方法已经可以实现MBSE的核心理念

### SysML的局限性

- SysML只是MBSE的**一种建模语言**，不是MBSE本身
- 仅有建模语言而不具备支持系统工程语义的数据库工具，MBSE效果大打折扣
- Dam的观点：MBSE需要的是"系统工程语义驱动的数据库"，而非仅是"画图的工具"

### 实际需求：基于语义的公共语言

2011年NASA首席工程师Ryschkewitsch提出：系统工程工具的**可扩展性需求**意味着必须引入云计算。Dam延伸了这一观点——MBSE需要一个基于系统工程语义的公共语言，而非各自为政的私有格式。这直接催生了LML。

## LML（Lifecycle Modeling Language）语义本体

### 设计哲学

LML不是另一种图形建模语言，而是一套**简化的语义本体**，可以映射到DoDAF、UAF、SysML、BPMN等多种框架和语言。其核心设计理念是：用最少的核心概念覆盖系统工程全生命周期的信息需求。

### 12个核心类（名词）

| # | 类 | 含义 | 典型实例 |
|---|----|------|---------|
| 1 | **Action** | 行动/活动 | 测试、集成、评审 |
| 2 | **Artifact** | 制品 | 文档、代码、模型 |
| 3 | **Asset** | 资产 | 硬件、软件、设施 |
| 4 | **Characteristic** | 特性 | 性能参数、质量属性 |
| 5 | **Connection** | 连接 | 接口、数据流、物理连接 |
| 6 | **Cost** | 成本 | 开发成本、运维成本 |
| 7 | **Decision** | 决策 | 里程碑评审、权衡决策 |
| 8 | **Input/Output** | 输入/输出 | 数据、信号、物料 |
| 9 | **Location** | 位置 | 地理、组织、架构层 |
| 10 | **Risk** | 风险 | 技术风险、进度风险 |
| 11 | **Statement (Requirement)** | 陈述/需求 | 功能需求、性能需求 |
| 12 | **Time** | 时间 | 里程碑、持续时间 |

### 双向关系（动词）

所有12个核心类通过**双向关系**（动词）连接，形成语义网络。关系是可扩展的，2015年已为SysML提供了语义本体映射。

### 设计优势

- **简洁性**：12个核心类比SysML/UAF的上百个元类更易学习和使用
- **映射能力**：可映射至DoDAF视图、SysML图、BPMN流程
- **可扩展性**：语义本体可在不破坏核心结构的前提下扩展
- **工具中立性**：LML本体可与多种工具生态对接

## 工具演进路径：从SREM到Innoslate

| 时期 | 工具/方法论 | 关键特点 | 国防应用 |
|------|-----------|---------|---------|
| 1969-1990s | **SREM → RDD-100** | 第一个真正MBSE方法论，基于需求驱动的数据库 | TRW项目 |
| 1990s-2010s | **Vitech Core / Genesys** | 桌面应用，成为国防项目主流工具 | NCES, FCS |
| 2011-至今 | **Innoslate** | 云原生，语义本体驱动，LML为核心 | 全生命周期MBSE |

### Innoslate的关键创新

- **云原生架构**：响应NASA对可扩展性的需求
- **LML语义本体驱动**：12个核心类 + 双向关系
- **多框架支持**：DoDAF、UAF、SysML、BPMN
- **全生命周期覆盖**：从需求到运维的端到端可追溯性

## 对MOSA的意义

LML的语义本体方法为MOSA的**模块化接口定义**提供了可移植的形式化基础：

- **接口作为Connection类**：MOSA的关键接口可在LML中作为Connection的本体实例，携带特征（Characteristic）描述性能、风险（Risk）描述集成风险、需求（Statement）描述合规要求
- **跨框架映射**：LML到DoDAF/UAF/SysML的映射意味着MOSA接口定义可以在不同框架间无损转换——这在多供应商、多军种的MOSA生态中至关重要
- **可自动验证**：如果MOSA接口能用语义本体（而非仅文档）定义，模块间的互操作性可被工具自动验证——这与SysML v2的API原生、机器可读方向高度一致
- **全生命周期追溯**：LML的全生命周期覆盖（Time类 + Artifact类）使MOSA模块从设计到退役的接口演化历史可以被追踪和审计
