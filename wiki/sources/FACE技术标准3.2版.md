---
title: "FACE技术标准 V3.2"
created: 2026-04-19
updated: 2026-05-21
tags: [FACE, 航电, 开放标准, The Open Group, 软件架构, 互操作]
source: [raw/papers/FACE技术标准3.2版.pdf, raw/articles/FACE技术标准3.2版.md]
confidence: EXTRACTED
type: source
---

# FACE技术标准 V3.2

## 概述

Future Airborne Capability Environment（FACE）技术标准第3.2版，由The Open Group FACE Consortium于2023年8月发布（文档编号C232，ISBN 1-957866-29-1）。这是航空电子领域最重要的**开放软件架构标准**，定义了航电软件的可移植性和互操作性技术规范。是DoD MOSA生态中**软件层面最核心的标准之一**。

## 标准定位

- **领域**：航空电子（机载软件）
- **层级**：DoD MOSA标准生态 → 平台/系统级 → **FACE（软件）**
- **管理方**：The Open Group FACE Consortium（行业联盟）
- **状态**：V3.2为当前最新稳定版（2023年8月）

## MOSA标准生态中的位置

```
MOSA（DoD政策框架）
├── 平台级：SOSA（传感器硬件）、CMOSS（C5ISR）、VICTORY（地面车辆）
├── 软件级：FACE（航电软件）★
├── 接口级：UAI（武器接口）、MORA（射频）
└── 建模级：SysML v2、UAF
```

## FACE架构核心概念

### 架构分层（Segment）

FACE架构将航电软件系统分为多个段（Segments），通过标准化接口隔离：

1. **Operating System Segment (OSS)** — 操作系统层
2. **I/O Services Segment (IOSS)** — I/O服务层
3. **Platform-Specific Services Segment (PSSS)** — 平台特定服务层
4. **Transport Services Segment (TSS)** — 传输服务层
5. **Portable Components Segment (PCS)** — 可移植组件层

### 关键目标

- **软件可移植性**：不同供应商的航电应用可在不同平台上运行
- **组件可复用性**：已验证的软件组件可在新项目中复用
- **供应商竞争**：通过标准接口解锁供应商锁定
- **快速能力插入**：新功能可快速集成到现有航电系统

## V3.2版本更新

- 2023年8月发布
- 兼容前一版V3.1
- 持续演进中——The Open Group标注了"Future Directions"

## 应用的MOSA案例项目

- **FLRAA** (Bell V-280 Valor) — 陆军未来远程突击机，明确要求FACE对齐
- **F-35 TR3** (Technology Refresh 3) — 洛马正在推进FACE兼容性
- **B-21 Raider** — GAO认证的完整MOSA计划项目
- PEO Aviation FACE TIM演示（2021）— 20家公司参与

## 笔记

- FACE V3.2是航电软件领域的"通信协议"——不是规定怎么做，而是规定不同模块之间如何对话
- The Open Group同时管理FACE和SOSA两个标准——硬件（SOSA）+软件（FACE）=完整航电MOSA方案
- V3.2的"Future Directions"章节暗示了与SysML v2和数字工程的进一步集成
- 对于非航电领域的参考价值：FACE的分层架构模型对其他领域的模块化设计有示范意义
