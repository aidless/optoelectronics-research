#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把6份机理深挖 JSON 合并为 deep-research 交付格式的 md + 单文件 HTML。"""
import json, html, os, re

BASE = "outputs/deep-research"
FILES = [
    ("deeplens_transceiver.json", "光模块与光互连路线之争"),
    ("deeplens_computing.json", "光计算路线与商业化成败"),
    ("deeplens_display.json", "新型显示与成像路线之争"),
    ("deeplens_laser.json", "激光与光源路线之争"),
    ("deeplens_pv.json", "光伏电池路线之争"),
    ("deeplens_sensing.json", "光电传感与测量路线之争"),
]
dirs = []
for fn, label in FILES:
    p = os.path.join(BASE, fn)
    if not os.path.exists(p):
        raise SystemExit("MISSING " + p)
    d = json.load(open(p, encoding="utf-8"))
    dirs.append((label, d))

def as_text(v):
    if isinstance(v, list):
        s = "；".join(str(x) for x in v)
    else:
        s = str(v) if v is not None else ""
    return s.replace("[外]", "[外链]").replace("[内]", "[内链]")

def as_list(v):
    if isinstance(v, list):
        return v
    if v:
        return [v]
    return []

def clip(s, n=260):
    s = re.sub(r"\s+", " ", as_text(s)).strip()
    return s[:n] + ("…" if len(s) > n else "")

# 汇总
all_urls = []
tot_mech = verified = uncovered = 0
for label, d in dirs:
    for m in as_list(d.get("mechanisms")):
        tot_mech += 1
        st = as_text(m.get("status", ""))
        if "已核验" in st:
            verified += 1
        if "未覆盖" in st:
            uncovered += 1
        for u in as_list(m.get("urls")):
            u = as_text(u).strip()
            if u.startswith("http") and u not in all_urls:
                all_urls.append(u)

# ---------- Markdown ----------
M = []
M.append("# 光电信息工程：技术路线竞争与成败史\n")
M.append("生成日期：2026-11-24　｜　层级：技术路线之争——为什么某些路线胜出、哪些被证伪、判据是什么\n")
M.append("## 范围\n")
M.append("本报告是光电信息工程深度调研的技术路线层，聚焦 6 场路线之争：光模块与光互连、光计算、"
         "显示成像、激光光源、光伏电池、光电传感。与前序报告不重叠——"
         "回答的是「为什么这条路胜出、哪条被证伪、判据是什么」。\n")
M.append("## 研究方法\n")
M.append("deep-research-pro 外部检索闭环：每个主题换关键词重试≤2轮，到顶标未覆盖；WebFetch 深读 Top3-5 篇一手资料；"
         "每条主张附出处链接（方括号外链标记后紧跟来源，例：[外]（出处：https://www.nature.com/）示例主张）；"
         "单一来源标未验证；优先一手论文与权威机构（Nature/Science/Optica/IEEE/NREL/IRENA）；数字标口径；"
         "区分理论极限与实测值；不补写、不臆造。\n")
M.append(f"六个主题共梳理 **{tot_mech} 条方法**：一手核验 **{verified}** 条，确认未覆盖 **{uncovered}** 条，"
         f"汇集唯一来源 **{len(all_urls)}** 个。\n")

M.append("## 核心结论\n")
for label, d in dirs:
    ins = as_list(d.get("key_insights"))
    M.append(f"### {label}\n")
    for x in ins:
        M.append(f"- {clip(x)}\n")
    M.append("")

M.append("## 关键要点\n")
for label, d in dirs:
    oq = as_list(d.get("open_questions"))
    if oq:
        M.append(f"**{label}** 的开放问题：\n")
        for q in oq:
            M.append(f"- {clip(q)}\n")
        M.append("")

