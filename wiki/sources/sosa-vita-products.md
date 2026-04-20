---
title: "SOSA产品技术概览与产品指南"
created: 2026-04-19
updated: 2026-04-19
type: source_summary
source: raw/papers/sosa-vita-products-capabilities.pdf
author: "Elma Electronic"
tags: [SOSA, VITA, OpenVPX, 硬件, 产品指南]
---

# SOSA产品技术概览与产品指南

## 文档概况
- **全称**：Sensor Open Systems Architecture (SOSA) Technical Overview and Product Guide
- **发布者**：Elma Electronic（VITA/OpenVPX硬件厂商）
- **页数**：约20
- **类型**：产品导向的技术概览

## 核心内容

### SOSA标准架构
SOSA技术参考架构整合多个开放标准，定义模块化、互操作性的方法论。核心是 **VITA 65 (OpenVPX)**——广泛采用的坚固高性能计算架构和外形标准。

### OpenVPX标准族
OpenVPX定义了系统级互操作性：
- **模块到模块**：标准化接口
- **模块到背板**：数据/控制/扩展平面
- **背板到机箱**：电源/散热/机械

### SOSA引用的关键VITA标准
| VITA标准 | 功能 |
|----------|------|
| VITA 46 (VPX) | 基础坚固计算架构 |
| VITA 46.30/.31 | 高数据率VPX |
| VITA 46.6 | 千兆以太网控制平面 |
| VITA 62 | VPX电源 |
| VITA 65 | **OpenVPX**（SOSA核心） |
| VITA 65.1 | 新插槽和模块配置 |
| VITA 67 | RF/混合信号 |
| VITA 68 | SpaceVPX |

### DoD政策引用
SOSA标准被2019年DoD备忘录（国防部长和军种部长联合签署）引用，要求在适用的采办项目中考虑SOSA标准。

## 对MOSA的意义

这份产品指南展示了MOSA/SOSA从标准到**可购买硬件**的转化：
- SOSA不只是架构文档——已经有合规的商业现成（COTS）硬件产品
- VITA/OpenVPX生态提供了物理层模块化的实际载体
- 证明了MOSA"开放接口"原则在硬件层面的可实现性

## 相关内容
- [[mosa-defense-acquisition]] — MOSA核心概念
- [[sosa-reference-architecture-v2]] — SOSA参考架构标准
- [[cmoss-overview-2022]] — CMOSS（共享VITA标准）
- [[modular-architecture-patterns]] — 模块化架构模式

---
*产品指南。展示了SOSA标准到实际COTS硬件产品的映射。*
