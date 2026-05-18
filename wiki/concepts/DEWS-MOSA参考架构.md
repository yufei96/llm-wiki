---
title: "定向能武器系统MOSA参考架构（DEWS MOSA RA）"
created: 2025-04-26
updated: 2026-04-26
type: concept
tags: [MOSA, 定向能武器, 参考架构, SOSA, MITRE, DEWS, MBSE, 数字工程]
sources:
  - /root/mosa-defense-applications/results/DEWS_MOSA参考架构.json
  - raw/papers/mitre-dews-mosa-ra.pdf
confidence: EXTRACTED
evidence: "基于原始文档综合"
---

# 定向能武器系统MOSA参考架构（DEWS MOSA RA）

## 概述

定向能武器系统MOSA参考架构（DEWS MOSA RA）是首个为定向能（DE）武器系统领域制定的通用开放系统架构参考框架，由MITRE Corporation受OUSD(R&E)委托开发。该架构旨在为高能激光（HEL）和高功率微波（HPM）系统提供统一的模块化架构指导，V1.0于2022年7月正式发布，V1.1于2023年更新。架构正在通过SOSA联盟DEWS分委员会进行与 [[SOSA参考架构V2]] 的整合。

## 要点

### 架构核心理念

DEWS MOSA RA基于五大愿景目标：
1. **广泛适用** — 与运行环境和宿主平台无关
2. **基于MOSA原则** — 利用开放/商业标准，非专有、供应商无关
3. **加速创新交付** — 采用"灰盒"（Gray Box）概念，为近远期技术提供替代插入方法
4. **增加复用** — 促进向后兼容和跨武器组合的可移植模块应用
5. **加快采办** — 减少传统集成测试时间

### 约20个功能模块

DEWS MOSA RA将定向能武器系统功能聚合为约20个定义明确的功能模块：

**管理与控制：**
- 系统监控器、火控、DEWS管理

**感知与跟踪：**
- 摄像头、追踪器、综合传感器、航迹管理器、外部数据导入器

**波束生成与导向：**
- DE源（产生电磁能量）、波束传输、波束导向器

**安全与接口：**
- 冲突解除安全、本地操作员HMI、宿主平台接口

**支持服务：**
- 安全服务、数据存储、支持服务、热管理、电力、支持系统操作

### "灰盒"概念

架构定义模块和接口**做什么**（功能），不定义**如何做**（实现）。这种"灰盒"方法：
- 保护供应商IP——模块内部实现保留为供应商专有
- 促进竞争——供应商在模块边界内保留完全技术自由度
- 支持技术插入——新旧技术可在模块内部替换而不影响接口

### 架构开发方法论

开发流程遵循"接口服务于模块"原则，依次经过：
利益相关者需求 → 质量属性 → 用例 → 架构原则 → 功能详细列表 → 功能聚合准则 → 模块定义 → 模块I/O需求 → 接口定义 → 示例 → 数字模型

### SOSA整合

SOSA整合过程中形成了三类模块：
1. **DEWS-SOSA通用模块**（12个：系统管理/监控、任务管理/火控、外部数据导入、追踪/航迹管理、安全服务、存储、导航数据/支持服务、电力、宿主平台接口等）
2. **DEWS专用模块**（7个：本地操作员HMI、本地传感器、冲突解除安全、DE源、波束传输、波束导向器、热管理）
3. **SOSA专用模块**（13个：发射器/收集器、信号检测器/提取器、信号表征器、态势评估器、影响评估器等）

整合面临的主要挑战：模块语义对齐、功能合并、消息/数据模型统一、领域特异性模块映射。

### 关键技术差异（DEWS vs SOSA Power模块）

- DEWS开机过程与SOSA（高度机箱导向）不同
- DEWS储能关注能量浪涌（高功率脉冲需求），SOSA储能关注间歇断电时的延续
- 部分SOSA功能在DEWS中需要合并或重新定义

### 质量属性优先级

模块性 > 可升级性 > 可移植性 > 可扩展性 > 互操作性 > 安全性 > 可靠性 > 可配置性 > 弹性 > 可部署性

