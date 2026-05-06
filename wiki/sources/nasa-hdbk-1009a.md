---
title: "NASA-HDBK-1009A: NASA系统建模手册（系统工程用）"
created: 2026-04-29
updated: 2026-04-29
type: source
tags: [NASA, MBSE, SysML, 系统建模, 元模型, SE引擎, V&V, ConOps, 需求, MOE, MOP, TPM]
sources: [raw/papers/NASA-HDBK-1009A.pdf, raw/articles/2025-03-12-NASA-HDBK-1009A.md]
---

# NASA-HDBK-1009A: NASA系统建模手册（系统工程用）

## 摘要

NASA-HDBK-1009A（2025年3月12日批准，Revision A）是NASA系统建模（MBSE）的核心实践指南，88页，展示了如何使用SysML®建模语言与NASA系统工程流程（NPR 7123.1）整合。该手册从Baseline版（2022年11月）扩展了覆盖范围——从ConOps、需求和V&V产品扩展到利益攸关方识别、MOE、MOP、TPM等完整SE工作产品体系。它包含元模型定义、SysML建模示例、以及从模型生成SE产品图表的具体指导。

## 要点

### 文档定位与范围
- **适用对象**：使用OMG SysML v1.7的系统建模者，经验水平各异
- **覆盖的NASA SE工作产品**：

| SE流程 | 覆盖的工作产品 |
|--------|--------------|
| 利益攸关方期望定义 | 利益攸关方识别与期望定义、ConOps、MOE定义 |
| 技术需求定义 | 技术需求、MOP、TPM定义 |
| 产品验证 | 验证需求、验证规划、验证结果与报告 |
| 产品确认 | 确认需求、确认规划、确认结果与报告 |

- **工具无关性**：虽然引用SysML v1.7，但元模型适用于任何建模语言
- **配套模型**：可在 https://standards.nasa.gov 获取配套MagicDraw模型

### MBSE三大方面（Section 4.3）

#### 1. 建模语言（SysML）
- **9种图类型**：4种行为图（活动act、序列sd、状态机stm、用例uc）、1种需求图（req）、4种结构图（bdd、ibd、pkg、par）
- **4大建模支柱**：结构、行为、需求、参数化

#### 2. 建模方法论
- **与NASA SE引擎对齐**：在SE引擎基础上增加两个模型特有步骤
- **模型规划**（对应技术规划过程）
- **设置模型**（对应系统设计过程Step 0）
- 借鉴INCOSE OOSEM（面向对象SE方法）的模型特有步骤

#### 3. 建模框架
- **MBSE Grid框架**：NASA SE技术过程（行）× SysML四大支柱（列）
- 适配NASA SE引擎的9个技术过程
- 用于组织SysML图表在模型中的位置

### 元模型（Section 7，核心内容）
Rev A扩展的元模型覆盖：

| 元素类别 | 包含内容 |
|----------|---------|
| 利益攸关方 | 利益攸关方识别、期望声明 |
| 系统上下文 | 系统边界、外部接口 |
| 用例 | 系统用例、活动序列 |
| 结构 | 系统分解、组件接口 |
| 功能 | 功能分解、活动模型 |
| 需求 | 系统需求、需求层级 |
| MOE/MOP/TPM | 有效性度量、性能度量、技术性能度量 |
| V&V | 验证/确认需求、规划、结果 |
| ConOps | 运行概念 |

### 模型构建示例（Section 8）
22个SysML建模示例，涵盖：
1. 利益攸关方识别BDD和表格
2. NGO（需求、目标、目标）需求图
3. 系统上下文BDD和IBD
4. 系统用例图
5. 支持用例的活动图
6. 结构分解BDD
7. 结构互连IBD
8. 功能分解BDD
9. 系统需求图
10. 需求追溯表
11. MOE/MOP/需求追溯图
12. 结构分解与MOP/TPM标识
13-15. 验证需求/追溯图
16-17. 验证需求矩阵/VCS
18-20. V&V用例/配置分解/活动序列
21-22. 确认需求/确认VCS

### 从模型生成SE产品（Section 9）
Rev A扩展的SE产品生成：
- **利益攸关方识别与期望**：从模型提取图表和表格
- **ConOps**：运行概念的模型化表达（新增附录F：ConOps模板）
- **MOE定义**：有效性度量的模型化定义
- **技术需求**：需求的模型化管理
- **MOP**：性能度量的模型化追踪
- **TPM**：技术性能度量的模型化监控
- **V&V**：验证/确认的模型化支撑

### Rev A关键变更（对比Baseline 2022）
1. **范围扩展**：从ConOps/需求/V&V扩展到利益攸关方识别、MOE、MOP、TPM
2. **新增附录F**：ConOps模板（含模型内容，遵循SE手册模板）
3. **元模型扩展**：新增利益攸关方期望、MOE、MOP、TPM、V&V元素
4. **Section 8扩展**：新增支持扩展元模型的示例图表和表格
5. **Section 9扩展**：新增SE工作产品的图表和表格生成示例

### 方法论背景
- **OOSEM**（面向对象SE方法）：INCOSE OOSEM工作组的SE方法
- **MBSE Grid**（Morkevicius等，2017）：简化的SysML方法论
- **OpenSE Cookbook**（Karban等，2018）：JPL的30米望远镜SE实践
- **Parrott & Weiland (2017)**：MBSE支持NASA项目生命周期技术评审

## 与MOSA/数字工程的关系

NASA-HDBK-1009A是NASA MBSE实践的**最直接操作指南**：

- **SysML元模型**直接支持[[model-based-systems-engineering]]在NASA的实施
- **NASA SE引擎对齐**确保建模活动与NPR 7123.1流程一致——这是[[nasa-se-handbook-rev2]]的建模层
- **V&V模型化**与[[nasa-hdbk-7009a]]的M&S V&V体系互补
- **数据生成能力**（Section 9）直接服务于[[nasa-hdbk-1004]]中的MBx数据交付
- **MBSE Grid方法**为MOSA接口建模提供组织框架
- **从模型到文档**的自动化生成能力是数字工程"基于模型而非基于文档"的核心使能器
- SysML v1.7→v2过渡是[[sysml-v2-transition-bottleneck]]的关键影响因素

## 相关内容

- [[nasa-se-handbook-rev2]] — NASA系统工程手册（SE引擎基础，本文档的SE流程对齐基础）
- [[nasa-hdbk-7009a]] — NASA建模与仿真手册（M&S V&V，与本文档的V&V建模互补）
- [[nasa-hdbk-1004]] — NASA数字工程采办框架（本文档生成的MBx数据可直接用于DRD交付）
- [[ieee-nasa-de-journey-2024]] — NASA数字工程转型历程（MBSE部署状态）
- [[digital-engineering-ecosystem]] — 数字工程生态系统概述
- [[digital-engineering-practice]] — 数字工程实践
- [[model-based-systems-engineering]] — 基于模型的系统工程
- [[sysml-v2-specification]] — SysML v2规范（本文档基于v1.7，v2过渡是下一步）
- [[three-se-handbooks-complement]] — 三本SE手册互补
- [[incose-se-handbook-v5]] — INCOSE SE Handbook V5

---

*本文档是NASA MBSE实践的最直接操作指南，从元模型定义到SysML示例到SE产品生成，是数字工程建模层的核心参考。*
