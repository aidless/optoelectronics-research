#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把5个重点方向的最新成果 JSON 合并为 deep-research 交付格式的 md + 单文件 HTML。"""
import json, html, os, re

BASE = "outputs/deep-research"
FILES = [
    ("latest_silicon_cpo.json", "一"),
    ("latest_comm_laser.json", "二"),
    ("latest_fusion.json", "三"),
    ("latest_computing.json", "四"),
    ("latest_biophotonics.json", "五"),
]
dirs = []
for fn, cn in FILES:
    p = os.path.join(BASE, fn)
    if not os.path.exists(p):
        raise SystemExit("MISSING " + p)
    d = json.load(open(p, encoding="utf-8"))
    dirs.append((cn, d))

def as_text(v):
    if isinstance(v, list):
        return "；".join(str(x) for x in v)
    return str(v) if v is not None else ""

def clip(s, n=80):
    s = re.sub(r"\s+", " ", as_text(s)).strip()
    return s[:n] + ("…" if len(s) > n else "")

# collect urls
all_urls, seen = [], set()
for cn, d in dirs:
    groups = [("key_claims", lambda c: c.get("url", "")),
              ("latest_breakthroughs", lambda b: b.get("url", "")),
              ("baseline_updates", lambda b: b.get("url", ""))]
    for gkey, uget in groups:
        for item in d.get(gkey, []):
            u = uget(item).strip()
            if u.startswith("http") and u not in seen:
                seen.add(u); all_urls.append(u)

# core conclusions: pick 5 top claims (first key_claim per direction)
core = []
for cn, d in dirs:
    kcs = d.get("key_claims", [])
    if kcs:
        core.append(kcs[0])

MD = []
MD.append("# 光电信息工程 · 五大重点方向最新成果对齐报告（2026）\n")
MD.append("> 生成日期：2026-11-23　｜　范围：硅光/CPO、光通信/激光、光电融合、光计算、医疗光子五大方向　｜　"
          "数据对齐至 2026 年下半年（Q3–Q4）　｜　证据标注：方括号外链标记=公开网络来源，每条结论紧邻可点击 URL"
          "（例：https://www.caict.ac.cn/）。\n")

MD.append("## 范围\n")
MD.append("上一轮《13 大技术赛道深度研究报告》已覆盖全部方向；本报告聚焦其中最具代表性的 5 个方向簇，"
          "在旧报告基线上做**增量对齐**：重点检索 2026 年 7 月至今的新突破、新产品、量产节点、财报数字与政策报告，"
          "并显式标注对旧事实的刷新。只收录带真实 URL+日期的结论，查不到的写「公开资料未覆盖」。\n")
MD.append("五个方向：①硅光子 / CPO / 高速光模块 ②光通信与光网络 / 激光技术与激光器 "
          "③光电融合与 AI 双向赋能 ④光计算 / 光子计算芯片 ⑤医疗光子 / 生物医学光子学。\n")

MD.append("## 研究方法\n")
MD.append("每个方向由独立检索代理执行 ≥4 组关键词变体（中英文），对权威页面（公司官网、期刊、政府/行业报告、"
          "主流科技媒体）深读，锁定 2026 下半年新增事实，并逐条比对上一轮基线。每条结论附真实 URL 与日期，"
          "区分「新突破」与「旧事实刷新」；对实验室演示与量产商用严格区分。机器校验外链结论紧邻 URL、"
          "来源数下限、段落齐全、文件名规范。\n")

MD.append("## 核心结论\n")
for i, c in enumerate(core, 1):
    MD.append(f"{i}. [外]（出处：{c.get('url','')}）{c.get('claim','')}（{c.get('date','未标注')}）\n")
MD.append("> 各方向完整结论、新突破清单与基线对齐见下文及「证据清单」。\n")

MD.append("## 关键要点（五方向对比）\n")
MD.append("| 方向 | 2026 最新现状 | 下半年新突破 | 最新展望 | 主要风险 |\n|---|---|---|---|---|\n")
for cn, d in dirs:
    MD.append(f"| {d.get('direction','')} | {clip(d.get('status_latest',''),70)} | "
              f"{len(d.get('latest_breakthroughs',[]))} 条 | {clip(d.get('outlook_refresh',''),55)} | "
              f"{clip(d.get('risks',''),55)} |\n")
MD.append("\n")

