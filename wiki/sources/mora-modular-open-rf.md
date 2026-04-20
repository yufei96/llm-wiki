---
title: "MORA — 模块化开放射频架构"
date: 2026-04-19
type: source_summary
source: raw/papers/mora-modular-open-rf-architecture.pdf
author: "Jason Broczkowski, Derek Bailey, Troy Ryder, Jason Dirner"
tags: [MORA, 射频, CMOSS, VICTORY, GVSETS]
---

# MORA — 模块化开放射频架构

## 文档概况
- **全称**：Modular Open RF Architecture (MORA): Standardizing the RF Chain
- **发布场合**：2019 NDIA Ground Vehicle Systems Engineering and Technology Symposium (GVSETS)
- **作者**：Jason Broczkowski (ASRC Federal), Derek Bailey, Troy Ryder, Jason Dirner (DEVCOM C5ISR)
- **日期**：2019年8月13-15日
- **页数**：8
- **版本**：MORA规范当时为v2.3

## 核心内容

MORA是CMOSS标准套件中的**射频架构标准**，旨在将整个RF链（从天线到数字处理）标准化为开放、模块化的架构。

### 定位
MORA从VICTORY（车辆C4ISR/EW互操作性）架构衍生而来，于2015年GVSETS上以v1.0首次推出，经过行业、学术和政府合作伙伴的协作演进到v2.3。

### 核心目标
- 标准化RF链的**全部环节**（不仅限于前端）
- 开放和模块化的方式替代专有RF集成
- 支持CMOSS的Universal A-Kit中RF组件的互换

### MORA在CMOSS中的角色
CMOSS套件中：
- **VICTORY** = 数据总线和系统互操作
- **MORA** = 射频前端和链路标准化
- **SOSA** = 传感器模块化（包含RF）
- **OpenVPX/VITA** = 硬件卡板标准

MORA填补了CMOSS中**RF链标准化**的空白，使通信、电子战、信号情报系统能够共享天线和放大器资源。

## 对MOSA的意义

MORA是MOSA在**射频领域**的具体实施。CMOSS概述文档中提到"共享天线和放大器"，MORA就是实现这一承诺的技术标准。

MORA从v1.0到v2.3的演进（2015-2019）证明了MOSA标准是**活的**——通过行业协作持续改进，而非一次性文档。

## 相关内容
- [[cmoss-overview-2022]] — CMOSS（MORA是其RF组件）
- [[mosa-defense-acquisition]] — MOSA概念
- [[victory-ground-vehicle]] — VICTORY（MORA的源头架构）
- [[dsp-journal-mosa-2020]] — DSP Journal综述

---
*8页。MOSA RF标准生态的最后一块拼图。*
