---
title: "开放架构层次体系：从平台到部组件的四层结构"
created: 2026-05-06
updated: 2026-05-06
type: comparison
tags: [开放架构, MOSA, 层次结构, OMS, WOSA, SOSA, FACE, HOST, MORA, DEWS, CMOSS, VICTORY, UCS, GRA, AMS, A-GRA, ABMS, COARPS, SCARS, R-EGI, NC3, Sentinel, CFW]
sources:
  - raw/articles/Chris-Garrett-Presentation-Sep-2024.md
  - raw/articles/Tri-Service-Memo-Signed-17Dec2024.md
  - raw/articles/defense-news-open-standards-2024.md
  - raw/articles/dau-next-gen-acquisition-2024.md
  - raw/articles/crs-nc3-if11697.md
  - raw/articles/crs-sentinel-icbm-if11681.md
  - raw/articles/afrc-a-gra-cca-validation-2025.md
  - raw/articles/dvids-r-egi-pnt-flight-2024.md
  - raw/articles/usaf-coarps-rfi-2021.md
  - raw/articles/ntsa-scars-stcf-2025.md
  - raw/articles/navair-osmp-guide-v1-2025.md
---

# 开放架构层次体系：从平台到部组件的四层结构

## 概述

美国国防部的开放系统架构不是扁平的——它们存在明确的**层次关系**，从平台级到部组件级逐层分解。本页覆盖21种已识别的开放架构实现，理解这个层次对于系统架构设计、采办策略和技术集成至关重要。

## 四层结构总览（21种实现）

```
┌─────────────────────────────────────────────────────────────────┐
│  第1层：平台级（Platform）                                       │
│  OMS/UCI · UCS/STANAG 4586 · ABMS GRA                          │
├─────────────────────────────────────────────────────────────────┤
│  第2层：分系统级（Subsystem）                                    │
│  WOSA · DEWS MOSA RA · NC3 GRA · Sentinel GRA · CFW ICD        │
├─────────────────────────────────────────────────────────────────┤
│  第3层：设备级（Equipment/Unit）                                 │
│  SOSA · MORA · CMOSS · VICTORY · AMS GRA · A-GRA               │
│  PNT GRA/R-EGI · COARPS · SCARS · Mission Planning GRA         │
├─────────────────────────────────────────────────────────────────┤
│  第4层：部组件级（Component）                                    │
│  FACE · HOST                                                    │
└─────────────────────────────────────────────────────────────────┘
```

## 第1层：平台级

定义整个平台（飞机、无人机、指控系统）的任务系统架构和互操作框架。

**OMS/UCI（开放任务系统/通用指挥控制接口）**
- **定义域**：航空任务系统
- **核心角色**：抽象服务总线（ASB）隔离器，连接FACE/SOSA/UAI等标准域
- **主导方**：美国空军
- **应用**：F-35、B-21、CCA、ABMS
- **概念页**：[[open-mission-systems]]

**UCS/STANAG 4586（无人系统指控标准）**
- **定义域**：无人系统指挥控制（UAV/UGV/UUV）
- **核心角色**：五级互操作性接口（LOI 1-5）
- **主导方**：NATO
- **概念页**：[[ucs-control-station]]

**ABMS GRA（先进战斗管理系统）**
- **定义域**：空中C2/作战管理
- **核心角色**：DAF BATTLE NETWORK核心，CJADC2空军贡献
- **主导方**：空军部PEO C3BM
- **五大产品**：数字基础设施、可部署系统（TOC-L）、软件和应用（CBC2）、空中网络、远程火力
- **主承包商**：SAIC（CBC2）
- **概念页**：[[abms-gra-advanced-battle-management]]

## 第2层：分系统级

定义武器、核C3、导航等功能分系统的内部模块化架构和接口标准。

