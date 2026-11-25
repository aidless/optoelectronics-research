# CPO/近封装光学的键合应力—光纤对准—光电协同在测耦合机理与良率预测方法研究

## 立项书（开题报告级 · 方向级框架）

- 方向编号：P1
- 文本类型：科研立项书 / 开题报告（方向级，框架对、逻辑通，不写操作级 SOP）
- 目标读者：评审专家 / 导师
- 周期：4 年
- 起草日期：2026-11-23
- 数字来源：`outputs/deep-research/latest_silicon_cpo.json`、`outputs/deep-research/latest_comm_laser.json`，缺口数字来自 `outputs/deep-research/research_tracks_partial.json`；纠偏证据来自 `outputs/deep-research/deep-research-20261124-opto-gaps-deepdive.md`（P1 章节，新增主张均带其给出的一手/厂商 URL）；全文不自造数字。

---

## 摘要（约 300 字）

共封装光学（CPO）已从技术验证跨入量产与首批规模部署：机构预测 CPO 市场 2026 年约 9.5 亿美元、2036 年约 204 亿美元（CAGR 32.4%），2026 年 11 月 NVIDIA 与 Lambda 已在加拿大魁北克用 Quantum-X CPO 连接 1 万余张 Blackwell Ultra GPU 实现全球首个规模化商用部署；但机构判断真正放量窗口在 2027—2028 年，工程攻关正当其时。与此同时，近封装光引擎的良率瓶颈集中在三处：COUPE 式"PIC+EIC+硅基板"三明治键合存在纳米级应力与晶圆翘曲、8 芯保偏 FAU 光纤阵列对位偏差需 <0.1° 且熟练工一天仅做 1—2 个、单台高端测试设备日测仅个位数晶圆且光电同测吞吐不足。上述缺口数字来自本地证据文件；深挖后，前两处补到间接公开读数：台积电 COUPE/imec 讲座一手会议 PDF 给出硅光**芯片测试良率 10%–70%**、光纤—硅耦合损耗 >±2.5 dB、晶圆级共振波长漂移控制 1.5 nm；FAU 自动对位厂商口径为 <90 秒/件、相对手工 3× 吞吐、位置公差 ±0.5 µm。口径必须区分：10%–70% 是硅光**芯片测试**良率，光引擎**整机**良率仍未找到一手数字；"对位 <0.1°、熟练工 1—2 个/天"两轮换词检索无任何一手 URL（公开口径为保偏偏振轴 ±1°、V 槽位置 ±0.5 µm，与之量级冲突），继续标本地证据来源。本项目围绕一个中心科学问题展开：键合应力场与 FAU 对准误差如何跨工序耦合为光学插损与良率损失，能否用光电协同的工序间在测—建模闭环把这一耦合辨识出来并用于良率预测。研究拟建立应力—对准—光电的耦合可辨识模型、自动化对位方法与光电协同在测平台，形成跨工序良率预测与 Go/No-Go 判据。预期产出可测的敏感系数量化、对准一致性数据、良率预测区分度与测试吞吐提升读数，为近封装光引擎量产提供一种"测试前移 + 物理信息建模"的良率工程方法。

**关键词**：共封装光学（CPO）；近封装光学（NPO）；三明治键合应力；FAU 保偏光纤阵列对位；光电协同测试；良率预测；可辨识性

---

## 一、立项依据与研究意义

### 1.1 产业拐点：从"是否发生"转为"何时放量"

三组带出处的数字把窗口钉在当下：

1. **规模部署已经发生，不是预测。** 2026 年 11 月 16 日 SC26 上，Lambda 披露与 NVIDIA 的 Quantum-X Photonics CPO 已在加拿大魁北克连接 10,000 余张 GB300 NVL72 架构 Blackwell Ultra GPU 投产，采用 Q3450-LD 交换机（144×800 Gb/s、115.2 Tb/s 无阻塞、18 个可现场更换外部激光源 ELS）；相对可插拔，机架级网络延迟降 3.8%、Pod 级降最多 10.1%，光引擎中位运行温度 36°C 对 51°C（降 15°C），组件可靠性提升最多 15 倍、激光器数量少 4 倍（来源：CASRAI，2026-11-16，见参考文献 [2]）。这是全球首个 CPO 在 AI 云环境的规模化商用部署。
2. **量产节点已过，放量在即。** NVIDIA Spectrum-X CPO（台积电 COUPE 封装、400 Tb/s）2026 年 8 月进入全面量产（来源：NVIDIA 官方频道，2026-08-12，见 [4]）；博通 51.2T Bailly CPO 持续小量出货、功耗最多降 70%、Meta 已完成部署验证。机构（TrendForce，2026-07-29，见 [5]）判断 CPO 放量期在 **2027—2028 年**，并点名三大瓶颈：光引擎良率（激光与调制器集成、良率与散热）、硅光晶圆代工与后段封装、先进封装产能（COUPE 与 AI/HPC 争抢 2.5D/3D 产能）。
3. **市场与端口曲线陡峭。** 机构预测 CPO 市场 2026 年约 9.5 亿美元、2036 年约 204 亿美元、CAGR 32.4%（ResearchAndMarkets，2026-11-19，见 [1]）；LightCounting 端口预测给出 NPO+CPO 合计 2027 年约 450 万、2029 年约 4200 万、2031 年约 1.89 亿端口，CPO 端口约 2030 年接近并超过 NPO（2026-10，见 [6]）。LightCounting 另判断 2026 年是硅光调制器收发器销售额首超 400 亿美元整体市场 50% 的"硅光元年"，光芯片市场 2025 年约 40 亿美元增至 2031 年约 150 亿美元（见 [3]）。

