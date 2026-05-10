---
title: "PNT政府参考架构 / 弹性嵌入式GPS/INS（R-EGI）"
created: 2026-05-06
updated: 2026-05-06
type: concept
level: 设备级
tags: [R-EGI, PNT, GPS, INS, MOSA, GRA, AFLCMC, 导航, 弹性, GPS拒止, 开放架构]
sources:
  - raw/articles/insidegnss-r-egi-milestone-2024.md
  - raw/articles/dvids-r-egi-pnt-flight-2024.md
  - raw/articles/is4s-r-egi-c12j-flight.md
  - raw/articles/rntfnd-r-egi-mosa-2024.md
confidence: EXTRACTED
evidence: "基于原始文档综合"
---

# PNT政府参考架构 / 弹性嵌入式GPS/INS（R-EGI）

## 摘要

R-EGI（Resilient-Embedded GPS/INS，弹性嵌入式GPS/INS）是美国空军生命周期管理中心电子系统局（AFLCMC/WNX）主导的政府拥有的PNT开放架构。R-EGI旨在为国防部平台提供在GPS拒止/降级环境中仍能可靠运行的定位、导航与授时（PNT）能力，是PNT领域政府参考架构（PNT GRA）的核心实现。该架构采用模块化开放系统架构（MOSA），支持即插即用的第三方PNT传感器集成，标志着国防部PNT体系从传统封闭系统向开放、可快速升级架构的范式转变。

## 核心目标

1. **弹性PNT**：在GPS信号被拒止、干扰或降级的环境中，仍能提供精确的定位、导航和授时能力
2. **政府拥有架构**：政府而非承包商掌握架构定义权，防止供应商锁定，促进竞争性采办
3. **模块化与可扩展**：通过MOSA实现传感器和算法的快速集成与升级，无需大规模系统重构
4. **跨平台适用**：设计支持多种平台和外形规格，实现PNT能力的广泛部署
5. **快速能力插入**：缩短新型PNT传感器从开发到部署的周期，支持8个月内完成原型到飞行验证

## 核心特点

### 架构设计

- **分层设计**：将安全关键功能（Safety Critical）与任务关键功能（Mission Critical）分离
- **Open VPX系统管理**：符合VITA 46.11标准的硬件管理
- **模型化系统工程（MBSE）**：确保接口一致性与复用性
- **安全关键软件**：按RTCA/DO-178B/C和MIL-STD-882E标准开发
- **开放软件环境**：支持第三方应用和互补PNT源（相机、LiDAR、雷达等）

### 硬件架构

R-EGI的快速原型飞行LRU包含以下核心硬件模块：

| 模块 | 供应商 | 功能 |
|------|--------|------|
| **大型F-16 LRU改装机箱** | GD-Mission Systems | 物理载体 |
| **安全关键导航（SCNAV）子系统** | Kearfott | 安全关键PNT、姿态和宿主接口 |
| **惯性测量单元（IMU）** | Kearfott | 高性能环形激光陀螺仪 |
| **GNSS接收机（GNSSR）** | Collins Aerospace | M-Code GPS接收机+Galileo开放服务夹层 |
| **任务能力导航（MCNAV）子系统** | GD-MS/IS4S | 通过pntOS和ASPN23消息实现弹性PNT |
| **Trimble Force 28M GPS M-Code接收机** | Trimble | 第三方即插即用集成验证 |

### 飞行验证里程碑

**2024年8月-10月（Holloman AFB）**：
- 三次核心飞行测试（8月20-22日）+ 一次补充飞行测试（10月）
- C-12J测试飞机搭载改装F-16 LRU
- 验证多种操作模式：混合M-Code GPS/IMU、仅GPS、仅IMU、MCNAV
- **<8个月**从团队组建到首飞的快速原型开发

**2025年2月（Centennial Airport, CO）**：
- 与AEVEX Aerospace和Northrop Grumman联合演示
- R-EGI成功集成AEVEX LynxVBN视觉导航系统
- 在模拟GPS拒止环境中仅使用视觉导航数据和IMU维持定位精度
- 验证"即插即用"功能和Alternative PNT消息标准合规性
- Trimble Force 28M接收机在**4周内**完成集成，展示架构灵活性

