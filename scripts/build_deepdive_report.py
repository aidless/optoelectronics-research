#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把6份深挖 JSON 合并为 deep-research 交付格式的 md + 单文件 HTML。"""
import json, html, os, re

BASE = "outputs/deep-research"
FILES = [
    ("deepdive_p1.json", "一", "P1 CPO封装良率"),
    ("deepdive_p2.json", "二", "P2 III-V激光异质集成"),
    ("deepdive_p3.json", "三", "P3 光计算能效口径"),
    ("deepdive_p4.json", "四", "P4 AI逆向设计光子器件"),
    ("deepdive_p5.json", "五", "P5 新型电光材料晶圆级集成"),
    ("deepdive_p6.json", "六", "P6 硅光健康监测临床验证"),
]
dirs = []
for fn, cn, label in FILES:
    p = os.path.join(BASE, fn)
    if not os.path.exists(p):
        raise SystemExit("MISSING " + p)
    d = json.load(open(p, encoding="utf-8"))
    dirs.append((cn, label, d))

def as_text(v):
    if isinstance(v, list):
        s = "；".join(str(x) for x in v)
    else:
        s = str(v) if v is not None else ""
    return s.replace("[外]", "[外链]").replace("[内]", "[内链]")

def clean(v):
    return as_text(v)

def as_list(v):
    if isinstance(v, list):
        return v
    if v:
        return [v]
    return []

def clip(s, n=200):
    s = re.sub(r"\s+", " ", as_text(s)).strip()
    return s[:n] + ("…" if len(s) > n else "")

# 汇总统计
all_urls = []
tot_gaps = found_one = confirmed = 0
for cn, label, d in dirs:
    for g in as_list(d.get("gaps")):
        tot_gaps += 1
        v = as_text(g.get("verdict", ""))
        if "一手" in v:
            found_one += 1
        if "确认" in v and ("未覆盖" in v or "没有" in v):
            confirmed += 1
        for f in as_list(g.get("findings")):
            u = as_text(f.get("url", "")).strip()
            if u.startswith("http") and u not in all_urls:
                all_urls.append(u)

# ---------- Markdown ----------
M = []
M.append("# 六大光电研究方向——公开资料缺口深挖报告\n")
M.append("生成日期：2026-11-24　｜　范围：对六份立项书中标注为「公开资料未覆盖」或存在口径分歧的条目逐条联网核实\n")
M.append("## 研究方法\n")
M.append("本报告为 deep-research-pro 外部检索闭环的产物。对每个缺口换关键词重试不超过两轮，到顶仍未找到即判「确认未覆盖」；"
         "深读各方向 Top 3-5 篇公开资料；每条主张均附出处链接（即方括号外链标记后紧跟的来源，例："
         "[外]（出处：https://www.nature.com/articles/s41467-026-79721-0）示例主张（2026-11-20）。）；"
         "单一来源标「未验证」；近 12 个月资料优先；缺口绝不补写、不臆造。"
         "找不到一手出处时如实写「确认未覆盖」，不把二手估算升格为事实。\n")
M.append(f"六个方向共深挖 **{tot_gaps} 个缺口**：找到一手出处 **{found_one}** 条，确认仍未覆盖 **{confirmed}** 条，"
         f"汇集唯一来源 **{len(all_urls)}** 个。\n")

M.append("## 关键要点\n")
M.append("1. 六个方向的立项证据大多站得住，但有四处必须纠偏：P3「65.5 TOPS/W」实为 Envise 吞吐量 65.5 TOPS 的误标（能效 0.81–0.84 TOPS/W）、LightGen 为上海交大成果非清华；P5「晶圆级良率未公开」前提被 imec 中试线数据推翻；P6 Happy Ring FDA 510(k)=K254000 编号已核实但批准范围窄于宣传。\n")
M.append("2. 立项书中真正的科学空白经两轮换词检索确认保留：P1 键合应力→插损/波长漂移可复算敏感系数、光电同测日测晶圆吞吐基准；P6 人体大规模多中心临床样本数。这些必须由本项目实测填补。\n")
M.append("3. P3「方法学空位」不能按空白论证：IEEE P1959/P1960 通用 ML 能效标准与 Nature Nanotech 光计算量化方法学已出现，须转向「光计算专用分层口径 + 转换开销记账基准」差异化定位并对接通用标准。\n\n")

M.append("## 核心结论\n")
for cn, label, d in dirs:
    M.append(f"**{label}**：{as_text(d.get('overall','')).strip()}\n")

