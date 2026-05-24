---
title: "SOSA参考架构 V2 — 传感器开放系统架构快照 2019"
created: 2026-04-19
updated: 2026-05-21
tags: [SOSA, 传感器, 开放架构, The Open Group, VITA, 硬件标准]
source: [raw/papers/SOSA参考架构V2.pdf, raw/articles/SOSA参考架构V2.md]
confidence: EXTRACTED
type: source
---

# SOSA参考架构 V2 — 传感器开放系统架构快照 2019

## 概述

The Open Group SOSA Consortium发布的**SOSA参考架构第1.0版第2卷快照**（Edition 1.0, Version 2 Snapshot），2019年发布，有效期至2019年12月31日。这是SOSA参考架构的早期公开版本，旨在征求行业反馈。引用退役海军中将Arthur K. Cebrowski的名言："你可以创造自己的未来，也可以成为别人为你创造的未来的受害者"——这正是SOSA的核心理念：通过开放标准掌控传感器系统的未来。

## Snapshot特征

- **性质**：草案（Snapshot），非正式标准
- **目的**：在正式发布前向感兴趣方传播SOSA联盟当前方向
- **反馈截止**：2019年12月31日
- **批准**：88ABW-2019-0039，2019年1月7日清除
- **Distribution**：A — 公开发布

## SOSA核心架构概念

SOSA建立在OpenVPX（VITA 65）硬件标准之上，定义了：

### 硬件架构层级

1. **机箱/背板（Chassis/Backplane）** — 3U或6U OpenVPX
2. **插槽配置（Slot Profiles）** — 标准化的板卡角色定义
3. **模块（Modules）** — SBC、GPU、FPGA、I/O、射频、存储等
4. **互连（Interconnects）** — PCIe、以太网、Serial RapidIO等
5. **冷却（Cooling）** — 传导冷却或空气冷却

### 软件架构

- 基于POSIX的操作系统
- 标准化的中间件和服务接口
- 与FACE（航电软件）的互补集成

## 在MOSA标准生态中的位置

SOSA是DoD MOSA生态中**传感器硬件层面的核心标准**：

```
SOSA（传感器硬件） + FACE（航电软件） = 完整的航电MOSA方案
SOSA（OpenVPX硬件） ⊂ CMOSS（标准套件，用VITA硬件）
```

## V2版本更新点

- 扩展了硬件插槽配置种类
- 增加了对MORA（射频架构，VITA 49.x）的兼容性
- 引入了更多I/O和存储模块定义

## 笔记

- 此Snapshot（2019年）是早期版本——后续有Edition 2.0等多版正式发布
- SOSA与CMOSS共享VITA硬件标准，但SOSA更专注传感器信号处理，CMOSS更专注C5ISR
- The Open Group同时管理SOSA和FACE——两个标准在设计上互补集成
- V2版的"Snapshot"属性意味着本文档代表方向而非最终定稿
