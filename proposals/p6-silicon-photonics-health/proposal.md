# 硅光健康监测的临床验证与转化：光声、光谱与无创传感的可靠性及人体验证

## 项目名称

面向可穿戴与重症监护场景的硅光无创传感——光声与光谱路线的可靠性验证框架及临床转化路径研究

## 摘要（约300字）

硅光与集成光子学已把血压、血糖、肺通气的无创测量压缩到芯片级：硅光光声血压传感器 SPADE 在 Nature Communications 报告了 NEP 2 mPa/√Hz、125 MHz 带宽、100 Hz 采样的器件性能；剑桥大学的卷积光谱仪在 Nature Photonics 上以 1200–1700 nm 宽带、<1 秒测量在模拟生理环境中测得血乳酸与血糖；上海交大团队以 42 名新生儿、110.66 小时同步有创数据验证了柔性多波长 PPG 连续血压的可行性。监管端，Conavi OCTIV 混合冠脉成像已获 FDA 510(k) 并完成美国首台商业装机，Neola 近红外早产儿肺监测获 FDA 突破性设备认定并进入 TAP Pilot——但认定不等同于上市批准。本方向的核心障碍不在器件灵敏度，而在证据链：两份 deep-research 报告一致把上述路线的"人体大规模临床样本数"标注为"公开资料未覆盖"，且高运动组 PPG 血压误差升至 14.23/11.08 mmHg，跨人群泛化尚未验证。本项目拟以"器件—离体/动物—小规模人体—临床队列"四级验证为主线，建立光声与光谱双模态可靠性对照方法、跨人群分层临床验证设计，并把监管路径前置为研究变量，形成可检验、可转化的证据包。周期 4 年，方向级框架。

**关键词**：硅光健康监测；光声传感；卷积光谱；无创血压；无创血糖；临床验证；医疗器械转化

---

## 一、立项依据与意义

可穿戴无创生理监测的价值池集中在无袖带血压与无创血糖，这两个方向的共同特征是"物理可行已被演示、临床可靠尚未证实"。2026 年下半年，器件侧与监管侧同时出现进展，但二者之间的证据链出现明显断层。

器件侧的三项代表性成果给出了灵敏度的下界证明。硅光光声路线以单探测元读取桡动脉光声信号（NEP 2 mPa/√Hz、125 MHz 带宽、100 Hz 采样），并用对准容差实验回应用户佩戴一致性质疑（Nature Communications，2026-09-17）。宽带光谱路线以低成本卷积光谱仪在模拟生理环境中测得皮肤水分、血醇、血乳酸与血糖，并对一名受试者进行长时间无创血糖追踪（Nature Photonics；ScienceDaily 2026-10-26 再报道）。多波长 PPG 路线在 42 名新生儿上取得 9378 个测试片段、SBP/DBP MAE 9.67/6.17 mmHg，SQI≥0.85 时降至 8.22/4.98 mmHg（Advanced Science；上海交大，2026-09-22）。

监管侧的进展改变了转化语境。Conavi OCTIV 混合冠脉成像系统（OCT+IVUS）已获 FDA 510(k) 批准，并于 2026-11 完成美国首台商业化装机，上市前两周约 25 例临床使用（StockTitan，2026-11-19，二手公司新闻稿聚合）。Neola 近红外无创早产儿肺监测于 2026 年 9 月获 FDA 突破性设备认定，季度结束后进入 FDA TAP Pilot（公司 Q3 报告，2026-11-18）。需明确：**突破性设备认定不等同于上市批准**，Neola 仍处认定与试验通道阶段。

意义落在证据而非概念：当器件性能已不是主要瓶颈，能否把"单受试者/小规模/模拟环境"的演示，升级为跨人群、真实佩戴条件下可复核的临床可靠性证据，并据此选择监管路径，是决定这类技术能否进入临床的关键。市场侧多家机构给出 2032 年约 1306 亿美元（ResearchAndMarkets，2026-11-03）等预测，但各家口径不一、不可直接比较，仅作背景，不构成本项目的立论依据。