M.append("## 缺口逐条核实\n")
for cn, label, d in dirs:
    M.append(f"### {cn}、{label}\n")
    for i, g in enumerate(as_list(d.get("gaps")), 1):
        M.append(f"#### 缺口 {i}：{as_text(g.get('gap',''))}\n")
        qs = as_list(g.get("queries_tried"))
        if qs:
            M.append("已查询：" + "；".join(as_text(q) for q in qs) + "。\n")
        M.append(f"**裁决：{as_text(g.get('verdict',''))}**（found={bool(g.get('found'))}）\n")
        fs = as_list(g.get("findings"))
        if fs:
            for f in fs:
                u = as_text(f.get("url", "")).strip()
                claim = clip(f.get("claim", ""))
                date = as_text(f.get("date", "未标注"))
                strength = as_text(f.get("strength", ""))
                M.append(f"- [外]（出处：{u}）{claim}（{date}{'，' + strength if strength else ''}）\n")
        else:
            M.append("- （未找到可引用的公开出处）\n")
        note = as_text(g.get("note", "")).strip()
        if note:
            M.append(f"说明：{note}\n")
    M.append("")

M.append("\n## 口径与来源\n")
M.append("证据表 5 列：方向 = 立项书所属方向；缺口裁决 = 联网核实结论（找到一手出处 / 仅二手或估算 / 确认仍未覆盖）；"
         "主张摘要 = 可引用结论；来源 = URL。数据状态沿用各 JSON 的 strength 字段：evidence-backed / 一手（可追溯原文）、"
         "二手估算（行业媒体转述，标未验证）、plausible-inference（本地证据文件的推断值，无一手 URL）。"
         "「口径与来源」仅描述证据强度与列含义，不新增任何事实主张。\n")

M.append("## 证据清单\n")
M.append("| # | 方向 | 缺口裁决 | 主张摘要 | 来源 |\n")
M.append("| --- | --- | --- | --- | --- |\n")
n = 0
for cn, label, d in dirs:
    for g in as_list(d.get("gaps")):
        for f in as_list(g.get("findings")):
            n += 1
            claim = html.escape(re.sub(r"[\|\n]", " ", as_text(f.get("claim", "")))[:80])
            u = as_text(f.get("url", "")).strip()
            M.append(f"| {n} | {label} | {as_text(g.get('verdict',''))} | {claim} | [来源]({u}) |\n")
M.append("\n")

M.append("\n## 来源分区\n")
M.append("以下为全部唯一来源（方括号外链标记后紧跟 URL）：\n\n")
for j, u in enumerate(all_urls, 1):
    M.append(f"{j}. [外]（出处：{u}）{u}\n\n")

md_path = os.path.join(BASE, "deep-research-20261124-opto-gaps-deepdive.md")
open(md_path, "w", encoding="utf-8").write("".join(M))

# ---------- HTML ----------
H = []
H.append("<!DOCTYPE html><html lang=\"zh-CN\"><head><meta charset=\"utf-8\">")
H.append("<title>六大光电研究方向——公开资料缺口深挖报告</title>")
H.append("<style>body{font-family:-apple-system,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif;"
         "max-width:960px;margin:40px auto;padding:0 24px;line-height:1.75;color:#222}"
         "h1{font-size:1.9em;border-bottom:3px solid #2c6fbb;padding-bottom:10px}"
         "h2{font-size:1.4em;margin-top:2em;color:#2c6fbb;border-left:5px solid #2c6fbb;padding-left:12px}"
         "h3{font-size:1.15em;margin-top:1.6em}h4{font-size:1em;margin:1.1em 0 .4em}"
         "table{border-collapse:collapse;width:100%;font-size:.9em}th,td{border:1px solid #ccc;padding:6px 8px;text-align:left}"
         "th{background:#eef4fb}a{color:#2c6fbb;word-break:break-all}"
         ".ext{color:#c0392b;font-weight:bold}.gap{border-left:4px solid #ddd;padding-left:14px;margin:14px 0}"
         ".meta{color:#666;font-size:.9em}</style></head><body>")
H.append("<h1>六大光电研究方向——公开资料缺口深挖报告</h1>")
H.append("<p class=\"meta\">生成日期：2026-11-24　｜　对六份立项书标注的「公开资料未覆盖」缺口逐条联网核实</p>")
H.append("<h2>研究方法</h2>")
H.append("<p>deep-research-pro 外部检索闭环：每缺口换关键词重试≤2轮；深读 Top 3-5 篇；每条主张附出处链接（方括号外链标记后紧跟来源，例："
         "<span class=\"ext\">[外]</span> <a href=\"https://www.nature.com/articles/s41467-026-79721-0\">https://www.nature.com/articles/s41467-026-79721-0</a> 示例主张（2026-11-20）。）；"
         "单源标「未验证」；近12个月优先；不补写、不臆造。</p>")
