# MOSA 知识库

**Modular Open Systems Approach (MOSA) 与数字工程知识库**

国防开放系统架构、智能网联汽车、军事开放标准的中文知识库。

## 快速开始

### 🌐 在线浏览

**[wiki.05132024.xyz](https://wiki.05132024.xyz)**

无需安装，直接浏览所有知识库页面。

### 📥 下载使用

```bash
git clone https://gitee.com/yufei96/llm-wiki.git
cd llm-wiki
```

#### 方式 1：Obsidian 本地浏览

1. 用 [Obsidian](https://obsidian.md) 打开克隆的文件夹
2. 直接浏览和编辑，所有 `[[wiki-links]]` 自动生效
3. 适合深度研究和内容贡献

#### 方式 2：导入 IMA Copilot

1. 克隆仓库
2. 在 [IMA Copilot](https://ima.qq.com) 中导入 `raw/` 目录下的 PDF 文件
3. IMA 自动生成知识图谱和问答

#### 方式 3：导入 NotebookLM

1. 克隆仓库
2. 上传 `wiki/` 目录到 [NotebookLM](https://notebooklm.google.com)
3. 自动生成知识图谱和对话式问答

#### 方式 4：Agent 交互

克隆仓库后，用支持知识库的 AI Agent 进行交互式问答：

```
"帮我查一下 MOSA 的五原则是什么"
"对比 FACE 和 SOSA 标准"
"总结 DOTE 2025 报告中 LTAMDS 的测试结果"
```

适用的 Agent 工具：Hermes Agent、Claude、ChatGPT 等支持文件上传的 LLM。

## 仓库结构

```
llm-wiki/
├── wiki/                    # 知识库主体（Markdown）
│   ├── sources/            # 原始来源摘要
│   ├── concepts/           # 核心概念定义
│   ├── entities/           # 组织、人物、项目
│   ├── topics/             # 纵向深度分析
│   └── comparisons/        # 横向对比分析
├── raw/                     # 原始文件（不可变）
│   ├── papers/             # PDF 原文
│   └── articles/           # 转换后的文本
├── SCHEMA.md                # 知识库规范
└── mkdocs.yml              # 网站构建配置
```

## 内容覆盖

- **MOSA 五原则**：模块化、开放接口、松耦合、可重用、可互操作
- **开放标准**：FACE、SOSA、OMS、UCI、VICTORY、CMOSS
- **国防采购**：自适应采购框架、数字工程、模型系统工程
- **中国案例**：车路云一体化、智能网联汽车开放架构
- **政策法规**：NDAA、DODI、三军联合备忘录
- **技术报告**：DOTE 年度评估、GAO 武器系统审计

## 数据来源

- 美国国防部公开报告（DOTE、GAO、CRS）
- NDAA 法案原文
- 军事标准文档（FACE、SOSA、OMS）
- 学术论文（NDIA、AIAA、NPS）
- 开源情报和新闻报道

## 贡献指南

1. Fork 仓库
2. 创建特性分支 (`git checkout -b feature/xxx`)
3. 提交更改 (`git commit -m 'Add xxx'`)
4. 推送到分支 (`git push origin feature/xxx`)
5. 创建 Pull Request

### 内容规范

- 遵循 [SCHEMA.md](SCHEMA.md) 定义的分类规则
- 原始文件放在 `raw/` 目录
- 摘要页面放在 `wiki/` 对应子目录
- 所有页面必须有 YAML frontmatter
- 使用 `[[wiki-links]]` 建立交叉引用

## 许可证

本知识库采用 [MIT 许可证](LICENSE)。

## 相关项目

- [LLM Wiki](https://github.com/karpathy/llm-wiki) - Andrej Karpathy 的知识库模式
- [MOSA 官方资源](https://www.acq.osd.mil/se/mosa/) - 美国国防部 MOSA 资源

## 联系方式

- 问题反馈：[Issues](https://gitee.com/yufei96/llm-wiki/issues)
- 讨论交流：[Discussions](https://gitee.com/yufei96/llm-wiki/discussions)

---

**更新频率**：持续更新  
**最后更新**：2026-05-08
