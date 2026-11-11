# -*- coding: utf-8 -*-
"""
作者：尹清华（24002120605）
建立时间：2026-11-11
使用大模型：DeepSeek-V4.1-Flash
功能名称：把 yqh_prompt.md 转换成可读的 yqh_prompt.html（浏览器直接打开即可查看）
说明：yqh_prompt.md 更新后，在仓库根目录执行 python md2html.py 重新生成一次即可。
"""

import html
import pathlib
import re

SRC = pathlib.Path("yqh_prompt.md")
DST = pathlib.Path("yqh_prompt.html")
# 只保留该日期（含）之后的记录
CUTOFF = "2026-11-10"

TEMPLATE = """<!DOCTYPE html>
<!--
  作者：尹清华（24002120605）
  建立时间：2026-11-11
  使用大模型：DeepSeek-V4.1-Flash
  功能名称：提示词记录阅读页（由 md2html.py 从 yqh_prompt.md 自动生成，请勿手改）
-->
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>提示词记录 · 高级网页设计</title>
<style>
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{
    font-family:"Microsoft YaHei","PingFang SC",system-ui,sans-serif;
    background:#f7f5ef;color:#2b2b2b;line-height:1.9;
    padding:32px 18px 60px;
  }}
  .yqh_home{{
    display:inline-block;margin-bottom:22px;text-decoration:none;font-size:13.5px;
    color:#7a5b2a;border:1px solid #d8c9a8;border-radius:999px;padding:7px 18px;background:#fff;
  }}
  .yqh_home:hover{{background:#f1e7d2}}
  .yqh_doc{{max-width:900px;margin:0 auto;background:#fff;border:1px solid #e6e0d2;border-radius:14px;padding:34px 38px;box-shadow:0 6px 20px rgba(90,70,30,.07)}}
  .yqh_doc h1{{font-size:25px;color:#3a2c14;margin-bottom:18px;letter-spacing:1px}}
  .yqh_doc h2{{font-size:17px;color:#8a5a12;margin:26px 0 8px;padding-top:16px;border-top:1px dashed #e8dfc8;letter-spacing:.5px}}
  .yqh_doc h2:first-of-type{{border-top:none;padding-top:0}}
  .yqh_doc h3{{font-size:15px;color:#4a3a1c;margin:16px 0 6px}}
  .yqh_doc p{{font-size:14.5px;margin:6px 0;color:#3b3b3b}}
  .yqh_doc hr{{border:none;border-top:1px solid #f0ead9;margin:18px 0}}
  .yqh_doc strong{{color:#8a3d0c}}
  .yqh_doc code{{background:#f6efe0;color:#8a4b00;padding:1px 6px;border-radius:5px;font-family:Consolas,monospace;font-size:13px}}
  .yqh_count{{text-align:center;font-size:12.5px;color:#a09780;margin-top:18px}}
</style>
</head>
<body>
<a class="yqh_home" href="index.html">← 返回首页</a>
<div class="yqh_doc">
{body}
</div>
<p class="yqh_count">{count} 条记录 · 由 yqh_prompt.md 自动生成</p>
</body>
</html>
"""


def inline(text):
    """yqh_inline：处理一行里的粗体与行内代码，并转义 HTML 特殊字符"""
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


def convert(md_text):
    """yqh_convert：把 markdown 逐行转成 HTML 片段，收集记录条数"""
    blocks = []
    buffer = []
    count = 0

    def flush():
        if buffer:
            blocks.append("<p>" + "<br>".join(buffer) + "</p>")
            buffer.clear()

    for raw in md_text.split("\n"):
        line = raw.rstrip()
        if not line.strip():
            flush()
            continue
        if re.match(r"^-{3,}$", line.strip()):
            flush()
            blocks.append("<hr>")
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush()
            level = len(m.group(1))
            title = inline(m.group(2))
            blocks.append(f"<h{level}>{title}</h{level}>")
            if level == 2:
                count += 1
            continue
        buffer.append(inline(line))
    flush()
    return "\n".join(blocks), count


def keep_blocks(md_text):
    """yqh_keepBlocks：按 '---' 切分记录块，只保留 CUTOFF 当天及之后的记录"""
    kept = []
    for block in re.split(r"\n-{3,}\n", md_text):
        m = re.search(r"^## (\d{4}-\d{2}-\d{2})", block, re.M)
        if not m:
            continue  # 文件开头的标题说明块没有日期，直接丢掉
        if m.group(1) >= CUTOFF:
            kept.append(block.strip())
    return "\n\n---\n\n".join(kept)


def main():
    md = SRC.read_text(encoding="utf-8")
    body, count = convert(keep_blocks(md))
    header = f'<h1>AI 提示词记录</h1>\n<p>仅保留 {CUTOFF} 起的 {count} 条记录</p>\n'
    DST.write_text(TEMPLATE.format(body=header + body, count=count), encoding="utf-8")
    print(f"已生成 {DST}，共 {count} 条记录（{CUTOFF} 起）")


if __name__ == "__main__":
    main()
