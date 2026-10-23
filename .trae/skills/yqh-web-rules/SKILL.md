---
name: yqh-web-rules
description: 沉淀本课程作业项目的持久规则——所有自建CSS类名id名JS变量以yqh_开头，用户提示词执行前先附加记录到yqh_prompt.md，新建html须含返回index.html链接，图标使用font与cdn本地资源。凡在本项目新建或修改页面、记录提示词、引用图标库时使用；不适用于其他项目。
---

# 字·线 图标工坊项目规则

本目录是高级网页设计课程作业（学号 24002120605 尹清华）的工作区。执行任何页面开发任务前，先按下列规则操作。

## 规则一：提示词先行记录

- 用户每条提示词必须在**执行之前**以附加方式写入项目根目录的 `yqh_prompt.md`，不得覆盖已有内容。
- 记录格式（与文件中既有条目保持一致）：

```markdown
---

## yyyy-MM-dd HH:mm:ss | 模型：<模型名>

**提示词：**

<用户原话>

**执行说明/执行计划：** <一句话说明将做什么>
```

- 时间用 `Get-Date -Format "yyyy-MM-dd HH:mm:ss"` 获取。

## 规则二：yqh_ 命名前缀

- 所有**自建** CSS 类名、id 名、JS 变量（含函数名、参数、局部变量、对象属性、CSS keyframes 动画名、data-* 属性名）一律以 `yqh_` 开头，如 `yqh_tabbar`、`yqh_cart_badge`、`yqh_rise_bar`、`data-yqh-label`。
- 第三方库自身的类名与 API 不改名：Font Awesome 的 `fa-solid`/`fa-brands`、Lucide 的 `data-lucide`、iconfont 的 `iconfont`/`icon-*` 保持原样。

## 规则三：新建 HTML 的必备项

- 每个新建的 html 文件在页面内加入指向首页的超链接入口，形如 `<a class="yqh_home" href="index.html">← 返回首页</a>`，通常放在顶栏与页脚。
- `<html lang="zh-CN">`、UTF-8、viewport 移动端适配（`viewport-fit=cover` 用于含固定底栏的页面）。

## 规则四：图标资源全部本地化

- Font Awesome：`cdn/fontawesome/css/all.min.css` + `cdn/fontawesome/webfonts/`（CSS 相对路径自动加载 woff2/ttf）。
- Lucide：`cdn/lucide/lucide.min.js`，占位符 `<i data-lucide="名">` 由 `lucide.createIcons()` 替换为内联 SVG。
- iconfont.cn 包：`font/` 目录。字体方式引 `font/iconfont.css` 后用 `<i class="iconfont icon-xxx">`；SVG 方式引 `font/iconfont.js`（自动注入 symbol 精灵）后用 `<svg><use href="#icon-xxx"></use></svg>`。注意 iconfont 精灵中部分 path 写死 fill 属性，换色前需 `removeAttribute('fill')`。
- 现有图标清单见 `font/iconfont.json`（首页/购物车/收藏/我的 4 枚）。

## 页面设计基调

- 系列视觉「字·线 图标工坊」：卷一/卷三用 瓷纸×玄墨×靛青×朱砂（楷体标题），卷二/卷四用 雾纸×炭墨×青瓷×藤黄（重黑体标题）。
- 遵循 skills/frontend-design/SKILL.md 的设计要求；动效克制，尊重 `prefers-reduced-motion` 与键盘焦点样式。
