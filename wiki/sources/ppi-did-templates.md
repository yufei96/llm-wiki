---
title: "PPI数据项描述（DID）模板合集"
created: 2026-04-19
updated: 2026-04-19
type: source
tags: [PPI, DID, 模板, 系统工程, 需求, 设计, 合同]
sources: [raw/papers/ppi-did-conops-osd.pdf, raw/papers/ppi-did-sep.pdf, raw/papers/ppi-did-sow.pdf, raw/papers/ppi-did-ssdd.pdf, raw/papers/ppi-did-syrs.pdf, raw/papers/ppi-sem-definitions.pdf, raw/articles/ppi-did-conops-osd.md, raw/articles/ppi-did-sep.md, raw/articles/ppi-did-sow.md, raw/articles/ppi-did-ssdd.md, raw/articles/ppi-did-syrs.md, raw/articles/ppi-sem-definitions.md]
---

# PPI数据项描述（DID）模板合集

## 来源

Project Performance International (PPI) — Robert J. Halligan主导编制。PPI是INCOSE和ISO/IEC SC7的长期参与者，这些DID模板基于MIL-STD-490/498系列和EIA 632标准演化而来，适用于DoD和NATO项目的合同数据要求。

## 概述

数据项描述（Data Item Description, DID）是**合同中规定供应商必须交付的文档的格式和内容模板**。在MOSA项目中，DID是将MOSA原则转化为可执行合同要求的关键工具——合同通过DID规定供应商交付什么格式的接口文档、设计文档和需求规范。

## 7个DID一览

### 1. CONOPS/OSD（概念文档，6页）
- PPA-004023-8，2023年1月
- **用途**：描述实现企业能力的概念性方法，聚焦运营层面
- **与MOSA的关系**：MOSA项目在方案阶段用CONOPS描述模块化架构的概念设计，定义系统主要解决方案元素及其接口
- **关键区别**：CONOPS/OSD ≠ OCD（Operational Concept Description），前者聚焦运营概念，后者聚焦操作场景

### 2. SEP（系统工程计划，21页）
- PPA-005327-18，2023年1月
- **用途**：定义项目的技术管理计划和过程，是技术团队的主要工作指导
- **与MOSA的关系**：MOSA实施计划应嵌入SEP中——包括接口管理计划、开放标准选择策略、一致性认证计划
- **关键特点**：SEP不自成合同约束，而是源于项目计划、受合同引用

### 3. SOW（工作说明书，10页）
- PPA-000953-9，2020年11月
- **用途**：规定供应商执行的工作任务和方法
- **与MOSA的关系**：MOSA合同中SOW应包含：模块化设计任务、接口定义任务、开放标准采用任务、数据权利交付任务
- **继承自**：MIL-HDBK-245E（美国政府SOW编制手册）

### 4. SSDD（系统设计描述，9页）
- PPA-003461-5，2012年5月
- **用途**：描述系统/子系统的架构设计（概念级），包括外部行为和接口设计
- **与MOSA的关系**：SSDD是MOSA"指定关键接口"原则的交付载体——通过SSDD记录模块化架构的接口定义

### 5. SyRS（系统需求规范，14页）
- PPA-002235-18，2023年1月
- **用途**：规定系统/子系统需满足的需求，是采办、设计、验证的基础
- **与MOSA的关系**：SyRS中应嵌入MOSA需求——模块化要求、开放接口要求、数据权利要求

### 6. SEM Definitions（系统工程管理术语，8页）
- PPI-007725-9，2024年
- **用途**：系统工程和管理领域的标准术语定义
- **价值**：包含Architecture、Baseline、Build Standard等核心术语的精确定义，可作为知识库概念页的术语参考

### 7. Requirements Quality Metrics（需求质量度量，6页）
- PPA-005330-11，1993年（Halligan经典论文）
- **用途**：需求质量的结构化度量方法
- **核心发现**：需求缺陷是成本和进度超支的首要原因（与Shah论文一致）
- **与MOSA的关系**：MOSA的"一致性认证"原则需要需求质量度量作为基础

## 对知识库的价值

这些DID模板补充了知识库在**合同执行层面**的空白：
- 知识库已有法规层（10 USC、DoDI）、政策层（BBP 3.0、MOSA指南）、标准层（FACE/SOSA/CMOSS）
- DID模板填补了"怎么把MOSA写进合同"的实操层
- 特别是SOW/SEP/SSDD三个DID，与PEO Aviation的MOSA合同模板直接对应

## 相关内容

- [[peo-aviation-mosa-impl-guide]] — PEO Aviation MOSA合同模板（SOW/PWS/SPS检查清单）
- [[osa-contract-guidebook-v1.1]] — OSA合同指南
- [[mosa-defense-acquisition]] — MOSA核心概念
- [[mosa-five-pillars]] — MOSA五大支柱
- [[dfars-part-252-contract-clauses]] — DFARS合同条款
