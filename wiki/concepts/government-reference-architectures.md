---
title: "政府参考架构（GRA）模式"
created: 2026-04-29
updated: 2026-04-29
type: concept
tags: [GRA, 参考架构, MOSA, MBSE, AFMC, MIL标准, 模块化, 接口标准化]
sources: [raw/papers/Chris-Garrett-Presentation-Sep-2024.pdf, raw/articles/Chris-Garrett-Presentation-Sep-2024.md]
---

# 政府参考架构（GRA）模式

## 摘要

政府参考架构（Government Reference Architectures, GRA）是美国空军部（DAF）推动的架构模式，由政府拥有和维护参考架构，定义模块边界和标准化接口，供承包商在竞标和开发中引用。GRA是MOSA原则在架构层面的具体实施——政府掌握架构定义权，通过标准化接口促进竞争和可移植性。

## 要点

### GRA核心理念

- **政府拥有**：参考架构由政府而非承包商定义和维护
- **模块边界**：明确的功能模块划分和接口定义
- **竞争促进**：承包商在GRA框架内竞标和开发，降低切换成本
- **复用性**：跨项目、跨平台的架构复用

### 抽象模型分层

GRA采用分层管理的抽象模型体系：
- **功能配置基线**（Functional Configuration Baseline）：高层功能定义
- **分配配置基线**（Allocation Configuration Baseline）：功能到模块的分配
- **生产配置基线**（Production Configuration Baseline）：具体实现规范
- 从抽象到具体的模型层级管理

### AFMC GRA体系（Chris Garrett演示）

**AV GRA（飞行器政府参考架构）**：
- 基于MIL-STD-881的AV结构（WBS）
- 79个MIL文档→36个系统模型
- 聚焦电气子系统（MIL-HDBK-516第12节和JSSG-2009-8）
- 使用敏捷方法管理（Jira看板和Sprint）
- VV&A流程、样式指南、JSON格式

**功能GRA**：
- 武器GRA（[[wosa-architecture-tools|WOSA]]）
- 传感器GRA
- PNT GRA（R-EGI）
- ABMS GRA、SCARS GRA、任务规划GRA、NC3 GRA、Sentinel GRA等

**标准集成**：
- [[open-mission-systems|OMS/UCI]] — 任务系统互操作性
- [[face-technical-standard|FACE]] — 航空电子设备可移植性
- SOSA H/W — 传感器硬件标准化
- COARPS — 雷达系统
- UAI — 武器接口

### 目标架构

- 使命特定权衡，识别公共服务
- 软件应用服务层
- 可复用共享资产：模型、服务、组件、软件应用
- OMS作为抽象服务总线（ASB）隔离器
- FACE用于航空电子软件可移植性

### 与MOSA的关系

GRA是MOSA五原则/五大支柱的架构层实现：
- **模块化设计**：GRA定义功能模块边界
- **指定接口**：GRA标准化模块间接口
- **开放标准**：GRA基于MIL标准和行业开放标准
- **一致性认证**：GRA提供验证和确认框架
- **赋能环境**：政府拥有架构，促进竞争生态

## 相关内容

- [[open-architecture-hierarchy]] — 开放架构四层体系（GRA横跨各层）
- [[chris-garrett-presentation-2024]] — AFMC数字化转型演示（GRA详细描述）
- [[digital-materiel-management]] — DMM数字化物资管理
- [[modular-architecture-patterns]] — 模块化架构模式
- [[mosa-defense-acquisition]] — MOSA核心概念
- [[mosa-five-pillars]] — MOSA五大支柱
- [[face-technical-standard]] — FACE技术标准
- [[open-mission-systems]] — 开放任务系统
- [[wosa-weapons-open-systems-architecture]] — WOSA武器系统架构
- [[sosa-sensor-open-systems-architecture]] — SOSA传感器架构
- [[host-hardware-open-systems]] — HOST硬件开放系统
- [[c5isr-standards-convergence]] — C5ISR标准趋同
- [[six-validated-mosa-standards]] — 六大已验证MOSA标准
- [[mil-std-881d-wbs-defense-materiel]] — MIL-STD-881D WBS

## 笔记

- GRA模式的关键创新是"政府拥有架构定义权"——这直接对抗传统模式下承包商通过专有架构锁定政府的做法
- AV GRA将79个MIL文档转换为36个系统模型，是数字工程从文档驱动到模型驱动的典型实践
- GRA体系的广度（飞行器、武器、传感器、PNT、任务系统等）表明AFMC正在系统性地推进架构标准化
- SOSA H/W在目标架构中作为硬件标准化层覆盖多个领域，是MOSA硬件层面的核心标准
- GRA与现有的[[six-validated-mosa-standards|六大已验证标准]]互补——标准定义接口协议，GRA定义架构框架