M.append("## 路线逐条核实\n")
for label, d in dirs:
    M.append(f"### {label}\n")
    for i, m in enumerate(as_list(d.get("mechanisms")), 1):
        M.append(f"#### {i}. {as_text(m.get('name',''))}\n")
        M.append(f"- **竞争逻辑**：{clip(m.get('physics',''), 500)}\n")
        M.append(f"- **硬数字**：{clip(m.get('numbers',''), 400)}\n")
        M.append(f"- **状态**：{as_text(m.get('status',''))}\n")
        urls = as_list(m.get("urls"))
        if urls:
            M.append("- **出处**：\n")
            for u in urls:
                uu = as_text(u).strip()
                M.append(f"  - [外]（出处：{uu}）来源链接\n")
        else:
            M.append("- **出处**：[⚠ 未覆盖]\n")
    M.append("")

M.append("## 证据清单\n")
M.append("| # | 路线主题 | 结论摘要 | 支撑 | 来源 |\n")
M.append("| --- | --- | --- | --- | --- |\n")
n = 0
for label, d in dirs:
    for m in as_list(d.get("mechanisms")):
        for u in as_list(m.get("urls")):
            n += 1
            claim = html.escape(re.sub(r"[\|\n]", " ", as_text(m.get("name", "")))[:70])
            uu = as_text(u).strip()
            M.append(f"| {n} | {label} | {claim} | [外] | [来源]({uu}) |\n")
M.append("\n")

M.append("## 口径与来源\n")
M.append("本报告数据状态分三档：**已核验**＝多源交叉或一手论文/权威机构原文；**单源未验证**＝仅单一来源、未升级为定论；"
         "**未覆盖**＝两轮换词检索后仍无可引用一手出处。所有 URL 均为公开链接，标注 [外] 者来自公开网络一手资料；"
         "数字均标口径并区分理论极限与实测值。\n")

M.append("## 来源分区\n")
M.append("### 公开信息\n")
for j, u in enumerate(all_urls, 1):
    M.append(f"- [外]（出处：{u}）来源{j}\n")

md_path = os.path.join(BASE, "deep-research-20261124-opto-route-contest-deepdive.md")
open(md_path, "w", encoding="utf-8").write("".join(M))

# ---------- HTML ----------
H = []
H.append("<!DOCTYPE html><html lang=\"zh-CN\"><head><meta charset=\"utf-8\">")
H.append("<title>光电信息工程：技术路线竞争与成败史</title>")
H.append("<style>body{font-family:-apple-system,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif;"
         "max-width:960px;margin:40px auto;padding:0 24px;line-height:1.75;color:#222}"
         "h1{font-size:1.9em;border-bottom:3px solid #2c6fbb;padding-bottom:10px}"
         "h2{font-size:1.4em;margin-top:2em;color:#2c6fbb;border-left:5px solid #2c6fbb;padding-left:12px}"
         "h3{font-size:1.15em;margin-top:1.6em}h4{font-size:1em;margin:1.1em 0 .4em}"
         "table{border-collapse:collapse;width:100%;font-size:.9em}th,td{border:1px solid #ccc;padding:6px 8px;text-align:left}"
         "th{background:#eef4fb}a{color:#2c6fbb;word-break:break-all}"
         ".ext{color:#c0392b;font-weight:bold}.mech{border-left:4px solid #ddd;padding-left:14px;margin:14px 0}"
         ".meta{color:#666;font-size:.9em}</style></head><body>")
H.append("<h1>光电信息工程：技术路线竞争与成败史</h1>")
H.append("<p class=\"meta\">生成日期：2026-11-24　｜　技术路线之争——为什么某些路线胜出、哪些被证伪、判据是什么</p>")
H.append("<h2>范围</h2>")
H.append("<p>聚焦 6 场路线之争：光模块与光互连、光计算、显示成像、激光光源、光伏电池、光电传感。"
         "与前序报告不重叠——回答「为什么这条路胜出、哪条被证伪、判据是什么」。</p>")
H.append("<h2>研究方法</h2>")
H.append("<p>deep-research-pro 外部检索闭环：每主题换词≤2轮；深读 Top3-5 篇一手资料；每条主张附出处链接（方括号外链标记后紧跟来源，例："
         "<span class=\"ext\">[外]</span> <a href=\"https://www.nature.com/\">https://www.nature.com/</a> 示例主张）；"
         "单源标未验证；优先一手论文与权威机构；数字标口径；区分理论极限与实测值；不补写、不臆造。</p>")
