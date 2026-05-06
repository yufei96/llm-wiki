---
title: "SCARS STCF Brief — Simulators Common Architecture and Requirements (2025)"
source_type: conference_presentation
source_org: "NTSA (National Training & Simulation Association)"
source_url: "https://www.ntsa.org/-/media/sites/ntsa/events/2025/51a0/scars-stcf-brief.pdf"
date: 2025-04
event_date: 2025-04-16
downloaded: 2026-05-06
tags:
  - SCARS
  - simulator
  - MOSA
  - training
  - cybersecurity
  - CAE
  - USAF
  - OTI
  - sustainment
related_pages:
  - "[[open-architecture-hierarchy]]"
  - "[[scars]]"
  - "[[mosa-simulator]]"
  - "[[ca-e-usa]]"
data_quality: high
---

# NTSA SCARS STCF Brief — Simulators Common Architecture and Requirements (2025)

## 核心内容

- **SCARS** = Simulators Common Architecture and Requirements and Standards
- 日期：2025年4月16日，NTSA 会议
- **SCARS 是一个持续维护倡议**，旨在为空军模拟器逐步建立 **MOSA（模块化开放系统方法）**
- 程序发起人：**HAF/A3T**
- 支持的 MAJCOM：**ACC, AFGSC, AFRC, AFSOC, AMC, PACAF, USAFE**（共7个）
- 采购路径：Sustainment Initiative
- 主承包商：**CAE USA**
- 合同属性：**IDIQ**，5年基础订购期（2020-2025）+ 5个1年选项（2025-2030）

### 问题背景

- 超过 **2400 台训练设备**（50+ 平台），支持 9 个 MAJCOM
- 设备配置分散，复用性极低
- 网络威胁持续演进，RMF 合规成本高昂
- 训练系统对高保真度和互操作性的需求不断增加

### 三阶段方法

| 阶段 | 名称 | 内容 |
|------|------|------|
| Phase 1 | 高效网络安全 | 集中式漏洞扫描/补丁/防病毒/企业级 RMF 控制 |
| Phase 2 | 通用架构 | 功能迁移至通用基础设施，云/虚拟计算，通用建模和接口 |
| Phase 3 | 标准化应用 | 训练系统采用通用应用，仅硬件依赖软件为训练器专用 |

### 关键组件

- **Security Operations Center (SOC)** — 远程管理 OPE 和 WAN
- **On-Premise Equipment (OPE)** — 本地云托管仿真应用
- **WAN** — 利用现有合作伙伴网络
- **SCARS Standards** — 建立通用架构的基础

### SCARS 采用的行业标准

- OGC CDB (Common Database)
- SISO CIGI (Common Image Generator Interface)
- IoT (用于控制系统接口)
- ARINC-610C
- OMG SysML

### SCARS 内部标准

1. Basic On-premise Equipment Integration Standard
2. Common Security Controls Standard
3. Certification Process Standard
4. Application Certification Standard
5. Data Standard (含 MBSE Modeling Guide 和 Geospatial Data Spec)
6. DevSecOps Standard
7. Architecture Standard (MOSA 兼容模块化子系统和接口)

## 关键人员

| 姓名 | 职位 |
|------|------|
| Lt Col Virmil Delgadillo | Materiel Leader, Operational Training Infrastructure |
| Mr. Michael Baker | Chief Engineer, SCARS |

## 联系方式

- 标准请求：aflcmc.wns.scarsstandards@us.af.mil
- Innovation Cell：aflcmc.wns.sims_innovate@us.af.mil

## 数据质量评估

- **来源**: NTSA 官方会议简报 PDF，由项目负责人直接演示
- **限制**: 简报格式，部分细节需参考单独标准文件
- **价值**: 全面记录 SCARS 架构、三阶段路径、标准清单

## 相关页面

- [[open-architecture-hierarchy]] — SCARS 是 MOSA 在训练/仿真领域的实现
- [[scars]] — SCARS 项目详情
- [[mosa-simulator]] — MOSA 在模拟器中的应用
