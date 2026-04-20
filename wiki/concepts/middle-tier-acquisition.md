---
title: "中间采办层级（MTA）"
created: 2026-04-19
updated: 2026-04-19
type: concept
tags: [MTA, 中间采办, 快速采办, AAF, 自适应采办框架]
sources: [raw/papers/dodi-5000.80-middle-tier-acquisition-rapid-fielding-and-prototyping.pdf]
---

# 中间采办层级（MTA）

## 定义

中间采办层级（Middle Tier of Acquisition, MTA）是美国国防部自适应采办框架（[[adaptive-acquisition-framework]]）中的**快速采办路径**，由DoDI 5000.80建立，旨在将现有成熟技术快速转化为可用能力，**在5年内完成从立项到部署**。

## 核心特点

- **时间限制严格**：原型交付不超过5年，快速部署不超过5年
- **不需要里程碑**：跳过传统的A/B/C里程碑审查，采用精简的审批流程
- **聚焦成熟技术**：不用于基础研究或全新技术开发，只用于技术成熟度（TRL）6以上的技术
- **两条子路径**：
  - **原型制作（Prototyping）**：快速开发和测试原型
  - **快速部署（Rapid Fielding）**：快速将成熟解决方案部署到作战单位

## MTA与MOSA的关系

MTA路径中**MOSA不是强制要求**，但DoDI 5000.02鼓励MTA项目在可行时采用模块化开放系统方法。这一政策张力——MTA追求速度vs MOSA需要架构投入——是国防采办改革的核心议题之一。

## 绩效数据

根据GAO-24-106831（2024年武器系统年度评估）：
- MTA项目的平均成本增长为**3%**，远低于传统MDAP项目的**28%**
- 但MTA项目的进度延迟与传统项目相当
- 部分MTA项目在到达5年期限后延期为传统MDAP

## 在AAF中的位置

```
自适应采办框架（AAF）
├── 中间采办层级（MTA）← 快速通道，5年
├── 重大能力采办（MCAP）— DoDI 5000.85
├── 软件采办 — DoDI 5000.87
├── 紧急能力采办 — DoDI 5000.81
├── 国防业务系统 — DoDI 5000.75
└── 服务采办 — DoDI 5000.74
```

## 相关内容

- [[adaptive-acquisition-framework]]
- [[mosa-defense-acquisition]]
- [[defense-acquisition-overrun-trends]]
- [[dodi-5000-80-middle-tier-acquisition]]
- [[gao-24-106831-weapon-systems]]
