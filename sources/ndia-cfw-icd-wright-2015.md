---
title: "Constructing Common Fire Control Across Weapon Platforms"
source_type: conference_presentation
source_org: "NDIA (National Defense Industrial Association)"
source_url: "https://ndia.dtic.mil/wp-content/uploads/2015/armament/tues17345_Wright.pdf"
date: 2015
downloaded: 2026-05-06
tags:
  - common-fire-control
  - CFW
  - ICD
  - open-architecture
  - MFCS
  - Army
  - ARDEC
  - modular-hardware
  - software-reuse
related_pages:
  - "[[open-architecture-hierarchy]]"
  - "[[common-fire-control]]"
  - "[[mfcs]]"
  - "[[ardec]]"
data_quality: medium-high
---

# NDIA 2015 — Constructing Common Fire Control Across Weapon Platforms

## 核心内容

- **主题**: 跨武器平台构建通用火力控制（Common Fire Control）系统
- **作者**: Michael Wright, Ralph Tillinghast, Ross Arnold
- **机构**: US Army ARDEC, Fire Control Systems & Technology Directorate
- **分布**: Distribution Statement A（公开发布，无限制分发）

### 通用火力控制的目标

- 减少测试、成本、开发时间
- 提高可靠性、可支持性、互操作性
- 减少培训需求

### 当前状态

- 现有"通用火力控制"主要是**已有组件和软件的复用**
- 新系统开发后被视为独立系统
- 时间线展示了 2000-2014 年间的多个火控系统项目：MFCS-M, LHMBC, MCV, M777, PEFCS, MFCS-D, PLUMSS, M119A2, ADIM, AMPS, WULF

### 软件复用成本节约实例

| 项目 | 节约 |
|------|------|
| LHMBC 复用 MFCS 软硬件 | $2.4M / 18个月 |
| PEFCS 复用 | $9.59M / 36个月 |
| M777 Towed Artillery 数字化 | $5.5M / 36个月 |
| ONR/USMC EFSS Demo | $5.67M / 30个月 |
| MFCS(H) Heavy | $6M / 31个月 |

### 软件架构要点

- **通用后端架构**: 基于主干（Trunk Based）的模块化组件
- 模块化组件：MET（气象数据）、FSCM（火力支援协调措施）、PI（外设接口）、Comm-Network、GeoTrans（大地坐标转换）、Mapping、UI/SMI
- 平台适配：可适配源码、模块化运行环境（Net Warrior）、云基础考量

### 硬件架构要点

- **ICD 控制**: 预定义软硬件接口控制文档（ICD）
- **ICD 解释器组件**: 硬件通信标准适配层，设计在电缆后壳中
- 灵活/模块化硬件：模块化计算机、手持设备+坞站、标准化线缆
- 以太网贯穿线缆，通过解释器适配旧接口（RS232, RS485）
- 电源统一 24V，通过解释器降压

### 程序管理挑战

- 多个需求文档、需求重叠
- 通用 CPD/KPP
- 政府拥有 vs 承包商基于
- 多个 PM（各有独特项目时间线）
- 多个院校（School Houses）
- 跨军种（Army, USMC, Navy, Air Force）

## 关键人员

| 姓名 | 职位 |
|------|------|
| Michael Wright | Presenter |
| Ralph Tillinghast | Co-author |
| Ross Arnold | Co-author, US Army ARDEC, RDAR-WSF-M |

## 数据质量评估

- **来源**: NDIA 会议演示文稿 PDF，经 DTIC 托管
- **限制**: 幻灯片格式，细节有限；为概念性讨论而非技术规范
- **价值**: 记录了跨平台通用火力控制的 ICD 方法和成本节约数据

## 相关页面

- [[open-architecture-hierarchy]] — 通用火力控制 ICD 是武器系统领域开放架构的早期实践
- [[common-fire-control]] — 通用火力控制概念
- [[mfcs]] — Mortar Fire Control System
- [[ardec]] — Army Research, Development and Engineering Center
