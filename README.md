# LLM Wiki

持久的、结构化的知识库——由AI助手从摄取的文档（论文、政策文件、标准、文章）自动生成和维护。

与RAG不同：知识被编译成带有交叉引用的结构化wiki页面，因此每次查询都能从所有先前积累的上下文中受益。

## 架构

```
┌─────────────────────────────────────────────────────┐
│  raw/          ← 不可变的源文档                      │
│    papers/      → 原始PDF文件                       │
│    articles/    → PDF文本提取 + 网页抓取的markdown   │
│                                                     │
│  wiki/         ← LLM生成的结构化页面                │
│    overview.md  → 知识库总览（"我现在知道什么"）      │
│    index.md     → 内容目录                          │
│    log.md       → 活动时间线                        │
│    sources/     → 已摄取来源的摘要                  │
│    concepts/    → 概念定义与关系                    │
│    entities/    → 人物、组织、项目                  │
│    comparisons/ → 跨来源对比分析                    │
│    topics/      → 跨来源主题综合                    │
│                                                     │
│  output/       ← 交付工件                           │
│                                                     │
│  SCHEMA.md     ← 结构规则与约定                     │
└─────────────────────────────────────────────────────┘
```

## 工作流程

1. **摄取**：放入文档（PDF、文章、笔记）→ AI提取关键信息 → 创建/更新wiki页面
2. **查询**：向AI询问任何主题 → 它搜索wiki并从积累的知识中综合答案
3. **检查**：检查结构一致性（断开的链接、缺失的引用、孤立页面）

## 设计

基于[Karpathy的LLM Wiki模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)。

### 关键原则

- **来源不可变** — 一旦摄取，原始文件永不更改
- **Wiki页面是活的** — 随着新来源添加或矛盾信息而更新
- **交叉引用链接一切** — `[[wikilinks]]`连接概念、实体和来源
- **Git跟踪所有更改** — 完整的编辑历史，无信息丢失
- **推送到Gitee → GitHub镜像** 用于其他机器上的Obsidian同步

## 当前焦点：MOSA与开放系统架构

这个wiki从MOSA研究开始——国防部的一种采办策略，用于国防系统的模块化架构和开放接口。现已扩展到数字工程、系统工程手册、无人作战飞机、开放架构层次体系、中国智能网联汽车与无人机开放生态等领域。

### 核心知识网络

#### 开放架构层次体系（21种实现）

知识库的核心组织框架——美国国防部21种开放系统架构实现按四层结构组织（[[open-architecture-hierarchy]]）：

- **平台级**：OMS/UCI、UCS/STANAG 4586、ABMS GRA
- **分系统级**：WOSA、DEWS MOSA RA、NC3 GRA、Sentinel GRA、CFW ICD
- **设备级**：SOSA、MORA、CMOSS、VICTORY、AMS GRA、A-GRA、R-EGI、COARPS、SCARS
- **部组件级**：FACE、HOST

MOSA已从航空扩展到核力量、PNT、雷达、训练、自主等6+个领域。

#### MOSA发展历程（1994-2025）

30年演化四阶段（[[mosa-history-timeline]]）：

- **萌芽期（1994-2005）**：OSJTF宪章签署 → DoD IG审计 → MOSA写入DoDI 5000.2
- **政策推动期（2005-2017）**：OSA合同指南五原则 → BBP 3.0 → NDAA Section 805法定化
- **法定化期（2017-2020）**：三军部长备忘录（2019）→ NDAA Section 840 → SOSA标准发布
- **深度实施期（2020-至今）**：三军联合备忘录（2024）→ MOSA实施指南（2025）→ GAO专项审查

#### 柔性武器设计方法

符合WOSA要求的模块化武器设计（[[flexible-weapons-design-methodology]]）：

- **AFRL（2014）**：提出柔性武器概念——模块化"即插即用"、开放架构、UAI接口
- **Purdue大学（2015）**：论证五个关键架构因素（毁伤机制、引信、重量、制导、推进）
- **Raytheon（2024）**：可组合武器架构——标准化九类子系统组件

#### 数字工程生态系统
- **NASA数字工程三层体系**：HDBK-1004（采办框架）、HDBK-1009A（系统建模）、HDBK-7009A（M&S质量）
- **AFMC数字化物资管理（DMM）**：六大支柱框架，GRA体系将79个MIL文档转化为36个系统模型
- **MBSE/SysML v2**：OUSD RE过渡指导（FY2025试点→FY2028强制）

#### 协作作战飞机（CCA）
- DAF计划生产至少1000架CCA，2028年首次列装
- "架构三件套"：AMS GRA + A-GRA + OMS
- 多供应商竞争：Collins Aerospace vs Shield AI（自主），GA-ASI vs Anduril（平台）

#### 中国智能网联汽车与无人机开放生态
- **车路云一体化**（[[china-vehicle-road-cloud-integration]]）：云平台架构、测试评价体系、跨行业联合标准
- **华为车辆开放生态**（[[huawei-vehicle-open-ecosystem]]）：鸿蒙智行、iDVP数字底座、Car Kit开放API
- **大疆开放无人机架构**（[[dji-open-drone-architecture]]）：MSDK/PSDK/OSDK/Edge SDK/Cloud API五层开放体系

