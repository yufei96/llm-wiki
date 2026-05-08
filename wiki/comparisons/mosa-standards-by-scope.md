---
title: "美军开放架构标准分类：三军共用 vs 军种内推广"
created: 2026-05-08
updated: 2026-05-08
type: comparison
tags: [开放架构, MOSA, OMS, UCI, SOSA, FACE, VICTORY, AMS, WOSA, GARA, R-EGI, COARPS, HOST, MORA, UAI, UCS]
sources:
  - wiki/comparisons/open-architecture-hierarchy.md
  - wiki/topics/mosa-lifecycle-application.md
---

# 美军开放架构标准分类：三军共用 vs 军种内推广

## 概述

美国国防部的开放系统架构存在两种互补的分类方式：
1. **四层结构**（[[open-architecture-hierarchy]]）：按架构层级（平台→分系统→设备→部组件）分类
2. **推广范围**（本页）：按标准适用范围（三军共用 vs 军种内推广）分类

三军共用标准以 **2024年12月三军联合备忘录确认的6大标准**为权威来源。

---

## 一、三军共用标准（6种）

2024年12月三军联合备忘录首次在最高政策层面明确列举的已验证开放标准。这是MOSA标准生态的权威清单。

| 标准 | 全称 | 定义域 | 主导方 |
|------|------|--------|--------|
| **OMS/UCI** | Open Systems/Universal C2 Interface | 通用指挥控制接口 | 跨军种 |
| **SOSA** | Sensor Open Systems Architecture | 传感器开放系统架构 | The Open Group |
| **FACE** | Future Airborne Capability Environment | 未来机载能力环境 | The Open Group |
| **VICTORY** | Vehicle Integration for C4ISR/EW | 车辆C4ISR/EW集成 | 行业联盟 |
| **AMS GRA** | Agile Mission Suite Government Reference Architecture | 敏捷任务套件 | 政府 |
| **WOSA** | Weapons Open System Architecture | 武器开放系统架构 | 跨军种 |

### 关键特征

- **2024年12月三军联合备忘录**权威确认
- **法定基础**：10 USC 4401 要求 MDAP 采用 MOSA 方法（非具体标准列表）
- **联合采办项目**直接采用这些标准

### 应用案例

| 标准 | 典型项目 |
|------|----------|
| OMS/UCI | F-35、B-21、CCA、NGAD |
| SOSA | 雷达传感器、EO/IR 系统 |
| FACE | 陆军航空电子（FLRAA、FARA） |
| VICTORY | 陆军地面车辆（XM-30、AMPV） |
| AMS GRA | NGAD 体系任务系统、CCA |
| WOSA | 武器分系统（SiAW、PrSM） |

---

## 二、军种内推广标准（16种）

由特定军种主导，在本军种内推广使用。

### 陆军主导

| 标准 | 全称 | 定义域 |
|------|------|--------|
| **GARA** | Government Avionics Reference Architecture | 政府航空电子参考架构 |
| **R-EGI** | Resilient Embedded GPS/INS | 弹性嵌入式GPS/惯性导航 |
| **VICTORY** | Vehicle Integration for C4ISR/EW | 车辆C4ISR/EW集成 |

### 海军主导

| 标准 | 全称 | 定义域 |
|------|------|--------|
| **Raging Crow** | — | 愤怒乌鸦电子战架构 |
| **Big Iron** | Electric Warfare Focused Standard | 大铁电子战标准 |
| **SPEAD** | Scalable Payload for EA Development | 电子攻击可扩展载荷 |
| **TOSA** | Tester Open System Architecture | 测试器开放系统架构 |
| **CoPaIS** | Common Payload Interface Standard | 通用载荷接口标准 |

### 空军主导

| 标准 | 全称 | 定义域 |
|------|------|--------|
| **COARPS** | Common Open Architecture Radar Program | 通用开放架构雷达计划 |
| **COBRA** | Common Open Backend Reference Architecture | 通用开放后端参考架构 |
| **HOST** | Hardware Open Systems Technology | 硬件开放系统技术 |
| **MI-COARPS** | Multi-Intelligence COARPS | 多情报通用开放架构雷达计划 |
| **MORA** | Modular Open RF Architecture | 模块化开放射频架构 |

### 跨军种但军种主导

| 标准 | 全称 | 定义域 | 主导方 |
|------|------|--------|--------|
| **UAI** | Universal Armament Interface | 通用武器接口 | 空军 |
| **UCS** | Unmanned Control System | 无人系统指控 | 跨军种 |

---

## 三、两种分类的交叉映射

| 四层结构 | 三军共用 | 军种内推广 |
|----------|----------|------------|
| **平台级** | OMS/UCI | ABMS GRA、UCS |
| **分系统级** | WOSA | COARPS、MI-COARPS、Raging Crow、Big Iron、SPEAD |
| **设备级** | SOSA、VICTORY、AMS GRA | MORA、HOST、R-EGI、GARA、COBRA、TOSA、CoPaIS |
| **部组件级** | FACE | — |

---

## 四、推广路径对比

### 三军共用标准的推广路径

```
军种主导开发 → 联合确认（三军备忘录）→ 法定要求（NDAA）→ 全军强制
```

**案例**：
- OMS/UCI：空军开发 → 2024年三军备忘录确认 → 10 USC 4401 要求
- FACE：陆军开发 → 2024年三军备忘录确认 → 全军航空电子标准

### 军种内推广标准的推广路径

```
军种实验室 → 军种采办项目验证 → 军种内标准化 → 可能扩展到其他军种
```

**案例**：
- COARPS：空军实验室 → RFI 征集 → 空军雷达项目采用
- R-EGI：陆军/空军联合 → DVIDS 飞行测试验证 → 军种内推广

---

## 五、关键洞察

1. **三军共用标准更"硬"**：有法定要求和联合备忘录背书，MDAP 必须采用

2. **军种内推广标准更"灵活"**：军种可根据需求定制，但跨军种采用需额外协调

3. **OMS/UCI 是核心枢纽**：作为平台级标准，连接 FACE/SOSA/WOSA 等设备/分系统级标准

4. **陆军最积极**：FACE、VICTORY、GARA、R-EGI 均由陆军主导或深度参与

5. **海军标准最分散**：Raging Crow、Big Iron、SPEAD、TOSA、CoPaIS 等电子战/测试标准各自独立

6. **空军主导雷达/武器域**：COARPS、MI-COARPS、MORA、HOST、UAI 均为空军主导

---

## 六、与 MOSA 五大支柱的关系

| 支柱 | 三军共用标准（6种） | 军种内推广标准 |
|------|-------------------|---------------|
| **建立支持环境** | OMS/UCI、FACE | HOST、COBRA |
| **模块化分解** | SOSA、WOSA | COARPS、MORA |
| **开放接口** | VICTORY、AMS GRA | UAI、UCS、CoPaIS |
| **竞争性采办** | 所有三军共用标准 | 军种内竞争 |
| **数据与IP管理** | FACE（唯一具有一致性测试） | 军种自定义 |

---

## 相关内容

- [[open-architecture-hierarchy]] — 四层结构分类（21种实现）
- [[six-validated-mosa-standards]] — 6大已验证MOSA标准（三军备忘录确认）
- [[mosaic-modular-open-systems-approach]] — MOSA总体方法论
- [[mosa-lifecycle-application]] — 全寿命周期MOSA应用分析
- [[tri-service-memo-2024]] — 2024年12月三军联合备忘录

---

*基于用户提供的分类信息整理，与现有四层结构分类互补。2026-05-08 创建。*
