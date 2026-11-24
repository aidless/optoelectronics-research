#!/usr/bin/env python3
"""立项书结构自检：检查6份 proposal.md 的必需章节、证据标记与诚实标注。
用退出码表达：0=全过，1=有缺项。可从工作区任意位置运行（自动定位 proposals 根目录）。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EXPECTED = [
    "p1-cpo-packaging-test",
    "p2-iiiv-laser-integration",
    "p3-optical-computing-benchmark",
    "p4-ai-inverse-design",
    "p5-electrooptic-materials",
    "p6-silicon-photonics-health",
]
# 必需的一级/二级结构锚点（按立项书约定）
REQUIRED_SECTIONS = [
    "摘要", "立项依据", "国内外研究现状", "科学问题", "研究目标",
    "研究内容", "技术路线", "创新点", "可行性", "年度计划",
    "预期成果", "风险", "经费", "参考文献",
]
REQUIRED_APPENDIX = ["research_canon", "evidence_table", "argument_map"]
STRENGTH_MARKS = ["evidence-backed", "plausible-inference", "hypothesis"]

FAILS = []
WARNS = []


def check(path, slug):
    if not os.path.isfile(path):
        FAILS.append(f"[{slug}] 文件缺失：{path}")
        return
    txt = open(path, encoding="utf-8").read()
    if len(txt) < 3000:
        FAILS.append(f"[{slug}] 正文过短 {len(txt)} 字符 (<3000)")
    low = txt.lower()
    for sec in REQUIRED_SECTIONS:
        if sec not in txt:
            FAILS.append(f"[{slug}] 缺章节：{sec}")
    for ap in REQUIRED_APPENDIX:
        if ap.lower() not in low:
            FAILS.append(f"[{slug}] 缺附录：{ap}")
    urls = set(re.findall(r"https?://[^\s)\]>，。；、）]+", txt))
    if len(urls) < 8:
        FAILS.append(f"[{slug}] 唯一URL仅 {len(urls)} 个 (<8)")
    sm = [s for s in STRENGTH_MARKS if s.lower() in low]
    if len(sm) < 2:
        FAILS.append(f"[{slug}] 证据强度标记不足：{sm}")
    if "公开资料未覆盖" not in txt and "PLACEHOLDER" not in txt:
        WARNS.append(f"[{slug}] 未出现任何『公开资料未覆盖』或 [PLACEHOLDER] 诚实标注")
    # 禁止的夸大表述；但若命中处附近是否定语境（不得/不等于/禁止/不能/绝不/无/未），视为正当的禁用声明，不报错
    banned = ["已获批上市", "具有重要的理论和工程意义", "填补国内外空白"]
    negation = ["不得", "不等于", "禁止", "不能", "绝不", "而非", "不宣称", "未宣称", "无"]
    for b in banned:
        for m in re.finditer(re.escape(b), txt):
            ctx = txt[max(0, m.start() - 24):m.start()]
            if not any(n in ctx for n in negation):
                FAILS.append(f"[{slug}] 含禁用夸大表述：{b}")
                break
    print(f"[{slug}] 字符 {len(txt)} / 唯一URL {len(urls)} / 强度标记 {len(sm)}")


for s in EXPECTED:
    check(os.path.join(HERE, s, "proposal.md"), s)

print("\n=== 自检结论 ===")
for w in WARNS:
    print("WARN", w)
for f in FAILS:
    print("FAIL", f)
if FAILS:
    print(f"\n不通过：{len(FAILS)} 项缺项")
    sys.exit(1)
print(f"\n通过：6 份立项书全部满足必需结构（{len(WARNS)} 条 WARN）")
sys.exit(0)