## 二、国内外研究现状与缺口

按监管与验证成熟度分层，而非按时间罗列：

| 分层 | 代表成果 | 关键事实（含来源） | 对本项目的含义 |
|---|---|---|---|
| **已获 FDA 批准并已装机** | Conavi OCTIV 混合冠脉成像（OCT+IVUS） | FDA 510(k) 已批；2026-11 完成美国首台商业装机；上市前两周约 25 例临床使用（StockTitan，2026-11-19，二手聚合，细节以官方后续披露为准） | 腔内光子成像的"批准—装机—临床反馈"闭环已跑通，可作为转化路径的对照样本 |
| **已获 FDA 批准（治疗类，非监测）** | Ameluz 红光 PDT 治疗浅表基底细胞癌 | 2026-09-14 经 sNDA 扩适应症获批，为美国首个获批治疗皮肤癌的 PDT（BioSpace，2026-09-14） | 光子治疗监管先例成熟，但与本项目无创监测的证据要求不同，不直接外推 |
| **FDA 突破性设备认定（≠上市批准）** | Neola 近红外早产儿肺监测 | 2026-09 获突破性设备认定；2026-11 进入 TAP Pilot；可检测气胸与肺塌陷（Neola Q3，2026-11-18） | 新生儿/ICU 是伦理友好型临床验证的优先场景；认定只是通道资格，不是批准 |
| **FDA 510(k)（二手报道，编号待核）** | Happy Ring 无袖带血压智能戒指 | 2026-10 报道获 510(k)，号称首款无需袖带与外部校准的持续被动血压可穿戴；具体编号、型号与临床验证数据公开资料未覆盖，需查 FDA 510(k) 原始数据库（动脉网，2026-10-14） | 不纳入确证证据；作为"必须回原始数据库核验"的反面教材写入证据纪律 |
| **论文级器件/小规模临床验证** | SPADE；剑桥卷积光谱仪；上海交大 NEO-BP；InnoPIC | SPADE 器件性能见上；剑桥光谱仪为模拟环境+单受试者追踪；NEO-BP 为 42 例/110.66 h；InnoPIC 的 SiN+拉曼+SPAD+AI 方案仍属竞赛孵化/概念阶段（PhotonDelta，2025-08-26） | 共同瓶颈是样本规模、跨人群泛化与长期安全性，而非灵敏度 |
| **公开资料未覆盖** | 上述路线的人体大规模多中心临床样本数；无创血糖上市时间表；硅光健康监测芯片独立市场规模 | 两份 deep-research 报告一致标注"公开资料未覆盖"；下半年未见更大规模多中心临床更新 | 这就是本立项的核心研究空间 |

跨人群泛化已有可量化的警示：多波长 PPG 血压在高运动组误差升至 14.23/11.08 mmHg，模型跨人群泛化不足；拉曼血糖信号极弱，临床级精度尚未公开验证；无创光学测量受肤色、脂肪厚度、灌注、运动伪影与温度影响。监管侧 FDA 已发布无袖带血压设备临床性能测试指南草案，意味着后续产品须按统一性能标准竞争，而非单点宣发。

## 三、关键科学问题与研究目标

### 中心科学问题

在真实佩戴与临床场景下，硅光光声与宽带光谱两条无创传感路线的可靠性，究竟由器件物理灵敏度决定，还是由"人—器件—算法—场景"耦合决定？若为后者，其误差来源能否被分层、量化，并形成可支撑监管决策的临床证据包？

### 三个可检验子目标

1. **器件—场景可靠性解耦**：在统一佩戴位点下，量化光声与光谱两条路线各自的误差预算，检验"运动/灌注/肤色/温度"四类协变量对 MAE 的独立贡献是否显著大于器件本底噪声。（可检验：误差分解表与方差贡献比）
2. **跨人群临床验证设计**（必须为临床验证设计）：在伦理批准与临床合作落地的条件下，构建按肤色、灌注、运动强度分层的前瞻性队列，检验 SQI 阈值分层是否能把高运动组误差拉回至与静息组可比的水平。（可检验：分层前后 MAE 对比与 SQI 阈值曲线；样本量待定 [PLACEHOLDER]）
3. **监管路径前置研究**：以"突破性认定→TAP Pilot→510(k)"（Neola 型）与"直接 510(k)"（Conavi 型）两条路径为对照，检验哪类证据包结构更适配无创连续监测产品的clinical evaluation 要求。（可检验：监管路径决策树与临床证据包模板）

