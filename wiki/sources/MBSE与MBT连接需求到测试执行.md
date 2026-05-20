---
title: "MBSE与MBT连接需求到测试执行"
created: 2026-05-20
updated: 2026-05-20
type: source
tags: [MBSE, MBT, 测试, 需求工程, DoD, MBSE in Practice 2025]
sources: [MBSE in Practice Conference 2025, SEI]
confidence: VERIFIED
evidence: "从ALP International演讲原文提取"
---

# MBSE与MBT连接需求到测试执行

## 摘要

ALP International 展示如何用 MBSE 和基于模型的测试（MBT）将需求直接连接到测试执行。以通用雷达（搜索+IFF询问）为原型，演示了从 SysML 活动图 → MBTSuite 自动生成测试用例 → Python 代码执行 → Pass/Fail 结果的全流程。

## 来源

- **作者:** Andrew Pollner, Katherine Pilat (ALP International Corporation)
- **会议:** MBSE in Practice Conference 2025, August 21, SEI
- **机构:** ALP International — 为 DoD 提供 T&E 咨询服务（DOT&E, DTE&A, DOD CIO, USAF）

## 关键要点

### MBT三要素

1. **模型（Model）** — 系统模型描述系统内部行为，测试模型从测试视角复用系统模型元素
2. **自动测试设计（Automated Test Design）** — MBTSuite 等工具从测试模型自动生成测试用例，策略可选 Guided Path / Shortest Path / Random
3. **自动测试执行（Automated Test Execution）** — 生成的测试用例导出为 Python 代码，执行战术代表性代码获取 Pass/Fail

### 雷达原型演示

- **用例**: 搜索（Search）+ 询问（Interrogation）
- **系统模型**: 每个用例一个详细活动图，链接到需求
- **测试模型**: 每个用例一个高层活动图，复用系统模型元素，调用战术代表性 Python 代码
- **结果**: 6个测试用例全部 PASS

### 实施挑战

- 工具生态碎片化：模型导入 vs 独立创建的工具互不兼容
- 脚本生成 vs 自动化测试解决方案的界限模糊
- 政府云环境 ATO 障碍
- 非确定性模型（如生成式 AI）的测试挑战

## 对 MOSA 的意义

MBT 连接了 MBSE 模型与测试执行，是实现 **数字线程可追溯性** 的关键环节。在 MOSA 背景下，模块化接口的验证测试可自动化生成，大幅降低接口合规验证成本。这与 SysML v2 的模型驱动方法论高度互补。

## 相关内容

- [[wiki/topics/数字工程实践|数字工程实践]]
- [[wiki/topics/SysML v2过渡瓶颈|SysML v2过渡瓶颈]]
- [[wiki/concepts/基于模型的系统工程|MBSE]]
