---
title: "SysML v2 规范 — 下一代系统建模语言"
created: 2026-04-26
updated: 2026-04-26
type: source
sources: [raw/papers/SysML-v2-Basics-2024.pdf, raw/repo/sysml-v2-release/doc/2a-OMG_Systems_Modeling_Language.pdf, raw/repo/sysml-v2-release/doc/1-Kernel_Modeling_Language.pdf, raw/repo/sysml-v2-release/doc/3-Systems_Modeling_API_and_Services.pdf]
author: "Sanford Friedenthal (SAF Consulting, SysML v2 Submission Team)"
tags: [SysML, MBSE, 数字工程, OMG, 建模语言, MOSA, 接口建模]
confidence: EXTRACTED
evidence: "直接从原始文档提取"
---

# SysML v2 规范 — 下一代系统建模语言

## 文档概况
- **全称**：OMG Systems Modeling Language™ (SysML®) Version 2
- **标准化组织**：OMG（Object Management Group）
- **规范状态**：2023年6月OMG采纳beta规范，2025年6月正式采纳
- **核心规范**：KerML（内核建模语言）、SysML v2、Systems Modeling API & Services
- **参考实现**：raw/repo/sysml-v2-release/（含KerML/SysML v2/API规范PDF、BNF语法定义）
- **本页来源**：Friedenthal, S. "SysML v2 Basics," INCOSE IW 2024

## 演进脉络

| 版本 | 时间 | 状态 |
|------|------|------|
| SysML v1.0 | 2006 | OMG采纳（UML profile） |
| SysML v1.7 | 2022 | 最新v1修订 |
| SysML v2 Beta | 2023.06 | OMG采纳beta规范 |
| SysML v2 正式 | 2025.06 | OMG正式采纳 |

## SysML v2 vs v1 关键改进

| 维度 | SysML v1 | SysML v2 |
|------|----------|----------|
| **语言基础** | UML profile（受限于UML元模型） | 独立元模型（KerML），不依赖UML |
| **语义** | 半形式化 | 形式化语义，可自动验证 |
| **表示法** | 仅图形 | 图形+文本双语法 |
| **接口建模** | Port/Interface（v1的痛点） | 原生Part/Port/Connection，更精确 |
| **需求** | 属性+文字描述 | 约束表达式，可自动求解Pass/Fail |
| **分析集成** | 无原生支持 | Analysis Case，与求解器集成 |
| **API** | 无标准 | 标准化REST API |
| **可扩展性** | UML profile | 模型库扩展 |

## 语言架构

```
KerML（内核建模语言）
├── 形式逻辑的直接语义映射
├── 内核语法 + 内核模型库
└── SysML v2（系统建模语言）
    ├── 系统语法
    ├── 系统和领域模型库
    └── 能力：Structure / Behavior / Requirements / Analysis / Verification / View & Viewpoint
```

## 与MOSA的关联

### 接口建模能力
SysML v2 的核心改进之一是**接口和连接建模**的精确化，这直接支持MOSA的接口定义需求：

- **Part分解**：SysML v2 的Part可精确建模MOSA模块的层次分解
- **端口和连接**：原生的Port/Connection语义支持MOSA接口规范
- **约束表达式**：Requirements作为约束可自动验证接口合规性
- **变体建模**：支持MOSA的多配置/多供应商变体

### 数字线程集成
SysML v2 的标准化API使模型可与：
- CAD工具（FreeCAD集成示例）
- 分析求解器（Maple集成示例）
- 数字线程管理（Syndeia集成示例）

这实现了DoDI 5000.97要求的**数字线程贯通**。

### OUSD(R&E) SysML v1→v2 过渡指导
美国国防部研究与工程副部长办公室（OUSD(R&E)）已发布：
- SysML v2 信息页（2025年1月）
- SysML v1→v2 过渡规划大纲 v1.1
- 月度社区协作会议

**过渡建议**（来自Friedenthal）：
1. 将过渡规划与现有MBSE/数字工程倡议整合
2. 使用Jupyter环境启动试点评估
3. 与工具厂商讨论路线图
4. 制定增量计划（实践→工具→培训→指标）

## 工具厂商支持

以下厂商在beta规范采纳时声明支持SysML v2：
Ansys, Dassault Systèmes, IBM, Imandra, IncQuery, Intercax, Maple, Mgnite, PTC, QSI, Siemens, Sparx, Tom Sawyer Software, Vitech

## 在知识库中的位置

本文档补充了数字工程×MOSA交叉领域的**方法论层**——SysML v2 是MOSA接口建模的下一代语言基础：

- [[数字工程与模块化融合]] — 数字工程与MOSA融合
- [[数字工程工具对比]] — 数字工程工具链对比
- [[MOSA与数字工程]] — MOSA与数字工程
- [[国际系统工程理事会]] — INCOSE（SysML v2标准化的推动者）
- [[INCOSE系统工程手册V5]] — INCOSE SE Handbook V5（MBSE最佳实践）
- [[OSD SysML v2过渡指导]] — OUSD(R&E) 官方过渡指导
- [[NDIA SysML v2过渡2023]] — NDIA 2023 过渡指南项目简报
- [[接口工程演进]] — 接口工程三层演进
- [[SysML v2过渡瓶颈]] — SysML v2过渡作为MOSA数字工程瓶颈

## 待补充

（无）

---

