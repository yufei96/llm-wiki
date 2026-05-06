---
title: "NIST SP 800-160 Vol. 2 Rev. 1 — 赛博弹性系统开发"
created: 2026-04-26
updated: 2026-04-26
type: source_summary
sources: [raw/papers/NIST.SP.800-160v2r1.pdf]
author: "Ron Ross, Victoria Pillitteri, Richard Graubart, Deborah Bodeau, Rosalie McQuaid (NIST/MITRE)"
tags: [NIST, 赛博弹性, 网络安全, 系统安全工程, MOSA, 架构设计]
---

# NIST SP 800-160 Vol. 2 Rev. 1 — 赛博弹性系统开发

## 文档概况
- **全称**：Developing Cyber-Resilient Systems: A Systems Security Engineering Approach
- **发布者**：NIST（作者含 MITRE 赛博弹性部门）
- **发布日期**：2021年12月
- **页数**：310页
- **DOI**：https://doi.org/10.6028/NIST.SP.800-160v2r1
- **配套文档**：SP 800-160 Vol. 1（系统安全工程）、SP 800-37（风险管理框架）、SP 800-53（安全控制）

## 核心概念

### 赛博弹性定义
赛博弹性工程（Cyber Resiliency Engineering）是一种新兴的专业系统工程学科，旨在**预见、承受、恢复和适应**利用赛博资源的不利条件、压力、攻击或妥协。

### 四大目标（Goals）

| 目标 | 描述 |
|------|------|
| **Anticipate（预见）** | 保持对逆境的知情准备状态，包括威胁情报、漏洞发现、供应链妥协 |
| **Withstand（承受）** | 在逆境中继续执行必要的任务或业务功能 |
| **Recover（恢复）** | 在逆境中或之后恢复任务或业务功能 |
| **Adapt（适应）** | 修改以对抗类似的未来逆境，调整运营模式 |

### 框架构造（Constructs）
赛博弹性工程框架包含五层构造，从"做什么"到"怎么做"：

1. **Goals（目标）**：Anticipate / Withstand / Recover / Adapt
2. **Objectives（子目标）**：14个子目标，如 Preparedness、Data Integrity、Mission Continuity 等
3. **Techniques（技术）**：22种技术，如 Architectural Diversity（架构多样性）、Redundancy（冗余）、Segmentation（分区）
4. **Implementation Approaches（实施方法）**：具体实现路径
5. **Design Principles（设计原则）**：指导设计决策的原则

## 赛博弹性设计原则

### 战略性设计原则（5项）
指导整个系统生命周期的工程分析和风险分析：

| 原则 | 关键思想 |
|------|----------|
| **聚焦关键公共资产** | 有限资源优先保护关键且公共的资产 |
| **假设已妥协** | 假设系统组件已被妥协，据此设计 |
| **考虑任务/业务影响** | 从任务影响角度评估弹性需求 |
| **预期和对抗对手** | 了解对手能力和战术 |
| **关注系统生命周期** | 弹性贯穿设计、开发、运维、维护全周期 |

### 结构性设计原则（11项）
直接影响系统架构和设计：

| 原则 | 关键思想 | 与MOSA的关系 |
|------|----------|-------------|
| **限制信任需求** | 减少需要信任的系统元素数量 | MOSA接口隔离降低信任域 |
| **控制可见性和使用** | 控制对手可发现和利用的内容 | 接口可见性控制 |
| **约束和排除行为** | 限制可执行的操作范围 | 模块边界隔离 |
| **分层防御和分区资源** | 纵深防御+资源分区 | MOSA模块化天然支持 |
| **规划和管理多样性** | 消除单点攻击或故障 | 多供应商模块替换 |
| **维护冗余** | 配置更新后保持冗余 | 备份模块/路径 |
| **使资源位置可变** | 避免单点故障 | 模块可部署性 |
| **利用健康和状态数据** | 支持态势感知和异常检测 | 模块健康监控接口 |
| **维持态势感知** | 感知性能趋势和异常 | 系统级监控 |
| **风险自适应资源管理** | 根据风险动态调整资源 | 动态模块配置 |
| **最大化瞬时性** | 使用瞬态系统元素减少暴露时间 | 容器化/无状态模块 |
| **持续确定可信度** | 定期验证数据和软件完整性 | 接口完整性校验 |

## 与MOSA的关系

### MOSA作为赛博弹性的架构基础
NIST SP 800-160 Vol. 2 的结构性设计原则与 MOSA 的模块化原则高度对齐：

| NIST原则 | MOSA对应 |
|----------|----------|
| 分层防御和分区资源 | [[modular-architecture-patterns]] — 模块化天然实现分区 |
| 规划和管理多样性 | [[mosa-five-pillars]] — 多供应商竞争 |
| 维护冗余 | [[wosa-architecture-tools]] — 备份接口/路径 |
| 限制信任需求 | [[cybersecurity-vs-mosa-openness]] — 接口隔离降低攻击面 |
| 使资源位置可变 | 模块可替换性 = 位置无关性 |

### MOSA安全性的新视角
传统MOSA讨论聚焦于**竞争和互操作性**，NIST SP 800-160 Vol. 2 补充了**安全性维度**：
- 开放接口 ≠ 不安全接口——通过**控制可见性**和**约束行为**可实现安全的开放
- 模块化 = **攻击面隔离**——妥协一个模块不等于妥协整个系统
- 多供应商 = **架构多样性**——消除单点供应链攻击

## 在知识库中的位置

本文档是**数字工程×MOSA安全性**的关键交叉点，补充了以下现有页面的安全性维度：
- [[cybersecurity-vs-mosa-openness]] — 赛博安全与MOSA开放性
- [[mosa-digital-engineering]] — MOSA与数字工程
- [[digital-engineering-ecosystem]] — 数字工程生态系统
- [[nist-cyber-resilience-mosa-security]] — NIST设计原则作为MOSA安全性架构框架
- [[nasa-se-handbook-rev2]] — NASA SE Handbook Rev 2（NASA的安全性工程实践）

## 关键引用

> "Cyber resiliency engineering intends to architect, design, develop, maintain, and sustain the trustworthiness of systems with the capability to anticipate, withstand, recover from, and adapt to adverse conditions, stresses, attacks, or compromises that use or are enabled by cyber resources."

> "Many of the structural design principles are consistent with or leverage the design principles for security and/or resilience."

## 待补充

- NASA SP-2016-6105 Rev 2（NASA SE Handbook）下载后补充系统工程实践细节
- OUSD(R&E) SysML v2 过渡指南下载后补充 MBSE→MOSA 建模方法

---

