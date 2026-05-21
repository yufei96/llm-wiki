---
title: "VICTORY与GVA：地面车辆现代化白皮书"
created: 2026-04-19
updated: 2026-04-19
type: source
sources: [raw/papers/victory-gva-vehicle-modernization.pdf, raw/articles/victory-gva-vehicle-modernization.md]
author: "Curtiss-Wright Defense Solutions"
tags: [VICTORY, GVA, 车辆, 以太网, COTS]
confidence: EXTRACTED
evidence: "直接从原始文档提取"
---

# VICTORY与GVA：地面车辆现代化

## 文档概况
- **全称**：Ground Vehicle Modernization with VICTORY and GVA
- **发布者**：Curtiss-Wright Defense Solutions
- **页数**：约10（白皮书）
- **类型**：技术白皮书 + COTS解决方案展示

## 核心内容

### 历史问题
传统上在战术地面车辆上添加或增强C4ISR功能是重大挑战：专有接口、高昂集成成本、长周期。

### VICTORY架构
- **以太网数据总线**：所有子系统通过以太网通信
- **SOAP/XML数据发布**：VICTORY使用SOAP和XML
- 共享态势感知、通信、武器、防护等数据
- 替代MIL-STD-1553等专有总线

### GVA架构（英国通用车辆架构）
- **DDS数据分发服务**：GVA使用DDS而非SOAP/XML
- 关注物理层：电缆、连接器、电气接口
- 包含通用HMI（人机界面）方向

### VICTORY vs GVA对比

| 方面 | VICTORY | GVA |
|------|---------|-----|
| 数据交换 | SOAP/XML | DDS |
| 覆盖范围 | C4ISR/EW系统接口 | 物理层+HMI |
| 标准层 | 软件+数据 | 硬件+物理 |
| 网络基础 | 以太网 | 以太网（共通） |
| 适用方 | 美国陆军 | 英国MoD |

### 共同点
两者都是**网络中心架构**，支持设备或服务的发布者/订阅者模型：
- VICTORY使用SOAP/XML发布数据
- GVA使用DDS发布数据
- 现代框架基于共同的以太网数据总线

### COTS解决方案
- **DBH-672 Digital Beachhead**：集成以太网交换机和GPS的共享处理单元
- 支持VICTORY网络的坚固COTS交换机LRU
- 模块化子系统：可选功能升级（交换、处理、PNT）

## 对MOSA的意义

这份白皮书展示了**MOSA模块化开放接口在地面车辆中的实际落地**：
- 以太网替代专有总线 = "开放接口"原则的物理层实现
- VICTORY/GVA的多厂商兼容 = "竞争性采购"的支撑
- COTS解决方案证明了MOSA不是纯理论——有可购买的合规硬件

**跨国互操作**：VICTORY（美国）和GVA（英国）基于共同的以太网基础但使用不同的数据分发协议，这反映了MOSA国际扩展中的实际挑战——标准趋同但不完全统一。
