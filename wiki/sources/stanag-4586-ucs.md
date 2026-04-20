---
title: "STANAG 4586 — NATO UAV控制系统标准接口（UCS）"
date: 2026-04-19
type: source_summary
source: raw/papers/stanag-4586-ucs.pdf
author: "NATO / Mário Monteiro Marques"
tags: [UCS, STANAG, 无人系统, 互操作性, NATO]
---

# STANAG 4586 — NATO UAV控制系统标准接口

## 文档概况
- **全称**：STANAG 4586 – Standard Interfaces of UAV Control System (UCS) for NATO UAV Interoperability
- **来源**：NATO标准化协议 + 分析文章（作者：Mário Monteiro Marques, Escola Naval, Portugal）
- **页数**：14
- **MOSA提及**：间接相关——UCS是MOSA标准生态的组成部分

## 核心内容

STANAG 4586定义了NATO UAV控制系统（UCS）的**标准接口**，使不同厂商的无人机系统能够互操作。

### UCS架构
- 定义了UAV控制站与UAV之间的标准接口
- 支持不同厂商UAV的即插即用
- 包含指挥控制、任务规划、载荷管理等接口

### 与MOSA的关系
UCS被多次引用为MOSA标准生态的组成部分：
- **SOSA**引用UCS/STANAG 4586作为传感器到平台接口的C2标准
- **CMOSS**概述中提到UCS作为无人系统指挥控制标准
- **DSP Journal 2020**将UCS列为MOSA关键标准之一

### 标准化层级
UCS是**NATO级别的标准**（而FACE/SOSA/CMOSS是美国DoD/行业标准），这使其成为MOSA国际扩展的重要桥梁。

## 对MOSA的意义

UCS填补了MOSA标准生态中**无人系统指挥控制**的空白：
- FACE = 航电软件
- SOSA = 传感器
- CMOSS = C5ISR通用套件
- VICTORY = 车辆
- MORA = 射频
- **UCS = 无人系统C2**

UCS的NATO标准化身份也证明了MOSA理念的国际影响力——不仅是美国DoD政策，也在NATO盟国中被采纳。

## 相关内容
- [[ucs-control-station]] — UCS概念详解
- [[open-mission-systems]] — OMS（美军无人系统标准）
- [[face-technical-standard]] — FACE标准
- [[sosa-reference-architecture-v2]] — SOSA（引用UCS）
- [[mosa-defense-acquisition]] — MOSA概念

---
*14页。MOSA标准生态中UCS组件的入门文档。*
