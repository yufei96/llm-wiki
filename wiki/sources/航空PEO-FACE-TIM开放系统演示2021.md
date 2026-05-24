---
title: "PEO Aviation FACE TIM 2021 Open Systems Demonstration"
created: 2026-04-29
updated: 2026-04-29
type: source
sources: [raw/papers/航空PEO FACE TIM 2021演示.pdf, raw/articles/航空PEO FACE TIM 2021演示.md]
author: "Christopher Edwards, PEO Aviation MOSA Transformation Office"
tags: [PEO Aviation, FACE标准, 开放系统演示, TIM, MOSA一致性, TSS, ARINC-661, AMCE]
confidence: EXTRACTED
evidence: "直接从原始文档提取"
---

# PEO Aviation FACE TIM 2021 Open Systems Demonstration

## 摘要

2021年6月29日PEO Aviation在FACE技术互通会议（TIM）上的开放系统演示文档。由Christopher Edwards代表MOSA转型办公室发布，展示了MOSA TO的五大技术目标及其实现方式。演示汇集了20家行业公司、9个DoD组织、29个软件产品、5个操作系统、7个硬件产品和8个TSS产品，是FACE生态系统迄今为止最大规模的集成演示。

## 要点

### 技术目标
1. **MOSA一致性能力** — TES HOST测试演示、FACE一致性软件使用、FACE传输用于集成
2. **演练AMCE概念与假设** — 开放图形接口、开放传输、可配置处理、混合关键性、多TSS实现
3. **FACE/SOSA互操作性** — 容器探索（Stellar Relay）、来宾操作系统、通过多处理卡分离DAL
4. **跨平台应用集成** — 将持续机队飞机系统软件集成到FACE架构（PM UH/FW/EUAS/AMSA/CARGO）
5. **对演示系统建模** — 捕获关键接口、物理/逻辑系统模型、KILA映射

### MOSA TO与MOSA五大原则的对应
- **建立赋能环境** → 组织和结构化讨论、RADD参考架构描述文档
- **采用模块化设计** → EAF定义MSC为模块化元素、架构描述中的合理性说明
- **指定关键接口** → 通过ACWG审查行业输入、EAF中的关键接口开发
- **使用开放标准** → EAF中使用开放标准、实施指南和RADD中标准应用指导
- **认证一致性** → MOSA一致性能力评估、多次里程碑审查和ITRA评估支持

### 参与方（规模）
- **20家行业公司**：AdaCore、Ansys、Avalex、BAE、Bell、Boeing、Collins、DDC-I、General Atomics、L3/Harris、Lockheed Martin、Lynx、Mercury Mission Systems、NAI、Northrop Grumman、OAR、Parry Labs、RTI、Skayl、TES、Wind River
- **9个DoD组织**：DEVCOM/ASIF、DEVCOM AvMC/TDD-A、DEVCOM/CAPT、PEO Aviation、PM AMSA/UAS/UH/CARGO/FW、PMA 209（海军）
- **29个软件产品**、**5个操作系统**（CentOS 7、DDC-I DEOS+RTEMS、LynxOS 178、RedHat 8、VxWorks）
- **7个硬件产品**、**8个TSS产品**

### 关键技术集成
- **飞行显示**：UH-60V飞行甲板软件在TRMC上、Ansys ARINC-661 CDS、Avalex替代显示器
- **动力系统**：ITEP发动机PSSS、ARINC 429总线、TSS替换演示（RTI DDS ↔ 60V传输）
- **导航**：Collins MFMS FACE一致性UoC、Collins AAR一致性UoC、威胁过滤器TSS转换
- **编队**：PM EUAS+UH PO LOI 4集成、多TSS代理方法（Skayl开发）、FACE 2.1和3.0版本混合
- **战术**：ADS-B+IDM+BAE相关器+Link-16+ATAK设备、FACE 2.1→3.x传输桥接
- **TRMC**：T4080处理器+VxWorks、60V软件+Ansys CDS
- **PSM**：P2080处理器+VxWorks作为虚拟机管理器、LynxOS来宾OS
- **Stellar Relay**：Intel i7+Red Hat Linux+Docker容器、PM EUAS的Grey Eagle计算环境
- **Mercury AMCS原型**：双Intel i7卡、混合DAL实现（RTOS+Red Hat Linux）
- **SIU（NAI）**：ARM处理器+FACE一致性DEOS和RTEMS、HOST/SOSA硬件方法

### 关键技术发现
- FACE Technical Standard 3.0的新特性提供了极其有效的方式来混合传输而无需重新编译软件
- FACE方法包含如何将FACE技术标准带入遗留系统的指导，通过FACE包装器实现
- 容器在航电系统中仍有差距：当前实现使用的代码无法达到飞行关键适航性
- 多TSS实现需要代理方法来支持不同FACE技术标准版本之间的无缝互操作
- TSS替换的复杂性表明需要成熟的系统模型来驱动TSS代码和配置生成器

### MOSA法定定义（引用10 U.S. Code 2446a）
- 采用使用模块化系统接口的模块化设计
- 经受验证以确保相关模块化系统接口
- 使用允许可分割性的系统架构
- 遵守FAR中规定的10 U.S. Code 2320技术数据权利指南

## 对MOSA的意义

这份文件是MOSA从理论到实践的**最生动证明**：
- **FACE生态系统的成熟度**：20家公司×29个软件产品×8个TSS在一个演示中集成
- **MOSA互操作性的真实案例**：不同FACE版本（2.1/3.0/3.1）、不同TSS（RTI DDS/Kafka/CiNC/L3H/NG）、不同RTOS（VxWorks/LynxOS/DEOS/CentOS）在同一系统中共存
- **遗留系统集成路径**：UH-60V软件、IDM应用等通过FACE包装器和TSS桥接融入开放架构
- **硬件MOSA标准的实践**：TRMC、PSM、Stellar Relay、SIU、Mercury AMCS展示了HOST/SOSA/CMOSS兼容硬件的实际应用
- **挑战暴露**：TSS替换复杂性、容器适航性差距、CSM开发困难
