---
title: "PEO Aviation MOSA Transformation Office Industry Day 2022"
created: 2026-04-19
updated: 2026-04-29
type: source
sources: [raw/papers/PEO_Aviation_MOSA_TO_Industry_Days_2022.pdf, raw/articles/PEO_Aviation_MOSA_TO_Industry_Days_2022.md]
author: "Matt Sipe (MOSA Director), Scott Dennis (Chief Technical Architect), Wren Keith, Jesse Givens, Mark Chess, Jeff Belanger, Greg Bordelon, Mark Hasemeyer"
tags: [PEO Aviation, MOSA实施, 陆军航空, 行业合作, 企业架构, CSM, EAF, MOSA一致性]
confidence: EXTRACTED
evidence: "直接从原始文档提取"
---

# PEO Aviation MOSA Transformation Office Industry Day 2022

## 摘要

2022年9月12日PEO Aviation MOSA转型办公室举办的行业日活动，包含多位演讲者的完整幻灯片集。涵盖MOSA 9条工作线、企业架构框架（EAF）、企业产品架构（EPA）、组件规格模型（CSM）、MOSA一致性能力（MCC）等核心主题。这是PEO Aviation——陆军最大MOSA实施推动者的全面技术与业务战略展示。

## 要点

### MOSA 9条工作线（Lines of Effort）
PEO Aviation将MOSA实施分解为9条具体工作线：
1. **治理与政策（G&P）** — MOSA实施指南V2、OSCE（"Army gold standard"）
2. **架构与标准（A&S）** — 企业架构产品、标准应用与成熟化
3. **软件开发（SWD）** — FACE技术标准实施、软件复用目录、DevSecOps
4. **MOSA一致性能力（MCC）** — FACE一致性等级、一致性计划与验证
5. **协作数字环境（CDE）** — 利用更多行业标准工具
6. **合同策略** — 减少单一来源主合同依赖、模块级采购
7. **可负担性/资金/节约（AFS）** — BCA要求、约束PM独特投资
8. **资质与材料发布（QMR）** — IMA流程应用于AMCE
9. **战略沟通** — ACWG/VLC、CRADA、论文/技术论坛、社交媒体

### VLC与ACWG协作
- VLC（虚拟联盟委员会）：成员资格管理、行业影响力渠道
- ACWG（架构协作工作组）：行业公司+USG共同参与
- CRADA任务：航空企业架构产品、MOSA一致性、持续机队桥接策略、FACE一致性测试套件、FMS/国际MOSA策略

### 企业架构框架（EAF）
- 基于ISO 42020的一致性计划
- UAF（统一架构框架）核心结构
- 企业级模型框架 + 支持赋能环境 + MOSA EA治理/管理流程
- 引用Conway定律：松耦合组织产生更模块化的产品
- 使用Cameo Enterprise Architecture 2021x + Teamwork Cloud (TWC)

### 企业产品架构（EPA）
- PLE（产品线工程）：单一模型覆盖武器系统舰队
- 配置变体（CV）+ 特性（Features）+ 变化点（Variation Points）
- SAS（共享资产超集，150%模型）→ PAI（产品资产实例，100%模型）
- 基于FAF v4开发，已成功用于UAS系统族架构模型

### 组件规格模型（CSM）
- CSM是未来采办的基础要素
- 由IPT领导，各PM主导的航空企业产品开发
- 通过ACWG执行行业审查
- 主要挑战：FAF元素选择困难、信息分散、缺乏正式培训、指南不足以覆盖所有视图
- CSM开发者反馈：模板从FAF 3.0到4.0显著变化，MAESTRO指南修订频繁

### MOSA一致性能力（MCC）
- 测量系统的模块化和开放性程度
- PM为中心的评估：法律、法规、政策评估
- 供应商为中心的评估：模型验证、软硬件一致性、迭代评估
- MOSA一致性计划（MCP）：PM记录其定制的MOSA方案及度量方法
- 评估内容：OSMP、MOSA用例、标准一致性、独立第三方评估

### 五大MOSA目标
1. 提升可负担性（Improved affordability）
2. 增加战备状态（Increased readiness）
3. 增强能力（Enhanced capability）
4. 减少进度压力（Reduced schedule pressure）
5. 降低供应链风险（Reduced supply chain risk）

### MSC优先事项
- **AMCE**（航空任务计算环境）— 模块化/可配置处理、开放式软件环境
- **CDC**（通信/数据链/控制）— 与PEO C3T和CMOSS协同、卡基解决方案
- **SCI**（先进编队/无人车辆控制）— S&T先进编队协同
- **EPS**（电力系统）— 储能→电力转换→发电机
- **DVE**（退化视觉环境）— FLRAA/FARA/CH机会

### 电力系统（EPS）CSM
- Tier 2陆军航空现代化优先事项和企业MSC
- 解决功率/热管理、发电、电池、APU/SPU、电力转换
- CSM v1.0（2022.4）→ v1.1（2023.1）：增加接口需求和数据模型

### AMCE架构
- 可配置/模块化硬件+软件元素，基于通用CSM
- 主要组件：可配置硬件（CMOSS一致性架构）、软件操作环境（FACE 3.1一致性）、软件加载（ARINC 615A-3/665-5）
- AMCE CSM 2.0.1：与FAF 4.0对齐
- 开放系统接口库（1.0）：FACE 3.1一致性数据建模接口

### 通信/数据链/控制
- 模块化通信：多个LRU设备收敛为开放标准模块化环境中的无线电卡
- 与CMFF A-CDD模块化通信努力对齐
- 路线图：Enduring（FY25）→ FVL（FY25-29）→ Future（FY27-30+）
- 通信机箱CSM v1（2022.7）→ v2（2022.12）

## 对MOSA的意义

PEO Aviation是**陆军最大的MOSA实施推动者**。这份文件展示了：
- MOSA从政策要求到**可执行工作线**的转化
- 9条LoE提供了MOSA实施的**结构化检查清单**
- EAF/EPA框架提供了企业级MOSA治理的实际模式
- CSM开发暴露了MBSE实践中的关键挑战（指南不充分、培训缺失、模板频繁变化）
- MCC提供了MOSA一致性评估的初步框架

对于任何试图在实际项目中落地MOSA的团队，这份文件是最直接的实践指南。

## 相关内容
- [[航空PEO-MOSA实施指南]] — PEO Aviation MOSA实施指南
- [[航空PEO-FACE-TIM开放系统演示2021]] — PEO Aviation FACE TIM 2021开放系统演示
- [[MOSA与国防采办]] — MOSA核心概念
- [[MOSA五支柱]] — MOSA五大支柱
- [[FACE技术标准]] — FACE技术标准
- [[自适应采办框架]] — 自适应采办框架
- [[C5ISR标准融合]] — C5ISR标准趋同
- [[宿主硬件开放系统]] — HOST硬件开放系统

---
*79页幻灯片，8位演讲者。MOSA从政策到实践的最佳案例研究。*
