---
title: "From Concept to Capability to Compliance: Making MOSA Work in Avionics"
source: http://mil-embedded.com/avionics/computers/from-concept-to-capability-to-compliance-making-mosa-work-in-avionics
author: Paul Maguire (Knowmadics)
date: 2026-05-07
publication: Military Embedded Systems
type: article
tags: [MOSA, avionics, certification, FACE, SOSA, OpenVPX, DO-178C, DO-254, integration]
---

# From Concept to Capability to Compliance: Making MOSA Work in Avionics

**Author:** Paul Maguire, Knowmadics
**Publication:** Military Embedded Systems, May 7, 2026
**Source:** http://mil-embedded.com/avionics/computers/from-concept-to-capability-to-compliance-making-mosa-work-in-avionics

## 核心论点

MOSA的目标已经确立，但交付滞后。项目往往在字面上满足MOSA合规要求，却未能实现其预期的作战敏捷性。这不是概念的失败，而是当前MOSA实施和激励方式的反映。认证体制、采办时间线和供应商商业模式仍然主要为稳定性和控制而优化，而非为快速集成和互操作性。

## 关键摩擦点

### 1. 认证与适航性约束

主要摩擦点是认证和适航性体制。军用航电受安全标准（软件DO-178C、硬件DO-254）约束，这些标准不关心模块化。

- 当供应商在OpenVPX机箱中更换卡或更新FACE兼容环境中的软件模块时，速度优势往往会碰壁
- 当前协议通常要求对即使是微小的模块化变更也进行完整的系统重新认证
- 战术边缘的创新周期现在以月为单位（受商业硅片和AI快速进步驱动），而认证周期仍以年为单位
- 近期对DoD作战测试与评估（OT&E）项目的削减加剧了这一脱节

### 2. 多厂商架构中"开放"的极限

MOSA实施并不总能达到架构预期的开放程度。常见问题包括：

- 供应商控制的中间件
- 不完整的接口文档
- 封闭的开发工具链
- 平台可能在纸面上符合MOSA，但如果主承包商掌握API和数据模式的密钥，政府仍被锁定在专有生态系统中

这种缺乏真正透明度的情况阻碍了传感器到射手的管道——如果模块通过专有黑盒中间件通信，杀伤链的速度由最慢供应商的共享意愿决定。

### 3. 战术边缘性能

任务关键系统要求极低延迟、高计算密度和紧密时序同步。FACE和SOSA等标准为互操作性而设计，但抽象层和中间件引入了开销。

- 高强度冲突中，延迟直接影响电子战和自主飞行控制等任务性能
- 模块化抽象与生存所需裸机性能之间存在持久张力
- 矫正方法是**操作员锚定工程**（operator-anchored engineering）——由在对抗环境中依赖这些系统的操作员验证设计

### 4. 硬件刷新周期 vs 商业计算

- OpenVPX和SOSA标准成功创建了模块化硬件基础，但难以跟上AI加速器和GPU的快速演进
- 商业计算周期每12-18个月更新一次，而军用资质周期可延长至十年
- MOSA合规加固机箱部署时，内部处理能力往往落后最新版本三代
- 需要更好地容纳异构架构并能以商业市场速度刷新的硬件框架

### 5. 分布式架构中的集成负担

MOSA改变了集成风险的分配方式：

- 传统专有建造中，主承包商负责使一切协同工作的风险
- MOSA世界中，集成责任通常上移至政府项目办公室或系统集成商
- 导致更高的系统工程负担、更复杂的接口管理和配置控制、跨模块版本控制挑战
- **模块化不消除复杂性，而是重新分配复杂性**

### 6. 开放系统中的网络安全

- 开放接口固有地增加了攻击面
- 在战术环境中验证第三方模块和保护固件更新链复杂且资源密集
- 跨多厂商生态系统维护网络安全合规与适航认证同样具有挑战性

## MOSA正在交付可衡量收益的领域

- 采用OpenVPX和SOSA方法的项目在边缘任务计算机上看到更快的增量刷新
- 此前被锁定在主要平台之外的小型创新技术企业现在能够贡献特定模块
- 多域融合架构开始展示可重用能力库如何加速跨不同技术域的交付
- FACE技术标准使任务关键代码可以跨平台移植，所需工作量大幅减少

## 需要改变什么

1. **完整可访问的接口定义**——数据模式、API和文档，使集成无需依赖单一供应商
2. **认证方法演进**——将安全关键航电功能与快速演进的任务应用分离，使软件更新无需触发完整系统重新认证
3. **集成从后期活动变为持续学科**——共享集成环境提供公共空间，频繁早期验证模块
4. **硬件策略反映商业创新步伐**——更频繁地插入新计算技术，特别是AI和自主工作负载

## 关键引用

> "Programs often meet the letter of MOSA compliance without realizing the operational agility it was intended to enable."

> "Modularity does not eliminate complexity, but rather redistributes it."

> "Innovation cycles at the tactical edge are now measured in months... yet certification cycles remain measured in years."
