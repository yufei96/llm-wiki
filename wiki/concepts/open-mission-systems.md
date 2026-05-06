---
title: "开放任务系统（OMS）"
created: 2026-04-05
updated: 2026-04-29
type: concept
tags: [OMS, 传感器互操作, 开放架构, MOSA, CCA, GRA, FACE, SOSA, UAI, ASB]
sources: [raw/mosa-us-defense-acquisition-shah-2021.pdf, raw/papers/peo-avn-face-tim-2021-presentation.pdf, raw/papers/Chris-Garrett-Presentation-Sep-2024.pdf]
---

# 开放任务系统（OMS）

## 摘要

开放任务系统（Open Mission Systems, OMS）是美国空军主导制定的传感器与任务系统开放架构标准，是MOSA在航空任务系统领域的核心落地规范。OMS定义了任务系统之间的标准化服务接口，使不同供应商的传感器、载荷和任务系统能够即插即用。在AFMC政府参考架构（GRA）体系中，OMS被定位为**抽象服务总线（ASB）隔离器**，在FACE/SOSA/UAI等不同标准域之间提供隔离和互操作能力。

## 核心目标

解决不同供应商的传感器、载荷、任务系统之间的互操作问题，实现传感器即插即用，不需要定制开发集成接口。

## 核心特点

- 标准化的传感器数据接口：所有传感器输出格式统一，支持任意系统接入
- 服务化架构：功能以服务形式提供，支持动态组合与调用
- 硬件无关：不绑定特定硬件平台，支持跨平台移植
- 抽象服务总线：作为隔离器连接不同标准域（FACE/SOSA/UAI）

## 在GRA目标架构中的角色

Chris Garrett的AFMC演示（[[chris-garrett-presentation-2024]]）详细描述了OMS在政府参考架构目标架构中的关键角色：

### OMS作为抽象服务总线（ASB）隔离器

在GRA目标架构中，OMS被定位为**连接不同标准域的核心集成层**：

```
┌──────────────────────────────────────────┐
│          GRA目标架构                       │
│                                          │
│  ┌──────┐  ┌──────┐  ┌──────┐           │
│  │ FACE │  │ SOSA │  │ UAI  │  标准域    │
│  │航电   │  │传感器 │  │武器  │           │
│  └──┬───┘  └──┬───┘  └──┬───┘           │
│     │         │         │               │
│  ┌──┴─────────┴─────────┴──┐            │
│  │     OMS（ASB隔离器）     │  集成层    │
│  │  抽象服务总线             │            │
│  └─────────────────────────┘            │
│                                          │
│  • 软件应用服务层                         │
│  • 可复用共享资产：模型/服务/组件/软件      │
└──────────────────────────────────────────┘
```

OMS的隔离器角色意味着：
- FACE组件可以独立演进而不影响SOSA硬件层
- SOSA传感器可以替换而不影响FACE航电软件
- UAI武器接口可以更新而不影响其他域
- 各域通过OMS标准化接口实现松耦合集成

### 功能GRA中的OMS

在AFMC的功能GRA体系中，OMS/UCI出现在多个领域：
- **传感器GRA**：OMS/UCI作为传感器数据接口标准
- **PNT GRA（R-EGI）**：OMS/UCI作为PNT数据服务接口
- **武器GRA（WOSA）**：OMS/UCI与UAI配合实现武器-传感器集成

## OMS与CCA的关系

[[collaborative-combat-aircraft|协作作战飞机（CCA）]]明确采用OMS框架：

- **架构框架**：AFRL的OMS框架是CCA任务系统的核心架构标准
- **任务系统接口**：CCA的分布式任务系统组合通过OMS标准化接口实现互操作
- **[[software-defined-capabilities|软件定义能力]]**：OMS接口标准是CCA"软件定义能力"理念的技术基础——通过标准化服务接口，CCA的任务能力可通过软件配置快速调整
- **供应商竞争**：OMS的开放接口使多家供应商可以竞争性提供CCA的传感器和任务系统模块

FY2024 SAB S&T审查ToR（[[fy24-st-terms-of-reference]]）将CCA任务系统列为重点审查领域，OMS框架的技术成熟度和集成能力是审查的关键关切。

## FACE TIM 2021中的OMS实践

PEO Aviation FACE TIM 2021演示（[[peo-aviation-face-tim-2021]]）展示了OMS在实际系统集成中的应用：

- **OMS/UCI作为集成层**：连接FACE航电软件组件与外部系统（Link-16、ATAK设备等）
- **多TSS桥接**：OMS接口支持不同传输服务子系统（TSS）之间的无缝切换（RTI DDS ↔ 60V传输），无需重新编译软件
- **FACE 2.1/3.0/3.1互操作**：OMS接口层使不同版本的FACE软件组件可以共存
- **遗留系统集成**：通过OMS接口层，UH-60V飞行甲板软件等遗留系统可以融入开放架构

## 应用案例

- **F-35战斗机**传感器集成
- **全球鹰无人机**地面控制站
- **下一代轰炸机**（B-21）任务系统
- **CCA**（协作作战飞机）任务系统框架
- **ABMS**（先进战斗管理系统）C2集成
- PEO Aviation FACE TIM 2021演示中的多平台集成

## 与其他标准的关系

| 标准 | 与OMS的关系 |
|------|-----------|
| [[face-technical-standard\|FACE]] | FACE定义航电软件可移植性，OMS定义任务系统服务接口——两者互补 |
| SOSA | SOSA定义传感器硬件标准，OMS建立在SOSA硬件之上 |
| UAI | UAI定义武器接口，OMS与UAI配合实现传感器-武器集成 |
| [[mosa-defense-acquisition\|MOSA]] | OMS是MOSA在航空任务系统领域的核心落地规范 |
| HOST | HOST定义硬件开放系统技术，OMS在HOST硬件平台上运行 |

## 相关内容

- [[open-architecture-hierarchy]] — 开放架构四层体系（OMS为平台级）
- [[mosa-defense-acquisition]] — MOSA核心概念
- [[face-technical-standard]] — FACE航电标准
- [[ucs-control-station]] — 无人系统指挥控制标准
- [[collaborative-combat-aircraft]] — CCA：OMS框架的旗舰应用
- [[government-reference-architectures]] — GRA：OMS作为ASB隔离器的目标架构
- [[chris-garrett-presentation-2024]] — AFMC演示（OMS在GRA中的角色）
- [[peo-aviation-face-tim-2021]] — FACE TIM 2021演示（OMS集成实践）
- [[software-defined-capabilities]] — 软件定义能力
- [[c5isr-standards-convergence]] — C5ISR标准趋同
- [[modular-architecture-patterns]] — 模块化架构模式

## 笔记

- OMS在GRA目标架构中被定位为"抽象服务总线隔离器"是一个重要的架构决策——它使各标准域可以独立演进
- CCA采用OMS框架是MOSA原则在新一代无人平台上的直接体现
- FACE TIM 2021演示中OMS/UCI的实际集成验证了其在多供应商、多版本环境中的互操作能力
- OMS与FACE的区别经常被混淆：FACE解决"软件能不能在不同平台上跑"（可移植性），OMS解决"不同系统能不能对话"（互操作性）

---

*最初摘自Shah 2021年工程博士实践报告。2026-04-29大幅扩展：新增GRA目标架构中的ASB隔离器角色、CCA关联、FACE TIM 2021实践数据、多来源交叉引用。*
