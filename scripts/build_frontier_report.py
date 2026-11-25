#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把6份前沿盲区 JSON 合并为 deep-research 交付格式的 md + 单文件 HTML。"""
import json, html, os, re

BASE = "outputs/deep-research"
FILES = [
    ("deepfront_metasurface.json", "超表面 / 平面光学"),
    ("deepfront_microcomb.json", "光频梳 / 微腔光频梳"),
    ("deepfront_quantum.json", "集成量子光子学"),
    ("deepfront_nonlinear.json", "非线性光子与拓扑光子"),
    ("deepfront_2dmaterial.json", "二维材料光子学"),
    ("deepfront_thz.json", "太赫兹与中红外光子"),
]
dirs = []
for fn, label in FILES:
    p = os.path.join(BASE, fn)
    if not os.path.exists(p):
        raise SystemExit("MISSING " + p)
    dirs.append((label, json.load(open(p, encoding="utf-8"))))

def as_text(v):
    if isinstance(v, dict):
        s = "；".join(f"{k}：{as_text(x)}" for k, x in v.items())
    elif isinstance(v, list):
        s = "；".join(as_text(x) for x in v)
    else:
        s = str(v) if v is not None else ""
    return s.replace("[外]", "[外链]").replace("[内]", "[内链]")

def as_list(v):
    return v if isinstance(v, list) else ([v] if v else [])

def clip(s, n=300):
    s = re.sub(r"\s+", " ", as_text(s)).strip()
    return s[:n] + ("…" if len(s) > n else "")

all_urls = []
tot = verified = uncovered = 0
for label, d in dirs:
    for m in as_list(d.get("mechanisms")):
        tot += 1
        st = as_text(m.get("status", ""))
        verified += int("已核验" in st)
        uncovered += int("未覆盖" in st)
        for u in as_list(m.get("urls")):
            u = as_text(u).strip()
            if u.startswith("http") and u not in all_urls:
                all_urls.append(u)

M = []
M.append("# 光电信息工程：前沿盲区深挖\n")
M.append("生成日期：2026-11-25　｜　层级：前 13 赛道未系统覆盖的新机制、新器件与新成熟度曲线\n")
M.append("## 范围\n")
M.append("本报告聚焦六个前沿盲区：超表面/平面光学、光频梳/微腔光频梳、集成量子光子学、"
         "非线性光子与拓扑光子、二维材料光子学、太赫兹与中红外光子学。"
         "目标不是追加产业热度榜，而是判断新机制是否已有可复算的实测性能、处于何种成熟度、"
         "能否与现有硅光/CPO/光计算/显示/传感赛道接口，以及未来 3–5 年哪些问题值得下注。\n")
M.append("## 研究方法\n")
M.append("采用 deep-research-pro 外部检索闭环：每个主题换关键词不超过两轮，到顶标未覆盖；深读 Top 3–5 篇一手资料；"
         "优先 Nature/Science/Optica/PRL/IEEE/arXiv 原文；每条主张附来源链接（例："
         "[外]（出处：https://www.nature.com/）示例主张）；单一来源标未验证。"
         "严格区分仿真/实测、器件/系统、实验室/原型/商用，不把单元效率写成镜头效率、不把量子采样写成通用计算优势。\n")
M.append(f"共梳理 **{tot} 条前沿机制**：一手核验 **{verified}** 条，确认未覆盖 **{uncovered}** 条，"
         f"汇集唯一来源 **{len(all_urls)}** 个。\n")
M.append("## 核心结论\n")
for label, d in dirs:
    M.append(f"### {label}\n")
    for x in as_list(d.get("key_insights")):
        M.append(f"- {clip(x)}\n")
    M.append("")
M.append("## 关键要点：未来 3–5 年值得下注的问题\n")
for label, d in dirs:
    qs = as_list(d.get("open_questions"))
    if qs:
        M.append(f"### {label}\n")
        for q in qs:
            M.append(f"- {clip(q)}\n")
        M.append("")
M.append("## 前沿机制逐条核实\n")
for label, d in dirs:
    M.append(f"### {label}\n")
    for i, m in enumerate(as_list(d.get("mechanisms")), 1):
        M.append(f"#### {i}. {as_text(m.get('name',''))}\n")
        M.append(f"- **物理机制**：{clip(m.get('physics',''),500)}\n")
        M.append(f"- **可复算性能**：{clip(m.get('numbers',''),450)}\n")
        M.append(f"- **证据状态**：{as_text(m.get('status',''))}\n")
        M.append(f"- **成熟度**：{as_text(m.get('maturity','未标注'))}\n")
        M.append(f"- **与现有赛道接口**：{clip(m.get('link_to_existing','未标注'))}\n")
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
M.append("| # | 前沿主题 | 结论摘要 | 成熟度 |\n| --- | --- | --- | --- |\n")
n = 0
for label, d in dirs:
    for m in as_list(d.get("mechanisms")):
        for u in as_list(m.get("urls")):
            n += 1
            name = re.sub(r"[\|\n]", " ", as_text(m.get("name", "")))[:75]
            uu = as_text(u).strip()
            M.append(f"| {n} | {label} | [{name}]({uu}) | {as_text(m.get('maturity','未标注'))} |\n")
M.append("\n## 来源分区\n### 公开信息\n")
for j, u in enumerate(all_urls, 1):
    M.append(f"- [外]（出处：{u}）来源{j}\n")
