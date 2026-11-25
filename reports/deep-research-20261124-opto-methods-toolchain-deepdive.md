# 光电信息工程：研究方法论与工具链深挖
生成日期：2026-11-24　｜　层级：从物理极限下沉到怎么算、怎么做、怎么测的方法与工具
## 范围
本报告是光电信息工程深度调研的方法论层，聚焦 6 个主题：电磁仿真与设计工具链、微纳制造工艺、表征与测试方法、可靠性与失效分析、AI 辅助设计、标准计量与测试规范。与前序物理极限报告不重叠——回答的是「怎么算出来、怎么做出来、怎么测出来、怎么验可靠」。
## 研究方法
deep-research-pro 外部检索闭环：每个主题换关键词重试≤2轮，到顶标未覆盖；WebFetch 深读 Top3-5 篇一手资料；每条主张附出处链接（方括号外链标记后紧跟来源，例：[外]（出处：https://www.nature.com/）示例主张）；单一来源标未验证；优先一手论文与权威机构（Nature/Science/Optica/IEEE/NREL/IRENA）；数字标口径；区分理论极限与实测值；不补写、不臆造。
六个主题共梳理 **75 条方法**：一手核验 **50** 条，确认未覆盖 **8** 条，汇集唯一来源 **188** 个。
## 核心结论
### 电磁仿真与设计工具链
- FDTD 的主流误差预算不是网格色散，而是 PML、阶梯化/亚像素、材料数据拟合与有限仿真域；Ansys 2D Mie 案例中精细网格后 FDTD-Mie 差 0.15%，但换材料数据源就到 4.2%，说明仿真-实测差距常被材料与工艺主导。
- 算力口径要成对报：mesh accuracy 4≈18 点/波长；Meep 高 Q 腔 Q~1e7 需 4e7 光周期，Harminv 用约 1000 周期带来约 4 个数量级运行时收益；MPB 3D 10 能带×31 k 点×16³ 网格 8 秒（2.8 GHz Opteron）。
- 方法选择由结构决定：FDTD 宽带全波、FEM 复杂几何/多物理/窄带、BPM 单向波导近似、RCWA 分层二维周期；COMSOL 二阶单元实用网格 5–10 个/波长、CFL≈0.1，与 FDTD 的 Courant 口径不可混用。
- 逆向设计的成本结构是每轮 1 次前向 + 1 次伴随仿真，与参数维度近似无关；lumopt 4 通道实例约 1000 次迭代、数小时到数天；优化前必须先做正演收敛测试。
- 多物理耦合的关键是可信数据桥梁：Mechanical HEX20 应力/变形经 Python 插值成 Lumerical (n,k) 网格；只算应力使 MRR 位移 0.25–0.5 nm，叠加 dn/dT=1.8e-4/K 后可达 nm 量级，温度项不可省略。
- 开源三件套 MEEP/MPB/S4 均 GPL v2+，可脚本化、可并行且适配逆设计；商用工具价值在多物理互操作、EDA 衔接（GDSII/compact model/MC 良率）与工程化支持。
### 微纳制造工艺方法
- 目标层是工艺方法而非产能新闻: 决定光子器件极限的是图形化(光刻/NIL)、图形转移(刻蚀)、成膜(沉积)与集成/封装(键合/转印/耦合)四条工艺链, 各自有独立的精度/损耗/良率瓶颈。
- EUV(尤其高NA)把 CMOS 图形化推到单次曝光 8nm/16nm pitch, 但焦深随 NA² 下降(高NA减 2-3 倍)、胶厚需<20nm, 且光子器件特征多>50nm, 量产主力仍是 193nm 浸没式与 NIL; EBL 用于原型与母版。
- NIL 是光子器件最具性价比的图形化路线: sub-20nm overlay(200mm)、sub-10nm 分辨率、低压室温 UV 压印, 但胶折射率(1.5-1.6)与母模寿命/多层对准是瓶颈, PER 填充胶(1.8-2.0)正在补折射率短板。
- 刻蚀侧壁粗糙度是硅光损耗主因: σ≈10nm 即显著散射, 用 SiO2 硬掩模+优化氟基 RIE 可把传播损耗压到 0.89dB/cm; 氧化平滑是关键抑损手段。
- 异质集成三条路各有精度-成本定位: 混合键合对准到亚微米(pad 1µm 需 100-250nm 键合机精度, W2W 向 200nm pitch), 微转印对准±0.5-1.5µm 但材料兼容性最好, 单片集成对准最优但热预算/晶格失配受限。
- 耦合与封装是光子集成的隐性主导成本(封装占模块成本可达 80%): 光栅对准容差宽(1dB±2.5µm)适合晶圆级测试, 边缘耦合效率高但需 sub-micron 对准; 胶固化收缩 1.5%×20µm=0.3µm 已占 4µm 耦合器 1dB 预算 1/3。
- 工艺变异下微环对 1nm 线宽偏差即产生谐振漂移, 必须从'工艺完美'转向'统计鲁棒设计'+后工艺微调。
- 单源/片段证据(EBL 吞吐、湿法刻蚀选择比、溅射应力、ALD 均匀性、气密水汽率、单片集成热预算、工艺变异敏感度)尚需一手正文深读才能升级为可引用硬数字。
### 表征与测试方法学
- 测量口径比测量本身更容易出错：调制器『3dB带宽』用光功率还是电 S21 读数可差 1.4–4.7×（光3dB=VNA 6dB）；探测器带宽用电流幅值还是功率定义差 3dB；这类口径混用是最大系统误差源。
- 全部损耗类测量(cut-back、晶圆端口插损)的本质困难是『耦合/对准变化』与『器件本征变化』混叠在一个读数里；解法共同指向——先证明重复性、把界面变稳，再用长度扫描或近场在路成像把两者拆开。
- 窄线宽测量存在方法学天花板与陷阱：延迟自外差要够长延迟才满足非相干(>6τc)却同时引入 1/f 频率噪声虚高(50km 把 5.1kHz 读成 31.77kHz)；短延迟+包络极值反演可抑制，频率鉴别法可下探到 0.7 Hz，但综述明确『测量技术落后于光源发展』、无单一方法通吃 GHz→亚Hz。
- 探测器量级陷阱：50Ω 未放大时热噪声 NEP≈18 pW/√Hz，比 10nA 暗电流的散粒限 0.06 pW/√Hz 高约300倍；报 NEP 必须注明是裸探测器还是含部署态放大器、负载阻抗与带宽。
- 计量可溯源性决定绝对精度上限：响应度靠 NIST 可溯源参考表(±2–5% 常规)，光功率绝对定标靠低温辐射计(0.02%, k=2)；相对测量(拍频、cut-back 斜率)精度可远高于绝对测量。
- 瞬态效应让标准方法失效：暗电流 I-V 扫描在有电荷俘获/离子迁移时不适用，回滞与扫速依赖是诊断信号；线性度须在接近 NEP 的低功率端验证。
- 厂商与二手技术手册(inZiv/Photonica/Keysight 产品页)提供了大量可复算的实测数字，但缺独立第三方验证，已在 status 中标单源未验证；一手论文/权威(Nature/PMC/NIST)正文核实的才标已核验。
### 可靠性与失效分析方法
- 方法层主线：先界定失效机理→选不跨机理的加速应力（温度/电压/电流/湿度/机械）→用Arrhenius/Eyring/Black/Coffin-Manson/威布尔模型外推→用现场失效分析回校；没有机理确认的外推只是曲线拟合。
- Telcordia GR-468-CORE把激光器可靠性变成可审计流程：逐只85°C/48h burn-in + 12组×11只加速试验零失效、ΔP≤10%（或0.5 dB）/Δλ≤0.1 nm；GR-468加速老化CO 70°C/2000 h、UNC 85°C/2000 h是方法中最核心的标准硬数字。
- Intel混合激光器给出“加速试验<0.1 FIT（>55000只）”与“现场0.05 FIT（>6百万只、3年、100%FA确认）”的同向印证，说明光模块FIT应同时给加速上界与现场点估计，而不是二选一。
- 硅光失效的新增维度是光参数本身：PD暗电流、波导插损、VπL相移效率与耦合效率都进入失效判据；热应力通过折射率变化直接变成相位误差/BER退化，IRPS 2026称其为系统级多物理场问题。
- 统计是薄弱环节：R=0.999/CL=95%/β=1/1倍寿命零失效要求2995只；16只激光器1000 h加速外推个体寿命360–16460 h（约45×离散），少数样本外推必须同时报告β、置信区间与加速模型适用边界。
- 标准正文可得性缺口：JEDEC JESD22-A104官方PDF需登录，IEC TR 62721正文未取到，GR-326插拔寿命循环数未核验——这三类数字只能引用厂商认定计划或摘要，并在报告中标注口径。
### AI辅助设计方法学
- 伴随法的核心价值是梯度成本与参数数解耦：一次前向+一次伴随仿真即可给出全部设计变量梯度，因此拓扑优化能支撑数千自由度；代价是每轮仍需 >100 次全波仿真且非凸易陷局部最优。
- 所有 AI 辅助方法的共同瓶颈是数据/仿真成本：代理模型需数千个全波仿真标注样本，扩散模型用 15,000 个训练图案，PIRL 用 20,000 组伴随梯度对——物理信息( Maxwell 残差、伴随梯度、PINN PDE 损失)是降低样本复杂度的主线条。
- 仿真-实测差距是方法落地的硬约束：SiN WDM 模拟串扰−8dB 实测退化到 O 波段≈−3dB，归因于侧壁角与间隙填充；PRISM 指出『几何接近≠功能接近』，需以伴随灵敏度加权的功能保真而非像素级几何匹配做掩膜优化。
- 2025-2026 前沿从单一 NN 转向混合范式：物理引导生成模型(MxDiffusion 用 Maxwell 残差做中间 E 场表征)、物理信息 RL、可微求解器、LLM/Agent 编排，用领域物理换取样本效率与泛化。
### 标准计量与测试规范
- 标准分层：IEEE 802.3 定义光 PHY 的波长/速率/距离，OIF IA 定义相干/CPO 的互操作协议，MSA（OSFP/QSFP-DD）定义形态与电接口——三者共同构成光模块可互换的规范栈；产品验收须逐层对齐，缺一层即不互操作。
- GR-2854-CORE 的关键纠偏：它实际是『光纤色散补偿器通用要求』(Issue 2, 2013-01-12)，不是通用光接口规范；真正的光电器件可靠性基线是 GR-468-CORE。把两者混用是研究/验收的典型错误。
- CPO 标准化已落地：OIF 3.2T Co-Packaged Module IA（OIF-Co-Packaging-3.2T-Module-01.0, 2023-03-29）是业界首个共封装标准，标志光电接口从可插拔走向封装内定义；但 LPO 尚无一手带编号 IA，仍是开放标准缺口。
- 光伏效率的可比性建立在 STC=1000 W/m²+AM1.5G(ASTM G173-03)+25 °C 的刚性口径上，并靠 NREL/Fraunhofer ISE 跨实验室循环比对（7 组件×4 实验室×3 大洲）压缩不确定度；真实工况光谱失配是效率偏差主因。
- 激光安全是直接的设计约束：IEC 60825-1:2014 用 AEL=MPE×限制光阑面积分级（Class2=1 mW/0.25 s/400–700 nm、3R=5 mW、3B=500 mW、4>0.5 W），决定光功率/波长/封装的可允许工作点。
- 量值可复算是计量根基：NIST 光谱响应度标尺 200–1800 nm、千瓦级 NIST-PTB 光子动量比对、CCPR-K1.a 光谱辐照度 250–2500 nm 比对，经 GUM(JCGM 100:2008, U=k·uc) 评定不确定度，再由 CIPM MRA/KCDB 互认把量值传到产业仪表（建议 12 个月复校）。
## 关键要点
**电磁仿真与设计工具链** 的开放问题：
- CST 在光子/纳米光学器件上的一手精度与运行时基准未覆盖；两轮换词后停止。
- Lumerical Courant 时间步 0.99 理论上限与 lumopt 约 1000 次迭代/数小时至数天来自 Ansys 官方搜索摘要（原页 Cloudflare 拦截），按单源未验证处理。
- RCWA 529 harmonics / 22.8× GPU 加速来自 2026 预印本单源，尚未用 S4 官方或同行评审版本交叉验证。
- 商用工具（Ansys/COMSOL/RSoft/CST）的具体授权计价与算力限额本次未纳入，只核实授权类型。
- 未获取 BPM 与 FDTD/RCWA 在同一光子器件上的同口径数值误差对照实验。
**微纳制造工艺方法** 的开放问题：
- EBL/CEBL 的分辨率-套刻-throughput 三方硬数字(如最小线宽 nm、overlay nm、wafer/hour)未逐字核验, 需读 MAPPER/CEBL 原始论文正文。
- 湿法刻蚀各向异性比与选择比(KOH/TMAH 晶面速率比、BOE 对 Si/SiO2 选择比)未覆盖, 需权威工艺手册一手数据。
- 溅射光学薄膜的厚度均匀性/折射率/应力硬数字未覆盖。
- ALD 光学镀膜厚度均匀性与应力硬数字未取得(正文被付费墙/题录限制)。
- 气密 vs 非气密封装的水汽透过率/氦漏率硬数字未覆盖, 仅有 Telcordia GR-1221 可靠性判据。
- 单片(monolithic)异质集成专门的对准精度与热预算硬数字未覆盖。
- 工艺变异→波长漂移/插损的敏感度系数(nm 偏差→nm 波长漂移、dB 插损)缺可核验正文; Synopsys 白皮书 PDF 被 402 拦截, 需换通道获取。
- ASML DUV/EUV 官方产品规格页正文被 404 拦截, 现有 DUV 数字来自搜索片段, 需用 ASML 产品手册或权威 foundry 白皮书复核。
**表征与测试方法学** 的开放问题：
- Keysight N4391A/N4391B 光调制分析器的 EVM 精度与带宽规格未取到(datasheet 直抓只有导航壳)；BERT 的 BER 测量下限与眼图抖动分解精度需以原版 datasheet/应用笔记补齐。
- 光子器件专用的共聚焦/超分辨分辨率极限一手实测数字缺失(PMC 综述遇 reCAPTCHA)，两轮关键词到顶标未覆盖；若需精确口径应换出版商原文或 DOI 直连重取。
- 晶圆级光测试的吞吐硬指标(每小时 uph、每 die 对准时间分布、KGD 判据良率相关)只有厂商自述，缺独立基准测试；CPO 高密度下每晶圆数千光 I/O 的具体数字仅搜索片段。
- add-drop ring 法与 cut-back 法测同一低损耗波导的交叉比对(一致性/偏差)未见直接一手数据，Vermeulen 2016 ring 法正文未深读。
- NSOM 分辨率数字(0.25 μm 线宽/0.07 μm 边缘锐度)来自 1987 AIP 搜索片段，原文被 Cloudflare 拦截未核；现代 s-SNOM 在集成光子器件中的定量损耗成像精度待补。
**可靠性与失效分析方法** 的开放问题：
- 氢逃逸/氢外扩散在硅光波导与掺锗光纤中的激活能、加速试验条件与损耗量化关系未覆盖（两轮检索上限）。
- 连接器插拔寿命的权威循环数（GR-326/IEC 61300-2-22原文）与端面污染—插损退化—损伤的定量映射未取得一手标准全文。
- JEDEC JESD22-A104/A101条件字母与光引擎适用判据的完整表（官方PDF受限），当前仅有TI/onsemi等厂商计划转述。
- 光致退化论文的Erdogan模型数字取自Optica摘要页的表格抓取（表头符号丢失），需原PDF复核1.32/1.50 eV与FWHM 0.31/0.34 eV的列含义，并补第二来源。
- 热载流子效应在硅光相移器/调制器中的独立加速模型与硬数字（区别于Ge PD缺陷产生）未找到可核验来源。
- IEC TR 62721:2012正文中的浴盆曲线分段假设、Weibull/lognormal选择与现场-设计可靠性对应关系未取到，仅检索摘要。
**AI辅助设计方法学** 的开放问题：
- LLM/Agent 驱动光子设计(arXiv:2611.08127、2604.01480、2608.20688、2606.00915、2508.10277、2608.18279)本轮仅命中摘要未深读全文，其实测验证与相对基线的量化增益尚未核验，标注单源未验证。
- 代理模型与扩散模型的泛化误差缺少可跨任务引用的统一数值口径，多数论文仅在各自设计空间内报告相对基线提升。
- PINN 用于光学逆问题的计算速度相对成熟 FDTD/FDFD 求解器尚无统一 benchmarks；beam-shaping PINN(arXiv:2607.18012)与近场 PINN(doi:10.1364/ol.586379)未深读。
- RL 的 PCSEL 结果(波长误差降64%、功率增47%)为仿真值，尚缺流片实测验证；PRISM 的良率提升也未给统一百分比。
- 光子晶体扩散设计论文(PMC12717900)WebFetch 返回 reCAPTCHA 未读到正文，其内容未纳入结论，仅记录检索命中。
**标准计量与测试规范** 的开放问题：
- LPO（Linear Pluggable Optics）是否有正式、带编号的 OIF/MSA Implementation Agreement？本次两轮检索未核到一手原文，仅有 448G workshop 与 CMIS 线索——需查 OIF Implementation Agreements 列表页与 OIF 2024–2026 新闻稿确认。
- ESTI（欧盟 JRC 光伏认证）的具体测量不确定度预算与认证流程文档未核到一手来源；NREL 与 Fraunhofer ISE 已核，ESTI 待补。
- IEEE 802.3bs/df 光 PMD 的具体波长与功率/眼图限值（如 400GBASE-FR4/DR4、800GBASE）未从 IEEE Xplore 一手正文核到（付费墙）；当前仅有标准编号体系与 MSA 合规声明交叉印证。
- OIF 400ZR-02.0、3.2T CPO IA、Telcordia GR-468/GR-2854、IEC 60825-1 AEL 表、Fraunhofer ISE 不确定度 PDF 的一手 PDF 正文抓取被 challenge/付费墙拦截，本次引用以一手页面摘要 + 搜索片段 + 权威二手交叉印证为主；逐条限值数值需在可下载原文中复核。
- GR-2854-CORE 与 GR-468-CORE 在产业 datasheet 中常被笼统写为『Telcordia 合规』，二者适用范围差异（DCM vs 光电器件可靠性）在验收条款中是否被正确区分，需按具体产品规范逐项确认。
## 方法逐条核实
### 电磁仿真与设计工具链
#### 1. FDTD 原理与数值误差来源（Yee 网格 / Courant / 色散 / 阶梯化 / PML / 材料拟合）
- **方法原理**：把空间离散成 Yee 网格，在时间上显式推进 E/H；二阶精度格式在均匀介质中对网格分辨率呈二次收敛，但材料界面不连续会把 O(Δx²) 降为 O(Δx)。误差不是只由网格大小决定：PML 反射及倏逝场接触 PML 会移动/压低谐振 Q；网格色散使有限 dx/dt 下色散关系偏离自由空间；阶梯化带来几何误差；色散材料须拟合为多系数模型(MCM)才能在时域更新，拟合本身有残差；有限 dt 下数值介电常数与 MCM 极限不同；非均匀网格的渐变区会产生微弱增益/损耗与散射，细网格区易困住高频并产生下采样混叠；源的模式轮廓只在中心频率精确，宽带仿真偏离中心频率会引入反射；监视器默认场插值也有误差。
- **硬数字**：Meep：Courant 因子默认 S=0.5，cΔt=SΔx，稳定条件 S≤n_min/sqrt(维数)；resolution 默认 10 pixel/距离单位；双精度计算，HDF5 可改单精度输出省 2 倍空间；亚像素平滑把无平滑的一阶收敛恢复到近似二阶，仅适用于无损、频率无关介质（硅 1.55 μm 是典型例子），界面处仍至多一阶。Ansys Lumerical：时间步默认取理论最大步长的 0.99（由 Courant 稳定判据算得）；mesh accuracy 1–2 用于初算，4 档对应每波长约 18 个网格点。网格细分下限：单精度约 dx~λ/1e7、双精度约 λ/1e16（1000 nm 光对应约 1e-4 nm），实际远未触及。2D Mie 金纳米线实例中，64 层 PML + dx=0.1 nm + mesh accuracy 4 + 2 μm 仿真域，消光截面与 Mie…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://meep.readthedocs.io/en/latest/Scheme_User_Interface/）来源链接
  - [外]（出处：https://meep.readthedocs.io/en/latest/Subpixel_Smoothing/）来源链接
  - [外]（出处：https://kb.lumerical.com/en/layout_analysis_test_convergence_fdtd.html）来源链接
  - [外]（出处：https://kb.lumerical.com/redirect/fdtd-fix-divergence.html）来源链接
  - [外]（出处：https://kb.lumerical.com/en/ref_sim_obj_simulation_fdtd.html）来源链接
#### 2. FDTD 典型光子器件仿真精度与算力开销
- **方法原理**：精度靠逐项收敛扫描量化：Ansys 官方定义 Δσ(i)=sqrt(∫(σ_i-σ_{i-1})²dλ/∫σ_i²dλ) 作为相邻参数步的相对差，Δσ_N(i)=sqrt(∫(σ_i-σ_N)²dλ/∫σ_N²dλ) 作无解析解时的绝对误差估计；先扫便宜的 PML 距离/层数，最后才扫最贵的网格。算力开销随网格点数与步数上升（3D 尤为受限）。对高 Q 慢衰减腔，直接时域需追到场衰减，可用 Harminv 信号处理和频域迭代求解器替代。
- **硬数字**：2D 金纳米线 Mie 案例（直径 140 nm，300–1000 nm）：PML 距离约 1 μm 时误差<1e-3(0.1%)；PML 层数 2–32 层贡献约 3e-5(0.03%)；mesh accuracy 4 贡献约 1e-3；内网格 dx=1 nm 时绝对误差约 1%，3 nm 处 Δσ 走平（其他误差主导）；加到 64 层 PML 后 dx=0.1 nm 误差降至约 2.5e-3(0.25%)。改用 Johnson-Christy 原始材料数据而非作者 MCM 拟合，误差跃至约 4.2%，且不同文献金光学常数彼此差异更大；mesh accuracy 2 + 1 nm 网格的算例 '可在几秒内完成'。Meep 环形腔 Q~1e7：直接时域需约 4×10^7 个光周期解析衰减，Harminv 只用约 1000 个周期，运行时长约降低 4 个数量级；Meep 频域求解器 BiCG…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://r.jina.ai/https://kb.lumerical.com/en/layout_analysis_test_convergence_fdtd.html）来源链接
  - [外]（出处：https://kb.lumerical.com/en/layout_analysis_test_convergence_fdtd.html）来源链接
  - [外]（出处：https://meep.readthedocs.io/en/latest/Subpixel_Smoothing/）来源链接
  - [外]（出处：https://meep.readthedocs.io/en/latest/Scheme_User_Interface/）来源链接
#### 3. FEM（COMSOL Wave Optics）适用边界与网格口径
- **方法原理**：有限元解频域时谐 Maxwell 方程（电场为未知量），适合复杂几何、各向异性/多物理场、窄带高 Q 与模式本征值问题；对传播方向快速振荡的光波代价高，故 COMSOL 提供 Beam Envelopes（包络场）接口把快振荡解析提出来，只求解慢变包络，适合长距离波导/透镜；模式分析则用 FEM + 本征值求解器解 Helmholtz 方程。瞬态波动问题用二阶二次单元，需空间与时间同时分辨波。
- **硬数字**：COMSOL 官方 KB1118：默认二阶(quadratic)单元，Nyquist 最低 2 个单元/局部波长但精度不可接受；实用建议每个局部波长至少 5 个二阶单元、很少超过 10 个；时间步 Δt=CFL/(N·f_max)，二阶单元 CFL<0.2、0.1 接近最优；声学瞬态接口默认手动步长 1/(60·f_max)，对应 6 单元/波长时 CFL=0.1。推荐 Generalized alpha 时间步进。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.comsol.com/support/knowledgebase/1118）来源链接
  - [外]（出处：https://comsol.com/blogs/how-to-use-the-beam-envelopes-method-for-wave-optics-simulations）来源链接
  - [外]（出处：https://comsol.com/blogs/mode-analysis-for-electromagnetic-waveguides-in-comsol）来源链接
  - [外]（出处：https://blogs.ethz.ch/ps_comsol/files/2020/05/WaveOpticsModuleUsersGuide.pdf）来源链接
#### 4. BPM（RSoft BeamPROP）适用边界与取舍
- **方法原理**：光束传播法把 Maxwell 方程化为沿传播方向 z 的初值问题，原始 BPM 基于慢变包络近似/近轴单向模型，只能算前向传播、不能严格处理强反射、大角度散射与背向耦合；后续有广义/双向改进版。RSoft 工具链中 BeamPROP 面向集成与光纤波导器件，配套 FullWAVE(FDTD)、DiffractMOD(RCWA) 与有效折射率法(EIM)把 3D 近似降为 2D 以省算力。
- **硬数字**：Synopsys 官方资料称 BeamPROP 为 'industry-leading' BPM 工具，并给出 EIM 白名单式用途：3D→2D 近似大幅降低时间与内存（未给具体加速倍数）；本次未取到 BeamPROP 官方页面的可核验精度/速度硬数字（页面 HTTP 403）。方法学上 BPM 与 FDTD/RCWA 的取舍属单向传播近似 vs 严格全波。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://www.synopsys.com/photonic-solutions/rsoft-photonic-device-tools/passive-device-beamprop.html）来源链接
  - [外]（出处：https://www.synopsys.com/photonic-solutions/rsoft-photonic-device-tools/rsoft-products.html）来源链接
  - [外]（出处：https://qacf-www.synopsys.com/content/dam/synopsys/photonic-solutions/documents/whitepapers/rsoft-effective-index-method.pdf）来源链接
  - [外]（出处：https://en.wikipedia.org/wiki/Beam_propagation_method）来源链接
