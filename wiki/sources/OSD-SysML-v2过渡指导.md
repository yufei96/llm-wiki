---
title: "OUSD(R&E) SysML v1→v2 过渡指导"
created: 2026-04-26
updated: 2026-04-26
type: source
sources: [raw/papers/SysML-Info-Sheet-Jan2025.pdf, raw/papers/SysML-v2-TransitionOutline-1.1.pdf]
author: "OUSD(R&E) SE&A Digital Engineering, Modeling & Simulation (DEM&S)"
tags: [SysML, MBSE, 数字工程, 过渡指导, OUSD, DoDI 5000.97]
confidence: EXTRACTED
evidence: "直接从原始文档提取"
---

# OUSD(R&E) SysML v1→v2 过渡指导

## 文档概况
- **发布者**：美国国防部研究与工程副部长办公室（OUSD(R&E)）系统工程与架构（SE&A）数字工程、建模与仿真（DEM&S）团队
- **文档类型**：官方过渡指导（Technical Highlight + 规划大纲）
- **发布日期**：2025年1月（信息页）、2024年3月（规划大纲 v1.1）
- **保密等级**：Distribution Statement A（公开发布）

## 背景

SysML v2 是 OMG 开发的下一代系统建模语言，预计 2025 年正式发布。DoD 作为 SysML 的最大用户之一（15,000+ 政府拥有模型，25% DoD 工程师使用模型），需要系统化的过渡指导。

### SysML v2 三大核心改进
1. **API**：引入标准化 API，支持工程学科和机构间的无缝协作
2. **KerML**：使用标准化内核语言，使模型机器可读，确保所有项目干系人获得共同的可计算系统架构理解
3. **改进互操作性**：跨团队无缝数据共享，为项目经理提供更好的项目可见性、减少错误、加快开发周期

## 过渡指导建议

OUSD(R&E) 建议采办项目：
1. **制定战略计划**：为团队过渡制定战略计划
2. **熟悉新语言**：学习 SysML v2 文本语法和 API
3. **试点评估**：使用实践模型获取经验，开展试点

### 过渡规划六步法（来自规划大纲）

**Step 1 — 建立过渡团队**
- 确定过渡负责人和核心团队
- 识别利益相关者

**Step 2 — 制定战略和计划**
- 2.1 过渡目标：明确为什么要过渡
- 2.2 过渡风险：识别技术、组织、工具风险

**Step 3 — 开展试点评估影响**
- 使用实践模型评估对当前 MBSE 实践的影响
- 评估语法差异、语义变化、工具兼容性

**Step 4 — 更新建模基础设施**
- 4.1 工具评估和选择
- 4.2 更新建模环境
- 4.3 更新建模方法论和实践
- 4.4 更新 MBSE 培训
- 4.5 更新实践社区网站/仓库
- 4.6 更新参考架构和可复用资产

**Step 5 — 考虑部署到项目的因素**
- 评估项目就绪度
- 制定迁移时间表

**Step 6 — 部署 MBSE with SysML v2 到项目**
- 6.1 监控改进效果

## DoD 过渡指导资源

所有指导文件发布在 OMG Wiki：
- OMG Wiki: https://www.omgwiki.org/MBSE/doku.php?id=mbse:sysml_v2_transition
- SE&A: https://www.cto.mil/sea/
- DEM&S: https://www.cto.mil/sea/dems
- 社区协作会议：每月举行，联系 osd-sea@mail.mil

## 与MOSA的关系

SysML v2 过渡直接影响 MOSA 的数字工程落地：
- **接口建模**：SysML v2 的 port/connection 语义改进，支持更精确的 MOSA 接口定义
- **标准化 API**：实现 MOSA 模型与 CAD/PDM/仿真工具的互操作
- **机器可读性**：KerML 使 MOSA 接口规范可自动验证

## 在知识库中的位置

- SysML-v2规范 — SysML v2 规范概述
- 数字工程工具对比 — 数字工程工具链对比
- 数字工程与模块化融合 — 数字工程与 MOSA 融合
- DoDI-5000.97数字工程 — DoDI 5000.97 数字工程指令

---

