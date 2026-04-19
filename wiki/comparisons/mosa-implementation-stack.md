---
title: "MOSA实施全栈：从法律到合同执行"
created: 2026-04-19
updated: 2026-04-19
type: comparison
tags: [MOSA, 实施全栈, 法律, 政策, 标准, 合同, DID, 层级结构]
sources: [raw/papers/ppi-did-templates.pdf, raw/papers/osa-contract-guidebook-v1.1-rev1.pdf, raw/papers/mosa-implementation-guidebook-2025.pdf]
---

# MOSA实施全栈：从法律到合同执行

## 概述

MOSA的实施不是一个文件能覆盖的——它需要**五层架构**从法律要求逐级传递到具体的合同执行。每一层将上一层的原则转化为下一层可执行的具体条款。知识库现在覆盖了全部五层。

## 五层架构

### 第1层：法律（Congress）
**10 USC §4401-4403** — "To the maximum extent practicable, MDAP必须采用MOSA"

- 性质：强制性法律要求
- 受众：国防部所有采办项目
- 局限：模糊的"practicable"豁免条款
- 知识库页面：`[[2026-04-05-10usc-4401-4403-mosa-law]]`

### 第2层：政策（DoD）
**DoDI 5000.85 + BBP 3.0 + 2025 MOSA实施指南**

- 性质：DoD内部政策，将法律转化为操作要求
- 受众：项目管理办公室、里程碑决策当局
- 关键输出：MOSA五大支柱、采办路径适配要求
- 知识库页面：`[[better-buying-power-3-0]]`、`[[mosa-five-pillars]]`、`[[2026-04-05-dodi-5000-85-2020]]`

### 第3层：标准（行业/军种）
**FACE、OMS、CMOSS、SOSA、VICTORY、MORA**

- 性质：技术标准，规定"模块化"长什么样
- 受众：系统架构师、工程师
- 关键输出：接口规范、硬件平台标准、软件组件标准
- 知识库页面：`[[face-technical-standard]]`、`[[open-mission-systems]]`、`[[c5isr-standards-convergence]]`

### 第4层：合同模板（项目级）
**OSA合同指南v1.1 + PEO Aviation实施指南 + DFARS条款**

- 性质：合同条款模板，将MOSA写入可执行的合同要求
- 受众：合同经理、项目经理
- 关键输出：SOW中的MOSA任务、PWS中的接口要求、TEMP中的验证计划
- 知识库页面：`[[2026-04-19-osa-contract-guidebook-v1.1]]`、`[[2026-04-19-peo-aviation-mosa-impl-guide]]`

### 第5层：文档模板（交付级）
**PPI DID模板 — CONOPS/SEP/SOW/SSDD/SyRS**

- 性质：数据项描述模板，规定供应商必须交付什么格式的文档
- 受众：供应商工程师、文档编制人员
- 关键输出：接口定义文档、系统设计描述、需求规范
- 知识库页面：`[[2026-04-19-ppi-did-templates]]`

## 层间传递机制

```
法律(10 USC)
  ↓ "必须采用MOSA"
政策(DoDI/BBP/指南)
  ↓ "五大支柱、适配各路径"
标准(FACE/OMS/CMOSS)
  ↓ "用这些接口标准"
合同模板(SOW/PWS/TEMP)
  ↓ "供应商须交付X、Y、Z"
DID模板(CONOPS/SEP/SSDD)
  ↓ "文档须包含A、B、C章节"
供应商交付物
```

## 断裂点分析

当前知识库暴露的几个断裂：

1. **第2层→第3层断裂**：政策说"用开放标准"，但没有明确指定用哪个标准。军种各自选择（空军用OMS，陆军用VICTORY）。
2. **第3层→第4层断裂**：标准存在，但合同模板中如何引用标准没有统一做法。OSA合同指南（2013）太老了。
3. **第4层→第5层断裂**：合同模板规定了任务，但DID模板中的具体内容与MOSA要求的对应关系不清晰。

## 这个框架对知识库的意义

之前的分析页（五原则演化、标准趋同、国际化、速度张力）都是在某一层或跨层分析。**实施全栈是把这些分析组织在一起的框架**——任何MOSA问题都可以定位到具体层级。

## 相关内容

- [[mosa-defense-acquisition]] — MOSA核心概念
- [[mosa-five-pillars]] — 第2层核心文档
- [[c5isr-standards-convergence]] — 第3层标准趋同
- [[2026-04-19-osa-contract-guidebook-v1.1]] — 第4层合同指南
- [[2026-04-19-ppi-did-templates]] — 第5层DID模板
- [[2026-04-19-ppi-integrating-pm-se]] — PM-SE整合（层级间协调）
- [[speed-vs-modularity]] — 速度张力（第2层内部矛盾）
