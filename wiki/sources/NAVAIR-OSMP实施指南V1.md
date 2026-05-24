---
title: "NAVAIR OSMP Implementation Description Guide v1.0 2025"
created: 2026-05-07
updated: 2026-05-21
tags: [OSMP, NAVAIR, MOSA, 实施指南, 合同语言, 采办策略]
source:
  - raw/papers/NAVAIR-OSMP指南V1 2025.pdf 2025.pdf 2025.pdf
  - raw/articles/NAVAIR-OSMP指南V1 2025.md
confidence: EXTRACTED
evidence: "从原始文档逐节提取关键框架、RFP语言模板和常见错误"
type: source
---

# NAVAIR OSMP Implementation Description Guide v1.0 2025

## 摘要

NAVAIR 于 2025 年 6 月发布的 OSMP 实施描述指南 v1.0（35页，Approved for Distro A）。由 Rich Ernst 主导编写，DASN/MITR 审阅。本指南是海军航空系统司令部对 DoD MOSA 政策的**实操级响应**，提供了从采办策略到合同条款的完整 OSMP 编写框架，包含可直接裁剪的 RFP Section L/M 语言模板、CDRL 交付要求和里程碑对齐方案。

核心贡献：首次系统化地将 MOSA 五大原则与 DoDI 5000 采办框架对齐，并给出了从 Pre-Milestone A 到全生命周期的 OSMP 演进路线图。

## NAVAIR 的 MOSA 实施五阶段框架

指南提出 BDFD（Business-Driven Functional Decomposition）驱动的五阶段 MOSA 实施框架：

1. **业务模型与架构分解**：系统分解为可替换的模块化单元（传感器模块、处理器、软件服务），每个模块有明确定义的角色。允许多供应商竞争单个组件，降低全生命周期成本
2. **关键接口定义**：硬件、软件、数据格式的交互点通过开放标准接口定义。供应商基于政府所有或开放标准的接口开发，促进互操作性和模块可复用性
3. **模块化系统接口（MSI）仓库**：中央仓库存储接口定义、版本历史和使用指南，为所有供应商提供透明的关键接口规范访问，减少集成错误
4. **标准合规**：采用广泛接受的共识标准（OMS、UCI、AMS-GRA、FACE、SOSA、WOSA、POSIX）
5. **验证与确认测试（VVT）**：独立测试确保模块符合开放系统架构和开放标准。支持渐进式模块认证，允许预认证供应商方案加速部署

## OSMP 过程框架（六步流程）

指南定义了从业务目标到系统增量交付的完整流程：

1. **对齐海军与项目办业务目标** — 确保系统开发方法与组织战略一致
2. **选择 MOSA 与方法论** — 确定实现模块化开放系统的最佳方法
3. **执行 MOSA 策略** — 五个子步骤：
   - 设计模块级别架构
   - 记录模块化选择理由
   - 确定设计披露和数据权利策略
   - 指定接口及管理流程
   - 定义生命周期管理流程
4. **更新业务和技术需求** — 反映演进中的需求
5. **迭代评估与规划（MOSA 支持计划）** — 持续改进和调整
6. **交付系统增量** — 分阶段集成和交付模块化组件

## 与 DoDI 5000 采办框架的战略对齐

指南强调 OSMP 必须在采办生命周期的**最早阶段**（Pre-Milestone A / Milestone A 的 Materiel Solution Analysis 阶段）就开始对齐 DoDI 5000。四条对齐原则：

- **塑造系统需求**：将模块化、互操作性、技术复用作为驱动系统设计的基本需求
- **优化采办策略**：利用 OSMP 作为关键使能器，设计鼓励供应商竞争、采用开放标准的合同方法
- **降低成本和风险**：减少对专有技术的依赖，促进竞争性供应商环境
- **增强互操作性和未来集成**：早期和持续的开放架构强调，确保新系统与现有和未来技术无缝集成

## 提案评估与合同授予指南

指南给出了可直接裁剪的 **RFP 语言模板**：

**Section L 建议：**
> "The Offeror SHALL prepare and submit a draft OSMP IAW OSMP DID [DI-MGMT-82099 Rev A]，detailing the development of an open system. This includes their open architecture approach (3.3.1), design disclosure and data rights strategy (3.3.5), and interface design and management (3.4)."

**Section M 评估因素：**
> "The Government will evaluate the extent to which the proposed approach supports the development and sustainment of an open system. This includes considerations such as design disclosure, data rights strategy, interface design, and interface management. The Government will assess the offeror's approach to managing sub-vendor relationships, ensuring that expectations for openness and modularity are effectively flowed down."

**合同授予后交付要求：**
- 合同授予后短期内交付初始 OSMP（最少覆盖 3.3.1、3.3.5、3.4 三节）
- 每个重大里程碑前提交更新版 OSMP + 变更摘要
- SOW 中明确引用 OSMP DID，作为合同约束条款
- CDRL 设置周期性交付项，反映迭代更新过程

## 关键业务与技术驱动因素

指南从 11 个维度阐述 OSMP 需考虑的关键因素：

- **系统工程（含 BDFD）**：业务驱动的功能分解，将技术决策与成本/竞争/可持续性对齐
- **软件工程**：软件组件化，遵循开放标准
- **模块化分解与评估**：模块粒度决策依据业务案例
- **接口管理**：ICD 的版本控制、变更管理、兼容性追溯
- **数据权利策略**：区分政府目的权利、有限权利、商业权利
- **知识产权管理**：避免供应商锁定，保障竞争性维护
- **竞争性采办策略**：通过开放接口吸引多方参与
- **生命周期成本**：通过模块化降低维护和升级成本
- **技术插入路径**：预留升级槽位和接口扩展能力
- **供应链安全**：多源供应降低单点依赖
- **验证与认证**：增量验证策略，降低集成风险

## 附录 A：MOSA 实施常见错误

指南附录列出 MOSA 实施中的典型问题：

1. **术语误用**：
   - 不存在 "MOSA 接口" → 正确术语是 **开放接口**
   - 不存在 "MOSA 标准" → 正确术语是 **开放标准**
   - 避免笼统使用 "MOSA 需求" → 应精确指定具体需求
2. **MOSA ≠ 架构**：MOSA 的 "A" 代表 Approach（方法），不是 Architecture。MOSA 是一种方法论，OSA（开放系统架构）才是其产出的架构实现
3. **开放系统架构三个必要元素**：模块化 + 基于开放标准的开放接口 + 验证机制。缺少任何一项都需重新评估
4. **所有权模式偏离**：指南指出，在特定情况下（紧急需求、COTS 产品能完全满足需求且寿命有限），专有方案可能被接受——但必须记录未来迁移策略
