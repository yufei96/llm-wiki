---
title: "Karpathy LLM Wiki原版 vs 我们的实现"
created: 2026-04-05
updated: 2026-04-20
type: comparison
tags: [wiki, karpathy, 架构, 对比]
sources: [gist:442a6bf555914893e9891c11519de94f]
---

# Karpathy原版 vs 我们的实现

## 结构差异

| 方面 | Karpathy原版 | 我们的实现 | 状态 |
|------|-------------|-----------|------|
| **三层结构** | raw/（不可变）→ wiki/（LLM拥有）→ output（可交付物） | raw/ → wiki/ → output/ | ✅ 已对齐 |
| **raw/组织** | articles/、papers/、repos/、assets/ | 平铺 + assets/ | ⚠️ 需要子目录 |
| **wiki/页面** | 概念、实体、对比、概述、综合、摘要 | concepts/、entities/、comparisons/、synthesis/、sources/ | ✅ 已对齐 |
| **Schema文件** | CLAUDE.md / AGENTS.md（顶层代理指令） | wiki/SCHEMA.md | ⚠️ 应在顶层 |
| **index.md** | 在wiki/根目录；按类别内容目录 | 在wiki/根目录；按类别组织 | ✅ 已对齐 |
| **log.md** | 在wiki/根目录；仅追加、可解析条目 | 在wiki/根目录；仅追加 | ✅ 已对齐 |
| **output/** | 未明确为文件夹；可交付物归档回wiki | 明确的output/目录 | ⚠️ 额外层级 |
| **Sources子文件夹** | sources在raw/，wiki有来源摘要 | wiki/sources/用于文档摘要 | ✅ 已对齐 |

## 操作对齐

| 操作 | Karpathy | 我们的SCHEMA.md |
|------|----------|----------------|
| **Ingest** | 放入raw/，LLM处理，更新wiki页面、index、log | 记录的相同3步流程 | ✅ |
| **Query** | 搜索wiki，综合，将好的答案归档回wiki页面 | 记录的相同流程 | ✅ |
| **Lint** | 矛盾、孤立、过期声明的健康检查 | 记录的相同清单 | ✅ |
| **用户参与** | "我更喜欢一次处理一个并保持参与" | "和宇飞讨论要点" | ✅ |
| **每次ingest页面数** | "每个来源10-15个wiki页面" | 预期相同范围 | ✅ |

## 关键哲学观点（Karpathy）

1. **"wiki是持久的、复合的工件。"** — 交叉引用已存在，矛盾已标记，综合反映所有已读内容
2. **"你永远不要自己写wiki——LLM编写和维护全部"** — 用户提供来源，LLM做苦力
3. **"Obsidian是IDE；LLM是程序员；wiki是代码库"** — 开发隐喻
4. **"繁琐的部分不是阅读或思考——是簿记"** — LLM不会厌倦，不会忘记交叉引用

## 我们缺少的（来自Karpathy的提示）

- ✗ **Obsidian Web Clipper** — 浏览器扩展 → raw/（宇飞可以用Obsidian桌面版）
- ✗ **图片下载流程** — 附件到raw/assets/
- ✗ **Marp** — markdown转幻灯片格式
- ✗ **Dataview** — Obsidian插件，用于frontmatter查询
- ✗ **图形视图** — 可视化wiki连接
- ✗ **qmd** — 本地markdown搜索引擎（BM25 + 向量 + LLM重排序）
- ✗ **CLI工具** — 用于LLM wiki操作的自定义工具

## 我们添加的（超越Karpathy）

- ✅ **YAML frontmatter**在每个页面上（Karpathy提到它是可选的，配合Dataview使用）
- ✅ **页面格式模板**，包含摘要/关键点/相关/笔记结构
- ✅ **Git版本控制**通过Gitee镜像 → GitHub（基础设施约束解决方案）
- ✅ **SCHEMA.md**作为明确的wiki指令文件（Karpathy使用CLAUDE.md / AGENTS.md）

---

*2026-04-05 初始结构审计时生成对比，2026-04-20 翻译成简体中文*