**WOSA（武器开放系统架构）**
- **定义域**：常规武器系统
- **核心角色**：武器分系统模块化接口标准
- **主导方**：跨军种
- **应用**：超音速武器、SiAW、CCA武器集成
- **概念页**：[[wosa-weapons-open-systems-architecture]]

**DEWS MOSA RA（定向能武器MOSA参考架构）**
- **定义域**：定向能武器系统（HEL/HPM）
- **核心角色**：约20个功能模块的参考框架
- **主导方**：MITRE/OUSD(R&E)
- **概念页**：[[dews-mosa-reference-architecture]]

**NC3 GRA（核指挥控制通信）**
- **定义域**：核C3系统
- **核心角色**：约204个地面/空间/机载系统的架构框架
- **主导方**：US STRATCOM / OSD
- **预算**：FY2025 $11.4B请求；CBO估计2025-2034 $154B
- **关键元素**：PAVE PAWS、PARCS、COBRA DANE雷达；SBIRS天基红外；AEHF通信；TACAMO；SAOC
- **概念页**：[[nc3-gra-nuclear-c3]]

**Sentinel GRA（LGM-35A洲际弹道导弹）**
- **定义域**：洲际弹道导弹系统
- **核心角色**：替代Minuteman III，采用开放系统架构支持全生命周期改进
- **主导方**：空军 / Northrop Grumman
- **规模**：634枚导弹（400枚部署），FY2026 $4.1B RDT&E
- **里程碑**：Nunn-McCurdy违规，里程碑B撤销，2030s IOC目标
- **概念页**：[[sentinel-gra-icbm]]

**CFW ICD（通用火力控制接口控制文档）**
- **定义域**：武器火力控制接口
- **核心角色**：跨武器平台的通用火力控制接口标准
- **主导方**：Army ARDEC / 跨军种
- **与UAI关系**：CFW ICD是UAI体系的具体接口文档
- **来源页**：[[ndia-cfw-icd-wright-2015]]、[[samgov-uai-rfi]]

## 第3层：设备级

定义传感器、射频、C5ISR套件、自主模块等设备/子系统的硬件和集成标准。

**SOSA（传感器开放系统架构）**
- **定义域**：传感器子系统（雷达、EO/IR、SIGINT、EW）
- **核心角色**：传感器硬件模块化标准，GRA中几乎所有功能域的硬件基座
- **主导方**：The Open Group
- **概念页**：[[sosa-sensor-open-systems-architecture]]

**MORA（模块化开放射频架构）**
- **定义域**：RF链（天线→射频前端→数字处理）
- **核心角色**：RF链全链路标准化
- **主导方**：NDIA GVSETS / DEVCOM C5ISR
- **概念页**：[[mora-modular-open-rf-architecture-concept]]

**CMOSS（C5ISR/EW模块化开放标准套件）**
- **定义域**：C5ISR/EW通用硬件平台
- **核心角色**：整合MORA+VICTORY+SOSA+VITA为Universal A-Kit
- **主导方**：DEVCOM C5ISR Center
- **来源页**：[[cmoss-overview-2022]]

**VICTORY（车辆C4ISR/EW互操作性）**
- **定义域**：地面战术车辆
- **核心角色**：以太网数据总线+SOAP/XML数据发布
- **主导方**：美国陆军
- **来源页**：[[victory-ground-vehicle]]

**AMS GRA（敏捷任务套件）**
- **定义域**：NGAD/CCA下一代空中优势体系
- **核心角色**："Software Defined and Hardware Enabled"的政府参考架构
- **主导方**：空军
- **应用**：CCA增量2国际合作核心架构
- **合规产品**：NG InSight处理器（OMS UCI 2.0 + SOSA + AMS-GRA）
- **概念页**：[[ams-gra-agile-mission-suite]]

**A-GRA（自主政府参考架构）**
- **定义域**：自主系统/CCA任务自主
- **核心角色**：政府拥有的模块化开放框架，建立通用自主标准
- **主导方**：空军
- **应用**：RTX Collins + Shield AI集成，General Atomics YFQ-42 / Anduril YFQ-44半自主飞行测试
- **战略意义**：防止供应商锁定，构建竞争生态系统
- **概念页**：[[a-gra-autonomy-reference-architecture]]

