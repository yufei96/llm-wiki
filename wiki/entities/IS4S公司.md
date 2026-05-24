---
source: []
title: "IS4S"
created: 2026-05-07
updated: 2026-05-24
tags: [IS4S, R-EGI, PNT, GPS, MOSA, 设计代理, M-code, GPS拒止, 开放架构, 导航战]
confidence: SYNTHESIZED
evidence: "基于IS4S官方新闻稿、DVIDS飞行测试报道、Inside GNSS里程碑报道、RNTFND MOSA分析等多源综合"
type: entity
---

# IS4S

## 摘要

Integrated Solutions for Systems（IS4S），中文常称"集成系统解决方案公司"，是一家专注于开放架构导航系统、PNT技术与国防电子系统集成的美国非传统国防承包商。IS4S在美国空军R-EGI（弹性嵌入式GPS/INS）项目中担任总设计代理（Design Agent），主导开发基于MOSA的下一代军用导航系统，旨在替代传统GPS嵌入式模块，为国防部平台提供在GPS拒止/降级环境中仍能可靠运行的定位、导航与授时能力。

## 公司成立背景

IS4S由Glenn Rolader（现任总裁兼CEO）创立，总部位于美国阿拉巴马州亨茨维尔（Huntsville, AL）——该地区紧邻红石兵工厂（Redstone Arsenal）和美国陆军航空与导弹司令部，是国防科技企业高度集中的创新走廊。IS4S定位为"集成系统解决方案"提供商，专注于复杂电子系统和导航技术的快速原型开发、开放架构设计与系统集成。

IS4S在国防采办生态中属于**非传统承包商**（Non-Traditional Defense Contractor, NTDC）——其规模和背景不同于Northrop Grumman、RTX Collins等传统防务巨头，但正因为规模灵活且专注MOSA开放架构，IS4S在R-EGI等项目中获得了核心角色。这一现象本身即是MOSA政策效果的直接体现：开放标准降低了市场准入壁垒，使创新型企业能够参与过去由巨头垄断的领域。

## R-EGI项目

### 项目概述

R-EGI（Resilient-Embedded GPS/INS，弹性嵌入式GPS/INS）是美国空军生命周期管理中心电子系统局（AFLCMC/WNX）主导的政府拥有PNT开放架构项目。IS4S在该项目中担任**总设计代理**（System Design Agent）——这是R-EGI项目最具创新性的采办模式：政府掌握架构定义权和接口标准，IS4S作为总集成方负责架构设计、系统集成和技术协调，多家供应商在统一的开放架构框架内提供竞争性子系统。

### 设计代理模式下的团队构成

IS4S作为总设计代理，协调以下核心供应商和测试单位：

| 角色 | 机构 | 职责 |
|------|------|------|
| 总设计代理 | **IS4S** | 架构设计、系统集成、项目管理 |
| SCNAV子系统 | Kearfott Corporation | 安全关键导航、IMU（环形激光陀螺仪） |
| LRU硬件/MCNAV | General Dynamics-Mission Systems | 改装F-16 LRU机箱、任务能力导航子系统 |
| GNSS接收机 | Collins Aerospace | M-Code GPS接收机 + Galileo开放服务夹层 |
| 第三方验证 | Trimble | Force 28M GPS M-Code接收机（4周内完成集成） |
| 飞行测试 | 746th/586th测试中队 | 飞行验证支持 |

### 快速原型与飞行验证

IS4S领导的R-EGI快速原型团队在**不到8个月**的时间内从团队组建到完成首飞，这在国防采办中极为罕见，体现了开放架构的集成效率。

**2024年8月-10月（Holloman AFB）**：
- 三次核心飞行测试（8月20-22日）+ 一次补充飞行测试（10月）
- C-12J测试飞机搭载改装F-16 LRU
- 验证混合M-Code GPS/IMU、仅GPS、仅IMU、MCNAV等多种操作模式
- 在White Sands Missile Range完成动态机动飞行和跨州航线飞行

**2025年2月（Centennial Airport, CO）**：
- 与AEVEX Aerospace和Northrop Grumman联合演示
- R-EGI成功集成AEVEX LynxVBN视觉导航系统（即插即用）
- 在模拟GPS拒止环境中仅使用视觉导航数据和IMU维持定位精度
- 验证Alternative PNT和ASPN23消息标准合规性
- Trimble Force 28M接收机**4周内**完成集成，展示架构灵活性

## M-Code与GPS拒止环境

### M-Code（军用GPS信号）

