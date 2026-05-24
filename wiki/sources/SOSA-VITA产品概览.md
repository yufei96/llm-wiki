---
title: "SOSA VITA产品概览 — 传感器开放系统架构硬件指南"
created: 2026-04-19
updated: 2026-05-21
tags: [SOSA, VITA, OpenVPX, Elma, 硬件标准, 模块化, 传感器]
source: [raw/papers/SOSA VITA产品能力.pdf, raw/articles/SOSA VITA产品能力.md]
confidence: EXTRACTED
type: source
---

# SOSA VITA产品概览 — 传感器开放系统架构硬件指南

## 概述

Elma Electronic发布的**SOSA产品概览和技术指南**。Elma是VITA/SOSA/PICMG等开放标准的关键参与者和贡献者，在航空、地面和舰载平台的加固解决方案方面有长期积累。本文档将SOSA技术标准映射到**实际可采购的硬件产品**——从机箱、背板到模块和互连。

## SOSA标准概述

SOSA核心硬件规范基于**VITA 65（OpenVPX）**——一种广泛采用的加固高性能计算架构和外形标准。OpenVPX标准族定义了模块级系统级互操作性：

| 标准 | 描述 |
|------|------|
| VITA 46.0 | VPX基础规范 |
| VITA 46.4 | PCI Express on VPX |
| VITA 46.6 | 千兆以太网控制平面 on VPX |
| VITA 46.7 | 10千兆以太网 on VPX |
| VITA 46.9 | XMC映射后I/O on VPX |
| VITA 46.10 | VPX后传输模块（RTM） |
| VITA 46.30/31 | 更高数据速率VPX |
| VITA 42 | XMC夹层卡 |
| VITA 17.3 | sFPDP Gen 3.0串行前面板数据端口 |

## MOSA五步实施

Elma引用DoD MOSA实施五步：

1. **建立使能环境**（Establish Enabling Environment）
2. **采用模块化设计**（Employ Modular Design）
3. **指定关键接口**（Designate Key Interfaces）
4. **使用开放标准**（Use Open Standards）
5. **认证一致性**（Certify Conformance）

## 法律与政策背景

- 2019年三军备忘录要求未来武器系统采用开放标准
- MOSA已编入美国法典（10 USC 2446a）：2019年1月1日后MDAP"应使用MOSA设计和开发"
- SOSA被三军备忘录**点名**为关键使能标准

## Elma在SOSA生态中的角色

- VITA标准组织（VSO）成员——ANSI认可的标准开发组织
- 多个VITA工作组的**关键贡献者**
- 为SOSA提供从机箱、背板到模块的**完整硬件解决方案**

## 笔记

- 此文档来自硬件供应商（Elma）——与The Open Group的SOSA标准文档（纯规范）互补
- 产品概览将"标准"转化为"可采购的硬件"——对项目经理的实用价值高
- VITA标准的全面列表是本文档的独特贡献——一目了然地展示SOSA的硬件标准基础