## 四、研究内容（4 个子课题）

**子课题 1｜传感器件与系统集成。** 围绕光声与光谱两条路线，建立可比对的系统集成基线：光声侧关注单探测元对准容差的工程复现（对应 SPADE 报告的 ±10 mm 平移、30° 偏航）；光谱侧关注 1200–1700 nm 波段的低功耗采样与弱信号读出。本子课题是"可交付主线"：文献支持充分、器件条件相对具备，产出为可复现的硬件基线与标定协议。**不追求**在此阶段突破器件灵敏度极限。

**子课题 2｜离体/动物验证。** 在组织光学体模与动物模型上建立"gold standard 对照—误差归因"流程，回答子目标 1 的误差分层问题。此阶段为**审慎探索**：体模/动物与人体组织的散射、灌注差异可能使结论不可直接外推，因此设置 Go/No-Go 判据——仅当层间误差趋势在体模与动物上方向一致，才进入人体队列。兜底方案：退回纯器件可靠性表征，暂缓人体推进。

**子课题 3｜人体临床队列设计。** 本项目的核心。设计前瞻性、分层入组、以有创动脉血压或参考级设备为对照的临床验证方案。新生儿/ICU 场景因临床刚需明确、伦理路径相对成熟被优先考虑（对应 Neola 与 NEO-BP 的场景选择）。**样本量、中心数、入组标准、对照金标准均为待定 [PLACEHOLDER]，须在伦理审批与临床合作协议签署后依方案确定，本立项书不预先给出任何具体数值。** 交集配置：临床合作单位 [PLACEHOLDER]、伦理审批状态 [PLACEHOLDER]。

**子课题 4｜数据/算法与监管路径。** 建立误差分层算法与 SQI 可信度评估（对应 NEO-BP 中 SQI≥0.85 的降误差机制），并同步开展监管路径研究：梳理 FDA 无袖带血压临床性能测试指南草案的要求，对照 Happy Ring 报道中"编号待核"的证据缺陷，形成可提交的临床证据包模板。产出为算法流程与监管决策树，不宣称任何注册结果。

## 五、技术路线与实验方案（方向级）

总体路线：`器件基线建立 → 体模/动物误差归因 → Go/No-Go 门 → 分层人体队列 → 算法与监管证据包`。

- **阶段 A（器件与体模）**：统一标定流程，输出两条路线的误差预算初表；判据为重复性系数达到预设阈值 [PLACEHOLDER]。
- **阶段 B（动物）**：验证误差分层趋势的方向一致性；Go/No-Go：方向一致才进入阶段 C，否则退回阶段 A 的纯器件表征。
- **阶段 C（人体队列）**：分层前瞻性入组，采集与参考金标准同步的数据。**临床样本量：[PLACEHOLDER]（待伦理与统计方案确定，不得引用任何外部推测值）**。对照选择、盲法与统计计划写入独立方案，不在本方向级文本中固化。
- **阶段 D（算法与转化）**：在锁定的测试集上评估 SQI 分层对误差的影响，形成误差分解报告与监管路径决策树。

本路线刻意不写操作级 SOP、设备型号与具体手术/采样步骤——这些属于进入实验前的专项计划，而非开题级框架。

## 六、创新点（3 条可检验贡献）