M-Code是美军新一代军用GPS信号，具有更强的抗干扰、抗欺骗和加密性能。R-EGI项目中Collins Aerospace提供的GNSS接收机和Trimble Force 28M均支持M-Code。2025年2月的联合飞行测试中，Northrop Grumman EGI-M的6次飞行中有5次使用了M-Code GPS（仅1次使用传统C/A码），标志着M-Code从开发测试向作战应用的过渡。

### GPS拒止环境

GPS拒止环境（GPS-Denied Environment）是R-EGI项目核心作战场景之一。在现代化电子战和对抗性空域中，GPS信号极易受到干扰、欺骗或完全阻断。R-EGI通过以下途径应对GPS拒止：

1. **多源PNT融合**：将M-Code GPS与惯性测量单元（IMU）、视觉导航、LiDAR、雷达等互补PNT源融合
2. **即插即用架构**：IS4S的pntOS和ASPN23消息标准使第三方传感器（如AEVEX LynxVBN）可快速接入
3. **分层设计**：安全关键（SCNAV）与任务关键（MCNAV）分离，即使GPS完全丢失，MCNAV仍可通过互补传感器维持导航精度

2025年2月的飞行测试成功验证了这一能力：R-EGI在模拟GPS拒止条件下仅依靠视觉导航数据和IMU维持了定位精度。

## MOSA关联

R-EGI是[[MOSA与国防采办|MOSA（模块化开放系统架构）]]原则在PNT领域的典型实现。IS4S作为设计代理，其工作贯穿以下MOSA核心要素：

| MOSA原则 | R-EGI实现 | IS4S角色 |
|----------|----------|----------|
| 模块化设计 | PNT传感器可独立替换、第三方即插即用 | 定义模块接口和集成流程 |
| 指定接口 | ASPN23消息标准化、Open VPX/VITA 46.11 | 确保接口一致性和合规性 |
| 开放标准 | SOSA、OMS、FACE四标准集成 | 架构设计与标准选型 |
| 政府拥有 | 架构定义权归AFLCMC/政府 | 支撑政府掌握技术架构 |
| 快速竞争 | 多供应商竞标、8个月内首飞 | 管理多供应商集成周期 |

IS4S通过R-EGI项目展示了MOSA的实际效益：**<8个月**完成从概念到首飞的快速原型开发、**4周内**集成第三方GPS接收机、在GPS拒止环境中成功验证视觉导航即插即用。这些成就被Inside GNSS、DVIDS、RNTFND（Resilient PNT Foundation）等多方报道。

在更宏观的[[GRA生态演进]]中，IS4S被列为通过开放架构进入传统国防市场的**新兴企业**典型代表，与Anduril、Shield AI等公司并列，共同受益于MOSA降低准入门槛的政策目标。

## 相关内容

- [[PNT政府参考架构-R-EGI导航]] — PNT GRA / R-EGI 弹性嵌入式GPS/INS概念详情
- [[R-EGI-C12J飞行测试]] — IS4S官方C-12J飞行测试新闻
- [[R-EGI导航飞行测试2024]] — DVIDS报道的飞行演示
- [[R-EGI里程碑达成2024]] — Inside GNSS关键里程碑报道
- [[R-EGI导航系统未来展望]] — RNTFND MOSA分析
- [[GRA生态演进]] — GRA体系中的IS4S定位
- [[MOSA与国防采办]] — MOSA政策背景

## 参考来源

- IS4S官方新闻稿：R-EGI Takes Flight on Military C-12J Test Aircraft (Victoria Carson)
- DVIDS Story ID 497633：R-EGI PNT Systems Flight Demonstrations (2025.05.12)
- Inside GNSS：R-EGI Program Achieves Key Milestone (2024)
- RNTFND：The Future of Navigation (MOSA) Is Happening — USAF R-EGI Project (2024.11.19)
- AFLCMC电子系统局：NAVWAR分部飞行测试简报

## 笔记

- IS4S作为非传统承包商获得R-EGI总设计代理角色，是MOSA政策效果的直接证明
- 设计代理模式（政府拥有架构 + IS4S总集成 + 多家供应商竞争）是国防采办模式的创新实践
- IS4S的pntOS政府拥有PNT操作系统是R-EGI开放软件环境的核心
- 从<8个月首飞到4周第三方集成，IS4S持续展示开放架构的速度优势
- IS4S与Northrop Grumman的EGI-M在相同测试框架中并行演示，体现了美军开放架构与传统升级双轨策略
