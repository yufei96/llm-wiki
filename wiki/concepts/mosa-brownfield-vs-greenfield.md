---
title: "MOSA棕地改造与绿地新建（Brownfield vs Greenfield）"
created: 2025-04-26
updated: 2025-04-26
type: concept
tags: [MOSA, 棕地改造, 绿地新建, 遗留系统, H-60M, CANES]
sources:
  - /root/mosa-defense-applications/results/MOSA遗留系统改造挑战.json
  - /root/mosa-defense-applications/results/B-21_Raider_MOSA实施.json
---

# MOSA棕地改造与绿地新建（Brownfield vs Greenfield）

## 概述

MOSA实施面临的一个核心挑战是**棕地改造**（Brownfield）与**绿地新建**（Greenfield）之间的显著差异。棕地改造指在现有遗留系统上引入MOSA架构，需要在维持现有作战能力的前提下逐步引入开放架构；绿地新建指从设计初期即融入MOSA原则的全新系统。棕地改造的前期投资通常高于绿地项目，但长期节约（模块化升级、竞争性采购、减少供应商锁定）更为显著。

## 要点

### 棕地改造典型案例

#### H-60M Black Hawk

H-60M作为服役数十年的平台，其legacy航电架构改造是最典型的棕地挑战：
- 采用**Digital Backbone**（数字骨干网）架构，将以太网骨干替代传统点对点模拟布线
- 2025年3月获8000万美元合同实施MOSA航电升级（柯林斯航空航天/RTX）
- 采用 [[face-technical-standard]] 实现软件复用和跨平台互操作
- 为与 [[flraa-mv75-mosa]] 等未来垂直升力平台兼容奠定基础
- 采用MBSE方法支持Digital Backbone架构设计

#### CANES 舰载网络

- 从传统舰载网络向容器化DevSecOps架构转型
- 使用UDS平台实现"集成一次、随处部署"的模块化交付
- 软件部署时间从数月缩短至数天
- 引入零信任架构应对开放接口的安全挑战
- 由PEO C4I & Space管辖

#### MAPS 模块化主动防护系统

- 证明了将非MOSA遗留产品改造为MAPS合规标准的可行性
- 采用MTA快速原型路径

### 绿地新建典型案例

#### B-21 Raider

- 全新第六代隐身轰炸机，从2015年EMD设计阶段即嵌入开放系统架构（OSA）
- 被视为国防部MOSA旗舰案例
- 参见 [[b21-raider-mosa]]

#### SDA PWSA 太空星座

- 全新架构，不基于现有卫星系统改造
- 通过NEBULA/OISL标准实现多供应商即插即用
- 参见 [[space-development-agency]]

### 棕地改造的六大集成挑战

1. **技术层面** — legacy硬件接口（MIL-STD-1553、ARINC 429）到现代以太网/光纤的转换需要专用适配器和网关
2. **认证层面** — 已有适航认证（如DO-178C）在引入模块化变更后需要重新验证，成本高昂
3. **数据权利层面** — 遗留系统的接口规范通常被原始承包商视为专有技术数据
4. **作战连续性** — 改造不能中断现有作战能力，需要严格的分阶段实施计划
5. **网络安全** — 开放接口引入新的攻击面（如CANES的零信任架构应对）
6. **文化转变** — 采办人员和集成商需从整体采购思维转向模块化迭代升级思维

### 棕地改造不实施MOSA的主要障碍

1. 短期成本和时间增加——设计工作、接口数据权利获取、适配器开发需要大量前期投资
2. 缺乏正式要求——部分采办路径（如MTA）的政策未明确包含MOSA要求
3. 供应商锁定——原OEM通过专有接口和技术数据控制阻碍开放化
4. 资源和专业知识不足——军种部门尚未评估MOSA所需资源需求
5. 缺乏跨项目协调——PEO级MOSA协调机制不充分
6. 网络安全顾虑——开放接口可能引入漏洞
7. 认证复杂性——遗留系统的认证约束限制了模块化变更的范围

### 成本效益分析的缺失

根据 [[gaor-25-106931-mosa-review]]，20个采办项目中**无一进行正式的MOSA成本效益分析**，因为DoD政策并未明确要求。棕地改造的前期投资通常高于绿地项目，但长期节约更为显著。GAO建议DoD开发标准化的MOSA成本效益分析方法。

## 相关内容

- [[b21-raider-mosa]] — B-21绿地新建MOSA旗舰案例
- [[space-development-agency]] — SDA PWSA太空域绿地新建
- [[flraa-mv75-mosa]] — FLRAA未来远程突击飞行器MOSA
- [[gaor-25-106931-mosa-review]] — GAO MOSA专项审查报告
- [[mosaic-modular-open-systems-approach]] — MOSA总体方法论
- [[dews-mosa-reference-architecture]] — DEWS参考架构主要面向绿地
- [[face-technical-standard]] — FACE航电软件标准（H-60M采用）
- [[vendor-lock-in]] — 供应商锁定问题
- [[gao-24-106831-weapon-systems]] — GAO武器系统报告

## 笔记

棕地改造是MOSA大规模落地的关键战场。美国国防部现有武器系统的平均服役年限远超设计寿命，大量冷战时期和后冷战时期的平台仍需服役数十年。这些系统的MOSA改造不仅是一个技术问题，更是一个经济和政治问题——原OEM掌握大量接口数据和技术诀窍，新供应商进入壁垒仍然较高。DoD IP Cadre（知识产权专业团队）正推动在合同中平衡IP权利，但进展缓慢。2017 NDAA Sec 805首次以法律形式要求MOSA，但2025年GAO报告表明，棕地项目的MOSA实施仍然面临系统性障碍。
