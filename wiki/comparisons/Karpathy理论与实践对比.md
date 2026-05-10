---
title: "Karpathy LLM Wiki原版 vs 我们的实现"
created: 2026-04-05
updated: 2026-04-20
type: comparison
tags: [wiki, karpathy, 架构, 对比]
sources: [gist:442a6bf555914893e9891c11519de94f]
confidence: INFERRED
evidence: "基于多源综合分析"
---

# Karpathy原版 vs 我们的实现

## 结构差异

| 方面 | Karpathy原版 | 我们的实现 | 状态 |
|------|-------------|-----------|------|
| **三层结构** | raw/（不可变）→ wiki/（LLM拥有）→ output（可交付物） | raw/ → wiki/ → output/ | ✅ 已对齐 |
| **raw/组织** | articles/、papers/、repos/、assets/ | articles/、papers/、assets/ | ✅ 已对齐 |
| **wiki/页面** | 概念、实体、对比、概述、综合、摘要 | concepts/、entities/、comparisons/、topics/、sources/ | ✅ 已对齐 |
| **Schema文件** | CLAUDE.md / AGENTS.md（顶层代理指令） | SCHEMA.md（项目根目录） | ✅ 已对齐 |
| **overview.md** | 单一综合叙事 | wiki/overview.md（5条故事线） | ✅ 已对齐 |
| **index.md** | 内容目录 | wiki/index.md（按类别组织） | ✅ 已对齐 |
| **log.md** | 仅追加日志 | wiki/log.md（可解析条目） | ✅ 已对齐 |
| **topics/** | 原版无此文件夹（综合在overview.md中） | 跨来源主题综合 | ➕ 我们扩展的 |
| **entities/** | 实体页面 | 实体页面 | ✅ 已对齐 |

## 操作对齐

| 操作 | Karpathy | 我们的SCHEMA.md | 状态 |
|------|----------|----------------|------|
| **Ingest** | 放入raw/，LLM处理，更新wiki页面、index、log | 含post-ingest checklist的6步流程 | ✅ |
| **Query** | 搜索wiki，综合，将好的答案归档回wiki页面 | 记录的相同流程 | ✅ |
| **Lint** | 矛盾、孤立、过期声明的健康检查 | 健康检查 + 模式发现 | ✅ |
| **Synthesize** | 累积后发现涌现模式 | 5+来源后触发，保存到comparisons/topics | ✅ |
| **用户参与** | "我更喜欢一次处理一个并保持参与" | "和宇飞讨论要点" | ✅ |
| **每次ingest页面数** | "每个来源10-15个wiki页面" | post-ingest checklist确保下游更新 | ✅ |

## 关键哲学观点（Karpathy）

1. **"wiki是持久的、复合的工件。"** — 交叉引用已存在，矛盾已标记，综合反映所有已读内容
2. **"你永远不要自己写wiki——LLM编写和维护全部"** — 用户提供来源，LLM做苦力
3. **"Obsidian是IDE；LLM是程序员；wiki是代码库"** — 开发隐喻
4. **"繁琐的部分不是阅读或思考——是簿记"** — LLM不会厌倦，不会忘记交叉引用

## 我们缺少的（来自Karpathy的提示）

- ✗ **Obsidian Web Clipper** — 浏览器扩展 → raw/
- ✗ **图片下载流程** — 附件到raw/assets/
- ✗ **Marp** — markdown转幻灯片格式
- ✗ **Dataview** — Obsidian插件，用于frontmatter查询
- ✗ **图形视图** — 可视化wiki连接
- ✗ **qmd** — 本地markdown搜索引擎（BM25 + 向量 + LLM重排序）

## 我们添加的（超越Karpathy）

- ✅ **post-ingest checklist** — 强制检查5个下游文件夹（Karpathy未明确）
- ✅ **topics/文件夹** — 跨来源主题综合（Karpathy的综合在overview.md中）
- ✅ **SCHEMA.md** — 中文版明确操作规范
- ✅ **YAML frontmatter** — 每个页面都有完整元数据
- ✅ **Gitee镜像** — 国内可达的git远程仓库

## 相关内容
- [[数字工程实践]]
- [[三本系统工程手册详细对比]]
- [[MOSA历史时间线]]

- [[概述]] — 知识库总览