**意义判断（降承诺）**：对高校与科研机构而言，真正的机会不在复现某家厂商的量产线，而在量产窗口打开前，把"良率为什么掉、如何提前测出来"这一共性问题做成可迁移的方法与判据。本立项的落点是方法与测量仪器层面的共性能力，而非与 fab 争产能。

### 1.2 核心缺口：三处卡点都指向"耦合"与"在测"

本地证据文件 `research_tracks_partial.json`（硅光赛道 risks 字段）给出三处缺口；深挖后，键合应力与 FAU 两处补到了相邻的一手/厂商口径，但对位原始数字与测试吞吐原始数字仍只有本地证据来源：

- **键合应力与翘曲**：COUPE 式"PIC+EIC+硅基板"三明治键合存在纳米级应力与晶圆翘曲，良率仍在爬坡。一手会议资料给出相邻规格：12 英寸 65 nm 硅光、10 µm 对准容差对应 0.3 dB 垂直耦合损耗、76 GHz 微环调制器、晶圆级中心共振波长漂移控制 1.5 nm（台积电 COUPE/imec 讲座 PDF，https://swissphotonics.net/libraries.files/Swissphotonics_Lunch_Chat_EmmaXu_1014.pdf ；IEEE HIR 9.0 Photonics 路线图亦在做翘曲建模，https://eps.ieee.org/wp-content/uploads/2026/05/HIR_9_Photonics_rev0.9.pdf）。但这些是规格/控制目标，**不是**"应力/翘曲 → 插损 dB / 波长漂移 nm"的可复算敏感系数。
- **FAU 对准瓶颈**：8 芯保偏 FAU 对位偏差需 <0.1°，熟练工一天仅 1—2 个，FAU 产能与成本直接卡光引擎规模化交付。该两句原始数字经两轮中英换词检索未找到任何一手 URL，维持本地证据来源（plausible-inference）；公开厂商口径为自动对位 6 自由度、单件 <90 秒、相对手工 3× 吞吐、生产级位置公差 ±0.5 µm（https://en.hongjing-optech.com/fiber-array-unit-explained-types-specs-and-how-to-choose-the-right-one ，二手估算），保偏 FAU 偏振轴误差口径为 ±1°（https://www.fiber-mart.com/news/fiber-array-unit-fau-everything-you-need-to-know-a-6842.html），与 <0.1° 量级冲突，不可混引。
- **测试吞吐瓶颈**：单台高端测试设备日测仅个位数晶圆，光电同测吞吐不足；测试集中在终检，难以反馈到工序。公开资料只到"high-throughput 光电同测设备已商用"（ficonTEC 300 mm 双面测试，https://www.ficontec.com/ficontec-releases-innovative-wafer-level-test-cell-to-complement-existing-ate）与"测试左移 / Known Good Optical Engine 是产业共识"（SemiVision，https://tspasemiconductor.substack.com/p/cpos-biggest-bottleneck-is-not-opticsit），以及 <1 s/die 的目标值（https://eureka.patsnap.com/report-improve-wafer-level-silicon-photonics-testing-throughput），**没有** wafers/day 的一手硬基准。

三处缺口并非彼此独立：键合应力改变波导有效折射率与光纤—波导耦合条件，FAU 对准误差直接调制耦合损耗与偏振串扰，热—电—光参数在终检才被观测，导致良率损失无法回溯到具体工序。深挖后口径需精确化：台积电 COUPE/imec 讲座一手 PDF 已给出硅光**芯片测试良率 10%–70%**（https://swissphotonics.net/libraries.files/Swissphotonics_Lunch_Chat_EmmaXu_1014.pdf），故"良率硬数字公开未覆盖"不再笼统成立；但**光引擎整机良率**、**键合应力/晶圆翘曲→插损/波长漂移的可复算敏感系数**、**光电同测日测晶圆吞吐基准**经两轮检索确认**公开资料仍未覆盖**，这三条是本项目要用实测数据填补的科学空白。成本侧仍只有二手估算（ELS 模块约 USD 500、CW 激光芯片约 USD 32，https://global.eefocus.com/article/npo-cpo-industrialization-pm-fiber-fau-yield-and-vcsel-technical-route.html），CPO 渗透率仅见二手转引的 0.5%（2026）→35%（2030，https://www.vitextech.com/blogs/blog/co-packaged-optics-cpo-2026-the-complete-technical-guide）。防混引警示：检索命中的"50%"多为**硅光调制器**渗透率而非 CPO（https://news.futunn.com/en/post/74584585/will-the-race-for-next-generation-optical-modules-avoid-a），"±1°"是**保偏 FAU 偏振轴**误差而非本文的 <0.1° 对位（https://www.fiber-mart.com/news/fiber-array-unit-fau-everything-you-need-to-know-a-6842.html），二者均不可混引。本项目不引用任何来自股吧或自媒体的良率数字，相关量化一律作为"目标值"在本项目中自行测定。

### 1.3 研究意义

把光电协同测试从终检前移到工序间，并用可辨识的耦合模型把在测数据映射为良率，直接对应机构点名的"光引擎良率"与"后段封装"两大瓶颈（[5]）；同时，FAU 对准的自动化与一致性量化，对应国产链在 FAU/MPO/MT 插芯环节被反复提示的脆弱性。这两点构成立项的可检验动机，而非泛泛的产业意义陈述。

---

## 二、国内外研究现状与缺口（区分"已量产 / 实验室 / 未覆盖"）

### 2.1 已量产或规模部署（有带 URL 的出处）

