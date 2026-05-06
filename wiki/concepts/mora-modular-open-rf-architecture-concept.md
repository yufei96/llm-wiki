---
title: "模块化开放射频架构（MORA）"
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: [MORA, 射频, CMOSS, SOSA, MOSA, 开放架构, RF链]
sources: [raw/articles/mora-modular-open-rf-architecture.md, raw/articles/navair-mosa-overview.md]
---

# 模块化开放射频架构（MORA）

## 摘要

模块化开放射频架构（Modular Open RF Architecture, MORA）是CMOSS标准套件中的射频架构标准，旨在将整个RF链（从天线到数字处理）标准化为开放、模块化的架构。MORA从VICTORY（车辆C4ISR/EW互操作性）架构衍生而来，于2015年GVSETS上以v1.0首次推出，经行业协作演进到v2.3（2019年）。MORA填补了CMOSS中**RF链标准化**的空白。

## 核心目标

- 标准化RF链的**全部环节**（不仅限于前端）
- 以开放和模块化方式替代专有RF集成
- 支持CMOSS的Universal A-Kit中RF组件的互换
- 使通信、电子战、信号情报系统能够共享天线和放大器资源

## 核心特点

- **全链路标准化**：覆盖从天线→射频前端→放大器→数字处理的完整RF链
- **资源共享**：多个功能系统（通信、EW、SIGINT）可共享天线和放大器
- **模块化RF前端**：RF组件可独立替换，不影响系统其他部分
- **CMOSS集成**：MORA是CMOSS标准套件的RF组件层
- **VICTORY衍生**：从车辆C4ISR互操作架构演进而来

## 在CMOSS/SOSA中的角色

MORA在CMOSS标准套件中的定位：

```
CMOSS标准套件

VICTORY  = 数据总线和系统互操作
MORA     = 射频前端和链路标准化
SOSA     = 传感器模块化（包含RF）
OpenVPX  = 硬件卡板标准
VITA     = 物理层标准
```

MORA与SOSA的关系：
- SOSA定义传感器模块化架构，MORA定义RF链内部标准
- MORA侧重RF前端资源共享，SOSA侧重传感器子系统整体架构
- 两者共享OpenVPX/VITA硬件基础

## 三军互操作性演示验证

NAVAIR PMA-209与陆军PEO Aviation、AFLCMC合作的TSOA-ID演示中：
- MORA和Redhawk/TOA解码RF信号，发布到OMS/UCI
- MORA与HOST、FACE标准集成，实现RF信号的端到端处理
- 验证了MORA在多军种、多平台环境下的互操作能力

## 标准演进

- **2015年**：MORA v1.0在GVSETS首次发布
- **2019年**：MORA v2.3，行业、学术和政府合作伙伴协作演进
- **持续迭代**：MOSA标准是**活的**——通过行业协作持续改进

## 与其他标准的关系

- [[sosa-sensor-open-systems-architecture]] — SOSA定义传感器模块化架构，MORA定义RF链内部标准
- [[cmoss-overview-2022]] — MORA是CMOSS标准套件的RF组件层
- [[host-hardware-open-systems]] — HOST定义嵌入式计算硬件，MORA定义RF硬件
- [[mosa-defense-acquisition]] — MORA是MOSA在射频领域的具体实施
- [[victory-ground-vehicle]] — VICTORY是MORA的源头架构
- [[open-mission-systems]] — MORA处理的RF数据通过OMS/UCI发布

## 笔记

- MORA的独特价值在于"全链路"——不只是天线标准化，而是从天线到数字处理的整个RF链
- MORA从v1.0到v2.3的演进证明了MOSA标准的活力
- 在三军互操作演示中，MORA是RF信号处理的核心标准，与HOST/SOSA硬件和FACE软件配合实现端到端集成

---

*基于MORA论文（Broczkowski等, 2019）、NAVAIR MOSA概述和三军互操作演示综合整理。2026-05-06创建。*
