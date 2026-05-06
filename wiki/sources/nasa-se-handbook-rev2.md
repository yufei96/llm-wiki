---
title: "NASA/SP-2016-6105 Rev 2 — NASA系统工程手册"
created: 2026-04-26
updated: 2026-04-26
type: source_summary
sources: [raw/papers/NASA-SP-2016-6105-Rev2.pdf]
author: "NASA (Linda Bromley, ed.)"
tags: [NASA, 系统工程, SE, 接口管理, 生命周期, V&V]
---

# NASA/SP-2016-6105 Rev 2 — NASA系统工程手册

## 文档概况
- **全称**：NASA Systems Engineering Handbook, Revision 2
- **编号**：NASA/SP-2016-6105 Rev 2
- **发布者**：NASA Headquarters
- **发布日期**：2016年（Rev 2）
- **页数**：~260页（含附录）
- **前版**：SP-6105 Rev 1（2007）、SP-6105（1995）

## 核心内容

### 结构
1. **引言** — 目的、范围
2. **系统工程基础** — SE引擎、通用技术过程、产品验证vs确认
3. **NASA项目生命周期** — Pre-Phase A 到 Phase F（概念研究→退役）
4. **技术过程** — 利益攸关方期望→技术需求→逻辑分解→设计解决方案→产品实现→产品集成→V&V
5. **技术管理过程** — TPM、风险管理、配置管理、技术数据管理、技术评估、决策分析
6. **交叉领域过程** — 接口管理、技术风险管理

### NASA项目生命周期阶段

- **Pre-Phase A**：概念研究
- **Phase A**：概念与技术开发
- **Phase B**：初步设计与技术完成
- **Phase C**：最终设计与制造
- **Phase D**：系统装配、集成与测试、发射
- **Phase E**：运行与保障
- **Phase F**：收尾

### SE引擎（核心框架）

SE引擎是一个迭代递归的过程框架，贯穿所有项目阶段：
1. 利益攸关方期望定义
2. 技术需求定义
3. 逻辑分解
4. 设计解决方案
5. 产品实现
6. 产品集成
7. 产品验证
8. 产品确认

## 接口管理（Section 6.3）— 与MOSA最相关

### 定义
接口管理是控制产品开发的过程，当工作由多方（政府、承包商、地理分散的技术团队等）分工时，定义和维护产品间的互操作性。

### 基本任务
- 定义接口
- 识别接口特征（物理、电气、机械、人机等）
- 确保所有定义接口的兼容性
- 在设计、建造、运行等阶段严格控制接口过程

### 接口控制文档
- **IRD**（Interface Requirements Document）— 接口需求文档
- **ICD**（Interface Control Document/Drawing）— 接口控制文档/图
- **IDD**（Interface Definition Document）— 接口定义文档
- **ICP**（Interface Control Plan）— 接口控制计划

### 接口工作组（IWG）
由接口各方的技术代表组成，负责接口活动的规划、调度和执行。

## 与MOSA的关系

### NASA接口管理 = MOSA接口规范的工程实践版
NASA的接口管理体系为MOSA提供了**经过验证的工程实践**：

| NASA接口管理 | MOSA对应 |
|-------------|----------|
| ICD（接口控制文档） | [[wosa-architecture-tools]] — WOSA接口标准 |
| IWG（接口工作组） | [[tri-service-memo-2024]] — 三军协调机制 |
| 接口特征定义（物理/电气/机械） | [[sosa-reference-architecture-v2]] — SOSA接口规范 |
| 接口变更控制 | [[mosa-five-pillars]] — 持续竞争的制度保障 |

### 关键差异
- NASA是**单一机构**内部的接口管理，MOSA是**跨军种/跨供应商**的接口标准化
- NASA强调**控制**，MOSA强调**开放**——但两者都需要严格的接口定义和变更管理

## 在知识库中的位置

本文档补充了系统工程实践层，与现有政策/标准层形成互补：

- [[iso-15288-2023]] — ISO/IEC/IEEE 15288（NASA SE的国际标准基础）
- [[incose-mbse-methodology-survey]] — INCOSE MBSE方法论调查
- [[digital-engineering-ecosystem]] — 数字工程生态系统
- [[wosa-architecture-tools]] — WOSA接口标准
- [[incose-se-handbook-v5]] — INCOSE SE Handbook V5（通用SE方法论，与NASA手册互补）
- [[three-se-handbooks-detailed-comparison]] — 三本SE手册详细对比

## 待补充

（无）

---

