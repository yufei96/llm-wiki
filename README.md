# MOSA 知识库

**Modular Open Systems Approach (MOSA) 与数字工程知识库**

国防开放系统架构、智能网联汽车、军事开放标准的中文知识库。涵盖 MOSA、GRA、FACE、SOSA、CMOSS、WOSA、OMS 等标准体系。

📊 当前规模：**266 篇知识页面** · **255 篇原始文档** · **23,000+ 行内容** · **1,800+ 交叉引用**

## 快速开始

### 🌐 在线浏览

**[wiki.05132024.xyz](https://wiki.05132024.xyz)**

由 Cloudflare Pages 构建部署，支持全文搜索和标签导航。

### 📥 下载使用

```bash
git clone https://gitee.com/yufei96/llm-wiki.git
cd llm-wiki
```

#### 方式 1：Obsidian 本地浏览

用 [Obsidian](https://obsidian.md) 打开仓库目录，`[[wikilinks]]` 自动生效，适合深度研究和内容贡献。

#### 方式 2：导入 IMA / NotebookLM

克隆后在 [IMA Copilot](https://ima.qq.com) 或 [NotebookLM](https://notebooklm.google.com) 中导入 `wiki/` 目录，自动生成知识图谱和问答。

#### 方式 3：Agent 交互

```text
"MOSA 的五原则是什么"
"对比 FACE 和 SOSA 标准"
"总结 DOTE 2025 报告中 LTAMDS 的测试结果"
```

## 构建部署

```bash
make check      # 健康检查（YAML 校验 + 死链/孤儿页检测）
make build      # 构建站点（同上 + MkDocs 构建）
make graph      # 生成知识图谱
make all        # check + build + graph
make deploy     # 全部 + 部署到 Cloudflare Pages
make serve      # 本地预览 http://localhost:8000
make clean      # 清理构建产物
```

构建流程：

```
check-yaml.py → site_builder.py（索引生成 → wikilink 转换
  → 健康检查 → nav 自动生成 → mkdocs 构建）→ deploy
```

## 仓库结构

```
llm-wiki/
├── wiki/                    # 知识库主体（Markdown + Mermaid 图表）
│   ├── concepts/           # 概念定义——"这是什么"（SOSA、GRA、ACE 等）
│   ├── topics/             # 主题分析——"这个领域怎么样"（趋势、实施、对比）
│   ├── entities/           # 组织、人物、项目（描述性，80-200 行）
│   ├── comparisons/        # 横向对比分析（标准间、方法间）
│   └── sources/            # 原始来源摘要——单文档"说了什么"
├── raw/                     # 原始文件（不可变，来源文档）
│   ├── papers/             # PDF 原文
│   └── articles/           # 转换后的文本
├── site/                    # 构建系统
│   ├── doc_config.py       # 标签映射与导航配置
│   ├── link_converter.py   # [[wikilink]] 转换引擎
│   └── site_builder.py     # 构建编排器
├── scripts/                 # 辅助工具
│   └── wiki-health-check.py# 健康检查（死链/孤儿页/标签覆盖率）
├── Makefile                 # 一键构建部署
├── SCHEMA.md                # 知识库规范
└── mkdocs.yml               # 网站配置
```

## 内容覆盖

- **MOSA 五大支柱**：赋能环境、模块化设计、指定接口、开放标准、一致性认证
- **政府参考架构（GRA）**：A-GRA、ABMS-GRA、AMS-GRA、NC3-GRA、PNT-GRA、Sentinel-GRA、DEWS-GRA
- **开放标准**：FACE、SOSA、OMS、VICTORY、CMOSS、WOSA、HOST、MORA
- **国防采办**：AAF、MTA、中间层采办、自适应采办框架、数字工程
- **MBSE 与 SysML v2**：OMG MBSE 标准族、SysML v2 过渡路线
- **军事项目案例**：CCA（协作作战飞机）、Sentinel（GBSD）、B-21、FLRAA
- **中国案例**：车路云一体化、智能网联汽车、华为车辆开放生态、大疆无人机架构
- **政策法规**：NDAA、DoDI 5000 系列、三军联合备忘录

## 内容流水线

原始文档 → `raw/` → 摘要 → `sources/` → 综合 → `concepts/` + `topics/`

```
raw/（原始 PDF/文本，不可变）
  → sources/（EXTRACTED：单文档摘要）
    → concepts/（SYNTHESIZED：概念定义，横向关系网络）
    → topics/（SYNTHESIZED：主题分析，纵向深度论述）
    → comparisons/（SYNTHESIZED：跨域对比）
```

参考资料 → `entities/`（人物、组织、项目的描述性条目）

### 内容定位

| 分类 | 回答 | 典型内容 |
|------|------|----------|
| `concepts/` | 这是什么 | 定义、特征、关系、语法规则 |
| `topics/` | 这个领域怎么样 | 发展脉络、挑战、趋势、方案对比 |
| `entities/` | 谁/什么机构 | 背景、项目、关键事件、MOSA 关联 |
| `comparisons/` | 有什么区别 | 跨标准/跨方法对比分析 |
| `sources/` | 文档说了什么 | 单篇摘要、提取关键论点 |

## 构建特性

### Mermaid 图表支持

核心概念页使用 Mermaid 图表（`block-beta`、`graph TB`、`graph LR`）展示架构关系。当前覆盖：SOSA 三层架构、A-GRA 四层体系、MOSA 五大支柱、GRA 变体关系、标准层级分类。

### 健康检查

```bash
make check   # 自动检测：死链、孤儿页、标签覆盖率、YAML 完整性
```

当前状态：**0 死链** · **8 孤儿页**（均为低频来源文档）· **161 个标签映射**

### 标签分类

每个 section 有独立的标签→分类映射（`doc_config.py`），确保导航和索引按语义分组而非按字母排列。

## 数据来源

- 美国国防部公开报告（DOTE、GAO、CRS、DSB）
- NDAA 法案原文
- 军事标准文档（FACE、SOSA、OMS、VICTORY）
- 学术论文（NDIA、AIAA、NPS、Purdue）
- 开源情报和新闻报道（Defense News、Military Embedded、Breaking Defense）

## 贡献指南

1. Fork 仓库
2. 创建特性分支
3. 提交更改
4. 创建 Pull Request

### 内容规范

- 遵循 [SCHEMA.md](SCHEMA.md) 定义的分类规则
- 原始文件放在 `raw/` 目录
- 摘要页面放在 `wiki/` 对应子目录
- 所有页面必须有 YAML frontmatter（`type`、`tags`、`sources`、`confidence`）
- 使用 `[[wikilinks]]` 建立交叉引用

## 项目结构演进

- **2026-05-24**：拆分 `build-site.py` → `doc_config.py` + `link_converter.py` + `site_builder.py`；新增 `Makefile`；nav 自动生成；Mermaid 图表支持
- **2026-05-16**：新增 `wiki-ingest.py` 批量入库管道；`wiki-health-check.py` 健康检查
- **2026-05-10**：`check-yaml.py` YAML 完整性预检；`build-site.py` 自动索引生成

## 许可证

[CC BY-SA 4.0](LICENSE)

## 相关项目

- [LLM Wiki](https://github.com/karpathy/llm-wiki) — Andrej Karpathy 的知识库模式
- [MOSA 官方资源](https://www.acq.osd.mil/se/mosa/) — 美国国防部 MOSA 资源

## 联系方式

- 问题反馈：[Issues](https://gitee.com/yufei96/llm-wiki/issues)
- 讨论交流：[Discussions](https://gitee.com/yufei96/llm-wiki/discussions)

---

**更新频率**：持续更新
**最后更新**：2026-05-24