| 主体 | 具体进展 | 出处 |
|---|---|---|
| NVIDIA | Spectrum-X CPO（TSMC COUPE、400 Tb/s）2026-08 全面量产；Quantum-X 经 Lambda 在 1 万+ GPU 集群投产 | [2][4][5] |
| 博通（Broadcom） | 51.2T Bailly CPO 小量出货进入量产，台达电/Micas 导入，Meta 完成部署验证；Tomahawk 6 集成 16 个 6.4T 硅光引擎、交换容量 102.4T、功耗降约 70% | [5][11] |
| 台积电（TSMC） | COUPE 光子引擎平台 2026 进入量产，为 Spectrum-X CPO 供货；第二代 6.4T CPO 计划 2026 下半年量产 | [4][13] |
| 中际旭创（Innolight） | NPO 器件基于 Tower PH18M 工艺进入早期量产；2026Q3 营收 277.69 亿元（+171.83%）、归母净利 85.87 亿元（+173.74%） | [8][9] |
| 天孚通信 | CPO 配套产品已进入批量交付阶段，预计 2027 起逐步提量；NPO 配套处研发/送样/验证 | [12] |
| Lumentum | FY2026 Q4 首次出货 1.6T 收发器，季度营收 10.06 亿美元 | [14] |
| 源杰科技 | 获 17.44 亿元大功率激光器芯片订单，面向 CPO/NPO 的 300 mW 研发推进中 | [15] |

### 2.2 实验室 / 验证 / 标准阶段（有带 URL 的出处）

- **光迅科技**：全球首款 3.2T 硅光单模 NPO 已在头部云服务商完成验证，推出 6.4T NPO 与 12.8T XPO（CIOE 2026，见 [11]）。
- **标准组织**：OIF 2023 年发布首个 3.2T CPO 实施协议，2026Q2 立项《12.8 Tb/s 光电近封装模块》，由中国信通院、华为、腾讯、阿里云、美团、中国移动联合提交（见 [13]）。华为 2026-07 牵头 20 余家启动 OPEN NPO 项目并发布国内首个 NPO MSA（见 [13]）。
- **器件级工艺**：京瓷与东北大学用激光退火把光隔离器直接集成到硅光芯片，背反射降约 95%；NLM Photonics 与 SilOriX 签 JDA 推进硅—有机混合调制器（见 [10]）。这些属材料/器件层进展，尚未构成封装良率与测试的方案。

### 2.3 未覆盖 / 公开资料未覆盖（深挖后精确化）

- **键合应力—翘曲—光学性能的定量耦合**：一手讲座 PDF 只给出规格/控制目标（共振波长漂移 1.5 nm、10 µm→0.3 dB，https://swissphotonics.net/libraries.files/Swissphotonics_Lunch_Chat_EmmaXu_1014.pdf），IEEE HIR 9.0 路线图确认业界在做翘曲建模（https://eps.ieee.org/wp-content/uploads/2026/05/HIR_9_Photonics_rev0.9.pdf）；X 射线键合应变测量给出 0.188°→41.68 µm 弓形→64.12 µm 翘曲（https://pmc.ncbi.nlm.nih.gov/articles/PMC5445873），InP/Si 倒装混合集成给出 sub-300 nm→<2 dB（https://doi.org/10.1109/jstqe.2022.3223641）。**公开资料仍未覆盖**"键合应力/晶圆翘曲 → 插损 dB / 波长漂移 nm"的可复算敏感系数（如 nm/MPa、dB/µm warp），此为本项目科学空白。
- **FAU 自动对位的可公开指标**："对位需 <0.1°、熟练工 1—2 个/天"来自本地证据文件综述条目，两轮换词检索**无任何一手公开 URL**；公开口径（保偏偏振轴 ±1°、V 槽位置 ±0.5 µm）与之量级冲突。间接公开读数仅限厂商口径 <90 秒/件、3× 吞吐、位置公差 ±0.5 µm（https://en.hongjing-optech.com/fiber-array-unit-explained-types-specs-and-how-to-choose-the-right-one），**无**严格可复算的自动化 vs 手工一致性分布。
- **光电同测吞吐**："单台日测个位数晶圆"来自本地证据文件，**公开资料仍未覆盖** wafers/day 硬基准；公开只到商用设备与"测试左移"共识（https://www.ficontec.com/ficontec-releases-innovative-wafer-level-test-cell-to-complement-existing-ate ； https://tspasemiconductor.substack.com/p/cpos-biggest-bottleneck-is-not-opticsit）及 <1 s/die 目标值（https://eureka.patsnap.com/report-improve-wafer-level-silicon-photonics-testing-throughput）。
- **良率硬数字**：已部分覆盖，须按口径区分——**硅光芯片测试良率 10%–70% 有一手出处**（台积电 COUPE/imec 讲座 PDF，https://swissphotonics.net/libraries.files/Swissphotonics_Lunch_Chat_EmmaXu_1014.pdf）；FAU 穿线良率 70%–75%（24/36 芯）/ 90%–95%（天孚产线）为二手行业媒体口径（https://global.eefocus.com/article/npo-cpo-industrialization-pm-fiber-fau-yield-and-vcsel-technical-route.html）；**光引擎整机良率百分比公开资料仍未覆盖一手数字**，TrendForce 官方新闻稿只确认"高制造良率"是瓶颈、未给百分比（https://trendforce.com/presscenter/news/20260727-13151.html）。

**缺口判定**：产业界在量产与标准上领先，且"硅光芯片测试良率"已有一手量化；但"应力—对准—光电—良率"的跨工序可辨识模型、应力→插损/波长漂移可复算敏感系数、光电同测日测晶圆吞吐基准，在本证据集范围内**未见公开覆盖**（后两者经两轮换词检索确认为真空白）。本立项定位为这一空白的方向级攻关，不宣称国内外完全无人做，只声明在所给证据范围内未被覆盖。

---

## 三、关键科学问题与研究目标

### 3.1 一个中心科学问题