1. **双模态同点可靠性对照方法**：把光声（SPADE 型）与宽带光谱（剑桥型）两条原本独立发展的路线放到同一佩戴位点、同一分层协议下比较，产出跨模态一致性与误差分解报告。可检验判据：两条路线在四类协变量上的方差贡献比可被独立复算。这不是"提出一个新传感器"，而是提出一个可复用的对照方法。
2. **面向跨人群泛化的分层验证设计**：针对 NEO-BP 高运动组误差升至 14.23/11.08 mmHg 的公开缺口，把 SQI 阈值与分层入组绑定为可检验假设，产出"SQI 分层前后 MAE 对比曲线"。可检验判据：高运动组 MAE 是否在预设 SQI 阈值下向静息组收敛。
3. **监管路径作为研究变量**：把 Neola 型（突破性认定→TAP Pilot）与 Conavi 型（直接 510(k)）两条路径作为对照，产出无创连续监测的证据包结构决策树。可检验判据：决策树能否对 Happy Ring 型"编号待核"报道给出明确的证据缺口判定。**特别约束：本贡献绝不等于宣称任何产品已获批上市。**

## 七、可行性与已有基础

已有基础限于可核验的公开证据：SPADE 论文已完成号—题核验（Nature Communications，卷 17 文章 10931）；Neola 突破性认定措辞已回原文核验（公司 Q3 报告，2026-11-18）；上海交大 NEO-BP、剑桥光谱仪、Conavi OCTIV 均有可追溯 URL。

需补齐的前置条件（全部标注为假设，未落实前不作为承诺）：临床合作单位 [PLACEHOLDER]；伦理审批 [PLACEHOLDER]；参考级金标准设备与场地 [PLACEHOLDER]；硅光流片/封装通道 [PLACEHOLDER]；队列样本量及其统计功效测算 [PLACEHOLDER]。按降承诺原则，队列推进属于"审慎探索"，其 Go 门未通过时，项目仍可在器件与体模层面交付主线成果，不至于整体落空。

## 八、年度计划（4 年，分阶段 + 交付物）

| 年度 | 阶段 | 主要工作 | 交付物 |
|---|---|---|---|
| 第 1 年 | 器件与基线 | 建立光声/光谱硬件基线与统一标定协议；完成公开证据复核 | 硬件基线报告；误差预算初表；foundation 证据账本 |
| 第 2 年 | 体模/动物 | 误差归因实验；执行 Go/No-Go 门；签署临床合作与伦理申报 | 误差分层报告；Go/No-Go 结论；伦理申报材料 [PLACEHOLDER] |
| 第 3 年 | 人体队列 | 分层前瞻性入组与同步采集（样本量 [PLACEHOLDER]） | 临床数据集；采集协议；中期评估报告 |
| 第 4 年 | 算法与转化 | SQI 分层评估；监管路径决策树；结题 | 误差分解报告；监管证据包模板；论文与专利草案 |

## 九、预期成果（指标可测）

成果按"论文/专利/临床数据在先提交"的顺序陈述，避免以注册结果作为承诺：

1. 论文：围绕双模态可靠性对照与跨人群分层验证，目标 [PLACEHOLDER] 篇，投稿前完成证据溯源核查。
2. 专利：围绕同点双模态标定与 SQI 分层方法，目标 [PLACEHOLDER] 项。
3. 临床数据：形成一份可审计的分层验证数据集与误差分解报告，样本量与指标在伦理批准后锁定，本阶段不预设数值。
4. 方法学产物：监管路径决策树 1 份、临床证据包模板 1 份。
5. 所有对外数字均附可复算来源；无法核验者一律标注"公开资料未覆盖"或 [PLACEHOLDER]。

## 十、风险与对策

