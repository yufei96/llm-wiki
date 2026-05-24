---
title: "NASA系统工程手册 Rev2"
created: 2026-05-21
updated: 2026-05-21
tags: [NASA, 系统工程, 手册, SE引擎, 生命周期, 设计过程]
source: [raw/papers/NASA特别出版物2016-6105修订2.pdf, raw/articles/NASA特别出版物2016-6105修订2.md]
confidence: EXTRACTED
type: source
---

# NASA系统工程手册 Rev2

## 概述

NASA Systems Engineering Handbook Rev 2（NASA/SP-2016-6105 Rev2），NASA的**机构级系统工程标准**。不同于INCOSE SEH（行业通用）和DoDI 5000.02（采办框架），这是NASA为航天任务定制的系统工程实践指南。分为Part 1（过程指南）和Part 2（技术附录），是NASA SE的"圣经"级文档。

## 手册结构

### Part 1：系统工程项目管理

| 章节 | 内容 |
|------|------|
| **1. Introduction** | 目的、范围与深度 |
| **2. Fundamentals of SE** | SE引擎、通用技术过程、验证vs确认、成本效益、人因系统集成 |
| **3. NASA项目生命周期** | Phase A-F全生命周期（概念研究→退役）、预算周期、NPR 7123.1裁剪 |

### Part 2：系统设计过程（17个过程）

| 章节 | 过程 |
|------|------|
| **4.0** | 系统设计过程概述 |
| **4.1** | Stakeholder Expectations Definition（利益相关方期望定义） |
| **4.2** | Technical Requirements Definition（技术需求定义） |
| **4.3** | Logical Decomposition（逻辑分解） |
| **4.4** | Design Solution Definition（设计方案定义） |

### 技术管理过程

| 章节 | 过程 |
|------|------|
| **5.1** | Technical Planning（技术规划） |
| **5.2** | Requirements Management（需求管理） |
| **5.3** | Interface Management（接口管理） |
| **5.4** | Technical Risk Management（技术风险管理） |
| **5.5** | Configuration Management（配置管理） |
| **5.6** | Technical Data Management（技术数据管理） |
| **5.7** | Technical Assessment（技术评估） |
| **5.8** | Decision Analysis（决策分析） |

### 产品实现与评估

| 章节 | 过程 |
|------|------|
| **6.1-6.8** | 产品实现（采购、集成、验证、确认、转移） |
| **7.0** | 产品评估（Product Transition、Validation等） |

## NASA SE引擎

NASA手册的核心模型：**SE引擎**——一个迭代循环，包含三大过程组：
1. **系统设计过程**（4章）→ 从期望到设计
2. **技术管理过程**（8章）→ 规划、控制、评估
3. **产品实现过程**（6-7章）→ 从设计到产品

SE引擎按项目阶段（Phase A-F）递归运行，每个阶段深度递增。

## 与INCOSE SEH V5的异同

| 维度 | NASA SEH Rev2 | INCOSE SEH V5 |
|------|--------------|---------------|
| **定位** | 机构定制 | 行业通用 |
| **焦点** | 航天任务（发射、运行） | 全行业 |
| **生命周期** | NASA Phase A-F | ISO/IEC 15288 |
| **核心模型** | SE引擎 | 技术过程+协议过程 |
| **权威性** | NASA标准 | 行业共识 |

## 笔记

- NASA手册是HDBK-1009A（系统建模手册）和HDBK-1004（数字工程采办）的基础参考
- SE引擎模型是理解和实施MOSA的关键——MOSA的模块化设计必须在SE引擎的"逻辑分解"和"设计方案定义"阶段嵌入
- Rev2版本时间（2016年）早于DoD数字工程战略（2018年）——NASA是先驱