### 数字工程集成

使用Digital Cameo模型（Dassault Systems CATIA Cameo Enterprise Architecture 19.0 SP4 / MSOSA）进行架构建模，创建可执行的架构数字模型。架构开发过程与MBSE方法论一致。

V1.1交付物包含：参考架构文档（MS Word）、Magic Draw数字模型、HTML提取、实施指南、RA评估、采办框架。

### 数据模型

Track消息数据对象包含详细API定义：
- **Acceleration**: x/y/z加速度分量（km/s²）
- **Aimpoint**: 瞄准点位置（XYZ、AzEl、LatLong坐标系）
- **ModeOfOperation**: AUTOMATIC / SEMI_AUTOMATIC / MANUAL
- **Orientation**: yaw/pitch/roll（度）
- **Pose**: 位置与方向组合

### 开机序列

10步标准化开机序列：Power on → Power Distribution → Orderly Power On → System Initialization → H&S Reports → Report H&S → Receive Host Power → System Init (SMM) → Perform BIT → Monitor H&S

### 成本效益

核心效益包括：缩短研发到作战测试时间、通过增量升级延长服役寿命、通过规模经济扩展工业基础、跨项目/军种增加复用、对齐研发投入。OUSD(R&E)认为DEWS RA可"弯曲成本曲线"。

## 参考的在研定向能系统

架构开发参考了多军种定向能武器项目经验：

| 项目 | 军种 | 类型 | 域 | 主管 | 行业伙伴 |
|------|------|------|----|------|----------|
| Bane | 海军 | HPM | 陆 | Dahlgren DEW Office | |
| THOR | 空军 | HPM | 陆 | AFRL | BAE, Leidos, Verus |
| DE-MSHORAD | 陆军 | HEL | 陆 | RCCTO | Kord |
| IFPC-HEL | 陆军 | HEL | 陆 | RCCTO/OSD/SMDC | Dynetics, LMC, MZA |
| HiJENKS | 海军/空军 | HPM | 空 | Dahlgren/Kirtland | LMC |
| SHiELD | 空军 | HEL | 空 | AFRL | LMC |
| HELIOS | 海军 | HEL | 海 | PEO IWS 2 | LMC |
| SSL-TM | 海军 | HEL | 海 | Dahlgren | Northrop Grumman |

## 相关内容

- [[开放架构层级]] — 开放架构四层体系（DEWS RA为分系统级）
- [[WOSA武器开放系统架构]] — WOSA武器系统架构（常规武器分系统标准）
- [[SOSA传感器开放系统架构]] — SOSA传感器架构，DEWS RA整合的核心标准
- [[CMOSS模块化标准概述]] — CMOSS标准概述，与SOSA同属开放标准体系
- [[MOSAIC方法]] — MOSA总体方法论
- [[MOSA五支柱评估]] — OUSD(R&E) MOSA五大支柱评估框架
- [[MOSA棕地与绿地对比]] — DEWS RA主要面向greenfield应用
- [[DoDI-5000.85重大能力收购]] — DoDI 5000.85 重大能力采办
- [[GAO-MOSA专项审查报告全文]] — GAO MOSA专项审查报告
- [[诺格公司-洞察开放处理器]]

## 笔记

DEWS MOSA RA的独特之处在于：它是首个由政府（通过MITRE FFRDC）主导开发的特定武器领域参考架构，而非依赖行业标准组织。"灰盒"概念是对传统"黑盒"（完全不透明）和"白盒"（完全透明）方法的折中，在IP保护与开放竞争之间找到了平衡点。RFI阶段即吸引了13家公司的300+条意见，表明行业对该架构的广泛关注。值得注意的是，架构本身的采用也面临障碍——已有DE项目在架构发布前已启动开发，重构成本高，且各军种独立开发文化导致跨军种架构统一的政治阻力。

2023年6月Kitty Hawk Week完整技术简报（MITRE PRS-23-1891）提供了远超幻灯片摘要的详细技术内容，包括完整的模块定义、函数封装示例、数据模型API、开机序列活动图和SOSA整合的详细函数级对比。