| 风险 | 触发信号 | 对策 / 备选 |
|---|---|---|
| **临床入组失败** | 伦理通过后入组进度低于计划阈值 [PLACEHOLDER] | 启用备选场景（成人 ICU/运动负荷人群）与备选中心 [PLACEHOLDER]；若仍失败，退回子课题 1/2 的器件与体模主线，按"边界确认"交付操作窗口与 Go/No-Go 判据 |
| **伦理审批延期** | 首轮伦理未在计划节点获批 | 先完成体模/动物与算法仿真，把队列阶段整体后移；同步准备多中心伦理互认方案 [PLACEHOLDER]；不提前开展任何人体采集 |
| **跨人群泛化不足** | 高运动组 MAE 未随 SQI 阈值收敛（复现 14.23/11.08 mmHg 型退化） | 收窄适用人群声明，把结论降级为"边界确认"；公开标注失效子群，不做泛化承诺 |
| **无创血糖信号过弱** | 光谱路线在体模上无法达到可分辨信噪比（InnoPIC 型风险） | 该路线降为审慎探索，主线转向光声血压与肺监测；保留光谱路线为对照臂而非核心交付 |
| **监管语义误读** | 外部传播把突破性认定写成"获批上市" | 全文与对外材料强制使用"突破性设备认定（≠上市批准）"；引用 Happy Ring 型二手报道时标注编号待核，须回 FDA 510(k) 原始库核验 |
| **数据隐私** | 连续生理波形属敏感健康数据 | 数据去标识与访问控制写入采集协议；存储与共享方案 [PLACEHOLDER] |

## 十一、经费与条件概要

经费总额、设备费、流片/封装费、临床合作与受试者 compensation、伦理与注册咨询费均为 [PLACEHOLDER]，待合作单位与队列方案确定后编制。条件概要：硅光流片/封装通道 [PLACEHOLDER]；参考级金标准设备 [PLACEHOLDER]；临床场地与统计支持 [PLACEHOLDER]。

---

## 参考文献（每条含真实 URL 与日期）

1. Nature Communications（卷 17，文章 10931），*Silicon-photonics optoacoustic sensor for fully wearable blood pressure monitoring*，2026-09-17。https://www.nature.com/articles/s41467-026-77580-3
2. ScienceDaily，剑桥大学光学卷积光谱仪（Nature Photonics）再报道，2026-10-26。https://www.sciencedaily.com/releases/2026/10/261022081312.htm
3. StockTitan，Conavi Medical OCTIV 混合冠脉成像首台商业装机（二手公司新闻稿聚合），2026-11-19。https://www.stocktitan.net/news/CNVIF/conavi-medical-highlights-commercial-launch-and-significant-growth-vb5k4qqycrdl.html
4. Neola Medical，Q3 Report 2026 – FDA Breakthrough Device Designation（认定≠批准），2026-11-18。https://neolamedical.com/mfn_news/neola-medical-q3-report-2026-fda-breakthrough-device-designation-strengthens-u-s-regulatory-pathway
5. 上海交通大学，柔性多波长 PPG 新生儿无创连续血压（Advanced Science，NEO-BP），2026-09-22。https://news.sjtu.edu.cn/jdzh/20260922/226182.html
6. PhotonDelta，InnoPIC 无创连续血糖（SiN PIC+拉曼+SPAD+AI，概念阶段），2025-08-26。https://www.photondelta.com/news/integrated-photonics-for-healthcare-and-biomedical
7. 动脉网（信源：器械之家），Happy Ring 智能戒指 FDA 510(k) 报道（二手，编号待核），2026-10-14。https://www.vbdata.cn/intelDetail/1118328
8. Yahoo Finance / ResearchAndMarkets，Biophotonics: Global Strategic Business Report 2026，2026-11-03。https://finance.yahoo.com/healthcare/articles/biophotonics-global-strategic-business-report-144500184.html
9. ZEISS，EURETINA 2026 扩展 Retina Workflow（ALTA DUO 300、CR3），2026-09-24。https://www.zeiss.com/meditec-ag/en/media-news/press-releases/2026/euretina.html
10. BioSpace，FDA 批准 Ameluz 红光 PDT 治疗浅表基底细胞癌，2026-09-14。https://www.biospace.com/press-releases/biofrontera-announces-fda-approval-of-ameluz-red-light-pdt-for-the-treatment-of-superficial-basal-cell-carcinoma

---

## 附录 A｜research_canon（硬事实与边界，≥5 条，均带来源 URL）

