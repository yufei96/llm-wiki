---
title: "先进战斗管理系统政府参考架构（ABMS GRA）"
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: [ABMS, ABMS-GRA, GRA, CJADC2, BATTLE-NETWORK, C2, CBC2, 作战管理, 平台级, 数字基础设施]
sources:
  - raw/articles/afmc-abms-distributed-connectivity.md
  - raw/articles/dote-fy2024-abms.md
  - raw/articles/senate-defense-hunter-testimony-2024.md
confidence: EXTRACTED
evidence: "基于原始文档综合"
---

# 先进战斗管理系统政府参考架构（ABMS GRA）

## 摘要

先进战斗管理系统政府参考架构（Advanced Battle Management System Government Reference Architecture, ABMS GRA）是空军部（DAF）BATTLE NETWORK的核心，也是空军对联合全域指挥控制（CJADC2）的贡献。ABMS GRA在开放架构四层体系中位于**平台级（Platform）**，由DAF PEO C3BM（指挥、控制、通信和作战管理计划执行办公室）主导。与传统将作战管理能力嵌入单一平台（如E-8 JSTARS）的方式不同，ABMS GRA采用**分布式方法**——通过网络连接现有且物理分散的传感器和平台，实现作战管理能力的网络化集成。

## 核心目标

1. **分布式作战管理**：从单平台集中式向分布式网络化作战管理转型
2. **DAF BATTLE NETWORK**：建立连接空军和太空军传感器、系统和武器的数据网络
3. **CJADC2空军贡献**：作为联合全域指挥控制的空军组成部分
4. **软件定义网络**：基于可适应的软件定义网络架构实现作战管理
5. **决策优势**：为作战人员提供实时、完整的战场态势和快速决策能力

## 核心特点

### 五大产品线

ABMS GRA由五个产品分支和一个企业系统工程团队组成：

| 产品线 | 功能 | 说明 |
|--------|------|------|
| **数字基础设施（Digital Infrastructure）** | 网络连接基础 | DAF BATTLE NETWORK的"幕后"基础——使所有系统协同运行的网络层 |
| **可部署系统（Deployable Systems）** | TOC-L战术作战中心 | 为前沿部署作战管理人员提供的紧凑模块化可部署套件 |
| **软件和应用（Software & Apps）** | CBC2云指挥控制 | 唯一已安排作战测试的ABMS组件 |
| **空中网络（Aerial Networking）** | 空中通信网络 | 空中平台间的数据链路和网络连接 |
| **远程火力（Remote Fires）** | 远程打击 | 远程火力控制和打击协调 |

### 分布式架构哲学

ABMS GRA的根本转变是**从平台中心到网络中心**：

- **旧模式**：E-8 JSTARS将作战管理能力嵌入单一平台
- **新模式**：通过网络连接物理分散的传感器和平台，最大化生存性
- **Dr. Bryan Tipton**（DAF BATTLE NETWORK架构师）："你必须创建一个强调架构能力而非各个单独能力性能规格的系统。无论你认为自己今天有多好，别人在12、18、24或36个月后会更好。如果你不能快速引入和集成那个新能力，你就会输。"

### 软件定义网络

- **核心理念**：基于可适应的软件定义网络进行作战管理
- **自适应性**：系统能够快速整合新的能力来源
- **多路径连接**：可靠地通过不同路径连接，确保网络韧性

### CBC2：云指挥控制

CBC2（Cloud-Based Command and Control）是ABMS中最关键的软件组件：
- **功能**：取代Battle Control System-Fixed，创建单一融合C2空中态势图
- **开发合作**：与加拿大皇家空军合作开发
- **主承包商**：SAIC（弗吉尼亚州罗斯林）
- **采购路径**：软件采购路径
- **作战测试**：唯一已安排作战测试的ABMS组件

## 在GRA目标架构中的位置

ABMS GRA位于开放架构四层体系的**平台级**，定义整个平台（飞机、指控系统）的作战管理架构：

```
┌─────────────────────────────────────────────────────────────────┐
│  第1层：平台级（Platform）                                       │
│  OMS/UCI · UCS/STANAG 4586 · ABMS GRA ← 此处                   │
├─────────────────────────────────────────────────────────────────┤
│  第2层：分系统级（Subsystem）                                    │
│  WOSA · DEWS MOSA RA · NC3 GRA · Sentinel GRA · CFW ICD        │
├─────────────────────────────────────────────────────────────────┤
│  第3层：设备级（Equipment/Unit）                                 │
│  SOSA · MORA · CMOSS · VICTORY · AMS GRA · A-GRA               │
│  PNT GRA/R-EGI · COARPS · SCARS · Mission Planning GRA         │
├─────────────────────────────────────────────────────────────────┤
│  第4层：部组件级（Component）                                    │
│  FACE · HOST                                                    │
└─────────────────────────────────────────────────────────────────┘
```

