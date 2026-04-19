---
title: "ARSENL — 空军架构标准与工程库"
date: 2026-04-19
type: source_summary
source: raw/papers/arsenl.pdf
author: "AFMC / AFLCMC"
tags: [ARSENL, MOSA标准, USAF, 标准库, 参考架构]
---

# ARSENL — 架构标准与工程库

## 文档概况
- **全称**：Architectures, Standards and Engineering Library (A.R.S.EN.L)
- **发布者**：Air Force Materiel Command (AFMC)
- **URL**：`https://www.vdl.afrl.af.mil/programs/arsenl/standards.php`
- **页数**：4（概览文档，实际标准库在线访问需VDL账号）
- **类型**：标准库索引

## 核心内容

ARSENL是AFMC建立的**USAF MOSA使能标准的官方索引**，包含政府参考架构、MOSA使能标准和系统接口信息。

### USAF认可的MOSA使能标准清单

ARSENL列出了USAF官方认可的MOSA标准：
1. **FACE Technical Standard** — 航电开放架构
2. **SOSA** — 传感器开放系统架构
3. **SCA (Software Communications Architecture)** — 软件定义无线电架构（JTNC发布）
4. **REDHAWK** — SDR框架，支持实时软件无线电应用开发部署
5. **CoPaIS (Common Payload Interface Standard)** — 标准化航天器总线-载荷接口

### 访问方式
- 公开标准：VDL公开页面可访问
- 分销限制/ITAR材料：需VDL账号+政府赞助人
- 流程：VDL注册 → 请求ARSENL项目访问 → 政府代表审批

## 对MOSA的意义

ARSENL是理解**USAF MOSA标准生态官方视图**的关键文档。它告诉我们USAF实际采用的标准组合：
- **FACE + SOSA** 作为两大支柱（与我们的分析一致）
- **SCA + REDHAWK** 补充了软件定义无线电领域（我们之前未覆盖）
- **CoPaIS** 补充了航天领域（我们之前未覆盖）

SCA和REDHAWK代表了MOSA在**通信/SDR领域**的延伸，CoPaIS代表了MOSA在**航天领域**的延伸。

## 相关内容
- [[face-technical-standard]] — FACE标准
- [[2026-04-19-sosa-reference-architecture-v2]] — SOSA
- [[mosa-defense-acquisition]] — MOSA概念
- [[2026-04-19-dsp-journal-mosa-2020]] — DSP Journal综述

---
*4页。USAF MOSA使能标准的官方清单，发现SCA/REDHAWK/CoPaIS三个新标准领域。*