#### 5. RCWA / 傅里叶模态法（S4）用于光栅与超表面
- **方法原理**：Stanford S4 是频域求解器：对 2D 周期、分层平面结构把 Maxwell 方程按 Fourier 级数展开（RCWA/FMM），用 S 矩阵算法递推层间散射，直接给透射/反射/吸收谱、场分布及线/体积积分；周期天然满足，谱极光滑，适合周期超表面与局部/全局优化。能力边界：要求分层 + 2D 周期；截断的 Fourier 阶数决定精度；非周期/任意 3D 结构不适用，需改用 FDTD/FEM。
- **硬数字**：S4 1.1.1 为最新 Lua 5.2.x/Python 版，1.0 为 CPR 论文原版；CPC 183, 2233 (2012) 为其一手论文。GitHub 接口注释以 n 为 Fourier 阶数（2n/4n 展开）。2026 年一篇预印本报告 529 个 Fourier harmonics 下 GPU 上 BCM 层构建比传统特征分解快 22.8 倍（单源、预印本，非 S4 官方）。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://web.stanford.edu/group/fan/S4）来源链接
  - [外]（出处：https://web.stanford.edu/group/fan/publication/Liu_ComputerPhysicsCommunications_183_2233_2012.pdf）来源链接
  - [外]（出处：https://doi.org/10.1016/j.cpc.2012.04.026）来源链接
  - [外]（出处：https://github.com/victorliu/S4/blob/master/S4/rcwa.h）来源链接
  - [外]（出处：https://arxiv.org/pdf/2608.06185）来源链接
#### 6. 主流商用/开源工具能力矩阵与授权模式
- **方法原理**：Lumerical(Ansys)：FDTD 全波 + MODE(FDE/EME/varFDTD) + INTERCONNECT 线路级 + CHARGE/HEAT 多物理 + lumopt/lumopt2 逆设计，商业授权；COMSOL Multiphysics + Wave Optics，FEM 为主、全耦合多物理，商业授权；RSoft(Synopsys)：BeamPROP(BPM)/FullWAVE(FDTD)/DiffractMOD(RCWA) + CAD，商业授权；CST Studio Suite(Dassault)：FIT/频域与瞬态及 FEM 多求解器，商业授权；MEEP：GPL FDTD（Python/Scheme/C++，MPI 并行，含 adjoint solver 与 GDS import），MPB：GPL 平面波展开求周期结构能带/模式（支持 MPI、各向异性、目标频率本征求解，不支持损耗/色散），S4：GPL RCWA + S 矩阵。
- **硬数字**：MEEP、MPB、S4 均为 GPL v2 或更高（官方 License 页逐字确认；S4 用户自写 Lua 脚本不算衍生作品，MEEP 用户自写 Python/Scheme 控制脚本同理，链接 MEEP C++ 库分发则受 GPL 约束）；MPB 官方案例：3D 介质球金刚石晶格最低 10 条能带、16×16×16 网格、31 个 k 点共 8 秒（2.8 GHz AMD Opteron，ATLAS BLAS），即每 k 点 81920 自由度 0.26 秒。Lumerical lumopt2 示例明确要求有效 Lumerical FDTD 授权且 2026 R1.2 及以上。商用工具授权条款为商业许可，本次未逐项抓取报价。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://meep.readthedocs.io/en/latest/License_and_Copyright/）来源链接
  - [外]（出处：https://mpb.readthedocs.io/en/latest/）来源链接
  - [外]（出处：https://web.stanford.edu/group/fan/S4/license.html）来源链接
  - [外]（出处：https://lumerical.docs.pyansys.com/version/stable/examples/lumopt2/y_branch/pylumerical_y_branch.html）来源链接
  - [外]（出处：https://www.synopsys.com/photonic-solutions/rsoft-photonic-device-tools/rsoft-products.html）来源链接
  - [外]（出处：https://www.3ds.com/products/simulia/cst-studio-suite/electromagnetic-simulation-solvers）来源链接
  - [外]（出处：https://www.comsol.com/products/licensing/）来源链接
#### 7. 光-热-电-应力多物理场耦合与 Lumerical↔Ansys 互操作
- **方法原理**：CPO/封装翘曲链路：Ansys Mechanical 用 HEX20 实体单元解热-结构（CTE 失配 → 翘曲 + 应力 σ=EαΔT），把节点的变形/应力用 Python 插值到笛卡尔网格，转成空间 (n,k) 材料对象喂给 Lumerical FDTD；弹性光效应与热光效应共同改变有效折射率，进而移动微环谐振波长。其他链路：Mechanical 应变 → MODE FDE 求 Δn_eff 与相位 → INTERCONNECT 系统级噪声/探测；Icepak 温度图 → FDTD 光栅耦合器；RHSC ET/SIwave 温度图 → 折射率扰动。边界：插值只能内插不能外推，需区分网格点是否在结构内；不同材料弹性光系数不同；大芯片中心到边缘变形不均与插值速度仍是待改进项。
- **硬数字**：Ansys 2025 CPO 互操作 webinar：应力-free 参考 25 °C，回流峰值 260 °C；MRR 变形约 0.3 nm；ΔT=50 K 时 Si 应力 19.5 MPa（E=150 GPa, α=2.6e-6/K）、SiO2 1.75 MPa（E=70 GPa, α=0.5e-6/K）；仅应力的谐振波长 22→75 °C 位移 +0.25 nm、22→125 °C +0.5 nm，FSR 约 8.4 nm（公式给出，谱读数约 9 nm）；若叠加热光 dn/dT=1.8e-4/K，ΔT=50 K 给 Δn=0.009，位移可达 nm 量级。DFOS 示例：15 mm 光纤嵌 SS360，压力扫描脚本约 10 分钟，噪声标准差 0.495 mW 时 >35 MPa 才正确定位扰动（1.112 km）。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://ansys.com/content/dam/web/webinars/ansys-cpo-multiphysics-lumerical-mechanical-interop-flow.pdf）来源链接
  - [外]（出处：https://r.jina.ai/https://ansys.com/content/dam/web/webinars/ansys-cpo-multiphysics-lumerical-mechanical-interop-flow.pdf）来源链接
  - [外]（出处：https://optics.ansys.com/hc/en-us/articles/46499056867603）来源链接
  - [外]（出处：https://r.jina.ai/https://optics.ansys.com/hc/en-us/articles/46499056867603）来源链接
  - [外]（出处：https://optics.ansys.com/hc/en-us/articles/5258777726227-Thermally-aware-photonic-circuit-simulation-of-a-WDM-transceiver-Icepak-integration）来源链接
  - [外]（出处：https://kb.lumerical.com/en/ref_scripts_addimportheat.html）来源链接
#### 8. 光子器件逆向设计：伴随法、拓扑优化、遗传算法与 ML 代理模型
- **方法原理**：伴随法把 N 维参数梯度压缩为每轮固定两次全波仿真（前向 + 伴随），与参数个数近似无关；拓扑优化把设计区每个像素的介电常数当变量，经滤波/二值化转成可制造版图；形状/参数优化用有限维控制点；遗传算法等无梯度方法每代需大量正演；ML 代理模型用于替代重复正演或生成紧凑模型。前置条件：正演本身必须已收敛，否则优化的是数值误差。边界：伴随梯度要求 FOM 光滑；二值化、制造约束和工艺扰动会改变最优解。
- **硬数字**：lumopt2（Ansys Lumerical 2026 R1.2+）官方示例：每轮 adjoint gradient = 1 次 forward + 1 次 adjoint，宣称每迭代成本与无梯度法相同但收敛更好；Y 分支例用 L-BFGS-B、max_iter=30、11 个波长(1300–1800 nm)、25 nm 优化网格、mesh accuracy 3，输出 GDSII；梯度校验扰动 1e-9。旧版 lumopt 4 通道解复用器拓扑优化示例约 1000 次迭代，视算力需数小时到数天。Meep 也提供 Python Adjoint Solver 与像素密度不低于 FDTD resolution 的建议。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://lumerical.docs.pyansys.com/version/stable/examples/lumopt2/y_branch/pylumerical_y_branch.html）来源链接
  - [外]（出处：https://support.lumerical.com/hc/en-us/articles/1500007188582）来源链接
  - [外]（出处：https://support.lumerical.com/hc/en-us/articles/360050995394）来源链接
  - [外]（出处：https://support.lumerical.com/hc/en-us/articles/360052044913）来源链接
  - [外]（出处：https://meep.readthedocs.io/en/latest/Python_Tutorials/Adjoint_Solver/）来源链接
  - [外]（出处：https://arxiv.org/pdf/2410.07353v1）来源链接
#### 9. 仿真正确性验证与仿真-实测差距来源
- **方法原理**：四层核验：①网格/PML/仿真域收敛（用 Δσ(i)、Δσ_N(i) 量化）；②能量守恒（Parseval 定理比对时域与频域能量；Poynting 矢量面积分得到净透射功率，功率箱检查净流出）；③与解析解/互易/对称性等独立解比对（Mie 散射、偶极源源功率解析值）；④与实测比对并分解误差：材料光学常数本身的不确定性、工艺线宽/膜厚偏差、侧壁粗糙度与散射损耗、温度/应力、耦合与测量误差。关键纪律是让数值误差低于工艺与测量误差即可，不要为 1% 数值精度付出不成比例的算力。
- **硬数字**：Ansys 示例：工艺只能做到 10 nm 精度时没必要把 dx 设到 1 nm；实验误差约 5% 时无需强求仿真误差<1%；数值 dt=1.17e-17 s（内网格 5 nm）引起的有限 dt 差异仅 0.01%；FDTD 对 MCM 拟合数据的误差 1.3%，但换成 Johnson-Christy 原始数据误差约 4.2%，且超过 3 组文献金数据彼此的差异；最终精细设置与 Mie 理论差 0.15%。硅光综述指出 'last nanometer' 灵敏度使容差分析（线宽/厚度）成为必需。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://kb.lumerical.com/en/layout_analysis_test_convergence_fdtd.html）来源链接
  - [外]（出处：https://r.jina.ai/https://kb.lumerical.com/en/layout_analysis_test_convergence_fdtd.html）来源链接
  - [外]（出处：https://optics.ansys.com/hc/en-us/articles/360034394274-Using-Parseval-s-theorem-to-check-for-energy-conservation-between-the-time-and-frequency-domain）来源链接
  - [外]（出处：https://optics.ansys.com/hc/en-us/articles/1500007397442-Integrating-the-Poynting-Vector）来源链接
  - [外]（出处：https://onlinelibrary.wiley.com/doi/10.1002/lpor.201700237）来源链接
  - [外]（出处：https://arxiv.org/pdf/2410.07353v1）来源链接
#### 10. 与 EDA 工具链的衔接（GDSII → 全波 → 紧凑模型 → 系统级）
- **方法原理**：逆设计/版图优化结果直接导出 GDSII 进入流片；全波得到的 S 参数/模式与热-光系数被压缩成 compact model（如 CML Compiler 生成），再由 INTERCONNECT 做链路级 Monte-Carlo 与良率分析；Python API（PyLumerical/PyAnsys）把 CAD 建模、求解、后处理串成脚本；Meep 支持 GDS import 便于直接读取版图仿真。
- **硬数字**：lumopt2 Y 分支示例：优化结束后 gdsopen/gdsbegincell/gdsaddstencil/gdsendcell/gdsclose 导出最终 GDSII；CPO 其他流程示例用 optiSLang 驱动 Lumerical+Zemax 生成单光纤耦合损失矩阵 ROM，CML Compiler 做统计紧凑模型，INTERCONNECT 做 MC 扫角算多光纤耦合良率，Mechanical 做光纤附着错位 MC 并抽取相关矩阵。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://lumerical.docs.pyansys.com/version/stable/examples/lumopt2/y_branch/pylumerical_y_branch.html）来源链接
  - [外]（出处：https://r.jina.ai/https://ansys.com/content/dam/web/webinars/ansys-cpo-multiphysics-lumerical-mechanical-interop-flow.pdf）来源链接
  - [外]（出处：https://meep.readthedocs.io/en/latest/Python_Tutorials/GDS_Import/）来源链接
#### 11. CST 在光子器件上的专项精度/算力基准
- **方法原理**：CST Studio Suite 提供 FIT/时域、频域与 FEM 等多求解器，文献中常与 HFSS(FEM) 对比：FIT/时域偏宽带，FEM/频域偏高 Q 窄带。但本次两轮换词只拿到通用天线/微波对比与厂商总览页，没有拿到面向光子/纳米光学器件的、带明确网格口径的一手基准数字。
- **硬数字**：未覆盖：未取得 CST 用于光电/光子器件的一手精度百分比、网格/自由度或运行时间硬数字；仅能标定性取舍。检索到的是通用 EM 求解器对比（CST 时域 FIT/FDTD vs HFSS 频域 FEM）与厂商求解器总览页。
- **状态**：未覆盖
- **出处**：
  - [外]（出处：https://www.3ds.com/products/simulia/cst-studio-suite/electromagnetic-simulation-solvers）来源链接
  - [外]（出处：https://onlinelibrary.wiley.com/doi/10.1155/ijap/2733569）来源链接
  - [外]（出处：https://arxiv.org/abs/0907.3570）来源链接
### 微纳制造工艺方法
#### 1. EUV 光刻 (13.5nm, 高NA 0.55) 在光子器件图形化中的分辨率极限
- **方法原理**：极紫外投影光刻: 13.5nm 波长由锡等离子体光源产生, 全部光路为反射式(多层膜反射镜), 40-50 对 Si/Mo 多层膜(~300nm 总厚)+Ru 顶帽层, TaBN 吸收层 60-70nm 构成掩模。分辨率遵循 Rayleigh 判据 R=k1·λ/NA; 高 NA 采用变形镜(anamorphic, x 方向 4×/y 方向 8× 缩倍), 把 x 与 y 方向 NA 解耦。0.33NA→0.55NA 使 NA 提升 67%, 单次曝光分辨率理论达 8nm/16nm pitch。焦深 DOF∝λ/NA², 因此 NA 从 0.33→0.55 时 DOF 缩减 2-3 倍, 要求极薄光刻胶(<20nm, 2:1 纵横比)与超平整晶圆。适用于先进 CMOS 驱动的光子集成、高密度光子晶体/超表面若需 CMOS 产线级套刻; 但光子器件特征尺寸通常>50nm, 多数场景 DUV/EBL/NIL 更经济。
- **硬数字**：λ=13.5nm; NA 0.33→0.55(+67%); 高NA理论单次曝光 8nm 线宽 / 16nm pitch; 已打印 24nm pitch lines/spaces 与 28nm pitch contact holes; NXE:3400B(0.33NA)单次曝光 28nm pitch; HVM 实用分辨极限约 13nm(26nm pitch); 7nm 逻辑节点 metal pitch 36-40nm; 反射镜多层膜~300nm(40-50 层 Si/Mo+Ru); TaBN 吸收层 60-70nm; 胶厚<20nm(纵横比 2:1); DOF 随 NA² 下降, 高NA减少 2-3 倍; CNT pellicle 可承受>600W。口径: imec 官方技术文章(研究机构一手口径, 非 ASML 产品规格书)。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.imec-int.com/en/articles/high-na-euvl-next-major-step-lithography）来源链接
#### 2. DUV 193nm 浸没式光刻 (ArFi) 在光子器件中的分辨率与吞吐
- **方法原理**：193nm ArF 准分子激光经高 NA 投影物镜, 镜头与晶圆间以去离子水浸没(水 n≈1.44)把有效 NA 提到 1.35, 等效缩短波长。配合 OPC/相移掩模/离轴照明等分辨率增强技术。是硅光(sub-100nm 波导/光栅)主流量产图形化手段, 套刻与吞吐优于 EBL, 分辨率次于 EUV。
- **硬数字**：193nm ArFi; ASML NXT:1970Ci 分辨率≤38nm, NA=1.35, 吞吐≥250 wph; NXT:2000i NA=1.35, 40nm(C-quad 照明)/38nm(dipole 照明)。口径: ASML 官网产品规格页(仅搜索片段, 正文页被 404 拦截, 未逐字核验)。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://asml.com/en/products/duv-lithography-systems/twinscan-nxt1970ci）来源链接
  - [外]（出处：https://asml.com/en/en/products/duv-lithography-systems/twinscan-nxt2000i）来源链接
#### 3. 电子束光刻 EBL / 多电子束 (CEBL) 的分辨率-吞吐权衡
- **方法原理**：聚焦电子束直接在电子胶上扫描写入, 无掩模, 分辨率可达 sub-10nm, 是科研级光子晶体、光栅耦合器、超表面原型的首选。缺点是串行逐点/逐特征写入, throughput 极低; 多电子束(CEBL, 多柱阵列)通过并行化提升产率但系统复杂。常用于制作 NIL 母版。
- **硬数字**：MAPPER 多电子束平台 13,000 束并行(片段); 单柱 CEBL 逐特征写入吞吐显著低于光学曝光(片段)。未获得可逐字核验的 EBL 对准/套刻精度与 wafer/hour 硬数字。口径: 公开片段, 未深读原始论文正文。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://repository.tudelft.nl/file/File_4570eb9d-759c-47b8-a9d3-8af3ba1cf531?preview=1）来源链接
  - [外]（出处：https://doi.org/10.1117/12.916118）来源链接
#### 4. 纳米压印 NIL (UV/热/卷对卷) 的分辨率、套刻与在光子器件中的应用
- **方法原理**：机械方式把母模纳米图形压入抗蚀剂并固化: 热 NIL 在 Tg 以上(100-200°C)加压 1-10MPa 使热塑胶流动填充模腔, 冷却脱模; UV-NIL 在室温低压(几 bar)下用 365/405nm 紫外固化光敏胶。变体含 P2P/R2P/R2R、反向压印(R-NIL)、对准多层压印、刻蚀转移。母模多为硅/石英(刻蚀 EBL 图形), 可复制到 PDMS/Topas 软模。适合光栅、光子晶体、超表面、波导与大面积柔性光子, 高吞吐低成本。局限: 母模磨损、多层对准、脱模缺陷、胶折射率偏低(1.5-1.6)。
- **硬数字**：UV-NIL 分辨率 sub-100nm; 综述称 NIL 达 sub-10nm 分辨率; 热 NIL 压力 1-10MPa、温度 100-200°C(>Tg); UV-NIL 低压几 bar、室温; 对准多层压印套刻<100nm; EVG SmartNIL(2014 起)200mm 晶圆 sub-20nm overlay; 常规 NIL 胶折射率 1.5-1.6, 纳米颗粒填充胶(PER, TiO2/ZrO2)达 1.8-2.0; sol-gel 波导 45µm×35µm 损耗~0.5dB/cm@1550nm; UV 压印单模聚合物波导 0.35dB/cm。口径: IOP Nanotechnology 综述(同行评审, 开放获取, 已深读)。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://iopscience.iop.org/article/10.1088/1361-6528/ae150a）来源链接
  - [外]（出处：https://doi.org/10.1088/1361-6528/ae150a）来源链接
#### 5. ICP-RIE 干法刻蚀 SiO2 硬掩模: 侧壁角控制与各向异性
- **方法原理**：电感耦合等离子体反应离子刻蚀: 高密度等离子体与独立偏压解耦, 氟基气体(SF6/CF4)物理溅射+化学反应协同实现各向异性刻蚀。SF6/CF4 比例调控侧壁倾角, CF4/O2 刻蚀 SiO2 可平滑波导侧壁, SiO2 硬掩模降低线边缘粗糙度转移到硅芯。是 SOI 硅光波导定义的核心工艺, 侧壁质量直接决定传播损耗。
- **硬数字**：采用 SiO2 硬掩模+氟基 RIE 优化后最小传播损耗 0.89 dB/cm; SF6/CF4 混气控制侧壁角; CF4/O2 平滑 SiO2 侧壁。口径: IOP J. Micromech. Microeng. 25 015003 (2015, Lee et al., DOI 10.1088/0960-1317/25/1/015003, 已深读)。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://iopscience.iop.org/article/10.1088/0960-1317/25/1/015003）来源链接
#### 6. 侧壁粗糙度→散射损耗的定量关系
- **方法原理**：刻蚀导致的波导侧壁线边缘粗糙度(LER)把导模耦合到辐射模与反向模, 产生散射损耗。散射损耗近似随粗糙度 RMS 的平方与模场在侧壁的强度增长; 因此>10nm rms 的侧壁起伏显著抬高 dB/cm 损耗。抑制手段: 氧化平滑(牺牲氧化消耗粗糙层)、优化刻蚀化学、抗蚀剂回流/热回流、SiO2 硬掩模。
- **硬数字**：SOI RIE 波导侧壁粗糙度 σ≈10nm (Optics Letters 36, 2480, 2011, DOI 10.1364/ol.36.002480, 片段); 粗糙度>10nm rms 时散射损耗显著(IEEE doc 4895221, 2009, 片段); 常规/氧化平滑/各向异性刻蚀三法的散射对比(Optics Letters 26(23) 1888, 片段)。口径: 均为题录/片段, 未深读正文。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://doi.org/10.1364/ol.36.002480）来源链接
  - [外]（出处：https://ieeexplore.ieee.org/document/4895221）来源链接
  - [外]（出处：https://opg.optica.org/abstract.cfm?URI=ol-26-23-1888）来源链接
#### 7. 湿法刻蚀的各向异性/选择比 (缺口)
- **方法原理**：湿法刻蚀依靠化学腐蚀, 通常各向同性; 特定晶面相关的各向异性湿刻(如 KOH 刻 Si 的{111}面停止、TMAH)与晶圆键合/减薄、V 槽制作有关; 选择比由腐蚀液化学体系决定。在光子器件中主要用于 SOI 释放、V 槽与牺牲层去除。
- **硬数字**：未覆盖: 两轮检索未取得可核验的湿法刻蚀各向异性比/选择比硬数字(如 KOH/TMAH 各晶面刻蚀速率比、BOE 刻 SiO2 对 Si 选择比具体数值)。仅确认其为各向同性/晶面依赖的常规工艺事实。
- **状态**：未覆盖
- **出处**：[⚠ 未覆盖]
#### 8. PECVD 沉积光学薄膜的折射率控制与均匀性
- **方法原理**：等离子增强化学气相沉积在较低温度下(通常<400°C)解离前驱体成膜, 用于波导芯层/包层与掺杂玻璃(如 Ge 掺杂 SiO2)。通过气体流量比控制组分→折射率, 均匀性由腔体气流/温度场决定。低温使其适合 back-end 与聚合物/异质集成。
- **硬数字**：Ge 掺杂 PECVD 低损耗波导膜: 折射率控制 ±0.0005、折射率均匀性 ±0.0002 (SPIE DOI 10.1117/12.483242, 2002, 片段)。厚 SiN PECVD vs LPCVD 特性对比见 Southampton eprints TSM3583925(2025), 正文被 Anubis 拦截未深读。口径: 仅题录/片段。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://doi.org/10.1117/12.483242）来源链接
  - [外]（出处：https://eprints.soton.ac.uk/504148/1/TSM3583925.pdf）来源链接
#### 9. LPCVD 化学计量 Si3N4 薄膜的应力与折射率
- **方法原理**：低压化学气相沉积在高温(约 700-800°C)下热解前驱体, 膜致密、均匀性/台阶覆盖优异、光学损耗低, 是低损耗 SiN 波导与光栅的主流。但化学计量 Si3N4 固有张应力大, 厚膜易开裂, 需应力工程(富硅配比/退火/图形化释放)。
- **硬数字**：LPCVD 化学计量 Si3N4 残余张应力约 1000 MPa, 需工艺优化实现 crack-free (arXiv 2610.15754, 片段)。口径: 仅片段, 未深读正文。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://arxiv.org/html/2610.15754v1）来源链接
#### 10. ALD 原子层沉积在光学薄膜/保形涂覆中的作用
- **方法原理**：自限制表面反应逐原子层沉积, 厚度可按循环数亚纳米级精确控制, 保形性极佳, 用于高折射率涂覆(如 TiO2/HfO2 包覆 NIL 压印结构提升折射率对比)、精确厚度调谐与温度敏感器件的低温成膜。缺点是沉积速率慢。
- **硬数字**：ALD 用于光学镀膜精密控制与降低温度诱导形变(Optics Letters 34(13) 1958, 2009, 题录); ALD 膜表征方法(UMN MNC 设备资料)。未取得可核验的厚度均匀性/应力硬数字。口径: 题录与设备资料片段。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://opg.optica.org/abstract.cfm?URI=ol-34-13-1958）来源链接
  - [外]（出处：https://apps.mnc.umn.edu/pub/equipment/ald-film-characterization.pdf）来源链接