ABMS GRA在架构层次中的关系：
- **上层**：ABMS GRA是空军对CJADC2的贡献，连接联合层级的指挥控制
- **同层**：与OMS/UCI（任务系统互操作性）和UCS（无人系统指控）协作
- **下层**：使用COARPS（雷达）、AMS GRA（任务套件）、A-GRA（自主）等设备级标准

## 与其他标准的关系

| 关系类型 | 相关标准 | 说明 |
|----------|----------|------|
| **任务系统** | OMS/UCI | ABMS通过OMS标准实现子系统间互操作 |
| **设备级调用** | AMS GRA | ABMS使用AMS GRA规范的任务系统 |
| **自主能力** | A-GRA | ABMS可调用A-GRA规范的自主算法 |
| **传感器** | COARPS | ABMS集成COARPS规范的雷达数据 |
| **PNT** | R-EGI | ABMS依赖PNT GRA提供定位导航授时 |
| **互操作** | CJADC2 | ABMS GRA是CJADC2的空军组成部分 |

## 应用案例

### CBC2作战测试进展

DOT&E FY2024报告对CBC2的评估：
- **季度MVCR**：空军自2023年6月起进行季度最小可行能力发布（MVCR）
- **作战评估推迟**：AFOTEC因**软件不成熟**推迟了CBC2作战评估
- **测试框架**：DOT&E于2024年8月批准CBC2 TES（测试与评估策略）和OA测试计划
- **预期时间**：CBC2 OA报告预计FY26发布
- **观察**：AFOTEC Detachment 2观察了所有MVCR事件

**DOT&E建议**：
1. 继续开发其余ABMS组件的TES
2. 提交M&S工具的VV&A计划
3. 更新CBC2网络测试策略

### TOC-L可部署系统

TOC-L（Tactical Operations Center - Light）是ABMS的重要产品：
- **用途**：为前沿部署作战管理人员提供核心网络连接
- **特点**：相对紧凑的模块化可部署套件
- **实战验证**：在陆军主导的Project Convergence - Capstone 5实验中使用
- **适用环境**：不支持持续连接和大型服务器架部署的环境

### Project Convergence - Capstone 5

ABMS的TOC-L在PC-C5中的参与展示了：
- 跨军种互操作性（空军ABMS + 陆军实验）
- 前沿部署场景下的网络韧性
- 软件定义网络在受限环境中的适应性

## 治理与组织

- **主导方**：DAF PEO C3BM
- **高级物资领导**：Col. Bai Lan Zhu
- **架构师**：Dr. Bryan Tipton（DAF BATTLE NETWORK架构师）
- **位置**：Hanscom AFB, Massachusetts
- **CBC2主承包商**：SAIC（弗吉尼亚州罗斯林）

## 笔记

- ABMS GRA的独特之处在于它是**平台级**的GRA——定义整个作战管理系统的架构，而非某个设备或子系统。这使其成为所有设备级GRA（AMS GRA、A-GRA等）的"上层用户"
- DOT&E对CBC2"软件不成熟"的评估反映了大型C2软件系统面临的共同挑战——软件复杂度高、迭代周期长、作战评估门槛高
- ABMS从E-8 JSTARS的"单平台集中式"向"分布式网络化"的转变，本质上是将作战管理能力从硬件平台转移到软件网络——这与AMS GRA的"软件定义"理念一脉相承
- CBC2与加拿大皇家空军的合作开发是ABMS GRA框架下国际合作的实例，呼应了CSIS报告中MOSA促进盟国负担分担的理念
- Dr. Tipton的"架构能力优于单个能力性能规格"的表述，揭示了ABMS GRA的核心设计哲学——系统韧性来自架构而非单一组件的优越性
- ABMS的五大产品线覆盖了从底层网络基础设施（数字基础设施）到高层应用（CBC2、远程火力）的完整栈——这在GRA体系中是最全面的平台级架构
- PC-C5实验中的TOC-L部署证明ABMS GRA正在从概念向实战能力过渡，但CBC2的OA推迟表明这一过渡仍在进行中

---

## 相关内容
- [[空军装备司令部-ABMS分布式连接]]
- [[DOT&E年度报告ABMS章节2024]]
- [[SAM-ABMS广泛机构公告]]
