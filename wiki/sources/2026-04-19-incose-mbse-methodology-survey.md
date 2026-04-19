---
title: "INCOSE MBSE方法论调查"
created: 2026-04-19
updated: 2026-04-19
type: source
tags: [MBSE, INCOSE, 方法论, 系统工程, SysML, 模型驱动]
sources: [raw/papers/mbse-methodology-survey-revb.pdf]
---

# INCOSE MBSE方法论调查

## 来源

INCOSE MBSE Initiative。作者：Jeff A. Estefan，NASA Jet Propulsion Laboratory (JPL)。修订版B，2008年5月。70页。

## 概述

对主流MBSE（基于模型的系统工程）方法论的系统调查。定义：MBSE方法论 = 相关过程、方法和工具的集合，用于在"基于模型"或"模型驱动"的语境中支撑系统工程学科。

## 调查覆盖的MBSE方法论

| 方法论 | 来源 | 核心思想 |
|--------|------|---------|
| **OOSEM** (Object-Oriented SE Method) | Lockheed Martin / INCOSE | 面向对象的SE方法，基于SysML |
| **IBM Harmony-SE** (RUP SE) | IBM Rational | RUP在SE领域的扩展 |
| **Vitech MBSE** (CORE) | Vitech Corporation | 基于CORE工具的方法论 |
| **JPL State Analysis** | NASA JPL | 状态分析，控制/状态驱动 |
| **INCOSE OOSM** | INCOSE | 面向对象的系统建模 |

## MBSE的核心特征

1. **模型是主要工件** — 不是文档，模型是SE的主要产出
2. **可执行模型** — 模型可仿真、可验证，不只是图形
3. **单一模型库** — 所有利益相关者基于同一模型工作
4. **自动化追溯** — 需求→设计→测试的自动追溯链

## MBSE与数字工程的关系

MBSE是数字工程的**核心引擎**：
- DoD DE Strategy 2018目标3："通过使用基于模型的方法来增强创新和技术成熟度"
- MBSE提供需求和架构层面的模型，数字孪生提供运行层面的模型
- 数字线程将MBSE模型与CFD/FEM/控制仿真等学科模型连接

## MBSE与MOSA的关系

MOSA为MBSE提供**互操作基础**：
- 不同MBSE工具（Cameo/MagicDraw、Rhapsody、Capella）通过SysML标准交换模型 → MOSA的"开放标准"原则
- 模块化接口定义是MBSE模型交换的"路由表" → MOSA的"指定关键接口"原则
- 避免被单一MBSE工具锁定 → MOSA的反供应商锁定核心目标

## 对知识库的价值

MBSE是知识库此前完全空白的领域。这份调查提供了：
- MBSE方法论全景图
- 各方法论的核心特点和适用场景
- MBSE与传统SE的区别
- MBSE工具生态的早期状态（2008年）

**注意**：此调查发布于2008年，MBSE领域已大幅发展（SysML v2、Capella等后续出现）。但作为基础认知仍有价值。

## 相关内容

- [[mosa-digital-engineering]] — MOSA与数字工程
- [[2026-04-19-dod-de-strategy-2018]] — DoD数字工程战略
- [[modular-architecture-patterns]] — 模块化架构模式
- [[requirements-quality-mosa]] — 需求质量（MBSE是需求质量的形式化工具）
- [[2026-04-19-ppi-requirements-analysis]] — PPI需求分析方法论