**PNT GRA / R-EGI（弹性嵌入式GPS/INS）**
- **定义域**：定位导航授时（PNT）
- **核心角色**：政府拥有的PNT开放架构，支持GPS拒止环境替代导航
- **主导方**：AFLCMC/WNX
- **关键里程碑**：F-16 LRU试飞成功，C-12J试飞成功，AEVEX LynxVBN视觉导航即插即用集成
- **设计代理**：IS4S、Kearfott、GD-Mission Systems、Collins Aerospace
- **概念页**：[[pnt-gra-r-egi]]

**COARPS（通用开放架构雷达程序规范）**
- **定义域**：雷达系统
- **核心角色**：开放雷达架构规范，使雷达子系统可独立采购
- **五大目标**：独立采购、硬件刷新不重写软件、第三方模式插入、缩短模式获取时间、标准化流程
- **主导方**：AFLCMC/HBSA（Hanscom AFB）
- **起源**：2019年ABMS GMTI项目
- **概念页**：[[coarps-radar-architecture]]

**SCARS（模拟器通用架构需求标准）**
- **定义域**：空军训练模拟器
- **核心角色**：增量建立MOSA标准，改善网络弹性，最小化全生命周期成本
- **主导方**：HAF/A3T
- **主承包商**：CAE USA
- **范围**：50+平台、2380+训练设备、7个MAJCOM
- **概念页**：[[scars-simulator-architecture]]

**Mission Planning GRA（任务规划）**
- **定义域**：任务规划系统
- **来源**：Garrett演示中提及，信息有限
- **主导方**：AFLCMC/C3BM任务规划部门

## 第4层：部组件级

定义软件可移植性、硬件基础标准等底层规范。

**FACE（未来机载能力环境）**
- **定义域**：航电软件
- **核心角色**：软件组件跨平台/跨供应商可移植性
- **主导方**：The Open Group
- **概念页**：[[face-technical-standard]]

**HOST（硬件开放系统技术）**
- **定义域**：高性能嵌入式计算硬件
- **核心角色**：嵌入式计算平台架构框架
- **主导方**：NAVAIR PMA-209
- **概念页**：[[host-hardware-open-systems]]

## 管理流程（非架构标准）

**OSMP（开放系统管理计划）**
- **性质**：MOSA实施管理流程文档，不是架构标准
- **核心角色**：海军MOSA实施的"活的参考文件"
- **主导方**：NAVAIR
- **关键变化**：从"承包商撰写"转为"海军内部撰写"初稿
- **包含标准**：AMS-GRA、FACE、OMS、SOSA、WOSA、UCI等
- **来源页**：[[navair-osmp-guide-v1-2025]]、[[military-embedded-navy-osmp-2025]]

## GRA体系架构模式

[[government-reference-architectures|政府参考架构（GRA）]]是横跨各层次的架构模式——政府拥有架构定义权，通过标准化接口促进竞争。AFMC的GRA体系（Chris Garrett演示，2024.9）包含：

**功能GRA映射到四层结构：**
- **平台级**：ABMS GRA（空中C2）
- **分系统级**：武器GRA（WOSA）、NC3 GRA、Sentinel GRA
- **设备级**：传感器GRA（SOSA+OMS）、PNT GRA（R-EGI）、COARPS（雷达）、AMS GRA（任务套件）、A-GRA（自主）、SCARS（模拟器）、Mission Planning GRA
- **部组件级**：FACE、HOST

**GRA目标架构（Garrett演示）：**
```
武器(WOSA)  传感(COARPS)  通信    自主(A-GRA)  PNT(R-EGI)
    │           │          │         │           │
    └───────────┴──────────┴─────────┴───────────┘
                          │
              OMS（ASB隔离器）
                          │
                    ┌─────┴─────┐
                    │  FACE     │  Aircraft (safety critical)
                    │  SOSA H/W │  Mission Functions
                    │  CMOSS    │  Universal A-Kit
                    └───────────┘
```

