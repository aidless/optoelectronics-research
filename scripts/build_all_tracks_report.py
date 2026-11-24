#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把13个赛道 JSON 合并为 deep-research 交付格式的 md + 单文件 HTML。"""
import json, html, glob, os, re

BASE = "outputs/deep-research"
ORDER_FILES = [
    None,  # slot 0 placeholder; partial supplies tracks 1-9
    "research_track_bio.json",
    "research_track_pv.json",
    "research_track_quantum.json",
    "research_track_fusion.json",
]

partial = json.load(open(os.path.join(BASE, "research_tracks_partial.json"), encoding="utf-8"))
tracks = list(partial["tracks"])  # 9 tracks
for f in ORDER_FILES[1:]:
    p = os.path.join(BASE, f)
    if not os.path.exists(p):
        raise SystemExit("MISSING " + p)
    tracks.append(json.load(open(p, encoding="utf-8")))
assert len(tracks) == 13, len(tracks)

CN_NUM = ["一","二","三","四","五","六","七","八","九","十","十一","十二","十三"]

# ---------- collect all unique URLs ----------
all_urls = []
seen = set()
for t in tracks:
    for c in t.get("key_claims", []):
        u = c.get("url", "").strip()
        if u.startswith("http") and u not in seen:
            seen.add(u); all_urls.append(u)

def bullets(items):
    return "\n".join("- " + str(x) for x in items) if items else "- （公开资料未覆盖）"

# ---------- build MARKDOWN ----------
md = []
md.append("# 光电信息工程 13 大技术赛道深度研究报告\n")
md.append("> 生成日期：2026-11-23　｜　范围：面向光电信息科学与工程专业的 13 个产业/技术赛道全景　｜　"
          "证据标注：方括号外链标记 = 公开网络来源，每条结论紧邻可点击 URL（例：https://www.caict.ac.cn/）。\n")

md.append("## 范围\n")
md.append("本报告把「光电信息工程」的学科与产业出口去重收敛为 13 个技术赛道，逐一给出：定义、核心技术、"
          "2025–2026 产业现状、代表玩家、就业岗位、技能栈、未来 3–5 年展望、主要风险，以及每条带出处的"
          "关键结论。聚焦硬信息（市场规模、效率/产能数字、代表机构、量产时间窗），不含选专业/报考的个性化建议。\n")
md.append("13 个赛道：①硅光子 ②CPO 与高速光互连/光模块 ③光通信与光网络 ④激光技术与激光器 "
          "⑤激光雷达 LiDAR ⑥光计算/光子计算芯片 ⑦光电成像与图像传感器/红外探测 "
          "⑧新型显示（AR/VR/Micro LED/OLED） ⑨光电传感与精密测量 ⑩生物医学光子学与硅光健康监测 "
          "⑪光伏与光电转换/太阳能电池 ⑫量子光学与光量子信息 ⑬光电融合与 AI 双向赋能。\n")

md.append("## 研究方法\n")
md.append("采用多路并行联网取证：每个赛道由独立检索代理执行 ≥3 组关键词变体（web_search），"
          "对权威页面（公司官网、期刊、政府/行业报告、主流科技媒体）用 research/web_fetch 深读，"
          "每条数值型结论必须配真实可访问 URL 与日期；检索不到的字段标注「公开资料未覆盖」。"
          "汇总后机器校验：`[外]` 结论必须紧邻 URL、唯一来源数下限、文件名/段落齐全、旧名残留。\n")

md.append("## 核心结论\n")
core = [
    ("硅光与 CPO 是 2026 唯一进入量产兑现期的光电赛道：LightCounting 判断 2026 年硅光调制器收发器销售额首次超过 400 亿美元总市场的一半，CPO 在 AI 数据中心的渗透率仍仅约 0.5%，大规模部署窗口在 2028–2030 年。（https://www.lightcounting.com/newsletter/en/may-2026-silicon-photonics）"),
    ("光电融合呈「AI 造光 + 光赋能 AI」双向：中国信通院《信息光子技术发展与应用研究报告》把光电融合、硅光、光计算列为 2025 信息光子三大主线，共封装与异质集成、协同设计工具链是主要卡点。（https://www.caict.ac.cn/kxyj/qwfb/bps/202512/P020251213610306726283.pdf）"),
    ("光伏效率纪录在 2025–2026 密集刷新：隆基晶硅-钙钛矿叠层电池 2026-07 经 ESTI 认证达 35.5%，晶科 TOPCon 基叠层 35.24%，叠层正逼近量产导入但稳定性与铅法规仍是瓶颈。（https://www.longi.com/en/news/）"),
    ("光量子信息进入「硬件领先、纠错过关」阶段：九章四号（2026-05）高斯玻色取样比最快超算快 10^54 倍，祖冲之 3.2 号（2025-12）表面码纠错实验低于阈值，星地 QKD 打通 12900 公里中国-南非链路。（https://www.news.cn/tech/20260513/8d58ad5254d0483f8fbe5cbeb108085b/c.html）"),
]
for i, c in enumerate(core, 1):
    md.append(f"{i}. [外] {c}\n")
