# 面向可比能效口径与评测基准的光计算／光子AI芯片方法学研究

## 项目名称

光计算／光子AI芯片可比能效口径与可复现评测基准研究

## 摘要（约300字）

光计算与光子AI芯片的能效宣称在快速抬高，可比性却没有同步建立。证据显示，清华"太极"报告160 TOPS/W（879 T MACS/mm²）、另有65.5 TOPS/W等数字，但这类亮眼数值被指来自未同时公布吞吐与整机功耗的研究芯片，无法做苹果对苹果比较；可核验口径只有Lightmatter Envise约0.84 TOPS/W，两者相差约两个数量级。与此同时，量产落地集中在光互连与光交换器件（OCS硅光PIC、共封装光引擎），全光计算芯片仍处实验室验证，光电反复转换的额外功耗还会抵消部分光子能效优势。口径混乱使路线选择、采购评估与标准制定缺少共同基准。本项目拟在三年内建立分层能效口径（器件级／光矩阵核级／系统级）、可复现基准套件与跨架构对照实验，把不可比宣称转化为可核验区间，明确在何种边界与负载下光计算确有能效增益，并形成工具链接口与标准建议稿。成果以方法、数据与开源工具交付，不承诺新器件流片，也不以统一业界标准为目标。

**关键词**：光计算；光子AI芯片；能效口径；评测基准；可复现性；共封装；异质集成

---

## 一、立项依据与意义