#### 概念（39个）
- **核心概念**：MOSA、供应商锁定、自适应采办框架（AAF）、模块化架构模式
- **技术标准**：FACE、OMS、UCS、SOSA、MORA、WOSA、HOST、CMOSS、VICTORY
- **GRA体系**：AMS GRA、A-GRA、ABMS GRA、NC3 GRA、Sentinel GRA、R-EGI、COARPS、SCARS、DEWS RA
- **数字工程**：MBSE、系统韧性工程、NASA DE实施体系
- **采办路径**：MTA、紧急能力采办

#### 实体（30个）
- **军事组织**：DoD、AFMC、AFLCMC、AFGSC、STRATCOM、NATO、PMA-209
- **行业联盟**：The Open Group、INCOSE、DSB
- **承包商**：Northrop Grumman、Lockheed Martin、CAE USA、General Atomics、Anduril、Shield AI、Collins Aerospace、IS4S
- **政策/监督**：GAO、OMB、OUSD RE、DAF SAB

#### 对比分析（20个）
- **架构层次**：开放架构四层体系、GRA生态演进
- **标准趋同**：C5ISR标准趋同、接口工程三层演进
- **政策张力**：速度vs模块化、赛博安全vs开放接口
- **中美对比**：中美开放架构十维对比
- **项目对比**：SiAW vs AARGM-ER、MOSA实施状态矩阵（20项目）

#### 来源（116个）
- **法律/政策**：NDAA（2017-2021）、DoDI 5000系列、DFARS、三军备忘录（2019/2024）
- **标准/架构**：FACE 3.2、SOSA、OMS、WOSA、MORA、CMOSS
- **评估/审计**：GAO武器系统年度评估、MOSA专项审查、DoD IG审计（2000）
- **学术/研究**：Purdue柔性武器论文、GWU MOSA博士论文、DSP Journal专刊
- **MOSA起源**：OSJTF宪章（1994）、DoD IG审计（2000）、DSP Journal（2001）

### 关键洞察

#### 1. GRA生态的层次化
GRA从零散标准发展为四层架构体系。不同GRA定位在不同层次，存在明确的纵向依赖和横向互补关系。

#### 2. MOSA的领域扩张
MOSA从航空（OMS/FACE）扩展到核（NC3/Sentinel）、PNT（R-EGI）、雷达（COARPS）、训练（SCARS）、自主（A-GRA）。每次扩张遵循相同模式：政府定义参考架构 → 行业在框架内竞争 → 即插即用验证。

#### 3. CCA催生新旧供应商竞争格局
传统巨头（Northrop Grumman、RTX Collins）与新兴企业（Anduril、Shield AI）在CCA同台竞技。A-GRA的架构设计使这种竞争成为可能。

#### 4. MOSA评估差距
没有标准化的MOSA合规性或ROI指标。FACE是唯一具有实际一致性测试过程的标准。

#### 5. NASA构建了全球最完整的数字工程三层体系
对比DoD：DoDI 5000.97定义九大要素（政策层），但缺少可操作的实施手册。

#### 6. SysML v2 过渡是最大瓶颈
工具成熟度不足、培训缺口大、遗留模型转换成本高。

#### 7. 中国开放架构"做了但没说"
华为鸿蒙智行、大疆无人机、凌空天行驭空戟-1000等实践在工程层面已实现模块化开放架构，但缺乏类似MOSA的顶层政策框架和法律要求。

## 仓库结构

```
.
├── README.md          ← 本文件
├── SCHEMA.md          ← Wiki结构规则和约定
├── raw/               ← 不可变的源文档
│   ├── papers/        → 原始PDF（100个）
│   └── articles/      → PDF文本提取+网页抓取（150个）
├── wiki/              ← LLM生成的markdown页面（222个）
│   ├── overview.md    → 知识库总览
│   ├── index.md       → 内容目录
│   ├── log.md         → 活动时间线
│   ├── sources/       → 来源摘要（116个）
│   ├── concepts/      → 概念定义（39个）
│   ├── entities/      → 实体页面（30个）
│   ├── comparisons/   → 对比分析（20个）
│   └── topics/        → 主题综合（17个）
├── output/            ← 交付工件（导出文档）
├── LICENSE            ← CC BY-SA 4.0 许可证
└── .gitignore         ← 排除.git-credentials
```

## 同步

- **服务器 → Gitee**：直接 `git push`（本机）
- **Gitee → GitHub**：通过Gitee仓库镜像功能自动镜像
- **GitHub → 本地（Obsidian）**：从GitHub拉取用于Obsidian查看

## 使用方法

将文档（PDF、文章、笔记）发送给AI助手——它将自动摄取它们并更新wiki。

## 许可证

本知识库采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 许可证发布。

- ✅ 可以自由分享和改编
- ✅ 可以用于商业目的
- ⚠️ 必须注明出处
- ⚠️ 衍生作品必须采用相同许可证

原始来源文档（`raw/` 目录）可能受其各自的版权保护。美国政府作品（CRS报告、GAO报告、DoD出版物等）属于公共领域。

---

*赫妹🪽 维护 — 最后更新 2026-05-07*