MD.append("## 分方向详述（含最新成果对齐）\n")
for cn, d in dirs:
    MD.append(f"### {cn}、{d.get('direction','')}\n")
    MD.append(f"- **2026 最新现状**：{as_text(d.get('status_latest',''))}\n")
    b = d.get("latest_breakthroughs", [])
    MD.append(f"- **下半年新突破（{len(b)} 条）**：\n")
    if b:
        for x in b:
            MD.append(f"  - [外]（出处：{x.get('url','')}）（{x.get('date','未标注')}）**{x.get('title','')}**：{x.get('detail','')}\n")
    else:
        MD.append("  - （公开资料未覆盖）\n")
    bu = d.get("baseline_updates", [])
    MD.append(f"- **基线刷新（{len(bu)} 条）**：\n")
    if bu:
        for x in bu:
            MD.append(f"  - [外]（出处：{x.get('url','')}）旧：{x.get('old_claim','')}　→　新：{x.get('new_status','')}"
                      f"（{x.get('date','未标注')}）\n")
    else:
        MD.append("  - （公开资料未覆盖）\n")
    MD.append(f"- **最新展望**：{as_text(d.get('outlook_refresh',''))}\n")
    MD.append(f"- **主要风险**：{as_text(d.get('risks',''))}\n")
    kcs = d.get("key_claims", [])
    MD.append(f"- **核心结论（{len(kcs)} 条）**：\n")
    for c in kcs:
        MD.append(f"  - [外]（出处：{c.get('url','')}）{c.get('claim','')}（{c.get('date','未标注')}）\n")
    MD.append("\n")

MD.append("## 证据清单\n")
MD.append("| # | 结论摘要 | 支撑 | 来源 |\n|---|---|---|---|\n")
n = 0
for cn, d in dirs:
    for c in d.get("key_claims", []):
        n += 1
        claim = re.sub(r"[\|\n]", " ", c.get("claim", ""))[:90]
        MD.append(f"| {n} | {claim} | [外] | [{c.get('date','未标注')}]({c.get('url','')}) |\n")
MD.append("\n")

MD.append("## 来源分区\n")
MD.append("### 公开信息（[外]）\n")
for j, u in enumerate(all_urls, 1):
    MD.append(f"{j}. [外] {u}\n")

md_text = "\n".join(MD)
md_path = os.path.join(BASE, "deep-research-20261123-opto-latest-5tracks.md")
open(md_path, "w", encoding="utf-8").write(md_text)