1. SPADE 为硅光光声无袖带血压传感器，NEP 2 mPa/√Hz、−6 dB 带宽 125 MHz、100 Hz 采样，对 ±10 mm 平移与 30° 偏航鲁棒，与袖带参考一致；论文号—题已核验。来源：https://www.nature.com/articles/s41467-026-77580-3 （2026-09-17）
2. 剑桥光学卷积光谱仪覆盖 1200–1700 nm、<1 秒测量、浓度精度约 0.01%、物质分类成功率 100%，在模拟生理环境测得血糖/乳酸并对一名受试者长时追踪；论文属 2026 年，10 月为再报道。来源：https://www.sciencedaily.com/releases/2026/10/261022081312.htm （2026-10-26）
3. Conavi OCTIV（OCT+IVUS）FDA 510(k) 已批，2026-11 完成美国首台商业装机，上市前两周约 25 例；二手公司聚合，细节以官方后续披露为准。来源：https://www.stocktitan.net/news/CNVIF/conavi-medical-highlights-commercial-launch-and-significant-growth-vb5k4qqycrdl.html （2026-11-19）
4. Neola 近红外早产儿肺监测 2026-09 获 FDA 突破性设备认定，2026-11 进入 TAP Pilot；**认定不等同于上市批准**。来源：https://neolamedical.com/mfn_news/neola-medical-q3-report-2026-fda-breakthrough-device-designation-strengthens-u-s-regulatory-pathway （2026-11-18）
5. 上海交大 NEO-BP：42 名新生儿、110.66 小时同步有创数据、9378 个测试片段，SBP/DBP MAE 9.67/6.17 mmHg，SQI≥0.85 时 8.22/4.98 mmHg；高运动组误差升至 14.23/11.08 mmHg。来源：https://news.sjtu.edu.cn/jdzh/20260922/226182.html （2026-09-22）
6. Happy Ring 获 510(k) 为二手行业媒体报道，编号、型号与临床验证数据公开资料未覆盖，须查 FDA 510(k) 原始库。来源：https://www.vbdata.cn/intelDetail/1118328 （2026-10-14）
7. InnoPIC 的 SiN+拉曼+SPAD+AI 无创血糖方案仍属竞赛孵化/概念阶段，未见 2026 下半年临床或产品里程碑。来源：https://www.photondelta.com/news/integrated-photonics-for-healthcare-and-biomedical （2025-08-26）

**禁用声明（forbidden claims）**：①不得把"突破性设备认定"写成"已获批上市"；②不得编造临床样本量或临床结果；③不得把单受试者/模拟环境的演示写成临床级验证；④不得把不同机构的市场口径直接相减。

## 附录 B｜evidence_table（claim | evidence/URL | strength | risk）

