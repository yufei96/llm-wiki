---
title: "自主政府参考架构（A-GRA）"
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: [A-GRA, GRA, MOSA, CCA, 自主, 开放架构, 设备级, NGAD, 算法市场, 供应商锁定]
sources:
  - raw/articles/afrc-a-gra-cca-validation-2025.md
  - raw/articles/executivegov-a-gra-cca-2025.md
  - raw/articles/csis-mosa-burden-sharing-2025.md
  - raw/articles/dau-next-gen-acquisition-2024.md
---

# 自主政府参考架构（A-GRA）

## 摘要

自主政府参考架构（Autonomy Government Reference Architecture, A-GRA）是美国空军主导的政府拥有模块化开放系统框架，为CCA（协同作战飞机）平台建立通用的自主任务标准。A-GRA在开放架构四层体系中位于**设备级（Equipment/Unit）**，其核心使命是**防止供应商锁定，建立自主算法竞争市场**。2026年2月，A-GRA已在多个供应商平台和机型上完成验证——RTX Collins在YFQ-42（General Atomics）、Shield AI在YFQ-44（Anduril）上分别完成半自主飞行测试，证明任务软件可以与特定飞行器硬件解耦。

## 核心目标

1. **防止供应商锁定**：建立政府拥有的自主标准，避免任何单一供应商控制自主能力生态
2. **算法竞争市场**：在任何A-GRA兼容平台上快速部署来自不同供应商的最佳算法
3. **跨平台扩展**：架构可扩展到多个平台和任务类型
4. **降低进入门槛**：为传统和非传统国防企业提供统一的自主集成框架
5. **可负担性与可扩展性**：通过标准化降低集成成本，支持规模化部署

## 核心特点

### 政府拥有的开放自主标准

- **架构所有权归政府**：接口定义和标准由政府维护，非供应商专利
- **开放通用接口**：所有接口标准化，不依赖特定供应商实现
- **模块化设计**：自主架构可适配不同平台和任务需求

### 跨供应商验证

2026年2月的关键里程碑——A-GRA在多个平台上完成跨供应商验证：

| 自主供应商 | 飞行平台 | 机型 | 验证内容 |
|-----------|----------|------|----------|
| RTX Collins Aerospace | General Atomics | YFQ-42 | 半自主飞行测试 |
| Shield AI | Anduril | YFQ-44 | 半自主飞行测试 |

> **Col. Timothy Helfrich**（战斗机和先进飞机投资组合采办执行官）："在多个合作伙伴间验证A-GRA对我们的采办策略至关重要。它证明我们不会被锁定到单一解决方案或单一供应商。我们正在建立一个竞争生态系统，在这个系统中，最佳算法可以快速部署到任何A-GRA合规平台上的作战人员手中，无论算法由哪个供应商提供。"

### 软件硬件解耦

- **核心能力**：任务软件可与特定飞行器硬件解耦
- **战略意义**：打破技术集成壁垒，构建更具竞争力和创新力的生态系统
- **实践证明**：同一自主架构在不同机身（YFQ-42 vs YFQ-44）和不同自主供应商（Collins vs Shield AI）间成功运行

### 快速迭代能力

- **敏捷开发**：支持跨机队快速迭代战术和能力
- **算法快速注入**：来自多元化供应商（包括非传统企业）的新软件和算法可快速上架
- **威胁响应速度**：保持领先于威胁变化的能力迭代节奏

## 在GRA目标架构中的位置

A-GRA位于开放架构四层体系的**设备级**，与AMS GRA等设备级标准并列：

```
武器(WOSA)  传感(COARPS)  通信    自主(A-GRA)  PNT(R-EGI)
    │           │          │         │           │
    └───────────┴──────────┴─────────┴───────────┘
                          │
              OMS（ASB隔离器）
                          │
                    ┌─────┴─────┐
                    │  FACE     │
                    │  SOSA H/W │
                    │  CMOSS    │
                    └───────────┘
```

在AFMC GRA体系（Chris Garrett 2024.9演示）中，A-GRA被列为候选GRA之一：
- **GARA** — OMS-based Government Ref Arch
- **AMS GRA** — Agile Mission Suite Gov't Ref Arch
- **A-GRA** — Autonomy Gov't Ref Arch
- **W-GRA** — Weapons Gov't Ref Arch