在 PIC+EIC+硅基板三明治键合与 FAU 光纤耦合共同决定的近封装光引擎中，**纳米级键合应力/晶圆翘曲与亚度级 FAU 对位误差如何跨工序耦合、传播为器件级光学插入损耗与系统级良率损失；能否用一个光电协同的工序间在测—建模闭环，把这一"应力—对准—热—光电"映射从在测数据中辨识出来，并在封装完成前预测良率损失？**

这是一个可证伪的问题：若应力与对准效应在目标体系中不可分离、或在测特征对最终良率无预测力，则本项目的中心论点不成立。

### 3.2 中心论点（预期检验的假设）

近封装光引擎的良率损失主要不是单一工序的随机误差，而是"键合应力场—FAU 对准误差—热—光电性能"的跨工序耦合结果；因此，把光电协同测试从终检前移到工序间，并用物理信息模型把在测数据映射为良率，可以在不过度依赖熟练工手工对位的前提下，同时提升对准一致性与测试吞吐。

### 3.3 三个可检验子目标

1. **耦合量化**：测定三明治键合应力与晶圆翘曲对波导有效折射率、光纤—波导耦合效率的影响，建立可测的应力—光学映射。
   - 检验判据：应力—插损敏感系数的测量值与模型值偏差 ≤ 目标值（目标值，需实测后标定）。
2. **对准量化**：建立 FAU 角度/平移/间隙误差与耦合损耗、偏振串扰的定量关系，量化自动化对位相对熟练工手工对位的一致性与节拍。
   - 检验判据：自动化对位精度分布、单件节拍与耦合损耗分布相对手工基线给出明确对比读数（数值为目标值）。
3. **良率预测**：构建光电协同在测平台与跨工序良率预测模型，验证在测特征对最终良率的预测能力与模型可辨识性。
   - 检验判据：良率预测的区分度（AUC 或准确率，目标值）、测试吞吐相对基线提升倍数（目标值）、可辨识性检验通过。

---

## 四、研究内容（四个子课题）

### 子课题 1：三明治键合应力—晶圆翘曲—光学性能耦合机理与测量方法

- **要解决的问题**：纳米级键合应力与晶圆翘曲如何改变波导有效折射率、波导—光纤耦合边界条件，进而造成插损与波长漂移的离散？"良率仍在爬坡"缺少可复算的机理解释。
- **方法（方向级）**：建立"PIC+EIC+硅基板"叠层的有限元应力场模型，与波长/偏振分辨的晶圆级光学测量对照；通过控制温度与对准变量做单因素解耦实验，避免把对准误差与温度效应误归因于应力。
- **可测输出指标**：应力—有效折射率/插损敏感系数（测量值 + 模型值 + 偏差，数值为目标值）；翘曲—插损空间分布图；可复现的测量协议 1 份。

### 子课题 2：FAU 保偏光纤阵列高精度自动化对位与耦合/串扰建模

- **要解决的问题**：8 芯保偏 FAU 对位需 <0.1°、熟练工一天仅 1—2 个（本地证据文件），瓶颈在对位一致性与节拍，需要把"手艺"变成可测、可迁移的工艺参数。
- **方法（方向级）**：机器视觉粗定位 + 多轴微位移台精对 + 闭环搜索；建立角度/平移/间隙误差到耦合损耗与偏振串扰的映射模型。以熟练工手工对位为对照基线（能力是否可得见第七节 [PLACEHOLDER]）。
- **可测输出指标**：对位精度分布（角度，目标值）、单件对位节拍（分钟/件，目标值）、耦合损耗与偏振串扰分布；自动化相对手工的一致性对比表。

### 子课题 3：光电协同工序间在测平台与测试吞吐提升方法

- **要解决的问题**：单台高端设备日测仅个位数晶圆、光电同测吞吐不足（本地证据文件），且测试集中在终检、无法反馈工序。
- **方法（方向级）**：在晶圆级/封装级把光学探针（光功率/插损/光谱）与电学探针卡（I-V、眼图、误码率）及温控同步采集，形成"光学—电学—热学"同源在测；把测试节点从终检前移到关键工序之间；用并行多通道与抽样策略缓解吞吐瓶颈。
- **可测输出指标**：单晶圆测试节拍（目标值）、并行通道数（目标值）、光电参数同步采集完整率（目标值）；在测数据格式与接口规范草案 1 份。

### 子课题 4：跨工序良率模型与 Go/No-Go 判据

- **要解决的问题**：应力、对准、热、光电性能跨工序耦合，缺少把在测特征映射为最终良率、且能跨批次泛化的可追溯模型。
- **方法（方向级）**：以子课题 1—3 得到的敏感系数为物理先验，构建物理信息模型并与统计/数据驱动方法对照；重点检验参数可辨识性与跨批次泛化，而非单纯拟合优度。
- **可测输出指标**：良率预测区分度（AUC/准确率，目标值）、可辨识性检验结果、跨批次泛化差距（目标值）；Go/No-Go 判据集 1 套。

---

## 五、技术路线与实验方案（方向级）

技术路线分三层，逐层收敛：

**测量层——光电协同测试平台**。设计思路是"同一片样品、同一温控条件下，同步拿到光学与电学读数"。输入是晶圆级/封装级样品，输出是带工序标签的光学参数（插损、回反、偏振串扰）、电学参数（I-V、眼图、误码率）与温度记录的对齐数据集。关键设计取舍：并行通道数与抽样密度的权衡——全检吞吐不现实，故采用"关键工序全测 + 非关键工序抽样 + 模型外推"。平台所需设备能力见第七节的假设清单。

**机理层——应力—对准—光学耦合模型**。构建思路是把有限元应力场与解析耦合模型结合：应力场给出波导有效折射率与形变分布，解析/半解析耦合模型给出其对光纤—波导耦合效率与偏振串扰的贡献；对准误差作为独立通道并入。核心是**解耦实验设计**——用温度、对准的单因素变化把三者分离，否则模型参数不可辨识。输出是子课题 1、2 的敏感系数体系，作为良率模型的物理先验。

