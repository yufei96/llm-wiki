---
title: "SOSA传感器开放系统架构参考架构技术标准"
date: 2026-04-19
type: source_summary
source: raw/papers/sosa-reference-architecture-v2.pdf
author: "The Open Group SOSA Consortium"
tags: [SOSA, 传感器, C4ISR, 开放架构, The Open Group]
---

# SOSA — 传感器开放系统架构（Sensor Open Systems Architecture）

## 文档概况
- **全称**：Technical Standard for SOSA™ Reference Architecture, Edition 1.0, Version 2 (Snapshot)
- **发布者**：The Open Group SOSA Consortium
- **日期**：2019年（Snapshot版，2021年正式发布Edition 1.0）
- **页数**：214
- **MOSA提及**：若干（SOSA是MOSA在传感器领域的具体实施）

## 核心内容

SOSA是由The Open Group SOSA联盟开发的**传感器领域开放系统架构标准**，旨在为雷达、EO/IR、SIGINT、通信、电子战等传感器系统定义开放接口和模块化架构。

### 使命
> "Empower government and industry to collaboratively develop open standards and best practices to enable, enhance, and accelerate the deployment of affordable, capable, interoperable sensor systems."

### 架构层次

| 层次 | 内容 |
|------|------|
| **Sensor-to-Platform** | 传感器与平台间标准化（电子机械、物理/环境、C2/载荷接口） |
| **Intra-sensor** | 传感器内部标准化（可互换硬件/软件组件，FACE™, OpenVPX, VITA） |
| **Multi-INT** | 多情报传感器集成（雷达+EO/IR+SIGINT共用处理平台） |

### 关键标准引用
- **OMS/UCI**：开放任务系统/通用指挥控制接口
- **NATO STANAG 4586**：无人系统指挥控制
- **FACE™**：机载能力环境标准
- **VITA/OpenVPX**：硬件卡板标准

### SOSA与CMOSS的关系
CMOSS和SOSA高度重叠：
- CMOSS侧重**陆军C5ISR通用套件**（Universal A-Kit + 卡板式硬件）
- SOSA侧重**跨军种传感器标准化**（The Open Group联盟驱动）
- 两者共享底层标准（VITA, OpenVPX, MORA）
- SOSA联盟中包含CMOSS团队成员

## 对MOSA的意义

SOSA是MOSA在**传感器/C4ISR领域最成熟的标准之一**：
- 由The Open Group管理（与FACE同一机构）
- 覆盖传感器全生命周期：设计→集成→测试→运维
- 提供具体的接口规范（而非MOSA政策层面的原则性要求）

SOSA与FACE构成了MOSA标准层的**双支柱**：
- **FACE** = 航电软件层开放架构
- **SOSA** = 传感器硬件/集成层开放架构

## 相关内容
- [[mosa-defense-acquisition]] — MOSA概念
- [[modular-architecture-patterns]] — 模块化架构模式
- [[face-technical-standard]] — FACE航电标准
- [[cmoss-overview-2022]] — CMOSS（与SOSA高度重叠）
- [[open-mission-systems]] — OMS（传感器软件接口标准）

---
*214页（Snapshot版）。SOSA是理解MOSA在传感器领域落地的关键标准文档。*