#### 11. 溅射沉积光学薄膜的厚度/应力 (缺口)
- **方法原理**：磁控溅射用高能离子轰击靶材, 原子沉积成膜, 附着力好、可沉积金属与氧化物/氮化物, 用于反射镜、金属电极与部分电光薄膜。厚度由溅射速率×时间控制, 应力与腔压/功率/气氛强相关。
- **硬数字**：未覆盖: 两轮检索未取得可核验的溅射光学薄膜厚度均匀性/折射率/应力硬数字。
- **状态**：未覆盖
- **出处**：[⚠ 未覆盖]
#### 12. 混合键合 (hybrid bonding) 的对准精度、热预算与良率
- **方法原理**：Cu-Cu 直接键合+介质(如 SiCN)熔融键合一体化: 铜 CMP 达到极高平坦度并留微小铜凹陷(recess), 等离子激活介质表面产生悬挂 Si-O- 键, DI 水水合后面对面贴合, 退火使 Cu 与介质同时成键。实现最短垂直互连、亚微米间距。分 W2W(晶圆到晶圆)与 D2W(芯片到晶圆, 含 collective D2W)。关键瓶颈: CMP 平坦/铜凹陷、对准、颗粒/空洞、热预算、翘曲、吞吐。
- **硬数字**：常规炉退火 350°C/2h; SiCN 介质工艺可从 350°C 降到 200°C 区间(HBM); Applied Materials 300°C/5min 退火使吞吐提升两个数量级, 满足 250nm copper CD @ 500nm pitch; 铜 CMP 晶圆 TTV 平坦+约 1nm copper recess variation; EVG 无机 adhesive bonding+laser release 使硅载片 TTV=100nm、精度 far less than 100nm; HVM 倒装键合机对准±3µm(3σ)→1µm(3σ); 经验法则: 键合机精度=pad 直径的 0.1-0.25×(1µm pad→100-250nm); Intel 指出 sub-1µm pitch 对准超出当前设备、D2W attach 是最慢最贵步骤; 流体自对准(CEA-Leti+I…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://semiengineering.com/hybrid-bonding-makes-strides-toward-manufacturability/）来源链接
  - [外]（出处：https://arxiv.org/abs/2611.18713）来源链接
#### 13. 微转印 (micro-transfer printing, µTP) 的对准精度与粘附切换
- **方法原理**：用弹性印章(通常 PDMS)从供体晶圆拾取微器件 coupon, 再精准印到目标晶圆/光子芯片上, 实现不同材料体系(InP/Si/TFLN/GaN)异质集成。核心是粘附力可切换: 通过动力学速度、热释放胶、溶剂/光敏/仿生微结构在拾取时高粘附、释放时低粘附。可在晶圆级并行转移已知良品 die。
- **硬数字**：商用 TP 工具对准精度 ±1.5µm(器件阵列)、±0.5µm(单个 coupon); 动力学 TP 拾取速度~10cm/s、印刷速度~1mm/s; 热释放带~100°C; 粘附切换比: kinetic~3、solvent>200、photo-sensitive 117.5、gecko~204、aphid>1000、octopus~293、PVA>10^6; 器件实例: C 波段 SOA gain 17-23dB、DFB 激光 SMSR>40dB、InGaAs PD 3dB 带宽 17.5GHz、TFLN 调制器 IL 3.3dB / ER 39dB / >50GHz。口径: Light: Science & Applications 2025;14:396 综述(中科院长春光机所, 已深读)。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC12680666）来源链接
  - [外]（出处：https://doi.org/10.1038/s41377-025-02064-w）来源链接
#### 14. 单片集成 (monolithic integration) 的对准/热预算 (缺口)
- **方法原理**：在同一晶圆上顺序外延/沉积并图形化多种功能层(如直接在硅上外延 III-V 激光器), 避免键合/转移的对准误差, 但受晶格失配、热预算累积与工艺兼容限制。区别于混合键合/转印的异质路线。
- **硬数字**：未覆盖: 两轮检索未取得可核验的单片集成专门对准精度/热预算硬数字; 仅有定性结论(混合键合把前端与后端拉到一起、顺序 3D 集成为下一代方向)。
- **状态**：未覆盖
- **出处**：
  - [外]（出处：https://semiengineering.com/hybrid-bonding-makes-strides-toward-manufacturability/）来源链接
#### 15. FAU 光纤阵列附着与单模耦合对准容差
- **方法原理**：光纤阵列单元(FAU)在 V 槽基板中按固定 pitch 排布, 用被动/主动对准贴装到光子芯片的光栅或边缘耦合器, 以 UV 胶固化固定。耦合损耗由横向偏移、角度倾斜、轴向间隙与模场失配决定; Marcuse 近似给出单模 1dB 容差约为 d=0.48w(=0.24×MFD)。pitch 累积误差、胶固化收缩、热失配是长期可靠性关键。
- **硬数字**：FAU pitch 127µm/250µm; V 槽间距±0.5µm、纤芯位置±0.7µm(≤16ch)/±1.0µm(48ch)/±1.5µm(72ch, Corning OEM-039); SMF-28 Ultra 包层 125.0±0.7µm、同心度≤0.5µm、MFD@1550nm 10.4±0.5µm(Corning PI1424); 1dB 容差(横向/倾角/气隙): MFD10.4µm→±2.5µm/1.8°/55µm(空气), 6µm→±1.4µm/3.1°/18µm, 4µm→±1.0µm/4.7°/8µm, 3.2µm UHNA-7→±0.8µm/5.9°/5µm; 实测(Avdeev 2024, arXiv:2405.11980): ±2.8µm SMF-28 / ±1.4µm 4µm / ±1.2µm UHNA-7; pitch 误差 0.05%(127.06 vs…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://photonica.io/articles/fiber-array-attach）来源链接
#### 16. 光栅耦合器 vs 边缘耦合器的对准容差与封装成本
- **方法原理**：光栅耦合器通过周期光栅把芯片模式衍射到近垂直/倾斜光纤, 无需切端面、可在晶圆级测试, 但带宽窄、偏振敏感、对角度与波长敏感(峰波长随角度漂移)。边缘耦合器用倒锥/spot-size converter 把模场扩展到匹配光纤, 带宽宽、耦合效率高, 但需切割/抛光端面且对准容差更严(sub-micron)。
- **硬数字**：光栅耦合器: <0.5dB@1µm 横向偏移、0.5dB@2°倾角、峰波长漂移~9nm/度(Taillaert 2006); 1dB 窗: 光栅±2.5µm vs 边缘±0.5µm(Carroll 2016); 端面抛光 0.3°角度误差=3nm 波长偏移; 边缘耦合器需 sub-micron 对准, 常配 SiON/polymer mode-adapter(IEEE 8054676, 2017, 片段); 封装占光模块成本最高约 80%(Tyndall IPIC 引述)。口径: Photonica 深读(引 Taillaert/Carroll)+MDPI Appl Sci 10(4)1538 片段(正文 403 未深读)。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://photonica.io/articles/fiber-array-attach）来源链接
  - [外]（出处：https://doi.org/10.3390/app10041538）来源链接
  - [外]（出处：https://nature.com/articles/s41377-025-02048-w）来源链接
#### 17. 气密/非气密封装的可靠性判据 (水汽率缺口)
- **方法原理**：光子器件封装分气密(hermetic, 金属/陶瓷腔体)与非气密(塑封/胶封)。可靠性按 Telcordia GR-1221 等标准做温度循环、湿热、机械冲击与保持力测试, 以插损变化 ΔIL 判定通过。
- **硬数字**：Telcordia GR-1221: -40~+85°C 500 次循环 / 85°C 85%RH 2000h / 500g 1ms 冲击 / 20g 振动 / 保持力 0.45-0.5kgf, 通过判据 ΔIL≤0.5dB(严格 0.2dB); Kumagai 2019: damp heat -0.11~+0.11dB、500 次循环±0.07dB。未覆盖: 气密 vs 非气密封装的水汽透过率(WVTR)/泄漏率硬数字未取得。口径: Photonica 深读引 Telcordia/文献。
- **状态**：未覆盖
- **出处**：
  - [外]（出处：https://photonica.io/articles/fiber-array-attach）来源链接
#### 18. 工艺变异 (process variation) 对硅光器件性能的影响与鲁棒设计补偿
- **方法原理**：光刻/刻蚀/沉积的线宽(CD)、层厚、折射率存在 die 间(global/D2D)与 die 内(local/WID)、空间相关与随机确定性变异。微环/环形谐振器对波导有效折射率极敏感: 1nm 级线宽/厚度偏差→有效折射率变化→谐振波长漂移, 使 DWDM 通道失配、插损上升。补偿手段: 后工艺微调(post-fabrication trimming, 如激光退火/热光相变)、variation-aware 设计(加宽波导降低群折射率敏感度)、两臂模式限制差异被动补偿、变容匹配与冗余调谐、统计建模+PDK 蒙特卡洛。
- **硬数字**：microring 波导 1nm 偏差→谐振波长漂移, 需 post-fabrication trimming(IEEE 6621507, 2013, 片段); 变异分类: Global(inter-die/D2D)/Local(intra-die/WID)/spatially correlated/random deterministic(Synopsys 白皮书 2022-07-19, PDF 402 未深读); 补偿: 全硅 FIR 滤波器用两臂模式限制差异被动补偿 linewidth/热变化而不改工艺(IEEE 7029048, 2015)、DWDM microring variation-aware matching(IEEE 9252537, 2020)、variation-tolerant 片上光网络(ACM 10.1145/3208073, 2018)。口径: 均为题录/片…
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://pubs.acs.org/doi/full/10.1021/acsphotonics.2c01194）来源链接
  - [外]（出处：https://ieeexplore.ieee.org/document/6621507）来源链接
  - [外]（出处：https://www.synopsys.com/content/dam/synopsys/photonic-solutions/documents/whitepapers/modeling-silicon-photonics-wp.pdf）来源链接
  - [外]（出处：https://dev.photonicsmanufacturing.org/sites/default/files/documents/2024_ipsr-i_silicon_photonics_updated_v2.pdf）来源链接
### 表征与测试方法学
#### 1. 波导插损 cut-back（截断法）测量与不确定度
- **方法原理**：在相同输入/输出耦合条件下测一系列不同长度 L 的直波导透射功率，按 P(L)=P0·ηc²·10^(−αL/10) 线性拟合 log P–L 斜率得传播损耗 α(dB/cm)，截距含两端耦合效率 ηc²，从而把耦合损耗与传输损耗分离。设备口径：稳定光源(±0.02 dB)+功率计(线性度±0.05 dB、动态范围≥60 dB)。验耦合漂移判据=最短波导复测差<0.1 dB；充分长度判据 α(Lmax−Lmin)>10σP。参考 ITU-T G.650.1、Vermeulen et al. 2016 环形谐振法。
- **硬数字**：典型 α@1550nm：SOI 220nm ridge 0.3–1 dB/cm、strip 1–3 dB/cm；SiN 200nm 0.05–0.2 dB/cm、SiN 800nm 0.001–0.05 dB/cm；InP shallow ridge 1.5–4 dB/cm；doped silica on Si 0.01–0.05 dB/cm。实测例 L=1/5/25/100 cm→P=−15.3/−15.6/−17.0/−22.1 dBm，拟合 α=0.069 dB/cm、95%CI ±0.002 dB/cm、R²>0.999、每耦合器≈7.6 dB。误差口径：长度误差10%→α误差10%；耦合变化好≈0.5 dB/差>2 dB；激光漂移0.01–0.05 dB/min；偏振漂移0.1–1 dB。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://photonica.io/articles/cutback-propagation-loss）来源链接
  - [外]（出处：https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nbsspecialpublication637v2.pdf）来源链接
  - [外]（出处：https://photonica.io/articles/waveguide-loss-measurement-methods-compared）来源链接
#### 2. 耦合损耗与波导传输损耗的无歧义分离（add-drop ring / 阵列波导法）
- **方法原理**：cut-back 的截距法依赖耦合在多长度间恒定；对低损耗(<0.05 dB/cm)或耦合不可复现的器件，改测 add-drop 环形谐振腔的直通/下载端口，用谐振处 Power Area Method 同时反演本征损耗与耦合系数 κ，无需截断样品即可分离耦合与传输损耗。
- **硬数字**：搜索命中：add-drop ring 同时无歧义测定传播损耗与耦合系数（PubMed 40219451, 2025-03-27）；Power Area Method 在白噪声+闪烁噪声下估计误差<7%（Micromachines 2025 综述，已核）。阵列波导结构精确表征 Opt. Express 26(14):18082 (2018)、低损耗螺旋波导 in situ Opt. Lett. 35(17):2849 —— 后者正文抓取失败(Optica JS 挑战)，仅搜索片段。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://pubmed.ncbi.nlm.nih.gov/40219451）来源链接
  - [外]（出处：https://opg.optica.org/abstract.cfm?uri=oe-26-14-18082）来源链接
  - [外]（出处：https://opg.optica.org/abstract.cfm?URI=ol-35-17-2849）来源链接
#### 3. 调制器 Vπ / Vπ·L 测量（DC 拟合、Bessel 零点、小信号法）
- **方法原理**：DC 传输曲线 P(V)=C+Bcos(πV/Vπ+φb) 全曲线拟合；Bessel 载波零点法用正弦驱动 β=πVm/Vπ，找 J0 首个零点 β=2.40483→Vπ=πVm,null/2.40483，推挽再除以2；小信号正交偏置斜率法 Vπ=πVm(Pmax−Pmin)/ΔPpp。半波电压×长度 Vπ·L 归一化器件效率。误差源：LiNbO3 DC 漂移、硅等离子色散非线性(须在指定偏置定义 Vπ)、RF 电平须在电缆末端实测。
- **硬数字**：全曲线拟合优于两点读数：峰值两点法使 Vπ 偏低 10–50%。Bessel 首零点 J0=2.40483；实测 15mm x-cut TFLN MZM：18.4 dBm 入 50Ω→Vm=2·50·0.0692=2.63 V→Vπ=1.72 V，拟合 Vπ=1.73 V/消光27 dB/φb=0.4 rad，Vπ·L≈2.6 V·cm。一手器件例：polymer-clad silicon slot Vπ=8 V@1mm→VπL=1.6 V·cm(单端)/0.8 V·cm(推挽, PubMed 20720943)；L型PN结 VπL=0.89 V·cm vs 横向 1.76 V·cm @10.5 dB/cm。参考 Wooten IEEE JSTQE 6,69(2000)、Wang et al. Nature 562,101(2018)。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.photonica.io/articles/modulator-vpi-measurement）来源链接
  - [外]（出处：https://pubmed.ncbi.nlm.nih.gov/20720943）来源链接
  - [外]（出处：https://iopscience.iop.org/article/10.35848/1347-4065/abeedd）来源链接
  - [外]（出处：https://optoelectronics.ece.ucsb.edu/sites/default/files/2017-03/16OL-zhang.pdf）来源链接
#### 4. 调制器电光带宽 S21（VNA + 校准 PD）与口径陷阱
- **方法原理**：VNA 驱动调制器、已校准高速 PD 接收：测得 S21=Hmod+HPD+Hpath(dB)，扣除 PD rolloff 与路径响应后得调制器本征 Hmod；频变半波电压 Vπ(f)=Vπ,DC/|m(f)|。设备=VNA+光波元件分析仪(内嵌工厂校准调制器/接收机)。
- **硬数字**：口径陷阱：VNA 读电功率∝调制深度²，故光 3 dB 对应 VNA 6 dB，两种『3dB 带宽』定义可差 1.4–4.7×；探测器/放大器饱和、PD rolloff 未扣是直接误差源。需在报告中标明用的是光功率 3dB 还是电 S21 3dB。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.photonica.io/articles/how-to-measure-modulator-bandwidth）来源链接
  - [外]（出处：https://www.photonica.io/articles/modulator-vpi-measurement）来源链接
  - [外]（出处：https://keysight.zinfi.net/concierge/OEMs/keysight/wwwcontent/Attachments/pdf/8177_5992-2481EN.pdf）来源链接
#### 5. 眼图 / BER / EVM 与光调制分析器
- **方法原理**：高速调制信号经 CDR 采样叠加成眼图(眼高/眼宽/抖动)，BERT 统计误码率(BER)，相干系统用光调制分析器(OM A)测 EVM/星座/光 SNR，并通过 S 参数嵌入-去嵌入把探针/夹具响应移出。设备：Keysight N4391A OMA、采样示波器、BERT。
- **硬数字**：Keysight N4391A 光调制分析器产品页与 datasheet(5990-3509)存在，但 datasheet 直抓只返回导航壳、无规格数字 → 具体 EVM 精度/带宽数字标单源未验证。100Gb/s QCSE 调制器实测例 Nat. Commun. s44172-025-00421-6（搜索命中，正文未深读）。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://www.keysight.com/us/en/product/N4391A/optical-modulation-analyzer.html）来源链接
  - [外]（出处：https://www.keysight.com/us/en/assets/7018-02043/data-sheets/5990-3509.pdf）来源链接
  - [外]（出处：https://keysight.zinfi.net/concierge/OEMs/keysight/wwwcontent/Attachments/pdf/8177_5992-2481EN.pdf）来源链接
  - [外]（出处：https://nature.com/articles/s44172-025-00421-6）来源链接
#### 6. 激光线宽延迟自外差（delay self-heterodyne）与测量下限
- **方法原理**：激光分两臂，一臂经长光纤延迟 τd 再与另一臂拍频，ESA 看拍频线型。两臂须非相干：延迟 > ~6×相干时间才得洛伦兹线型，满足 Δf=1/(π·τc)。为测 Hz/mHz 级窄线宽需极长延迟(数十 km)，但长延迟同时把 1/f 频率噪声积分进来造成虚高；改进为短延迟(100 m)+拍频包络极值幅度差反演，或用自外差(加声光移频)替代自零差以避开低频噪声。参考 Okoshi 1980、Richter IEEE JQE 22,2070(1986)、Mercer JLT 9,485(1991)。
- **硬数字**：相干条件 τd>6τc。长延迟虚高实例：50 km 光纤把标称 5.1 kHz 积分线宽的 RIO0175-5-07-1 激光器读成 31.77 kHz。短延迟法：100 m 延迟，仿真 5.5 kHz→反演 5.504/5.502 kHz；实验近中心极值对(m=1,k=0)得 6.61 kHz，远中心(m=1,k=2)得 17.34 kHz，差异源于 ESA 噪声底淹没远端极小值。极窄线宽参照：Kessler et al. Nat. Photon. 2012 亚 40 mHz、Gundavarapu et al. Nat. Photon. 2019 亚 Hz。出处 Micromachines 2022 13(8):1311, doi 10.3390/mi13081311。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC9416656/）来源链接
  - [外]（出处：https://arxiv.org/pdf/1307.2417）来源链接
  - [外]（出处：https://opg.optica.org/abstract.cfm?uri=oe-30-17-30600）来源链接
#### 7. 激光线宽多方法学全景（GHz→亚 Hz）与口径选择
- **方法原理**：按线宽量级选方法：宽线宽用自外差洛伦兹拟合；窄线宽用频率鉴别法(延迟干涉+相位噪声谱积分)、光相干接收(120°干涉)、交叉相关+β 算法；THz QCL 等用频率梳拍频或自混合干涉(OFI)。结论=无单一方法通吃全区间，测量技术落后于窄线宽光源发展。
- **硬数字**：方法表硬数字：交叉相关+β 算法 26.9 kHz；频率鉴别法 0.7 Hz / 269 Hz / 45 Hz；光相干接收(120°干涉) 4.36 kHz 积分 / 3.58 kHz 洛伦兹；延迟自零差/自外差相干接收 50 kHz、20 kHz–2 MHz。频率梳拍频测 THz QCL 本征线宽 230 Hz@2 mW(Ravaro)；自混合干涉测中红外 QCL 280 kHz(Caldiroli，局限：光反馈致线宽低估、热效应>1kHz)。应用口径要求：4-PSK<100 kHz；40Gbps 8/16/64-QAM≤1.2 kHz；FMCW 激光雷达<100 Hz。出处 Micromachines 2025 16(9):990, doi 10.3390/mi16090990。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC12471392/）来源链接
  - [外]（出处：https://www.mdpi.com/1424-8220/23/1/122）来源链接
#### 8. 光电探测器带宽测量与光外差自校准
- **方法原理**：定义 H(f)=单位光调制的 RF 光电流归一化，3dB=20log10|H|=−3dB(电流幅值0.707)。三法：①校准调制器+VNA，S21=Hmod+HPD+Hpath 去嵌得 HPD(lightwave component analyzer)；②光外差——两单频激光拍频，等偏振等功率 iac=2R√(P1P2)，|H(f)|²=实测RF功率/低频预期，无需光参考、是校准①的基准；③脉冲响应——fs/ps 脉冲+采样示波器，傅里叶变换后除以光脉冲与示波器响应。
- **硬数字**：外差例：R=0.8 A/W、各 1 mW→iac=1.6 mA→入 50Ω 功率 64 μW(−11.9 dBm)，若探测器内置 50Ω 端接则分流成 1/4=−18.0 dBm；1550nm 拍频随波长 125 MHz/pm，100 GHz=0.80 nm。带宽极限：RC f=1/(2πRLCd)，1 pF@50Ω→3.2 GHz、0.1 pF→32 GHz；渡越 f≈0.45vs/w，1μm 耗尽+vs≈6e4 m/s→≈27 GHz。陷阱：偏压改变耗尽电容/渡越时间、高光电流空间电荷屏蔽使响应变慢(须≥2个光电流取不再变小信号值)、扩散慢尾在低频先滚降、参考曲线取标称 datasheet 会传递误差、外差偏振漂移伪装滚降。参考 Derickson 1998、Tan/Jungerman/Elliott IEEE MTT 37,1217(1989)、Kato IEEE MTT 47,12…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.photonica.io/articles/how-to-measure-photodetector-bandwidth）来源链接
  - [外]（出处：https://www.photonica.io/articles/photodetector-characterization）来源链接
  - [外]（出处：https://www.nature.com/articles/s41566-021-00893-w）来源链接
#### 9. 响应度 / 量子效率 / NEP 测量与量级陷阱
- **方法原理**：R(λ)=Iphoto/Pin，量子限 R=qλ/hc=λ[μm]/1.24 (A/W)，含内量子效率 ηIQE 与面反射：R=ηIQE(1−Rfac)Rquantum。用 NIST 可溯源校准参考功率计+分束器(互换位置校准分束比)扫波长。NEP=SI^1/2/R，SI 含散粒(2qIphoto)、暗电流散粒(2qIdark)、热噪声(4kBTR/RL)。比探测率 D*=A^1/2/NEP。
- **硬数字**：量子限 R@1550nm=1.25 A/W；ηIQE=0.85+AR 膜→实测≈1.0 A/W，商用 InGaAs PIN 0.85–0.95 A/W；量子效率反推 η=R·1.24/λ。NEP 量级：低噪声 InGaAs PIN 1–10 pW/√Hz，高速 PIN 23–36 pW/√Hz，Si APD 0.05–0.5、InGaAs APD 0.1–1 pW/√Hz。10 nA 暗电流+1 A/W→暗电流散粒 NEP=0.06 pW/√Hz，但 50Ω 热噪声=18 pW/√Hz(主导300×)，须用 TIA(10kΩ–1MΩ)才接近散粒限。误差口径：参考表校准不确定度±2–5%、偏振相关响应 PDR 自由空间<0.1 dB/波导耦合 0.5–2 dB、放大器噪声主导系统 NEP(须按部署态报)。计量权威：NIST SP250-41 光谱响应度校准 200–1800 nm、NIST …
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.photonica.io/articles/photodetector-characterization）来源链接
  - [外]（出处：https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication250-41e2008.pdf）来源链接
  - [外]（出处：https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.250-95.pdf）来源链接
  - [外]（出处：https://www.bipm.org/documents/20126/44556012/CCPR-K2.b.2016.pdf）来源链接
#### 10. 暗电流测量与瞬态效应诊断（Nature Photonics 共识）
- **方法原理**：暗电流 Idark 常规用 I-V 扫描；但当存在电荷俘获、电容充放电、离子/缺陷迁移等瞬态时 I-V 扫描不适用，须加偏压后充分稳定再读，并报告阶跃电压下的暗电流瞬态。双向扫描回滞与扫速依赖是诊断信号。响应度线性度须在接近 NEP 的光功率下验证，只在远高于 NEP 处测线性不足以支撑结论。
- **硬数字**：Nature Photonics 共识声明 2025-11-03, vol.19 pp.1178–1188, doi 10.1038/s41566-025-01759-1（59位学界/业界作者、13张补充表格）。无单一硬数字阈值，给出的是测量有效性判据：瞬态未稳定则 I-V 读数无效；回滞/扫速依赖=瞬态存在的判据。相关比探测率 D* 指南 Nat. Rev. Mater. s41578-025-00830-1。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.nature.com/articles/s41566-025-01759-1）来源链接
  - [外]（出处：https://www.nature.com/articles/s41578-025-00830-1）来源链接
#### 11. 近场扫描光学显微镜（NSOM）用于光子器件表征
- **方法原理**：光纤探针(孔径/散射型)在样品表面纳米尺度扫描，探针-样品间距由剪切力反馈锁定，突破远场衍射极限直接成像近场光场分布，可定位波导/弯曲/耦合器中的光传播与损耗点，也用于晶圆级在路(in-circuit)失效定位。
- **硬数字**：搜索命中硬数字：collection-mode NSOM 可分辨 0.25 μm 铝线、线间隔 0.25 μm、边缘锐度 0.07 μm（Appl. Phys. Lett. 1987, doi 10.1063/1.98956）；InZiv Omni-SiPh LightView 用近场探针在路成像，宣称把迭代周期从数周缩到数小时（厂商口径）。AIP 原文页被 Cloudflare 拦截、NSOM 综述(1996)与光伏应用(2004)正文未深读 → 分辨率数字按单源未验证处理；光子器件专用分辨率极限未获一手核实。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://doi.org/10.1063/1.98956）来源链接
  - [外]（出处：https://sciencedirect.com/science/article/pii/S1359028696800623）来源链接
  - [外]（出处：https://inziv.com/content/wafer-level-optical-testing-how-to-separate-device-variation-from-coupling）来源链接
  - [外]（出处：https://photonics.com/Articles/Near-Field_Scanning_Optical_Microscopy_and/a18134）来源链接
#### 12. 共聚焦显微与超分辨成像的光子器件表征极限
- **方法原理**：共聚焦用针孔抑制离焦光提高轴向分辨率，但仍受 Abbe 衍射极限约束；STED/PALM/STORM 等超分辨技术突破衍射极限。用于光子器件的形貌/场分布表征时，横向分辨率与工作波长、NA 直接相关。
- **硬数字**：未覆盖：共聚焦受 Abbe 衍射极限≈200 nm 约束(搜索片段口径)，STED 突破极限的引用 doi 10.1117/12.2000807 与综述 PMC4823800 抓取遇 reCAPTCHA，未取得可核实的正文硬数字；未找到针对光子器件(而非生物样品)的一手分辨率极限实测数字。两轮关键词到顶，标未覆盖。
- **状态**：未覆盖
- **出处**：
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC4823800）来源链接
  - [外]（出处：https://doi.org/10.1117/12.2000807）来源链接
  - [外]（出处：https://iopscience.iop.org/article/10.1088/2050-6120/aaae0c）来源链接
#### 13. 晶圆级光电同测与 Known Good Die（KGD）方法
- **方法原理**：在有源/无源探针台或自动化晶圆测试机上，把电探针卡(ATE，如标准 93k)与光纤阵列 FAU 同时接到 PIC，逐 die 测 IV/LIV/波长与每通道光插损，做全晶圆 pass/fail 与良率/均匀性图，从而在封装前筛出 KGD。端口读数是『探针→芯片界面→电路→出去』的单一光功率值，混叠了耦合与器件损耗；先建立测量重复性，再降耦合变化，端口数据无法解释时用近场在路成像定位。测试插入点：键合前晶圆→键合后(PIC/EIC)晶圆→切割后单 die。
- **硬数字**：厂商规格口径(InZiv Glide-SiPh PIC，2026-11-01，厂商自述 AI 辅助撰写并审校)：被动对准、每器件数秒、无六轴台/无逐器件光反馈搜索；玻璃深沟槽 FAU 可进窄至 30 μm 的沟槽、pitch 低至 30 μm；支持 200/300 mm 晶圆、FOUP 兼容；多通道光电同测+每通道光插损+全晶圆 pass/fail+良率均匀性图。FormFactor 全自动硅光晶圆测试用 KGD probe card、电 wafer sort 用标准 93k ATE。以上均厂商/产品资料，缺独立第三方实测吞吐数字 → 单源未验证。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://inziv.com/content/wafer-level-optical-testing-how-to-separate-device-variation-from-coupling）来源链接
  - [外]（出处：https://inziv.com/content/which-wafer-level-test-systems-handle-die-to-die-optical-alignment）来源链接
  - [外]（出处：https://formfactor.com/download/fully-automated-integrated-silicon-photonic-wafer-test?wpdmdl=82376）来源链接
  - [外]（出处：https://swtestasia.org/2024proc/pdf/F05_02_ROTTOLI_SWTestAsia2024.pdf）来源链接
#### 14. 晶圆级光测试吞吐瓶颈与对准策略
- **方法原理**：主动对准(每 die 用光反馈搜索耦合)把对准时间累加到每个测试点，成为量产吞吐主瓶颈；被动对准用预先标定几何+晶圆 fiducials 定位探针，跳过逐器件搜索。对比维度：每器件对准时间、光可达性(表面光栅 vs 沟槽内边耦合)、耦合重复性、自动化程度。CPO/高密集成下每晶圆数千光 I/O 使光测试成为高量产瓶颈。
- **硬数字**：被动对准每器件数秒(InZiv 口径，见上条)；每晶圆数千光 I/O、光测试成最大瓶颈(Micromachines 2026 17(5):592 与 siliconcodesign 2026-10-07 搜索命中、正文抓取 Access Denied，仅片段)；smart sensor-augmented probe card for CPO(Micromachines 2026 5(3):21, 2026-08-02, MDPI Access Denied)仅有标题。缺可复算的吞吐(uph/die)硬数字 → 单源未验证。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://inziv.com/content/which-wafer-level-test-systems-handle-die-to-die-optical-alignment）来源链接
  - [外]（出处：https://www.mdpi.com/2072-666X/17/5/592）来源链接
  - [外]（出处：https://www.mdpi.com/2674-0729/5/3/21）来源链接
  - [外]（出处：https://siliconcodesign.com/p/why-optical-high-volume-test-is-10x）来源链接
### 可靠性与失效分析方法
#### 1. 半导体激光器：Burn-in筛选、Arrhenius温度加速、FIT/MTTF推算与Telcordia GR-468-CORE
- **方法原理**：方法原理：早夭期由制造缺陷（位错增殖、腔面氧化、电极金属扩散、键合/热沉退化）主导，用100%器件的短时通电老化（burn-in, <100 h）在出厂前消耗，判据为阈值电流Ith、给定电流下光功率Pop@Iop、给定功率下电流Iop@Pop及斜效率的漂移（典型5–30%）；稳态失效率FIT用加速老化+Arrhenius外推，寿命L=At*exp(Ea/kT)，k=8.6173e-5 eV/K；恒失效率下P(存活到t)=exp(-FIT*1e-9*t)，MTTF(MTBF)=1e9/FIT [h]。跨机理/跨温度外推必须先证明确是同一失效机理；子系统的FIT按独立组件FIT求和。Telcordia GR-468-CORE给出器件级筛选、加速老化、TC、湿热、机械等统一鉴定框架。
- **硬数字**：口径：MKS/ILX厂商白皮书：Ea典型0.2–0.7 eV；Ea=0.7 eV时中位寿命1e5 h@室温→约2300 h@70°C；burn-in典型<100 h，判据漂移5–30%；16只DFB 75°C/1000 h加速老化（EOL判据电流变化20%），个体外推寿命360–16460 h、Weibull MTTF 2200 h；老化设备稳定度需0.1%/1000 h量级、TO-can热阻5–10°C/W，腔温波动0.1°C即可见功率噪声。Agiltron GR-468-CORE Issue 2（2004-09）合格报告：逐只85°C/48 h burn-in+10次-40↔+85°C温循；12组×11只并联试验、零失效；通过判据ΔP≤10%或0.5 dB、Δλ≤0.1 nm、ΔSMSR≤5 dB；加速老化CO 25/70°C 2000 h(min)/5000 h(info)、UNC …
- **状态**：已核验
- **出处**：
  - [外]（出处：https://api.p1.mks.com/medias/sys_master/images/images/h44/h10/8797304946718/WP-Laser-Diode-Burn-In-and-Reliability-Testing.pdf）来源链接
  - [外]（出处：https://cdn-agl.agiltron.com/dlc/certificates/SWLDlaserGR468-qualificationreport2021-03-16__Agiltron.pdf）来源链接
  - [外]（出处：https://ieee802.org/3/hssg/public/jan07/winzer_01_0107.pdf）来源链接
  - [外]（出处：https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2026-09/spie-pw-2026-published-1-.pdf）来源链接
  - [外]（出处：https://electrontest.com/telcordia-bellcore-gr-468-core）来源链接
#### 2. 硅光/光子集成：相移器与加热器的TDDB、电迁移(EM)与应力迁移应力加速
- **方法原理**：方法原理：TDDB由栅/介质场强与缺陷产生导致漏电流漂移乃至击穿，寿命模型含电场指数与温度Arrhenius项并做面积缩放；EM由电子风+焦耳热驱动，阴极空洞/阳极挤出，Black方程型TTF∝J^-n*exp(Ea/kT)，n为电流指数；硅光加热器存在温度梯度，教科书式均匀温度EM模型需修正。应力迁移(SM)源于CTE失配应力梯度；热循环(TC)主要打击芯片-封装界面与通孔，相移/加热结构的局部电场、局部温度必须分开加速。鉴定用加速应力+基于物理的寿命投影（电压、温度、电流密度、面积缩放），并保持应力不跨失效机理边界。
- **硬数字**：口径：IEEE IRPS 2026综述（Marvell）：先进封装主导机理为TDDB、EM、SM、TC；TDDB受间距缩小、等离子损伤、liner变薄、low-k脆弱放大；Si CTE≈2.6 ppm/°C，基板/聚合物/焊料≈10–50 ppm/°C；SiPh封装特有失效：PD暗电流漂移、波导光损耗上升、相移器/加热器TDDB与EM、激光器退化、激光-SiPho与光纤-SiPho耦合损耗。imec IEEE REPP 2022报告：W加热器150 µm×0.6 µm，300°C/12.5 mA应力，Ea=0.94±0.08 eV、电流指数n≈2.7、t50=235±25 h(UCUT)对181±13 h，M2注入器比M1寿命>10×；热梯度使EM不适用简单手册模型。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://eps.ieee.org/wp-content/uploads/2026/04/Reliability-TC-Article-2025-IEEE-International-Reliability-Physics-Symposium-_Richard-Rao.pdf）来源链接
  - [外]（出处：https://attend.ieee.org/repp/wp-content/uploads/sites/244/croes22.pdf）来源链接
#### 3. 硅光Ge光电探测器暗电流退化：热载流子/缺陷产生与电压-温度双应力外推
- **方法原理**：方法原理：反偏Ge VPIN中缺陷产生与载流子俘获改变暗电流，监测I(t)相对初始值的漂移ΔI/I0=k*t^m；m负=缺陷/载流子俘获导致的退化率下降(DFR)，m正=缺陷持续产生(DGR)。应在单一机理区内施加电压与温度双应力，用TTF∝exp(Ea/kBT)*V^-m拟合；须检查应力电压是否跨过机理拐点（拐点后外推失效），并用不同温度/电压组验证Ea与m的一致性。
- **硬数字**：口径：imec REPP 2022：Ge VPIN PD在V>3.8 V暗电流漂移趋平、4 V出现不同机理，因此最大应力限于3.8 V以内；局部Ea=0.05–0.60 eV（低温/扩散约Ge带隙Ebg≈0.66 eV，SRH中心约0.33 eV）；1 V→2 V加速2.7–3.2×；取保守Ea=0.6 eV、m=2.5时，1 V/90°C/5年寿命需175°C/2 V应力约460 h；相移器175°C/-5 V应力最长5000 h，另设85/85与150°C组，VπL退化由偏压驱动而非温度驱动；籽晶退火可降低穿位错密度。IRPS 2026独立确认SiPh封装中PD暗电流漂移为关键失效模式（未给同组数字）。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://attend.ieee.org/repp/wp-content/uploads/sites/244/croes22.pdf）来源链接
  - [外]（出处：https://eps.ieee.org/wp-content/uploads/2026/04/Reliability-TC-Article-2025-IEEE-International-Reliability-Physics-Symposium-_Richard-Rao.pdf）来源链接
#### 4. 光致退化(photodarkening)与热漂白的可逆退化加速方法
- **方法原理**：方法原理：掺杂光纤在高功率/紫外泵浦下产生色心导致附加吸收（光致退化），其归一化吸收系数的时间演化符合幂律；升温可热漂白恢复到光照前状态。用不同温度下的复原曲线按Erdogan热衰减分布模型反演激活能谱，从而区分缺陷种类并预测给定温度下的退化/恢复速率；-vs-永久性损耗需以“可否热漂白”作为判据。该机理属高功率掺稀土光纤/光纤激光器，不等同于硅波导的稳态光致退化，迁移到SiPh需另做机理确认。
- **硬数字**：口径：Optics Letters 34(17), 2637–2639 (2009), DOI 10.1364/OL.34.002637，Söderlund等：热漂白符合Erdogan等[J. Appl. Phys. 76, 73 (1994)]幂律热衰减模型；表1两根商用大模场Yb光纤的激活能分布峰分别1.32 eV、1.50 eV，FWHM分别0.31 eV、0.34 eV（对应漂白特征温度979 K、1129 K，前处理指数因子2.0 GHz；初始致暗损耗栏1750 / 600 dB/m，页面表格表头符号在抓取中丢失，数值需以原PDF复核）。WebFetch仅得到摘要与表1，正文方程受订阅限制，且未找到第二篇交互验证来源。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://opg.optica.org/abstract.cfm?URI=ol-34-17-2637）来源链接
  - [外]（出处：https://doi.org/10.1364/OL.34.002637）来源链接
#### 5. 氢逃逸/氢外扩散(hydrogen out-diffusion)对波导与光纤损耗的影响及加速测试
- **方法原理**：方法原理（待验证）：氢在石英/锗硅网络中的扩散与逃逸会改变Si-H/Ge-H缺陷钝化状态，可能引起光吸收与折射率漂移；通常用高温烘烤/氢气氛暴露做加速，并对损耗谱或暗电流前后对比。两轮关键词检索未取得可核验的一手标准/论文与硬数字，故不填方法细节与数字，避免臆造。
- **硬数字**：未覆盖：两轮检索（换关键词≤2轮）未获得可引用的氢逃逸激活能、加速倍数或JEDEC/Telcordia试验条件；不臆造数字。
- **状态**：未覆盖
- **出处**：[⚠ 未覆盖]
#### 6. 封装可靠性：温度循环、湿热85/85、机械冲击(JESD22)与光引擎特有失效
- **方法原理**：方法原理：温度循环利用CTE失配在焊点/界面产生剪切疲劳，按Coffin-Manson型循环寿命外推；湿热（85/85、 biased HAST/HAST）以温度+湿度+偏压加速离子污染、腐蚀与界面分层；机械冲击/变频振动验证焊点、键合与封装完整性。光引擎额外以“光参数”为失效判据：热湿和残余应力改变折射率→相位误差、插损、眼图与BER劣化；翘曲导致光纤耦合失准，光纤贴装与光子引线键合退化。需组件级(CLR)/板级(BLR)/系统级(SLR)分层评价，FEA用于找应力热点。
- **硬数字**：口径：JEDEC JESD22-A104官方PDF需登录，条件数取自厂商鉴定计划：TI DMD鉴定JESD22-A104 -55↔125°C/1000 cyc，77只×3批=231只；JESD22-B104机械冲击1500g、5次，15×3=45只；JESD22-B103振动20g峰值；JESD22-A101/A110 110°C/85%RH/264h（231只）；JESD22-A118 110°C/85%RH/264h；JESD22-A108 120°C/500h；早期失效120°C/48h；6面1.2 m跌落。onsemi PCN：JESD22-A101 85°C/85%RH反偏1008h；A104 -55~150°C/1000 cyc；A118 130°C/85%RH/18.8 psig/96h；HTS 150°C/1008h。Agiltron GR-468报告：UNC TC -40…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/94/PPAP_5F00_EXTERNAL_5F00_Qual_5F00_Memo_5F00_DLP5530SAFYSQ1.pdf）来源链接
  - [外]（出处：https://mouser.com/PCN/onsemi_Generic_IPCN25638X.pdf）来源链接
  - [外]（出处：https://cdn-agl.agiltron.com/dlc/certificates/SWLDlaserGR468-qualificationreport2021-03-16__Agiltron.pdf）来源链接
  - [外]（出处：https://eps.ieee.org/wp-content/uploads/2026/04/Reliability-TC-Article-2025-IEEE-International-Reliability-Physics-Symposium-_Richard-Rao.pdf）来源链接
  - [外]（出处：https://jedec.org/sites/default/files/docs/22a104d.pdf）来源链接
#### 7. 光纤连接器端面污染与清洁的量化检验(IEC 61300-3-35:2022)
- **方法原理**：方法原理：把端面分区（纤芯A区/包层B区）并对碎屑(debris)、划痕(scratch)、缺陷(defect)分类计数，显微镜需按标准规定的视场与最小可检出尺寸验证；先做清洁度检验，再做缺陷/划痕判定。目视检验是性能检验的补充，不能替代插损/回损测量；清洁后用IEC TR 62627-01等规定流程。该方法是把“端面污染→插损/回损劣化→激光端面损伤”的定性经验变成可复现判据。
- **硬数字**：口径：IEC 61300-3-35:2022 Ed3：SFOV视场≥250 µm，需检出2 µm颗粒与3 µm宽划痕；LFOV视场≥6.4×2.5 mm，需检出10 µm颗粒；圆柱插芯中心250 µm区，135–250 µm环带建议≤10颗5–10 µm颗粒、不得有>10 µm颗粒；矩形插芯建议≤10颗10–25 µm颗粒、不得有>25 µm；单模PC A区(核心25 µm)：缺陷≥2–3 µm最多1个、>3 µm不允许（RL≥26 dB及fiber-stub收发器）；RL≥35 dB时核心区3–4 µm划痕最多1条；B区25–110 µm：≤25 µm缺陷不限、>25 µm不允许；2022版取消C/D区要求，并明确“目视不合格但光性能合格仍可使用”。Rayoptic列出GR-326-Core Issue 4条件：85°C/85%RH 168h、-40↔+75°C 21循环/168h等（实…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://webstore.iec.ch/en/publication/64254）来源链接
  - [外]（出处：https://cdn.standards.iteh.ai/samples/102780/60eef617872d4d05ab4d1ca0d7e30692/IEC-61300-3-35-2022.pdf）来源链接
  - [外]（出处：https://www.rayopticcom.com/quality-control/）来源链接
#### 8. 光纤弯曲损耗与连接器插拔寿命：机械耐久试验的口径缺口
- **方法原理**：方法原理：宏弯损耗随弯曲半径指数上升，工程上通过规定最小弯曲半径与绕轴试验控制；插拔寿命用规定次数重复插拔后测插损/回损漂移来表征端面磨损与对准结构退化，清洁常作为循环中的规定步骤。Telcordia GR-326/GR-3120与GR-468对光纤处理给出条件，但不同报告引用的判据（循环数、拉力、清洁间隔）并不一致，必须逐条核对标准原文。
- **硬数字**：口径：Agiltron GR-468-CORE合格报告：光纤弯曲半径绝对最大限值30 mm（安装/处理限）；光纤拉力1 kg/5 s×3次。Rayoptic实验室页（转述GR-326-Core Issue 4）：直线拉力68 N/300 s、90°侧拉34 N/300 s；加固连接器GR-3120为450 N/67 N；IL≤0.3 dB、RL>50 dB(UPC)/>60 dB(APC)。Verizon QAPS文件VZ-TPR-9431搜索摘要仅给“50次耐久循环、每5次清洁、每10次测量”的试验序列，未获全文，插拔循环数标准值（常见500次说法）在本轮检索中未核验。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://cdn-agl.agiltron.com/dlc/certificates/SWLDlaserGR468-qualificationreport2021-03-16__Agiltron.pdf）来源链接
  - [外]（出处：https://www.rayopticcom.com/quality-control/）来源链接
  - [外]（出处：http://verizonnebs.com/TPRs/VZ-TPR-9431.pdf）来源链接
#### 9. 相干/可插拔光模块：现场数据 vs 加速测试、浴盆曲线与冗余设计
- **方法原理**：方法原理：浴盆曲线分早夭（工厂burn-in消耗）、稳态恒定失效率(FIT)与磨损失效三段；加速老化用于压缩前两段并预测第三段，而现场数据用于校验加速模型是否高估/低估。现场数据短板：器件不运行在最坏允许极限，样本暴露量与失效数通常不足；因此加速试验给出早期与稳态上界、现场失效分析确认真实机理。并行/多波长系统的FIT按失效独立性求和或加冗余通道（N+1）降低系统级失效率，但集成度不足时可能出现超线性。
- **硬数字**：口径：Intel 2026 SPIE：>6百万只混合激光器、3年现场、100%FA确认0.05 FIT；>55000只ALT <0.1 FIT；45k h/32只HTOL退化可忽略。Cisco博客（2019表述）：光模块遵循Telcordia GR-468，另加扩展功耗循环/加速老化，量产随机抽样ORT，现场返修率<100 ppm。IEEE 802 HSSG：FIT归一化到1e9小时，10 million device hours零失效→FIT<100但99%置信区间近一个数量级，需≈100次失效；10×10G并行转发器若失效独立则FIT≈N×单波长FIT，增加1个冗余波长可显著降低系统失效率；SR-332 Issue 2 (2006-09)为FIT预算依据。MKS白皮书给出浴盆曲线三段。IEC TR 62721:2012检索摘要涉及bathtub curve、design vs fiel…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2026-09/spie-pw-2026-published-1-.pdf）来源链接
  - [外]（出处：https://blogs.cisco.com/sp/peace-of-mind-with-cisco-optics-part-2-of-3）来源链接
  - [外]（出处：https://ieee802.org/3/hssg/public/jan07/winzer_01_0107.pdf）来源链接
  - [外]（出处：https://api.p1.mks.com/medias/sys_master/images/images/h44/h10/8797304946718/WP-Laser-Diode-Burn-In-and-Reliability-Testing.pdf）来源链接
  - [外]（出处：https://standards.iteh.ai/catalog/standards/iec/42e28adc-f7b5-4914-9245-6c890fe63626/iec-tr-62721-2012）来源链接
#### 10. 加速寿命试验统计：零失效样本量、置信下界与威布尔少样本外推风险
- **方法原理**：方法原理：给定目标可靠度R、置信水平CL、威布尔形状参数β与加速倍数AF，零失效试验需满足(1-CL)≥(1-R)^(n*AF^β)以反解样本量n或等效试验时长；零失效只给单边置信下界，出现1次失效则必须改用比例法/序贯抽样。威布尔拟合用中位秩回归或MLE，少样本时β与特征寿命的置信区间极宽；若应力跨越机理、或外推超过观测时间的数量级，β的微小误差会被幂律放大成寿命数量级误差；不同批次/不同加速应力的合并需先检验机理一致性。
- **硬数字**：口径：reliability.readthedocs零失效样本量表：目标R=0.999、95%单侧置信、β=1、等效试验=1倍寿命→n=2995（若4.5万小时等效产品寿命则可能不适用），等效3倍寿命→n=999；1次失效使该下界失效。复算：ln(0.05)/ln(exp(-1))≈2996、ln(0.05)/ln(exp(-3))≈999，与页面一致（取整口径）。IEEE 802 HSSG：1e7器件小时零失效宣称FIT<100，但99%置信下单失效估计不确定度近10×，需≈100次失效；类比BER需100次错误。MKS例子16只DFB、75°C/1000 h外推360–16460 h、Weibull MTTF 2200 h——跨度约45×，直接展示小样本外推离散度。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://reliability.readthedocs.io/en/stable/Sample%20size%20required%20for%20no%20failures.html）来源链接
  - [外]（出处：https://ieee802.org/3/hssg/public/jan07/winzer_01_0107.pdf）来源链接
  - [外]（出处：https://api.p1.mks.com/medias/sys_master/images/images/h44/h10/8797304946718/WP-Laser-Diode-Burn-In-and-Reliability-Testing.pdf）来源链接
### AI辅助设计方法学
#### 1. 逆向设计：伴随法(adjoint)梯度与拓扑优化自由度 / 对比传统参数优化
- **方法原理**：伴随法用一次前向+一次反向(伴随)全波仿真，借助 Lorentz 互易性把目标函数对全部设计变量的梯度一次算出，每迭代成本与参数数目无关；拓扑优化把每个网格单元的介电常数当作连续设计变量，自由度可达数千至上万，再经投影/滤波收敛到二值结构；传统参数优化只调有限个几何参数(如半径、线宽)，自由度少、搜索空间小但可表达的结构受限。复杂度口径：adjoint/reverse-mode AD 时间 O(N_output·N_V·N_T·N_f)、内存 O(N_input·N_V·N_f)(或 reverse-mode 内存 O(N_output·N_V·N_T·N_f))，forward-mode AD 时间 O(N_input·N_V·N_T·N_f)；当输入(设计变量)数 N_input 远大于输出(目标)数 N_output 时 adjoint/reverse-mode 显著省时。局限：目标非凸、依赖初值、易陷局部最优。
- **硬数字**：口径=综述汇总的仿真/计算代价：无梯度演化算法需 thousands of evaluations(数千次全波仿真)；adjoint/拓扑优化典型需 >100 次全波仿真迭代；单次伴随仿真给出全部梯度、每迭代成本与参数数无关；50μm² 超表面在 5nm 网格下 FDTD≈100h/100GB，外推到 1cm² 同分辨率≈20,000h(约2.28年)/20TB(总约190PB)；当前全3D逆向设计超表面直径上限≈200λ(约100μm²)，representation-learning 综述给约500λ；厘米级器件需 TB 级内存与年级计算。上述均为仿真/计算代价，非实测器件性能。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC11465988/）来源链接
  - [外]（出处：https://arxiv.org/html/2507.00546v2）来源链接
  - [外]（出处：https://www.nature.com/articles/s41467-026-73390-9）来源链接
#### 2. 深度学习代理模型(surrogate)：NN 替代电磁仿真加速设计空间搜索
- **方法原理**：训练深度神经网络学习『结构→光学响应』的正向映射(或在给定目标下预测结构)，推理速度比全波仿真快数个量级，用于替代或预筛仿真以加速搜索；代表范式：PEDS、WaveY-Net(物理增强代理，U-Net 预测近场并用 Maxwell 残差正则)、神经伴随 patch solver。核心瓶颈：训练数据需用全波仿真标注，成本常高到不可行；随机采样会把差结构灌满训练集造成仿真浪费；分布外(OOD)目标/条件泛化失败；逆映射一对多使直接几何预测困难。
- **硬数字**：口径=综述结论(多为定性+量级)：大多数深度 NN 代理仍需 thousands of labeled device examples(数千个已标注器件样本)；用 3D 全波仿真为 NN 标注常在计算上不可行；训练分布外(OOD)目标会失败。硬数字：物理增强代理 PIRL 预训练用 20,000 组结构-伴随梯度对(U-Net)，adjoint 近似梯度仅2次仿真 vs 精确有限差分 N+1=257次仿真(>2个数量级效率)——此处为代理训练样本量与仿真调用数的口径，见强化学习条。泛化误差无统一数值，综述强调需针对特定设计空间实测。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://arxiv.org/html/2507.00546v2）来源链接
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC11636486/）来源链接
#### 3. 生成模型用于光子器件设计：物理引导扩散(MxDiffusion) / VAE / GAN
- **方法原理**：生成模型在潜空间学习设计分布，按目标光谱/性能条件生成结构：VAE 条件生成能力弱，GAN 易模式崩塌/训练不稳定，扩散模型更稳但需多步采样。MxDiffusion 采用两阶段：①用 Maxwell curl-curl 波方程残差损失(∇×(μ0⁻¹∇×E)−ω²εrE=0)训练扩散 U-Net，由目标光谱生成 2D 电场(E 场作中间物理表征)；②以光谱+E 场为条件生成最终二值几何；采样时无需实时电磁仿真。
- **硬数字**：口径=论文的仿真基准：训练用 15,000 个随机金图案(40nm 厚金、320nm 周期、0.5–1.8μm 波长、33×33 电场@10nm 网格、120 点透射谱、64×64 二值图案)；Maxwell 物理损失仅在扩散 t<100 施加(75% 从 [0,20]、25% 从 [21,100] 采样)；采样无需实时电磁仿真，训练/采样成本与纯数据驱动扩散相当；在 OOD 目标光谱与相变材料可调带通滤光片(超出训练集最优)上显著优于纯数据驱动扩散基线(论文未给统一百分比)。上述为仿真验证，未见流片实测。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC13088363/）来源链接
  - [外]（出处：https://arxiv.org/html/2507.00546v2）来源链接
#### 4. LLM/Agent 驱动的光子设计(2025-2026 前沿)
- **方法原理**：把大语言模型作为编排器/智能体：调用仿真工具、解释目标、规划多步逆向设计流程、跨验证并迭代；2026 年出现自演化 agentic 框架、多目标集成光子设计 agent、MCP 工具调用式超光学逆向设计。该方向 2025-2026 前沿方法大量以 arXiv 预印本形式出现，本轮仅命中搜索摘要，未深读全文。
- **硬数字**：口径=本轮仅搜索命中、未深读正文，故不引用具体性能数字，避免臆造。命中条目：An Agent-Driven, Cross-Validated Inverse-Design Pipeline for Dielectric Metasurfaces, arXiv:2611.08127(2026-11-05)；A Self-Evolving Agentic Framework for Metasurface Inverse Design, arXiv:2604.01480(2026-10-21)；VortexChat: An agentic framework for autonomous multi-objective integrated photonic design, arXiv:2608.20688(2026-08-24)；Autonomous agentic design for p…
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://arxiv.org/abs/2611.08127）来源链接
  - [外]（出处：https://arxiv.org/abs/2604.01480）来源链接
  - [外]（出处：https://arxiv.org/abs/2608.20688）来源链接
  - [外]（出处：https://arxiv.org/abs/2606.00915）来源链接
  - [外]（出处：https://arxiv.org/abs/2508.10277）来源链接
  - [外]（出处：https://arxiv.org/abs/2608.18279）来源链接
#### 5. 可微分光学 / 物理信息神经网络(PINN)：物理方程嵌入网络端到端优化
- **方法原理**：PINN 把 Maxwell 矢量 Helmholtz 方程(及增益介质的四能级速率方程)作为 PDE 残差项嵌入训练损失，用自动微分求梯度，实现无仿真数据(data-free)或部分物理约束的正/逆求解与端到端优化；hPINN(hard-constrained PINN)对 Poisson/Helmholtz 用硬约束与周期边界正弦特征；可微求解器(如 SPINS、FDFD+reverse AD)把仿真器本身写成可微计算图以直接反传设计梯度。PINN 解逆问题耗时与正问题相当，作正求解器慢于 SOTA 但逆问题有竞争力。
- **硬数字**：口径=实验实测(论文报道)：NanoPhotoNet-Lase 用 Rhodamine B 染料纳米激光，实测激射阈值 Pth=565 μJ/cm²、发射波长 620nm，与模型预测偏差 <1%(实测-预测偏差)；优化准 BIC 高 Q 几何，实现相梯度纳米激光金属透镜与光束转向相干定向发射。硬约束 PINN 出处 Lu et al. SIAM J Sci Comput 2021, 43(6):B1105–B1132。其余 beam-shaping PINN(arXiv:2607.18012)、近场 PINN(doi:10.1364/ol.586379)仅搜索命中。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://arxiv.org/abs/2607.00739）来源链接
  - [外]（出处：https://arxiv.org/html/2507.00546v2）来源链接
  - [外]（出处：https://arxiv.org/abs/2607.18012）来源链接
#### 6. 强化学习(RL)在光子设计：结构搜索与物理信息预训练
- **方法原理**：把结构搜索建模为马尔可夫决策过程：状态=当前器件结构，动作=翻转某单元材料，奖励=光学效率增量 Δη，用 DQN 学长期回报以跳出局部最优；PIRL 先用伴随法算的效率梯度预训练 U-Net(Δη_approx=(∂η/∂n_i)Δn_i)作 Q 网络初值，再用 RL 微调；通过 reward engineering 强制最小特征尺寸(可制造性约束)；迁移学习把 agent 从一个设计问题迁移到相似问题进一步提升样本效率。
- **硬数字**：口径=论文仿真基准：设计空间 ~10^74(1D 256 单元二元光栅，325nm 柱高，λ=900/1000/1100nm，θ=50/60/70°)；精确有限差分 Δη 需 N+1=257 次仿真，adjoint 近似仅 2 次仿真(>2 个数量级效率)；预训练数据 20,000 组结构-伴随梯度对；样本效率比常规 RL 提升一个数量级(约10倍)；γ∈[0.99,1)，16 workers 并行。另一工作 When Every Simulation Counts(arXiv:2607.23469)在 PCSEL 7 变量、83 次仿真调用预算、4 个匹配初值下比较 DQN+6 变体：Dueling DQN 是唯一改善全部 4 seeds 的变体，相对首批评估结构波长误差降 64%、向上功率增 47%(均为仿真值)；Double DQN 重现基线、Rainbow-lite 高上限但强 s…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC11636486/）来源链接
  - [外]（出处：https://arxiv.org/abs/2607.23469）来源链接
#### 7. 方法可复现性与局限：仿真-实测差距、逆向设计的可制造性约束
- **方法原理**：仿真最优与实测存在系统差距：DUV 193nm 下逆向设计图案因圆化/模糊/桥接近乎零良率，EBL 分辨率高但昂贵且仍有畸变；『几何接近≠功能接近』，小区域误差或系统性过/欠刻蚀偏置即使整体 L2 小也主导性能退化。PRISM 用可识别性驱动的标定图样合成+物理接地可微制造数字孪生(Hopkins/SOCS DUV、双高斯 PSF EBL，或 CNN/FNO/UNet)+光子信息 ILT：用伴随灵敏度 Γ=|∂FoM/∂M0|(归一化[0.5,1.5])加权 ℓ4 损失 ‖Γ⊙(W−W*)‖₄⁴，levelset 低分辨率 latent+高斯模糊+sigmoid(α=200)，并注入工艺角(0.85,1.0,1.15)。实测检验方面 Nature Communications SiN 工作直接对比 FDTD 仿真与流片实测。
- **硬数字**：口径=分别标注仿真/实测。SiN 实测(Nature Commun 2026)：WDM 5×5μm²(194/232THz)模拟串扰−8/−8dB、实测 C 波段≈−7dB/O 波段≈−3dB(退化归于侧壁角、间隙填充不完全)；8×8μm²(196/202THz)实测串扰≈−11dB、插损≈−1.5dB(与模拟接近)；MDM 8×8μm²/400nm 模拟−18dB@197THz，实测小 MDM −18dB@194.5THz 与模拟吻合；FP 反射器实测最大 finesse 162→Q≈210,000、单镜反射率 98.5%，环谐振器实测本征 Q>2千万；footprint 比传统耦合器小 ~50–300×(WDM)、~500×(MDM)。PRISM 仿真/标定口径：标定预算 10 个 3×3μm² 图样、2μm 间隔、有效 90μm²/总占 250μm²；孪生参数 CNN~0.4M/FN…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.nature.com/articles/s41467-026-73390-9）来源链接
  - [外]（出处：https://arxiv.org/html/2602.15762）来源链接
  - [外]（出处：https://arxiv.org/html/2507.00546v2）来源链接
### 标准计量与测试规范
#### 1. IEEE 802.3 以太网光接口（光 PHY / PMD 规范层）
- **方法原理**：IEEE 802.3 是以太网物理层的国际标准族，光接口由 PMD（Physical Medium Dependent）与 PCS 子层定义：规定光模块的中心波长、速率、链路距离、光纤类型与光眼图/功率预算，使不同厂商的光模块互操作。按速率演进：10G(802.3ae)、40G/100G(802.3ba)、200G/400G(802.3bs)、800G(802.3df)。光模块 MSA（QSFP-DD/OSFP）在机械与电接口层引用并声明符合对应 IEEE 802.3bs 光 PMD。口径：IEEE 标准正文在 IEEE Xplore 付费墙内，本次以标准编号体系 + MSA 合规声明交叉印证，未逐条读取功率/眼图限值原文。
- **硬数字**：速率档：10G/40G/100G/200G/400G/800 GbE；关键修订 802.3ae(10G)、802.3ba(40/100G)、802.3bs(200/400G)、802.3df(800G)。QSFP-DD 光模块合规声明明确引用 IEEE 802.3bs（ATGBics、FS.com 二手佐证）。具体波长/距离限值（如 400GBASE-FR4/DR4）本次未从 IEEE 一手正文核到，不写死数值。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://ieeexplore.ieee.org/Xplore/home.jsp）来源链接
  - [外]（出处：https://atgbics.com/pages/qsfp-dd-optical-transceiver-technology-overview）来源链接
  - [外]（出处：https://fs.com/eu-en/blog/differences-between-qsfpdd-and-qsfp-qsfp28-qsfp56-osfp-cfp8-cobo-b1217.html）来源链接
#### 2. OIF 400ZR / 800ZR 相干光接口实施协议（IA）
- **方法原理**：OIF（Optical Internetworking Forum）用 Implementation Agreement（实施协议，IA）定义相干光模块电/光接口与 DSP-FEC 框架，是厂商互操作的实用标准层。400ZR 面向数据中心互联(DCI)/城域，规定相干调制、FEC、光接口与达到 120 km 左右的无电中继链路。IA 由 OIF 成员投票批准，非 ISO/IEC 法定标准但产业事实标准。
- **硬数字**：OIF-400ZR-02.0 实施协议，批准日期 2022-11-03；400ZR IA Update 项目 oif2020.194.03 于 2023-01-12 启动。800ZR/800G ZR+ 相干模块：800ZR 用于放大 DWDM 链路约 120 km，800G ZR+ 超过 1000 km（Cisco 800G 相干模块数据手册，厂商口径）。400ZR 具体 FEC/波特率数值本次未从 OIF 一手 PDF 深读到（PDF 抓取被 challenge 拦截），不臆造。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://oiforum.com/wp-content/uploads/OIF-400ZR-02.0.pdf）来源链接
  - [外]（出处：https://lightwaveonline.com/optical-tech/transmission/article/14175125/oif-releases-400zr-optical-interface-implementation-agreement）来源链接
  - [外]（出处：https://cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/qsfp-dd-osfp-800g-zr-zr-plus-coherent-optics.pdf）来源链接
#### 3. Telcordia GR-468-CORE 光电器件可靠性认证测试规范
- **方法原理**：GR-468-CORE 是光电器件（激光二极管、LED、光电二极管 PD、探测器/发射器组件）的通用可靠性保证要求（Reliability Assurance Requirements），规定器件级 qualification 测试：机械、环境、电应力、完整性与长时老化测试，采用抽样方案（sampling plan）与加速应力筛选，定义失效率与可接受判据。是光模块/器件产品验收的事实可靠性基线（Bellcore/Telcordia 体系）。
- **硬数字**：测试族：器件级 qual（Laser diode/LED/PD）、机械/环境/电、完整性 harsh 测试、长时老化、抽样 plan（electrontest 综述 2018-07-26）。Hamamatsu 对 Koheras 光纤激光器的 GR-468 合规声明：15 个代表性样品做严苛环境与可靠性测试（2024-04-08，厂商口径）。具体测试时长/温度/抽样数需查 GR-468 原文，本次未深读全文，不写死。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://electrontest.com/telcordia-bellcore-gr-468-core）来源链接
  - [外]（出处：https://lf.hamamatsu.com/certified-reliability）来源链接
#### 4. Telcordia GR-2854-CORE 光纤色散补偿器通用要求（澄清范围）
- **方法原理**：GR-2854-CORE 易被误当作通用光接口规范；实测其一手标题为 GENERIC REQUIREMENTS FOR FIBER OPTIC DISPERSION COMPENSATORS，即光纤色散补偿器（DCM）的通用要求，规定 DCM 在 Bellcore Client Company(BCC)系统与电信网络中的性能与可靠性判据（插损、偏振模色散 PMD、C 波段斜率补偿、可靠性符合性）。产品 datasheet 常写“性能/可靠性符合 GR-2854-CORE”。这是本次纠偏的关键点。
- **硬数字**：GR-2854-CORE Issue 2，发布日期 2013-01-12（Intertek Inform 标准发行记录）。产品口径：低插损、低 PMD、C 波段 100% 斜率补偿，性能与可靠性均声明符合 GR-2854-CORE（GIGALIGHT DCM 2023-07-11；FS 80 km 无源 DCM 2021-03-01）。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://intertekinform.com/en-au/standards/gr-2854-core-issue-2-1063776_saig_tel_tel_2474337）来源链接
  - [外]（出处：https://gigalight.com/ols-dcm.html）来源链接
  - [外]（出处：https://img-en.fs.com/file/datasheet/80-km-passive-dispersion-compensation.pdf）来源链接
#### 5. OIF 3.2T 共封装光学（CPO）模块实施协议与共封装框架
- **方法原理**：OIF 于 2023 年发布业界首个共封装标准 3.2T Co-Packaged Module IA，属于 Co-packaging Framework Document umbrella 下的首个项目。它定义 3.2 Tb/s 光引擎与交换 ASIC 共封装的光电接口、光引擎模块形态与互操作约定，把光 I/O 从面板可插拔移到封装边缘，是 CPO 互操作的标准基线。LPO（Linear Pluggable Optics，线性直驱可插拔）是与之并行的低功耗路线，去除 DSP，本次未核到 OIF 一手 LPO IA 编号（见开放问题）。
- **硬数字**：OIF-Co-Packaging-3.2T-Module-01.0，2023-03-29；3.2 Tb/s 共封装模块；新闻发布日期 2023-04-05，称为业界首个共封装标准。LPO/448G 相关的 OIF 448Gbps Signaling for AI Workshop 于 2025-04-15/16 举办（OIF 官网），但未见正式 LPO IA 编号，标为缺口。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.oiforum.com/oif-launches-the-industrys-first-co-packaging-standard-the-3-2t-co-packaged-module-implementation-agreement）来源链接
  - [外]（出处：https://www.oiforum.com/wp-content/uploads/OIF-Co-Packaging-3.2T-Module-01.0.pdf）来源链接
  - [外]（出处：https://www.oiforum.com/meetings-events/448gbps-signaling-for-ai-workshop-apr-2025/）来源链接
#### 6. OSFP MSA 光模块形态/电接口规范
- **方法原理**：OSFP（Octal Small Form Factor Pluggable）MSA 定义可插拔光模块的机械尺寸、连接器与电接口，使多厂商 800G 模块互换。规范规定 60 触点 edge connector、8 对高速差分收发，新增 800G PMD 与电接口章节，是 800G 光模块的主流形态标准之一。
- **硬数字**：OSFP Module Specification Rev 4.1（2021-08-02）新增 800G OSFP 规范（PMD 见 Sec.10.2，电接口见 Sec.11.4）；电接口为 60 触点 edge connector，含 8 对高速差分发送（16 触点）。Arista 800G 支持 OSFP 与 QSFP-DD 两种形态，OSFP-800G-2VSR4 双 MPO-12 APC，达 50 m（厂商口径 2026-09-14）。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://osfpmsa.org/assets/pdf/OSFP_Module_Specification_Rev4_1.pdf）来源链接
  - [外]（出处：https://arista.com/assets/data/pdf/Datasheets/Arista-800G_Optics_FAQ.pdf）来源链接
#### 7. QSFP-DD MSA 高密度可插拔光模块规范
- **方法原理**：QSFP-DD（Quad Small Form Factor Pluggable Double Density）MSA 通过把高速电接口数量加倍（8 收 8 发）在相近体积实现 400G/800G，定义机械、电、热与管理接口，并声明符合 IEEE 802.3bs。2017 年发布首个规范集，定义机械、电与光学参数。
- **硬数字**：QSFP-DD 连接器 76 触点、两排 edge 设计（38+38 触点分两段插入），8 对高速差分发送 + 8 对接收（canjinoptics 2026-10-30）；符合 IEEE 802.3bs 与 QSFP-DD MSA（ATGBics 2026-09-20）。首个规范集发布于 2017-03-16（Lightwave）。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://lightwaveonline.com/optical-tech/transmission/article/16673333/qsfpdd-msa-group-releases-optical-transceiver-form-factor-specification）来源链接
  - [外]（出处：https://canjinoptics.com/qsfp-dd-msa-hardware-walkthrough）来源链接
  - [外]（出处：https://fs.com/eu-en/blog/differences-between-qsfpdd-and-qsfp-qsfp28-qsfp56-osfp-cfp8-cobo-b1217.html）来源链接
#### 8. LPO / LRO 线性直驱可插拔光模块互操作框架（缺口标注）
- **方法原理**：LPO（Linear Pluggable Optics）/LRO 通过去除光模块内 DSP、把均衡上移到交换 ASIC SerDes 降低功耗与时延，需要主机-模块电接口链路预算与 FFE/DFE 协同规范。产业上由 OIF、OIF CMIS 与多家 MSA 推动，但本次两轮关键词检索未核到一份一手、带编号的 LPO Implementation Agreement 原文（OIF 3.2T CPO IA 与 448G workshop 是相关但非 LPO IA）。按方法纪律到顶标未覆盖。
- **硬数字**：未核到一手 LPO IA 编号/正式发布日期。相关一手线索：OIF 448Gbps Signaling for AI Workshop 2025-04-15/16；OIF CMIS（Common Management Interface Specification）教程系列。无硬数字可引用，标未覆盖。
- **状态**：未覆盖
- **出处**：
  - [外]（出处：https://www.oiforum.com/meetings-events/448gbps-signaling-for-ai-workshop-apr-2025/）来源链接
  - [外]（出处：https://www.oiforum.com/meetings-events/cmis-tutorial-webinar-series/）来源链接
#### 9. 光伏效率认证标准：AM1.5G 光谱与 STC 标准测试条件
- **方法原理**：光伏器件效率在统一标准光谱与条件下测量才可比。STC（Standard Test Conditions）定义为辐照度 1000 W/m²、光谱 AM1.5G、电池温度 25 °C。AM1.5G 是 ASTM 定义的大气质量 1.5 全球（global，含散射）太阳光谱，ASTM G173-03 为当前标准光谱文件（取代早期 G159）。测试用太阳模拟器或 EQE 积分，并用标准电池/标准组件定标。真实工况光谱与 STC 差异导致效率偏差（spectral mismatch），是认证与研究的基础口径。
- **硬数字**：STC：1000 W/m²，AM1.5G，25 °C（Solener 2018/2021 论文口径；NLR Solar Module Efficiency Data Guide 2020-03-11）。标准光谱 ASTM G173-03（2013 版），早期为 ASTM G-159（1980s 推导，NREL/Preprint 2002）。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://doi.org/10.1016/j.solener.2021.01.024）来源链接
  - [外]（出处：https://doi.org/10.1016/j.solener.2018.02.071）来源链接
  - [外]（出处：https://nlr.gov/media/docs/libraries/pv/solar-module-efficiency-data-guide.pdf）来源链接
  - [外]（出处：https://docs.nlr.gov/docs/fy02osti/32284.pdf）来源链接
#### 10. 光伏效率认证的跨实验室比对与不确定度（NREL / Fraunhofer ISE / ESTI）
- **方法原理**：权威效率认证由具备资质的参考实验室完成，并通过国际/全球比对保证量值一致。NREL 组织 world-wide PV module calibration intercomparison，用传递标准组件在多个参考实验室间循环测量；Fraunhofer ISE CalLab PV Modules 建立 c-Si 与薄膜组件的测量流程与完整不确定度预算（I-V 曲线、辐照度、温度、光谱失配）。ESTI（欧盟 JRC）为另一权威认证机构，但本次未核到 ESTI 一手不确定度文档。
- **硬数字**：NREL 全球比对（2017 报告 fy18osti/70016）：7 块 PV 组件、4 个参考实验室、3 大洲循环校准（含 Fraunhofer ISE，Heidenhofstr. 2, 79110 Freiburg）。Fraunhofer ISE 降低 c-Si 与薄膜组件测量不确定度流程与不确定度分析（publica-rest 2013-08-14，PDF 正文抓取被 challenge 拦截，仅摘要片段）。ESTI 独立不确定度数字本次未核到，标缺口。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://nrel.gov/docs/fy18osti/70016.pdf）来源链接
  - [外]（出处：https://publica-rest.fraunhofer.de/server/api/core/bitstreams/45de307b-9a27-4c48-8d75-a646807cde3d/content）来源链接
  - [外]（出处：https://nlr.gov/media/docs/libraries/pv/solar-module-efficiency-data-guide.pdf）来源链接
#### 11. IEC 60825-1 激光产品安全等级与可达发射限值（AEL）
- **方法原理**：IEC 60825-1:2014（Ed.3.0）是激光产品安全的国际主标准，适用波长 180 nm–1 mm。按可达发射限值 AEL 与观看条件分级：AEL = MPE × 限制光阑(LA)面积，LA 基于瞳孔(7 mm)与热点(1 mm)等物理因素；M 类还需用光学仪器条件（50 mm@2 m、7 mm@14 mm）判定。等级约束光电系统的功率/波长设计：Class 1 在合理可预见使用下安全（含光学仪器）；Class 2 限可见光靠 0.25 s 眨眼反射；Class 3R/3B/4 逐级危险。对功率/波长设计是直接硬约束。
- **硬数字**：IEC 60825-1:2014 适用 180 nm–1 mm（IEC webstore 3587）。典型 CW AEL：Class 1≈40 µW(蓝光)、Class 2=1 mW(400–700 nm,0.25 s)、Class 3R=5 mW(可见 Class2 的 5×/不可见 Class1 的 5×)、Class 3B=500 mW、Class 4>0.5 W 无上限（RLI/Chart Courtesy David Sliney）。Class 1M 波长 302.5–4000 nm；Class 3R 302.5 nm–106 nm（RLI 原文疑为 1 µm 量级，此处照录源文并标注存疑）。Class 1 AEL 点源 0.39 mW(HeNe 例)。测量光阑 7 mm/50 mm/1 mm；眨眼时间 0.25 s；长时 100 s 或 30000 s。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://webstore.iec.ch/en/publication/3587）来源链接
  - [外]（出处：https://assets.vde-verlag.de/iec-normen/preview-pdf/info_iec60825-1%7Bed3.0%7Db.pdf）来源链接
  - [外]（出处：https://rli.com/resources/articles/classification.aspx）来源链接
  - [外]（出处：https://drs.illinois.edu/Page/SafetyLibrary/LaserClassification）来源链接
  - [外]（出处：https://seibersdorf-laboratories.at/fileadmin/user_upload/docs/le/las/publ/whitepaper_iec-60825-1.pdf）来源链接
#### 12. 光功率/波长/响应度计量溯源（NIST 国家计量院标准与量值传递）
- **方法原理**：光电量的量值溯源链：NIST 用标准探测器（硅/锗光电二极管）建立光谱辐射功率响应度标尺（基于探测器测量的绝对标尺，不依赖标准光源），通过校准服务把量值传递给二级标准与客户仪表。光纤功率计通过绝对功率校准（平行光或光纤连接器条件）与光谱响应度校准溯源到 SI。校准周期通常 12 个月。
- **硬数字**：NIST SP 250-41e（2008，NIST Measurement Services: Spectroradiometric Detector Measurements）：校准光谱辐射功率响应度 200–1800 nm，Service ID 39071S–39081S。NIST SP 250-53：激光与光纤功率计光谱响应度校准服务 0.4–1.8 µm（1999）。光纤功率计绝对功率校准服务（NIST pub 706，2012-10-12）。Newport 建议光探测器 12 个月复校并维持 NIST 溯源（2026-08-28）。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication250-41e2008.pdf）来源链接
  - [外]（出处：https://doi.org/10.6028/nist.sp.250-41）来源链接
  - [外]（出处：https://doi.org/10.6028/nist.sp.250-53）来源链接
  - [外]（出处：https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=706）来源链接
  - [外]（出处：https://newport.com/t/nist-traceable-spectral-responsivity-calibration-of-photodiode-detectors）来源链接
#### 13. 多国国家计量院（NIST / PTB / NIM）高功率光计量比对与电替代辐射计
- **方法原理**：各国 NMI 用不同原理复现光功率单位并通过双边/多边比对验证等效度。NIST 用光子动量（photon momentum）原理的功率计测高功率激光；PTB 用另一套标准；NIM（罗马尼亚国家计量院）用电流替代辐射计（electrical substitution，constant power sum）作光辐射基准。比对结果进入 CIPM MRA 的 CMC，实现量值国际互认。
- **硬数字**：首个 NMI 间千瓦级(cw)光功率比对：NIST 用基于光子动量的功率计与 PTB 比对（NIST pub 956830，2024-02-08）。NIM-Romania 基准辐射计 ESERAD 1：电替代法(constant power sum)，7 mm 直径×40 mm 长空腔，吸收比理论估计并部分实测 0.998±0.001（IEEE IMTC 1999, doi 10.1109/imtc.1999.776144）。引力波观测台位移校准以激光功率为被测量，溯源到 NMI 的 SI 一级标准（NIST pub 932473，2021-07-29）。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=956830）来源链接
  - [外]（出处：https://doi.org/10.1109/imtc.1999.776144）来源链接
  - [外]（出处：https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=932473）来源链接
#### 14. 国际光电计量比对组织与关键比对（BIPM CCPR / APMP）
- **方法原理**：BIPM 下设 CCPR（Consultative Committee for Photometry and Radiometry，光度与辐射度咨询委员会）组织关键比对（Key Comparison, KC），确保各国 NMI 量值等效。KC 结果存入 KCDB，支撑 CIPM MRA 的校准与测量能力(CMC)互认。APMP 是 BIPM 认可的亚太区域计量组织(RMO)，其 PR（光度辐射度）比对遵循 CCPR-G6 指南并与 CCPR KC 关联。光电计量比对包含光谱辐照度、光功率等被测量。
- **硬数字**：CCPR-K1.a 关键比对：光谱辐照度，波长 250–2500 nm；CCPR-K1.a.1：250–1600 nm（BIPM KCDB 报告 2015-09-24，各波长独立分析）。CCPR-G6 Guidelines for RMO Key Comparisons in Photometry and Radiometry（2014-10-14，version 1.9）规范 RMO 关键比对并与 CCPR KC 链接。CCPR 主席 Dr M.L. Rastello，执行秘书 Dr J. Viallon（BIPM）。APMP 列为 BIPM 区域计量组织之一。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://bipm.org/kcdb/comparison/download/published-section-block-file/106/384/degree/384/ccpr-k1a_pdf_2015.pdf）来源链接
  - [外]（出处：https://bipm.org/documents/20126/2071034/CCPR-G6+Guidelines+for+RMO+key+comparisons+in+PR.pdf/ee7147f6-26a4-3af2-9f18-f3c7dce8c8d4?download=true&t=1731063340983&version=1.9）来源链接
  - [外]（出处：https://www.bipm.org/en/committees/cc/ccpr）来源链接
  - [外]（出处：https://www.bipm.org/en/liaison/regional/apmp）来源链接
#### 15. 测量不确定度评定：GUM（JCGM 100:2008）
- **方法原理**：GUM（Guide to the Expression of Uncertainty in Measurement）由 JCGM-WG1 维护，是全球统一的不确定度评定框架，从 NMI 到工业全链条使用。核心流程：建立被测量 Y 与输入量 Xi 的数学模型 Y=f(X1,…,XN)；评定各输入标准不确定度 u(xi)（A 类统计/B 类先验）；按不确定度传播律合成 uc(y)（含协方差项）；给出扩展不确定度 U=k·uc（k≈2 对应约 95%）；报告结果。是光电计量比对与产品认证不确定度声明的通用语言。
- **硬数字**：GUM 正式编号 JCGM 100:2008（GUM 1995 含少量修正），JCGM-WG1 维护（BIPM）。2025 年发布 Amendment 1: Non-linearity in measurement models（JCGM-WG1:GUM-2025-01，2025 circulating）。合成标准不确定度 uc(y)、扩展不确定度 U=k·uc，包含因子 k 典型取 2（GUM 第 8 章程序）。WG1 下次会议 2027-04-20。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.bipm.org/en/jcgm-wg1-gum）来源链接
  - [外]（出处：https://www.bipm.org/en/committees/jc/jcgm/wg/jcgm-wg1-gum）来源链接
  - [外]（出处：https://iso.org/sites/JCGM/GUM/JCGM100/C045315e-html/C045315e_FILES/MAIN_C045315e/08_e.html）来源链接
  - [外]（出处：https://iso.org/sites/JCGM/GUM/JCGM100/C045315e-html/C045315e_FILES/MAIN_C045315e/04_e.html）来源链接
## 证据清单
| # | 方法主题 | 结论摘要 | 支撑 | 来源 |
| --- | --- | --- | --- | --- |
| 1 | 电磁仿真与设计工具链 | FDTD 原理与数值误差来源（Yee 网格 / Courant / 色散 / 阶梯化 / PML / 材料拟合） | [外] | [来源](https://meep.readthedocs.io/en/latest/Scheme_User_Interface/) |
| 2 | 电磁仿真与设计工具链 | FDTD 原理与数值误差来源（Yee 网格 / Courant / 色散 / 阶梯化 / PML / 材料拟合） | [外] | [来源](https://meep.readthedocs.io/en/latest/Subpixel_Smoothing/) |
| 3 | 电磁仿真与设计工具链 | FDTD 原理与数值误差来源（Yee 网格 / Courant / 色散 / 阶梯化 / PML / 材料拟合） | [外] | [来源](https://kb.lumerical.com/en/layout_analysis_test_convergence_fdtd.html) |
| 4 | 电磁仿真与设计工具链 | FDTD 原理与数值误差来源（Yee 网格 / Courant / 色散 / 阶梯化 / PML / 材料拟合） | [外] | [来源](https://kb.lumerical.com/redirect/fdtd-fix-divergence.html) |
| 5 | 电磁仿真与设计工具链 | FDTD 原理与数值误差来源（Yee 网格 / Courant / 色散 / 阶梯化 / PML / 材料拟合） | [外] | [来源](https://kb.lumerical.com/en/ref_sim_obj_simulation_fdtd.html) |
| 6 | 电磁仿真与设计工具链 | FDTD 典型光子器件仿真精度与算力开销 | [外] | [来源](https://r.jina.ai/https://kb.lumerical.com/en/layout_analysis_test_convergence_fdtd.html) |
| 7 | 电磁仿真与设计工具链 | FDTD 典型光子器件仿真精度与算力开销 | [外] | [来源](https://kb.lumerical.com/en/layout_analysis_test_convergence_fdtd.html) |
| 8 | 电磁仿真与设计工具链 | FDTD 典型光子器件仿真精度与算力开销 | [外] | [来源](https://meep.readthedocs.io/en/latest/Subpixel_Smoothing/) |
| 9 | 电磁仿真与设计工具链 | FDTD 典型光子器件仿真精度与算力开销 | [外] | [来源](https://meep.readthedocs.io/en/latest/Scheme_User_Interface/) |
| 10 | 电磁仿真与设计工具链 | FEM（COMSOL Wave Optics）适用边界与网格口径 | [外] | [来源](https://www.comsol.com/support/knowledgebase/1118) |
| 11 | 电磁仿真与设计工具链 | FEM（COMSOL Wave Optics）适用边界与网格口径 | [外] | [来源](https://comsol.com/blogs/how-to-use-the-beam-envelopes-method-for-wave-optics-simulations) |
| 12 | 电磁仿真与设计工具链 | FEM（COMSOL Wave Optics）适用边界与网格口径 | [外] | [来源](https://comsol.com/blogs/mode-analysis-for-electromagnetic-waveguides-in-comsol) |
| 13 | 电磁仿真与设计工具链 | FEM（COMSOL Wave Optics）适用边界与网格口径 | [外] | [来源](https://blogs.ethz.ch/ps_comsol/files/2020/05/WaveOpticsModuleUsersGuide.pdf) |
| 14 | 电磁仿真与设计工具链 | BPM（RSoft BeamPROP）适用边界与取舍 | [外] | [来源](https://www.synopsys.com/photonic-solutions/rsoft-photonic-device-tools/passive-device-beamprop.html) |
| 15 | 电磁仿真与设计工具链 | BPM（RSoft BeamPROP）适用边界与取舍 | [外] | [来源](https://www.synopsys.com/photonic-solutions/rsoft-photonic-device-tools/rsoft-products.html) |
| 16 | 电磁仿真与设计工具链 | BPM（RSoft BeamPROP）适用边界与取舍 | [外] | [来源](https://qacf-www.synopsys.com/content/dam/synopsys/photonic-solutions/documents/whitepapers/rsoft-effective-index-method.pdf) |
| 17 | 电磁仿真与设计工具链 | BPM（RSoft BeamPROP）适用边界与取舍 | [外] | [来源](https://en.wikipedia.org/wiki/Beam_propagation_method) |
| 18 | 电磁仿真与设计工具链 | RCWA / 傅里叶模态法（S4）用于光栅与超表面 | [外] | [来源](https://web.stanford.edu/group/fan/S4) |
| 19 | 电磁仿真与设计工具链 | RCWA / 傅里叶模态法（S4）用于光栅与超表面 | [外] | [来源](https://web.stanford.edu/group/fan/publication/Liu_ComputerPhysicsCommunications_183_2233_2012.pdf) |
| 20 | 电磁仿真与设计工具链 | RCWA / 傅里叶模态法（S4）用于光栅与超表面 | [外] | [来源](https://doi.org/10.1016/j.cpc.2012.04.026) |
| 21 | 电磁仿真与设计工具链 | RCWA / 傅里叶模态法（S4）用于光栅与超表面 | [外] | [来源](https://github.com/victorliu/S4/blob/master/S4/rcwa.h) |
| 22 | 电磁仿真与设计工具链 | RCWA / 傅里叶模态法（S4）用于光栅与超表面 | [外] | [来源](https://arxiv.org/pdf/2608.06185) |
| 23 | 电磁仿真与设计工具链 | 主流商用/开源工具能力矩阵与授权模式 | [外] | [来源](https://meep.readthedocs.io/en/latest/License_and_Copyright/) |
| 24 | 电磁仿真与设计工具链 | 主流商用/开源工具能力矩阵与授权模式 | [外] | [来源](https://mpb.readthedocs.io/en/latest/) |
| 25 | 电磁仿真与设计工具链 | 主流商用/开源工具能力矩阵与授权模式 | [外] | [来源](https://web.stanford.edu/group/fan/S4/license.html) |
| 26 | 电磁仿真与设计工具链 | 主流商用/开源工具能力矩阵与授权模式 | [外] | [来源](https://lumerical.docs.pyansys.com/version/stable/examples/lumopt2/y_branch/pylumerical_y_branch.html) |
| 27 | 电磁仿真与设计工具链 | 主流商用/开源工具能力矩阵与授权模式 | [外] | [来源](https://www.synopsys.com/photonic-solutions/rsoft-photonic-device-tools/rsoft-products.html) |
| 28 | 电磁仿真与设计工具链 | 主流商用/开源工具能力矩阵与授权模式 | [外] | [来源](https://www.3ds.com/products/simulia/cst-studio-suite/electromagnetic-simulation-solvers) |
| 29 | 电磁仿真与设计工具链 | 主流商用/开源工具能力矩阵与授权模式 | [外] | [来源](https://www.comsol.com/products/licensing/) |
| 30 | 电磁仿真与设计工具链 | 光-热-电-应力多物理场耦合与 Lumerical↔Ansys 互操作 | [外] | [来源](https://ansys.com/content/dam/web/webinars/ansys-cpo-multiphysics-lumerical-mechanical-interop-flow.pdf) |
| 31 | 电磁仿真与设计工具链 | 光-热-电-应力多物理场耦合与 Lumerical↔Ansys 互操作 | [外] | [来源](https://r.jina.ai/https://ansys.com/content/dam/web/webinars/ansys-cpo-multiphysics-lumerical-mechanical-interop-flow.pdf) |
| 32 | 电磁仿真与设计工具链 | 光-热-电-应力多物理场耦合与 Lumerical↔Ansys 互操作 | [外] | [来源](https://optics.ansys.com/hc/en-us/articles/46499056867603) |
| 33 | 电磁仿真与设计工具链 | 光-热-电-应力多物理场耦合与 Lumerical↔Ansys 互操作 | [外] | [来源](https://r.jina.ai/https://optics.ansys.com/hc/en-us/articles/46499056867603) |
| 34 | 电磁仿真与设计工具链 | 光-热-电-应力多物理场耦合与 Lumerical↔Ansys 互操作 | [外] | [来源](https://optics.ansys.com/hc/en-us/articles/5258777726227-Thermally-aware-photonic-circuit-simulation-of-a-WDM-transceiver-Icepak-integration) |
| 35 | 电磁仿真与设计工具链 | 光-热-电-应力多物理场耦合与 Lumerical↔Ansys 互操作 | [外] | [来源](https://kb.lumerical.com/en/ref_scripts_addimportheat.html) |
| 36 | 电磁仿真与设计工具链 | 光子器件逆向设计：伴随法、拓扑优化、遗传算法与 ML 代理模型 | [外] | [来源](https://lumerical.docs.pyansys.com/version/stable/examples/lumopt2/y_branch/pylumerical_y_branch.html) |
| 37 | 电磁仿真与设计工具链 | 光子器件逆向设计：伴随法、拓扑优化、遗传算法与 ML 代理模型 | [外] | [来源](https://support.lumerical.com/hc/en-us/articles/1500007188582) |
| 38 | 电磁仿真与设计工具链 | 光子器件逆向设计：伴随法、拓扑优化、遗传算法与 ML 代理模型 | [外] | [来源](https://support.lumerical.com/hc/en-us/articles/360050995394) |
| 39 | 电磁仿真与设计工具链 | 光子器件逆向设计：伴随法、拓扑优化、遗传算法与 ML 代理模型 | [外] | [来源](https://support.lumerical.com/hc/en-us/articles/360052044913) |
| 40 | 电磁仿真与设计工具链 | 光子器件逆向设计：伴随法、拓扑优化、遗传算法与 ML 代理模型 | [外] | [来源](https://meep.readthedocs.io/en/latest/Python_Tutorials/Adjoint_Solver/) |
| 41 | 电磁仿真与设计工具链 | 光子器件逆向设计：伴随法、拓扑优化、遗传算法与 ML 代理模型 | [外] | [来源](https://arxiv.org/pdf/2410.07353v1) |
| 42 | 电磁仿真与设计工具链 | 仿真正确性验证与仿真-实测差距来源 | [外] | [来源](https://kb.lumerical.com/en/layout_analysis_test_convergence_fdtd.html) |
| 43 | 电磁仿真与设计工具链 | 仿真正确性验证与仿真-实测差距来源 | [外] | [来源](https://r.jina.ai/https://kb.lumerical.com/en/layout_analysis_test_convergence_fdtd.html) |
| 44 | 电磁仿真与设计工具链 | 仿真正确性验证与仿真-实测差距来源 | [外] | [来源](https://optics.ansys.com/hc/en-us/articles/360034394274-Using-Parseval-s-theorem-to-check-for-energy-conservation-between-the-time-and-frequency-domain) |
| 45 | 电磁仿真与设计工具链 | 仿真正确性验证与仿真-实测差距来源 | [外] | [来源](https://optics.ansys.com/hc/en-us/articles/1500007397442-Integrating-the-Poynting-Vector) |
| 46 | 电磁仿真与设计工具链 | 仿真正确性验证与仿真-实测差距来源 | [外] | [来源](https://onlinelibrary.wiley.com/doi/10.1002/lpor.201700237) |
| 47 | 电磁仿真与设计工具链 | 仿真正确性验证与仿真-实测差距来源 | [外] | [来源](https://arxiv.org/pdf/2410.07353v1) |
| 48 | 电磁仿真与设计工具链 | 与 EDA 工具链的衔接（GDSII → 全波 → 紧凑模型 → 系统级） | [外] | [来源](https://lumerical.docs.pyansys.com/version/stable/examples/lumopt2/y_branch/pylumerical_y_branch.html) |
| 49 | 电磁仿真与设计工具链 | 与 EDA 工具链的衔接（GDSII → 全波 → 紧凑模型 → 系统级） | [外] | [来源](https://r.jina.ai/https://ansys.com/content/dam/web/webinars/ansys-cpo-multiphysics-lumerical-mechanical-interop-flow.pdf) |
| 50 | 电磁仿真与设计工具链 | 与 EDA 工具链的衔接（GDSII → 全波 → 紧凑模型 → 系统级） | [外] | [来源](https://meep.readthedocs.io/en/latest/Python_Tutorials/GDS_Import/) |
| 51 | 电磁仿真与设计工具链 | CST 在光子器件上的专项精度/算力基准 | [外] | [来源](https://www.3ds.com/products/simulia/cst-studio-suite/electromagnetic-simulation-solvers) |
| 52 | 电磁仿真与设计工具链 | CST 在光子器件上的专项精度/算力基准 | [外] | [来源](https://onlinelibrary.wiley.com/doi/10.1155/ijap/2733569) |
| 53 | 电磁仿真与设计工具链 | CST 在光子器件上的专项精度/算力基准 | [外] | [来源](https://arxiv.org/abs/0907.3570) |
| 54 | 微纳制造工艺方法 | EUV 光刻 (13.5nm, 高NA 0.55) 在光子器件图形化中的分辨率极限 | [外] | [来源](https://www.imec-int.com/en/articles/high-na-euvl-next-major-step-lithography) |
| 55 | 微纳制造工艺方法 | DUV 193nm 浸没式光刻 (ArFi) 在光子器件中的分辨率与吞吐 | [外] | [来源](https://asml.com/en/products/duv-lithography-systems/twinscan-nxt1970ci) |
| 56 | 微纳制造工艺方法 | DUV 193nm 浸没式光刻 (ArFi) 在光子器件中的分辨率与吞吐 | [外] | [来源](https://asml.com/en/en/products/duv-lithography-systems/twinscan-nxt2000i) |
| 57 | 微纳制造工艺方法 | 电子束光刻 EBL / 多电子束 (CEBL) 的分辨率-吞吐权衡 | [外] | [来源](https://repository.tudelft.nl/file/File_4570eb9d-759c-47b8-a9d3-8af3ba1cf531?preview=1) |
| 58 | 微纳制造工艺方法 | 电子束光刻 EBL / 多电子束 (CEBL) 的分辨率-吞吐权衡 | [外] | [来源](https://doi.org/10.1117/12.916118) |
| 59 | 微纳制造工艺方法 | 纳米压印 NIL (UV/热/卷对卷) 的分辨率、套刻与在光子器件中的应用 | [外] | [来源](https://iopscience.iop.org/article/10.1088/1361-6528/ae150a) |
| 60 | 微纳制造工艺方法 | 纳米压印 NIL (UV/热/卷对卷) 的分辨率、套刻与在光子器件中的应用 | [外] | [来源](https://doi.org/10.1088/1361-6528/ae150a) |
| 61 | 微纳制造工艺方法 | ICP-RIE 干法刻蚀 SiO2 硬掩模: 侧壁角控制与各向异性 | [外] | [来源](https://iopscience.iop.org/article/10.1088/0960-1317/25/1/015003) |
| 62 | 微纳制造工艺方法 | 侧壁粗糙度→散射损耗的定量关系 | [外] | [来源](https://doi.org/10.1364/ol.36.002480) |
| 63 | 微纳制造工艺方法 | 侧壁粗糙度→散射损耗的定量关系 | [外] | [来源](https://ieeexplore.ieee.org/document/4895221) |
| 64 | 微纳制造工艺方法 | 侧壁粗糙度→散射损耗的定量关系 | [外] | [来源](https://opg.optica.org/abstract.cfm?URI=ol-26-23-1888) |
| 65 | 微纳制造工艺方法 | PECVD 沉积光学薄膜的折射率控制与均匀性 | [外] | [来源](https://doi.org/10.1117/12.483242) |
| 66 | 微纳制造工艺方法 | PECVD 沉积光学薄膜的折射率控制与均匀性 | [外] | [来源](https://eprints.soton.ac.uk/504148/1/TSM3583925.pdf) |
| 67 | 微纳制造工艺方法 | LPCVD 化学计量 Si3N4 薄膜的应力与折射率 | [外] | [来源](https://arxiv.org/html/2610.15754v1) |
| 68 | 微纳制造工艺方法 | ALD 原子层沉积在光学薄膜/保形涂覆中的作用 | [外] | [来源](https://opg.optica.org/abstract.cfm?URI=ol-34-13-1958) |
| 69 | 微纳制造工艺方法 | ALD 原子层沉积在光学薄膜/保形涂覆中的作用 | [外] | [来源](https://apps.mnc.umn.edu/pub/equipment/ald-film-characterization.pdf) |
| 70 | 微纳制造工艺方法 | 混合键合 (hybrid bonding) 的对准精度、热预算与良率 | [外] | [来源](https://semiengineering.com/hybrid-bonding-makes-strides-toward-manufacturability/) |
| 71 | 微纳制造工艺方法 | 混合键合 (hybrid bonding) 的对准精度、热预算与良率 | [外] | [来源](https://arxiv.org/abs/2611.18713) |
| 72 | 微纳制造工艺方法 | 微转印 (micro-transfer printing, µTP) 的对准精度与粘附切换 | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC12680666) |
| 73 | 微纳制造工艺方法 | 微转印 (micro-transfer printing, µTP) 的对准精度与粘附切换 | [外] | [来源](https://doi.org/10.1038/s41377-025-02064-w) |
| 74 | 微纳制造工艺方法 | 单片集成 (monolithic integration) 的对准/热预算 (缺口) | [外] | [来源](https://semiengineering.com/hybrid-bonding-makes-strides-toward-manufacturability/) |
| 75 | 微纳制造工艺方法 | FAU 光纤阵列附着与单模耦合对准容差 | [外] | [来源](https://photonica.io/articles/fiber-array-attach) |
| 76 | 微纳制造工艺方法 | 光栅耦合器 vs 边缘耦合器的对准容差与封装成本 | [外] | [来源](https://photonica.io/articles/fiber-array-attach) |
| 77 | 微纳制造工艺方法 | 光栅耦合器 vs 边缘耦合器的对准容差与封装成本 | [外] | [来源](https://doi.org/10.3390/app10041538) |
| 78 | 微纳制造工艺方法 | 光栅耦合器 vs 边缘耦合器的对准容差与封装成本 | [外] | [来源](https://nature.com/articles/s41377-025-02048-w) |
| 79 | 微纳制造工艺方法 | 气密/非气密封装的可靠性判据 (水汽率缺口) | [外] | [来源](https://photonica.io/articles/fiber-array-attach) |
| 80 | 微纳制造工艺方法 | 工艺变异 (process variation) 对硅光器件性能的影响与鲁棒设计补偿 | [外] | [来源](https://pubs.acs.org/doi/full/10.1021/acsphotonics.2c01194) |
| 81 | 微纳制造工艺方法 | 工艺变异 (process variation) 对硅光器件性能的影响与鲁棒设计补偿 | [外] | [来源](https://ieeexplore.ieee.org/document/6621507) |
| 82 | 微纳制造工艺方法 | 工艺变异 (process variation) 对硅光器件性能的影响与鲁棒设计补偿 | [外] | [来源](https://www.synopsys.com/content/dam/synopsys/photonic-solutions/documents/whitepapers/modeling-silicon-photonics-wp.pdf) |
| 83 | 微纳制造工艺方法 | 工艺变异 (process variation) 对硅光器件性能的影响与鲁棒设计补偿 | [外] | [来源](https://dev.photonicsmanufacturing.org/sites/default/files/documents/2024_ipsr-i_silicon_photonics_updated_v2.pdf) |
| 84 | 表征与测试方法学 | 波导插损 cut-back（截断法）测量与不确定度 | [外] | [来源](https://photonica.io/articles/cutback-propagation-loss) |
| 85 | 表征与测试方法学 | 波导插损 cut-back（截断法）测量与不确定度 | [外] | [来源](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nbsspecialpublication637v2.pdf) |
| 86 | 表征与测试方法学 | 波导插损 cut-back（截断法）测量与不确定度 | [外] | [来源](https://photonica.io/articles/waveguide-loss-measurement-methods-compared) |
| 87 | 表征与测试方法学 | 耦合损耗与波导传输损耗的无歧义分离（add-drop ring / 阵列波导法） | [外] | [来源](https://pubmed.ncbi.nlm.nih.gov/40219451) |
| 88 | 表征与测试方法学 | 耦合损耗与波导传输损耗的无歧义分离（add-drop ring / 阵列波导法） | [外] | [来源](https://opg.optica.org/abstract.cfm?uri=oe-26-14-18082) |
| 89 | 表征与测试方法学 | 耦合损耗与波导传输损耗的无歧义分离（add-drop ring / 阵列波导法） | [外] | [来源](https://opg.optica.org/abstract.cfm?URI=ol-35-17-2849) |
| 90 | 表征与测试方法学 | 调制器 Vπ / Vπ·L 测量（DC 拟合、Bessel 零点、小信号法） | [外] | [来源](https://www.photonica.io/articles/modulator-vpi-measurement) |
| 91 | 表征与测试方法学 | 调制器 Vπ / Vπ·L 测量（DC 拟合、Bessel 零点、小信号法） | [外] | [来源](https://pubmed.ncbi.nlm.nih.gov/20720943) |
| 92 | 表征与测试方法学 | 调制器 Vπ / Vπ·L 测量（DC 拟合、Bessel 零点、小信号法） | [外] | [来源](https://iopscience.iop.org/article/10.35848/1347-4065/abeedd) |
| 93 | 表征与测试方法学 | 调制器 Vπ / Vπ·L 测量（DC 拟合、Bessel 零点、小信号法） | [外] | [来源](https://optoelectronics.ece.ucsb.edu/sites/default/files/2017-03/16OL-zhang.pdf) |
| 94 | 表征与测试方法学 | 调制器电光带宽 S21（VNA + 校准 PD）与口径陷阱 | [外] | [来源](https://www.photonica.io/articles/how-to-measure-modulator-bandwidth) |
| 95 | 表征与测试方法学 | 调制器电光带宽 S21（VNA + 校准 PD）与口径陷阱 | [外] | [来源](https://www.photonica.io/articles/modulator-vpi-measurement) |
| 96 | 表征与测试方法学 | 调制器电光带宽 S21（VNA + 校准 PD）与口径陷阱 | [外] | [来源](https://keysight.zinfi.net/concierge/OEMs/keysight/wwwcontent/Attachments/pdf/8177_5992-2481EN.pdf) |
| 97 | 表征与测试方法学 | 眼图 / BER / EVM 与光调制分析器 | [外] | [来源](https://www.keysight.com/us/en/product/N4391A/optical-modulation-analyzer.html) |
| 98 | 表征与测试方法学 | 眼图 / BER / EVM 与光调制分析器 | [外] | [来源](https://www.keysight.com/us/en/assets/7018-02043/data-sheets/5990-3509.pdf) |
| 99 | 表征与测试方法学 | 眼图 / BER / EVM 与光调制分析器 | [外] | [来源](https://keysight.zinfi.net/concierge/OEMs/keysight/wwwcontent/Attachments/pdf/8177_5992-2481EN.pdf) |
| 100 | 表征与测试方法学 | 眼图 / BER / EVM 与光调制分析器 | [外] | [来源](https://nature.com/articles/s44172-025-00421-6) |
| 101 | 表征与测试方法学 | 激光线宽延迟自外差（delay self-heterodyne）与测量下限 | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC9416656/) |
| 102 | 表征与测试方法学 | 激光线宽延迟自外差（delay self-heterodyne）与测量下限 | [外] | [来源](https://arxiv.org/pdf/1307.2417) |
| 103 | 表征与测试方法学 | 激光线宽延迟自外差（delay self-heterodyne）与测量下限 | [外] | [来源](https://opg.optica.org/abstract.cfm?uri=oe-30-17-30600) |
| 104 | 表征与测试方法学 | 激光线宽多方法学全景（GHz→亚 Hz）与口径选择 | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC12471392/) |
| 105 | 表征与测试方法学 | 激光线宽多方法学全景（GHz→亚 Hz）与口径选择 | [外] | [来源](https://www.mdpi.com/1424-8220/23/1/122) |
| 106 | 表征与测试方法学 | 光电探测器带宽测量与光外差自校准 | [外] | [来源](https://www.photonica.io/articles/how-to-measure-photodetector-bandwidth) |
| 107 | 表征与测试方法学 | 光电探测器带宽测量与光外差自校准 | [外] | [来源](https://www.photonica.io/articles/photodetector-characterization) |
| 108 | 表征与测试方法学 | 光电探测器带宽测量与光外差自校准 | [外] | [来源](https://www.nature.com/articles/s41566-021-00893-w) |
| 109 | 表征与测试方法学 | 响应度 / 量子效率 / NEP 测量与量级陷阱 | [外] | [来源](https://www.photonica.io/articles/photodetector-characterization) |
| 110 | 表征与测试方法学 | 响应度 / 量子效率 / NEP 测量与量级陷阱 | [外] | [来源](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication250-41e2008.pdf) |
| 111 | 表征与测试方法学 | 响应度 / 量子效率 / NEP 测量与量级陷阱 | [外] | [来源](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.250-95.pdf) |
| 112 | 表征与测试方法学 | 响应度 / 量子效率 / NEP 测量与量级陷阱 | [外] | [来源](https://www.bipm.org/documents/20126/44556012/CCPR-K2.b.2016.pdf) |
| 113 | 表征与测试方法学 | 暗电流测量与瞬态效应诊断（Nature Photonics 共识） | [外] | [来源](https://www.nature.com/articles/s41566-025-01759-1) |
| 114 | 表征与测试方法学 | 暗电流测量与瞬态效应诊断（Nature Photonics 共识） | [外] | [来源](https://www.nature.com/articles/s41578-025-00830-1) |
| 115 | 表征与测试方法学 | 近场扫描光学显微镜（NSOM）用于光子器件表征 | [外] | [来源](https://doi.org/10.1063/1.98956) |
| 116 | 表征与测试方法学 | 近场扫描光学显微镜（NSOM）用于光子器件表征 | [外] | [来源](https://sciencedirect.com/science/article/pii/S1359028696800623) |
| 117 | 表征与测试方法学 | 近场扫描光学显微镜（NSOM）用于光子器件表征 | [外] | [来源](https://inziv.com/content/wafer-level-optical-testing-how-to-separate-device-variation-from-coupling) |
| 118 | 表征与测试方法学 | 近场扫描光学显微镜（NSOM）用于光子器件表征 | [外] | [来源](https://photonics.com/Articles/Near-Field_Scanning_Optical_Microscopy_and/a18134) |
| 119 | 表征与测试方法学 | 共聚焦显微与超分辨成像的光子器件表征极限 | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC4823800) |
| 120 | 表征与测试方法学 | 共聚焦显微与超分辨成像的光子器件表征极限 | [外] | [来源](https://doi.org/10.1117/12.2000807) |
| 121 | 表征与测试方法学 | 共聚焦显微与超分辨成像的光子器件表征极限 | [外] | [来源](https://iopscience.iop.org/article/10.1088/2050-6120/aaae0c) |
| 122 | 表征与测试方法学 | 晶圆级光电同测与 Known Good Die（KGD）方法 | [外] | [来源](https://inziv.com/content/wafer-level-optical-testing-how-to-separate-device-variation-from-coupling) |
| 123 | 表征与测试方法学 | 晶圆级光电同测与 Known Good Die（KGD）方法 | [外] | [来源](https://inziv.com/content/which-wafer-level-test-systems-handle-die-to-die-optical-alignment) |
| 124 | 表征与测试方法学 | 晶圆级光电同测与 Known Good Die（KGD）方法 | [外] | [来源](https://formfactor.com/download/fully-automated-integrated-silicon-photonic-wafer-test?wpdmdl=82376) |
| 125 | 表征与测试方法学 | 晶圆级光电同测与 Known Good Die（KGD）方法 | [外] | [来源](https://swtestasia.org/2024proc/pdf/F05_02_ROTTOLI_SWTestAsia2024.pdf) |
| 126 | 表征与测试方法学 | 晶圆级光测试吞吐瓶颈与对准策略 | [外] | [来源](https://inziv.com/content/which-wafer-level-test-systems-handle-die-to-die-optical-alignment) |
| 127 | 表征与测试方法学 | 晶圆级光测试吞吐瓶颈与对准策略 | [外] | [来源](https://www.mdpi.com/2072-666X/17/5/592) |
| 128 | 表征与测试方法学 | 晶圆级光测试吞吐瓶颈与对准策略 | [外] | [来源](https://www.mdpi.com/2674-0729/5/3/21) |
| 129 | 表征与测试方法学 | 晶圆级光测试吞吐瓶颈与对准策略 | [外] | [来源](https://siliconcodesign.com/p/why-optical-high-volume-test-is-10x) |
| 130 | 可靠性与失效分析方法 | 半导体激光器：Burn-in筛选、Arrhenius温度加速、FIT/MTTF推算与Telcordia GR-468-CORE | [外] | [来源](https://api.p1.mks.com/medias/sys_master/images/images/h44/h10/8797304946718/WP-Laser-Diode-Burn-In-and-Reliability-Testing.pdf) |
| 131 | 可靠性与失效分析方法 | 半导体激光器：Burn-in筛选、Arrhenius温度加速、FIT/MTTF推算与Telcordia GR-468-CORE | [外] | [来源](https://cdn-agl.agiltron.com/dlc/certificates/SWLDlaserGR468-qualificationreport2021-03-16__Agiltron.pdf) |
| 132 | 可靠性与失效分析方法 | 半导体激光器：Burn-in筛选、Arrhenius温度加速、FIT/MTTF推算与Telcordia GR-468-CORE | [外] | [来源](https://ieee802.org/3/hssg/public/jan07/winzer_01_0107.pdf) |
| 133 | 可靠性与失效分析方法 | 半导体激光器：Burn-in筛选、Arrhenius温度加速、FIT/MTTF推算与Telcordia GR-468-CORE | [外] | [来源](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2026-09/spie-pw-2026-published-1-.pdf) |
| 134 | 可靠性与失效分析方法 | 半导体激光器：Burn-in筛选、Arrhenius温度加速、FIT/MTTF推算与Telcordia GR-468-CORE | [外] | [来源](https://electrontest.com/telcordia-bellcore-gr-468-core) |
| 135 | 可靠性与失效分析方法 | 硅光/光子集成：相移器与加热器的TDDB、电迁移(EM)与应力迁移应力加速 | [外] | [来源](https://eps.ieee.org/wp-content/uploads/2026/04/Reliability-TC-Article-2025-IEEE-International-Reliability-Physics-Symposium-_Richard-Rao.pdf) |
| 136 | 可靠性与失效分析方法 | 硅光/光子集成：相移器与加热器的TDDB、电迁移(EM)与应力迁移应力加速 | [外] | [来源](https://attend.ieee.org/repp/wp-content/uploads/sites/244/croes22.pdf) |
| 137 | 可靠性与失效分析方法 | 硅光Ge光电探测器暗电流退化：热载流子/缺陷产生与电压-温度双应力外推 | [外] | [来源](https://attend.ieee.org/repp/wp-content/uploads/sites/244/croes22.pdf) |
| 138 | 可靠性与失效分析方法 | 硅光Ge光电探测器暗电流退化：热载流子/缺陷产生与电压-温度双应力外推 | [外] | [来源](https://eps.ieee.org/wp-content/uploads/2026/04/Reliability-TC-Article-2025-IEEE-International-Reliability-Physics-Symposium-_Richard-Rao.pdf) |
| 139 | 可靠性与失效分析方法 | 光致退化(photodarkening)与热漂白的可逆退化加速方法 | [外] | [来源](https://opg.optica.org/abstract.cfm?URI=ol-34-17-2637) |
| 140 | 可靠性与失效分析方法 | 光致退化(photodarkening)与热漂白的可逆退化加速方法 | [外] | [来源](https://doi.org/10.1364/OL.34.002637) |
| 141 | 可靠性与失效分析方法 | 封装可靠性：温度循环、湿热85/85、机械冲击(JESD22)与光引擎特有失效 | [外] | [来源](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/94/PPAP_5F00_EXTERNAL_5F00_Qual_5F00_Memo_5F00_DLP5530SAFYSQ1.pdf) |
| 142 | 可靠性与失效分析方法 | 封装可靠性：温度循环、湿热85/85、机械冲击(JESD22)与光引擎特有失效 | [外] | [来源](https://mouser.com/PCN/onsemi_Generic_IPCN25638X.pdf) |
| 143 | 可靠性与失效分析方法 | 封装可靠性：温度循环、湿热85/85、机械冲击(JESD22)与光引擎特有失效 | [外] | [来源](https://cdn-agl.agiltron.com/dlc/certificates/SWLDlaserGR468-qualificationreport2021-03-16__Agiltron.pdf) |
| 144 | 可靠性与失效分析方法 | 封装可靠性：温度循环、湿热85/85、机械冲击(JESD22)与光引擎特有失效 | [外] | [来源](https://eps.ieee.org/wp-content/uploads/2026/04/Reliability-TC-Article-2025-IEEE-International-Reliability-Physics-Symposium-_Richard-Rao.pdf) |
| 145 | 可靠性与失效分析方法 | 封装可靠性：温度循环、湿热85/85、机械冲击(JESD22)与光引擎特有失效 | [外] | [来源](https://jedec.org/sites/default/files/docs/22a104d.pdf) |
| 146 | 可靠性与失效分析方法 | 光纤连接器端面污染与清洁的量化检验(IEC 61300-3-35:2022) | [外] | [来源](https://webstore.iec.ch/en/publication/64254) |
| 147 | 可靠性与失效分析方法 | 光纤连接器端面污染与清洁的量化检验(IEC 61300-3-35:2022) | [外] | [来源](https://cdn.standards.iteh.ai/samples/102780/60eef617872d4d05ab4d1ca0d7e30692/IEC-61300-3-35-2022.pdf) |
| 148 | 可靠性与失效分析方法 | 光纤连接器端面污染与清洁的量化检验(IEC 61300-3-35:2022) | [外] | [来源](https://www.rayopticcom.com/quality-control/) |
| 149 | 可靠性与失效分析方法 | 光纤弯曲损耗与连接器插拔寿命：机械耐久试验的口径缺口 | [外] | [来源](https://cdn-agl.agiltron.com/dlc/certificates/SWLDlaserGR468-qualificationreport2021-03-16__Agiltron.pdf) |
| 150 | 可靠性与失效分析方法 | 光纤弯曲损耗与连接器插拔寿命：机械耐久试验的口径缺口 | [外] | [来源](https://www.rayopticcom.com/quality-control/) |
| 151 | 可靠性与失效分析方法 | 光纤弯曲损耗与连接器插拔寿命：机械耐久试验的口径缺口 | [外] | [来源](http://verizonnebs.com/TPRs/VZ-TPR-9431.pdf) |
| 152 | 可靠性与失效分析方法 | 相干/可插拔光模块：现场数据 vs 加速测试、浴盆曲线与冗余设计 | [外] | [来源](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2026-09/spie-pw-2026-published-1-.pdf) |
| 153 | 可靠性与失效分析方法 | 相干/可插拔光模块：现场数据 vs 加速测试、浴盆曲线与冗余设计 | [外] | [来源](https://blogs.cisco.com/sp/peace-of-mind-with-cisco-optics-part-2-of-3) |
| 154 | 可靠性与失效分析方法 | 相干/可插拔光模块：现场数据 vs 加速测试、浴盆曲线与冗余设计 | [外] | [来源](https://ieee802.org/3/hssg/public/jan07/winzer_01_0107.pdf) |
| 155 | 可靠性与失效分析方法 | 相干/可插拔光模块：现场数据 vs 加速测试、浴盆曲线与冗余设计 | [外] | [来源](https://api.p1.mks.com/medias/sys_master/images/images/h44/h10/8797304946718/WP-Laser-Diode-Burn-In-and-Reliability-Testing.pdf) |
| 156 | 可靠性与失效分析方法 | 相干/可插拔光模块：现场数据 vs 加速测试、浴盆曲线与冗余设计 | [外] | [来源](https://standards.iteh.ai/catalog/standards/iec/42e28adc-f7b5-4914-9245-6c890fe63626/iec-tr-62721-2012) |
| 157 | 可靠性与失效分析方法 | 加速寿命试验统计：零失效样本量、置信下界与威布尔少样本外推风险 | [外] | [来源](https://reliability.readthedocs.io/en/stable/Sample%20size%20required%20for%20no%20failures.html) |
| 158 | 可靠性与失效分析方法 | 加速寿命试验统计：零失效样本量、置信下界与威布尔少样本外推风险 | [外] | [来源](https://ieee802.org/3/hssg/public/jan07/winzer_01_0107.pdf) |
| 159 | 可靠性与失效分析方法 | 加速寿命试验统计：零失效样本量、置信下界与威布尔少样本外推风险 | [外] | [来源](https://api.p1.mks.com/medias/sys_master/images/images/h44/h10/8797304946718/WP-Laser-Diode-Burn-In-and-Reliability-Testing.pdf) |
| 160 | AI辅助设计方法学 | 逆向设计：伴随法(adjoint)梯度与拓扑优化自由度 / 对比传统参数优化 | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC11465988/) |
| 161 | AI辅助设计方法学 | 逆向设计：伴随法(adjoint)梯度与拓扑优化自由度 / 对比传统参数优化 | [外] | [来源](https://arxiv.org/html/2507.00546v2) |
| 162 | AI辅助设计方法学 | 逆向设计：伴随法(adjoint)梯度与拓扑优化自由度 / 对比传统参数优化 | [外] | [来源](https://www.nature.com/articles/s41467-026-73390-9) |
| 163 | AI辅助设计方法学 | 深度学习代理模型(surrogate)：NN 替代电磁仿真加速设计空间搜索 | [外] | [来源](https://arxiv.org/html/2507.00546v2) |
| 164 | AI辅助设计方法学 | 深度学习代理模型(surrogate)：NN 替代电磁仿真加速设计空间搜索 | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC11636486/) |
| 165 | AI辅助设计方法学 | 生成模型用于光子器件设计：物理引导扩散(MxDiffusion) / VAE / GAN | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC13088363/) |
| 166 | AI辅助设计方法学 | 生成模型用于光子器件设计：物理引导扩散(MxDiffusion) / VAE / GAN | [外] | [来源](https://arxiv.org/html/2507.00546v2) |
| 167 | AI辅助设计方法学 | LLM/Agent 驱动的光子设计(2025-2026 前沿) | [外] | [来源](https://arxiv.org/abs/2611.08127) |
| 168 | AI辅助设计方法学 | LLM/Agent 驱动的光子设计(2025-2026 前沿) | [外] | [来源](https://arxiv.org/abs/2604.01480) |
| 169 | AI辅助设计方法学 | LLM/Agent 驱动的光子设计(2025-2026 前沿) | [外] | [来源](https://arxiv.org/abs/2608.20688) |
| 170 | AI辅助设计方法学 | LLM/Agent 驱动的光子设计(2025-2026 前沿) | [外] | [来源](https://arxiv.org/abs/2606.00915) |
| 171 | AI辅助设计方法学 | LLM/Agent 驱动的光子设计(2025-2026 前沿) | [外] | [来源](https://arxiv.org/abs/2508.10277) |
| 172 | AI辅助设计方法学 | LLM/Agent 驱动的光子设计(2025-2026 前沿) | [外] | [来源](https://arxiv.org/abs/2608.18279) |
| 173 | AI辅助设计方法学 | 可微分光学 / 物理信息神经网络(PINN)：物理方程嵌入网络端到端优化 | [外] | [来源](https://arxiv.org/abs/2607.00739) |
| 174 | AI辅助设计方法学 | 可微分光学 / 物理信息神经网络(PINN)：物理方程嵌入网络端到端优化 | [外] | [来源](https://arxiv.org/html/2507.00546v2) |
| 175 | AI辅助设计方法学 | 可微分光学 / 物理信息神经网络(PINN)：物理方程嵌入网络端到端优化 | [外] | [来源](https://arxiv.org/abs/2607.18012) |
| 176 | AI辅助设计方法学 | 强化学习(RL)在光子设计：结构搜索与物理信息预训练 | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC11636486/) |
| 177 | AI辅助设计方法学 | 强化学习(RL)在光子设计：结构搜索与物理信息预训练 | [外] | [来源](https://arxiv.org/abs/2607.23469) |
| 178 | AI辅助设计方法学 | 方法可复现性与局限：仿真-实测差距、逆向设计的可制造性约束 | [外] | [来源](https://www.nature.com/articles/s41467-026-73390-9) |
| 179 | AI辅助设计方法学 | 方法可复现性与局限：仿真-实测差距、逆向设计的可制造性约束 | [外] | [来源](https://arxiv.org/html/2602.15762) |
| 180 | AI辅助设计方法学 | 方法可复现性与局限：仿真-实测差距、逆向设计的可制造性约束 | [外] | [来源](https://arxiv.org/html/2507.00546v2) |
| 181 | 标准计量与测试规范 | IEEE 802.3 以太网光接口（光 PHY / PMD 规范层） | [外] | [来源](https://ieeexplore.ieee.org/Xplore/home.jsp) |
| 182 | 标准计量与测试规范 | IEEE 802.3 以太网光接口（光 PHY / PMD 规范层） | [外] | [来源](https://atgbics.com/pages/qsfp-dd-optical-transceiver-technology-overview) |
| 183 | 标准计量与测试规范 | IEEE 802.3 以太网光接口（光 PHY / PMD 规范层） | [外] | [来源](https://fs.com/eu-en/blog/differences-between-qsfpdd-and-qsfp-qsfp28-qsfp56-osfp-cfp8-cobo-b1217.html) |
| 184 | 标准计量与测试规范 | OIF 400ZR / 800ZR 相干光接口实施协议（IA） | [外] | [来源](https://oiforum.com/wp-content/uploads/OIF-400ZR-02.0.pdf) |
| 185 | 标准计量与测试规范 | OIF 400ZR / 800ZR 相干光接口实施协议（IA） | [外] | [来源](https://lightwaveonline.com/optical-tech/transmission/article/14175125/oif-releases-400zr-optical-interface-implementation-agreement) |
| 186 | 标准计量与测试规范 | OIF 400ZR / 800ZR 相干光接口实施协议（IA） | [外] | [来源](https://cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/qsfp-dd-osfp-800g-zr-zr-plus-coherent-optics.pdf) |
| 187 | 标准计量与测试规范 | Telcordia GR-468-CORE 光电器件可靠性认证测试规范 | [外] | [来源](https://electrontest.com/telcordia-bellcore-gr-468-core) |
| 188 | 标准计量与测试规范 | Telcordia GR-468-CORE 光电器件可靠性认证测试规范 | [外] | [来源](https://lf.hamamatsu.com/certified-reliability) |
| 189 | 标准计量与测试规范 | Telcordia GR-2854-CORE 光纤色散补偿器通用要求（澄清范围） | [外] | [来源](https://intertekinform.com/en-au/standards/gr-2854-core-issue-2-1063776_saig_tel_tel_2474337) |
| 190 | 标准计量与测试规范 | Telcordia GR-2854-CORE 光纤色散补偿器通用要求（澄清范围） | [外] | [来源](https://gigalight.com/ols-dcm.html) |
| 191 | 标准计量与测试规范 | Telcordia GR-2854-CORE 光纤色散补偿器通用要求（澄清范围） | [外] | [来源](https://img-en.fs.com/file/datasheet/80-km-passive-dispersion-compensation.pdf) |
| 192 | 标准计量与测试规范 | OIF 3.2T 共封装光学（CPO）模块实施协议与共封装框架 | [外] | [来源](https://www.oiforum.com/oif-launches-the-industrys-first-co-packaging-standard-the-3-2t-co-packaged-module-implementation-agreement) |
| 193 | 标准计量与测试规范 | OIF 3.2T 共封装光学（CPO）模块实施协议与共封装框架 | [外] | [来源](https://www.oiforum.com/wp-content/uploads/OIF-Co-Packaging-3.2T-Module-01.0.pdf) |
| 194 | 标准计量与测试规范 | OIF 3.2T 共封装光学（CPO）模块实施协议与共封装框架 | [外] | [来源](https://www.oiforum.com/meetings-events/448gbps-signaling-for-ai-workshop-apr-2025/) |
| 195 | 标准计量与测试规范 | OSFP MSA 光模块形态/电接口规范 | [外] | [来源](https://osfpmsa.org/assets/pdf/OSFP_Module_Specification_Rev4_1.pdf) |
| 196 | 标准计量与测试规范 | OSFP MSA 光模块形态/电接口规范 | [外] | [来源](https://arista.com/assets/data/pdf/Datasheets/Arista-800G_Optics_FAQ.pdf) |
| 197 | 标准计量与测试规范 | QSFP-DD MSA 高密度可插拔光模块规范 | [外] | [来源](https://lightwaveonline.com/optical-tech/transmission/article/16673333/qsfpdd-msa-group-releases-optical-transceiver-form-factor-specification) |
| 198 | 标准计量与测试规范 | QSFP-DD MSA 高密度可插拔光模块规范 | [外] | [来源](https://canjinoptics.com/qsfp-dd-msa-hardware-walkthrough) |
| 199 | 标准计量与测试规范 | QSFP-DD MSA 高密度可插拔光模块规范 | [外] | [来源](https://fs.com/eu-en/blog/differences-between-qsfpdd-and-qsfp-qsfp28-qsfp56-osfp-cfp8-cobo-b1217.html) |
| 200 | 标准计量与测试规范 | LPO / LRO 线性直驱可插拔光模块互操作框架（缺口标注） | [外] | [来源](https://www.oiforum.com/meetings-events/448gbps-signaling-for-ai-workshop-apr-2025/) |
| 201 | 标准计量与测试规范 | LPO / LRO 线性直驱可插拔光模块互操作框架（缺口标注） | [外] | [来源](https://www.oiforum.com/meetings-events/cmis-tutorial-webinar-series/) |
| 202 | 标准计量与测试规范 | 光伏效率认证标准：AM1.5G 光谱与 STC 标准测试条件 | [外] | [来源](https://doi.org/10.1016/j.solener.2021.01.024) |
| 203 | 标准计量与测试规范 | 光伏效率认证标准：AM1.5G 光谱与 STC 标准测试条件 | [外] | [来源](https://doi.org/10.1016/j.solener.2018.02.071) |
| 204 | 标准计量与测试规范 | 光伏效率认证标准：AM1.5G 光谱与 STC 标准测试条件 | [外] | [来源](https://nlr.gov/media/docs/libraries/pv/solar-module-efficiency-data-guide.pdf) |
| 205 | 标准计量与测试规范 | 光伏效率认证标准：AM1.5G 光谱与 STC 标准测试条件 | [外] | [来源](https://docs.nlr.gov/docs/fy02osti/32284.pdf) |
| 206 | 标准计量与测试规范 | 光伏效率认证的跨实验室比对与不确定度（NREL / Fraunhofer ISE / ESTI） | [外] | [来源](https://nrel.gov/docs/fy18osti/70016.pdf) |
| 207 | 标准计量与测试规范 | 光伏效率认证的跨实验室比对与不确定度（NREL / Fraunhofer ISE / ESTI） | [外] | [来源](https://publica-rest.fraunhofer.de/server/api/core/bitstreams/45de307b-9a27-4c48-8d75-a646807cde3d/content) |
| 208 | 标准计量与测试规范 | 光伏效率认证的跨实验室比对与不确定度（NREL / Fraunhofer ISE / ESTI） | [外] | [来源](https://nlr.gov/media/docs/libraries/pv/solar-module-efficiency-data-guide.pdf) |
| 209 | 标准计量与测试规范 | IEC 60825-1 激光产品安全等级与可达发射限值（AEL） | [外] | [来源](https://webstore.iec.ch/en/publication/3587) |
| 210 | 标准计量与测试规范 | IEC 60825-1 激光产品安全等级与可达发射限值（AEL） | [外] | [来源](https://assets.vde-verlag.de/iec-normen/preview-pdf/info_iec60825-1%7Bed3.0%7Db.pdf) |
| 211 | 标准计量与测试规范 | IEC 60825-1 激光产品安全等级与可达发射限值（AEL） | [外] | [来源](https://rli.com/resources/articles/classification.aspx) |
| 212 | 标准计量与测试规范 | IEC 60825-1 激光产品安全等级与可达发射限值（AEL） | [外] | [来源](https://drs.illinois.edu/Page/SafetyLibrary/LaserClassification) |
| 213 | 标准计量与测试规范 | IEC 60825-1 激光产品安全等级与可达发射限值（AEL） | [外] | [来源](https://seibersdorf-laboratories.at/fileadmin/user_upload/docs/le/las/publ/whitepaper_iec-60825-1.pdf) |
| 214 | 标准计量与测试规范 | 光功率/波长/响应度计量溯源（NIST 国家计量院标准与量值传递） | [外] | [来源](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication250-41e2008.pdf) |
| 215 | 标准计量与测试规范 | 光功率/波长/响应度计量溯源（NIST 国家计量院标准与量值传递） | [外] | [来源](https://doi.org/10.6028/nist.sp.250-41) |
| 216 | 标准计量与测试规范 | 光功率/波长/响应度计量溯源（NIST 国家计量院标准与量值传递） | [外] | [来源](https://doi.org/10.6028/nist.sp.250-53) |
| 217 | 标准计量与测试规范 | 光功率/波长/响应度计量溯源（NIST 国家计量院标准与量值传递） | [外] | [来源](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=706) |
| 218 | 标准计量与测试规范 | 光功率/波长/响应度计量溯源（NIST 国家计量院标准与量值传递） | [外] | [来源](https://newport.com/t/nist-traceable-spectral-responsivity-calibration-of-photodiode-detectors) |
| 219 | 标准计量与测试规范 | 多国国家计量院（NIST / PTB / NIM）高功率光计量比对与电替代辐射计 | [外] | [来源](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=956830) |
| 220 | 标准计量与测试规范 | 多国国家计量院（NIST / PTB / NIM）高功率光计量比对与电替代辐射计 | [外] | [来源](https://doi.org/10.1109/imtc.1999.776144) |
| 221 | 标准计量与测试规范 | 多国国家计量院（NIST / PTB / NIM）高功率光计量比对与电替代辐射计 | [外] | [来源](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=932473) |
| 222 | 标准计量与测试规范 | 国际光电计量比对组织与关键比对（BIPM CCPR / APMP） | [外] | [来源](https://bipm.org/kcdb/comparison/download/published-section-block-file/106/384/degree/384/ccpr-k1a_pdf_2015.pdf) |
| 223 | 标准计量与测试规范 | 国际光电计量比对组织与关键比对（BIPM CCPR / APMP） | [外] | [来源](https://bipm.org/documents/20126/2071034/CCPR-G6+Guidelines+for+RMO+key+comparisons+in+PR.pdf/ee7147f6-26a4-3af2-9f18-f3c7dce8c8d4?download=true&t=1731063340983&version=1.9) |
| 224 | 标准计量与测试规范 | 国际光电计量比对组织与关键比对（BIPM CCPR / APMP） | [外] | [来源](https://www.bipm.org/en/committees/cc/ccpr) |
| 225 | 标准计量与测试规范 | 国际光电计量比对组织与关键比对（BIPM CCPR / APMP） | [外] | [来源](https://www.bipm.org/en/liaison/regional/apmp) |
| 226 | 标准计量与测试规范 | 测量不确定度评定：GUM（JCGM 100:2008） | [外] | [来源](https://www.bipm.org/en/jcgm-wg1-gum) |
| 227 | 标准计量与测试规范 | 测量不确定度评定：GUM（JCGM 100:2008） | [外] | [来源](https://www.bipm.org/en/committees/jc/jcgm/wg/jcgm-wg1-gum) |
| 228 | 标准计量与测试规范 | 测量不确定度评定：GUM（JCGM 100:2008） | [外] | [来源](https://iso.org/sites/JCGM/GUM/JCGM100/C045315e-html/C045315e_FILES/MAIN_C045315e/08_e.html) |
| 229 | 标准计量与测试规范 | 测量不确定度评定：GUM（JCGM 100:2008） | [外] | [来源](https://iso.org/sites/JCGM/GUM/JCGM100/C045315e-html/C045315e_FILES/MAIN_C045315e/04_e.html) |

## 口径与来源
本报告数据状态分三档：**已核验**＝多源交叉或一手论文/权威机构原文；**单源未验证**＝仅单一来源、未升级为定论；**未覆盖**＝两轮换词检索后仍无可引用一手出处。所有 URL 均为公开链接，标注 [外] 者来自公开网络一手资料；数字均标口径并区分理论极限与实测值。
## 来源分区
### 公开信息
- [外]（出处：https://meep.readthedocs.io/en/latest/Scheme_User_Interface/）来源1
- [外]（出处：https://meep.readthedocs.io/en/latest/Subpixel_Smoothing/）来源2
- [外]（出处：https://kb.lumerical.com/en/layout_analysis_test_convergence_fdtd.html）来源3
- [外]（出处：https://kb.lumerical.com/redirect/fdtd-fix-divergence.html）来源4
- [外]（出处：https://kb.lumerical.com/en/ref_sim_obj_simulation_fdtd.html）来源5
- [外]（出处：https://r.jina.ai/https://kb.lumerical.com/en/layout_analysis_test_convergence_fdtd.html）来源6
- [外]（出处：https://www.comsol.com/support/knowledgebase/1118）来源7
- [外]（出处：https://comsol.com/blogs/how-to-use-the-beam-envelopes-method-for-wave-optics-simulations）来源8
- [外]（出处：https://comsol.com/blogs/mode-analysis-for-electromagnetic-waveguides-in-comsol）来源9
- [外]（出处：https://blogs.ethz.ch/ps_comsol/files/2020/05/WaveOpticsModuleUsersGuide.pdf）来源10
- [外]（出处：https://www.synopsys.com/photonic-solutions/rsoft-photonic-device-tools/passive-device-beamprop.html）来源11
- [外]（出处：https://www.synopsys.com/photonic-solutions/rsoft-photonic-device-tools/rsoft-products.html）来源12
- [外]（出处：https://qacf-www.synopsys.com/content/dam/synopsys/photonic-solutions/documents/whitepapers/rsoft-effective-index-method.pdf）来源13
- [外]（出处：https://en.wikipedia.org/wiki/Beam_propagation_method）来源14
- [外]（出处：https://web.stanford.edu/group/fan/S4）来源15
- [外]（出处：https://web.stanford.edu/group/fan/publication/Liu_ComputerPhysicsCommunications_183_2233_2012.pdf）来源16
- [外]（出处：https://doi.org/10.1016/j.cpc.2012.04.026）来源17
- [外]（出处：https://github.com/victorliu/S4/blob/master/S4/rcwa.h）来源18
- [外]（出处：https://arxiv.org/pdf/2608.06185）来源19
- [外]（出处：https://meep.readthedocs.io/en/latest/License_and_Copyright/）来源20
- [外]（出处：https://mpb.readthedocs.io/en/latest/）来源21
- [外]（出处：https://web.stanford.edu/group/fan/S4/license.html）来源22
- [外]（出处：https://lumerical.docs.pyansys.com/version/stable/examples/lumopt2/y_branch/pylumerical_y_branch.html）来源23
- [外]（出处：https://www.3ds.com/products/simulia/cst-studio-suite/electromagnetic-simulation-solvers）来源24
- [外]（出处：https://www.comsol.com/products/licensing/）来源25
- [外]（出处：https://ansys.com/content/dam/web/webinars/ansys-cpo-multiphysics-lumerical-mechanical-interop-flow.pdf）来源26
- [外]（出处：https://r.jina.ai/https://ansys.com/content/dam/web/webinars/ansys-cpo-multiphysics-lumerical-mechanical-interop-flow.pdf）来源27
- [外]（出处：https://optics.ansys.com/hc/en-us/articles/46499056867603）来源28
- [外]（出处：https://r.jina.ai/https://optics.ansys.com/hc/en-us/articles/46499056867603）来源29
- [外]（出处：https://optics.ansys.com/hc/en-us/articles/5258777726227-Thermally-aware-photonic-circuit-simulation-of-a-WDM-transceiver-Icepak-integration）来源30
- [外]（出处：https://kb.lumerical.com/en/ref_scripts_addimportheat.html）来源31
- [外]（出处：https://support.lumerical.com/hc/en-us/articles/1500007188582）来源32
- [外]（出处：https://support.lumerical.com/hc/en-us/articles/360050995394）来源33
- [外]（出处：https://support.lumerical.com/hc/en-us/articles/360052044913）来源34
- [外]（出处：https://meep.readthedocs.io/en/latest/Python_Tutorials/Adjoint_Solver/）来源35
- [外]（出处：https://arxiv.org/pdf/2410.07353v1）来源36
- [外]（出处：https://optics.ansys.com/hc/en-us/articles/360034394274-Using-Parseval-s-theorem-to-check-for-energy-conservation-between-the-time-and-frequency-domain）来源37
- [外]（出处：https://optics.ansys.com/hc/en-us/articles/1500007397442-Integrating-the-Poynting-Vector）来源38
- [外]（出处：https://onlinelibrary.wiley.com/doi/10.1002/lpor.201700237）来源39
- [外]（出处：https://meep.readthedocs.io/en/latest/Python_Tutorials/GDS_Import/）来源40
- [外]（出处：https://onlinelibrary.wiley.com/doi/10.1155/ijap/2733569）来源41
- [外]（出处：https://arxiv.org/abs/0907.3570）来源42
- [外]（出处：https://www.imec-int.com/en/articles/high-na-euvl-next-major-step-lithography）来源43
- [外]（出处：https://asml.com/en/products/duv-lithography-systems/twinscan-nxt1970ci）来源44
- [外]（出处：https://asml.com/en/en/products/duv-lithography-systems/twinscan-nxt2000i）来源45
- [外]（出处：https://repository.tudelft.nl/file/File_4570eb9d-759c-47b8-a9d3-8af3ba1cf531?preview=1）来源46
- [外]（出处：https://doi.org/10.1117/12.916118）来源47
- [外]（出处：https://iopscience.iop.org/article/10.1088/1361-6528/ae150a）来源48
- [外]（出处：https://doi.org/10.1088/1361-6528/ae150a）来源49
- [外]（出处：https://iopscience.iop.org/article/10.1088/0960-1317/25/1/015003）来源50
- [外]（出处：https://doi.org/10.1364/ol.36.002480）来源51
- [外]（出处：https://ieeexplore.ieee.org/document/4895221）来源52
- [外]（出处：https://opg.optica.org/abstract.cfm?URI=ol-26-23-1888）来源53
- [外]（出处：https://doi.org/10.1117/12.483242）来源54
- [外]（出处：https://eprints.soton.ac.uk/504148/1/TSM3583925.pdf）来源55
- [外]（出处：https://arxiv.org/html/2610.15754v1）来源56
- [外]（出处：https://opg.optica.org/abstract.cfm?URI=ol-34-13-1958）来源57
- [外]（出处：https://apps.mnc.umn.edu/pub/equipment/ald-film-characterization.pdf）来源58
- [外]（出处：https://semiengineering.com/hybrid-bonding-makes-strides-toward-manufacturability/）来源59
- [外]（出处：https://arxiv.org/abs/2611.18713）来源60
- [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC12680666）来源61
- [外]（出处：https://doi.org/10.1038/s41377-025-02064-w）来源62
- [外]（出处：https://photonica.io/articles/fiber-array-attach）来源63
- [外]（出处：https://doi.org/10.3390/app10041538）来源64
- [外]（出处：https://nature.com/articles/s41377-025-02048-w）来源65
- [外]（出处：https://pubs.acs.org/doi/full/10.1021/acsphotonics.2c01194）来源66
- [外]（出处：https://ieeexplore.ieee.org/document/6621507）来源67
- [外]（出处：https://www.synopsys.com/content/dam/synopsys/photonic-solutions/documents/whitepapers/modeling-silicon-photonics-wp.pdf）来源68
- [外]（出处：https://dev.photonicsmanufacturing.org/sites/default/files/documents/2024_ipsr-i_silicon_photonics_updated_v2.pdf）来源69
- [外]（出处：https://photonica.io/articles/cutback-propagation-loss）来源70
- [外]（出处：https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nbsspecialpublication637v2.pdf）来源71
- [外]（出处：https://photonica.io/articles/waveguide-loss-measurement-methods-compared）来源72
- [外]（出处：https://pubmed.ncbi.nlm.nih.gov/40219451）来源73
- [外]（出处：https://opg.optica.org/abstract.cfm?uri=oe-26-14-18082）来源74
- [外]（出处：https://opg.optica.org/abstract.cfm?URI=ol-35-17-2849）来源75
- [外]（出处：https://www.photonica.io/articles/modulator-vpi-measurement）来源76
- [外]（出处：https://pubmed.ncbi.nlm.nih.gov/20720943）来源77
- [外]（出处：https://iopscience.iop.org/article/10.35848/1347-4065/abeedd）来源78
- [外]（出处：https://optoelectronics.ece.ucsb.edu/sites/default/files/2017-03/16OL-zhang.pdf）来源79
- [外]（出处：https://www.photonica.io/articles/how-to-measure-modulator-bandwidth）来源80
- [外]（出处：https://keysight.zinfi.net/concierge/OEMs/keysight/wwwcontent/Attachments/pdf/8177_5992-2481EN.pdf）来源81
- [外]（出处：https://www.keysight.com/us/en/product/N4391A/optical-modulation-analyzer.html）来源82
- [外]（出处：https://www.keysight.com/us/en/assets/7018-02043/data-sheets/5990-3509.pdf）来源83
- [外]（出处：https://nature.com/articles/s44172-025-00421-6）来源84
- [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC9416656/）来源85
- [外]（出处：https://arxiv.org/pdf/1307.2417）来源86
- [外]（出处：https://opg.optica.org/abstract.cfm?uri=oe-30-17-30600）来源87
- [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC12471392/）来源88
- [外]（出处：https://www.mdpi.com/1424-8220/23/1/122）来源89
- [外]（出处：https://www.photonica.io/articles/how-to-measure-photodetector-bandwidth）来源90
- [外]（出处：https://www.photonica.io/articles/photodetector-characterization）来源91
- [外]（出处：https://www.nature.com/articles/s41566-021-00893-w）来源92
- [外]（出处：https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication250-41e2008.pdf）来源93
- [外]（出处：https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.250-95.pdf）来源94
- [外]（出处：https://www.bipm.org/documents/20126/44556012/CCPR-K2.b.2016.pdf）来源95
- [外]（出处：https://www.nature.com/articles/s41566-025-01759-1）来源96
- [外]（出处：https://www.nature.com/articles/s41578-025-00830-1）来源97
- [外]（出处：https://doi.org/10.1063/1.98956）来源98
- [外]（出处：https://sciencedirect.com/science/article/pii/S1359028696800623）来源99
- [外]（出处：https://inziv.com/content/wafer-level-optical-testing-how-to-separate-device-variation-from-coupling）来源100
- [外]（出处：https://photonics.com/Articles/Near-Field_Scanning_Optical_Microscopy_and/a18134）来源101
- [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC4823800）来源102
- [外]（出处：https://doi.org/10.1117/12.2000807）来源103
- [外]（出处：https://iopscience.iop.org/article/10.1088/2050-6120/aaae0c）来源104
- [外]（出处：https://inziv.com/content/which-wafer-level-test-systems-handle-die-to-die-optical-alignment）来源105
- [外]（出处：https://formfactor.com/download/fully-automated-integrated-silicon-photonic-wafer-test?wpdmdl=82376）来源106
- [外]（出处：https://swtestasia.org/2024proc/pdf/F05_02_ROTTOLI_SWTestAsia2024.pdf）来源107
- [外]（出处：https://www.mdpi.com/2072-666X/17/5/592）来源108
- [外]（出处：https://www.mdpi.com/2674-0729/5/3/21）来源109
- [外]（出处：https://siliconcodesign.com/p/why-optical-high-volume-test-is-10x）来源110
- [外]（出处：https://api.p1.mks.com/medias/sys_master/images/images/h44/h10/8797304946718/WP-Laser-Diode-Burn-In-and-Reliability-Testing.pdf）来源111
- [外]（出处：https://cdn-agl.agiltron.com/dlc/certificates/SWLDlaserGR468-qualificationreport2021-03-16__Agiltron.pdf）来源112
- [外]（出处：https://ieee802.org/3/hssg/public/jan07/winzer_01_0107.pdf）来源113
- [外]（出处：https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2026-09/spie-pw-2026-published-1-.pdf）来源114
- [外]（出处：https://electrontest.com/telcordia-bellcore-gr-468-core）来源115
- [外]（出处：https://eps.ieee.org/wp-content/uploads/2026/04/Reliability-TC-Article-2025-IEEE-International-Reliability-Physics-Symposium-_Richard-Rao.pdf）来源116
- [外]（出处：https://attend.ieee.org/repp/wp-content/uploads/sites/244/croes22.pdf）来源117
- [外]（出处：https://opg.optica.org/abstract.cfm?URI=ol-34-17-2637）来源118
- [外]（出处：https://doi.org/10.1364/OL.34.002637）来源119
- [外]（出处：https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/94/PPAP_5F00_EXTERNAL_5F00_Qual_5F00_Memo_5F00_DLP5530SAFYSQ1.pdf）来源120
- [外]（出处：https://mouser.com/PCN/onsemi_Generic_IPCN25638X.pdf）来源121
- [外]（出处：https://jedec.org/sites/default/files/docs/22a104d.pdf）来源122
- [外]（出处：https://webstore.iec.ch/en/publication/64254）来源123
- [外]（出处：https://cdn.standards.iteh.ai/samples/102780/60eef617872d4d05ab4d1ca0d7e30692/IEC-61300-3-35-2022.pdf）来源124
- [外]（出处：https://www.rayopticcom.com/quality-control/）来源125
- [外]（出处：http://verizonnebs.com/TPRs/VZ-TPR-9431.pdf）来源126
- [外]（出处：https://blogs.cisco.com/sp/peace-of-mind-with-cisco-optics-part-2-of-3）来源127
- [外]（出处：https://standards.iteh.ai/catalog/standards/iec/42e28adc-f7b5-4914-9245-6c890fe63626/iec-tr-62721-2012）来源128
- [外]（出处：https://reliability.readthedocs.io/en/stable/Sample%20size%20required%20for%20no%20failures.html）来源129
- [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC11465988/）来源130
- [外]（出处：https://arxiv.org/html/2507.00546v2）来源131
- [外]（出处：https://www.nature.com/articles/s41467-026-73390-9）来源132
- [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC11636486/）来源133
- [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC13088363/）来源134
- [外]（出处：https://arxiv.org/abs/2611.08127）来源135
- [外]（出处：https://arxiv.org/abs/2604.01480）来源136
- [外]（出处：https://arxiv.org/abs/2608.20688）来源137
- [外]（出处：https://arxiv.org/abs/2606.00915）来源138
- [外]（出处：https://arxiv.org/abs/2508.10277）来源139
- [外]（出处：https://arxiv.org/abs/2608.18279）来源140
- [外]（出处：https://arxiv.org/abs/2607.00739）来源141
- [外]（出处：https://arxiv.org/abs/2607.18012）来源142
- [外]（出处：https://arxiv.org/abs/2607.23469）来源143
- [外]（出处：https://arxiv.org/html/2602.15762）来源144
- [外]（出处：https://ieeexplore.ieee.org/Xplore/home.jsp）来源145
- [外]（出处：https://atgbics.com/pages/qsfp-dd-optical-transceiver-technology-overview）来源146
- [外]（出处：https://fs.com/eu-en/blog/differences-between-qsfpdd-and-qsfp-qsfp28-qsfp56-osfp-cfp8-cobo-b1217.html）来源147
- [外]（出处：https://oiforum.com/wp-content/uploads/OIF-400ZR-02.0.pdf）来源148
- [外]（出处：https://lightwaveonline.com/optical-tech/transmission/article/14175125/oif-releases-400zr-optical-interface-implementation-agreement）来源149
- [外]（出处：https://cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/qsfp-dd-osfp-800g-zr-zr-plus-coherent-optics.pdf）来源150
- [外]（出处：https://lf.hamamatsu.com/certified-reliability）来源151
- [外]（出处：https://intertekinform.com/en-au/standards/gr-2854-core-issue-2-1063776_saig_tel_tel_2474337）来源152
- [外]（出处：https://gigalight.com/ols-dcm.html）来源153
- [外]（出处：https://img-en.fs.com/file/datasheet/80-km-passive-dispersion-compensation.pdf）来源154
- [外]（出处：https://www.oiforum.com/oif-launches-the-industrys-first-co-packaging-standard-the-3-2t-co-packaged-module-implementation-agreement）来源155
- [外]（出处：https://www.oiforum.com/wp-content/uploads/OIF-Co-Packaging-3.2T-Module-01.0.pdf）来源156
- [外]（出处：https://www.oiforum.com/meetings-events/448gbps-signaling-for-ai-workshop-apr-2025/）来源157
- [外]（出处：https://osfpmsa.org/assets/pdf/OSFP_Module_Specification_Rev4_1.pdf）来源158
- [外]（出处：https://arista.com/assets/data/pdf/Datasheets/Arista-800G_Optics_FAQ.pdf）来源159
- [外]（出处：https://lightwaveonline.com/optical-tech/transmission/article/16673333/qsfpdd-msa-group-releases-optical-transceiver-form-factor-specification）来源160
- [外]（出处：https://canjinoptics.com/qsfp-dd-msa-hardware-walkthrough）来源161
- [外]（出处：https://www.oiforum.com/meetings-events/cmis-tutorial-webinar-series/）来源162
- [外]（出处：https://doi.org/10.1016/j.solener.2021.01.024）来源163
- [外]（出处：https://doi.org/10.1016/j.solener.2018.02.071）来源164
- [外]（出处：https://nlr.gov/media/docs/libraries/pv/solar-module-efficiency-data-guide.pdf）来源165
- [外]（出处：https://docs.nlr.gov/docs/fy02osti/32284.pdf）来源166
- [外]（出处：https://nrel.gov/docs/fy18osti/70016.pdf）来源167
- [外]（出处：https://publica-rest.fraunhofer.de/server/api/core/bitstreams/45de307b-9a27-4c48-8d75-a646807cde3d/content）来源168
- [外]（出处：https://webstore.iec.ch/en/publication/3587）来源169
- [外]（出处：https://assets.vde-verlag.de/iec-normen/preview-pdf/info_iec60825-1%7Bed3.0%7Db.pdf）来源170
- [外]（出处：https://rli.com/resources/articles/classification.aspx）来源171
- [外]（出处：https://drs.illinois.edu/Page/SafetyLibrary/LaserClassification）来源172
- [外]（出处：https://seibersdorf-laboratories.at/fileadmin/user_upload/docs/le/las/publ/whitepaper_iec-60825-1.pdf）来源173
- [外]（出处：https://doi.org/10.6028/nist.sp.250-41）来源174
- [外]（出处：https://doi.org/10.6028/nist.sp.250-53）来源175
- [外]（出处：https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=706）来源176
- [外]（出处：https://newport.com/t/nist-traceable-spectral-responsivity-calibration-of-photodiode-detectors）来源177
- [外]（出处：https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=956830）来源178
- [外]（出处：https://doi.org/10.1109/imtc.1999.776144）来源179
- [外]（出处：https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=932473）来源180
- [外]（出处：https://bipm.org/kcdb/comparison/download/published-section-block-file/106/384/degree/384/ccpr-k1a_pdf_2015.pdf）来源181
- [外]（出处：https://bipm.org/documents/20126/2071034/CCPR-G6+Guidelines+for+RMO+key+comparisons+in+PR.pdf/ee7147f6-26a4-3af2-9f18-f3c7dce8c8d4?download=true&t=1731063340983&version=1.9）来源182
- [外]（出处：https://www.bipm.org/en/committees/cc/ccpr）来源183
- [外]（出处：https://www.bipm.org/en/liaison/regional/apmp）来源184
- [外]（出处：https://www.bipm.org/en/jcgm-wg1-gum）来源185
- [外]（出处：https://www.bipm.org/en/committees/jc/jcgm/wg/jcgm-wg1-gum）来源186
- [外]（出处：https://iso.org/sites/JCGM/GUM/JCGM100/C045315e-html/C045315e_FILES/MAIN_C045315e/08_e.html）来源187
- [外]（出处：https://iso.org/sites/JCGM/GUM/JCGM100/C045315e-html/C045315e_FILES/MAIN_C045315e/04_e.html）来源188
