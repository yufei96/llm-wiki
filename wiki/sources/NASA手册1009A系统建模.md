---
title: "NASA-HDBK-1009A — NASA系统建模手册"
created: 2026-05-07
updated: 2026-05-21
tags: [NASA, 系统建模, SysML, MBSE, 系统工程, 手册, 元模型]
source: [raw/papers/NASA手册1009A-非金属材料控制.pdf, raw/articles/NASA手册1009A-非金属材料控制.md]
confidence: EXTRACTED
type: source
---

# NASA-HDBK-1009A — NASA系统建模手册

## 概述

NASA技术手册，全称"NASA Systems Modeling Handbook for Systems Engineering"，2025年3月12日批准（修订版A）。由NASA总工程师办公室发布，面向系统工程实践者。**定义了如何使用SysML进行系统建模，并与NASA系统工程过程（NPR 7123.1）集成**。88页，公开无限分发。

## 修订版A主要变化

相对于2022年11月初版，修订版A（2025年3月）的重大扩展：

1. **范围扩展**：从仅覆盖ConOps、需求和V&V产品 → 扩展至：Stakeholder识别与期望定义、ConOps、MOE定义、技术需求、MOP、TPM定义、V&V需求/计划/结果/报告
2. **新增附录F**：ConOps模板（含模型内容），遵循SE Handbook模板
3. **元模型扩展**（Section 7）：新增Stakeholder Expectations、MOE、MOP、TPM和V&V
4. **示例扩展**（Section 8-9）：为元模型扩展提供图表示例
5. **新增视图**：Stakeholder识别与期望定义、MOE定义、MOP和TPM视图

## 核心内容

### SE过程覆盖

手册覆盖NASA SE Engine四大过程的工作产品：

| 过程 | 工作产品 |
|------|---------|
| **Stakeholder Expectation Definition** | 利益相关方识别与期望陈述、ConOps、MOE定义 |
| **Technical Requirements Definition** | 技术需求、MOP、TPM定义 |
| **Product Verification** | V&V需求、V&V计划、V&V结果与报告 |
| **Product Validation** | 同上 |

### 手册结构（10个章节+6个附录）

1. **Scope** — 目的与适用性
2. **Reference Documents** — 引用文档（政府+非政府）
3. **Acronyms and Definitions** — 术语定义
4. **MBSE Overview** — NASA SE过程概述、MBSE三方面（建模语言/方法/框架）
5. **Model Planning** — 建模规划
6. **Setting Up the Model** — 模型设置（含组织）
7. **The Metamodel** — **核心**：演示系统建模元素和关系
8. **Building the Model** — 16类SysML图表示例：
   - bdd（利益相关方、系统上下文、结构分解、功能分解）
   - ibd（内部块图、结构互连）
   - req（需求图、MOE/MOP/验证需求、追溯性）
   - uc（用例图）
   - act（活动图）
   - 需求验证矩阵表
9. **Generating Diagrams and Tables** — 从系统模型生成图表支持NASA SE工作产品
10. **Appendices**

### MBSE三方面

手册第4.3节定义了NASA视角的MBSE三个支柱：

1. **Modeling Language**（建模语言）：SysML®（含9种图类型、4个建模支柱）
2. **Modeling Methodology**（建模方法）：如何用SysML建模
3. **Modeling Framework**（建模框架）：组织模型元素的架构

## 与DoD相关标准的异同

- 与DoD数字工程战略（2018）和DoDI 5000.97互补——NASA聚焦航天系统工程，DoD聚焦武器系统采办
- SysML v2过渡：手册仍用SysML v1.x，但OMG正推动v2迁移（参见 SysML-v2规范 和 NDIA-SysML-v2过渡指南）
- 与INCOSE SE Handbook V5：方法论层面一致，NASA版为机构级定制

## 笔记

- 修订版A的扩展时机（2025年3月）与DoD数字工程制度化（DoDI 5000.97, 2023年12月）同步——反映航空航天领域MBSE标准化的加速
- 手册强调"模型是工程产品，不是文档的附属品"——这与DoD数字工程战略的"Authoritative Source of Truth"理念一致
- 附录F的ConOps模板是NASA特有的贡献——将SysML建模与ConOps文档模板直接关联
