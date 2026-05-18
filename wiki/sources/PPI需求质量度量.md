---
title: "PPI: Requirements Quality Metrics (Halligan 1993)"
created: 2026-04-19
updated: 2026-04-19
type: source
tags: [requirements-engineering, metrics, quality, systems-engineering]
sources: [raw/papers/ppi-requirements-quality-metrics.pdf, raw/articles/ppi-requirements-quality-metrics.md]
confidence: EXTRACTED
evidence: "直接从原始文档提取"
---

# Requirements Quality Metrics: The Basis of Informed Requirements Engineering Management

## 来源信息

- **作者**: Robert J. Halligan FIE Aust CPEng IntPE(Aus)
- **机构**: Project Performance (Australia) Pty Ltd
- **发表**: 1993 CSESAW Workshop, Calvados, MD, USA
- **文档号**: PPA-005330-11 (2017年再版, 6页)
- **文件**: `raw/papers/ppi-requirements-quality-metrics.pdf`

## 核心主张

缺陷需求是国防和航天项目成本与进度超支的主导原因。TRW数据显示30%的设计问题源于错误或不完整的规格书，另有24%源于有意识偏离需求。纠正错误的成本随系统生命周期推移增加20-1000倍。

## 十大需求质量因子

| # | 因子 | 英文 | 定义 |
|---|------|------|------|
| 1 | 正确性 | Correctness | 需求陈述中无事实错误 |
| 2 | 完整性 | Completeness | 包含所有必要信息（约束、条件），使需求可实施且满足需要 |
| 3 | 一致性 | Consistency | 不与任何其他需求或自身结构冲突 |
| 4 | 清晰性 | Clarity | 无需语义分析即可理解 |
| 5 | 无歧义性 | Non-Ambiguity | 仅有一种语义解释 |
| 6 | 连通性 | Connectivity | 需求内所有术语与其他需求及定义充分关联 |
| 7 | 单一性 | Singularity | 不能合理地拆分为两个以上具有不同主语/谓语/宾语的需求 |
| 8 | 可测试性 | Testability | 存在有限且客观的过程来验证需求已被满足 |
| 9 | 可修改性 | Modifiability | 可完整一致地修改；同一需求仅规定一次 |
| 10 | 可行性 | Feasibility | 在物理约束、技术状态和其他绝对约束内可满足 |

## 需求结构模板（自然语言解析）

将需求语句解析为7个结构元素：

| 元素 | 示例（HQ交换机需求） |
|------|---------------------|
| 1. 主体 (Actor) | "an HQ Switch" |
| 2. 动作条件 (Conditions) | "In the Combat Zone" |
| 3. 动作 (Action) | "shall be given" |
| 4. 动作对象 (Object) | "two (2) independent links" |
| 5. 动作约束 (Constraints) | — |
| 6. 对象精化 (Refinement of Object) | — |
| 7. 动作精化 (Refinement of Action) | "to at least two (2) other nodes in the network" |

## 度量体系

### 产品度量

- **IRQ** (Individual Requirement Quality): 单条需求质量，0-1。= 适用元素得分之和 / 适用元素数
- **IQF1-IQF10**: 十个因子对应的单需求度量（1=无缺陷，0=有缺陷）
- **RQ** (Requirements Quality): 需求集合的聚合质量度量
- **Omission Ratio**: 遗漏比。估计现有需求暗示的缺失需求数，用于补充完整性度量

### 过程度量

| 度量 | 含义 |
|------|------|
| RSTA | 已开始分析的源需求百分比 |
| RTBD | 包含TBD的需求百分比 |
| RCOM | 已完成分析的百分比 |
| RAPP | 已批准（子需求纳入目标文档）的百分比 |
| RALL | 已分配到下级WBS元素的百分比 |

## 典型度量值（质量等级对照）

| 质量等级 | RQ | Correctness | Completeness | Consistency | Clarity |
|---------|-----|-------------|-------------|-------------|---------|
| 很差（需大量开发） | 0.01-0.3 | 0.9 | -5 | 0.9 | 0.9 |
| 尚可（可能可用于招标） | 0.3-0.7 | 0.98 | 0 | 0.97 | 0.97 |
| SRR适合推进开发 | 0.85-0.99 | 0.99 | 0.95 | 0.99 | 0.99 |
| 适合关键开发 | 0.99+ | 0.99+ | 0.99+ | 0.99+ | 0.99+ |

## 完整性估计三种方法（附录A）

1. **遗漏比法 (Omission Ratio)**: 现有需求暗示的缺失需求数量估计。适合初始完整度>50%的情况。
2. **关系规范法**: 功能需求vs外部接口需求的比例应相近（差异<10%）；其他质量需求占比：小系统5-10%，大系统约1%。
3. **历史基准法**: 基于历史数据的"应有需求量"估计。

### 历史基准需求量

| 系统 | 需求量 |
|------|--------|
| 商务喷气机 | 2500-4500 |
| 紧急通信浮标 | 100-200 |
| 心脏起搏器 | 800 |
| 大型客机 | 8000-10000 |
| 高速列车 | 4500 |

## 与知识库的关联

- 需求质量是[[MOSA需求质量]]的核心——接口定义质量直接决定MOSA成败
- PPI需求分析方法论（[[PPI需求分析方法论]]）基于此度量框架
- PM与SE整合（[[PPI-集成项目管理与系统工程]]）中的RE投资回报论证引用此论文的TRW数据
- 完整性因子（Completeness）可为负值的特性对[[MOSA与国防采办]]中的需求工程有直接影响
- MIL-STD-499B（论文引用）是[[自适应采办框架]]演化历史中的关键节点

## 关键引用

- Boehm, "Software Engineering Economics", 1981 — 修正成本增加20-1000倍的数据来源
- MIL-STD-499B Draft "Systems Engineering", 1992
- Alford, "Strengthening the Systems/Software Engineering Interface for Real-Time Systems", NCOSE 1992
- Pinkerton & Fogle, "Requirements Management/Traceability: NASA NLS", NCOSE 1992
- Fuji, IV&V course notes, 1989 — 结构模板定义来源
