# LLM Wiki Schema

## 概述
持久的、结构化的、相互链接的Markdown知识库，由LLM增量维护。不是RAG——知识编译一次后保持最新，随时间积累。

## 架构（Karpathy, 2025）
三层结构：

| 层 | 角色 | 规则 |
|----|------|------|
| **raw/** | 不可变的源文档（文章、论文、图像、数据） | LLM只读，永不写入。真实来源。 |
| **wiki/** | LLM生成的Markdown页面（摘要、概念、实体、对比） | LLM完全拥有此层。只读。 |
| **output/** | 派生可交付物（Marp幻灯片、图表、报告） | 从wiki生成，可归档回wiki。 |

## 目录结构
```
wiki-project/
├── raw/                      # 不可变的源文档
│   ├── articles/
│   ├── papers/
│   ├── assets/               # 下载的图像、附件
│   └── repos/
├── wiki/                     # LLM拥有的wiki层
│   ├── SCHEMA.md             # 本文件 — 约定和工作流程
│   ├── index.md              # 内容目录（所有页面，按类别）
│   ├── log.md                # 按时间顺序、仅追加的活动日志
│   ├── concepts/             # 主题/概念页面
│   ├── entities/             # 实体页面（人物、组织、产品）
│   ├── comparisons/          # 对比和综合页面
│   └── sources/              # 原始文档的摘要/索引
└── output/                   # 派生可交付物
    ├── slides/
    ├── charts/
    └── reports/
```

## 语言约定

- **内容语言**：所有wiki页面正文使用**简体中文**
- **保留原文**：文件名保持英文，代码块保留原文，关键英文缩写（MOSA、DoDI、AAF等）保留不翻译
- **Source页摘要**：即使原文是英文，摘要用中文撰写

## 命名约定

- **文件名**：kebab-case，如 `mosa-defense-acquisition`、`vendor-lock-in`
- **标题**：使用简体中文标题，英文缩写保留（如"模块化开放系统方法（MOSA）"）
- **YAML frontmatter**在每个wiki页面上：`created`、`updated`、`tags`、`source`

## 页面格式

```markdown
---
title: "页面标题"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [标签1, 标签2]
source: [raw/源文件.md]
---

# [标题]

## 摘要
一段概述。

## 要点
- ...

## 相关内容
- [[相关页面-1]]
- [[相关页面-2]]

## 笔记
自由格式的笔记、矛盾、注意事项。
```

## 操作

### 摄取（Ingest）

将新来源放入 `raw/`，告诉LLM处理它：

1. 阅读来源，与用户讨论关键要点
2. 在 `wiki/sources/` 写一个摘要页面（含完整YAML frontmatter）
3. 在 `wiki/concepts/` 创建/更新概念页面（新概念若被3+处引用则建独立页）
4. 在 `wiki/entities/` 创建/更新实体页面
5. **补双向交叉引用**：source页加`## 相关内容`链接相关concept，concept页加对应source链接
6. 更新 `wiki/index.md`（内容目录）
7. 追加条目到 `wiki/log.md`：`## [YYYY-MM-DD] ingest | 来源标题`
8. **验证完整性**：跑一次wikilink断链检查，确保新增链接目标存在

一个来源可能涉及10-15个wiki页面。保持参与——阅读摘要并指导重点。

### 查询（Query）

针对wiki提问：

1. 阅读 `wiki/index.md` 找到相关页面
2. 详细阅读相关页面
3. 综合答案并引用来源
4. 如果查询产生有价值的分析（对比、连接），保存为 `wiki/comparisons/` 或 `wiki/synthesis/` 中的新页面

好的答案应该归档回wiki作为新页面——探索像摄取的来源一样复合增长。

### 检查（Lint）

定期审查wiki的健康状况和涌现结构：

**健康检查：**

1. 阅读 `wiki/log.md` 获取上次检查时间戳
2. 扫描所有wiki页面：
   - 页面之间的矛盾
   - 被新来源取代的过时声明
   - 没有入站链接的孤立页面
   - 缺失的交叉引用
3. 运行wikilink完整性检查（所有 `[[page]]` 目标存在）

**模式发现（综合）：**

4. 累积5+新来源后，整体审查语料库：
   - 跨来源出现但没有单一页面捕捉的模式？
   - 标准/政策/概念之间存在什么连接？
   - 概念正在如何演化（政策版本、范围扩展）？
   - 材料中存在什么张力或矛盾？
5. 将涌现洞察保存为 `wiki/comparisons/` 或 `wiki/topics/` 中的新页面
6. 报告发现并建议新问题进行调查

这是Zettelkasten的"涌现结构"步骤——知识不是计划的，当累积密度达到阈值时浮现。

## 索引和日志

**index.md** — 面向内容的目录。每个wiki页面列出链接、一行摘要和类别。按类型组织（实体、概念、来源等）。每次摄取时更新。在中等规模（~100个来源，~数百个页面）下，这比嵌入式RAG效果更好。

**log.md** — 按时间顺序、仅追加的记录。每个条目：`## [YYYY-MM-DD] 操作 | 标题`。可用Unix工具解析：`grep "^## \\[" wiki/log.md | tail -5`。

## 输出格式

查询答案可以采用不同形式，全部归档回wiki：
- **Markdown页面**（默认） — 用于概念、实体、笔记
- **对比表格** — 用于并排分析
- **Marp幻灯片** — 用于演示（基于markdown）
- **Matplotlib图表** — 用于数据可视化

## 提示

- Obsidian是IDE；LLM是程序员；wiki是代码库
- 下载图像到 `raw/assets/` 以便LLM直接查看
- Obsidian图形视图显示wiki形状——连接、中心、孤立
- wiki只是一个git仓库——版本历史、分支、协作
- 值得调查的好问题与答案一样有价值

## 危险信号

- 摄取后不更新 `index.md`
- 摄取后不追加到 `log.md`
- LLM修改源文件（raw应不可变）
- 查询结果在聊天后丢弃而不是保存为wiki页面
- 页面之间的矛盾未标记
- 孤立页面增长未审查