A-GRA为S&T到平台项目提供桥梁——GRAs和标准为社区提供设计参数，实现技术转化的速度和规模。

## 与CCA的关系

A-GRA是CCA项目的**核心自主框架**：

### CCA采办策略中的A-GRA

Andrew Hunter在2024年参议院证词中明确指出：CCA作为"下一代采办模式"的探路者，"利用了两个政府参考架构——AMS GRA和A-GRA"。A-GRA在CCA中的角色：

- **增量1**：A-GRA作为自主标准支撑CCA的设计、建造和测试
- **自主供应商选择**：RTX Collins和Shield AI作为任务自主供应商，分别集成A-GRA
- **平台供应商**：General Atomics（YFQ-42）和Anduril（YFQ-44）提供飞行平台
- **增量2**：A-GRA将继续作为国际合作的核心标准框架

### CCA生态系统扩展

A-GRA验证的生态系统模式：
- **传统国防企业**：RTX Collins Aerospace
- **非传统企业**：Shield AI（新兴防务科技公司）
- **平台供应商**：General Atomics、Anduril
- **竞争机制**：未获得增量1选项的供应商仍可竞争增量1生产和未来增量

## 与其他标准的关系

| 关系类型 | 相关标准 | 说明 |
|----------|----------|------|
| **垂直集成** | OMS/UCI | A-GRA通过OMS抽象服务总线与平台级系统集成 |
| **同层协作** | AMS GRA | 任务套件标准，与A-GRA共同构成CCA的两大GRA |
| **硬件基座** | SOSA | A-GRA的硬件组件基于SOSA标准 |
| **平台级集成** | ABMS GRA | 作战管理系统可调用A-GRA自主能力 |
| **武器集成** | WOSA | 通过UAI/CFWI与武器系统标准连接 |

## 应用案例

### CCA半自主飞行测试（2026年2月）

空军预备役司令部（AFRC）报道的关键里程碑：
- A-GRA在RTX Collins + YFQ-42（General Atomics）和Shield AI + YFQ-44（Anduril）上成功验证
- 证明同一自主架构可在不同机身和不同自主供应商间运行
- 为CCA项目的持续评估提供基础数据，支持决定性作战能力的部署

### CCA国际合作准备

CSIS报告（2024.12）建议：
- 盟国应尽早熟悉A-GRA标准，为CCA增量2国际合作做准备
- A-GRA的模块化设计支持通过模块替换实现技术敏感性的管理
- 支持建立盟国间的"生产网络"（production web），各国专注于自主能力的特定领域

### Skyborg到CCA的演进

A-GRA的技术路线可追溯到AFRL的Skyborg先锋项目：
- Skyborg作为S&T项目展示了自主架构的可行性
- 演变为CCA项目后，A-GRA成为标准化的自主框架
- 从实验室原型到作战采办的"垂直整合"路径

## 笔记

- A-GRA的2026年2月验证是CCA项目的关键转折点——它首次证明任务自主软件可以跨机身和跨供应商运行，直接打破了"供应商锁定"的质疑
- A-GRA的治理模式（政府拥有架构）与商业模式（供应商竞争市场）的结合，是MOSA五原则在自主领域的典型实践
- Col. Helfrich的表述"best algorithms can be deployed rapidly"暗示A-GRA可能支持类似App Store的算法部署模式
- 与AMS GRA的分工值得注意：AMS GRA定义"任务系统"（传感器到显示），A-GRA定义"自主决策"——两者共同构成CCA的完整软件栈
- A-GRA的"common user experience"特性（DAU演示）意味着不同供应商的自主算法在操作员界面上应呈现一致体验
- 非传统企业（如Shield AI）的参与证明A-GRA确实在降低进入门槛——这是MOSA政策目标的重要验证
- A-GRA的验证涉及4个不同的实体（2个自主供应商 + 2个平台供应商），展示了MOSA生态系统的复杂供应链关系

---

*基于AFRC新闻稿、ExecutiveGov报道、CSIS分析报告、DAU演示综合整理。2026-05-06创建。*
