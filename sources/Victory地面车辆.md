---
created: 2026-05-21
updated: 2026-05-21
confidence: EXTRACTED
type: source
title: VICTORY与GVA地面车辆现代化
tags:
  - VICTORY
  - GVA
  - NGVA
  - 地面车辆
  - C4ISR
  - MOSA
  - 开放架构
  - Curtiss-Wright
---

## 概述

本文是Curtiss-Wright Defense Solutions于2019年发布的技术白皮书，系统阐述了美国陆军VICTORY（Vehicle Integration for C4ISR/EW Interoperability）和英国国防部GVA（Generic Vehicle Architecture）两种地面车辆电子架构标准的背景、技术路径和差异。文档聚焦如何通过COTS开放标准解决战术地面车辆C4ISR系统"螺栓式附加"、供应商锁定和SWaP冗余问题。

## 核心内容

### 问题背景

传统战术地面车辆在升级C4ISR能力时采用"螺栓附加"（bolt-on）方式，引入大量专有接口的独立电子设备，导致：多个独立GPS接收机和HMI外设冗余部署、系统间无法共享数据、占用车内宝贵空间、增加操作员负担。烟囱式采办流程使得每个新能力都携带独立机箱、线缆、键盘等组件。

### VICTORY标准

由美国陆军PEO C3T于2010年启动，定义C4ISR/EW系统间开放标准物理和逻辑接口。核心特征：基于以太网的VICTORY数据总线（VDB）、基于SOAP/XML的Web服务通信、开源软件库支持COTS交换机与路由器——不规定LRU内部实现，仅规范LRU间互操作方式。目标：恢复车内空间、降低重量和功耗、实现平台系统信息共享、支持未来技术无缝插入。

### GVA标准

由英国国防部Def Stan 23-09定义，覆盖范围比VICTORY更广——不仅包括电子和电力基础设施，还包括机械接口、HMI和健康使用监测系统（HUMS）。采用DDS（Data Distribution Service）中间件实现发布/订阅式数据交换。GVA公开可获取，而VICTORY仅限美国公民用于美国项目。

### 关键差异对比

- **覆盖范围**：VICTORY专注C4ISR/EW系统；GVA覆盖全车电子系统（含物理接口、HMI、视频分发）
- **中间件**：VICTORY使用SOAP/XML；GVA使用DDS（OMG标准）
- **可访问性**：GVA从MOD网站免费获取；VICTORY受出口管制
- **认证**：VICTORY提供自测试套件；GVA无第三方认证机构，由开发者自行判定合规
- **理论互操作**：通过中间件转换可桥接两种框架，但完全互操作需多年发展

### 全球衍生标准

NATO GVA（NGVA）扩展GVA覆盖无人车辆等更广平台；澳大利亚AS GVA定义Land Data Model和DDS实现，案例：通用动力Ajax装甲车采用GVA数字架构，传感器和通信系统即插即用无需重新设计。

### 升级与新研

新系统若全面合规，未来地面车辆升级仅需插拔网络线缆即可更换角色能力。但现有系统升级仍需大量软件配置工作。

## 笔记

- VICTORY和GVA已成为DoD和MOD RFP中的事实标准条款，跨越"临界点"
- 合规声明存在模糊空间——声称"支持VICTORY"可能仅指硬件具备以太网和软件运行能力，实际合规需完整软件集成
- 白皮书代表Curtiss-Wright商业立场，其DBH-672/670数字滩头堡、GVDU任务显示器等产品定位为VICTORY/GVA现成解决方案
- MOSA政策与VICTORY/GVA目标一致，VICTORY是MOSA在地面车辆领域的具体实现