**决策层——良率模型与判据**。把每道工序的在测特征作为输入、最终良率作为标签，训练物理信息 + 统计混合模型；用独立批次检验泛化，用可辨识性分析判定模型是否"学到了机理"而非记住了批次。输出是良率预测值与 Go/No-Go 判据，用于决定某片样品是否进入下一道工序。

**实验方案的阶段逻辑**：先做单因素解耦实验建立敏感系数（子课题 1、2），再搭建并标定光电协同在测平台（子课题 3），最后做跨批次融合验证（子课题 4）。验证的判据不是"模型拟合得多好"，而是"在独立批次上能否提前识别出会掉良率的样品"。

---

## 六、创新点（三条可检验的具体贡献）

1. **跨工序耦合的可辨识模型**：提出并验证"键合应力场—FAU 对准—光电性能"的敏感系数量化体系，给出应力—插损敏感系数与对准—串扰敏感系数的可测量定义；检验方式是模型预测与独立实测的偏差 ≤ 目标值（目标值）。可检验产出：敏感系数表 + 偏差报告，而非定性结论。
2. **光电协同的工序间在测方法**：把光电协同测试从终检前移为工序间在测，给出"在测特征→最终良率"的可检验映射；检验方式是在独立批次上的良率预测区分度（AUC/准确率，目标值）与测试吞吐相对基线的提升倍数（目标值）。可检验产出：在测数据集、预测模型与吞吐对照。
3. **FAU 自动化对位的一致性量化与判据**：给出自动化对位相对熟练工手工对位在精度分布、单件节拍、耦合损耗分布三个维度上的对比结论，并给出可迁移的 Go/No-Go 判据；检验方式是对照实验的统计结果（数值为目标值）。可检验产出：对比表 + 判据集。

> 说明：本立项将"应力—光学机理模型"与"良率预测方法"列为可交付主线（有产业瓶颈与在测数据支撑），将"自动化对位全面替代熟练工"列为审慎探索（对位精度能否达标需实测验证）；若对位精度不达标，退化为"人工粗对 + 机器精调 + 多通道并行"的协作方案，仍可交付一致性与吞吐提升。

---

## 七、可行性分析与已有基础

### 7.1 立论可行性

产业拐点有带 URL 的出处支撑（[1]—[6]），三处缺口来自本地证据文件，研究内容与缺口一一对应，中心问题可被实测证伪。方法层面采用"机理模型 + 数据驱动"双轨，任一轨受阻时另一轨可做兜底（见第十节）。

### 7.2 假设具备的能力与设备（均为 [PLACEHOLDER]，需在开题前逐项落实）

以下为开展本项目所**假设具备**的条件，当前未经核实，一律以 [PLACEHOLDER] 标注：

- 硅光晶圆与 PIC+EIC 键合样品获取渠道：[PLACEHOLDER]
- 晶圆级光学探针台与电学探针卡：[PLACEHOLDER]
- 多轴微位移台、机器视觉与闭环控制组件：[PLACEHOLDER]
- 光电测试仪器（光功率计/光谱仪/眼图仪/误码率测试仪）：[PLACEHOLDER]
- 有限元仿真软件与计算资源：[PLACEHOLDER]
- 温控与洁净/键合工艺环境：[PLACEHOLDER]
- 合作封装厂或中试线，以及可作为对照的熟练对位人员：[PLACEHOLDER]
- 项目团队的硅光器件物理、先进封装与光电测试经验：[PLACEHOLDER]

**诚实声明**：上述条件中任何一项若为"否"，对应研究内容需要调整（见第十节风险 4）。本项目不以"已有基础充分"为前提写承诺，而以"条件清单可核查"为开题前置动作。

---

## 八、年度计划（4 年，每阶段有可交付物）

- **第 1 年｜机理建模与方案设计**：完成三明治键合应力—翘曲有限元模型初版与单因素解耦实验方案；完成光电协同测试平台总体方案与测量协议。
  - 可交付物：应力—光学模型初版 1 份、平台方案 1 份、测量协议 1 份；阶段报告 1 篇。
- **第 2 年｜对位建模与平台搭建**：完成 FAU 自动对位样机与对准—损耗/串扰模型；搭建并标定光电协同在测平台 v1。
  - 可交付物：自动对位样机 1 套及精度/节拍数据、对准模型 1 份、在测平台 v1；论文或专利草案 [PLACEHOLDER] 件。
- **第 3 年｜良率模型与跨批次融合**：融合前三子课题的在测特征，建立良率预测模型 v1，完成可辨识性与跨批次泛化检验。
  - 可交付物：在测数据集 1 套、良率模型 v1、可辨识性检验报告 1 份；论文/专利 [PLACEHOLDER] 件。
- **第 4 年｜验证、收敛与标准化建议**：完成全链验证，收敛 Go/No-Go 判据，形成面向标准组织的测试/对位接口建议草案。
  - 可交付物：全链验证报告 1 份、Go/No-Go 判据集 1 套、标准建议草案 1 份；原型平台 1 套；学位论文/系列论文 [PLACEHOLDER] 篇。

---

## 九、预期成果（指标可测，无证据的数值标"目标值"）