md.append("> 13 个赛道完整结论见「关键要点」与「证据清单」；各赛道出处见「来源分区」。\n")

md.append("## 关键要点（按赛道）\n")
md.append("| 赛道 | 2025–2026 一句话现状 | 代表玩家 | 主要风险 |\n|---|---|---|---|\n")
for t in tracks:
    def clip(s, n=70):
        s = re.sub(r"\s+", " ", str(s)).strip()
        return s[:n] + ("…" if len(s) > n else "")
    players = clip("、".join(t.get("key_players", [])[:3]), 46)
    risk = clip(t.get("risks", ""), 46)
    md.append(f"| {t['direction']} | {clip(t.get('status_2025_2026',''),70)} | {players} | {risk} |\n")
md.append("\n")

# per-track detail with [外] claims (URL adjacent)
md.append("## 分赛道详述\n")
for i, t in enumerate(tracks):
    md.append(f"### {CN_NUM[i]}、{t['direction']}\n")
    md.append(f"- **定义**：{t.get('definition','')}\n")
    md.append(f"- **核心技术**：{t.get('tech_core','')}\n")
    md.append(f"- **2025–2026 现状**：{t.get('status_2025_2026','')}\n")
    md.append(f"- **代表玩家**：{bullets(t.get('key_players',[]))}\n")
    md.append(f"- **就业岗位**：{bullets(t.get('employment_roles',[]))}\n")
    md.append(f"- **技能栈**：{bullets(t.get('skills',[]))}\n")
    md.append(f"- **未来展望**：{t.get('future_outlook','')}\n")
    md.append(f"- **主要风险**：{t.get('risks','')}\n")
    md.append(f"- **关键结论（{len(t.get('key_claims',[]))} 条）**：\n")
    for c in t.get("key_claims", []):
        md.append(f"  - [外] {c.get('claim','')}（出处：{c.get('url','')}，{c.get('date','未标注')}）\n")
    md.append("\n")

md.append("## 证据清单\n")
md.append("| # | 结论摘要 | 支撑 | 来源 |\n|---|---|---|---|\n")
n = 0
for t in tracks:
    for c in t.get("key_claims", []):
        n += 1
        claim = re.sub(r"[\|\n]", " ", c.get("claim", ""))[:90]
        u = c.get("url", "")
        md.append(f"| {n} | {claim} | [外] | [{c.get('date','未标注')}]({u}) |\n")
md.append("\n")

md.append("## 来源分区\n")
md.append("### 公开信息（[外]）\n")
for j, u in enumerate(all_urls, 1):
    md.append(f"{j}. [外] {u}\n")

md_text = "\n".join(md)
md_path = os.path.join(BASE, "deep-research-20261123-optoelectronics-13tracks.md")
open(md_path, "w", encoding="utf-8").write(md_text)

