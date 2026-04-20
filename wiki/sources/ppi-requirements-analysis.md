---
title: "PPI — 需求分析方法论（有效 + 概览）"
created: 2026-04-19
updated: 2026-04-19
type: source
tags: [PPI, 需求分析, 方法论, 系统工程, Robert-Halligan]
sources: [raw/papers/ppi-requirements-analysis-that-works.pdf, raw/papers/ppi-requirements-analysis-overview.pdf]
---

# PPI — 需求分析方法论

## 来源

Robert J. Halligan，PPI Managing Director。两份文档：
- *Requirements Analysis That Works!*（2024更新，8页）— 详细方法
- *Requirements Analysis Overview*（2024，6页）— 流程概览

## 概述

系统化的需求分析方法论，目标是将"不合格"的需求转化为"合格"的需求。核心判据：**如果需求集被满足，相关利益相关者需求未被满足的风险水平足够低**（通常期望损失2-3%以内）。

## 需求分析流程（PPI推荐）

```
原始需求 → 完整性检查 → 一致性检查 → 可验证性检查 → 可行性检查 → 可追溯性建立 → 优先级排序 → 基线化
```

关键步骤：
1. **完整性**：需求是否覆盖所有利益相关者需要？
2. **一致性**：需求之间是否矛盾？
3. **可验证性**：每个需求是否有明确的验证方法？
4. **可行性**：技术上是否可实现？
5. **可追溯性**：需求是否追溯到来源（利益相关者需要、法规、标准）？

## 关键观点

- 需求分析不是一次性活动——需求随时间变化（问题空间变化 + 技术可能性变化）
- 需求分析的投入回报率极高：通常0.1-2%的开发成本投入可避免10-80%的成本超支
- 需求质量的"自然衰减"：即使初始需求优秀，随着时间推移和变更累积，质量会下降

## 与MOSA的关系

MOSA的接口定义本质上是需求分析的子集：
- **接口完整性**：是否覆盖所有模块间的数据/信号/服务交换？
- **接口一致性**：不同接口标准之间是否矛盾？
- **接口可验证性**：一致性认证是否可自动化？

WOSA工具链的"架构合规性扫描"就是将PPI需求分析流程自动化应用于MOSA接口。

## 相关内容

- [[ppi-did-templates]] — PPI DID模板（SyRS等）
- [[wosa-architecture-tools]] — WOSA架构工具链
- [[mosa-five-pillars]] — MOSA五大支柱
- [[ppi-business-case-re]] — 需求工程投资回报
