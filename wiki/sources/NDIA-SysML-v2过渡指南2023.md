---
title: "NDIA 2023 — DoD SysML v2 过渡指南项目简报"
created: 2026-04-26
updated: 2026-04-26
type: source
sources: [raw/papers/星期四-Stirk演讲.pdf]
author: "Daniel Hettema (Director, DEM&S, OUSD(R&E))"
tags: [SysML, MBSE, NDIA, 过渡, 数字工程, OUSD]
confidence: EXTRACTED
evidence: "直接从原始文档提取"
---

# NDIA 2023 — DoD SysML v2 过渡指南项目简报

## 文档概况
- **场合**：第26届 NDIA 系统与任务工程会议（弗吉尼亚州诺福克）
- **演讲者**：Daniel Hettema，OUSD(R&E) DEM&S 主任
- **日期**：2023年10月
- **保密等级**：Distribution Statement A（公开发布）
- **DOPSR Case**：# 24-T-0075

## 核心内容

### SysML v2 架构变化
SysML v2 不是 v1 的修补，而是全新架构：
- **KerML**：提供核心概念、构造和语义
- **SysML v2**：全新语言 + 修订方法论，不依赖 UML
- **API**：标准化接口，支持模型存储、模型交换、与外部工具（CAD/PDM/仿真/分析）交互

### v1→v2 语法差异

**SysML v1** → **SysML v2**：
- block / part property → part / part def
- value property / value type → attribute / attribute def
- proxy port / interface block → port / port def
- action / activity → action / action def
- state / state machine → state / state def
- constraint property / constraint block → constraint / constraint def
- Requirement → requirement / requirement def
- connector / association block → connection / connection def
- view → view / view def

### DoD 影响范围
- **15,000+** DoD 政府拥有模型
- **25%** DoD 工程师使用模型
- 不含承包商生态系统模型和用户

### 过渡步骤
1. **熟悉变化**：新概念、语法、语义
2. **识别影响**：分析 v2 对现有模型、建模工具的影响
3. **协作**：跨社区合作推进过渡

### DoD 过渡指南项目
- 组建跨社区协作团队
- 在 OMG Wiki 上发布过渡指导文件
- 50+ FAQ 覆盖 12 个类别
- 12 个过渡指导用例
- 工具厂商路线图整合

## 关键人物

- **Daniel Hettema** — OUSD(R&E) DEM&S 主任，SysML v2 过渡指导项目负责人
- **Tom Simms** — SE&A 执行主任
- **Heidi Shyu** — OUSD(R&E) 副部长（时任）

## 与MOSA的关系

- SysML v2 的标准化 API 直接支持 MOSA 要求的工具互操作性
- 15,000+ DoD 模型的过渡是 MOSA 数字工程落地的关键基础设施
- v1→v2 语法变化影响 MOSA 接口建模方法

## 在知识库中的位置

- SysML-v2规范 — SysML v2 规范概述
- OSD-SysML-v2过渡指导 — OUSD(R&E) 官方过渡指导
- 数字工程工具对比 — 数字工程工具链对比
- 数字工程与模块化融合 — 数字工程与 MOSA 融合

---