| # | claim | evidence/URL | strength | risk |
|---|---|---|---|---|
| 1 | 硅光光声血压传感达到可穿戴级灵敏度（NEP 2 mPa/√Hz、125 MHz、100 Hz） | Nature Communications；https://www.nature.com/articles/s41467-026-77580-3 | evidence-backed | 器件性能不等于临床精度 |
| 2 | 卷积光谱仪可在模拟生理环境测血糖/乳酸并做单受试者追踪 | ScienceDaily/Nature Photonics；https://www.sciencedaily.com/releases/2026/10/261022081312.htm | evidence-backed | 样本量=1，0.01% 为模拟环境精度 |
| 3 | 多波长 PPG 新生儿连续血压可行（MAE 9.67/6.17 mmHg） | 上海交大；https://news.sjtu.edu.cn/jdzh/20260922/226182.html | evidence-backed | 42 例小规模；跨人群泛化不足 |
| 4 | 高运动组 PPG 血压误差升至 14.23/11.08 mmHg | research_track_bio.json risks；https://news.sjtu.edu.cn/jdzh/20260922/226182.html | evidence-backed | 直接支撑"分层验证"设计动机 |
| 5 | Conavi OCTIV 已获 510(k) 并完成美国首台商业装机 | StockTitan；https://www.stocktitan.net/news/CNVIF/conavi-medical-highlights-commercial-launch-and-significant-growth-vb5k4qqycrdl.html | evidence-backed（二手聚合） | 细节以官方披露为准 |
| 6 | Neola 获突破性设备认定（≠批准）并进入 TAP Pilot | Neola Q3；https://neolamedical.com/mfn_news/neola-medical-q3-report-2026-fda-breakthrough-device-designation-strengthens-u-s-regulatory-pathway | evidence-backed（原文核验） | 易被误读为已上市 |
| 7 | Happy Ring 获 510(k)（二手报道，编号待核） | 动脉网；https://www.vbdata.cn/intelDetail/1118328 | plausible-inference（二手） | 须回 FDA 510(k) 原始库核验 |
| 8 | InnoPIC 无创血糖为概念/孵化阶段 | PhotonDelta；https://www.photondelta.com/news/integrated-photonics-for-healthcare-and-biomedical | evidence-backed | 非临床验证 |
| 9 | **公开资料未覆盖**：SPADE、剑桥光谱仪、InnoPIC 的人体大规模多中心临床样本数 | 两份 deep-research 报告一致标注；latest_biophotonics.json / research_track_bio.json | unsupported（缺口声明） | 本立项的核心研究空间，禁止以推测值填充 |
| 10 | **公开资料未覆盖**：无创血糖上市时间表、硅光芯片独立市场规模 | research_track_bio.json risks；latest_biophotonics.json risks | unsupported（缺口声明） | 不得据此做规模测算或进度承诺 |
| 11 | FDA 已发布无袖带血压设备临床性能测试指南草案 | 动脉网报道；https://www.vbdata.cn/intelDetail/1118328 | plausible-inference | 指南为草案，细节待核 |

## 附录 C｜argument_map（论证结构）

- **科学张力**：器件层（SPADE 灵敏度、剑桥光谱、NEO-BP 可行性）与监管层（Conavi 装机、Neola 认定）均在 2026 下半年取得进展，但两份报告一致把"人体大规模临床样本数"标为"公开资料未覆盖"。已知"能测"，未知"在跨人群真实佩戴下能否可靠地测、能否据此走通注册"——这一断层使临床级转化悬空。
- **中心问题**：无创硅光传感的可靠性主要由器件物理灵敏度决定，还是由人—器件—算法—场景耦合决定？后者能否被分层、量化并转化为监管可用的证据包？
- **中心论点**（假设）：灵敏度已非主要瓶颈；限制转化的是可靠性证据缺失。因此应把研究重心放在"器件—离体/动物—小规模人体—临床队列"的逐级验证，并把监管路径前置为研究变量。
- **支撑论证 1**：SPADE 与剑桥光谱仪证明器件灵敏度足够（NEP 2 mPa/√Hz；1200–1700 nm、<1 s）。**局限**：人体大规模样本未覆盖，剑桥为单受试者。
- **支撑论证 2**：NEO-BP 的 SQI≥0.85 降误差（9.67/6.17→8.22/4.98 mmHg）说明算法/质量分层可改善可靠性。**局限**：高运动组误差反弹至 14.23/11.08 mmHg，泛化不足。
- **支撑论证 3**：Conavi 510(k) 装机与 Neola 认定进入 TAP Pilot 显示监管通道已可及。**局限**：认定≠批准；Happy Ring 型二手报道编号待核，证据纪律必须收紧。
- **反论证**：也许瓶颈仍在器件物理层（拉曼血糖信号极弱，临床级精度未公开），临床验证只是"等器件成熟"，提前投入队列为时过早。**回应**：本立项把器件与临床验证并行，用 Go/No-Go 门控制风险——若体模/动物误差趋势不一致或信号不可分辨，则退回器件主线，临床队列不启动，避免沉没成本。
- **收尾结论**：把"公开资料未覆盖"从一句缺口描述，转化为一个可执行、可证伪、带失败判据的临床验证与转化研究设计，是本方向当下最紧迫且可交付的科学任务。评审应据此判断框架是否成立，而非期待本阶段给出具体样本量或注册结果。
