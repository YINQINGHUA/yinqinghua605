# AGENTS.md

## 仓库概览

- 纯静态课程作业仓库：原生 HTML/CSS/JS，无构建、无依赖安装、无测试/lint/类型检查。改完直接在浏览器打开 `index.html` 验证。
- Git 仓库根是整个工作区（`D:\高级网页设计`），不是 `24002120605尹清华/`；git 命令在根目录执行。
- 两个独立项目：
  - `24002120605尹清华/` — 当前课堂实践，入口 `index.html`（练习目录），新代码放这里。
  - `24002120605-尹清华-三·四级项目/` — 旧的 Keep H5 多页项目，入口 `index.html`，类名用 `yin_` 前缀，与 `yqh_` 规则无关，勿混用。

## 强制工作流（先做，再做别的）

- 执行任何用户提示词之前，先把记录**追加**到 `24002120605尹清华/yqh_prompt.md`，绝不覆盖。格式照现有条目：`## yyyy-MM-dd HH:mm:ss | 模型：<模型>`、`**提示词：**`、原话、`**执行说明/执行计划：**`。时间用 `Get-Date -Format "yyyy-MM-dd HH:mm:ss"`。纯讲解/提问也照记。
- 项目级规则以 `.trae/skills/yqh-web-rules/SKILL.md` 为准，优先于通用习惯。

## 命名与页面约定（`24002120605尹清华/`）

- 所有**自建** CSS 类名、id、JS 变量（含函数名、参数、局部变量、对象属性、keyframes、`data-*`）一律以 `yqh_` 开头。
- 第三方类名/API 不改名：`fa-solid`/`fa-brands`、`data-lucide`、`iconfont`/`icon-*`。
- 例外：`starter-level1.html`、`starter-level2.html` 是固定教学模板（HTML 结构、id、函数名已约定），沿用模板命名，不要套 `yqh_`。
- 每个新建 HTML 必须含返回首页链接 `<a class="yqh_home" href="index.html">← 返回首页</a>`；`<html lang="zh-CN">`、UTF-8、viewport；含固定底栏的页面加 `viewport-fit=cover`。
- `index.html` 的课堂目录是手动维护的卡片列表；新增页面时同步补一条入口。

## 本地资源（运行时不引外链）

- Font Awesome：`cdn/fontawesome/css/all.min.css` + `cdn/fontawesome/webfonts/`。
- Lucide：`cdn/lucide/lucide.min.js`；占位 `<i data-lucide="...">` 后调用 `lucide.createIcons()`。
- iconfont.cn 包在 `font/`（4 个图标，清单见 `font/iconfont.json`）：字体方式引 `font/iconfont.css` + `<i class="iconfont icon-xxx">`；SVG 方式引 `font/iconfont.js` + `<svg><use href="#icon-xxx"></use></svg>`。精灵里部分 path 写死 `fill`，换色前先 `removeAttribute('fill')`。

## 页面设计

- 新页面遵循 `skills/frontend-design/SKILL.md`：拒绝模板化视觉，字体/配色/布局要有明确意图，尊重 `prefers-reduced-motion` 与键盘焦点。
- 既有「字·线 图标工坊」系列视觉基调见 `.trae/skills/yqh-web-rules/SKILL.md`。

## 数据练习

- `data.js` 暴露 `window.STUDENTS` / `window.SUBJECTS`。
- `starter-level1.html` / `starter-level2.html` 按 `TODO` 注释补全函数；模板注释要求与 `target.html` 一比一还原，但该参考文件未入库。

## Git / Gitee

- `origin` = `https://gitee.com/neusoft_wangyao_jsj/webprojectyinqinghua.git`，分支 `master`。
- 仅在用户明确要求时 commit/push；提交前先 `git status`、`git diff`。
- 推送凭证用 Gitee 私人令牌（经 Windows 凭据管理器），**令牌绝不写入任何文件或 `.git/config`**；可走 `gitee-project-submit` skill。

## 工具注意

- PowerShell 控制台可能把中文显示成乱码，但文件本身是 UTF-8。读写/搜索中文内容用 Read/Grep/Edit 工具，不要用 `Get-Content`/`Select-String` 判断内容是否损坏。
