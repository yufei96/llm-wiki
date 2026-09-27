# Issue tracker：GitHub Issues

项目议题与规格以 GitHub Issues 为准，使用 `gh` CLI 操作。

## 常用操作

- 创建：`gh issue create --title "标题" --body-file <文件>`。
- 查看议题及评论：`gh issue view <编号> --comments`。
- 列出未关闭议题：`gh issue list --state open`。
- 评论：`gh issue comment <编号> --body "内容"`。
- 添加或移除标签：`gh issue edit <编号> --add-label <标签>` 或 `--remove-label <标签>`。
- 关闭：`gh issue close <编号> --comment "解决说明"`。

仓库的 pull request 不作为功能请求或议题入口。

## Wayfinder 操作

- 地图是带 `wayfinder:map` 标签的单个议题；决策议题是地图的子议题。
- 子议题带一个 `wayfinder:<type>` 标签，type 为 `research`、`prototype`、`grilling` 或 `task`。
- 使用 GitHub 原生 issue dependencies 表示阻塞；不可用时，在子议题正文记录 `Blocked by: #<编号>`。
- 前沿议题指所有阻塞议题均已关闭、议题未关闭且尚未指派的子议题；按地图顺序处理。
- 开始处理前先将议题指派给当前开发者。解决时记录答案、关闭议题，并在地图的 Decisions so far 中添加一句摘要和链接。
- 一次只解决一个议题；并行研究只限 Wayfinder 技能规定的 research 议题。

## Pull request

Pull request 不作为功能请求入口。不要将外部 pull request 纳入议题分流。
