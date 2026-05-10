---
title: "SysML v1→v2过渡：MOSA数字工程落地的基础设施瓶颈"
created: 2026-04-26
updated: 2026-04-26
type: topic
tags: [SysML, MBSE, 数字工程, MOSA, 过渡, 瓶颈, DoDI 5000.97]
sources: [raw/papers/SysML-v2-Basics-2024.pdf, raw/papers/Thurs_1560710_Stirk.pdf, raw/papers/SysML-v2-TransitionOutline-1.1.pdf, raw/papers/SysML-Info-Sheet-Jan2025.pdf, raw/papers/dsb-digital-engineering-2024.pdf]
confidence: INFERRED
evidence: "基于多源综合分析"
---

# SysML v1→v2过渡：MOSA数字工程落地的基础设施瓶颈

## 摘要

DoDI 5000.97 将 MOSA 列为数字工程九大要素之一，SysML v2 是 MOSA 接口建模的下一代语言基础。但 DoD 拥有 **15,000+ 政府模型**，其中 **25% DoD 工程师使用模型**——这些模型全部基于 SysML v1。SysML v1→v2 的过渡不是语言升级，而是**整个数字工程基础设施的迁移**，是 MOSA 数字工程落地的最大瓶颈。

## 过渡规模

| 指标 | 数据 | 来源 |
|------|------|------|
| DoD 政府拥有模型 | 15,000+ | [[NDIA SysML v2过渡2023]] |
| DoD 工程师使用模型比例 | 25% | [[NDIA SysML v2过渡2023]] |
| v1→v2 语法差异 | 9大类（block→part, port→port def, ...） | [[NDIA SysML v2过渡2023]] |
| OUSD 过渡规划步骤 | 6步（团队→战略→试点→基础设施→部署→监控） | [[OSD SysML v2过渡指导]] |
| SysML v2 正式采纳 | 2025年6月 | [[SysML v2规范]] |

## 为什么是瓶颈

### 1. 语法不兼容
SysML v2 不是 v1 的增量更新，而是全新架构：
- UML profile → 独立元模型（KerML）
- 半形式化语义 → 形式化语义
- 仅图形 → 图形+文本双语法

**9大语法差异**：block→part, value property→attribute, proxy port→port, action→action, state→state, constraint→constraint, Requirement→requirement, connector→connection, view→view

### 2. 工具链需要重写
SysML v1 工具（MagicDraw/Cameo, Rhapsody, Enterprise Architect）不能直接加载 v2 模型。14家厂商已声明支持 v2，但**商业工具尚未发布 v2 版本**。

### 3. 人员需要重新培训
25% DoD 工程师需要学习新语言、新工具、新方法论。OUSD 过渡指导建议：
- 熟悉 SysML v2 文本语法和 API
- 使用实践模型开展试点
- 逐步更新培训和实践社区

### 4. 模型需要迁移或重建
15,000+ 模型不能自动转换。需要：
- 评估哪些模型值得迁移
- 制定迁移优先级
- 可能需要部分重建

## 对MOSA的影响

### 正面影响
- SysML v2 的接口建模能力**直接支持 MOSA 接口规范**
- 标准化 API 实现**工具互操作**——MOSA 要求的跨供应商协作
- 形式化语义支持**自动验证**——MOSA 接口合规性检查

### 负面影响
- 过渡期间**建模能力可能退化**——旧工具不再维护，新工具尚未成熟
- **数字线程断裂**——v1 模型和 v2 模型之间的数据贯通
- **成本和时间**——过渡需要大量投入，可能延迟 MOSA 数字工程的全面落地

## 过渡路径

OUSD(R&E) 官方过渡指导（[[OSD SysML v2过渡指导]]）建议：

1. **建立过渡团队** — 确定负责人和核心团队
2. **制定战略和计划** — 明确目标和风险
3. **开展试点** — 使用实践模型评估影响
4. **更新基础设施** — 工具→环境→方法论→培训→社区→参考架构
5. **部署到项目** — 评估就绪度，制定时间表
6. **监控改进** — 持续评估过渡效果

## 关键发现

1. **过渡是基础设施问题，不是语言问题**：15,000+ 模型、工具链、人员技能都需要迁移，这是整个数字工程生态的升级

2. **过渡窗口期是 MOSA 的风险期**：v1 工具在退化，v2 工具未成熟，这个窗口期内 MOSA 的数字工程能力可能暂时下降

3. **试点是关键**：OUSD 建议先试点再推广——但 DoD 的采办节奏可能不允许缓慢过渡

4. **与DSB报告的呼应**：DSB 2024 数字工程报告指出"文化变革是真正瓶颈"——SysML v2 过渡正是这一判断的具体体现

## 相关内容

- [[SysML v2规范]] — SysML v2 规范
- [[OSD SysML v2过渡指导]] — OUSD 官方过渡指导
- [[NDIA SysML v2过渡2023]] — NDIA 过渡指南项目简报
- [[数字工程与模块化融合]] — 数字工程与MOSA融合
- [[数字工程工具对比]] — 数字工程工具链对比
- [[科学委员会数字工程2024]] — DSB数字工程报告（文化变革瓶颈）
- [[数字工程实践]] — 数字工程实践（OUSD过渡时间线、SysML v2使能、NASA/INCOSE框架）

---

- [[NDIA-MOSA白皮书2019]]
