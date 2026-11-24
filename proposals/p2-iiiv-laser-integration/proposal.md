# 项目名称

**面向 CPO/NPO 光源的 III-V 族激光器硅基异质集成：界面缺陷—耦合效率—可靠性协同判据研究**

（方向级开题报告，研究周期 4 年；调研证据截至 2026 年 11 月）

---

# 摘要（约 300 字）

硅的间接带隙使其难以高效发光，片上光源因而成为硅光与共封装光学（CPO）/近封装光学（NPO）绕不开的卡口。产业侧，200G 以上高速激光芯片高端产能约 90% 集中于住友电工、JX 金属、AXT、Coherent 四家（[证据来源](../../deep-research/research_tracks_partial.json)，该条未附独立 URL）；InP 激光器 2025 年占光芯片市场 58%，机构预测 2031 年仍占 46%、约 69 亿美元（[LightCounting, 2026-05](https://www.lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377)）。形态演进并未削弱光源地位：Lambda 在 SC26 披露的 Quantum-X CPO 交换机使用 18 个可现场更换外部激光源（ELS）（[CAS RAI, 2026-11-16](https://casrai.org/news/lambda-nvidia-photonics-co-packaged-optics-sc26-2026)），中际旭创基于 Tower PH18M 工艺的 NPO 器件已进入早期量产（[OpenPR, 2026-11-03](https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries)）。本项目聚焦 III-V 族激光器硅基异质集成，围绕界面缺陷、光耦合效率与器件可靠性三者的相互制约，建立"路径比较—缺陷机理—耦合容差—可靠性判据"研究框架，设 1 个中心问题与 3 个可检验子目标，输出可测的 Go/No-Go 判据与多目标对照矩阵。定位为方向级开题，不写操作级工艺细则；无公开证据的指标一律标注"目标值"。

**关键词**：III-V 族激光器；硅基异质集成；界面缺陷密度；光耦合效率；器件可靠性；CPO/NPO；外部激光源（ELS）

---

# 一、立项依据与意义

**（1）根问题在材料，不在封装。** 硅光子学的产业叙事已从"速率升级"转向"系统集成"，但物理底层未变：硅是间接带隙材料，难以高效发光，片上光源必须借助 III-V 族材料异质集成（[研究赛道证据, research_tracks_partial.json](../../deep-research/research_tracks_partial.json)，硅光子 tech_core 字段）。这意味着无论 CPO/NPO 形态如何演进，激光器的产生与集成环节都无法被硅光工艺本身消解。

**（2）市场结构放大了供给风险。** LightCounting 测算，用于收发器/AOC/LPO/LRO/NPO/CPO 的光芯片市场 2025 年约 40 亿美元，机构预测 2031 年增至约 150 亿美元；其中 InP 激光器（含 CW 激光、EML）2025 年占 58%，2031 年仍占 46%（约 69 亿美元），为最大细分（[LightCounting, 2026-05](https://www.lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377)）。更集中的是上游产能：200G 以上高速激光芯片依赖 InP 衬底，全球高端产能约 90% 集中于住友电工、JX 金属、AXT、Coherent 四家（[研究赛道证据](../../deep-research/research_tracks_partial.json)，硅光子 risks 字段）。另一口径显示高端约 90% 产能由 Lumentum/Coherent/博通把持、订单排至 2027 年底（[产业动态汇总, 2026 下半年](../../deep-research/latest_comm_laser.json)，status_latest 字段）——两个口径的机构构成不同，均指向单点依赖，本立项不合并引用其机构名单。

**（3）异质集成光源是 CPO/NPO 的关键卡位，且需求是"拉动"而非"替代"。** 材料侧的判断是：InP 激光在 2031 年仍占光芯片 46%，硅光不取代 InP 激光，反而拉动 CW 激光需求（[产业动态汇总, latest_silicon_cpo.json](../../deep-research/latest_silicon_cpo.json)，outlook_refresh 字段）。工程侧的证据是：Lambda 的 Quantum-X Photonics 交换机以 144×800Gb/s 端口（115.2 Tb/s 无阻塞）配置 18 个可现场更换 ELS，光引擎中位运行温度 36°C（可插拔方案 51°C）、组件可靠性最多提升 15 倍（[CAS RAI, 2026-11-16](https://casrai.org/news/lambda-nvidia-photonics-co-packaged-optics-sc26-2026)）；中际旭创基于 Tower PH18M 工艺的首款 NPO 器件已在其加州工厂进入早期量产（[OpenPR, 2026-11-03](https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries)）。两条路线同时把"光源如何集成进硅基"推到前台。

**（4）瓶颈已被产业界点名，但公共证据不足以支撑优化承诺。** TrendForce 将"光引擎（激光+调制器集成、良率与散热）"列为 CPO 三大放量瓶颈之一（[Chiplet Marketplace 转载, 2026-07-29](https://chiplet-marketplace.com/insights/news/nvidia-broadcom-cpo-switches)）；ResearchAndMarkets 指出异构集成推高成本、良率、散热压力，测试/标准/互操作仍处早期（[GlobeNewswire, 2026-11-19](https://www.globenewswire.com/news-release/2026/11/19/3406896/28124/en/co-packaged-optics-cpo-market-analysis-and-forecast-2026-2036-ai-data-center-demand-drives-32-4-cagr-creating-a-20-4-billion-market-by-2036.html)）。但"量产良率/单位成本"的权威硬数字、异质集成激光器的界面缺陷密度—寿命定量关系，公开资料未覆盖。因此本项目把承诺定位在"建立判据与对照框架"而非"给出最优工艺窗口"。

**意义边界**：本立项的贡献对象是异质集成光源的**评价方法与判据**，不是激光芯片产能本身，也不承诺替代现有 InP 供应体系。

---

# 二、国内外研究现状与缺口

按证据强度分三档陈述；"未覆盖"严格按公开资料可得性标注。

## 2.1 已量产 / 已进入供货

| 主体 | 进展 | 证据 |
|---|---|---|
| NVIDIA | Spectrum-X Ethernet Photonics 于 2026-08 宣布全面量产；与 TSMC 联合开发、COUPE 封装、400 Tb/s（[NVIDIA 官方发布, 2026-08-12](https://www.youtube.com/watch?v=CNM6Mmqrfeg)；[TrendForce 转载, 2026-07-29](https://chiplet-marketplace.com/insights/news/nvidia-broadcom-cpo-switches)） | 官方 + 机构 |
| Broadcom | 51.2T Bailly CPO 持续小量出货并进入量产，Meta 等完成部署验证（[TrendForce 转载, 2026-07-29](https://chiplet-marketplace.com/insights/news/nvidia-broadcom-cpo-switches)） | 机构 |
| Tower + 中际旭创 | 基于 Tower PH18M（200mm）工艺的首款 NPO 器件在加州工厂进入 early production，另有产品在 300mm 平台流片（[OpenPR, 2026-11-03](https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries)） | 企业公告 |
| 源杰科技 | 大功率 CW 70mW 已大批量出货、100mW 批量交付；2026-11-13 获 17.44 亿元大功率激光器芯片订单（[818 Laser Hub, 2026-11-13](https://www.818laserhub.cn/newsinfo/11396403.html)） | 企业公告 |
| 天孚通信 | CPO 配套产品已进入批量交付阶段，预计 2027 起逐步提量（[新浪财经, 2026-11-18](https://finance.sina.com.cn/roll/2026-11-18/doc-inizensx6831692.shtml)） | 企业公告 |

## 2.2 实验室 / 验证 / 早期部署

- **Lambda + NVIDIA**：SC26 披露 Quantum-X CPO 在魁北克 1 万余张 Blackwell Ultra GPU 集群投产，18 个可现场更换 ELS；相对可插拔，机架级延迟降 3.8%、Pod 级最多降 10.1%（[CAS RAI, 2026-11-16](https://casrai.org/news/lambda-nvidia-photonics-co-packaged-optics-sc26-2026)）。ELS 形态验证，异质集成片上光源形态未见同等规模披露。
- **光迅科技**：3.2T 硅光单模 NPO 在头部云服务商完成验证，并推出 6.4T NPO 与 12.8T XPO（[36Kr, 2026-09-09](https://eu.36kr.com/zh/p/4001118301425796)）。
- **京瓷 + 东北大学**：激光退火把光隔离器直接集成到硅光芯片，背向反射减少约 95%（[OpenPR, 2026-10-01](https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries)）。属无源器件集成工艺突破，与 III-V 光源集成互补。
- **NLM Photonics + SilOriX**：签 JDA 推进硅-有机混合调制器与电光材料（[OpenPR, 2026-09-21](https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries)）。
- **GlobalFoundries**：获美商务部约 3 亿美元 CHIPS 研发意向，聚焦先进光学材料、晶圆技术与 3D 混合键合以支持 NPO/CPO（[OpenPR, 2026-07-01](https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries)）。
- **源杰科技**：面向 CPO/NPO 的 300mW 大功率激光器仍在研发推进中（[818 Laser Hub, 2026-11-13](https://www.818laserhub.cn/newsinfo/11396403.html)）。

## 2.3 公开资料未覆盖 / 证据不足

- 2026Q3/Q4 CPO 量产的良率与单位成本权威硬数字——公开资料未覆盖；可见者多为机构估算或自媒体口径，不予采信（[产业动态汇总, latest_silicon_cpo.json](../../deep-research/latest_silicon_cpo.json)，uncovered 字段）。
- 异质集成 III-V 激光器在硅基上的界面缺陷密度与阈值电流、老化退化率的定量关系——公开资料未覆盖。
- 台积电 COUPE 2026 下半年具体产能晶圆片数——公开资料未覆盖；薄膜铌酸锂 CPO 3.2T 实测商用数据——公开资料未覆盖（同上，uncovered 字段）。
- CPO 在 AI 数据中心光模块的精确渗透率百分比更新——机构仅给定性"跨入量产"与端口预测，未披露精确口径（同上，uncovered 字段）。

## 2.4 缺口归纳

现有公开证据把"光源供给集中""CPO/NPO 形态卡位""光引擎良率瓶颈"三条线索分别坐实，但没有一条把**界面缺陷—耦合效率—可靠性**三者放进同一个可测框架。国外以大厂垂直整合（TSMC COUPE、GF+AMF、Tower PH18M）推进；国内在光模块与 NPO 器件环节卡位，异质集成光源的方法学层面公开证据有限。这正是本立项的切入位置。

---

# 三、关键科学问题与研究目标

## 3.1 中心问题

**在硅基平台上异质集成 III-V 激光器时，界面缺陷密度、光耦合效率与器件可靠性三者如何相互制约，能否用一组可测指标把它们约束到同时满足 CPO/NPO 光源工程门槛的操作窗口内？**

该问题可证伪：若实验表明三者无法在同一窗口内同时达标，则结论为"需要分离 ELS 与片上集成两种形态分别优化"，而非强行给出统一最优解。

## 3.2 三个可检验子目标

| 编号 | 子目标 | 可检验形式 | 承诺等级 |
|---|---|---|---|
| G1 | 建立异质集成路径的多目标比较框架 | 输出晶圆键合、异质外延、芯片级贴装三路径在界面缺陷密度、耦合效率、成本、可扩展性四维的量化对照矩阵；各维度给出量纲、测试方法与数据缺口标注 | 可交付主线 |
| G2 | 厘清界面缺陷密度与阈值电流、可靠性退化的关系 | 给出缺陷密度—阈值电流、缺陷密度—加速老化退化率的两组拟合关系及置信区间；若数据不支持单调关系，如实报告 | 审慎探索 |
| G3 | 建立耦合效率—对准容差的量化模型并给出 CPO/NPO 链路预算窗口 | 输出耦合效率随横向/角向对准偏差的曲面，以及满足既定链路插损预算的容差窗口；窗口上下界标为目标值 | 边界确认 |

**降承诺说明**：G1 有充分文献与产业线索支撑（[OpenPR, 2026-11-03](https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries) 证实多工艺平台并存），列为主线；G2 缺少目标体系下的公开定量关系，降为审慎探索，并预设 Go/No-Go 判据；G3 只回答"能不能达到预算窗口"，不追求效率极值。

---

# 四、研究内容

## 子课题 1：异质集成路径比较与界面缺陷表征框架（对应 G1）

- **问题**：键合、外延、贴装三条路径在硅基上引入的界面缺陷类型与密度量级不同，公开资料未给出同口径对照。
- **方法**：建立统一的表征口径（缺陷密度 Saxon/单位面积、位错与层错分类、界面粗糙度），对三条路径的文献数据与自测样本做同口径归一；对缺失口径明确标注而非插补。
- **可测输出指标**：三路径 × 四维对照矩阵 1 份；缺陷密度表征方法清单 ≥ 3 项；每个指标附量纲、测试条件与证据等级。
- **边界**：不评价具体代工厂工艺优劣，只评价路径层面的可测差异。

## 子课题 2：界面缺陷—阈值电流—可靠性耦合机理（对应 G2）

- **问题**：缺陷是只抬高阈值电流，还是同时加速工作退化？两者能否解耦？
- **方法**：在缺陷密度梯度样本上测阈值电流与自发辐射效率；做加速老化（高温/大电流应力），提取退化率与加速因子；用统计模型区分缺陷贡献与其他退化通道。
- **可测输出指标**：缺陷密度—阈值电流拟合关系 1 组；缺陷密度—老化退化率拟合关系 1 组；加速因子估计值（目标值）；关系显著性检验结果（含"不显著"的如实报告）。
- **Go/No-Go**：若两组关系均不显著或在应力区间内被其他通道主导，则终止机理归因，退回"仅做缺陷密度—阈值统计相关"的保守结论。

## 子课题 3：光耦合效率与对准容差建模（对应 G3）

- **问题**：异质集成光源到硅波导的耦合效率对准偏差敏感，需要一个能对接链路预算的容差模型。
- **方法**：建立耦合效率对横向、纵向、角向偏差的响应曲面；结合倒锥/光栅耦合等方向的既有器件知识（方向级，不写版图）；以 ELS 与片上集成两种形态分别设定插损预算。
- **可测输出指标**：耦合效率—对准偏差曲面 1 套；满足插损预算的容差窗口上下界（目标值）；两种形态的窗口对照表 1 份。

## 子课题 4：面向 CPO/NPO 两种形态的判据集成（对应 G1–G3）

- **问题**：ELS（可现场更换）与片上集成对可靠性、耦合、可维护性的权重不同，需要分别成判据。
- **方法**：把子课题 1–3 的指标汇总为判据集，按形态设定权重；以产业已披露的 ELS 规模部署（[CAS RAI, 2026-11-16](https://casrai.org/news/lambda-nvidia-photonics-co-packaged-optics-sc26-2026)）与 NPO 早期量产（[OpenPR, 2026-11-03](https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries)）作为现实锚点校验判据合理性。
- **可测输出指标**：ELS 形态与片上集成形态各 1 套 Go/No-Go 判据；判据—指标映射表 1 份；判据未覆盖项清单。

---

# 五、技术路线与实验方案（方向级）

## 5.1 异质集成路径比较

三路径并列评估，不预设赢家：

1. **晶圆级键合**：III-V 外延片与硅晶圆键合后减薄/去除原衬底。优点是对准由光刻定义、可扩展到晶圆级；风险是界面缺陷与应力。
2. **异质外延**：直接在硅上生长 III-V。优点是工艺集成度潜在最高；风险是晶格失配导致的位错密度，公开资料未给出目标体系的成熟对照数据。
3. **芯片级贴装 / 微转移打印**：将预制 III-V 激光芯片转移到硅光晶圆。优点是先用成熟芯片、解耦光源与硅光工艺；风险是贴装精度与吞吐。

比较维度统一为：界面缺陷密度、耦合效率、成本结构、可扩展性、与 CPO/NPO 形态的适配度。每维度标注证据等级，缺口写"公开资料未覆盖"。

## 5.2 可靠性测试（方向级）

- 以加速老化获取退化率，用温度/电流两类应力提取加速因子；不写具体温度点、时长与设备型号（属执行级 SOP，留待实验前计划）。
- 判据化的核心量：退化率斜率、加速因子、失效分布形态；与 ELS 可现场更换形态的可靠性指标（[CAS RAI, 2026-11-16](https://casrai.org/news/lambda-nvidia-photonics-co-packaged-optics-sc26-2026) 披露组件可靠性最多提升 15 倍、光引擎温度 36°C vs 51°C）做量级对照，不直接等同。
- 反向检查：若可靠性优势主要来自"可更换"这一系统架构而非器件本身，须在结论中分离系统级与器件级贡献。

## 5.3 耦合效率测试（方向级）

- 以插损为统一量纲，扫描横向/纵向/角向对准偏差，拟合响应曲面；分别设定 ELS 与片上集成的插损预算。
- 参考产业侧已公开的耦合相关瓶颈：FAU 保偏光纤对位精度与产能是光引擎规模化交付的约束（[研究赛道证据](../../deep-research/research_tracks_partial.json)，硅光子 risks 字段）；本项目只建模容差窗口，不展开 FAU 工艺。

## 5.4 总体流程

证据梳理与 canon 固化 → 路径比较矩阵（G1） → 缺陷与阈值/退化关系（G2，含 Go/No-Go） → 耦合容差窗口（G3） → 两形态判据集成 → 结题评审。G2 未通过判据时，路线切换到保守统计相关结论，不影响 G1/G3/G4 交付。

---

# 六、创新点（可检验）

1. **缺陷密度—阈值电流—可靠性三者联动的可测判据**。可检验形式：给出两组拟合关系及其置信区间，并明确"三者能否同时达标"的二元结论；区别于只优化单一指标的常规做法。现有公开资料未给出该体系的定量关系，属方法学新增。
2. **面向 ELS 与片上集成两种形态的统一耦合—可靠性评估框架**。可检验形式：同一套指标在两种形态下的对照表，且各自给出 Go/No-Go 判据；锚点是产业已分别披露 ELS 规模部署（[CAS RAI, 2026-11-16](https://casrai.org/news/lambda-nvidia-photonics-co-packaged-optics-sc26-2026)）与 NPO 早期量产（[OpenPR, 2026-11-03](https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries)），但未见把两者放进同一判据框架。
3. **异质集成路径的多目标对照矩阵与判据阈值**。可检验形式：三路径 × 四维矩阵，每格带量纲、测试方法与证据等级，判据阈值明确标注"目标值"；可复核、可逐格证伪，不含"显著提高""填补空白"类表述。

---

# 七、可行性与已有基础

- **平台与设备**：[PLACEHOLDER]（硅光流片/键合/外延/贴装可用的工艺平台、PDK 版本与访问方式）
- **测试能力**：[PLACEHOLDER]（阈值/老化/耦合测试设备、光电同测与可靠性试验条件）
- **样本与材料来源**：[PLACEHOLDER]（III-V 外延片/芯片与硅光晶圆的获取渠道）
- **团队基础**：[PLACEHOLDER]（异质集成、器件物理、可靠性统计方向的人员与既往成果）
- **数据与算力**：[PLACEHOLDER]（拟合与曲面建模所需的数据管理与计算环境）

**可行性判据**：上述 [PLACEHOLDER] 项在开题后 3 个月内落实；若键合/外延平台不可得，则 G2 退回文献数据同口径归一 + 保守统计相关，项目仍可交付 G1/G3/G4。证据侧的产业锚点已具备：CPO/NPO 量产与部署节点有公开披露（[TrendForce 转载, 2026-07-29](https://chiplet-marketplace.com/insights/news/nvidia-broadcom-cpo-switches)；[OpenPR, 2026-11-03](https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries)）。

---

# 八、年度计划（4 年，分阶段）

| 年度 | 阶段目标 | 主要工作 | 交付物 |
|---|---|---|---|
| 第 1 年 | 证据固化与路径框架 | 建立 research_canon/evidence_table；确定三路径表征口径；完成路径对照矩阵 v1 | 路径对照矩阵 v1；证据台账 1 套；开题论证报告 |
| 第 2 年 | 缺陷机理探索 | 缺陷密度梯度样本表征；阈值电流测量；加速老化方案设计；执行首次 Go/No-Go | 缺陷—阈值拟合关系；可靠性测试方案；Go/No-Go 记录 |
| 第 3 年 | 耦合容差与可靠性建模 | 耦合效率响应曲面；对准容差窗口；退化率与加速因子估计 | 耦合容差曲面 1 套；退化率/加速因子报告 |
| 第 4 年 | 判据集成与结题 | 两形态判据集成；判据合理性校验；结题评审 | ELS/片上集成判据集；结题报告；可复核数据表 |

每年度末设置一次内部复核；G2 的 Go/No-Go 在第 2 年末执行，未通过则切换保守路线。

---

# 九、预期成果（指标可测）

| 类别 | 成果 | 指标 / 口径 | 证据属性 |
|---|---|---|---|
| 方法 | 异质集成路径多目标对照矩阵 | 3 路径 × 4 维度，每格含量纲/测试方法/证据等级 | 可交付 |
| 数据 | 缺陷密度—阈值电流拟合关系 | ≥ 1 组，附置信区间与显著性检验 | 可交付；关系显著性为目标值 |
| 数据 | 缺陷密度—老化退化率拟合关系 | ≥ 1 组；若不显著则如实报告 | 审慎探索 |
| 模型 | 耦合效率—对准偏差响应曲面 | 三偏差方向的曲面 1 套 + 容差窗口上下界 | 窗口数值为目标值 |
| 判据 | ELS / 片上集成 Go/No-Go 判据集 | 各 1 套，判据—指标映射完整 | 可交付 |
| 展望对照 | 产业端口与市场规模 | 光芯片市场 2031 约 150 亿美元、InP 激光 2031 占 46%（约 69 亿美元） | 机构预测（[LightCounting, 2026-05](https://www.lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377)），非本项目产出 |

**不承诺项**：不承诺具体量产良率、单位成本、绝对耦合效率极值——这些量的权威基线在公开资料中未覆盖，任何数值只能标"目标值"。

---

# 十、风险与对策（≥3 条，含备选路线）

| # | 风险 | 触发信号 | 对策 / 备选路线 |
|---|---|---|---|
| R1 | 键合/外延平台不可得 | 开题 3 个月内 [PLACEHOLDER] 未落实 | 主线改为"文献数据同口径归一 + 芯片级贴装样本自测"；G2 降为统计相关，不做事理归因 |
| R2 | 缺陷—退化关系不显著或被其他通道主导 | 显著性检验不通过 | 执行 Go/No-Go：终止机理归因，退回保守统计结论；判据集改用缺陷—阈值单变量版本 |
| R3 | 路线替代风险：ELS 与片上集成权重变化 | CPO 全面以可更换 ELS 为主、片上集成需求后移 | 判据集按形态分离，允许只交付 ELS 形态判据；锚点参考 ELS 规模部署（[CAS RAI, 2026-11-16](https://casrai.org/news/lambda-nvidia-photonics-co-packaged-optics-sc26-2026)）与 NPO 量产（[OpenPR, 2026-11-03](https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries)） |
| R4 | 供给与材料约束 | InP 衬底短缺延续、6 英寸片涨价（[产业动态汇总, risks](../../deep-research/latest_comm_laser.json)） | 样本来源多渠道并行；把"材料可获得性"列为对照矩阵第五维，避免单路径依赖 |
| R5 | 数据口径不可比 | 不同来源良率/份额口径分歧（如 1.6T 出货预测 860 万至 7140 万只，[36Kr, 2026-09-07](https://eu.36kr.com/zh/p/4001118301425796)） | 统一量纲与口径后再比较；无法归一的数据标"公开资料未覆盖"，不插补、不混用 |
| R6 | 异构集成成本/散热/标准不确定性 | CPO 测试与互操作标准仍处早期（[GlobeNewswire, 2026-11-19](https://www.globenewswire.com/news-release/2026/11/19/3406896/28124/en/co-packaged-optics-cpo-market-analysis-and-forecast-2026-2036-ai-data-center-demand-drives-32-4-cagr-creating-a-20-4-billion-market-by-2036.html)） | 判据只覆盖器件级可测量；系统级成本/散热作为边界条件单列，不纳入量化承诺 |

---

# 十一、经费与条件概要

- 经费总额：[PLACEHOLDER]（万元）
- 设备/测试平台使用费：[PLACEHOLDER]
- 材料与流片/键合费用：[PLACEHOLDER]
- 人员与数据中心：[PLACEHOLDER]
- 合作单位与分工：[PLACEHOLDER]
- 条件缺口与补足方式：[PLACEHOLDER]

---

# 参考文献（每条含真实 URL 与日期）

1. LightCounting. *Silicon Photonics, LPO/LRO and NPO/CPO*, 2026-05. https://www.lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377
2. CAS RAI. *Lambda / NVIDIA Photonics CPO at SC26*, 2026-11-16. https://casrai.org/news/lambda-nvidia-photonics-co-packaged-optics-sc26-2026
3. OpenPR. *Silicon Photonics Market Gains Momentum — GlobalFoundries / Tower / Kyocera / NLM*, 2026-11-03（条目日期跨 2026-07 至 2026-11）. https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries
4. 818 Laser Hub. *源杰科技获 17.44 亿元大功率激光器芯片订单*, 2026-11-13. https://www.818laserhub.cn/newsinfo/11396403.html
5. GlobeNewswire / ResearchAndMarkets. *Co-Packaged Optics Market Analysis and Forecast 2026–2036*, 2026-11-19. https://www.globenewswire.com/news-release/2026/11/19/3406896/28124/en/co-packaged-optics-cpo-market-analysis-and-forecast-2026-2036-ai-data-center-demand-drives-32-4-cagr-creating-a-20-4-billion-market-by-2036.html
6. Chiplet Marketplace（转载 TrendForce）. *NVIDIA / Broadcom CPO Switches Enter Production*, 2026-07-29. https://chiplet-marketplace.com/insights/news/nvidia-broadcom-cpo-switches
7. OIF. *Industry's First Co-Packaging Standard: 3.2T Co-Packaged Module IA*, 2023-04-05. https://www.oiforum.com/oif-launches-the-industrys-first-co-packaging-standard-the-3-2t-co-packaged-module-implementation-agreement/
8. NVIDIA（官方视频发布）. *Spectrum-X Ethernet Photonics Full Production*, 2026-08-12. https://www.youtube.com/watch?v=CNM6Mmqrfeg
9. 36Kr. *CIOE 2026 / 硅光 NPO / 光博会综合*, 2026-09-09. https://eu.36kr.com/zh/p/4001118301425796
10. SimpleTechTrend（转载 LightCounting OCP 2026）. *CPO/NPO Port Forecast*, 2026-10. https://www.simpletechtrend.com/en/post/ocp-2026-lightcounting-cpo-npo-forecast-scenarios-en
11. 新浪财经. *新易盛 1.6T 放量 / 天孚通信 CPO 配套批量交付*, 2026-11-18. https://finance.sina.com.cn/roll/2026-11-18/doc-inizensx6831692.shtml
12. LightCounting. *December 2025 Quarterly Market Update*, 2025-12. https://www.lightcounting.com/newsletter/chinese/december-2025-quarterly-market-update-322
13. 本地证据文件. *latest_comm_laser.json / latest_silicon_cpo.json / research_tracks_partial.json*, generated/compiled 2026-11-23. 相对路径：`outputs/deep-research/`

---

# 附录 A — research_canon（带来源 URL 的硬事实）

| # | 硬事实 | 来源 URL / 文件 | 属性 |
|---|---|---|---|
| A1 | 硅为间接带隙，难高效发光；片上光源需 III-V 异质集成 | `outputs/deep-research/research_tracks_partial.json` 硅光子 tech_core（无独立 URL） | 领域常识 + 赛道证据 |
| A2 | 200G 以上激光芯片高端产能约 90% 集中于住友电工/JX/AXT/Coherent 四家 | `outputs/deep-research/research_tracks_partial.json` 硅光子 risks（无独立 URL；口径见正文"一（2）"） | 赛道证据，未挂 URL |
| A3 | InP 激光 2025 占光芯片 58%，2031 预测仍占 46%（约 69 亿美元） | https://www.lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377 | 机构预测（2031 部分） |
| A4 | 光芯片市场 2025 约 40 亿美元 → 2031 预测约 150 亿美元 | https://www.lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377 | 机构预测（2031 部分） |
| A5 | Lambda Quantum-X CPO 交换机配 18 个可现场更换 ELS，115.2 Tb/s，光引擎 36°C vs 51°C | https://casrai.org/news/lambda-nvidia-photonics-co-packaged-optics-sc26-2026 | 已部署披露 |
| A6 | 中际旭创基于 Tower PH18M 的 NPO 器件进入早期量产 | https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries | 企业公告 |
| A7 | 光引擎（激光+调制器集成、良率、散热）为 CPO 放量瓶颈之一 | https://chiplet-marketplace.com/insights/news/nvidia-broadcom-cpo-switches | 机构判断 |
| A8 | 源杰大功率 CW 70mW 大批量出货、100mW 批量交付；300mW 研发中 | https://www.818laserhub.cn/newsinfo/11396403.html | 企业公告 |
| A9 | OIF 于 2023-04-05 发布首个 3.2T CPO 实施协议，2025 推进 ELSFP | https://www.oiforum.com/oif-launches-the-industrys-first-co-packaging-standard-the-3-2t-co-packaged-module-implementation-agreement/ | 标准事实 |
| A10 | 异构集成推高成本/良率/散热，测试与标准仍处早期 | https://www.globenewswire.com/news-release/2026/11/19/3406896/28124/en/co-packaged-optics-cpo-market-analysis-and-forecast-2026-2036-ai-data-center-demand-drives-32-4-cagr-creating-a-20-4-billion-market-by-2036.html | 机构判断 |
| A11 | CPO 端口预测：2027 约 450 万 → 2031 约 1.89 亿（NPO+CPO 合计） | https://www.simpletechtrend.com/en/post/ocp-2026-lightcounting-cpo-npo-forecast-scenarios-en | 机构预测 |

**禁用声明（canon 约束）**：不得把 A3/A4/A11 的预测值写成已实现数据；不得把 A2 的机构名单与"高端 90% 由 Lumentum/Coherent/博通把持"口径合并；不得据 A7/A10 推出具体量产良率数字。

---

# 附录 B — evidence_table

格式：`claim | evidence/URL | strength | risk`

1. 硅难发光、需 III-V 异质集成 | `research_tracks_partial.json` 硅光子 tech_core（无独立 URL） | evidence-backed | 领域共识，缺一手论文 URL，标领域常识
2. 200G+ 激光芯片高端产能约 90% 集中于四家 | `research_tracks_partial.json` 硅光子 risks（无独立 URL） | plausible-inference | 该条未挂 URL，机构名单与另一口径冲突，不合并
3. InP 激光 2025 占光芯片 58%、2031 预测 46% | lightcounting.com/newsletter/en/may-2026-... | evidence-backed（2025 值）/ 机构预测（2031 值） | 预测不可当实测
4. 光芯片市场 2025 约 40 亿 → 2031 预测约 150 亿美元 | 同上 | evidence-backed / 机构预测 | 口径为收发器+AOC+NPO+CPO 相关芯片，勿泛化
5. Lambda 用 18 个可现场更换 ELS | casrai.org/news/lambda-nvidia-photonics-co-packaged-optics-sc26-2026 | evidence-backed | 为 ELS 形态证据，非片上集成证据
6. 中际旭创 NPO 用 Tower PH18M 进入早期量产 | openpr.com/news/4694210/... | evidence-backed | 企业公告，"早期量产"≠规模良率达标
7. 光引擎为 CPO 三大瓶颈之一 | chiplet-marketplace.com/insights/news/nvidia-broadcom-cpo-switches | plausible-inference | 机构判断，非实测良率
8. 异构集成推高成本/良率/散热、标准早期 | globenewswire.com/news-release/2026/11/19/3406896/... | plausible-inference | 市场报告附带判断，需审慎
9. 源杰 CW 70/100mW 出货、300mW 研发中 | 818laserhub.cn/newsinfo/11396403.html | evidence-backed | 企业口径，无第三方验证
10. 京瓷+东北大学激光退火集成隔离器，背反射降约 95% | openpr.com/news/4694210/...（2026-10-01 条目） | evidence-backed | 无源器件，与光源集成互补不可互证
11. 缺陷密度—阈值电流—寿命存在定量关系 | 公开资料未覆盖 | hypothesis | 无支撑，列审慎探索 + Go/No-Go
12. 量产良率/单位成本硬数字 | 公开资料未覆盖（latest_silicon_cpo.json uncovered） | unsupported | 不采信自媒体口径，标未覆盖
13. CPO 端口 2031 约 1.89 亿 | simpletechtrend.com/en/post/ocp-2026-... | 机构预测 | 预测值，注明来源
14. 200G EML 单价约 15 美元、2026 需求约 1.5 亿颗 | `latest_comm_laser.json` status_latest（无独立 URL） | plausible-inference | 汇总文件口径，引用需标来源文件

---

# 附录 C — argument_map

- **科学张力**：已知——硅难发光需 III-V 异质集成（A1），光源供给高度集中（A2、A3），CPO/NPO 形态把光源卡位推向前台（A5、A6），光引擎良率/散热是瓶颈（A7、A8）。未知——公开资料未给出同口径的界面缺陷密度—耦合效率—可靠性定量关系，也未给量产良率/成本硬数字（A12 对应 uncovered）。张力在于：产业已要求工程门槛，方法学层面却缺少把三者放进同一可测框架的证据。

- **中心问题**：硅基异质集成 III-V 激光器时，界面缺陷密度、光耦合效率与器件可靠性如何相互制约，能否用一组可测指标约束到同时满足 CPO/NPO 光源门槛的窗口内？

- **中心论点**：可以先交付"路径比较矩阵 + 两形态 Go/No-Go 判据"，把缺陷—阈值—退化关系作为审慎探索并预设失败判据；若关系不成立，结论改为"ELS 与片上集成分别优化"，而非强行给出统一最优工艺。

- **支撑论证 1**：多工艺平台并存与 NPO 早期量产（A6）使三路径同口径比较具备现实对象。局限：企业公告只证实存在，不证实性能可比。

- **支撑论证 2**：ELS 规模部署披露（A5）提供可靠性/热指标的量级锚点，可校验判据合理性。局限：该锚点是系统级（可更换），与器件级可靠性不可等同。

- **支撑论证 3**：InP 激光占比长期维持 46%（A3，机构预测）说明需求是被拉动而非替代，投资异质集成方法学有稳定对象。局限：2031 占比为预测值，存在保守假设下修可能。

- **反论证**：若 scale-up 机架内继续以铜为主、光仅用于多机架，CPO 渗透可能低于乐观预期，两形态判据的应用价值下降。回应：判据按形态分离，允许只交付 ELS 形态；且把材料可获得性列为对照矩阵第五维以对冲路线切换。

- **收尾结论**：读完本立项，评审应接受"异质集成光源的评价方法与判据"是独立于产能、且证据可支撑的研究对象；同时明确哪些指标是目标值、哪些公开资料未覆盖，不把探索级内容误读为交付级承诺。