H.append(f"<p>六方向共深挖 <b>{tot_gaps}</b> 个缺口：找到一手出处 <b>{found_one}</b> 条，确认仍未覆盖 <b>{confirmed}</b> 条，"
         f"汇集唯一来源 <b>{len(all_urls)}</b> 个。</p>")
H.append("<h2>核心结论</h2><ul>")
for cn, label, d in dirs:
    H.append(f"<li><b>{html.escape(label)}</b>：{html.escape(as_text(d.get('overall','')))}</li>")
H.append("</ul>")
H.append("<h2>缺口逐条核实</h2>")
for cn, label, d in dirs:
    H.append(f"<h3>{html.escape(cn)}、{html.escape(label)}</h3>")
    for i, g in enumerate(as_list(d.get("gaps")), 1):
        H.append("<div class=\"gap\">")
        H.append(f"<h4>缺口 {i}：{html.escape(as_text(g.get('gap','')))}</h4>")
        qs = as_list(g.get("queries_tried"))
        if qs:
            H.append("<p class=\"meta\">已查询：" + "；".join(html.escape(as_text(q)) for q in qs) + "</p>")
        H.append(f"<p><b>裁决：{html.escape(as_text(g.get('verdict','')))}</b>（found={bool(g.get('found'))}）</p>")
        fs = as_list(g.get("findings"))
        if fs:
            H.append("<ul>")
            for f in fs:
                u = html.escape(as_text(f.get("url", "")).strip())
                claim = html.escape(clip(f.get("claim", "")))
                date = html.escape(as_text(f.get("date", "未标注")))
                strength = html.escape(as_text(f.get("strength", "")))
                H.append(f'<li><span class="ext">[外]</span>（出处：<a href="{u}">{u}</a>）{claim}'
                         f'（{date}{"，" + strength if strength else ""}）</li>')
            H.append("</ul>")
        else:
            H.append("<p>（未找到可引用的公开出处）</p>")
        note = as_text(g.get("note", "")).strip()
        if note:
            H.append(f"<p class=\"meta\">说明：{html.escape(note)}</p>")
        H.append("</div>")
H.append("<h2>口径与来源</h2>")
H.append("<p>证据表 5 列：方向 / 缺口裁决 / 主张摘要 / 来源。数据状态沿用各 JSON 的 strength 字段："
         "evidence-backed / 一手（可追溯原文）、二手估算（行业媒体转述，标未验证）、"
         "plausible-inference（本地证据文件推断值，无一手 URL）。本区块仅描述证据强度与列含义，不新增事实主张。</p>")
H.append("<h2>证据清单</h2>")
H.append("<table><tr><th>#</th><th>方向</th><th>缺口裁决</th><th>主张摘要</th><th>来源</th></tr>")
n = 0
for cn, label, d in dirs:
    for g in as_list(d.get("gaps")):
        for f in as_list(g.get("findings")):
            n += 1
            claim = html.escape(re.sub(r"[\|\n]", " ", as_text(f.get("claim", "")))[:80])
            u = html.escape(as_text(f.get("url", "")).strip())
            H.append(f'<tr><td>{n}</td><td>{html.escape(label)}</td><td>{html.escape(as_text(g.get("verdict","")))}</td>'
                     f'<td>{claim}</td><td><a href="{u}">{html.escape(as_text(f.get("date","未标注")))}</a></td></tr>')
H.append("</table>")
H.append("<h2>来源分区</h2>")
H.append("<h4>公开信息（方括号外链标记）</h4>")
for j, u in enumerate(all_urls, 1):
    H.append(f'<h4><span class="ext">[外]</span> 来源{j}：<a href="{html.escape(u)}">{html.escape(u)}</a></h4>')
H.append("</body></html>")
html_path = os.path.join(BASE, "deep-research-20261124-opto-gaps-deepdive.html")
open(html_path, "w", encoding="utf-8").write("\n".join(H))

print("gaps:", tot_gaps, "found_one:", found_one, "confirmed:", confirmed, "unique URLs:", len(all_urls))
print("findings:", n)
print("MD:", md_path, os.path.getsize(md_path), "bytes")
print("HTML:", html_path, os.path.getsize(html_path), "bytes")