md_path = os.path.join(BASE, "deep-research-20261125-opto-frontiers-deepdive.md")
open(md_path, "w", encoding="utf-8").write("".join(M))

H = []
H.append('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">')
H.append('<title>光电信息工程：前沿盲区深挖</title>')
H.append("<style>body{font-family:-apple-system,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif;max-width:1000px;margin:40px auto;padding:0 24px;line-height:1.75;color:#222}h1{font-size:1.9em;border-bottom:3px solid #2c6fbb;padding-bottom:10px}h2{font-size:1.4em;margin-top:2em;color:#2c6fbb;border-left:5px solid #2c6fbb;padding-left:12px}h3{font-size:1.15em;margin-top:1.6em}h4{font-size:1em;margin:1.1em 0 .4em}table{border-collapse:collapse;width:100%;font-size:.9em}th,td{border:1px solid #ccc;padding:6px 8px;text-align:left}th{background:#eef4fb}a{color:#2c6fbb;word-break:break-all}.ext{color:#c0392b;font-weight:bold}.front{border-left:4px solid #ddd;padding-left:14px;margin:14px 0}.meta{color:#666;font-size:.9em}</style></head><body>")
H.append("<h1>光电信息工程：前沿盲区深挖</h1>")
H.append('<p class="meta">生成日期：2026-11-25　｜　前 13 赛道未系统覆盖的新机制、新器件与新成熟度曲线</p>')
H.append("<h2>范围</h2><p>六个前沿盲区：超表面/平面光学、光频梳/微腔光频梳、集成量子光子学、非线性光子与拓扑光子、二维材料光子学、太赫兹与中红外光子学。重点判断可复算实测性能、成熟度、与现有赛道的接口，以及未来 3–5 年值得下注的问题。</p>")
H.append("<h2>研究方法</h2><p>deep-research-pro 外部检索闭环：每主题换词≤2轮；深读 Top3-5 篇一手资料；单源标未验证；严格区分仿真/实测、器件/系统、实验室/原型/商用。每条主张附出处链接（例：<span class=\"ext\">[外]</span> <a href=\"https://www.nature.com/\">https://www.nature.com/</a> 示例主张）。</p>")
H.append(f"<p>共梳理 <b>{tot}</b> 条前沿机制：一手核验 <b>{verified}</b> 条，确认未覆盖 <b>{uncovered}</b> 条，汇集唯一来源 <b>{len(all_urls)}</b> 个。</p>")
H.append("<h2>核心结论</h2>")
for label, d in dirs:
    H.append(f"<h3>{html.escape(label)}</h3><ul>")
    for x in as_list(d.get("key_insights")):
        H.append(f"<li>{html.escape(clip(x))}</li>")
    H.append("</ul>")
H.append("<h2>关键要点：未来 3–5 年值得下注的问题</h2>")
for label, d in dirs:
    qs = as_list(d.get("open_questions"))
    if qs:
        H.append(f"<h3>{html.escape(label)}</h3><ul>")
        for q in qs:
            H.append(f"<li>{html.escape(clip(q))}</li>")
        H.append("</ul>")
H.append("<h2>前沿机制逐条核实</h2>")
for label, d in dirs:
    H.append(f"<h3>{html.escape(label)}</h3>")
    for i, m in enumerate(as_list(d.get("mechanisms")), 1):
        H.append('<div class="front">')
        H.append(f"<h4>{i}. {html.escape(as_text(m.get('name','')))}</h4>")
        H.append(f"<p><b>物理机制</b>：{html.escape(clip(m.get('physics',''),500))}</p>")
        H.append(f"<p><b>可复算性能</b>：{html.escape(clip(m.get('numbers',''),450))}</p>")
        H.append(f"<p><b>证据状态</b>：{html.escape(as_text(m.get('status','')))}</p>")
        H.append(f"<p><b>成熟度</b>：{html.escape(as_text(m.get('maturity','未标注')))}</p>")
        H.append(f"<p><b>与现有赛道接口</b>：{html.escape(clip(m.get('link_to_existing','未标注')))}</p>")
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
H.append("<h2>证据清单</h2><table><tr><th>#</th><th>前沿主题</th><th>结论摘要</th><th>成熟度</th></tr>")
n = 0
for label, d in dirs:
    for m in as_list(d.get("mechanisms")):
        for u in as_list(m.get("urls")):
            n += 1
            name = html.escape(re.sub(r"[\|\n]", " ", as_text(m.get("name", "")))[:75])
            uu = html.escape(as_text(u).strip())
            H.append(f'<tr><td>{n}</td><td>{html.escape(label)}</td><td><a href="{uu}">{name}</a></td><td>{html.escape(as_text(m.get("maturity","未标注")))}</td></tr>')
H.append("</table><h2>来源分区</h2><h3>公开信息</h3>")
for j, u in enumerate(all_urls, 1):
    H.append(f'<h4><span class="ext">[外]</span> 来源{j}：<a href="{html.escape(u)}">{html.escape(u)}</a></h4>')
H.append("</body></html>")
html_path = os.path.join(BASE, "deep-research-20261125-opto-frontiers-deepdive.html")
open(html_path, "w", encoding="utf-8").write("\n".join(H))
print("frontiers:", tot, "verified:", verified, "uncovered:", uncovered, "unique URLs:", len(all_urls))
print("evidence rows:", n)
print("MD:", md_path, os.path.getsize(md_path), "bytes")
print("HTML:", html_path, os.path.getsize(html_path), "bytes")