### 设计代理模式

R-EGI创新性地采用"设计代理"（Design Agent）模式：
- **IS4S**：总设计代理，负责架构设计与系统集成
- **Kearfott**：IMU和安全关键导航子系统
- **GD-Mission Systems**：LRU硬件和MCNAV子系统
- **Collins Aerospace**：GNSS接收机
- **746th/586th测试中队**：飞行测试支持

### 软件架构

- **pntOS**：政府拥有的PNT操作系统，提供开放软件环境
- **ASPN23消息**：Assured PNT System Network标准化消息格式
- 支持互补PNT源的模块化插件架构

## 与其他标准的关系

### 在开放架构层次体系中的位置

R-EGI位于[[开放架构层级|开放架构四层体系]]的**第3层：设备级**，是PNT GRA的核心实现。

### 纵向关系

```
OMS（平台级）─────可集成─────→ R-EGI PNT服务
ABMS GRA（平台级）──使用──→ R-EGI提供PNT数据
R-EGI（设备级）──运行在──→ SOSA H/W兼容硬件
R-EGI（设备级）──即插即用──→ 第三方PNT传感器
```

### 横向互补

- **R-EGI ↔ AMS GRA**：PNT能力集成到任务套件
- **R-EGI ↔ A-GRA**：自主系统依赖弹性PNT
- **R-EGI ↔ COARPS**：雷达辅助PNT（地形匹配等）
- **R-EGI ↔ CMOSS/VICTORY**：地面车辆PNT集成

### 与MOSA的关系

R-EGI是[[MOSA与国防采办|MOSA原则]]在PNT领域的典型实现：
- **模块化设计**：PNT传感器可独立替换
- **指定接口**：ASPN23消息标准化
- **开放标准**：Open VPX、VITA 46.11
- **政府拥有**：架构定义权归政府
- **快速竞争**：第三方传感器即插即用

### 与政府参考架构体系的关系

R-EGI是[[政府参考架构|GRA体系]]在PNT领域的具体体现，与以下GRA互补：
- [[开放任务系统|OMS]] — 任务系统总线集成
- [[SOSA传感器开放系统架构|SOSA]] — 传感器硬件标准化

## 参考来源

- [[InsideGNSS-R-EGI里程碑2024]] — Inside GNSS报道：R-EGI关键里程碑
- [[DVIDS-R-EGI导航飞行测试2024]] — DVIDS报道：R-EGI与EGI-M飞行演示
- [[IS4S-R-EGI C12J飞行测试]] — IS4S报道：C-12J飞行测试详情
- [[RNTFND R-EGI导航系统2024]] — Resilient PNT基金会：R-EGI MOSA分析

## 笔记

- R-EGI的核心创新是"政府拥有架构+设计代理模式"——政府掌握接口定义，多个供应商在架构框架内竞争
- **<8个月**从团队组建到首飞的速度在国防采办中极为罕见，体现了MOSA架构的快速集成优势
- AEVEX LynxVBN的即插即用集成是MOSA理念的标志性验证——第三方视觉导航传感器无需修改即可接入
- Trimble接收机**4周内**完成集成，进一步证明了开放架构的灵活性
- pntOS作为政府拥有的PNT操作系统，类似于OMS作为任务系统的抽象服务总线——都是MOSA在各自领域的核心软件层
- R-EGI同时服务于**安全关键**和**任务关键**两个功能域，分层设计是架构安全性的基础
- 设计代理模式（IS4S为总代理，多家供应商提供子系统）是政府参考架构采办模式的创新实践
- 2025年计划包括：Q1互补PNT飞行演示、Q2 NAVFEST25高级接收机/天线演示、Q4功能鉴定测试
- R-EGI与Northrop Grumman的EGI-M在同一飞行测试框架中并行演示，表明空军采取双轨策略确保PNT弹性

---

