---
title: "MOSA在CCA中的应用：模块化开放系统方法与协作作战飞机"
created: 2026-04-29
updated: 2026-04-29
type: comparison
tags: [MOSA, CCA, OMS, 模块化, 采办, 速度, 模块化, MTA, 无人作战飞机]
sources: [raw/papers/FY24_ST_ToRs_-_for_public_release.pdf, raw/articles/FY24_ST_ToRs_-_for_public_release.md]
---

# MOSA在CCA中的应用：模块化开放系统方法与协作作战飞机

## 摘要

协作作战飞机（[[collaborative-combat-aircraft|CCA]]）是MOSA在下一代空中力量中最重大的应用——计划生产1000+架无人作战飞机，2028年首次列装，2030年形成早期作战能力。CCA明确采用[[open-mission-systems|OMS]]框架构建任务系统，软件定义能力，遵循C-SWaP约束。然而，CCA面临一个核心张力：**速度（2028年MTA路径deadline）vs 模块化（MOSA五大支柱要求）**。极端的采办时间压力可能迫使工程团队在MOSA合规性上做出妥协。

## 对比分析

### MOSA五大支柱 → CCA实施映射

| MOSA支柱 | CCA实施现状 | 挑战/张力 |
|----------|-----------|----------|
| **赋能环境** | OMS框架作为赋能基础；DevSecOps流程建立中 | 工具链集成速度 vs 标准完善度 |
| **模块化设计** | 任务系统模块化（传感器/通信/电子战/处理器）；C-SWaP约束驱动物理模块化 | 集成测试时间不足（MTA timeline） |
| **指定接口** | OMS定义任务系统接口；软件定义能力要求数字接口 | 接口规范演进 vs 2028 deadline |
| **开放标准** | OMS作为事实标准；C5ISR标准趋同（CMOSS/SOSA） | 标准成熟度 vs 开发进度 |
| **竞争机制** | 多供应商竞争任务系统组件；软件定义能力降低切换成本 | 现有供应商主导 vs 新进入者壁垒 |

### CCA的规模与时间线

CCA项目是美国空军自F-35以来最大规模的作战飞机采购：

| 维度 | 数值 | 意义 |
|------|------|------|
| **计划产量** | 1000+架 | 大规模部署无人僚机 |
| **首次列装** | 2028年 | 极端紧迫的MTA路径 |
| **早期作战能力** | 2030年 | 初始作战能力形成 |
| **采办路径** | MTA或主要能力采办 | 速度优先于完整流程 |
| **成本目标** | 显著低于有人平台 | 经济可承受性驱动规模 |

### OMS框架在CCA中的应用

OMS（[[open-mission-systems|开放任务系统]]）是CCA任务系统层的核心接口框架：

- **架构层**：OMS定义任务系统的标准接口，支持即插即用的传感器、通信和电子战模块
- **软件层**：软件定义能力——通过软件升级而非硬件替换实现能力演进
- **C5ISR整合**：OMS与[[c5isr-standards-convergence|CMOSS/SOSA等标准]]趋同，共享硬件和软件接口
- **竞争支持**：OMS接口使多个供应商可以竞争同一功能模块，降低切换成本

### 核心张力：速度 vs 模块化

[[speed-vs-modularity|速度与模块化张力]]在CCA上达到极端：

**速度压力（2028 deadline）**：
- MTA路径（[[middle-tier-acquisition|中间层采办]]）在5年内完成采办→部署全流程
- 竞争对手（中国）的快速迭代速度要求美国加速
- "先部署再完善"的思维可能导致接口规范不完整
- 集成测试时间被压缩，MOSA模块独立验证不足

**模块化需求（MOSA要求）**：
- FY2017 NDAA Section 805法定要求MOSA
- CCA需要模块化以支持竞争——1000+架飞机的全生命周期升级
- 软件定义能力要求开放接口以支持第三方开发
- 1000+架的规模意味着任何架构锁定的代价都是天文数字

**潜在妥协**：
- 初始批次可能采用"足够好"的MOSA实施，后续批次逐步完善接口
- OMS框架的成熟度可能不足以支撑所有CCA任务需求
- 供应商锁定风险在MTA路径下更高——需要快速决策可能牺牲竞争
- 接口规范演进可能与生产节奏冲突

### 与其他MOSA应用的对比

| 应用 | 规模 | 时间压力 | MOSA成熟度 | 备注 |
|------|------|---------|-----------|------|
| **CCA** | 1000+架 | 极高（2028） | 中等 | OMS框架驱动 |
| **JADC2** | 全军种 | 高 | 低 | 架构层面MOSA |
| **CMOSS/SOSA** | 平台级 | 中等 | 高 | 标准成熟 |
| **FACE** | 航空电子 | 中等 | 高 | 软件标准 |

## 趋同与分歧

### 趋同点

1. **OMS标准**：CCA的OMS框架与C5ISR标准趋同（CMOSS/SOSA），共享接口理念
2. **软件定义**：CCA的软件定义能力与MOSA的模块化理念高度一致
3. **竞争机制**：多供应商竞争任务系统组件，与MOSA的竞争目标一致

### 分歧点

1. **时间 vs 标准**：MTA路径的2028 deadline vs MOSA标准的成熟度
2. **集成 vs 模块化**：快速集成测试的需求 vs MOSA模块独立验证的要求
3. **锁定 vs 开放**：MTA路径下需要快速决策，可能牺牲竞争开放性

## 相关内容

- [[open-architecture-hierarchy]] — 开放架构四层体系总览
- [[collaborative-combat-aircraft]] — CCA概念定义
- [[open-mission-systems]] — OMS框架
- [[mosa-five-pillars]] — MOSA五大支柱
- [[mosa-defense-acquisition]] — MOSA在国防采办中的应用
- [[speed-vs-modularity]] — 速度与模块化张力
- [[middle-tier-acquisition]] — 中间层采办（MTA）
- [[adaptive-acquisition-framework]] — 自适应采办框架（AAF）
- [[fy24-st-terms-of-reference]] — FY2024 S&T审查范围
- [[modular-architecture-patterns]] — 模块化架构模式
- [[c5isr-standards-convergence]] — C5ISR标准趋同

## 笔记

- CCA可能是MOSA历史上最大规模的测试——1000+架飞机意味着MOSA的成功或失败将被规模化放大
- OMS框架在CCA中的地位类似于FACE在航空电子中的地位——事实标准驱动模块化
- 2028 deadline意味着CCA不可能在首飞时实现完全MOSA合规——更现实的路径是"渐进式MOSA"
- 1000+架的规模本身就是MOSA的最佳辩护——即使初始锁定成本很小，乘以1000后也变得不可承受
- CCA的MOSA实施经验将直接影响NGAD（下一代空中优势）等后续项目的MOSA策略