| 类别 | 成果 | 可测指标 |
|---|---|---|
| 论文 | 系列论文 [PLACEHOLDER] 篇（目标值） | 围绕耦合机理、在测方法、良率模型三条主线 |
| 专利 | 发明专利 [PLACEHOLDER] 项（目标值） | 自动对位方法、光电协同在测方法与装置 |
| 标准 | 测试/对位接口建议草案 [PLACEHOLDER] 份（目标值） | 面向 OIF / OPEN NPO MSA 既有框架（[13]），不另起炉灶 |
| 原型 | 光电协同在测平台 1 套、FAU 自动对位样机 1 套（均为目标值） | 见下列量化指标 |
| 量化指标 | 应力—插损敏感系数测量/模型偏差 | ≤ 目标值 |
| 量化指标 | FAU 对位精度分布、单件节拍、耦合损耗与串扰分布 | 给出相对手工基线的对比读数（目标值） |
| 量化指标 | 良率预测区分度（AUC/准确率） | ≥ 目标值（目标值） |
| 量化指标 | 测试吞吐相对基线提升倍数 | ≥ 目标值（目标值） |

> 所有"目标值"均需在项目实测后标定；本项目不引用任何未经一手核实的外界良率数字作为基线。

---

## 十、风险与对策（含技术路线失败的备选）

1. **模型不可辨识风险**：键合应力效应与对准误差、温度效应在目标体系中混淆，导致耦合模型参数不可辨识。
   - 对策：先做单因素解耦实验，把三者分离；备选路线——若机理模型仍不可辨识，降级为"相关性监测 + 统计过程控制（SPC）"方案，不追求机理解释，仍保留良率预测与工序预警能力，保证主线交付不落空。
2. **FAU 对位精度不达标风险**：自动化对位精度达不到手工熟练工水平（<0.1° 的量级要求）。
   - 对策：引入人工粗对 + 机器精调的协作式对位；备选路线——把贡献从"替代熟练工"降为"提升一致性、可追溯性与节拍"，以多通道并行对位换吞吐，仍可交付一致性量化与判据。
3. **测试吞吐提升不及预期风险**：光学测试本身成为新瓶颈，并行与抽样仍无法显著提效。
   - 对策：优化抽样策略与在测特征维度；备选路线——把"全工序全检"降为"关键工序抽检 + 模型外推"，以良率模型的预测能力补偿测试覆盖的下降。
4. **样品/设备/对照条件不可得风险**：第七节任一 [PLACEHOLDER] 项为否。
   - 对策：开题前逐项核实并落实；若键合样品不可得，先用可获得的替代样品做方法学与建模验证，并明确结论适用范围不外推到未验证的封装形态。
5. **产业路线不确定风险**：CPO / NPO / 可插拔路线并存，机构也提示 scale-up 域仅 10—15% 迁移到 NPO/CPO 的保守假设（[3]）。
   - 对策：聚焦"近封装光引擎"的共性机理与测量问题，不绑定单一产品形态；即便某形态放量延后，方法与判据仍可迁移。

---

## 十一、经费与条件概要

- 经费总额：[PLACEHOLDER]
- 设备购置与加工：[PLACEHOLDER]
- 样品与流片/封装：[PLACEHOLDER]
- 测试与计算资源：[PLACEHOLDER]
- 人员与学生：[PLACEHOLDER]
- 合作与差旅（标准组织/产业调研）：[PLACEHOLDER]
- 场地与洁净环境：[PLACEHOLDER]

> 具体金额、来源与配比在可行性核实（第七节 [PLACEHOLDER] 项）完成后填报。

---

## 参考文献（数字与出处均取自证据 JSON；每条带真实 URL 和日期）

[1] ResearchAndMarkets. *Co-Packaged Optics (CPO) Market Analysis and Forecast 2026-2036*（CPO 市场 2026 约 9.5 亿美元、2036 约 204 亿美元、CAGR 32.4%）. 2026-11-19. https://www.globenewswire.com/news-release/2026/11/19/3406896/28124/en/co-packaged-optics-cpo-market-analysis-and-forecast-2026-2036-ai-data-center-demand-drives-32-4-cagr-creating-a-20-4-billion-market-by-2036.html

[2] CASRAI Editorial Board. *Lambda Deploys NVIDIA Co-Packaged Optics Across 10,000 GPUs*（SC26：Quantum-X CPO 连接 1 万+ Blackwell Ultra GPU；延迟降 3.8%—10.1%、光引擎 36°C 对 51°C、可靠性升最多 15 倍）. 2026-11-16. https://casrai.org/news/lambda-nvidia-photonics-co-packaged-optics-sc26-2026

[3] LightCounting. *2026 Is the Year of Silicon Photonics and Indium Phosphide*（2026 硅光元年；光芯片 2025 约 40 亿→2031 约 150 亿美元；scale-up 域 10—15% 迁移假设）. 2026-05. https://www.lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377

[4] NVIDIA 官方频道. *Spectrum-X Ethernet Photonics 进入全面量产*（台积电 COUPE、400 Tb/s，2026 下半年扩产）. 2026-08-12. https://www.youtube.com/watch?v=CNM6Mmqrfeg

[5] TrendForce / Chiplet Marketplace. *NVIDIA 与博通 CPO 交换机进入量产*（放量期 2027—2028；光引擎良率、硅光产能、先进封装三大瓶颈；博通 51.2T Bailly 功耗降最多 70%、Meta 已验证）. 2026-07-29. https://chiplet-marketplace.com/insights/news/nvidia-broadcom-cpo-switches

[6] LightCounting / SimpleTechTrend. *OCP 2026 CPO/NPO 端口分年预测*（NPO+CPO 合计 2027 约 450 万→2029 约 4200 万→2031 约 1.89 亿端口）. 2026-10. https://www.simpletechtrend.com/en/post/ocp-2026-lightcounting-cpo-npo-forecast-scenarios-en

[7] Tower Semiconductor / OpenPR. *Tower 与中际旭创扩大 NPO 合作*（Innolight 基于 Tower PH18M 的 NPO 器件进入早期量产）. 2026-11-03. https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries

