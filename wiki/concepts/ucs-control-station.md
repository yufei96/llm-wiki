---
title: "无人系统指挥控制标准接口（UCS）"
created: 2026-04-19
updated: 2026-04-19
type: concept
tags: [UCS, 无人系统, 指挥控制, STANAG 4586, NATO, 互操作]
sources: [raw/papers/stanag-4586-2nd-draft.pdf]
---

# 无人系统指挥控制标准接口（UCS）

## 定义

UCS（Unmanned Control Station）是一套为无人系统（UAV/UGV/UUV）指挥控制站定义的**开放架构标准接口**。由NATO通过STANAG 4586标准化，目标是实现不同国家、不同厂商的无人系统之间的**互操作性**。

## 核心目标

- **互操作性**：不同国家的无人机系统可在同一控制站操作，或由一个控制站指挥多国无人资产
- **即插即用**：新无人机型号通过适配UCS接口即可接入现有指控体系
- **避免供应商锁定**：控制站与无人机平台解耦，不绑定单一供应商
- **降低集成成本**：标准化接口取代每个项目各自开发集成方案

## 架构分层（STANAG 4586五级互操作性）

| 级别 | 描述 |
|------|------|
| LOI 1 | 间接接收无人机数据（如态势图） |
| LOI 2 | 直接接收无人机传感器数据 |
| LOI 3 | 控制无人机载荷（传感器、武器） |
| LOI 4 | 控制无人机飞行和起飞/降落 |
| LOI 5 | 完全遥控驾驶无人机 |

## 与MOSA生态的关系

UCS是MOSA在**无人系统指控领域**的落地标准，与以下标准互补：

- **[[open-mission-systems]]**（OMS）— 航空任务系统接口，UCS可建立在OMS之上
- **[[sosa-reference-architecture-v2]]** — 传感器开放架构，UCS可集成SOSA兼容的传感器
- **[[victory-ground-vehicle]]** — 地面车辆C4ISR互操作，与UCS在UGV领域重叠
- **CMOSS** — C5ISR/EW模块化标准，UCS机载指控台可采用CMOSS背板

## MOSA战略意义

UCS代表了MOSA在**多国协作**层面的落地。STANAG是NATO盟军标准化协议，通过UCS：
- 美国和盟国的无人资产可在联合行动中互操作
- 减少盟国对特定美国厂商的依赖
- 支持多国联合的无人系统快速部署

## 相关内容

- [[mosa-defense-acquisition]]
- [[mosa-five-pillars]]
- [[adaptive-acquisition-framework]]
- [[open-mission-systems]]
- [[stanag-4586-ucs]]
