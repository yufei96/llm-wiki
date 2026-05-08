---
title: "通用武器接口（UAI）概述"
created: 2026-05-08
updated: 2026-05-08
type: source
tags: [UAI, 武器接口, 空军, 标准化, MOSA, WOSA, 任务规划, LAR]
sources:
  - raw/papers/UAI-IQPC-Overview.pdf
  - raw/articles/UAI-IQPC-Overview.md
---

# 通用武器接口（UAI）概述

## 概述

UAI（Universal Armament Interface）是美国国防部和NATO倡议，旨在开发飞机、武器和任务规划之间的标准化功能接口，支持未来武器集成独立于飞机OFP周期。由美国空军航空系统中心（ASC）主导。

## 核心目标

- 标准化飞机与武器之间的功能接口
- 支持武器集成独立于飞机OFP（作战飞行程序）周期
- 解决精确弹药供应链短缺问题（如利比亚行动中暴露的问题）

## 技术范围

### 接口标准化

- **飞机-武器接口**：标准化物理和电气连接
- **武器-任务规划接口**：标准化数据交换格式
- **发射允许区（LAR）标准化**：基于通用真值数据集而非独立n-DOF分析

### 关键组件

- **UPC（Unique Planning Component）**：武器专用规划组件
- **CC（Common Component）**：通用组件
- **WDLI（Weapon Data Link Initialization）**：武器数据链初始化
- **KH（Key Handler）**：密钥处理器
- **MPICD（Mission Planning Interface Control Document）**：任务规划接口控制文档

### LAR标准化

- 问题：计算平台释放制导武器并命中目标的区域
- UAI标准化了LAR流程
- 基于通用真值数据集
- 开发通用流程和软件工具集
- 采用标准算法
- 添加配置控制
- 结果：平台LAR可通过任务数据更新，无需OFP更新

## 接口管理

- 采用MIL-STD-3014使用MiDEF文件
- 标准化接口控制文档（ICD）
- 配置数据集（CDS/CDF）管理

## 实施现状

- 空军主导实施
- NATO成员国参与
- 国际合作机会开放

## 数据质量评估

- **来源可靠性**: ★★★★★ — 美国空军ASC官方演示
- **时效性**: ★★★☆☆ — 演示文档（具体年份未标注，约2010年代）
- **独特价值**: UAI标准的技术细节和接口规范，WOSA武器接口标准的基础

## 相关页面

- [[wosa-weapons-open-systems-architecture]] — WOSA武器开放系统架构
- [[moatel-wosa-verification]] — MOATEL弹药开放架构试验鉴定实验室
- [[mosa-standards-by-scope]] — UAI作为军种内推广标准
- [[siaw-aargm-er-mosa-contrast]] — SiAW项目（采用WOSA/UAI）

---

*基于美国空军ASC UAI演示文档（IQPC）提取整理。2026-05-08创建。*