[8] 东方财富 F10. *中际旭创（300308）2026 年三季报*（Q3 营收 277.69 亿元 +171.83%、归母净利 85.87 亿元 +173.74%；前三季 695.47 亿/222.38 亿）. 2026-10-29. https://emweb.eastmoney.com/pc_hsf10/pages/index.html?code=300308.html

[9] OpenPR. *GlobalFoundries 获美商务部约 3 亿美元 CHIPS 研发意向，加速硅光/NPO/CPO（含 3D 混合键合）*. 2026-07-01. https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries

[10] OpenPR. *京瓷联合东北大学激光退火集成光隔离器，背反射降约 95%；NLM Photonics 与 SilOriX 签 JDA 推进硅—有机混合调制器*. 2026-10-01 / 2026-09-21. https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries

[11] 36Kr. *CIOE 2026：光迅 3.2T 硅光单模 NPO 完成头部云服务商验证、推出 6.4T NPO 与 12.8T XPO；博通 Tomahawk 6 集成 16 个 6.4T 硅光引擎、功耗降 70%*. 2026-09-09. https://eu.36kr.com/zh/p/4001118301425796

[12] 新浪财经. *新易盛 1.6T 进入大规模放量、天孚通信 CPO 配套产品进入批量交付*. 2026-11-18. https://finance.sina.com.cn/roll/2026-11-18/doc-inizensx6831692.shtml

[13] 36Kr. *华为牵头 20 余家启动 OPEN NPO 项目并发布国内首个 NPO MSA；OIF 2026Q2 立项《12.8Tb/s 光电近封装模块》；台积电 COUPE 二代 6.4T CPO 计划 2026 下半年量产*. 2026-07-09. https://eu.36kr.com/zh/p/4001118301425796

[14] Lumentum Investor Relations. *FY2026 Q4 首次出货 1.6T 收发器，季度营收 10.06 亿美元*. 2026-08-11. https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Fourth-Quarter-and-Full-Fiscal-Year-2026-Results/default.aspx

[15] 818 Laser Hub. *源杰科技获 17.44 亿元大功率激光器芯片订单，面向 CPO/NPO 的 300 mW 研发推进中*. 2026-11-13. https://www.818laserhub.cn/newsinfo/11396403.html

> 缺口数字来源（无独立公开 URL，本地证据文件）：`outputs/deep-research/research_tracks_partial.json`（硅光赛道 risks 字段）——FAU 8 芯对位 <0.1°、熟练工一天 1—2 个、三明治键合纳米级应力与晶圆翘曲、单台高端测试设备日测个位数晶圆。该文件为本地证据汇编，相关数字在正文中如实标注来源性质，不冒充一手公开出处。

---

## 附录 A｜research_canon（硬事实，每条带来源 URL）

1. 2026 年 11 月，Lambda 与 NVIDIA 已在 1 万余张 Blackwell Ultra GPU 上实现全球首个 CPO 规模化商用部署（延迟降 3.8%—10.1%，光引擎 36°C 对 51°C）。来源 [2]，https://casrai.org/news/lambda-nvidia-photonics-co-packaged-optics-sc26-2026
2. CPO 市场机构预测 2026 年约 9.5 亿美元、2036 年约 204 亿美元、CAGR 32.4%。来源 [1]，https://www.globenewswire.com/news-release/2026/11/19/3406896/28124/en/co-packaged-optics-cpo-market-analysis-and-forecast-2026-2036-ai-data-center-demand-drives-32-4-cagr-creating-a-20-4-billion-market-by-2036.html
3. 2026 年是硅光调制器收发器销售额首超 400 亿美元整体市场 50% 的年份；光芯片市场 2025 约 40 亿→2031 约 150 亿美元，且原文把 "limited production yields" 写入预测假设。来源 [3]，https://www.lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377
4. NVIDIA Spectrum-X CPO（TSMC COUPE、400 Tb/s）2026-08 进入全面量产；机构判断 CPO 放量期在 2027—2028 年，瓶颈含光引擎良率与后段封装。来源 [4][5]，https://www.youtube.com/watch?v=CNM6Mmqrfeg ； https://chiplet-marketplace.com/insights/news/nvidia-broadcom-cpo-switches
5. LightCounting 端口预测：NPO+CPO 合计 2027 约 450 万→2031 约 1.89 亿端口，CPO 约 2030 年接近/超过 NPO。来源 [6]，https://www.simpletechtrend.com/en/post/ocp-2026-lightcounting-cpo-npo-forecast-scenarios-en
6. 中际旭创 NPO 器件基于 Tower PH18M 进入早期量产；2026Q3 营收 277.69 亿元（+171.83%）。来源 [7][8]，https://www.openpr.com/news/4694210/silicon-photonics-market-gains-momentum-as-globalfoundries ； https://emweb.eastmoney.com/pc_hsf10/pages/index.html?code=300308.html
7. 标准进展：OIF 3.2T CPO IA 已发布、OIF 2026Q2 立项 12.8T NPO，华为牵头 OPEN NPO MSA。来源 [13]，https://eu.36kr.com/zh/p/4001118301425796
8. 三处核心缺口（FAU 8 芯对位 <0.1°、熟练工 1—2 个/天、三明治键合纳米级应力与晶圆翘曲、单台设备日测个位数晶圆）：来自本地证据文件 `outputs/deep-research/research_tracks_partial.json`（硅光赛道 risks），**无一手公开 URL**，公开资料未覆盖；正文按本地证据文件来源如实标注，不升级为一手事实。

---

## 附录 B｜evidence_table（claim | evidence/URL | strength | risk）

