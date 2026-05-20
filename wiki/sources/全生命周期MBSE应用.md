---
title: "全生命周期MBSE应用 — SPEC Innovations 30年实践"
created: 2026-05-20
updated: 2026-05-20
type: source
tags: [MBSE, 系统工程, 方法论, LML, INCOSE, MBSE in Practice 2025]
sources: [MBSE in Practice Conference 2025, SEI]
confidence: VERIFIED
evidence: "从SPEC Innovations Steven Dam演讲原文提取"
---

# 全生命周期MBSE应用 — SPEC Innovations 30年实践

## 摘要

SPEC Innovations 创始人 Steven H. Dam 回顾 30 年 MBSE 工程实践。核心主张：**MBSE ≠ SysML**——MBSE 概念可追溯至 1960 年代，第一个真正的 MBSE 方法论来自 TRW 的 SREM（1969）。2007 年 INCOSE 正式定义 MBSE 后，工具从 RDD-100 → Vitech Core/Genesys → 云原生 Innoslate 演进。

## 来源

- **作者:** Steven H. Dam, Ph.D., ESEP (SPEC Innovations)
- **会议:** MBSE in Practice Conference 2025, August 21, SEI
- **机构:** SPEC Innovations — 1993 年成立，参与 NCES、陆军未来作战系统等重大国防项目

## 关键要点

### MBSE ≠ SysML

- SysML 只是 MBSE 的一种建模语言，不是 MBSE 本身
- MBSE 需要一个基于系统工程语义的数据库工具才能有效
- SPEC 为此创建了 **LML（Lifecycle Modeling Language）**——一套简化的语义本体，映射到 DoDAF、UAF、SysML、BPMN

### LML 本体设计

- 12 个核心类（名词）：Action, Artifact, Asset, Characteristic, Connection, Cost, Decision, Input/Output, Location, Risk, Statement(Requirement), Time
- 双向关系（动词）连接所有类
- 可扩展，2015 年已为 SysML 提供语义本体

### 工具演进路径

| 时期 | 工具 | 特点 |
|---|---|---|
| 1969-1990s | SREM / RDD-100 | 第一个真正 MBSE 方法论 |
| 1990s-2010s | Vitech Core / Genesys | 桌面应用，国防项目主流 |
| 2011-至今 | Innoslate | 云原生，语义本体驱动 |

### 全生命周期需求

- 2011 年 NASA 首席工程师 Ryschkewitsch 提出：SE 工具的**可扩展性需求**意味着必须引入云计算
- 关键洞察：MBSE 需要一个基于系统工程语义的公共语言

## 对 MOSA 的意义

LML 的语义本体方法为 MOSA 的**模块化接口定义**提供了可移植的形式化基础。如果 MOSA 接口能用语义本体（而非仅文档）定义，模块间的互操作性可被工具自动验证。这与 SysML v2 的 API 原生、机器可读方向高度一致。

## 相关内容

- [[wiki/concepts/基于模型的系统工程|MBSE]]
- [[wiki/topics/SysML v2过渡瓶颈|SysML v2过渡瓶颈]]
- [[wiki/topics/数字工程实践|数字工程实践]]
