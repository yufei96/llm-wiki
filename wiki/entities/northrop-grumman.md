---
title: "诺斯罗普·格鲁曼（Northrop Grumman）"
created: 2025-04-26
updated: 2025-04-26
type: entity
tags: [承包商, MOSA, 国防工业, Northrop-Grumman, 武器系统]
sources:
  - /root/mosa-defense-applications/results/B-21_Raider_MOSA实施.json
  - /root/mosa-defense-applications/results/SiAW_vs_AARGM-ER_MOSA对比.json
  - /root/mosa-defense-applications/results/MOSA实施状态矩阵.json
---

# 诺斯罗普·格鲁曼（Northrop Grumman）

## 摘要

诺斯罗普·格鲁曼是美国五大国防承包商之一，在MOSA（模块化开放系统方法）领域展现出显著的内部矛盾：同一公司在不同项目中同时扮演MOSA积极倡导者和非MOSA方案的执行者角色。其关键MOSA项目包括B-21 Raider隐身轰炸机和SiAW近距攻击武器，但其AARGM-ER反辐射导弹项目则未实施MOSA。

## 要点

### 主要MOSA项目

- **B-21 Raider 突袭者**：被广泛视为国防部MOSA旗舰案例。从2015年EMD设计阶段即嵌入开放系统架构（OSA），允许在全寿命周期内持续升级航电、传感器和武器系统，无需对主体结构进行重大修改。参见 [[b21-raider-mosa]]
- **SiAW 近距攻击武器**：空军采办领导层推翻项目办公室初始的非MOSA方案，明确要求实施MOSA。SiAW是空军数字采办方法的标杆项目之一，首批采用模块化开放系统架构设计的导弹。参见 [[siaw-aargm-er-mosa-contrast]]
- **CANES 舰载网络**：从传统舰载网络向容器化DevSecOps架构转型，使用UDS平台实现模块化交付，软件部署时间从数月缩短至数天。参见 [[mosa-brownfield-vs-greenfield]]

### 非MOSA项目

- **AARGM-ER 增程型先进反辐射导弹**：GAO-25-106931明确列为"Not Implementing"（未实施MOSA）。海军出于短期采办成本考虑决定不实施，未进行正式的MOSA成本效益分析。专有/封闭设计，升级需要对整个系统进行较大改动

### 同一承包商MOSA实施差异的意义

诺斯罗普·格鲁曼的案例直接揭示了一个关键政策问题：**MOSA实施由项目层面的决策驱动，而非由承包商层面的统一策略决定**。B-21（空军MDAP）从设计之初采用OSA，SiAW（空军MTA）被空军领导层强制要求MOSA，而AARGM-ER（海军MDAP）则未被要求。这表明MOSA的执行高度依赖军种采办领导层的意愿和政策框架，而非承包商的技术能力。

根据 [[gaor-25-106931-mosa-review]]，14/20个项目实施MOSA，但无一进行正式成本效益分析。诺斯罗普·格鲁曼作为B-21的固定价格合同承包商，在LRIP阶段承担了超过20亿美元超支风险。

### 与SDA太空域MOSA的关系

诺斯罗普·格鲁曼也是SDA PWSA传输层和跟踪层的主要供应商之一，参与太空域MOSA标准（NEBULA/OISL）的实施。参见 [[space-development-agency]]

## 相关内容

- [[b21-raider-mosa]] — B-21 Raider MOSA旗舰案例
- [[siaw-aargm-er-mosa-contrast]] — SiAW与AARGM-ER MOSA对比分析
- [[mosa-brownfield-vs-greenfield]] — CANES遗留系统改造
- [[space-development-agency]] — SDA PWSA太空域MOSA
- [[gaor-25-106931-mosa-review]] — GAO MOSA专项审查报告
- [[mosa-implementation-status-matrix]] — 20项目MOSA实施状态矩阵
- [[mosaic-modular-open-systems-approach]] — MOSA总体方法论
- [[dodi-5000-85-2020]] — DoDI 5000.85 重大能力采办

## 笔记

诺斯罗普·格鲁曼的MOSA实施不一致性是一个重要的政策案例。同一技术团队和管理能力，在空军项目中实施MOSA而在海军项目中不实施，说明MOSA的落地更多取决于政策和领导层意志而非技术可行性。GAO报告指出海军是三军中MOSA指南最薄弱的军种——没有MOSA指南手册，其采办政策仅对法律要求进行高层级引用。
