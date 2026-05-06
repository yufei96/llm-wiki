---
title: "CMOSS（C5ISR/EW模块化开放标准套件）概述"
created: 2026-04-19
updated: 2026-04-19
type: source_summary
sources: [raw/papers/cmoss-overview-2022.pdf, raw/articles/cmoss-overview-2022.md]
author: "Jason Dirner, DEVCOM C5ISR Center"
tags: [CMOSS, MOSA, C5ISR, 通用套件, 陆军]
---

# CMOSS — C5ISR/EW模块化开放标准套件

## 文档概况
- **全称**：C5ISR/EW Modular Open Suite of Standards (CMOSS) Overview
- **发布者**：U.S. Army DEVCOM C5ISR Center, MOSA Management Office
- **作者**：Jason Dirner, MOSA Chief Engineer
- **日期**：2022年3月18日
- **页数**：32

## 核心概念

CMOSS是一个**标准套件**，旨在减少C5ISR和电子战系统的尺寸、重量和功耗（SWaP），同时增加灵活性和适应性。其核心理念是通过**通用硬件平台**实现多个功能的集成。

### 三大核心组件

1. **Universal A-Kit（通用套件）**
   - PM将能力作为**卡板**插入通用机箱
   - 消除了平台特定集成的需求
   - 大幅减少后勤保障负担

2. **Pooled Resources（共享资源）**
   - **天线和放大器**共享：通信、电子战（EW）、信号情报（SIGINT）系统共用
   - **处理资源**共享：计算机和显示器
   - **数据服务**共享：定位、导航和授时（PNT）

3. **Shared Services（共享服务）**
   - 增强C5ISR系统间的互操作性和同时性
   - 通过共同备件减少全生命周期成本
   - 最新硬件替换时实现快速技术插入

### 与其他标准的关系

CMOSS是**多个标准的集成框架**：
- **MORA**（模块化开放射频架构）：射频前端标准化
- **VICTORY**：车辆C4ISR/EW互操作性
- **SOSA**：传感器开放系统架构
- **VITA/OpenVPX**：硬件卡板标准

### 对MOSA的意义

CMOSS是MOSA理念在**硬件层面最具体的落地形式**。当MOSA要求"模块化设计"和"开放接口"时，CMOSS提供了：
- 物理层的模块化（卡板式硬件）
- 接口层的标准化（OpenVPX, MORA射频接口）
- 实际的通用后勤保障模型

CMOSS证明了MOSA不是抽象概念——它在C5ISR领域已经产生了可度量的SWaP减少和后勤简化效果。

## 相关内容
- [[open-architecture-hierarchy]] — 开放架构四层体系（CMOSS为设备级集成框架）
- [[mosa-defense-acquisition]] — MOSA概念
- [[face-technical-standard]] — FACE航电标准（软件层对等）
- [[sosa-sensor-open-systems-architecture]] — SOSA传感器架构
- [[mora-modular-open-rf-architecture-concept]] — MORA射频架构
- [[victory-ground-vehicle]] — VICTORY车辆标准
- [[modular-architecture-patterns]] — 模块化架构模式
- [[mosa-five-pillars]] — MOSA五大支柱

---
*32页。CMOSS是理解MOSA硬件实施的关键文档。*