| # | Claim | Evidence / URL | Strength | Risk |
|---|---|---|---|---|
| 1 | CPO 已实现规模商用部署（1 万+ GPU） | CASRAI 2026-11-16 [2] casrai.org/news/lambda-nvidia-photonics-co-packaged-optics-sc26-2026 | evidence-backed | 单一来源披露，细节（温度/延迟数字）宜以厂商原文二次核对 |
| 2 | CPO 放量窗口 2027—2028，瓶颈为光引擎良率/后段封装/先进封装 | TrendForce 2026-07-29 [5] chiplet-marketplace.com/insights/news/nvidia-broadcom-cpo-switches | evidence-backed | 机构判断非实测；放量节奏受路线与产能影响 |
| 3 | CPO 市场 2026→2036 高增长（CAGR 32.4%） | ResearchAndMarkets 2026-11-19 [1] globenewswire.com（URL 见参考文献） | evidence-backed | 机构预测值，非已实现数字；不同机构口径差异大 |
| 4 | 2026 为硅光元年，光芯片市场 4 年近 4 倍 | LightCounting 2026-05 [3] lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377 | evidence-backed | 预测含 10—15% scale-up 迁移假设，保守情景下会下修 |
| 5 | 三明治键合存在纳米级应力与晶圆翘曲，良率爬坡中 | 本地证据文件 research_tracks_partial.json（硅光赛道 risks） | plausible-inference | 无一手公开 URL；"纳米级/良率爬坡"为综述定性表述，需一手工艺文献复核 |
| 6 | FAU 8 芯对位需 <0.1°、熟练工 1—2 个/天 | 本地证据文件 research_tracks_partial.json（硅光赛道 risks） | plausible-inference | 无一手公开 URL；数字未按器件形态/芯数分层，需厂商口径核实 |
| 7 | 单台高端测试设备日测个位数晶圆，光电同测吞吐不足 | 本地证据文件 research_tracks_partial.json（硅光赛道 risks） | plausible-inference | 无一手公开 URL；设备型号与测试项未明，基线需自建 |
| 8 | 应力/对准/热/光电可跨工序耦合为良率损失 | 由 #5#6#7 综合 + 机构点名良率瓶颈 [5] | plausible-inference | 耦合机制为本项目待检验假设，未被直接实测证实 |
| 9 | 光电协同在测前移可提前识别良率损失 | 由 #7#8 推演的本项目中心论点 | hypothesis | 需项目实测验证；若不可辨识则走 SPC 兜底 |
| 10 | 自动化对位可达到/接近手工精度并提升节拍 | 由 #6 推演的审慎探索目标 | hypothesis | 对位精度能否达标未知；不达标则走协作式对位备选 |
| 11 | 光学参数（插损/串扰）可敏感反映对准与应力状态 | 器件物理常识 + 本项目拟验证 | plausible-inference | 需解耦实验确认，防止温度/对准混淆导致误归因 |
| 12 | 量产良率/单位成本的权威硬数字 | 公开资料未覆盖（证据 JSON uncovered 字段） | unsupported | 不引用自媒体/股吧数字；相关量化一律设为本项目目标值 |

---

## 附录 C｜argument_map（论证地图）

- **科学张力（已知 vs 未知 vs 为何重要）**：已知——CPO 已规模部署、放量在 2027—2028、机构点名光引擎良率与后段封装是瓶颈（[2][5]）；本地证据文件指出三处缺口（键合应力/翘曲、FAU <0.1° 对位、测试吞吐不足）。未知——应力与对准如何跨工序耦合为插损与良率损失，以及在测数据能否支撑提前预测。重要性——量产窗口正当口，方法层面的共性能力可跨产品形态迁移。
- **中心研究问题**：键合应力场与 FAU 对准误差如何跨工序耦合为器件级插损与系统级良率损失，能否用光电协同的工序间在测—建模闭环把该映射辨识出来并提前预测良率（见第三节）。
- **中心论点**：良率损失主要是跨工序耦合而非单一随机误差；把光电测试前移并用物理信息模型映射良率，可在不过度依赖熟练工手工对位的前提下同时改善对准一致性与测试吞吐。
- **支撑论证 1**：产业瓶颈真实存在——机构明确把光引擎良率与后段封装列为放量瓶颈（[5]，evidence-backed）。局限：机构判断非一手良率测量，且公开资料未覆盖良率硬数字。
- **支撑论证 2**：三处缺口指向同一机理——应力改折射率与耦合、对准改插损与串扰、测试滞后致损失不可回溯（本地证据文件，plausible-inference）。局限：缺口数字无一手公开 URL，耦合机制为待检验假设。
- **支撑论证 3**：技术路径可行——有限元应力建模、光学/电学同步在测、物理信息 + 统计混合建模均为成熟方法的组合（方法学 plausible-inference）。局限：在目标体系中参数可辨识性与跨批次泛化需实测检验，可能不成立。
- **支撑论证 4**：窗口适配——放量在 2027—2028（[5]），4 年周期覆盖攻关到验证窗口（evidence-backed + 时间推断）。局限：若产业路线转向或 scale-up 光替代延后（[3] 保守假设），方法仍可迁移但产业拉动减弱。
- **反论证**：①应力效应与对准/温度效应在目标体系中混淆，机理模型不可辨识——以单因素解耦实验回应，失败则退守 SPC 相关性监测；②自动化对位达不到 <0.1°——退守协作式对位与多通道并行，贡献改为一致性/可追溯/节拍；③测试并行与抽样仍不足——退守关键工序抽检 + 模型外推；④若 scale-up 域继续以铜为主（[3]），CPO 渗透低于预期——聚焦近封装共性机理，不绑定单一形态。
- **收尾结论**：读者应得出的判断是——在 CPO 量产窗口打开前，本项目针对的"应力—对准—光电—良率"跨工序耦合与在测前移是一个有真实产业需求、证据边界清晰、且可用可测指标证伪的方向级课题；其价值不依赖某家厂商的良率口碑，也不依赖对未覆盖数字的主观臆测。
