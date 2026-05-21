---
title: "FACE™ — 未来机载能力环境"
created: 2026-04-05
updated: 2026-05-21
type: concept
tags: [FACE, 航空电子, 开放架构, 软件标准, The Open Group, MOSA双支柱, 软件可移植性]
sources:
  - sources/FACE技术标准3.2版.md
  - sources/航空PEO-FACE-TIM开放系统演示2021.md
  - sources/MOSA与美国国防采办-Shah论文.md
  - comparisons/开放架构层级.md
confidence: SYNTHESIZED
evidence: "综合FACE技术标准V3.2原文、PEO Aviation FACE TIM 2021演示、Shah 2021博士论文第4章FACE案例分析、开放架构层级体系、三军备忘录2024"
---

# FACE™ — 未来机载能力环境

## 概述

Future Airborne Capability Environment（FACE）是由 **The Open Group** 维护的航空电子开放软件架构标准，2010年启动。FACE 定义航电软件的分段架构和标准接口，使不同供应商的软件组件可在不同硬件平台和操作系统之间**可移植、可复用、可互换**。当前最新版为 V3.2（2023年8月发布）。

FACE 是 DoD MOSA 生态中**软件层面最核心的标准之一**，与 SOSA（传感器硬件标准）形成 MOSA 标准层的**"双支柱"**。2024年12月三军联合备忘录将 FACE 列为6大已验证开放标准之一。Shah（2021）博士论文将 FACE 作为 MOSA 成功实施的"极具说服力的案例研究"主案例。

## FACE 五段架构

FACE 将航电软件系统分为五个段（Segments），通过标准化接口隔离，实现组件间解耦：

| 段 | 英文全称 | 职责 |
|----|----------|------|
| **OSS** | Operating System Segment | 操作系统抽象层，隔离应用与特定OS |
| **IOSS** | I/O Services Segment | I/O服务层，标准化硬件I/O访问 |
| **PSSS** | Platform-Specific Services Segment | 平台特定服务，封装硬件差异 |
| **TSS** | Transport Services Segment | 传输服务层，提供标准化的段间通信 |
| **PCS** | Portable Components Segment | 可移植组件层——最终目标，供应商软件"一次编写，多平台运行" |

**核心设计逻辑**：下层（OSS/IOSS/PSSS）封装平台差异 → TSS 提供统一通信 → PCS 的软件组件不感知底层实现。不同 FACE 版本（2.1/3.0/3.1）的组件可通过 TSS 代理方法在同一系统中共存。

## 在 MOSA 生态中的位置

```
MOSA（DoD 政策框架）
├── 平台级：OMS/UCI（任务系统）、UCS（无人机指控）
├── 传感器硬件：SOSA ★
├── 航电软件：FACE ★ （双支柱之一）
├── 武器接口：UAI、WOSA
├── 射频/通信：MORA、CMOSS、VICTORY
└── 部组件级：HOST（海军硬件）
```

FACE 处于**组件级**（开放架构四层体系的第4层），定义的是单个软件模块的接口规范。它与上层 OMS（航空任务系统服务总线）和同层 HOST（硬件标准）协同工作。

## 核心特征

- **公开发布的接口规范**：由 The Open Group FACE Consortium 维护，约70个组织、900余名个人贡献者参与
- **供应商中立**：不绑定特定操作系统（已验证支持 Windows、Linux、VxWorks、LynxOS、DEOS、RTEMS 等）
- **一致性和认证**：FACE Conformance Program 提供标准化的验证流程
- **向后兼容**：V3.2 兼容 V3.1，支持版本混合部署
- **覆盖领域**：航电显示、导航、动力系统、通信、传感器处理、任务计算

## 大规模验证：PEO Aviation FACE TIM 2021

2021年6月，PEO Aviation 在 FACE 技术互通会议（TIM）上组织了迄今**最大规模的 FACE 生态系统集成演示**：

- **20家行业公司**：Lockheed Martin、Boeing、Northrop Grumman、Collins、BAE、Bell、L3Harris、RTI、Wind River 等
- **9个 DoD 组织**：PEO Aviation、PMA 209（海军）、DEVCOM 多个部门
- **29个软件产品** × **5个操作系统** × **7个硬件平台** × **8个 TSS 实现**
- 实现 UH-60V 飞行软件、ITEP 发动机控制、Collins 导航系统、编队战术应用等跨供应商集成

**关键技术验证**：
- 不同 FACE 版本（2.1/3.0/3.1）的组件通过 TSS 桥接共存
- FACE 包装器可将遗留系统软件纳入开放架构
- HOST/SOSA 硬件 + FACE 软件 = 完整的航电 MOSA 方案
- TSS 替换的复杂性暴露了"需要成熟系统模型驱动 TSS 代码生成"的需求（→数字工程方向）

## 已应用的项目

- **FLRAA**（Bell V-280 Valor）— 陆军未来远程突击机，明确要求 FACE 对齐
- **F-35 TR3**（Technology Refresh 3）— 洛马正在推进 FACE 兼容性
- **B-21 Raider** — GAO 认证的完整 MOSA 实施项目
- **UH-60V 黑鹰升级** — 飞行甲板软件通过 FACE TIM 2021 验证
- 已应用于超过 **20个含 FACE 要求的国防采办项目**

## 与其他标准的关系

- **SOSA** — FACE（软件层）+ SOSA（传感器硬件层）= 完整航电 MOSA 方案。The Open Group 同时管理两者，TSOA-ID 验证了 HOST/SOSA 硬件 + FACE 软件快速集成（集成时间从月/年级降至周级）
- **OMS** — OMS 抽象服务总线建立在 FACE/SOSA 之上，实现任务系统级互操作
- **HOST** — NAVAIR 海军硬件标准，与 FACE 互补（HOST 定义硬件卡板，FACE 定义运行其上的软件）
- **CMOSS** — 陆军 C5ISR 标准，与 FACE 在不同域互补

## 笔记

- FACE 的**分层架构模型**对非航电领域的模块化设计有重要参考价值——"接口服务于模块"的设计哲学适用于任何需要供应商解耦的复杂系统
- FACE 的 The Open Group 管理模式使其具有**跨军种、跨供应商的中立性**——这是相比军种自研标准的独特优势
- TIM 2021 暴露了 FACE 当前关键缺口：TSS 替换复杂度（→需要自动代码生成）、容器适航性不足、CSM 开发困难——这些为 FACE 后续版本演进指明了方向
- Shah 论文的核心观察：FACE 是 MOSA "从理论到实践"的最佳实证，但缺乏 MOSA 效果的**定量衡量方法**仍是整个 MOSA 生态的关键挑战
- FACE V3.2 的"Future Directions"章节暗示下一步与 SysML v2 和数字工程的集成——这一方向与 DoD 整体的数字工程转型一致
