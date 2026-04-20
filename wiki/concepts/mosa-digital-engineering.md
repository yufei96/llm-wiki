---
title: "MOSA与数字工程"
created: 2026-04-19
updated: 2026-04-19
type: concept
tags: [MOSA, 数字工程, DEE, MBSE, 数字孪生, 基于模型]
sources: [raw/papers/dodi-5000-97-digital-engineering-2023.pdf, raw/papers/dsb-digital-engineering-2024.pdf]
---

# MOSA与数字工程

## 概述

MOSA从采办策略扩展为数字工程生态系统（DEE）的技术基础——这一质变发生在2023年DoDI 5000.97发布时。MOSA不再只是"怎么买模块化系统"，而是"怎么用数字化方式建一切系统"。

## 数字工程是什么

数字工程（Digital Engineering）是美国国防部推行的工程方法转型，核心是从**基于文档**转向**基于模型**：

| 传统方法 | 数字工程 |
|---------|---------|
| 文档驱动 | 模型驱动 |
| 阶段门审批 | 持续数据流 |
| 事后集成测试 | 虚拟验证与确认 |
| 纸质接口定义 | 数字线程贯通 |

## DoDI 5000.97九大要素

2023年发布的数字工程指令定义了DEE的九大技术要素，MOSA位列其中：

1. **权威数据源（Authoritative Data Source）** — 单一真实来源
2. **数字线程（Digital Thread）** — 贯穿生命周期的数据流
3. **数字孪生（Digital Twin）** — 物理系统的虚拟镜像
4. **基于模型的系统工程（MBSE）** — SysML/Cameo等
5. **模块化开放系统方法（MOSA）** — 开放接口支持模型互操作
6. **自动化测试与评估（T&E）** — 虚拟+物理联合测试
7. **DevSecOps** — 持续集成/持续部署
8. **数据治理** — 质量、可访问性、安全
9. **数字工程环境（DEE）** — 基础设施支撑

## MOSA在DEE中的角色

MOSA为数字工程提供**互操作基础**：

- **模型互操作**：不同工具生成的模型（MBSE、CFD、FEM、控制仿真）通过开放接口交换数据，不绑定单一工具链
- **数字线程贯通**：模块化接口定义是数字线程的"路由表"——数据流沿着接口定义的边界流动
- **供应商中立**：避免被单一数字工程工具（如Dassault 3DEXPERIENCE、Siemens Teamcenter）锁定

## DSB 2024报告的关键发现

国防科学委员会2024年数字工程报告指出：

- MOSA是DEE的**技术基础层**，不是可选项
- 自动化T&E依赖MOSA接口定义来实现虚拟组件替换
- 当前挑战：MOSA的"一致性认证"原则在数字工程环境中没有对应工具
- 建议：将WOSA架构工具集成到数字工程工作流中

## 已补充材料

- ✅ ASD(R&E) 2018数字工程战略 — `[[dod-de-strategy-2018]]`
- ✅ MBSE方法论调查 — `[[incose-mbse-methodology-survey]]`
- ✅ ISO/IEC/IEEE 15288:2023 — `[[iso-15288-2023]]`

## 仍待补充

- DoDI 5000.02 Section 3.10 — AAF框架中的DE政策要求
- 各军种DE实施计划（Army/Navy/Air Force）
- SysML v2标准原文

## 相关内容

- [[mosa-defense-acquisition]] — MOSA核心概念
- [[dodi-5000-97-digital-engineering]] — DoDI 5000.97 source页
- [[dsb-digital-engineering-2024]] — DSB数字工程报告source页
- [[wosa-architecture-tools]] — WOSA工具链
- [[modular-architecture-patterns]] — 模块化架构模式
- [[dod-de-strategy-2018]] — DoD数字工程战略（2018纲领文件）
- [[incose-mbse-methodology-survey]] — MBSE方法论调查
- [[iso-15288-2023]] — ISO/IEC/IEEE 15288系统生命周期过程
- [[osa-contract-guidebook-v1.1]] — OSA合同指南