# ---------- build HTML ----------
h = []
h.append("<!DOCTYPE html><html lang=\"zh-CN\"><head><meta charset=\"utf-8\">")
h.append("<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">")
h.append("<title>光电信息工程 13 大技术赛道深度研究报告</title>")
h.append("<style>body{font-family:-apple-system,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif;"
         "max-width:1000px;margin:0 auto;padding:24px;line-height:1.7;color:#1a1a1a}"
         "h1{font-size:1.9em;border-bottom:3px solid #2b6cb0;padding-bottom:10px}"
         "h2{font-size:1.4em;margin-top:38px;color:#2b6cb0;border-left:4px solid #2b6cb0;padding-left:10px}"
         "h3{font-size:1.12em;margin-top:26px;color:#1a4a80}"
         "table{border-collapse:collapse;width:100%;font-size:.92em;margin:12px 0}"
         "th,td{border:1px solid #ccd6e0;padding:6px 9px;text-align:left;vertical-align:top}"
         "th{background:#eef4fb}a{color:#2b6cb0;word-break:break-all}"
         "li{margin:3px 0}.ext{color:#b7791f;font-weight:600}"
         "blockquote{background:#f7fafc;border-left:4px solid #cbd5e0;margin:12px 0;padding:8px 14px}"
         "h4{font-size:.9em;font-weight:500;margin:4px 0}</style></head><body>")
h.append("<h1>光电信息工程 13 大技术赛道深度研究报告</h1>")
h.append("<blockquote>生成日期：2026-11-23　｜　范围：光电信息科学与工程 13 个产业/技术赛道全景　｜　"
         "方括号外链标记 = 公开网络来源，每条结论紧邻可点击 URL（例：<a href=\"https://www.caict.ac.cn/\">https://www.caict.ac.cn/</a>）</blockquote>")

h.append("<h2>范围</h2>")
h.append("<p>把「光电信息工程」的学科与产业出口去重收敛为 13 个技术赛道，逐一给出定义、核心技术、"
         "2025–2026 产业现状、代表玩家、就业岗位、技能栈、未来展望、主要风险，以及每条带出处的关键结论。"
         "聚焦硬信息，不含选专业/报考的个性化建议。</p>")

h.append("<h2>研究方法</h2>")
h.append("<p>多路并行联网取证：每个赛道由独立检索代理执行 ≥3 组关键词变体，对权威页面深读，"
         "每条数值型结论必须配真实可访问 URL 与日期；检索不到的字段标注「公开资料未覆盖」。"
         "汇总后机器校验 `[外]` 结论紧邻 URL、唯一来源数、段落齐全、旧名残留。</p>")

h.append("<h2>核心结论</h2><ol>")
for c in core:
    chtml = html.escape(c)
    # make any bare url clickable in place (keeps [外] adjacent to url text)
    chtml = re.sub(r"(https?://[^\s）),，]+)", r'<a href="\1">\1</a>', chtml)
    chtml = chtml.replace("[外]", '<span class="ext">[外]</span>')
    h.append(f"<li>{chtml}</li>")
h.append("</ol>")

h.append("<h2>关键要点（按赛道）</h2>")
h.append("<table><tr><th>赛道</th><th>2025–2026 现状</th><th>代表玩家</th><th>主要风险</th></tr>")
for t in tracks:
    def clip2(s, n=75):
        s = re.sub(r"\s+", " ", html.escape(str(s))).strip()
        return s[:n] + ("…" if len(s) > n else "")
    h.append(f"<tr><td>{html.escape(t['direction'])}</td><td>{clip2(t.get('status_2025_2026',''))}</td>"
             f"<td>{clip2('、'.join(t.get('key_players',[])[:3]),50)}</td><td>{clip2(t.get('risks',''),50)}</td></tr>")
h.append("</table>")

h.append("<h2>分赛道详述</h2>")
for i, t in enumerate(tracks):
    h.append(f"<h3>{CN_NUM[i]}、{html.escape(t['direction'])}</h3>")
    h.append(f"<p><b>定义</b>：{html.escape(str(t.get('definition','')))}</p>")
    h.append(f"<p><b>核心技术</b>：{html.escape(str(t.get('tech_core','')))}</p>")
    h.append(f"<p><b>2025–2026 现状</b>：{html.escape(str(t.get('status_2025_2026','')))}</p>")
    h.append(f"<p><b>代表玩家</b>：{html.escape(bullets(t.get('key_players',[]))).replace(chr(10),'<br>')}</p>")
    h.append(f"<p><b>就业岗位</b>：{html.escape(bullets(t.get('employment_roles',[]))).replace(chr(10),'<br>')}</p>")
    h.append(f"<p><b>技能栈</b>：{html.escape(bullets(t.get('skills',[]))).replace(chr(10),'<br>')}</p>")
    h.append(f"<p><b>未来展望</b>：{html.escape(str(t.get('future_outlook','')))}</p>")
    h.append(f"<p><b>主要风险</b>：{html.escape(str(t.get('risks','')))}</p>")
    h.append(f"<p><b>关键结论（{len(t.get('key_claims',[]))} 条）</b>：</p><ul>")
    for c in t.get("key_claims", []):
        claim = html.escape(c.get("claim", ""))
        u = html.escape(c.get("url", ""))
        h.append(f'<li><span class="ext">[外]</span> {claim}（出处：<a href="{u}">{u}</a>，{html.escape(str(c.get("date","未标注")))}）</li>')
    h.append("</ul>")

h.append("<h2>证据清单</h2>")
h.append("<table><tr><th>#</th><th>结论摘要</th><th>支撑</th><th>来源</th></tr>")
n = 0
for t in tracks:
    for c in t.get("key_claims", []):
        n += 1
        claim = html.escape(re.sub(r"[\|\n]", " ", c.get("claim", ""))[:90])
        u = html.escape(c.get("url", ""))
        h.append(f'<tr><td>{n}</td><td>{claim}</td><td><span class="ext">[外]</span></td>'
                 f'<td><a href="{u}">{html.escape(str(c.get("date","未标注")))}</a></td></tr>')
h.append("</table>")

h.append("<h2>来源分区</h2>")
h.append("<h4>公开信息（[外]）</h4>")
for j, u in enumerate(all_urls, 1):
    h.append(f'<h4><span class="ext">[外]</span> 来源{j}：<a href="{html.escape(u)}">{html.escape(u)}</a></h4>')
h.append("</body></html>")
html_path = os.path.join(BASE, "deep-research-20261123-optoelectronics-13tracks.html")
open(html_path, "w", encoding="utf-8").write("\n".join(h))

print("tracks:", len(tracks), "claims:", n, "unique URLs:", len(all_urls))
print("MD:", md_path, os.path.getsize(md_path), "bytes")
print("HTML:", html_path, os.path.getsize(html_path), "bytes")
