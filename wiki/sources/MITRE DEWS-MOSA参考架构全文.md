---
title: "MITRE DEWS MOSA参考架构完整文档"
created: 2026-04-26
updated: 2026-04-26
type: source
tags: [DEWS, MOSA, 参考架构, MITRE, 定向能武器, SOSA, MBSE, 数字工程, HEL, HPM]
sources: [raw/papers/mitre-dews-mosa-ra.pdf, raw/articles/mitre-dews-mosa-ra-full.md]
confidence: EXTRACTED
evidence: "直接从原始文档提取"
---

# MITRE DEWS MOSA参考架构完整文档

## 概述

这是MITRE Corporation受PEO IWS（综合作战系统项目执行办公室）委托开发的定向能武器系统MOSA参考架构（DEWS MOSA RA）完整会议简报文档（33页），作者Keegan Merkert，发布于2023年6月Kitty Hawk Week会议。该文档是[[DEWS-MOSA参考架构]]概念页面的原始来源，提供了架构开发方法论、模块定义、数据模型、SOSA整合和数字工程交付物的全面技术细节。

文档编号：PRS-23-1891，合同号W56KGU-18-D-0004，公开发布无限制。

## 核心内容

### MOSA理论基础

文档首先明确MOSA的定义和五大核心效益：

> "MOSA是一种集成业务和和技术策略，采用模块化设计，并在适当时定义使用广泛支持的共识标准的接口。"

五大效益：**改善互操作性**、**促进技术刷新**、**增强竞争**、**纳入创新**、**实现成本节约/避免**。

MOSA具有两个维度：
- **业务维度**：合同语言、知识产权、政策
- **技术维度**：模块化、共识标准和OSAs（FACE、OMS、SOSA、VICTORY）、一致性认证

### 三军部长备忘录（2019年1月7日）

三军部长联合签署备忘录，将MOSA确立为**作战必要条件**：
> "我们确定这些标准的持续实施，以及在缺乏标准的领域进一步开发MOSA标准，对我们的成功至关重要。"

### DEWS RA愿景与五大目标

**愿景：** 定向能武器项目利用广泛适用的参考架构，基于MOSA原则，加速创新、加快开发、增加标准元素的复用。

**五大目标及其使能条件：**

1. **广泛适用** — 与运行环境和宿主平台无关；利益相关者定义CV-1、质量属性、用例、架构原则
2. **基于MOSA原则** — 利用开放/商业标准；非专有模块和接口定义；保护供应商IP；大小企业全伙伴关系；一致性认证
3. **加速创新交付** — 采用"灰盒"概念（定义做什么而非如何做）；提供近远期技术替代插入方法；确保小企业全面参与
4. **增加复用** — 促进向后兼容；开放商业模式；可移植模块支持跨武器组合应用
5. **加快采办** — 减少传统集成测试时间；供应商无关的开放参考架构允许政府利用多个行业合作伙伴

### 架构开发方法论

开发流程遵循："接口服务于模块"

愿景/目标/使能条件 → 利益相关者输入 → 质量属性 → 用例 → 架构原则 → 功能详细列表 → 功能聚合为模块的准则 → 模块定义 → 模块I/O需求 → 接口定义 → 示例 → 示例数字模型 → 参考架构数字模型

### 约20个功能模块定义

**管理与控制：** 系统监控器、火控、DEWS管理
**感知与跟踪：** 摄像头、追踪器、综合传感器、本地传感器、航迹管理器、外部数据导入器
**波束生成与导向：** DE源、波束传输、波束导向器
**安全与接口：** 冲突解除安全、本地操作员HMI、宿主平台接口
**支持服务：** 安全服务、数据存储、支持服务、热管理、电力、支持系统操作

### 函数封装示例（模块21：本地操作员HMI）

文档展示了26个函数中的5个示例：
- 21.11 显示态势感知数据（MIL-STD-2525符号系统）
- 21.13 显示视频（支持TiVo式回放/暂停/倒带功能）
- 21.14 H&S状态更新
- 21.15 显示和控制状态
- 21.16 启动BIT

### 数据模型详细定义

Track消息数据对象包含：
- **Acceleration**: x/y/z加速度分量（km/s²）
- **Aimpoint**: 瞄准点位置（XYZ、AzEl、LatLong坐标系）
- **ModeOfOperation**: AUTOMATIC / SEMI_AUTOMATIC / MANUAL
- **Orientation**: yaw/pitch/roll（度）
- **Pose**: 位置与方向组合

### 开机序列活动图

10步开机序列：Power on → Power Distribution → Orderly Power On → System Initialization → H&S Reports → BIT → Monitor H&S

### 数字工程交付物

V1.1发布内容：
- 参考架构文档（MS Word）
- Magic Draw数字模型（Cameo/MSOSA 19.0 SP4）
- HTML提取（无Cameo用户可用）
- 补充材料：实施指南、RA评估、采办框架

### SOSA-DEWS整合详情

三类模块的详细映射：

**通用模块（12个）：** System Manager/System Monitor, Task Manager/Fire Control, External Data Ingestor, Tracker/Track Manager, Security Services, Storage/Data Storage, Nav Data/Supporting Services, Power, Host Platform Interface

**DEWS专用模块（7个）：** Local Operator HMI, Local Sensor(s), Deconfliction Safety, DE Source, Beam Transport, Beam Director, Thermal Management

**SOSA专用模块（13个）：** Emitter/Collector, Conditioner-Receiver-Exciter, Signal/Object Detector, Signal/Object Characterizer, Encoded Data Extractor, Situation Assessor, Impact Assessor and Responder, Reporting Services, Guard/Cross-Domain Service, Network Subsystem, Calibration Service, Compressor/Decompressor

### 关键技术差异

Power模块对比揭示了DEWS和SOSA在电力管理上的根本差异：
- DEWS开机过程与SOSA（高度机箱导向）不同
- DEWS储能关注能量浪涌，SOSA储能关注间歇断电时的延续
- 部分SOSA功能在DEWS中需要合并或重新定义

## 数据质量评估

- **来源可靠性**: ★★★★★ — MITRE FFRDC开发，政府委托，公开发布
- **内容深度**: ★★★★★ — 33页完整技术简报，包含模块定义、数据模型、活动图等
- **时效性**: ★★★★☆ — 2023年6月发布，V1.1版本
- **独特价值**: 这是DEWS MOSA RA最完整的公开技术文档，远超之前的幻灯片摘要

## 相关页面

- [[DEWS-MOSA参考架构]] — DEWS MOSA RA概念页面（将更新）
- [[MOSAIC方法]] — MOSA总体方法论
- [[SOSA参考架构V2]] — SOSA参考架构，DEWS整合的核心标准
