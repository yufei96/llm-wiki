---
title: "NGC2：下一代指挥与控制系统的MOSA需求"
created: 2026-05-12
updated: 2026-05-12
type: topic
tags: [NGC2, Army, MOSA, C2, 指挥控制, 地面作战, 航空平台, 开放架构]
sources: [raw/articles/陆军NGC2-MOSA信息征求.md]
confidence: EXTRACTED
evidence: "基于SAM.gov RFI (W15P7T-25-R-RFI)"
---

# NGC2：下一代指挥与控制系统的MOSA需求

## 摘要

NGC2（Next Generation Command and Control）是美国陆军的下一代指挥与控制系统，以MOSA为技术基础。2025年5月陆军发布RFI（W15P7T-25-R-RFI），就NGC2的MOSA解决方案征求行业反馈。核心问题：陆军目前缺乏以技术速度将新兴C2硬件和软件能力快速集成到地面作战和航空平台的能力。

## 核心问题陈述

> "Today, the Army lacks the ability to rapidly integrate emerging C2 hardware and software capabilities into its ground combat and aviation platforms at the speed of technology to gain and maintain decisive overmatch."

作战环境要求陆军比对手更快地集成C2技术。

## RFI基本信息

- **发布机构**：美国陆军 ACC-APG (W6QK)
- **Notice ID**：W15P7T-25-R-RFI
- **发布日期**：2025年5月30日
- **回复截止**：2025年6月30日
- **执行地点**：Aberdeen Proving Ground, MD
- **类型**：Sources Sought（信息征求）
- **状态**：已失效（Inactive），已有更新版本
- **更新链接**：https://sam.gov/opp/acd9ec88a1324b12bc557e035035fcf2/view

## 在MOSA生态中的定位

NGC2是陆军的平台级C2系统，在开放架构四层体系（[[开放架构层级]]）中对应**第1层：平台级**：

| 维度 | NGC2 | 对标 |
|------|------|------|
| 层级 | 平台级 | 空军ABMS GRA、海军OSMP |
| 军种 | 陆军 | 空军、海军各有对应 |
| 功能 | 地面/航空C2 | 空中C2（ABMS）、舰载C2 |
| MOSA角色 | 技术基础 | 与三军联合备忘录一致 |

## 与其他军种C2系统的对比

| 系统 | 军种 | 状态 | MOSA集成 |
|------|------|------|----------|
| **NGC2** | 陆军 | RFI阶段 | MOSA为基础 |
| **ABMS** | 空军 | 已部署TOC-L/CBC2 | GRA体系 |
| **OSMP** | 海军（NAVAIR） | 指南V1已发布 | 包含所有标准引用 |

## 对MOSA标准的需求推测

基于NGC2的C2功能需求，可能涉及的MOSA标准：

- **OMS/UCI**：通用指挥接口，平台级互操作
- **SOSA**：传感器硬件模块化
- **FACE**：软件可移植性
- **VICTORY**：地面车辆C4ISR互操作（陆军主导）
- **CMOSS**：C5ISR通用硬件平台
- **WOSA**：武器系统集成

## 战略意义

- 陆军从传统封闭C2架构向开放架构转型的标志性项目
- 与2024年12月三军联合备忘录的MOSA强制实施要求一致
- NGC2的MOSA实施将影响陆军未来数十年的C2能力架构
- 反映了MOSA从航空领域向地面/联合领域的扩展趋势

## 相关页面

- [[开放架构层级]] — 四层架构体系
- [[MOSA历史时间线]] — MOSA发展历程
- [[C5ISR标准融合]] — 标准趋同分析
- [[开放任务系统]] — OMS概念
- [[MOSA全生命周期应用]] — MOSA应用
- [[六项已验证的MOSA标准]] — 三军6大标准

---

- [[ABMS-GRA先进战斗管理]]
- [[NAVAIR-OSMP实施指南V1]]
