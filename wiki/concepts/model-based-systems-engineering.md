---
title: "基于模型的系统工程（MBSE）"
created: 2026-04-26
updated: 2026-04-26
type: concept
tags: [MBSE, SysML, 数字工程, 系统工程, 模型驱动]
sources: [raw/papers/incose-vision-2035.pdf, raw/papers/nasa-se-handbook-rev2.pdf]
---

# 基于模型的系统工程（MBSE）

## 定义

**基于模型的系统工程**（Model-Based Systems Engineering, MBSE）是指**形式化地应用建模技术**，以支持系统在全生命周期内的**需求、设计、分析、验证与确认（V&V）**活动。该定义源自INCOSE（国际系统工程学会）。

> MBSE is the formalized application of modeling to support system requirements, design, analysis, verification, and validation activities beginning in the conceptual design phase and continuing throughout development and later life cycle phases.
> — INCOSE SE Vision 2025/2035

## MBSE的三大支柱

MBSE的实践依赖于**语言、工具、方法**三者的协同：

| 支柱 | 说明 | 典型代表 |
|------|------|---------|
| **语言（Language）** | 系统建模的形式化表达 | SysML v1/v2、UML、Modelica、AADL |
| **工具（Tool）** | 建模、仿真与管理平台 | Cameo Systems Modeler、IBM Rhapsody、Capella（开源）、Modelio |
| **方法（Method）** | 建模流程与框架指导 | OSEM（Object-Oriented SE Method）、MagicGrid、SAFe MBSE、INCOSE MBSE Initiative |

三者缺一不可：**语言**定义表达能力，**工具**提供生产力，**方法**确保一致性与可重复性。

## MBSE vs 文档驱动系统工程

传统系统工程以**文档**为核心载体（需求文档、设计文档、接口控制文件等）。MBSE实现了一次根本性转变：

| 维度 | 文档驱动 SE | MBSE |
|------|-----------|------|
| **知识载体** | 多份独立文档（Word/PDF） | 统一的互联模型 |
| **一致性保障** | 人工审查、易出错 | 模型内自动一致性检查 |
| **变更影响** | 需逐文档追溯 | 模型内自动追溯与影响分析 |
| **信息冗余** | 大量重复描述 | 单一事实来源（Single Source of Truth） |
| **V&V** | 基于文档评审 | 模型仿真、形式化验证 |
| **团队协作** | 基于文档流转 | 基于模型的实时协同 |

**核心转变**：从"文档是知识的载体"到"模型是知识的载体"。文档从**主体**变为模型的**派生产物**（view）。

## SysML v2：MBSE的关键使能器

SysML v2（OMG标准）是下一代系统建模语言，为MBSE实践带来重大改进：

- **文本化表示（Textual Notation）**：支持基于文本的模型定义，与Git版本控制天然兼容，降低建模门槛
- **API优先（API-First）**：原生提供模型查询与操作API，支持工具间互操作和自动化流水线
- **改进的行为建模**：强化状态机、活动图、交互序列的表达能力
- **增强的互操作性**：标准化模型交换格式，减少供应商锁定
- **需求建模增强**：需求与模型元素的更紧密关联

SysML v2有望成为**数字工程生态系统的枢纽语言**，连接需求管理、架构设计、仿真验证、配置管理等环节。

> 参见：[[sysml-v2-specification]]、[[ousd-sysml-v2-transition-guidance]]

## INCOSE V5指南中的MBSE

INCOSE SE Handbook V5将MBSE定位为系统工程师的**核心能力（Core Competency）**：

- **数字线程（Digital Thread）**：MBSE模型作为数字线程的核心节点，贯穿需求→设计→制造→保障全链路
- **模型治理（Model Governance）**：建立模型质量标准、审查流程、配置管理规则
- **渐进式采纳**：从关键工程活动入手，逐步扩展MBSE覆盖范围
- **人才能力建模**：将MBSE能力纳入系统工程师能力框架（SE Competency Framework）

> 参见：[[incose-se-handbook-v5]]

## NASA SE Handbook中的模型方法

NASA系统工程手册（Rev 2）要求在工程实践中采用**基于模型的方法**：

- **需求建模**：以形式化模型表达系统需求，支持自动一致性检查
- **架构建模**：通过模型定义功能架构与物理架构的映射
- **V&V通过模型**：利用模型仿真执行验证与确认活动，减少实物测试成本
- **模型基线管理**：将模型纳入配置管理基线，与传统文档基线同等管理

> 参见：[[nasa-se-handbook-rev2]]

## MBSE与MOSA的协同

MBSE与模块化开放系统方法（MOSA）在实践中高度互补：

- **接口定义**：MBSE模型是定义模块接口的最精确、最形式化的手段
- **独立验证**：模块供应商可基于共享接口模型独立开发和验证模块
- **架构可视化**：MBSE模型清晰展示模块边界、接口关系和数据/信号流
- **变更管理**：当某个模块需要升级时，模型能精确分析接口影响范围
- **竞争性采办**：政府持有接口模型，降低供应商切换成本

**协同模式**：MOSA定义"做什么"（模块化原则），MBSE定义"怎么做"（模型化表达）。二者结合实现**可验证的模块化开放架构**。

> 参见：[[interface-engineering-evolution]]、[[architecture-framework]]

## 数字工程视角

MBSE是**数字工程（Digital Engineering）**的核心支柱之一。在国防部数字工程战略框架下：

- MBSE模型与**数字孪生（Digital Twin）**、**数字线程（Digital Thread）**共同构成数字工程基础设施
- 模型数据需遵循**FAIR原则**（Findable, Accessible, Interoperable, Reusable）
- 从"基于文档的里程碑评审"向"基于模型的持续评估"转变

> 参见：[[digital-engineering-practice]]

## 相关内容

- [[sysml-v2-specification]] — SysML v2语言规范
- [[incose-se-handbook-v5]] — INCOSE SE Handbook V5
- [[nasa-se-handbook-rev2]] — NASA系统工程手册Rev 2
- [[ousd-sysml-v2-transition-guidance]] — OUSD SysML v2转型指南
- [[digital-engineering-practice]] — 数字工程实践
- [[architecture-framework]] — 架构框架概念
- [[interface-engineering-evolution]] — 接口工程演进

---
*概念提取自INCOSE SE Vision、NASA SE Handbook、OMG SysML v2规范及国防部数字工程战略相关文献*