光计算正从实验室走向早期商用。2026年公开资料显示，曦智科技已完成港股上市并启动A股IPO辅导，2026年上半年营收7978万元、光互连收入6070万元占76%（[新浪，2026-11](https://k.sina.cn/article_6583770931_1886c5f3300101q10k.html)；[凤凰网，2026-11-18](https://i.ifeng.com/c/8y9xksprxK2)）；WAIC 2026上硅基光计算芯片、空间光计算方案同台亮相（[36氪，2026-07-28](https://m.36kr.com/p/3915125003703680)）。但产业的进展与评测的可信度并不同步，具体表现为三个可被证据指向的问题。

其一，**能效数字之间不可比**。聚合数据集归纳指出，仅Lightmatter Envise约0.84 TOPS/W具有可核验口径，160 TOPS/W（清华"太极"）、65.5 TOPS/W等数字来自未同时公布吞吐与功耗的研究芯片，"苹果对苹果比较尚不可能"（[Kaggle/Mind Lab数据集，2026-07-15](https://www.kaggle.com/datasets/kylefengkfeng209/photonic-ai-accelerators-vs-gpus)）。清华官网确实给出"太极"160 TOPS/W与879 T MACS/mm²，并说明论文发表于Science（[清华大学，2024](https://www.tsinghua.edu.cn/info/1175/110690.htm)）；这些是机构发布值，其系统边界与整机功耗并未在同一处给出。

其二，**原型与量产被混为一谈**。上海交大LightGen全光计算芯片端到端3.57×10⁴ TOPS、能效6.64×10² TOPS/W、计算密度2.62×10² TOPS/mm²、集成超210万光学神经元，但公开资料明确其"仍属实验室验证"；中科院上海光机所"流星一号"并行度>100亦属原型（[百度百科词条，2026-11](https://baike.baidu.com/item/%E5%85%A8%E5%85%89%E8%AE%A1%E7%AE%97%E8%8A%AF%E7%89%87/67112663)）。真正可核验量产的只是光互连／光交换器件：曦智OCS硅光PIC已量产，Lightmatter公开重心转向Passage系列（M1000总光带宽114Tbps，L200／L200X为32／64Tbps），公开资料未覆盖其2026下半年Envise新品（[insidedeeptech，2026-11](https://www.insidedeeptech.com/lightmatter-passage-photonic-interconnect-full-guide)）。

其三，**卡点本身就是评测问题**。行业归纳的四大短板包括"光电反复转换额外功耗抵消光子能效优势""软件生态零散、适配与落地成本高"，并指出共封装＋异质集成＋协同设计工具链仍未打通（[36氪，2026-07-28](https://m.36kr.com/p/3915125003703680)）。这些短板的共同特征是：缺少一个各方承认的、把转换开销与系统边界计入的能效尺子。

本项目的意义落在方法层面：给出一把可复算的尺，使宣称值能被还原为同口径的可核验区间。这直接服务于评审专家对方向价值的判断、导师对课题边界的把关，以及后续标准讨论有据可依；它不改变器件物理，但决定哪些物理进步能被领域共同确认。

---

## 二、国内外研究现状与缺口

下表逐条列出现有能效／性能数字、口径缺陷与出处。凡"公开资料未覆盖"处如实标明，不作填补。

| # | 公开数字 | 出处与日期 | 口径缺陷 | 证据强度 |
|---|---|---|---|---|
| 1 | Envise约0.84 TOPS/W，被指为唯一可核验口径 | [Kaggle数据集，2026-07-15](https://www.kaggle.com/datasets/kylefengkfeng209/photonic-ai-accelerators-vs-gpus) | 本身来自聚合数据集而非原始测试报告，仍需回原始文档核对负载、精度、边界 | 中（聚合） |
| 2 | 清华"太极"160 TOPS/W、879 T MACS/mm² | [清华大学，2024](https://www.tsinghua.edu.cn/info/1175/110690.htm) | 机构发布值；系统边界与整机功耗未在同处给出，聚合数据集据此把160列入"未同时公布吞吐／功耗"之列 | 中（发布，非第三方实测） |
| 3 | 65.5 TOPS/W | [Kaggle数据集，2026-07-15](https://www.kaggle.com/datasets/kylefengkfeng209/photonic-ai-accelerators-vs-gpus) | 与第1、2项同列，被归纳为未同时公布吞吐与功耗的研究芯片数字；对应芯片、负载、精度公开资料未覆盖 | 低—中（归纳） |
| 4 | LightGen：3.57×10⁴ TOPS、6.64×10² TOPS/W、2.62×10² TOPS/mm²、210万+光学神经元 | [百度百科词条，2026-11](https://baike.baidu.com/item/%E5%85%A8%E5%85%89%E8%AE%A1%E7%AE%97%E8%8A%AF%E7%89%87/67112663) | 实验室验证；数字经百科转述，需回Science原文核对是否含转换与主机开销 | 中（转述） |
| 5 | "流星一号"并行度>100 | [百度百科词条，2026-11](https://baike.baidu.com/item/%E5%85%A8%E5%85%89%E8%AE%A1%E7%AE%97%E8%8A%AF%E7%89%87/67112663) | 原型；不是TOPS/W，无法与第1—4项同量纲比较 | 低 |
| 6 | Q.ANT第二代NPU：LRZ独立评估较一代最高100倍性能、内部测试最高30倍能效／50倍单应用性能 | [Q.ANT，2026-05-19](https://qant.com/news/q-ant-takes-photonic-ai-computing-commercial-as-ais-power-demand-surges) | "倍"是相对值，未给绝对TOPS/W；内部测试与第三方评估边界不同；定位为GPU协处理器而非替代 | 中 |
| 7 | 曦智PACE 2：128×128光矩阵、超4万光子器件、600mm²、PCIe Gen4×16；PACE 3升至256×256 | [曦智科技，2026-11-17](https://www.xztech.ai/about-us/news/dynamic/137) | 厂商自述的硬件参数，未给TOPS/W；矩阵规模与有效算力之间缺换算口径 | 中（厂商发布） |
| 8 | "光立方"EIC与PIC峰值算力32 TOPs、1GHz、PIC时延200ps | [曦智产品页，2025](https://www.xztech.ai/products/photon-computing/lightcube) | "峰值算力"与实测吞吐、功耗的对应关系未公开 | 中（厂商发布） |
| 9 | 光本位256×256硅基光计算芯片、单晶粒超6.5万光计算单元、玻璃基光计算芯片 | [博客园行业盘点，2026-11-03](https://www.cnblogs.com/GEO-AI-20260730/p/23531781) | 被称为"全球最大／最高"属自我宣称；第三方实测流片良率、出货量、能效公开资料未覆盖 | 低—中 |
| 10 | 曦智2025年营收中光计算约20%、光互连约80%；2026H1光互连收入6070万元占76% | [华尔街见闻，2026-10-27](https://wallstreetcn.com/articles/3784581)；[新浪，2026-11](https://k.sina.cn/article_6583770931_1886c5f3300101q10k.html) | 说明量产收入来自互连而非计算，但营收结构不能反推能效 | 中 |

**缺口归纳**。第一，缺边界定义：同一TOPS/W可能指MZI器件级、光矩阵核级或含主机与ADC/DAC的系统级。第二，缺强制披露项：吞吐、功耗、精度、负载定义常不同时出现。第三，缺含转换开销的记账规则：光电反复转换的额外功耗被明确列为短板，却未进入能效分子分母的统一约定。第四，缺跨架构同任务对照：硅基MZI相干、光子存内计算、自由空间光计算与电子GPU基线之间没有共同负载套件。第五，缺第三方复现：高TOPS/W数字多为机构或厂商发布，公开资料未覆盖独立实测。已有的标准化努力集中在互连侧——OIF于2023-04-05发布首个3.2T共封装模块实施协议（[OIF，2023-04-05](https://www.oiforum.com/oif-launches-the-industrys-first-co-packaging-standard-the-3-2t-co-packaged-module-implementation-agreement/)），NVIDIA Spectrum-X Photonics以单端口1.6Tbps、整机能效提升3.5倍为宣称（[NVIDIA，2025-03-18](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Spectrum-X-Photonics-Co-Packaged-Optics-Networking-Switches-to-Scale-AI-Factories-to-Millions-of-GPUs/default.aspx)），但"计算能效"没有对应的公认口径。这就是本项目要占的方法学空位。

---

## 三、关键科学问题与研究目标

**中心问题（可检验）**：在光电混合与全光计算的器件形态、测量边界与负载定义均不一致的条件下，能否建立一套可复现、可审计、跨架构可比的能效口径与基准，使现有宣称值能被还原为同口径下的可核验区间？

**中心论点（待检验假设）**：现有光计算能效数字的数量级差异，主要来自测量边界与披露完整度的不一致，而非全部来自器件物理差异；通过统一边界定义、强制披露项与负载套件，可把不可比宣称转化为可核验区间，并暴露真实能效增益的适用范围。

**三个可检验子目标**：

- **G1 口径可还原**：形成三层边界的能效定义与最小披露清单。检验判据：对不少于5个公开案例（Envise、太极、LightGen、PACE 2／光立方、Q.ANT）逐一重算，能够逐项解释宣称值与核验值差距的来源，解释不清的项须列为"公开资料未覆盖"，不得补数。[PLACEHOLDER：解释比例阈值]
- **G2 基准可复现**：产出可复现benchmark套件（负载、输入分布、精度、温度与转换开销记账规则）。检验判据：第三方按套件独立复现Envise口径，得到的结果与公开值（约0.84 TOPS/W）在同一量级；复现次数与容差见[PLACEHOLDER]。
- **G3 对照可判决**：完成跨架构同任务对照实验矩阵。检验判据：给出同口径下的相对排序与"不可比项清单"，明确指出哪些宣称在补全边界后不再成立；若证据不足则给出Go/No-Go边界，不强出排序。

---

## 四、研究内容

**子课题1：能效指标体系与最小披露清单。** 定义三层边界：L1器件级（光矩阵／调制器本身，只计光学运算），L2核级（含光矩阵、驱动、探测与局部ADC/DAC），L3系统级（含主机、内存搬运、光电反复转换与散热）。每层规定必报字段：吞吐定义、有效位数／精度、负载与输入分布、功耗测量点、峰值／持续口径、是否含转换开销。输出为口径文档与字段字典。

**子课题2：可复现benchmark套件。** 选取矩阵乘与Transformer推理中的典型算子作为负载，固定输入分布与精度档，规定功耗采样窗口与转换开销记账方式。套件包含负载生成器、测量脚本、结果模板与审计清单，目标是把"TOPS/W是多少"改写为"在何边界、何负载、何精度下测得多少"。

**子课题3：跨架构对照实验。** 在统一负载与披露清单下，对硅基MZI相干（PACE系列公开参数）、光子存内计算（光本位公开参数）、空间光计算（每刻深思公开方案）与电子GPU／ASIC基线做同任务对照。受器件可及性限制，本子课题定位为"审慎探索"：可获得实物的做实测，只能取得公开参数的做参数级复算并标注证据等级，不把复算冒充实测。

**子课题4：工具链接口与标准建议。** 针对共封装＋异质集成＋协同设计工具链卡点，提出评测数据接口建议：仿真—版图—流片—测试各阶段应落盘的能效字段，使口径问题在工具链上游即被记录。输出标准建议稿，参考OIF在互连侧的标准化路径（[OIF，2023-04-05](https://www.oiforum.com/oif-launches-the-industrys-first-co-packaging-standard-the-3-2t-co-packaged-module-implementation-agreement/)），但不承诺被标准组织采纳。

---

## 五、技术路线与实验方案（方向级）

路线分四段，**先证据、后口径、再基准、最后对照与建议**。

1. **证据冻结与 canon 建立**：锁定本立项书使用的公开来源与日期，逐条登记 claim、URL、证据强度与风险；对"未同时公布吞吐／功耗""未覆盖第三方实测"等否定性表述保留出处，不改写为肯定。
2. **口径建模**：以Envise 0.84 TOPS/W为可核验锚点，以160／65.5 TOPS/W为不可比对立面，反推需要哪些字段才能把后者还原为前者口径；形成L1/L2/L3定义草案。
3. **基准设计与预注册**：在收集结果前固定负载、精度、容差与判定规则，避免按结论挑负载；对Envise案例做回溯复现，作为套件有效性的自检。
4. **对照与建议**：运行跨架构矩阵，区分"实测／参数复算／不可比"三态；按三态结果形成工具链接口与标准建议稿。

实验方案只到框架层：具体仪表型号、温控方式、探头布置与流片安排属操作级SOP，待硬件与经费确定后另行制定，不在此立项书展开。

---

## 六、创新点（3条可检验的具体贡献）

1. **三层边界能效口径与最小披露清单**。已有讨论把能效当作单一数字，本研究把它拆成L1/L2/L3并绑定必报字段。可检验判据：完成≥5个公开案例的口径重标注表，逐项给出"宣称值—可核验值—差距来源"三列，差距来源能归入边界、精度、负载、转换开销或"未披露"之一；无法归入的比例作为公开结果报告。[PLACEHOLDER：目标比例]
2. **面向光计算的可复现基准套件与审计清单**。区别于只比峰值的现有做法，套件强制记录转换开销与测量边界。可检验判据：第三方按文档独立复现Envise案例，量级与约0.84 TOPS/W一致；复现得到与不一致的案例数均公开，不选择性报告。
3. **跨架构同任务对照与不可比项判决**。给出MZI相干、光子存内、空间光与电子基线在同口径下的相对排序，并单列不可比项。可检验判据：产出一张对照矩阵与一份不可比项清单，明确判定"哪些高TOPS/W宣称在补全边界后不再成立"；证据不足时输出Go/No-Go判据而非排序。

三条贡献共同指向一个可证伪的命题：若重标注后差距无法用边界与披露差异解释，则中心论点被削弱，本研究据此修正而非维持原假设。

---

## 七、可行性与已有基础

**已有基础**：本立项已完成证据冻结，形成research_canon与evidence_table（见附录A、B），核心数字均有真实URL与日期；已核验清华官网160 TOPS/W与879 T MACS/mm²的原始表述、Kaggle数据集对Envise 0.84 TOPS/W与"未同时公布吞吐／功耗"的归纳、36氪对四大短板的归纳。论证地图（附录C）已明确中心张力与反论证，写作按"证据先于文字"推进。

**假设能力（需落实，均标[PLACEHOLDER]）**：[PLACEHOLDER：团队是否具备光电同测与功耗采样能力]；[PLACEHOLDER：可获得的实物平台——PACE系列／光立方／其他光电混合卡，或仅能取得公开参数]；[PLACEHOLDER：第三方复现合作方与复现次数]；[PLACEHOLDER：计算与存储资源，用于参数级复算与套件运行]。

**降承诺说明**：这是方法学立项，交付物是口径、套件、对照报告与建议稿。不承诺流片、不承诺获得厂商未披露的原始数据、不承诺标准被采纳。若子课题3的实物不可得，则退回参数级复算并明确标注，不把复算结果写成实测。

---

## 八、年度计划（3年分阶段＋交付物）

| 阶段 | 时间 | 主要工作 | 交付物 |
|---|---|---|---|
| 第一阶段 | 第1年 | 证据冻结与 canon 维护；完成L1/L2/L3口径草案与最小披露清单；对Envise、太极、LightGen做首批重标注 | 口径文档v1；字段字典；首批≥3例重标注表 |
| 第二阶段 | 第2年 | benchmark套件开发与预注册；第三方回溯复现Envise案例；按反馈修订容差与负载 | 开源套件v1（含负载、脚本、审计清单）；复现报告；中期论文[PLACEHOLDER] |
| 第三阶段 | 第3年 | 跨架构对照矩阵；区分实测／复算／不可比三态；形成工具链接口与标准建议稿；结题 | 对照矩阵与不可比项清单；标准建议稿；数据集与工具归档；结题报告 |

每阶段设置Go/No-Go检查：若披露字段无法从公开来源取得，则把该案例转入"不可比"清单，不拖延整体进度。

---

## 九、预期成果

**可测指标**：口径文档1份；最小披露清单1份；≥5个公开案例的口径重标注表；开源benchmark套件1套（仓库与DOI见[PLACEHOLDER]）；第三方复现报告≥1份[PLACEHOLDER：次数]；跨架构对照矩阵1张与不可比项清单1份；标准建议稿1份。

**数据集／工具开源计划**：负载生成器、测量脚本、结果模板、证据表与重标注表以开放许可发布[PLACEHOLDER：许可证与仓库地址]；证据表保留每条claim的URL与日期，使外部可审计、可增量更新。中期与结题论文按实际产出标注，不预设篇数。

---

## 十、风险与对策

1. **披露不足风险**：厂商与机构可能不提供功耗测量点与负载定义，导致重标注无法闭合。对策：把"未同时公布吞吐／功耗"本身作为结论证据（已有Kaggle归纳支持），转入不可比清单，不补数、不推测。
2. **证据时效风险**：2026下半年之后可能出现Envise新品或新实测，改变"0.84 TOPS/W为唯一可核验口径"的判断。对策：证据表记录日期，结题前做一次增量核验；结论表述限定在证据冻结时点。
3. **转换开销测量风险**：光电反复转换功耗难以单独分离，可能使L3口径无法落地。对策：L3先给上界／下界两种记账方式并公开差异，待条件具备再收敛；不强行给单值。
4. **口径争议风险**：三层边界可能被视为对既有发布值的贬低，引发争议。对策：定位为"并列报告"而非"取代"，保留原宣称值并注明边界；以可复算性为共同判据。
5. **标准采纳不确定风险**：建议稿可能不被标准组织采纳。对策：把交付物定义为建议稿与接口范式，其价值由第三方复现与案例采用衡量，不绑定采纳结果。

---

## 十一、经费与条件概要

[PLACEHOLDER：设备费／测试仪表与光电同测平台]；[PLACEHOLDER：流片或实物平台获取费用，若不涉流片则填无]；[PLACEHOLDER：机时、存储与软件许可]；[PLACEHOLDER：第三方复现合作与差旅]；[PLACEHOLDER：人员与研究生支持]。经费数额、来源与审批状态均待落实后填入，本立项书不自造预算数字。

---

## 参考文献

1. Kaggle / Mind Lab, *Photonic AI Accelerators vs GPUs*（聚合数据集，含Envise约0.84 TOPS/W与不可比口径归纳），2026-07-15. https://www.kaggle.com/datasets/kylefengkfeng209/photonic-ai-accelerators-vs-gpus
2. 清华大学，《电子系团队合作研发智能光芯片"太极" 赋能大模型算力》（160 TOPS/W、879 T MACS/mm²），2024-04-12. https://www.tsinghua.edu.cn/info/1175/110690.htm
3. 百度百科，《全光计算芯片》词条（LightGen 3.57×10⁴ TOPS／6.64×10² TOPS/W／2.62×10² TOPS/mm²；"流星一号"并行度>100），2026-11. https://baike.baidu.com/item/%E5%85%A8%E5%85%89%E8%AE%A1%E7%AE%97%E8%8A%AF%E7%89%87/67112663
4. 36氪，《光计算芯片，走到量产门口了吗？》（四大短板、WAIC 2026），2026-07-28. https://m.36kr.com/p/3915125003703680
5. Inside Deep Tech, *Lightmatter Passage Photonic Interconnect Full Guide*（M1000 114Tbps；L200 32Tbps／L200X 64Tbps），2026-11. https://www.insidedeeptech.com/lightmatter-passage-photonic-interconnect-full-guide
6. 新浪，《曦智科技2026H1营收与OCS硅光PIC量产》，2026-11. https://k.sina.cn/article_6583770931_1886c5f3300101q10k.html
7. Q.ANT, *Q.ANT takes photonic AI computing commercial as AI's power demand surges*（LRZ最高100倍性能、内部最高30倍能效／50倍单应用性能；IONOS首个商业客户），2026-05-19. https://qant.com/news/q-ant-takes-photonic-ai-computing-commercial-as-ais-power-demand-surges
8. 曦智科技，《天枢光电智能计算卡完成SenseNova Loop-9B Day 0适配》（PACE 2 128×128／4万器件／600mm²；PACE 3 256×256），2026-11-17. https://www.xztech.ai/about-us/news/dynamic/137
9. 华尔街见闻，《曦智营收结构：光计算约20%、光互连约80%》，2026-10-27. https://wallstreetcn.com/articles/3784581
10. 曦智科技，光立方产品页（EIC与PIC峰值算力32 TOPs、1GHz、PIC时延200ps），2025. https://www.xztech.ai/products/photon-computing/lightcube
11. 博客园GEO-AI-20260730，《国内光计算三大路线格局》（光本位256×256、6.5万光计算单元、玻璃基芯片），2026-11-03. https://www.cnblogs.com/GEO-AI-20260730/p/23531781
12. Nature, *Fully integrated perovskite active polaritonic circuits*，2026-11-18. https://www.nature.com/articles/s41586-026-11299-5
13. Nature Reviews Physics, *Photonic Ising machines towards and beyond a million spins*，2026-11-19. https://www.nature.com/articles/s42254-026-01010-y
14. OIF, *OIF launches the industry's first co-packaging standard: 3.2T Co-Packaged Module Implementation Agreement*，2023-04-05. https://www.oiforum.com/oif-launches-the-industrys-first-co-packaging-standard-the-3-2t-co-packaged-module-implementation-agreement/
15. NVIDIA Investor Relations, *NVIDIA Announces Spectrum-X Photonics Co-Packaged Optics Networking Switches*（1.6Tbps／端口、整机能效提升3.5倍），2025-03-18. https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Spectrum-X-Photonics-Co-Packaged-Optics-Networking-Switches-to-Scale-AI-Factories-to-Millions-of-GPUs/default.aspx
16. TrendForce, *NVIDIA begins shipping Spectrum-X CPO switches; optical engine yield and advanced packaging are bottlenecks*，2026-07-27. https://www.trendforce.com/presscenter/news/20260727-13151.html
17. Yahoo Finance, *Lightmatter raises $400M Series D at $4.4B valuation*，2024-10-16. https://finance.yahoo.com/news/lightmatter-raises-400m-series-d-130000982.html
18. 凤凰网，《曦智科技启动A股IPO辅导并与申万宏源签约》，2026-11-18. https://i.ifeng.com/c/8y9xksprxK2

---

## 附录A：research_canon（硬事实与边界）

- **C1 能效数字对立**：Envise约0.84 TOPS/W为可核验口径；160 TOPS/W、65.5 TOPS/W等来自据称未同时公布吞吐与功耗的研究芯片，"苹果对苹果比较尚不可能"。来源：<https://www.kaggle.com/datasets/kylefengkfeng209/photonic-ai-accelerators-vs-gpus>（2026-07-15）；"太极"160 TOPS/W／879 T MACS/mm²见<https://www.tsinghua.edu.cn/info/1175/110690.htm>（2024）。
- **C2 原型与量产界线**：可核验量产的仅光互连／光交换器件（OCS硅光PIC、CPO引擎）；全光计算（LightGen等）及多数高TOPS/W数字属实验室／原型。来源：<https://baike.baidu.com/item/%E5%85%A8%E5%85%89%E8%AE%A1%E7%AE%97%E8%8A%AF%E7%89%87/67112663>（2026-11）；<https://k.sina.cn/article_6583770931_1886c5f3300101q10k.html>（2026-11）。
- **C3 卡点**：共封装＋异质集成＋协同设计工具链未打通；光电反复转换额外功耗抵消光子能效优势；软件生态零散。来源：<https://m.36kr.com/p/3915125003703680>（2026-07-28）。
- **C4 相对倍数口径**：Q.ANT第二代NPU经LRZ独立评估最高100倍性能、内部测试最高30倍能效／50倍单应用性能，均为相对值且定位为GPU协处理器，不给绝对TOPS/W。来源：<https://qant.com/news/q-ant-takes-photonic-ai-computing-commercial-as-ais-power-demand-surges>（2026-05-19）。
- **C5 互连有标准、计算无口径**：OIF于2023-04-05发布3.2T共封装模块实施协议；计算能效未见公认口径。来源：<https://www.oiforum.com/oif-launches-the-industrys-first-co-packaging-standard-the-3-2t-co-packaged-module-implementation-agreement/>（2023-04-05）。
- **C6 公开资料未覆盖项**：大规模通用光计算芯片的量产良率、出货量与第三方实测能效；曦智PACE系列具体出货量；Envise 2026下半年新品。来源：<https://www.insidedeeptech.com/lightmatter-passage-photonic-interconnect-full-guide>（2026-11）；两份证据JSON的risks字段。
- **禁止性断言**：不得把160／65.5 TOPS/W写成"已核验的实测能效"；不得把LightGen数字写成"量产指标"；不得把Q.ANT的倍数写成绝对TOPS/W；不得用"公开资料未覆盖"处补造数字。
- **术语**：TOPS/W=每秒万亿次操作数每瓦；L1器件级／L2核级／L3系统级为本研究定义，须与厂商"峰值算力"区分；"可核验"指公开资料可复算其边界与测量点。

---

## 附录B：evidence_table

| claim | evidence / URL | strength | risk |
|---|---|---|---|
| Envise约0.84 TOPS/W是唯一可核验口径 | Kaggle数据集 <https://www.kaggle.com/datasets/kylefengkfeng209/photonic-ai-accelerators-vs-gpus> (2026-07-15) | evidence-backed（聚合） | 二手聚合，需回原始文档核对负载与边界 |
| 太极160 TOPS／W及879 T MACS/mm²为机构发布值 | 清华大学 <https://www.tsinghua.edu.cn/info/1175/110690.htm> (2024) | evidence-backed（发布） | 未给整机功耗与系统边界，非第三方实测 |
| 160／65.5 TOPS/W来自未同时公布吞吐与功耗的研究芯片 | Kaggle数据集 <https://www.kaggle.com/datasets/kylefengkfeng209/photonic-ai-accelerators-vs-gpus> (2026-07-15) | plausible-inference | 归纳性判断，非逐芯片审计；65.5对应芯片公开资料未覆盖 |
| LightGen端到端3.57×10⁴ TOPS、6.64×10² TOPS/W、2.62×10² TOPS/mm²、210万+神经元 | 百度百科 <https://baike.baidu.com/item/%E5%85%A8%E5%85%89%E8%AE%A1%E7%AE%97%E8%8A%AF%E7%89%87/67112663> (2026-11) | plausible-inference | 实验室验证；百科转述，需回Science原文 |
| 流星一号并行度>100属原型 | 百度百科 <https://baike.baidu.com/item/%E5%85%A8%E5%85%89%E8%AE%A1%E7%AE%97%E8%8A%AF%E7%89%87/67112663> (2026-11) | plausible-inference | 非TOPS/W，口径不可比 |
| 量产落地集中光互连：OCS硅光PIC量产，2026H1光互连收入6070万元占76% | 新浪 <https://k.sina.cn/article_6583770931_1886c5f3300101q10k.html> (2026-11) | evidence-backed（财报转述） | 二手转述；营收结构不能反推能效 |
| Lightmatter公开重心转光互连：M1000 114Tbps、L200 32Tbps／L200X 64Tbps | insidedeeptech <https://www.insidedeeptech.com/lightmatter-passage-photonic-interconnect-full-guide> (2026-11) | evidence-backed | 未覆盖Envise新品，不能推断其停止研发 |
| 共封装＋异质集成＋工具链卡点；光电转换额外功耗抵消光子能效优势 | 36氪 <https://m.36kr.com/p/3915125003703680> (2026-07-28) | plausible-inference | 行业归纳，非同行评议 |
| Q.ANT LRZ最高100倍性能、内部30倍能效／50倍单应用性能 | Q.ANT <https://qant.com/news/q-ant-takes-photonic-ai-computing-commercial-as-ais-power-demand-surges> (2026-05-19) | plausible-inference | 相对倍数非绝对TOPS/W；内部测试与第三方边界不同 |
| PACE 2为128×128光矩阵／4万光子器件／600mm²／PCIe Gen4×16，PACE 3升至256×256 | 曦智 <https://www.xztech.ai/about-us/news/dynamic/137> (2026-11-17) | evidence-backed（厂商发布） | 自述参数，未给TOPS/W |
| 光立方峰值算力32 TOPs、1GHz、PIC时延200ps | 曦智 <https://www.xztech.ai/products/photon-computing/lightcube> (2025) | evidence-backed（厂商发布） | 峰值与实测吞吐／功耗关系未公开 |
| 光本位256×256、6.5万光计算单元、玻璃基芯片为自我宣称 | 博客园 <https://www.cnblogs.com/GEO-AI-20260730/p/23531781> (2026-11-03) | plausible-inference | 第三方实测良率、出货量、能效公开资料未覆盖 |
| 曦智2025营收光计算约20%、光互连约80% | 华尔街见闻 <https://wallstreetcn.com/articles/3784581> (2026-10-27) | plausible-inference | 营收结构口径，不能反推能效 |
| OIF已发布3.2T CPO实施协议，计算能效无对应标准 | OIF <https://www.oiforum.com/oif-launches-the-industrys-first-co-packaging-standard-the-3-2t-co-packaged-module-implementation-agreement/> (2023-04-05) | evidence-backed | 标准存在不等于被采纳；计算侧无标准属检索结论 |
| NVIDIA Spectrum-X CPO为1.6Tbps／端口、整机能效提升3.5倍 | NVIDIA <https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Spectrum-X-Photonics-Co-Packaged-Optics-Networking-Switches-to-Scale-AI-Factories-to-Millions-of-GPUs/default.aspx> (2025-03-18) | evidence-backed（厂商发布） | 互连非计算；宣称口径未第三方核验 |

---

## 附录C：argument_map

**科学张力**：已知的一面是光计算能效宣称不断抬高（160 TOPS/W、65.5 TOPS/W、LightGen 6.64×10² TOPS/W），且器件与架构进步真实存在；未知的一面是可核验的同口径比较几乎只有Envise约0.84 TOPS/W，而量产落地集中在互连器件。为什么不把高数字直接当结论：这批数字未同时公布吞吐与功耗，且原型与量产被混用。张力的重要性在于，口径不可比会同时误导方向评估、采购判断与标准讨论。

**中心问题**：在形态与边界不一致的条件下，能否建立可复现、可审计、跨架构可比的能效口径与基准，把宣称值还原为同口径可核验区间？

**中心论点**：能效数字的数量级差异主要源于边界与披露完整度不一致，而非全部来自器件物理；统一边界、披露项与负载后可把不可比宣称转为可核验区间，并暴露真实增益的适用边界。

**支撑论证1 — 数字对立**。Envise 0.84 TOPS/W与160／65.5 TOPS/W之间约两个数量级差距，且后者被指未同时公布吞吐与功耗（Kaggle，2026-07-15）。局限：0.84本身也来自聚合数据集，必须回原始文档核对；否则锚点不稳。

**支撑论证2 — 原型／量产界线**。量产的是光互连（OCS硅光PIC、Passage系列、CPO），全光计算仍实验室验证（新浪2026-11；insidedeeptech 2026-11；百科2026-11）。局限：商业信息多为厂商或二手来源，量产与试点的界线可能随时间移动。

**支撑论证3 — 卡点即评测问题**。光电转换额外功耗抵消优势、软件生态零散、工具链未打通（36氪，2026-07-28）；互连侧已有OIF标准而计算侧无口径（OIF，2023-04-05）。局限：行业归纳非同行评议；"无标准"是检索结论，需持续复核。

**支撑论证4 — 相对口径不可通约**。Q.ANT以倍数报告且区分内部测试与LRZ评估（Q.ANT，2026-05-19），说明即使有第三方参与，边界不同仍不可通约。局限：单一案例，不足以代表全行业。

**反论证**：（a）统一口径可能抹平架构创新差异——MZI相干、衍射、存内计算的物理机制不同，单一数字会掩盖各自适用场景。回应：采用L1/L2/L3并列报告，不设单一排行榜。（b）标准化成本可能使初创无力参与，反而固化大厂优势。回应：最小披露清单只要求公开已有字段，不要求新增流片或仪表。（c）若统一后光计算能效不再亮眼，方法学会被视为"打压新技术"。回应：结论限定在证据冻结时点，且明确"在何边界下仍有增益"，不预设正反。

**收尾结论**：领域当前缺的不是又一个更高的TOPS/W，而是一把可复算的尺。本立项的交付是一套口径、一个套件、一张对照矩阵和一份建议稿；它们的价值由第三方复现与案例采用检验，而不是由宣称值大小检验。评审应据此判断：这是把不可比宣称转为可核验知识的基础工作，而非器件竞赛的又一轮加码。