## 层次间关系

### 纵向依赖（上层依赖下层）

```
OMS（平台级）──运行在──→ SOSA H/W（设备级）
OMS（平台级）──通过UAI──→ WOSA（分系统级）
OMS（平台级）──通过TSS──→ FACE（部组件级）
ABMS GRA（平台级）──使用──→ COARPS/AMS GRA/A-GRA（设备级）
UCS（平台级）──集成──→ SOSA/CMOSS（设备级）
Sentinel GRA（分系统级）──可能采用──→ SOSA/OMS（设备级/平台级）
FACE（部组件级）──运行在──→ HOST（部组件级）
R-EGI（设备级）──即插即用──→ 第三方PNT传感器
```

### 横向互补（同层协作）

- **WOSA ↔ DEWS RA ↔ CFW ICD**：常规武器/定向能/火力控制接口
- **NC3 GRA ↔ Sentinel GRA**：核C3系统 ↔ 洲际导弹
- **SOSA ↔ MORA ↔ CMOSS ↔ VICTORY**：传感器/射频/通用套件/车辆
- **AMS GRA ↔ A-GRA ↔ COARPS ↔ R-EGI**：任务套件/自主/雷达/PNT
- **FACE ↔ HOST**：软件层 ↔ 硬件层

## 跨平台对比

| 平台类型 | 平台级 | 分系统级 | 设备级 | 部组件级 |
|----------|--------|----------|--------|----------|
| **军用航空** | OMS | WOSA/DEWS | SOSA/MORA/AMS/A-GRA/COARPS/R-EGI | FACE/HOST |
| **战略核力量** | — | NC3 GRA/Sentinel GRA | — | — |
| **地面车辆** | — | — | CMOSS/VICTORY | VITA/OpenVPX |
| **无人系统** | UCS | — | SOSA/CMOSS/A-GRA | FACE/HOST |
| **训练模拟** | — | — | SCARS | — |
| **舰载系统** | OMS | WOSA | SOSA/MORA | HOST |

## 标准治理模式

| 标准 | 治理模式 | 持有方 |
|------|----------|--------|
| OMS/UCI | 军种主导 | 美国空军 |
| UCS | 多国标准化 | NATO |
| ABMS GRA | 军种主导 | 空军部PEO C3BM |
| WOSA | 跨军种 | DoD |
| DEWS RA | FFRDC开发 | MITRE/OUSD(R&E) |
| NC3 GRA | 跨组织 | US STRATCOM / OSD |
| Sentinel GRA | 军种+主承包 | 空军 / Northrop Grumman |
| CFW ICD | 跨军种 | Army ARDEC |
| SOSA | 行业联盟 | The Open Group |
| MORA | 行业协作 | NDIA GVSETS |
| CMOSS | 军种主导 | DEVCOM C5ISR Center |
| VICTORY | 军种主导 | 美国陆军 |
| AMS GRA | 军种主导 | 空军 |
| A-GRA | 军种主导 | 空军 |
| PNT GRA/R-EGI | 军种主导 | AFLCMC/WNX |
| COARPS | 军种主导 | AFLCMC/HBSA |
| SCARS | 军种主导 | HAF/A3T / CAE USA |
| FACE | 行业联盟 | The Open Group |
| HOST | 军种主导 | NAVAIR PMA-209 |
| OSMP | 军种内部 | NAVAIR |

## 三军联合确认

2024年12月三军联合备忘录确认的6大已验证标准：
1. **OMS/UCI** — 平台级
2. **WOSA** — 分系统级
3. **SOSA** — 设备级
4. **FACE** — 部组件级
5. **AMS GRA** — 设备级（新确认）
6. **VICTORY** — 设备级

