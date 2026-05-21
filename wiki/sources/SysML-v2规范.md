---
title: "SysML v2 — 下一代系统建模语言规范"
created: 2026-05-07
updated: 2026-05-21
tags: [SysML, SysML v2, OMG, 建模语言, MBSE, 标准]
source:
  - raw/papers/SysML-v2-specification.pdf
confidence: EXTRACTED
evidence: "从原始PDF和OMG公开资料综合提取"
type: source
---

# SysML v2 — 下一代系统建模语言规范

## 概述

- **全称**：OMG Systems Modeling Language v2
- **发布方**：Object Management Group (OMG)
- **定位**：SysML v1 的完全重写版，解决 v1 语言复杂度高、互操作性差的痛点

## v1 → v2 的重大变化

| 维度 | SysML v1 | SysML v2 |
|------|----------|----------|
| 底层 | UML 2 扩展 | 全新内核 KerML |
| 语法 | 仅图形 | **文本+图形双语法** |
| API | 无标准 | **标准 REST/JSON API** |
| 建模风格 | 以图为中心 | **以模型为中心** |
| 工具互操作 | 困难 | 原生互操作 |

## 关键特性

1. **KerML 内核**：不依赖 UML 的全新内核语言（Kernel Modeling Language）
2. **文本语法**：引入类似编程语言的结构化文本语法，支持 Git 版本控制
3. **标准 API**：REST/JSON API 使工具间模型交换成为可能
4. **更简洁**：语言元素从 ~300 减少到 ~100
5. **更好的分析支持**：原生支持变体管理、需求和架构的集成

## 对 MOSA 的意义

SysML v2 是 **MOSA 数字工程落脚的基础设施**：

- **模块化接口建模**：更简洁的语言便于定义和描述模块化系统接口
- **标准 API → 工具链开放**：任何工具都可以通过标准 API 访问模型，打破工具锁定
- **Git 友好 → 协同工程**：文本语法使模型可以像代码一样做 diff、merge
- **DoD 过渡指导**：OUSD(R&E) 已发布 SysML v1→v2 过渡指南，推动 DoD 项目迁移

## 过渡时间线

- 2023年：OMG 发布 SysML v2 最终规范
- 2024年：首批支持工具出现
- 2025-2027年：DoD 项目逐步迁移（配合 DoDI 5000.97 数字工程要求）
- 2028年+：预期成为主要采办项目的标准建模语言
