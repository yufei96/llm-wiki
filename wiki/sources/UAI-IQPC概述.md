---
title: "UAI IQPC 概述 — 通用武器接口技术与实施"
created: 2026-05-21
updated: 2026-05-21
tags: [UAI, 通用武器接口, 空军, 航电, 武器集成, NATO, 标准化]
source: [raw/papers/UAI-IQPC-Overview.pdf, raw/articles/UAI-IQPC概述.md]
confidence: EXTRACTED
type: source
---

# UAI IQPC 概述 — 通用武器接口技术与实施

## 概述

美国空军航空系统中心（Aeronautical Systems Center）Oren Edwards在IQPC会议上的技术简报"Dominant Air Power: Design For Tomorrow…Deliver Today"。系统介绍**通用武器接口（UAI）**的历史、技术范围、接口管理和实施进展。UAI是DoD和NATO联合倡议，旨在开发飞机、武器和任务规划之间的**标准化功能接口**，使未来武器集成独立于飞机OFP（作战飞行程序）循环。

## 核心概念

- **问题**：非标准软件接口驱动集成进度——每种武器需要针对每种飞机的定制化集成
- **UAI方案**：标准化飞机-武器之间的功能接口，使任何UAI兼容武器可在任何UAI兼容平台上使用
- **操作能力**：快速适应未计划需求——2011年利比亚冲突中NATO因缺乏通用集成能力而弹药短缺催生了UAI

## 简报结构

| 章节 | 内容 |
|------|------|
| **UAI历史** | 从概念到DoD/NATO联合倡议 |
| **能力概述** | 操作场景：多国飞机共享不同武器类型 |
| **技术范围** | UAI如何工作——标准化功能接口定义 |
| **接口管理** | 当前与计划的接口管控 |
| **USAF实施** | 美国空军具体实施路径 |
| **国际参与** | NATO成员国的参与机会 |

## 操作场景（简报核心示例）

1. 国家A飞机（UAI兼容，携带SDB弹药）和国家B飞机（UAI兼容，携带BRIMSTONE弹药）部署到同一前进基地
2. 国家A完成SEAD任务但弹药用尽，国家B有剩余BRIMSTONE
3. 如果国家B提供现有BRIMSTONE CDS或创建有限功能CDS：
   - 国家A飞机可快速升级能力
   - 两国飞机可共同打击剩余目标
4. **结论**：快速适应未计划需求是UAI提供的操作能力

## 技术架构

- 通用任务规划系统
- 通用数据需求和发射可接受区（LAR）算法
- 通用任务数据文件格式
- 标准化飞机-武器接口独立于OFP

## 与MOSA的关联

- UAI是MOSA在**武器-平台接口层**的具体实现
- 与FACE（航电软件）互补：FACE解决平台内软件可移植性，UAI解决平台-武器间互操作性
- 与NDIA CFW ICD（2015）一脉相承：通用火控武器接口是UAI的自然延伸

## 笔记

- 此简报来自IQPC（国防会议），不是正式标准文档——但Oren Edwards作为USAF ASC代表提供了权威的第一手信息
- 简报提出了NATO成员国的参与路径——表明UAI一开始就具有联盟互操作性目标
- 与SAM.gov上的UAI/CFW ICD信息征求（2023）形成前后呼应——从10年前的概念推广到近年正式采购
