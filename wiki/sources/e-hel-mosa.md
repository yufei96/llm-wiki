---
title: "E-HEL持久高能激光定向能武器MOSA实施"
created: 2026-04-26
updated: 2026-04-26
type: source
tags: [MOSA, E-HEL, 陆军, 定向能武器, DEWS参考架构, HII, 激光武器, GPR]
sources: [raw/articles/e-hel-mosa-case.md]
---

# E-HEL持久高能激光定向能武器MOSA实施

## 摘要

持久高能激光（E-HEL）是美国陆军首个定向能武器系统采购项目（program of record），由快速能力与关键技术办公室（RCCTO）定向能项目办公室（DEPO）管理。E-HEL从设计之初即采用MOSA，基于MITRE公司开发的DEWS MOSA参考架构（v1.0，2022年6月）进行开发，该架构由国防部副部长（研究与工程）办公室委托编制，适用于所有新的定向能系统。所有E-HEL子系统接口均附带政府目的权利（GPR）。

## 关键要点

- **MOSA实施状态**：从设计之初即采用MOSA，基于DEWS MOSA参考架构
- **DEWS参考架构**：由MITRE开发，OUSD(R&E)委托，适用于所有新的定向能系统
- **平台类型**：新研（Greenfield），陆军首个定向能武器采购项目
- **采办路径**：快速原型（MTA），由RCCTO管理
- **IP策略**：所有子系统接口附带GPR，模块内部保留供应商专有权利
- **灰盒概念**：架构定义模块功能（做什么），而非实现方式（怎么做）
- **灵活部署**：可配置为托盘化构型或集成到JLTV上，满足C-17空运要求
- **供应商竞争**：RFI要求基于DEWS MOSA架构，支持大小企业全面参与

## DEWS MOSA参考架构特点

1. 服务和领域无关，适用于所有定向能系统
2. 基于MOSA原则，利用开放/商业标准
3. 非专有、供应商无关的模块和接口定义
4. 保护供应商知识产权，模块内采用平衡的数据权利
5. 大小企业均为架构开发和治理的全面合作伙伴
6. 仅在必要时创建新标准

## 关键模块化子系统

1. 激光源模块（经验证的激光技术）
2. 光束控制/定向模块
3. 目标探测与跟踪模块（支持Group 1-3 UAS跟踪）
4. 电源与热管理模块
5. 指挥控制与通信模块（接受FAAD系统目标指示）
6. 平台适配模块（托盘化或JLTV集成）

## 主要里程碑

| 时间 | 事件 |
|------|------|
| 2024-07 | RCCTO发布E-HEL特别通知 |
| 2025-03 | HII Mission Technologies获得原型开发合同 |
| 2025-11 | RCCTO/DEPO发布E-HEL生产RFI（最多20套系统） |
| FY26 Q2+ | 计划启动竞争性源选择 |

## 原始资料链接

- [MITRE DEWS MOSA参考架构（PDF）](https://apps.dtic.mil/sti/trecms/pdf/AD1214114.pdf)
- [HII合同公告](https://hii.com/news/hii-is-awarded-contract-to-develop-high-energy-laser-weapon-system-for-the-us-army)
- DAU演示："Let's Be Modular and Open – Common Architecture for Directed Energy Weapons Systems"（2022年10月）

## 相关内容

- [[mosaic-modular-open-systems-approach]] — MOSA概念定义与理论框架
- [[dodi-5000-80-middle-tier-acquisition]] — 中间层采办指令
- [[mosa-implementation-guidebook-2025]] — 2025年国防部MOSA实施指南手册
- [[dfars-part-227-patents-data-and-copyrights]] — 数据权利与知识产权法规