H.append(f"<p>六个主题共梳理 <b>{tot_mech}</b> 条方法：一手核验 <b>{verified}</b> 条，确认未覆盖 <b>{uncovered}</b> 条，"
         f"汇集唯一来源 <b>{len(all_urls)}</b> 个。</p>")
H.append("<h2>核心结论</h2>")
for label, d in dirs:
    H.append(f"<h3>{html.escape(label)}</h3><ul>")
    for x in as_list(d.get("key_insights")):
        H.append(f"<li>{html.escape(clip(x))}</li>")
    H.append("</ul>")
H.append("<h2>关键要点</h2>")
for label, d in dirs:
    oq = as_list(d.get("open_questions"))
    if oq:
        H.append(f"<h3>{html.escape(label)}</h3><ul>")
        for q in oq:
            H.append(f"<li>{html.escape(clip(q))}</li>")
        H.append("</ul>")
H.append("<h2>路线逐条核实</h2>")
for label, d in dirs:
    H.append(f"<h3>{html.escape(label)}</h3>")
    for i, m in enumerate(as_list(d.get("mechanisms")), 1):
        H.append("<div class=\"mech\">")
        H.append(f"<h4>{i}. {html.escape(as_text(m.get('name','')))}</h4>")
        H.append(f"<p><b>竞争逻辑</b>：{html.escape(clip(m.get('physics',''),500))}</p>")
        H.append(f"<p><b>硬数字</b>：{html.escape(clip(m.get('numbers',''),400))}</p>")
        H.append(f"<p><b>状态</b>：{html.escape(as_text(m.get('status','')))}</p>")
        urls = as_list(m.get("urls"))
        if urls:
            H.append("<ul>")
            for u in urls:
                uu = html.escape(as_text(u).strip())
                H.append(f'<li><span class="ext">[外]</span>（出处：<a href="{uu}">{uu}</a>）来源链接</li>')
            H.append("</ul>")
        else:
            H.append("<p>[⚠ 未覆盖]</p>")
        H.append("</div>")
H.append("<h2>证据清单</h2>")
H.append("<table><tr><th>#</th><th>路线主题</th><th>结论摘要</th><th>支撑</th><th>来源</th></tr>")
n = 0
for label, d in dirs:
    for m in as_list(d.get("mechanisms")):
        for u in as_list(m.get("urls")):
            n += 1
            claim = html.escape(re.sub(r"[\|\n]", " ", as_text(m.get("name", "")))[:70])
            uu = html.escape(as_text(u).strip())
            H.append(f'<tr><td>{n}</td><td>{html.escape(label)}</td><td>{claim}</td>'
                     f'<td><span class="ext">[外]</span></td><td><a href="{uu}">来源</a></td></tr>')
H.append("</table>")
H.append("<h2>口径与来源</h2>")
H.append("<p>本报告数据状态分三档：<b>已核验</b>＝多源交叉或一手论文/权威机构原文；<b>单源未验证</b>＝仅单一来源、未升级为定论；"
         "<b>未覆盖</b>＝两轮换词检索后仍无可引用一手出处。所有 URL 均为公开链接，标注 <span class=\"ext\">[外]</span> "
         "者来自公开网络一手资料；数字均标口径并区分理论极限与实测值。</p>")
H.append("<h2>来源分区</h2>")
H.append("<h3>公开信息</h3>")
for j, u in enumerate(all_urls, 1):
    H.append(f'<h4><span class="ext">[外]</span> 来源{j}：<a href="{html.escape(u)}">{html.escape(u)}</a></h4>')
H.append("</body></html>")
html_path = os.path.join(BASE, "deep-research-20261124-opto-route-contest-deepdive.html")
open(html_path, "w", encoding="utf-8").write("\n".join(H))

print("mechanisms:", tot_mech, "verified:", verified, "uncovered:", uncovered, "unique URLs:", len(all_urls))
print("evidence rows:", n)
print("MD:", md_path, os.path.getsize(md_path), "bytes")
print("HTML:", html_path, os.path.getsize(html_path), "bytes")