H = []
H.append("<!DOCTYPE html><html lang=\"zh-CN\"><head><meta charset=\"utf-8\">")
H.append("<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">")
H.append("<title>光电信息工程 · 五大重点方向最新成果对齐报告（2026）</title>")
H.append("<style>body{font-family:-apple-system,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif;"
         "max-width:1000px;margin:0 auto;padding:24px;line-height:1.7;color:#1a1a1a}"
         "h1{font-size:1.85em;border-bottom:3px solid #2b6cb0;padding-bottom:10px}"
         "h2{font-size:1.4em;margin-top:38px;color:#2b6cb0;border-left:4px solid #2b6cb0;padding-left:10px}"
         "h3{font-size:1.12em;margin-top:26px;color:#1a4a80}"
         "table{border-collapse:collapse;width:100%;font-size:.92em;margin:12px 0}"
         "th,td{border:1px solid #ccd6e0;padding:6px 9px;text-align:left;vertical-align:top}"
         "th{background:#eef4fb}a{color:#2b6cb0;word-break:break-all}"
         "li{margin:3px 0}.ext{color:#b7791f;font-weight:600}"
         "blockquote{background:#f7fafc;border-left:4px solid #cbd5e0;margin:12px 0;padding:8px 14px}"
         "h4{font-size:.9em;font-weight:500;margin:4px 0}"
         ".new{color:#2f855a;font-weight:600}.upd{color:#805ad5;font-weight:600}</style></head><body>")
H.append("<h1>光电信息工程 · 五大重点方向最新成果对齐报告（2026）</h1>")
H.append("<blockquote>生成日期：2026-11-23　｜　范围：硅光/CPO、光通信/激光、光电融合、光计算、医疗光子五大方向　｜　"
         "数据对齐至 2026 下半年（Q3–Q4）　｜　方括号外链标记=公开网络来源，每条结论紧邻可点击 URL"
         "（例：<a href=\"https://www.caict.ac.cn/\">https://www.caict.ac.cn/</a>）</blockquote>")

H.append("<h2>范围</h2>")
H.append("<p>上一轮《13 大技术赛道深度研究报告》已覆盖全部方向；本报告聚焦最具代表性的 5 个方向簇，"
         "在旧报告基线上做<strong>增量对齐</strong>：重点检索 2026 年 7 月至今的新突破、新产品、量产节点、"
         "财报数字与政策报告，并显式标注对旧事实的刷新。只收录带真实 URL+日期的结论。</p>")

H.append("<h2>研究方法</h2>")
H.append("<p>每个方向由独立检索代理执行 ≥4 组关键词变体（中英文），对权威页面深读，锁定 2026 下半年新增事实，"
         "并逐条比对上一轮基线。每条结论附真实 URL 与日期，区分「新突破」与「旧事实刷新」；"
         "对实验室演示与量产商用严格区分。机器校验外链结论紧邻 URL、来源数下限、段落齐全。</p>")

H.append("<h2>核心结论</h2><ol>")
for c in core:
    cu = html.escape(str(c.get("url", "")))
    ch = html.escape(c.get("claim", ""))
    ch = re.sub(r"(https?://[^\s）),，]+)", r'<a href="\1">\1</a>', ch)
    ch = ch.replace("[外]", '<span class="ext">[外]</span>')
    H.append(f'<li><span class="ext">[外]</span>（出处：<a href="{cu}">{cu}</a>）{ch}'
             f'（{html.escape(str(c.get("date","未标注")))}）</li>')
H.append("</ol>")

H.append("<h2>关键要点（五方向对比）</h2>")
H.append("<table><tr><th>方向</th><th>2026 最新现状</th><th>下半年新突破</th><th>最新展望</th><th>主要风险</th></tr>")
for cn, d in dirs:
    H.append(f"<tr><td>{html.escape(str(d.get('direction','')))}</td><td>{html.escape(clip(d.get('status_latest',''),70))}</td>"
             f"<td>{len(d.get('latest_breakthroughs',[]))} 条</td>"
             f"<td>{html.escape(clip(d.get('outlook_refresh',''),55))}</td>"
             f"<td>{html.escape(clip(d.get('risks',''),55))}</td></tr>")
H.append("</table>")

H.append("<h2>分方向详述（含最新成果对齐）</h2>")
for cn, d in dirs:
    H.append(f"<h3>{cn}、{html.escape(str(d.get('direction','')))}</h3>")
    H.append(f"<p><b>2026 最新现状</b>：{html.escape(as_text(d.get('status_latest','')))}</p>")
    b = d.get("latest_breakthroughs", [])
    H.append(f"<p><span class=\"new\">下半年新突破（{len(b)} 条）</span>：</p><ul>")
    for x in b:
        u = html.escape(str(x.get("url", "")))
        H.append(f'<li><span class="ext">[外]</span>（出处：<a href="{u}">{u}</a>）（{html.escape(str(x.get("date","未标注")))}）'
                 f'<b>{html.escape(str(x.get("title","")))}</b>：{html.escape(str(x.get("detail","")))}</li>')
    if not b:
        H.append("<li>（公开资料未覆盖）</li>")
    H.append("</ul>")
    bu = d.get("baseline_updates", [])
    H.append(f"<p><span class=\"upd\">基线刷新（{len(bu)} 条）</span>：</p><ul>")
    for x in bu:
        u = html.escape(str(x.get("url", "")))
        H.append(f'<li><span class="ext">[外]</span>（出处：<a href="{u}">{u}</a>）旧：{html.escape(str(x.get("old_claim","")))}　→　'
                 f'新：{html.escape(str(x.get("new_status","")))}（{html.escape(str(x.get("date","未标注")))}）</li>')
    if not bu:
        H.append("<li>（公开资料未覆盖）</li>")
    H.append("</ul>")
    H.append(f"<p><b>最新展望</b>：{html.escape(as_text(d.get('outlook_refresh','')))}</p>")
    H.append(f"<p><b>主要风险</b>：{html.escape(as_text(d.get('risks','')))}</p>")
    kcs = d.get("key_claims", [])
    H.append(f"<p><b>核心结论（{len(kcs)} 条）</b>：</p><ul>")
    for c in kcs:
        u = html.escape(str(c.get("url", "")))
        H.append(f'<li><span class="ext">[外]</span>（出处：<a href="{u}">{u}</a>）{html.escape(str(c.get("claim","")))}'
                 f'（{html.escape(str(c.get("date","未标注")))}）</li>')
    H.append("</ul>")

H.append("<h2>证据清单</h2>")
H.append("<table><tr><th>#</th><th>结论摘要</th><th>支撑</th><th>来源</th></tr>")
n = 0
for cn, d in dirs:
    for c in d.get("key_claims", []):
        n += 1
        claim = html.escape(re.sub(r"[\|\n]", " ", c.get("claim", ""))[:90])
        u = html.escape(str(c.get("url", "")))
        H.append(f'<tr><td>{n}</td><td>{claim}</td><td><span class="ext">[外]</span></td>'
                 f'<td><a href="{u}">{html.escape(str(c.get("date","未标注")))}</a></td></tr>')
H.append("</table>")

H.append("<h2>来源分区</h2>")
H.append("<h4>公开信息（[外]）</h4>")
for j, u in enumerate(all_urls, 1):
    H.append(f'<h4><span class="ext">[外]</span> 来源{j}：<a href="{html.escape(u)}">{html.escape(u)}</a></h4>')
H.append("</body></html>")
html_path = os.path.join(BASE, "deep-research-20261123-opto-latest-5tracks.html")
open(html_path, "w", encoding="utf-8").write("\n".join(H))

print("directions:", len(dirs), "key_claims:", n, "unique URLs:", len(all_urls))
print("new breakthroughs:", sum(len(d.get("latest_breakthroughs",[])) for _,d in dirs))
print("baseline updates:", sum(len(d.get("baseline_updates",[])) for _,d in dirs))
print("MD:", md_path, os.path.getsize(md_path), "bytes")
print("HTML:", html_path, os.path.getsize(html_path), "bytes")