## 相关页面

### 概念页（按层次）
- [[open-mission-systems]] — OMS（平台级）
- [[ucs-control-station]] — UCS（平台级）
- [[abms-gra-advanced-battle-management]] — ABMS GRA（平台级）
- [[wosa-weapons-open-systems-architecture]] — WOSA（分系统级）
- [[dews-mosa-reference-architecture]] — DEWS RA（分系统级）
- [[nc3-gra-nuclear-c3]] — NC3 GRA（分系统级）
- [[sentinel-gra-icbm]] — Sentinel GRA（分系统级）
- [[sosa-sensor-open-systems-architecture]] — SOSA（设备级）
- [[mora-modular-open-rf-architecture-concept]] — MORA（设备级）
- [[ams-gra-agile-mission-suite]] — AMS GRA（设备级）
- [[a-gra-autonomy-reference-architecture]] — A-GRA（设备级）
- [[pnt-gra-r-egi]] — PNT GRA/R-EGI（设备级）
- [[coarps-radar-architecture]] — COARPS（设备级）
- [[scars-simulator-architecture]] — SCARS（设备级）
- [[face-technical-standard]] — FACE（部组件级）
- [[host-hardware-open-systems]] — HOST（部组件级）

### Source页
- [[dau-next-gen-acquisition-2024]] — DAU演示（全GRA清单）
- [[afrc-a-gra-cca-validation-2025]] — A-GRA/CCA验证
- [[csis-mosa-burden-sharing-2025]] — CSIS AMS GRA/A-GRA分析
- [[crs-nc3-if11697]] — NC3 CRS入门
- [[crs-sentinel-icbm-if11681]] — Sentinel CRS入门
- [[dvids-r-egi-pnt-flight-2024]] — R-EGI飞行演示
- [[usaf-coarps-rfi-2021]] — COARPS RFI
- [[ntsa-scars-stcf-2025]] — SCARS 2025简报
- [[navair-osmp-guide-v1-2025]] — OSMP实施指南

### 分析与框架页
- [[government-reference-architectures]] — GRA架构模式（横跨各层）
- [[c5isr-standards-convergence]] — C5ISR标准趋同分析
- [[six-validated-mosa-standards]] — 三军6大已验证标准
- [[mosa-implementation-stack]] — MOSA实施全栈
- [[interface-engineering-evolution]] — 接口工程三层演进
- [[modular-architecture-patterns]] — 模块化架构模式

### 应用案例
- [[mosa-cca-application]] — CCA中的MOSA应用
- [[siaw-aargm-er-mosa-contrast]] — SiAW vs AARGM-ER对比
- [[xm30-micv-mosa]] — XM-30地面车辆MOSA设计

## 笔记

- 四层结构是理解MOSA标准生态的关键框架——21种实现均可定位到具体层次
- OMS的"ASB隔离器"角色是架构设计的核心决策——它使各层可以独立演进
- GRA体系是MOSA在架构层面的具体实施——政府拥有架构定义权，通过标准化接口促进竞争
- AMS GRA和A-GRA是CCA项目的两个核心GRA，分别定义任务套件和自主标准
- NC3 GRA和Sentinel GRA是战略核力量领域的专用GRA，高度机密但已有CRS公开文档
- COARPS是雷达领域的开放架构规范，使雷达模式可从独立来源采购
- SCARS是训练模拟领域的MOSA实施，覆盖50+平台2380+设备
- R-EGI是PNT领域的政府开放架构，已成功验证GPS拒止环境下的即插即用
- CFW ICD/UAI是武器火力控制接口标准，与WOSA互补
- OSMP是海军MOSA管理流程，不是架构标准但包含所有架构标准的引用
- 跨平台对比揭示了地面/无人领域在平台/分系统级标准化的差距

---

*基于Chris Garrett AFMC演示、三军联合备忘录、DAU演示、CRS报告、DVIDS等综合整理。2026-05-06创建，持续更新。*
