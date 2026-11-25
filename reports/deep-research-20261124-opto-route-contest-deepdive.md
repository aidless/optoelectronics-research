# 光电信息工程：技术路线竞争与成败史
生成日期：2026-11-24　｜　层级：技术路线之争——为什么某些路线胜出、哪些被证伪、判据是什么
## 范围
本报告是光电信息工程深度调研的技术路线层，聚焦 6 场路线之争：光模块与光互连、光计算、显示成像、激光光源、光伏电池、光电传感。与前序报告不重叠——回答的是「为什么这条路胜出、哪条被证伪、判据是什么」。
## 研究方法
deep-research-pro 外部检索闭环：每个主题换关键词重试≤2轮，到顶标未覆盖；WebFetch 深读 Top3-5 篇一手资料；每条主张附出处链接（方括号外链标记后紧跟来源，例：[外]（出处：https://www.nature.com/）示例主张）；单一来源标未验证；优先一手论文与权威机构（Nature/Science/Optica/IEEE/NREL/IRENA）；数字标口径；区分理论极限与实测值；不补写、不臆造。
六个主题共梳理 **43 条方法**：一手核验 **30** 条，确认未覆盖 **4** 条，汇集唯一来源 **128** 个。
## 核心结论
### 光模块与光互连路线之争
- CPO 的胜负手不是功耗单点，而是「省电+可靠性」在 AI 集群被同时定价：22dB→4dB 的电损耗与 ELS 把最大失效源外置，共同越过可维护性阈值；2024前屡次落空正是因为可插拔一直跟得上且 FIT/可修性未被证明。
- 材料路线的归属由物理不可替与经济规模共同决定：硅光赢数据中心靠 CMOS 规模经济+外置 InP 激光补发光短板，InP 守长途因1550nm 唯一可全功能，VCSEL 守多模短距靠成本/耦合容差，但速率抬升（SR8→DR8）会把它推出高速率段。
- LPO/LRO 是「DSP 放哪里」的连续谱，不是三选一：DSP 换互通与链路预算，LPO 换功耗与可插拔，CPO 换最低功耗但弃可修；100G/lane 的 LPO 因存量 DSP 生态只是小众，1.6T 因>30W 散热转向 LRO（<20W）。
- CPO 采用 ELS 的本质是把光学引擎与激光两个不成熟良率解耦、把主导失效的激光变成可热插拔件，50 FIT vs 300 FIT 的可靠性目标比每 bit 功耗更能决定能否规模部署。
- 调制格式由距离与 DSP 工艺共同驱动：短距 PAM4 换低功耗，长距相干 DP-16QAM 换灵敏度与频谱效率；2nm 相干 DSP 让1.6T ZR 下沉到20km campus，说明「相干下沉」是工艺事件而非协议事件。
- 淘汰路线的共同判据：赢家不是单项参数最优，而是可靠性/可量产/单位成本/可维护性综合阈值最低者；术语也会误导（MEMS 固态仍属机械、硅光被看衰是因不发光而非无前景）。
### 光计算路线与商业化成败
- 全光计算屡屡商业化失败的物理根因不是线性MAC，而是缺可级联全光非线性器件与光存储：MIT 2025『全光网络』的实际非线性仍靠光电二极管+电调制，纯光路线至今未成立，工业界收敛到光做线性+电做非线性的混合架构。
- 最强成败判据是能效『口径』：曦智PACE 4.21 TOPS/W(不含激光)一旦计入激光降到2.38 TOPS/W，降幅约43%——厂商普遍用不含激光的口径报数，全系统墙插效率才是能否商用的一致标尺。
- 第二条判据是精度天花板：PACE 7.61 ENOB且±5°C掉约1 bit，模拟精度止步8–10 bit，决定了光计算只能做推理/组合优化，难以做需高精度与频繁权重更新的训练。
- 兑现已从『光计算』转移到『光互连』：Ayar $500M E轮、Lightmatter转向Passage、Marvell约$3.25B收购Celestial，都是CPO/光I/O；原因是互连接口标准清晰、可逐步替换、量测成熟、量产可行性远高于全光计算芯片。
- 最先落地的应用是组合优化(Ising/Max-cut)而非AI训练：PACE在5 ns循环下平均收敛率>92.72%，但迭代次数(537)多于A10(347)，宣称近500×只是单周期口径——评估必须用完整求解时间而非单步延迟。
- 历史周期：2010s『over-promised and it backfired』(MIT 2017元音识别仅77% vs电子90%、只验证构建块)，2020s由大模型算力与互连功耗墙重启，资本与并购真正落地在互连，计算仍处pilot/首批客户阶段。
### 新型显示与成像路线之争
- 显示/成像路线胜负的通用判据不是单项画质，而是“性能上限×良率×节拍×成本×生态规模”的乘积；Micro LED把画质上限推到极致，却败在亿级像素逐颗转移的统计良率和吞吐。
- 像素数把良率要求推到反直觉区间：4K>2400万子像素、8K约1亿；99.99999%良率仍有约2个4K坏点，KLA提出99.9999%（six nines）才是显示业可接受良率。
- AR近眼光学的胜者是形态因子：波导以几毫米眼镜形态和大eye box赢 lightweight AR，但50-200 nit/lm vs 几何组合器约4000 nit/lm说明其效率与制造仍是代价；birdbath靠10-15%显示光和25-30%透视上限换取低成本与量产。
- 衍射波导内部没有绝对赢家：SRG成熟但色散/漏光，VHG便宜快速但透射鬼影，PVG效率近理论上限但依赖偏振光源和大面积制造；判据是全FOV最小效率与均匀性，而非峰值效率。
- CMOS击败CCD、非制冷红外挤压制冷红外的共同逻辑是CMOS/MEMS工艺集成、功耗与成本规模化；高端性能路线（CCD、制冷 photon detector）不会立即消失，但被推向窄众高价值场景。
- 失败路线复盘需防事后叙述：PDP在2010年出货创纪录、2009年仍占全球电视7%，真正退出在2013年；DLP与3LCD则是长期并存，判据是应用匹配而非技术优劣。
### 激光与光源路线之争
- 路线胜负判据不是单一物理极限，而是多维权衡：波长/带隙可得性 × 电泵浦可行性 × 效率 × 光束质量 × 寿命/运维 × 成本/CMOS 兼容。谁在目标应用占的权重最大，谁胜出。
- 硅光源之争的分水岭是"电泵浦+1550nm+CMOS 兼容"三条同时满足：拉曼/多孔硅/掺 Er 各因光泵本质、低效率、无电泵净增益出局；键合 III-V 成近期商用最优，单片外延 QD 是长期方向。
- 工业加工的决定性数字是电光效率 50-55%(光纤) vs 10-15%(CO2) vs 3-5%(Nd:YAG) 与钢吸收率 35-40%@1.07μm vs 5-10%@10.6μm——这直接决定 5 年 TCO，光纤因此替代 CO2。
- "固态化/免维护化"是跨主题的统一替代逻辑：染料→钛宝石(避有毒溶液)、气体→光纤/半导体(避气体放电与镜片维护)、固体超快→光纤+SESAM(避自由空间对准)。
- 2026 窄线宽开始从"极限线宽单一指标"转向"线宽×无跳模调谐×集成度"的系统判据：RE-DBR 用 finesse 改写权衡，24Hz/34GHz/<4mm² 是这一转向的量化标志。
- 材料体系归属高度绑定工艺成熟度而非纯带隙最优：InP 拿 1310/1550(尽管 VCSEL 死穴多)、GaAs 拿 VCSEL(氧化孔径成熟)、GaN 拿蓝光(p 型 GaN 突破)。
### 光伏电池路线之争
- 光伏路线竞争的主判据是场址化LCOE与25–30年可融资寿命，不是裸电池冠军效率；效率只有转化为稳定量产良率、低CAPEX/O&M和更低系统成本时才改变产业份额。
- 晶硅胜出靠的是产业链共同学习曲线与制造生态，不是硅材料在物理上不可替代；当硅料暴涨时薄膜得到窗口，硅料崩跌后窗口关闭，说明成本冲击会重排路线。
- First Solar的CdTe是‘利基胜出’：在美国大型地面电站，用低衰减、高温表现、本地制造与政策/银行可融资性抵消效率低于晶硅，而不是在通用组件市场效率反超。
- 2025–26硅电池内部，TOPCon是成本-效率-设备兼容的当前主场，BC不是简单替代而是可叠加架构；BC能否扩份额取决于背面图形化良率、贵金属降耗和屋顶溢价。
- 最有望翻盘的下一代是钙钛矿-硅叠层；它的门槛已从‘小面积效率’转为‘大面积稳定效率+铅阻隔+25年寿命+良率+每瓦成本’，任何单指标破纪录都不构成产业化判决。
- CPV与多数第三代概念的共同教训是：电池物理效率提升若不能覆盖新增光学、机械、热管理和运维复杂度，就不会赢；系统级简化往往比峰值效率更具产业决定性。
- 2000s与2010s洗牌均由政策需求脉冲、原料/产能周期和融资杠杆共同触发；能够活下的企业不一定拥有当时最高实验室效率，但一定拥有最低可持续成本、最大规模与最强供应链。
### 光电传感与测量路线之争
- 车载LiDAR的胜出路线不是'最固态'，而是在150–350 m量程、车规、成本三重约束下把可动件和BOM一起压下来的905 nm VCSEL+一维转镜混合固态；纯机械在L2/L3近乎退出，OPA/Flash未量产。
- AEC-Q102式可靠性是比实验室峰值功率更硬的淘汰判据：42颗AR-VCSEL阵列6000 h HTOL零失效、FIT<0.8@90%置信，才把多结VCSEL从器件论文推到AT128级产品。
- FMCW的胜负判据是'每点速度+抗干扰'场景，不是通用替代ToF；其瓶颈已从线宽转到啁啾线性度与功率/封装，且2025原稿距离分辨率公式漏因子6，必须用2026更正式。
- 光纤传感没有单一赢家：FBG赢点精度与复用(1 pm/µε、100 km)，Brillouin赢10–100 km长距(0.2–3 m分辨)，Rayleigh/OFDR赢mm级局部细节(≤30 m)，判据是分辨率—量程—被测量的三角而非路线标签。
- 医学成像与无创血糖共同说明：分辨率/穿透深度或相关度/置信界的物理权衡不会因为算法而消失；无创血糖商用失败的根因是ISO/iCGM级可治疗决策准确度和FDA授权门槛，而非缺一个更好的光谱峰。
## 关键要点
**光模块与光互连路线之争** 的开放问题：
- Nature Communications 汽车 LiDAR 综述全文抓取超时（仅标题/摘要可见），机械→固态的量化分歧未从一手正文核实；LiDAR <$100/颗为 IEEE 文献摘要单源，未验证。
- 1.6T 各路线 pJ/bit 数字来自 Photonica 聚合估算，非厂商或测量实测；Nvidia 3.5x/10x、Broadcom 65%/100万端口小时均为厂商宣称，缺独立复测。
- LightCounting 的10-15% scale-up 互连迁 NPO/CPO 与$52.1B(2031) 为机构预测口径，真实渗透率取决于 2026-2027 出货兑现；400G/lane serdes 与 PAM6 走向未定（802.3dv）。
- Broadcom Tomahawk 6 Davisson 与 Nvidia Quantum-X/Spectrum-X 的批量出货/客户名单主要来自厂商与媒体，缺运营商侧独立验证。
**光计算路线与商业化成败** 的开放问题：
- Taichi 160 TOPS/W的精确口径(是否含激光、DAC/ADC与电子外围)在Science正文与清华官方新闻页均未标明，需读全文核实；本文件按清华官方『片上能效』口径记录。
- LightGen百万光神经元与7–8个数量级能效/算力提升属团队宣称，SCMP原文被Cloudflare拦截、Science正文未深读，需独立可复现的墙插数据才能从『单源未验证』升级。
- Celestial AI收购对价存在冲突：The Register称约$3.25B已成交，datadeep称最高$5.5B(现金+股票)，需一手并购公告厘清。
- Luminous Computing是否确于2023-05裁员并退出光计算类别，仅有datadeep单一二手来源，缺公司一手/权威媒体确认。
- NSR综述《Prospects of photonic computing for artificial intelligence》(doi 10.1093/nsr/nwag089)PMC镜像被reCAPTCHA拦截未能深读，其系统性判据未纳入本文件。
**新型显示与成像路线之争** 的开放问题：
- Micro LED何时翻盘：需跟踪消费级die ≤100 µm²、芯片良率/转移良率、≥G4.5/G6量产线与成本追平OLED的时间点；SID 2025称转移吞吐需>5个数量级提升。
- OLED烧屏量化寿命：RTINGS页面meta仅给出近3年、>10000小时、100台电视的加速测试，正文嵌入Vue未抽取逐面板/逐时长烧屏差异，需另取可解析原始数据。
- 量子点/有机图像传感器与QWIP/T2SL红外的路线内部判据未覆盖，需换可访问的一手论文/厂商数据补做。
- 早期LCoS失败判据未覆盖，需获取Springer章节、MDPI或其他可访问综述正文，验证开口率、光效、良率与量产成本。
- LCD被动矩阵到主动矩阵的量化淘汰判据未在本次两轮检索内取得可核验数字，只保留LCD响应5-25 ms/overdrive ~1 ms与主流化背景。
**激光与光源路线之争** 的开放问题：
- 主题4(超快)三篇仅摘要级证据，正文付费墙，SESAM 脉宽/平均功率/重频一手硬数字未取到；optics.org 综述 404，需补 Optica/IEEE 全文或厂商(如 Coherent/Menlo)白皮书。
- 主题1 中 GaAs/InP 精确带隙数值(约 1.42/1.35eV@300K)仅来自片段，未从一手表格核实；GaN 3.4eV 来自会议摘要片段，需权威数据表复核。
- 主题6 染料/气体激光的份额萎缩缺市场份额年份序列(如全球激光营收按类型占比)，目前仅定性替代逻辑+2002 年定性证据。
- 主题5 硅光亚 Hz(arxiv 2610.22596)与集成外腔 ECDL(arxiv 2601.18609)为预印本/实验室口径，量产一致性与温漂封装数据未覆盖。
- Photonic21/Photonics.com "50 Years of the Laser Industry" 被 Cloudflare 拦截，产业史量化节点(2013 $800M 之后)未取到。
**光伏电池路线之争** 的开放问题：
- 2026年PERC/TOPCon/HJT/TBC/HBC的‘名义产能、实际投产、有效产量、出货份额’缺少同口径公开表；当前只能以ITRPV的2025实际产量结构和2026量产效率预测替代，需取得VDMA/ITRPV原表后补足。
- 钙钛矿-硅叠层尚缺可核验的2026量产组件效率分布、良率、$/W、铅浸出与IEC/现场25年等效数据；实验室约35%纪录不能外推量产。
- 热载流子、MEG、中间带与量子点缺少同面积、同光谱、同稳态MPP与同认证机构的最新器件效率对照，故‘谁最接近实用’目前只能做工程成熟度判断，不能给硬排名。
- First Solar CdTe的成本优势来自制造、衰减、BOS、税收抵免与本地化的组合；公开资料没有可跨地区直接比较的统一$/W或LCOE底数，需用具体电站项目敏感性分析验证。
- CPV在高DNI地区是否存在利基复兴，需要2026年在运项目LCOE、追踪器故障率、清洗/运维与组件价格数据；本项只核验了2012–2015退场机制。
**光电传感与测量路线之争** 的开放问题：
- VCSEL+一维转镜方案在整车生命周期(>15年、振动+沙尘+温循)的现场失效率是否真能复现6000 h HTOL外推的FIT<0.8？需要车队级售后数据而非外推。
- 当$100 BOM门槛被满足时，混合固态与FMCW在L4 Robotaxi的实际TCO(含数据处理与冗余)谁更低？现有Nature评论只给分立成本/复杂度判断，没有整车账。
- Rayleigh OFDR声称的单点成本比Raman低100×，在>10 km分布式部署中是否仍成立？综述未给同口径现场报价。
- DiaMonTech MIR光热MARD 20.7%/19.6%离iCGM 70–180 mg/dL ±15% >70%的置信门槛仍远；其'adjunctive'定位能否转成FDA正式许可，2026年中上市计划后需复查。
## 路线逐条核实
### 光模块与光互连路线之争
#### 1. 可插拔光模块 vs CPO（共封装光学）：从反复狼来了到2026兑现
- **竞争逻辑**：路线对立：可插拔把光引擎做成独立、可热插拔的模块，CPO 把光引擎与交换 ASIC 封在同一基板/中介层。胜负判据是四条物理/工程约束的此消彼长——(1)信号完整性：CPO 让 ASIC 用低功耗 XSR/VSR SerDes 直驱光引擎，去掉模块 DSP 与 retimer，电损耗从约22dB降到约4dB（Nvidia 官方口径）；(2)功耗：51.2T 系统里光互连占总系统功耗约50%、光相关占系统成本约80%（IEEE EPS 引述），省 DSP 与长距 SerDes 可降系统功耗约25-30%；(3)可维护性：可插拔可30秒现场更换，CPO 除激光源（ELSFP 可热插拔）外的光引擎在机内，故障需整板返修，FIT 必须做到与 ASIC 同级；(4)散热：光引擎紧贴高功耗 ASIC 造成热密度与热串扰，需 TIM/热通道/分离散热盖，早期不可解。为什么2024前屡次狼来了：Cisco 在 OFC2023 演示 25.6T CPO（8×3.2T 光引擎、64×400G FR4）反响冷淡，SemiAnalysis 指出部署级产品到2025才出现，期间可插拔一直跟得上速率、且互通/可修…
- **硬数字**：电损耗约22dB→约4dB（Nvidia 技术博客2025-09-04，厂商口径）；系统功耗可降约25-30%、51.2T 光互连约占系统功耗50%/成本约80%（IEEE EPS CPO 综述引述）；1.6T 每端口 DSP可插拔22W≈13.8pJ/bit vs CPO≈10.2W≈6.4pJ/bit，网络级3.5x 能效（Photonica 聚合估算，非厂商实测）；Broadcom/Meta 100万 400G-equiv 端口设备小时 flap-free、65% 省电（厂商宣称）；Nvidia CPO resiliency 10x→GPU 利用率5x（厂商宣称）；CPO 市场2026 $34M→2031 $10B+，2026 数十万端口→2031 超300万端口（Lumentum 引 LightCounting 预测）；LightCounting 预测仅假设2030-31 有10-…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://lumentum.com/sites/default/files/2026-06/elsfpreliability-wp-cl-ae.pdf）来源链接
  - [外]（出处：https://www.lumentum.com/en/blog/reliability-becomes-new-currency-how-cpo-rewriting-laser-performance）来源链接
  - [外]（出处：https://eps.ieee.org/wp-content/uploads/2025/11/Photonics_TC_Co-Packaged_Optics_Final.pdf）来源链接
  - [外]（出处：https://photonica.io/articles/pluggable-lpo-lro-cpo）来源链接
  - [外]（出处：https://lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377）来源链接
  - [外]（出处：https://newsletter.semianalysis.com/p/co-packaged-optics-cpo-book-scaling）来源链接
  - [外]（出处：https://datacenterdynamics.com/en/analysis/optical-illusion-is-co-packaged-optics-the-savior-the-data-center-industry-has-been-waiting-for）来源链接
  - [外]（出处：https://theregister.com/special-features/2025/11/22/copackaged-optics-have-officially-found-their-killer-app/2014010）来源链接
#### 2. 硅光 vs InP vs VCSEL：中短距/长距的路线归属与物理经济判据
- **竞争逻辑**：路线对立根源在材料能带与工艺经济。硅是间接带隙，不能高效发光，但可导光/调制/分光/探测，且复用成熟 CMOS 产线，密度高、成本低、可大规模集成，因而在数据中心短距（DR/FR、500m-2km）调制器侧胜出——判据是单位 bit 成本与产能，而非发光能力，CW 光源靠外置 InP 激光补齐。InP 是直接带隙，在1550nm/1310nm 低损耗窗口能产生/放大/调制/接收光且电子迁移率高，是长距相干、可调激光与 CW 光源不可替代者——判据是1550nm 唯一可全功能材料 + 长距链路预算。VCSEL+多模光纤（850nm、50μm OM2-5）以低成本低功耗守极短距（100m 级 AI 机内/机架内），判据是耦合容差大、无需精密对准；但其带宽距离积受限，200G/lane 时铜逼近极限、VCSEL shortening。历史反转：Nvidia 从 800G SR8（VCSEL 多模）转 DR8（单模）直接终结2024中的 VCSEL 短缺，说明速率抬升会把路线从中短距多模推到单模硅光；同时 InP 激光因 CPO ELS 需求反而扩产紧俏。硅光赢数据中心是 CMOS 规模经济 …
- **硬数字**：2026 首次硅光调制器收发器销售额超过全部约$40B 收发器市场的50%，硅光从起步到起量耗时近十年（LightCounting 2026-05）；光芯片市场2025 $4B→2031 $15B（近4倍），硅光芯片占比约1/3→42%(约$6.3B)，InP 激光(CW/可调/PIC)占比58%→46%(约$6.9B)仍为最大细分（机构预测）；AI 光市场2025 $16.5B→2026 $26B（连续两年约60%增长），VCSEL 短缺因 Nvidia 800G SR8→DR8 于2024中消失、InP 激光扩产2026中缓解（LightCounting 2026-01）；10G SFP+ 单价2001 >$1000→2010 <$100→2023约$10（LightCounting 2023-11，说明硅化/规模经济压价）；Intel 研发硅光20+年、2016-17 推100G P…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377）来源链接
  - [外]（出处：https://lightcounting.com/newsletter/en/january-2026-optics-for-ai-clusters-366）来源链接
  - [外]（出处：https://lightcounting.com/research-note/november-2023-lumentum-is-back-in-intel-is-out-315）来源链接
  - [外]（出处：https://doi.org/10.1117/12.630237）来源链接
  - [外]（出处：https://trendforce.com/news/2026/08/06/news-inp-shortage-emerges-as-ai-optical-interconnect-bottleneck）来源链接
  - [外]（出处：https://cisco.com/c/dam/en/us/products/collateral/interfaces-modules/transceiver-modules/wp8350-hdr-mmf.pdf）来源链接
  - [外]（出处：https://blog.sumitomoelectriclightwave.com/vcsel-applications-for-ai-factory）来源链接
#### 3. LPO（线性直驱） vs DSP 可插拔 vs CPO：功耗/成本/链路预算三方之争
- **竞争逻辑**：三路线争的是把均衡与 CDR 放在哪。DSP 可插拔在模块内做完整均衡，代价是模块功耗的一半来自 DSP，但换来 any-to-any 互通与成熟链路预算（主 FEC RS(544,514) 终止在交换 ASIC，非模块）。LPO 用高线性 TIA 去掉 DSP/CDR，把均衡分摊给 switch ASIC+driver+TIA，省功耗降时延、保持可热插拔；代价是 BER 升高导致距离缩短、依赖 host-module 组合难多厂商互通、标准未定、SerDes 复杂度上升。CPO 把同样的去 DSP 逻辑封进厂商交换机，功耗最低但丧失现场可修与多厂商互通。LPO 在2024-2026重新升温的直接原因：DSP 模块在200G/lane 已达23-25W、散热逼近极限，而交换 ASIC 的 SerDes 能力已足以承接均衡；OFC2024/2025 Eoptolink、MACOM、Marvell、Innolight 与 OIF 互通展示把生态补齐。但 LRO（收端去 DSP、保发端 DSP 满足 IEEE 802.3）成为更现实的折中：CPO 阵营以可靠性/节能为主张，LPO 阵营以可插…
- **硬数字**：1.6T 每端口：DSP 可插拔22W≈13.8pJ/bit、LPO≈12.6W≈7.9pJ/bit(省43%)、CPO≈10.2W≈6.4pJ/bit(省54%)（Photonica 聚合估算，非实测）；200G/lane：DSP 模块23-25W(下一代约20W)、LRO/RTLR 约16W(下一代14-15W)、LPO 目标约10W（Semtech 厂商口径）；512口 Tomahawk-6 级交换机 DSP→LPO 模块级省约500W、含散热近1kW；LPO 光距离目标500m≈3dB，条件好可达约2km/4dB(DR)；die-to-die 电损耗预算 LPO 22dB vs DSP 32dB，OIF/Semtech 争取扩到26dB；1.6T LPO 初始>30W、LRO<20W（IEEE EPS/Cignal）；OFC2024 Eoptolink 200G/λ 4并口、MAC…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://eps.ieee.org/wp-content/uploads/2026/03/Linear-Pluggable-Optics_V2-UPDATED.pdf）来源链接
  - [外]（出处：https://blog.semtech.com/200g-lpo-power-reach-and-loss-real-numbers）来源链接
  - [外]（出处：https://photonica.io/articles/pluggable-lpo-lro-cpo）来源链接
  - [外]（出处：https://lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377）来源链接
#### 4. CW 光源路线：外置激光源 ELS/ELSFP vs 片上集成激光
- **竞争逻辑**：对立是「把激光放在哪」。CPO 当前普遍用 ELS，判据有三：(1)热——交换 ASIC 盖温高，激光在高温下阈值升高、WPE 下降、波长漂移并按 Arrhenius 加速磨损；(2)统计——激光主导失效预算，坏激光在 CPO 内等于整板返修，外置可热插拔更换；(3)经济——解耦光学引擎与激光两个都不成熟的良率，避免良率相乘。OIF 2023 定义 ELSFP IA（盲插+保偏光纤输出+管理），CW-WDM MSA 定义 O 波段8/16/32波，使 ELS 可多供应商化。片上集成激光（异质集成 III-V 或量子点梳）的瓶颈是可靠性与每线功率/效率：要满足 CPO 激光源50 FIT（可插拔约300 FIT）的目标，且高温下保持低噪声与足够出光。共享光源方案（一分多+micro-ring）用8波每调制器约1mW、总插损约11.7dB 反推每波需约15mW，15% WPE 下8波约0.8W电≈0.5pJ/bit，说明光源预算本身可行，真正卡点在热与 FIT。量子点梳可直接电泵、每线噪声低；Kerr 微梳线数多但转换效率/每线功率历史偏弱（2020 turnkey soliton、202…
- **硬数字**：OIF CPO IA 目标激光源50 FIT vs 可插拔约300 FIT（>5x，Lumentum 引 OIF）；Lumentum UHP 额定20 FIT@400mW，加速测试外推9 FIT@60%置信/23 FIT@90%，>1亿加速设备小时零失效；其 Raman 泵浦平台近50万颗部署、>200亿设备小时、<1 FIT、2014年来零激光二极管现场失效（厂商宣称）；100 FIT→20 FIT 在7x24下约每年9次→1.75次故障（5x 服务调用下降）；ELS 算例：1x8 分配9.0dB+插损0.5dB+PM跳线0.2dB+耦合1.5dB+过剩0.5dB=11.7dB，每波出光源约15mW，15% WPE 下8波约0.8W≈0.5pJ/bit（Photonica 计算示例）；ECOC2026 Lumentum 展示 DWDM ELSFP 供 OCI MSA。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://photonica.io/articles/co-packaged-optics-light-sources）来源链接
  - [外]（出处：https://lumentum.com/sites/default/files/2026-06/elsfpreliability-wp-cl-ae.pdf）来源链接
  - [外]（出处：https://www.lumentum.com/en/blog/reliability-becomes-new-currency-how-cpo-rewriting-laser-performance）来源链接
  - [外]（出处：https://eps.ieee.org/wp-content/uploads/2025/11/Photonics_TC_Co-Packaged_Optics_Final.pdf）来源链接
#### 5. 光互连调制格式路线：NRZ vs PAM4 vs 相干（相干下沉）
- **竞争逻辑**：速率提升时 NRZ（1bit/符号）要求翻倍波特率与带宽，在112G→224G SerDes 时不可持续；PAM4（2bit/符号）以约112GBaud 承载224Gbps/lane，代价是 SNR 代价与对 FEC/均衡的依赖，成为 800G/1.6T 数据中心以太网的事实选择（802.3df 2024 批准800G，802.3dj 定义8×224G SerDes）。相干用双偏振 DP-16QAM（4bit/符号×2偏振）+DSP 补偿色散/PMD，需更高 DSP 功耗但换来长距与频谱效率，OIF 400ZR 把它做成单载波相干可插拔。相干下沉的判据是 DSP 工艺节点：Marvell 用2nm 相干 DSP 把1.6T ZR 做到 campus20km/metro120km/regional1000km，800G 相干到1000km/600G 2000km/400G 3000km，说明相干从长途向 DCI/campus 渗透。判据总结：距离与带宽决定调制复杂度，短距用 PAM4 换低功耗低成本，长距用相干换灵敏度与色散容忍；NRZ 退守低速与部分芯片间接口。802.3dv 已在讨论…
- **硬数字**：1.6T 由8×224Gbps SerDes 构成，800G 由8×112Gbps/lane 构成（Teledyne LeCroy 白皮书）；800G 标准 IEEE 2024 批准、1.6T 在802.3dj 制定（标准口径）；OIF 400ZR IA：单载波相干 DP-16QAM、120km 以内放大点到点 DWDM（100GHz/75GHz）、C-FEC 后错误底<1.0E-15、约60Gbaud（OIF 标准原文）；Marvell COLORZ 1600 为业界首个1.6T ZR/ZR+ 可插拔+2nm Electra DSP，覆盖20km/120km/1000km、C+L 波段 OSFP、带 MACsec；COLORZ 800 用2nm Libra，800G到1000km/600G到2000km/400G到3000km（厂商新闻稿宣称）；ADTRAN 400ZR 点到点 DWDM…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://oiforum.com/wp-content/uploads/OIF-400ZR-03.0.1.pdf）来源链接
  - [外]（出处：https://cdn.teledynelecroy.com/files/whitepapers/800ge-vs-1-6te.pdf）来源链接
  - [外]（出处：https://investor.marvell.com/_assets/_88edfb3f52300551f17c1e541972f365/marvell/news/2026-03-05_Marvell_Extends_ZR_ZR_Leadership_with_Industry_1010.pdf）来源链接
  - [外]（出处：https://ieee802.org/3/dv/public/2611/shrikhande_3dv_01a_2611.pdf）来源链接
  - [外]（出处：https://ieee802.org/3/dj/public/25_01/shrikhande_3dj_01_2501.pdf）来源链接
  - [外]（出处：https://adtran.com/en/products-and-services/open-optical-networking/pluggables-and-subsystems/coherent-zr-series/coherent-400zr-series）来源链接
  - [外]（出处：https://fibermall.com/blog/800g-in-data-center-pam4-or-coherent.htm）来源链接
#### 6. 淘汰/边缘化路线复盘：LiDAR 机械→固态、硅光由看衰到翻盘
- **竞争逻辑**：从失败/边缘化路线提炼判据。LiDAR：机械旋转式因活动件多、可靠性/成本/车规量产不达标被边缘化，路线演化为机械→混合固态(MEMS 微镜/转镜)→全固态(flash/OPA)；判据是 OEM 的四条硬指标——高性能、可负担、可靠、可量产，核心是 fewer moving parts。术语陷阱：「solid-state」被滥用，含 MEMS 微镜者仍属机械（Ouster 观点），2016 Velodyne 把 spin 传感器称 solid-state hybrid；Ouster 认为真正固态 flash 是终局但受功率/散斑/距离限制。硅光翻盘：1980s末起长期被看衰（间接带隙不发光、耦合/封装难、良率），Intel 2004 做出首个类晶体管硅光器件、2011 50Gb/s 硅光链路，2016-17 推100G 产品、2018 抢份额逼对手认真；Cisco/Huawei/Intel 的早期决策加速采用；2023 Intel 把收发器制造/客户支持卖给 Jabil、保留 SiP 设计与 CPO 开发。翻盘判据不是物理全能，而是 CMOS 规模经济+外置激光补短板+头部厂商背书共同…
- **硬数字**：2026 硅光调制器收发器销售额首超约$40B 市场50%、起量耗时近十年（LightCounting 2026-05）；Intel 2004 首个类晶体管硅光器件、2011 50Gb/s 硅光链路、研发20+年、2023 出售制造业务保留 SiP/CPO（LightCounting 2023-11 / VentureBeat）；LiDAR 三类：机械/混合固态/全固态（Nature Communications 2024-09 综述标题与摘要，全文抓取超时未核）；固态 LiDAR <$100/颗（IEEE 文献搜索摘要，单源未验证）；OEM 四指标：高性能/可负担/可靠/可量产（Ouster 厂商观点）；2016-12 Velodyne 从机械转固态。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377）来源链接
  - [外]（出处：https://lightcounting.com/research-note/november-2023-lumentum-is-back-in-intel-is-out-315）来源链接
  - [外]（出处：https://venturebeat.com/2021/05/24/intel-sees-bright-future-for-silicon-photonics-moving-information-at-light-speed-in-datacenters-and-beyond）来源链接
  - [外]（出处：https://www.nature.com/articles/s41467-024-51975-6）来源链接
  - [外]（出处：https://ouster.com/insights/blog/what-is-the-end-state-of-automotive-lidar）来源链接
  - [外]（出处：https://blog.leddartech.com/velodyne-shift-toward-solid-state-lidar-for-automotive-applications）来源链接
  - [外]（出处：https://ieeexplore.ieee.org/document/10234174）来源链接
  - [外]（出处：https://ieeexplore.ieee.org/ielx7/5/8540482/08438526.pdf）来源链接
### 光计算路线与商业化成败
#### 1. 全光计算 vs 光电混合：非线性必须靠电、无光存储是关键物理判据
- **竞争逻辑**：竞争逻辑：光的线性矩阵乘(MAC)天然低延迟低功耗，但『全光非线性』缺乏可级联、低功耗、可规模化的器件，且没有光存储，必须在光-电-光之间转换。因此工业界收敛到光电混合：光做线性、电做非线性激活/存储/控制。成败判据=能否把非线性与存储的电学代价压到不吞掉光学增益；以及能否在量产线上做出大规模、可校准、低误差的光电集成。宣称vs可核验：MIT 2025宣称『全光网络』，原文与Ars解读证实其非线性实为抽少量光进光电二极管测功率后再电调制剩余光，本质仍是电非线性——所以纯光路线未成立，混合路线才是可兑现妥协。
- **硬数字**：MIT全光原型(Nature Photonics, DOI 10.1038/s41566-024-01567-z)：3层6神经元、仅2个非线性单元、132参数、端到端DNN延迟410 ps、元音识别92%——规模远小于LLM(GPT-4约10^12参数，团队目标约10^5参数)。曦智PACE(Nature 2025)混合方案：64×64矩阵、>16,000光器件、1 GHz时钟/3 ns周期、实测8.19 TOPS；能效4.21 TOPS/W(不含激光口径)→2.38 TOPS/W(含激光口径)，激光功耗使能效下降约43%；30,000随机向量点积误差均值0.06 LSB、σ1.18 LSB，25 MHz下平均7.61 ENOB，±5°C温漂掉约1 bit(口径：PACE整系统实测)。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.nature.com/articles/s41586-025-08786-6）来源链接
  - [外]（出处：https://arstechnica.com/science/2025/01/getting-an-all-optical-ai-to-handle-non-linear-math）来源链接
  - [外]（出处：https://news.mit.edu/2017/new-system-allows-optical-deep-learning-0612）来源链接
#### 2. 创业公司路线分化：Lightmatter从光计算转向光互连，曦智双线并行
- **竞争逻辑**：竞争逻辑：纯光计算芯片要同时解决非线性、精度、封装、良率、软件栈，兑现周期长；光互连只需替换数据搬运，接口标准清晰、可逐步替换、量测标准成熟，故资本与产品先向互连倾斜。成败判据=是否有真实出货/量产客户(而非原型或未来宣称)。宣称vs可核验：Lightmatter的Envise曾商品化为4U服务器(含16块光子AI推理芯片)，但2024年D轮后明确把Passage晶圆级光互连interposer作为主线，Envise与Idiom软件栈仍在官网却已移出products类；Passage首批集群『2025年底上线』属CEO未来宣称，非已交付。曦智则计算器(PACE2/Gazelle)与光互连(Photowave CXL、Lightsphere X)双线并行。
- **硬数字**：Lightmatter：2024-10 D轮$400M、投后估值$4.4B、累计融资$850M、约200员工；Passage最多48个compute die、晶圆级interposer、集成激光/调制器/探测器(公司宣称)。曦智PACE2官网规格：128×128可配置光矩阵、8 bit光计算输出精度、>40,000光子器件、3D TSV先进封装；PACE(2021发布)二进制编码、利用噪声反馈求解Ising/Max-cut。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.eetimes.com/lightmatter-raises-400-million-series-d/）来源链接
  - [外]（出处：https://lightelligence.ai/products/photon-computing/pace2）来源链接
  - [外]（出处：https://lightelligence.ai/community/papers/9）来源链接
#### 3. 光互连派：Ayar Labs / Celestial AI 靠CPO先兑现并被产业资本整合
- **竞争逻辑**：竞争逻辑：铜互连在>800 Gbps时受限到数米且需retimer；可插拔光模块距离远但功耗/延迟高；CPO(共封装光学)把光I/O直接并入GPU/加速器，带宽与能效兼得。成败判据=聚合带宽、能效、量产可得性与产业资本背书。宣称vs可核验：Ayar的>200 Tbps/封装为公司宣称(参考设计，8颗下一代TeraPHY)，1万GPU die scale-up域为CTO目标；NVIDIA $4B投向Coherent/Lumentum、Marvell收购Celestial AI为已发生事件(多方报道金额有分歧：$3.25B已成交 vs 最高$5.5B含对价)。
- **硬数字**：Ayar Labs：2026-03完成$500M E轮(Neuberger Berman领投，NVIDIA/MediaTek参投)；Alchip参考设计用8颗TeraPHY，公司宣称每封装>200 Tbps聚合带宽(对比NVIDIA Rubin双向28.8 Tbps，约7倍)；目标10,000 GPU die scale-up域、机柜约100 kW；Ayar 2015年成立即做互连，非从计算转型。Celestial AI：2025-03 C1轮$250M、估值$2.5B；Marvell于2026-02完成收购(The Register口径约$3.25B；datadeep口径最高$5.5B，存在冲突)。CPO能效口径：约5.4 W/800G vs 2×FR4可插拔约15 W(Meta ECOC 2025/datadeep转述)。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.theregister.com/on-prem/2026/03/03/ayar-labs-raises-500m-to-mass-produce-cpo-chiplets/4889700）来源链接
  - [外]（出处：https://datadeep.tech/photonic-neural-networks/）来源链接
  - [外]（出处：https://siliconangle.com/2025/03/11/celestial-ai-raises-250m-optical-interconnect-technology）来源链接
#### 4. 相干光计算 vs 强度(非相干)光计算 / 自由空间 vs 波导集成：精度与规模口径之争
- **竞争逻辑**：竞争逻辑：相干(MZI干涉网格，光场幅相)精度高但相位噪声/热漂移敏感、难大规模；非相干WDM广播-权重强度方案抗噪、易调矩阵、利于商用部署；自由空间(衍射/超表面)靠传播零能耗但难重构、集成度低；波导集成可量产但受 Thermal 串扰与ENOB上限约束。成败判据=有效精度(ENOB)、面积/能效口径是否含激光与电子外围、规模化是否与量产工艺兼容。宣称vs可核验：曦智明确选择非相干架构(精度控制/调矩阵灵活/抗噪利商用)，源于创始人2017相干开创论文后的工程路线调整；Taichi用『干涉-衍射混合』波导方案；LightGen自由空间全光则是团队宣称，需按理论/实测区分。
- **硬数字**：曦智PACE(Nature 2025)：非相干、4.21/2.38 TOPS/W(不含/含激光)、7.61 ENOB@25 MHz、±5°C掉约1 bit。清华Taichi(Science 2024-04-12, DOI 10.1126/science.adl1203)：干涉-衍射混合、64×64输入输出维度、160 TOPS/W片上能效口径、879 T MACS/mm²面积效率、片上网络达约10^10光神经元、1623类Omniglot分类91.89%、100类mini-ImageNet 87.74%(口径：清华官方新闻，能效为片上、是否含激光未在该页标明)。热漂移硬约束口径：硅热光系数约1.8×10^-4 /K→80–100 pm/K谐振漂移(二手datadeep)。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.nature.com/articles/s41586-025-08786-6）来源链接
  - [外]（出处：https://media.au.tsinghua.edu.cn/info/1016/1231.htm）来源链接
  - [外]（出处：https://dx.doi.org/10.1126/science.adl1203）来源链接
  - [外]（出处：https://datadeep.tech/photonic-neural-networks/）来源链接
#### 5. 自由空间全光生成式原型 LightGen：宣传口径与可核验口径存在落差
- **竞争逻辑**：竞争逻辑：自由空间全光做端到端视觉生成，试图绕开电非线性与光存储，卖点是『无ground truth训练、全光维度变换』。成败判据=是否给出独立可复现的墙插能效/延迟与量产路径。宣称vs可核验：团队宣称单芯片百万光神经元、支持3D/高清视频/语义生成、质量可比Stable Diffusion/NeRF；能效『较数字芯片提升2个数量级』标为当前器件口径，『算力7个数量级、能效8个数量级』明确标为先进器件理论值——均为宣称，不能当实测。SCMP原文被Cloudflare拦截未能深读，故单源。
- **硬数字**：LightGen(Science 2025-12-18)宣称：单芯片百万光神经元；当前器件端到端时间/能效较顶级数字芯片提升2个数量级；先进器件理论算力提升7个数量级、能效提升8个数量级(理论口径，非实测)；实验任务为高分辨率图像语义生成/3D/高清视频/去噪/特征迁移。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://www.chinadaily.com.cn/a/202512/20/WS6945ede4a310d6866eb2f9ad.html）来源链接
  - [外]（出处：https://scmp.com/news/china/science/article/3336918/chinese-team-builds-optical-chip-ai-100-times-faster-nvidias-market-leader）来源链接
#### 6. 应用场景之争：组合优化(Ising/Max-cut)先于AI训练落地，训练仍电子主导
- **竞争逻辑**：竞争逻辑：光计算最擅长快速重复矩阵乘+噪声反馈，正好契合Ising/Max-cut等组合优化(可用低精度、迭代求解)，故比通用AI训练更容易出可核验优势；AI训练需高精度、反向传播、频繁权重更新与存储，仍是电子GPU主导。成败判据=收敛率/迭代次数/单周期延迟的真实对比口径，是否端到端优于GPU。宣称vs可核验：PACE在Max-cut上单周期5 ns vs NVIDIA A10 >2300 ns(作者宣称近500×单周期)，但PACE平均537次迭代 vs A10 347次，总耗时优势需按完整求解口径折算，不能只看单周期。Taichi演示的是千类分类与AIGC(音乐/绘画)，非大模型训练。
- **硬数字**：曦智PACE(Nature 2025)：20,000次测试(10批×2,000)、5 ns循环下平均收敛率>92.72%；平均537次迭代 vs NVIDIA A10平均347次；单步周期5 ns vs A10 >2300 ns。Taichi(Science 2024)：1623类Omniglot 91.89%、100类mini-ImageNet 87.74%、片上AIGC(作曲/高分辨率风格画)。训练侧：片上光反向传播仍停留在Science 2023 (Pai et al., Science 380, 398)演示级，未规模化(datadeep转述)。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.nature.com/articles/s41586-025-08786-6）来源链接
  - [外]（出处：https://media.au.tsinghua.edu.cn/info/1016/1231.htm）来源链接
  - [外]（出处：https://datadeep.tech/photonic-neural-networks/）来源链接
#### 7. 历史教训：2010s光计算泡沫退潮与2020s AI算力需求重启
- **竞争逻辑**：竞争逻辑：2010s光计算『过度承诺』(over-promise)——声称矩阵乘零能耗、快几个数量级，但制造成本/非线性/精度/封装未解，兑现失败后热度退潮；2020s大模型算力与互连功耗墙重启需求，资本与CPO产业链真正兑现的是互连而非计算。成败判据=演示是否从『关键构建块』走到『整系统量产实测』，以及承诺是否被可复现数据支撑。宣称vs可核验：MIT 2017学者自述『people dramatically over-promised, and it backfired』，当时仅验证构建块非完整系统，元音识别77% vs 电子约90%；MIT TechReview 2016指光的优势长期未抵消额外制造成本；2025年PACE成为首个在商业产线制造、给出整系统实测的Nature级成果。
- **硬数字**：MIT 2017可编程纳米光子处理器：元音识别77% vs 常规系统约90%；宣称理论能效<1/1000为愿景口径。2016年MIT TechReview：光处理优势一直未抵过额外制造成本(定性)。2024–2025重启口径：光互连派融资>Ayar $500M E轮 + Lightmatter $400M D轮 + Celestial $250M C1；datadeep称2024–2025领域风投>$2B、三笔Tier-1并购；Yole预测首批光处理器出货2027–2028、2034年约100万颗(预测非实绩)。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://news.mit.edu/2017/new-system-allows-optical-deep-learning-0612）来源链接
  - [外]（出处：https://technologyreview.com/2016/11/18/155929/silicon-photonic-neural-network-unveiled）来源链接
  - [外]（出处：https://datadeep.tech/photonic-neural-networks/）来源链接
#### 8. Luminous Computing现状：2023年光子团队裁员、退出计算类别
- **竞争逻辑**：竞争逻辑：Luminous 2022年以系统级硅光互连(而非纯光非线性)切入，主打训练规模扩大100–1000倍，但一直pre-revenue、只有原型。失败判据=长期无产品出货且团队收缩。宣称vs可核验：2022年A轮$105M、约90人、宣称24个月内发开发套件、距商用5–10年；datadeep(2026二手)称其2023-05光子团队裁员后实质退出该类别——单一二手来源，未找到公司一手或权威媒体确认关停/转向，故不写成定论。
- **硬数字**：Luminous(VentureBeat 2022-03-03)：A轮$105M、投后估值$2–3亿、累计$115M、约90人、pre-revenue；宣称训练模型规模扩大100–1000倍、带宽每距离提升10–100倍；计划24个月内出开发套件。退出说法(datadeep 2026)：2023-05光子团队裁员(单源)。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://venturebeat.com/ai/luminous-computing-which-is-developing-a-light-based-ai-accelerator-chip-raises-105m）来源链接
  - [外]（出处：https://datadeep.tech/photonic-neural-networks/）来源链接
### 新型显示与成像路线之争
#### 1. Micro LED vs OLED vs LCD：量产胜出判据是像素级良率×转移节拍×晶粒成本，而非单点画质
- **竞争逻辑**：路线对立：LCD靠成熟面板产能/低成本占主流，OLED靠自发光、无限对比度和轻薄夺高端，但有机材料对水氧/热敏感、蓝光子像素寿命短；Micro LED理论兼具高亮、高效率、长寿命与无限对比度，但必须把数千万颗微米级LED逐个转移并修复。判据是每颗die的制造良率、转移良率、检测/修复速度、贴装精度与节拍，以及总成本能否接近OLED。量产与实验室分层：Micro LED 2010年代初已商业化于小尺寸/高端，但通用电视仍未翻盘；SID/Yole 2025指出2020-2023后质量进入平台期、Apple取消10年约30亿美元智能手表Micro LED项目；当前>20台转移设备/15+厂商仅适合中试和首批产品，Fluidic self-assembly仍在研究阶段。LCD早期以更低功耗/重量在2000年代初取代CRT，LC响应5-25ms（overdrive ~1ms）；OLED完美黑但蓝色EQE<25%、1000 nits下寿命<500 h、亮度约10^3 nits制约AR；Micro LED小die效率下降推高功耗，15×30/20×40 µm尺寸已平台化。
- **硬数字**：口径需区分：①像素数口径：4K >2400万子像素、8K约1亿子像素；即使良率99.99999%，4K屏仍约2颗坏LED（MicroLED Association白皮书，2023-02）。②行业目标口径：KLA称99.9999%（six nines）是经济可行且人眼可接受的显示良率。③节拍口径：8K约1亿芯片、±1 µm贴装、经济可行性要求<10-20分钟/台；现有最佳半导体键合机需约11年/台8K电视，pick-and-place需>5个数量级吞吐提升（SID 2025 Digest/Yole）。④成本口径：原型450-2000 µm² die是成本死路，消费级需接近/低于100 µm²；成本高出OLED约3-4倍（手表）到>10倍（电视）；microLED芯片占显示成本>50%（Insight Media 2025面板/芯片厂圆桌）。⑤改善口径：die成本规模化约降5倍、缩小尺寸可降>…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://sid.org/Portals/sid/Files/SID-Digest/docs/59-3.pdf）来源链接
  - [外]（出处：https://microledassociation.com/wp-content/uploads/2023/02/MicroLED-yields-2023-02.pdf）来源链接
  - [外]（出处：https://electronicdesign.com/technologies/industrial/displays/article/21273604/kla-corp-microled-displays-how-to-achieve-a-999999-yield）来源链接
  - [外]（出处：https://insightmedia.info/microled-market-is-developing-but-challenges-remain）来源链接
  - [外]（出处：https://www.nature.com/articles/s41377-025-02027-1）来源链接
#### 2. AR/VR近眼路线：Birdbath/自由曲面 vs 光波导（几何/衍射/全息）——赢在形态，卡在光效与制造
- **竞争逻辑**：路线对立：birdbath和自由曲面属于几何/自由空间组合器，靠分束镜+曲面半反镜或自由曲面棱镜折叠光路，效率高、色彩/FOV好、成本中等，但厚度和重量随eye box/FOV增长；光波导靠入耦-全反射扩瞳-出耦把 projector 做进几毫米镜片，得到眼镜形态和大eye box，成为轻量AR智能眼镜主流，但每次耦入/耦出都有衍射/吸收损耗、波长/角度选择性带来彩虹纹与均匀性问题，且纳米结构制造难、成本高。pancake用偏振折叠把长光路压薄、主导紧凑VR/MR，但偏振折叠丢弃大部分光，不适合透明AR。判据：光效(nit/lm)、真实世界透过率、FOV、eye box、厚度、可制造性/良率和成本；产品定位决定胜者而非绝对画质排名。
- **硬数字**：同行评审综述口径：几何组合器约4200 nit/lm（汇总表约4000），衍射波导典型50-200 nit/lm；几何组合器FOV 50-120°、eye box约8 mm，衍射波导FOV约50°、eye box约15 mm（Xiong et al. 2021, doi 10.1038/s41377-021-00658-8；经VRARWiki条目整理）。工程估算口径：理想50/50 birdbath 48%×48%≈23%光效，80/20分束≈14%；消费透视birdbath实际约10-15%显示光到眼，真实世界透过率≤25-30%；若调到81%透视，显示光仅约0.3%。尺寸口径：Nreal Light birdbath约25 mm厚（分束镜约18 mm），waveguide仅几毫米；Xreal One Pro以11 mm平面棱镜宣传比传统birdbath薄40.9%、FOV 57°、70…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://vrarwiki.com/wiki/Birdbath_optics）来源链接
  - [外]（出处：https://paloaltooptics.com/blog/waveguide-vs-birdbath-vs-pancake-near-eye-architectures）来源链接
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC11021499/）来源链接
  - [外]（出处：https://www.nature.com/articles/s41377-021-00658-8）来源链接
#### 3. 衍射光波导内部：SRG vs VHG vs PVG——效率/均匀性/色彩/可量产性的三角取舍
- **竞争逻辑**：SRG（表面浮雕光栅）用电子束/刻蚀/纳米压印形成周期结构，工艺成熟（HoloLens 2采用），但波导内的角度/波长选择性导致色散、彩虹纹、高阶漏光；VHG/体积全息光栅用光聚合物干涉曝光形成体折射率调制，研发成本低、生产快，透射式HOE会把真实世界光误衍射形成鬼影，反射式可避免；PVG（偏振体光栅）靠液晶各向异性周期变化，对偏振态选择性衍射，理论衍射效率接近100%，适合与偏振LCoS光机配合，但若光源是非偏振microLED，单片PVG优势会缩水。判据是入耦效率、全FOV最小效率、均匀性、色彩均匀性、鬼影/漏光、工艺窗口与大面积复制能力。
- **硬数字**：实验室设计口径（Nature Light Sci Appl 2024, doi 10.1038/s41377-024-01537-8）：10 mm高折玻璃蓝波段透过~95%，1 mm波导等效传播50 mm后蓝光吸收~23%；SRG全彩波导在Photonics West 2024展示20° FOV 4500 nits/lm（~10%）、30° FOV 1300 nits/lm（~3%）。70°对角FOV、n=2单色：极端角入耦损失>70%、FOV均匀性下降70%；全彩30° FOV：蓝/红入耦损失>73%/>51.5%、色彩均匀性下降~45%。50° FOV（30°H×40°V）PVG设计：W=3 mm、f=5.598 mm、t=0.55 mm、n=1.7、Λx≈407 nm；传统入耦理论下限~36%，一阶半波PVG（倾斜23°、厚0.7 µm）平均衍射效率~80%、最小入耦61.3%（1.…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://doi.org/10.1038/s41377-024-01537-8）来源链接
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC11021499/）来源链接
  - [外]（出处：https://link.springer.com/article/10.1186/s43593-023-00057-z）来源链接
#### 4. 图像传感器：CMOS vs CCD——集成度/功耗/成本压倒纯画质优势；BSI/堆叠式继续放大优势
- **竞争逻辑**：CCD以高画质电荷转移读出长期占据高端，但需多路时钟、外围驱动与较高功耗；CMOS把放大器/ADC/逻辑集成到标准CMOS工艺，元件更少、功耗更低、制造更便宜、数据吞吐更快。胜出判据从“单像素画质”转为“系统成本×功耗×速度×可集成度”；BSI把感光层置于电路背面，缓解FSI噪声与低照度劣势；堆叠式把像素与逻辑分层，进一步提速降功耗。量子点/有机传感器属于新路线但量产判据未覆盖。
- **硬数字**：iSuppli/Electronics Weekly口径：2010年全球出货17亿颗图像传感器，CCD份额9.8%（2009年11.4%），预测2014年仅4.7%；CMOS 2010年90.2%（2009年88.6%），卡片机CMOS渗透率2009年14%→2011年24%，2014年99% DSLR机型用CMOS。IHS/EDN口径：2011年CMOS占面积传感器92%≈21亿颗（2010年16亿、+31%）；CCD 8%=1.803亿颗（-2%）；预测2015年CMOS 36亿颗/97%、CCD 9520万/3%；手机占CMOS出货79%。BSI口径：2011年BSI成本比FSI约高20%，预计2012年在智能手机/高端功能机渗透56%、2015年92%；Sony 2012宣布堆叠式BSI样品3月起出货。量产分层：CMOS自2010年代初已主导量产；BSI/堆叠式进入手机主流量产；C…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://electronicsweekly.com/business/bye-bye-ccd-2010-10/）来源链接
  - [外]（出处：https://edn.com/cmos-image-sensors-continue-march-to-dominance-over-ccds/）来源链接
#### 5. 红外探测：制冷型InSb/HgCdTe vs 非制冷微测辐射热计——成本/SWaP/即开即用判定主流，性能高端留给定制冷
- **竞争逻辑**：制冷型是光子探测器，InSb/HgCdTe（以及QWIP/T2SL）需77–200 K低温抑制热噪声，NETD更低、响应微秒级、可覆盖MWIR并做远距离/高温目标识别，但杜瓦+斯特林制冷机带来重量、功耗、开机等待、成本和寿命短板。非制冷微测辐射热计（VOx/a-Si）用吸收膜温升引起电阻变化，室温工作、MEMS/晶圆级封装可规模化，成本/SWaP/MTTF占优，但热时间常数毫秒级、NETD较差。判据是NETD、响应/帧率、波段和目标温度、探测距离、SWaP、成本与MTBF；<3 km人体/常温目标偏非制冷，>5 km/高温目标/激光指示偏制冷。
- **硬数字**：厂商一手对比口径（SensorMicro/IRmodules，需按厂商来源理解）：制冷NETD <10–15或<20 mK vs 非制冷30–80/30–60 mK（高端<20 mK）；响应1–10 µs vs 8–15 ms，热时间常数8–12 ms、慢约10,000倍；制冷1–14 µm/3–5 µm、人体探测5–20 km，非制冷7.5–14 µm、1–4 km；同一口径下20 mK制冷比50 mK非制冷在同口径延长探测距离30–40%。SWaP口径：非制冷400×300 FPA <50 g/<1 W或模块50–150 g/1.5–3 W；制冷杜瓦+制冷机500–2000 g/5–20 W、降温5–15分钟。成本口径：制冷$10,000–$100,000+，非制冷$500–$5,000（1/5–1/20），制冷模块成本5–30倍，制冷机占成本30–50%、MTBF 5000–2000…
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://infraredcore.com/cases/cooled-vs-uncooled-infrared-detectors-principles-performance-and-cost-comparison-56968.html）来源链接
  - [外]（出处：https://www.irmodules.com/information/knowledge/cooled-mwir-vs-uncooled-lwir-a-buyer-s-guide-for-system-integrators/）来源链接
  - [外]（出处：https://www.mordorintelligence.com/industry-reports/uncooled-infrared-imaging-market）来源链接
#### 6. 被淘汰路线复盘：PDP vs LCD——尺寸/价格/功耗/产能的规模化判据
- **竞争逻辑**：PDP在40英寸以上曾凭宽视角、快响应和大屏定价占优；LCD借助更低功耗、更轻薄、更小尺寸覆盖能力、持续降价的面板产能和3D/4K时代生态扩张，从CRT替代战起就占据主流。胜负判据不是单项画质，而是单位英寸成本、功耗、产线规模、消费者尺寸迁移速度与供应链投资。PDP曾在2008-2009 Pioneer退出后短暂复苏，因此“2010年已死”是错误叙述；真正的退出是Panasonic 2013年宣布停产等离子面板。
- **硬数字**：DisplaySearch/CNET口径：Q4 2010全球PDP面板出货同比+9%至创纪录520万片；2010全年1910万片，2008年1510万片、2009年1480万片；Panasonic 2010份额40.7%（2009年43.1%）、出货量+22%、收入+4%，Samsung SDI份额33.7%、出货+37%、收入+15%，LG份额23.3%。Reuters/NBC口径（2010-04-19）：2009年全球电视约2.10亿台，LCD约70%、CRT<25%、PDP仅7%；42英寸LCD面板价格两年下降约40%，PDP在40英寸以上仍有价格/视角/响应优势。TWICE搜索摘要：Panasonic 2013-11确认12月结束等离子面板生产（正文被Cloudflare拦截，单源）。DLP vs 3LCD并未出现一方淘汰：ViewSonic/TI口径显示DLP（1987）和3LC…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.cnet.com/home/smart-home/study-plasma-tv-panel-shipments-hit-record-high/）来源链接
  - [外]（出处：https://www.nbcnews.com/id/wbna36645703）来源链接
  - [外]（出处：https://www.twice.com/news/industry-reacts-panasonics-plasma-exit-49364）来源链接
  - [外]（出处：https://viewsonic.com/library/tech/dlp-vs-3lcd-projector-which-one-is-better/）来源链接
#### 7. 量子点/有机图像传感器未覆盖：检索两轮到顶，未拿到可核验的量产良率/暗电流/成本数字
- **竞争逻辑**：原计划比较量子点（胶体QD）与有机光电二极管/ organic sensor 相对硅CMOS的带隙可调、弱光/色彩滤波集成优势，以及暗电流、稳定性、读出集成和量产判据。实际检索命中Nature Photonics《photodetector evaluation guidelines》与2025微显示综述，但两次WebFetch均30秒超时；按方法纪律不第三次重试、不臆造数字。
- **硬数字**：未覆盖：无可核验的量子点/有机传感器量产线良率、暗电流、EQE、响应度-带宽积、封装寿命或成本数字。仅作开放问题保留，不把实验室EQE当作量产判据。
- **状态**：未覆盖
- **出处**：
  - [外]（出处：https://www.nature.com/articles/s41566-025-01759-1）来源链接
  - [外]（出处：https://www.nature.com/articles/s44287-025-00199-x）来源链接
#### 8. QWIP/II类超晶格红外路线未覆盖：未拿到与MCT/InSb可比的量产良率与成本-性能数字
- **竞争逻辑**：原计划比较QWIP与Type-II superlattice相对HgCdTe/InSb在均匀性、暗电流、工作温度和晶圆成本上的取舍；现有红外资料只确认InSb/MCT/T2SL/QWIP均属制冷光子探测路线，未给出T2SL/QWIP的独立判据数字。
- **硬数字**：未覆盖：无T2SL/QWIP晶圆良率、_ARRAY均匀性、NETD@工作温度、暗电流或单位成本的可核验数字；仅能引用制冷vs非制冷的共性区间，不能用它替代路线内部比较。
- **状态**：未覆盖
- **出处**：
  - [外]（出处：https://teledynevisionsolutions.com/learn/learning-center/scientific-imaging/infrared-detector-sensor-materials）来源链接
  - [外]（出处：https://www.infraredcore.com/cases/cooled-vs-uncooled-infrared-detectors-principles-performance-and-cost-comparison-56968.html）来源链接
#### 9. 早期LCoS失败判据未覆盖：Springer章节被客户端挑战拦截，未获得可核验的良率/成本/量产数据
- **竞争逻辑**：原计划比较LCoS与DLP/LCD在反射式光阀、像素间隙、偏振光效、黑白响应和微显示量产上的竞争；现有材料只显示LCoS仍用于部分光机（如Google Glass与AR光机方案），不足以提炼“早期淘汰”判据。
- **硬数字**：未覆盖：无可核验的早期LCoS面板良率、开口率、响应时间、光效或成本数据；Springer条目返回Client Challenge，MDPI相关页面Access Denied，Nature微显示综述两次超时。
- **状态**：未覆盖
- **出处**：
  - [外]（出处：https://link.springer.com/article/10.1007/978-3-319-14346-0_126）来源链接
  - [外]（出处：https://www.mdpi.com/2813-446x/3/4/25）来源链接
  - [外]（出处：https://vrarwiki.com/wiki/Birdbath_optics）来源链接
### 激光与光源路线之争
#### 1. 半导体激光器材料体系：InP vs GaAs vs GaN 的波长归属
- **竞争逻辑**：胜负判据=带隙决定的发光波长与衬底外延质量的可得性。GaAs/AlGaAs 晶格匹配好、折射率差大、氧化孔径(oxide aperture)技术成熟，红→近红外(约650–980nm)易做，VCSEL 垂直腔需要高反射率 DBR 与可靠电流/光限制，GaAs 全部占优；但把发射波长拉到 1310/1550nm 极难。1.55μm 传统体系是 InP–InGaAsP，其在 VCSEL 上的死穴：折射率对比度低、热导率低、价带间吸收(intervalence band absorption)大、俄歇复合(Auger)强，且没有类似 GaAs 氧化的 Robust 孔径工艺。蓝光则靠 GaN/InGaN 宽禁带(约3.4eV)直接覆盖 450nm 附近，Nakamura 用 p 型 GaN 解决掺杂与异质外延后，蓝光 LD 才量产并催生光盘/固态照明。结论：不是材料"最优"，而是"波长窗口×外延/腔工艺成熟度"的绑定胜出——电信长波长归 InP，短距高速 VCSEL 归 GaAs，蓝光/绿光归 GaN。
- **硬数字**：GaN 禁带≈3.4eV（IOP Conf. Ser. 2426 012008 摘要片段，宽禁带口径）；Nakamura 蓝光 InGaN LD 波长≈450nm（Appl. Phys. Lett./J. Appl. Phys., doi 10.1063/1.125643，Nichia 2000，实验室首颗量产级蓝光 LD 口径）；IEEE JSTQE 2001 (doi 10.1109/2944.954127) 明确 1.55μm VCSEL 的四大限制：低折射率对比、低热导、高价带间吸收、高俄歇复合；OFC2015 Tu2H.1 长波长 VCSEL 40Gbps 传输 1km（单模通信口径，说明 InP 长波 VCSEL 仍未取代 InP 边发射）；GaAs VCSEL 覆盖红→近红外、"very challenging to stretch emission to 1310/1550…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://doi.org/10.1109/2944.954127）来源链接
  - [外]（出处：https://doi.org/10.1109/2944.788414）来源链接
  - [外]（出处：https://doi.org/10.1063/1.125643）来源链接
  - [外]（出处：https://doi.org/10.1002/andp.201500801）来源链接
  - [外]（出处：https://iopscience.iop.org/article/10.1088/1742-6596/2426/1/012008/pdf）来源链接
#### 2. 硅基光源路线之争：异质集成 III-V vs 键合 vs 外延直接生长 vs 拉曼激光
- **竞争逻辑**：判据=理想片上光源四条硬指标：①1310/1550nm 发光 ②电泵浦 ③高功率效率 ④CMOS 兼容制造。逐条淘汰：多孔硅/硅纳米晶波长不对且发光效率超低；Si 拉曼激光本质是光泵浦非线性，需外部泵浦源、不能电注入、系统效率极低；掺 Er 硅光泵下最高 Er 浓度 1.6e22 cm^-3、寿命 540μs、光泵增益>100dB/cm，但电激发 Er3+ 比例≤20%、效率仅 10^-2%，从未做出电泵浦 Er 激光器，无电泵净增益；Ge-on-Si 靠应变/重掺杂把 Γ-L 谷差 136meV 补上(0.25% 张应变+n 掺杂 7.6e19 cm^-3，δ 掺杂>4e19 cm^-3 才有增益)，却带来高自由载流子吸收与-room 温度可靠性问题。胜出路线：III-V 材料通过晶圆键合(heterogeneous integration/bonding)混合集成到硅上，四条里唯一同时满足电泵浦+1550nm+高功率+与 CMOS 后段兼容，故"近期商业化最佳"。长期看选择性/单片外延 III-V-on-Si(尤其 QD 量子点，对温度不敏感、缺陷容忍)以降成本提良率。AOP202…
- **硬数字**：电泵 Er 激光"从未实现"；Er3+ 电激发≤20%、效率≈10^-2%；Er 硅光泵增益>100dB/cm、Er 浓度 1.6e22 cm^-3、寿命 540μs（Nature LSA 2015 vol4 e358 综述口径）；Ge-on-Si Γ-L=136meV、0.25% 张应变+7.6e19 cm^-3 n 掺杂→直接带隙、δ 掺杂>4e19 cm^-3（同综述，材料物理口径）；键合 III-V 被明确判为"best performance and best opportunity for commercial usage in near future"（结论口径）；300mm 硅上 QD 激光器(s41377-022-00982-7)、SOI 单片嵌入 III-V(s41377-023-01128-z)、InP-on-Si 1.55μm CW(s41377-024-01389…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://nature.com/articles/lsa2015131）来源链接
  - [外]（出处：https://doi.org/10.1364/AOP.455976）来源链接
  - [外]（出处：https://opg.optica.org/aop/abstract.cfm?uri=aop-14-3-404）来源链接
  - [外]（出处：https://www.nature.com/articles/s41377-022-00982-7）来源链接
  - [外]（出处：https://www.nature.com/articles/s41377-023-01128-z）来源链接
  - [外]（出处：https://www.nature.com/articles/s41377-024-01389-2）来源链接
#### 3. 光纤激光器 vs 固体激光器 vs 半导体激光器：工业加工/通信/医疗归属
- **竞争逻辑**：判据=功率-光束质量(M²)-电光效率-寿命-总拥有成本(TCO)五维。光纤激光器全光纤结构取消自由空间腔/镜片/气体，1.07μm 波长对钢吸收率远高于 CO2 的 10.6μm，配合 50%+ 电光效率与>10万小时寿命，5 年 TCO 最低——在高功率金属切割/焊接上把 CO2(气体、镜片、20k 小时寿命)和 Nd:YAG(灯泵 3-5% 效率、M²10-25、500-1k 小时)挤出主流。半导体激光器本身不做高功率束加工主光源，但凭体积/效率/调制速度独占泵浦源与光通信/医疗(皮肤、牙科)低功率段。死穴：单模光纤功率>SRS/SBS 阈值，>10kW 需多模(M²2-6)，牺牲光束质量换功率。历史判据：2000 年千瓦级光纤激光改变金属加工，2013 年 IPG 8 亿美元营收标志光纤替代 CO2。
- **硬数字**：波长 1.07 / 10.6 / 1.064μm；电光效率 50-55% / 10-15% / 3-5%；M² <1.1(单模) / 1.1-1.3 / 10-25；CW 功率 1W-120kW / 10W-20kW / 10W-6kW；钢吸收率 35-40%@1.07μm vs 5-10%@10.6μm；寿命 >100,000h / ~20,000h / 500-1,000h；6kW 设备成本 $80-150k / $50-100k / $30-70k；5 年 TCO 光纤最低（IPG Photonics 官网技术对比页，厂商一手，2024 datasheet 口径）。IPG YLS-SM 单模最高 10kW、M²1.1/1.15/1.2<2.0（datasheet 口径）。>10kW 多模 M²2-6（SRS/SBS 限制口径）。2013 年光纤激光营收≈$800M（产业口径）。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://ipgphotonicsus.com/technology.html）来源链接
  - [外]（出处：https://cdn.ipgphotonics.com/3694f393-6e4c-49e4-9374-b1400126ebba/IPG_YLS-SM-Series_DS_EN_LTR.pdf）来源链接
#### 4. 超快激光器路线：钛宝石 vs 光纤 vs SESAM 可饱和吸收
- **竞争逻辑**：判据=工业化要"simplicity/maintenance/reliability"(简单/免维护/可靠)。传统钛宝石固体超快激光依赖自由空间腔、精密对准、昂贵泵浦，2004 年 IEEE 已判定其无法满足工业级简洁性/维护/可靠性；SESAM(低损耗、快速腔内半导体可饱和吸收体)让被动锁模在数百 kHz 重频下稳定自启动、参数可按需设计，把超快激光从科研推向工程。掺稀土(ER/Yb)多组分玻璃光纤提高增益系数，光纤超快凭高光束质量、可靠性、散热效率与紧凑体积，在加工/生物医学工业化场景胜出；钛宝石退守需要超短脉宽/高峰值功率的实验室与科学装置。注意：SESAM 本身是锁模机制而非与光纤对立的整体路线——二者结合(fiber+SESAM)才是工业化主流。
- **硬数字**：SESAM 使稳定被动锁模重频达数百 kHz(100s kHz)、吸收体参数可设计（IEEE 9484726, 2021 USP for Microfabrication review 摘要口径）；掺稀土多组分玻璃光纤提升增益系数、光纤激光高光束质量/可靠/散热好/紧凑（PubMed 29716015, 2018 摘要口径）；传统固体超快"不能"满足 simplicity/maintenance/reliability（IEEE 1308612, 2004 摘要口径）。注意：三篇均为摘要级证据，正文付费墙；optics.org 相关综述文章已 404。硬数字(脉宽 fs 级、平均功率 W 级)未从一手正文取到，标单源未验证。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://ieeexplore.ieee.org/document/9484726）来源链接
  - [外]（出处：https://pubmed.ncbi.nlm.nih.gov/29716015/）来源链接
  - [外]（出处：https://ieeexplore.ieee.org/document/1308612）来源链接
#### 5. 窄线宽光源路线：外腔半导体 ECL vs 光纤激光 vs 硅光集成（2026）
- **竞争逻辑**：判据=洛伦兹线宽×无跳模调谐范围×输出功率×集成度/体积×温漂，且不同应用匹配不同路线。2026 年 Nature LSA 的谐振器增强 DBR(RE-DBR)把高 Q 外腔与 DBR 结合：用 finesse F 把常规 DBR 的线宽-调谐权衡 Δν/Δν0>4(n_ga·L_a/(n_g·η0)·η)^2 改写为 (π²/F²)(...)²，当 F>π/2 时同时拿到 Hz 级线宽与大范围无跳模调谐，且单片<4mm²。与注入锁定(SIL)相比，SIL 虽可 Hz 级、Q 达百万级(6.19M)，但需要精确注入电流设定点、线宽∝R^-1，RE-DBR 依赖 (lnR)^2 更宽容、免外部伺服。光纤激光/光纤外腔窄线宽仍在长相干长度(干涉/传感)与高功率段占优；硅光外腔 ECDL(arxiv 2601.18609 硅条形波导外反馈)与亚 Hz 硅芯片(Q=3.46e9, arxiv 2610.22596)证明集成化路线逼近甚至达到亚 Hz，但实验室成熟度与温漂/封装仍未达量产。结论：2026 年"窄线宽+可调+小尺寸"由 RE-DBR/集成外腔拿下；"极限线宽+稳干长度"仍属光纤与超…
- **硬数字**：RE-DBR：24 Hz 洛伦兹线宽(白噪声基底 3.89 Hz²/Hz)；34 GHz 无跳模调谐(=33×纵模间隔 FSR 1.02GHz)；片上输出 22mW@174mA；SMSR 60dB；加载 Q≈0.56×10^6；finesse 90.7；尺寸<4mm²；>100mA 电流扫频免调；15–50°C 温漂<0.5nm（Nature LSA 2026 vol15 art142，实验室样片口径）。SIL 对比：加载 Q≈6.19×10^6 却线宽更宽、需精确电流设定点（同文对比口径）。Jin 等 Nat. Photonics 15, 346 (2021) Hz 线宽 CMOS 兼容超高 Q 微腔；Pockels 激光 Nat. Photonics 19, 709 (2025)；硅光亚 Hz 本征线宽 Q=3.46×10^9(arxiv 2610.22596, 2026-11, 实验…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://nature.com/articles/s41377-026-02249-x）来源链接
  - [外]（出处：https://www.nature.com/articles/s41377-026-02249-x）来源链接
  - [外]（出处：https://arxiv.org/abs/2610.22596）来源链接
  - [外]（出处：https://arxiv.org/abs/2601.18609）来源链接
#### 6. 淘汰路线复盘：染料激光器退场与气体激光器(He-Ne/CO2)份额萎缩
- **竞争逻辑**：判据=替代的净收益：当固体激光(钛宝石等)拿到同等波长覆盖而不必处理有毒染料溶液、寿命长、输出功率高时，染料激光被"替代逻辑"挤出——其曾长期垄断可调谐/超短脉冲，仅因特定光谱波段仍留在光谱学。气体激光(He-Ne/CO2/准分子/He-Cd)的萎缩来自：需气体/放电管、镜片/腔维护、效率低、寿命有限，而在工业加工被光纤激光(50%+效率、10万小时、免维护)替代，在低功率对准/计量被半导体激光二极管替代。反向证据：2002 年 OPN 仍列 CO2/准分子/He-Ne/He-Cd 在工业/科研/医疗在用，二极管芯片才是"最活跃角色"——说明这是份额转移而非物理淘汰，气体在特定波段/功率仍有存量。判据提炼：①毒性与运维成本 ②效率/寿命 ③光束质量与功率 ④是否被免维护固态方案覆盖。
- **硬数字**：染料激光：上能级寿命仅数 ns、增益≈10^3/cm、功率效率数%–~50%、平均输出 10mW–1W(脉冲峰值>1kW 可行)、调谐范围数十 nm（SPIE Field Guide to Lasers, Paschotta 2008, 典型值口径）；染料"largely replaced by solid-state (often Ti:sapphire)"因有毒溶液/有限寿命/有限输出（同书口径）；NASA 2003 年染料激光 532nm 泵浦→紫外 30mJ/脉冲（历史应用口径）；二极管激光被称 playing the liveliest role，而 CO2/excimer/He-Ne/He-Cd 仍用于工业/科研/医疗（Optics & Photonics News 13(5) 24-27, 2002, doi 10.1364/OPN.13.5.000024，摘要口径）。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://spie.org/publications/fg12_p79-80_dye_lasers）来源链接
  - [外]（出处：https://doi.org/10.1364/OPN.13.5.000024）来源链接
### 光伏电池路线之争
#### 1. 晶硅 vs CdTe/CIGS/非晶硅：成本、效率与产业链的路线筛选
- **竞争逻辑**：胜负判据不是单结极限效率，而是同一场址、同一电价与可靠性约束下的度电成本（LCOE）= 初始投资÷全寿命发电量 + O&M/融资等，并受供应链规模、设备折旧、良率、银行可融资性与政策本地化约束。晶硅凭可共享的半导体级硅料—硅片—电池—组件生态、快速学习曲线、成熟设备与大规模制造取得系统成本优势；CdTe/CIGS/非晶硅虽省硅料、可低温沉积，但产业规模、设备生态和客户认证较小。CdTe没有在通用市场翻盘，而是凭连续大面积镀膜、低材料用量、良好高温/光谱响应、低衰减及美国本地制造，守住炎热、高直射辐照的大型地面电站。First Solar Series 7的商业口径明确显示：组件最高19.7%，但核心卖点是30年线性质保、年衰减0.3%、温度/光谱/遮阴响应、安装BOS与美国本土制造；因此其活命逻辑是系统成本与政策市场适配，而不是效率超过晶硅。判据应表述为：在相同场址DNI/GHI、温度、追踪器与电价结构下，谁把组件价差转化为更低LCOE，并满足25–30年可融资寿命。
- **硬数字**：OECD 2022供应链报告：晶硅组件占全球产量>95%，CdTe占余下主要部分（产量口径，非2026市占率）；GMInsights估计2025晶硅占组件市场收入90.5%（收入口径，商业市调，非出货量）。First Solar Series 7 TR1：525–550 W、最高19.7%组件效率、30年线性质保、0.3%/年质保衰减（厂商产品口径，非实验室电池纪录）。NLR/DOE 2026 CdTe Core报告：23.1%为认证CdTe电池纪录，并明确CdTe当前是成本领先的薄膜技术、可与规模化硅直接竞争（实验室小电池认证口径，不能等同于量产组件效率）；报告亦指出CdTe主要损失来自低光电压与填充因子，平均光电压提升>100 mV。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://oecd.org/content/dam/oecd/en/publications/reports/2022/08/special-report-on-solar-pv-global-supply-chains_f884fe79/9e8b0121-en.pdf）来源链接
  - [外]（出处：https://gminsights.com/industry-analysis/solar-pv-module-market）来源链接
  - [外]（出处：https://firstsolar.com/Products/Series-7）来源链接
  - [外]（出处：https://osti.gov/biblio/3025381）来源链接
  - [外]（出处：https://cell.com/joule/fulltext/S2542-4351(25)00416-7）来源链接
#### 2. PERC vs TOPCon vs HJT vs BC：效率溢价能否覆盖改线成本
- **竞争逻辑**：PERC是存量基准，成本最低但提效空间趋窄；TOPCon以隧穿氧化层+掺杂多晶硅钝化接触，在效率、成本、设备兼容与量产良率间取得当前最佳折中，因而成为主流；HJT用非晶硅异质结和本征薄层获得高钝化、低温度系数与双面友好，但低温工艺、靶材/银浆与设备投资构成成本门槛；BC把正负电极全部移到背面，消除正面栅线遮阴，可叠加在TOPCon或HJT上（TBC/HBC/HTBC），获得更高效率，却增加双极性图形化、激光/对准、背面钝化与良率复杂度。因此路线胜负判据是每瓦有效成本：银耗/铜耗、设备改造CAPEX、良率与碎片率、双面率、高温衰减、可追溯质保，以及屋顶等高溢价市场能否消化BC溢价。当前不是BC一次性取代TOPCon，而是TOPCon继续主导、BC从存量TOPCon线升级并共存。
- **硬数字**：ITRPV 17版（TaiyangNews 2026-09转述）：2025晶硅电池生产中TOPCon约75%、PERC约14%、HJT约5%；这是2025实际产量结构，不能写成2026产能份额。TBC约5%→2036约23%，HBC约0.1%→2036约5%（预测产量份额）。2026量产组件效率预测：TOPCon 23.9%、HJT 23.9%、BC 24.3%；2036分别25.2%、25.3%、25.6%（ITRPV预测口径）。InfoLink/pv magazine 2025-07：xBC产能2025年底预计>80 GW，出货2023约7 GW→2024约23 GW→2025预计35–40 GW（行业预测）；主流TBC电池成本仍比TOPCon高约CNY0.07/W，采用钢网与复合 ribbon 后可缩小至税前电池+组件高CNY0.03/W，而TBC组件溢价约CNY0.05–0.07/…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://taiyangnews.info/technology/itrpv-expects-topcon-to-lead-as-bc-and-tandem-technologies-expand）来源链接
  - [外]（出处：https://jrsttechnology.com/knowledge/back-contact-bc-solar-cells-india）来源链接
  - [外]（出处：https://pv-magazine-india.com/2025/07/07/bringing-back-contact-to-the-foreground）来源链接
  - [外]（出处：https://infolink-group.com/energy-article/solar-topic-solar-back-contact-technology-industry-progress-outlook--xbc）来源链接
#### 3. 单结钙钛矿 vs 钙钛矿-硅叠层：效率上限与可运营寿命的竞赛
- **竞争逻辑**：单结钙钛矿材料可调、带隙可匹配，低成本溶液/蒸发沉积潜力大，适合室内光伏、柔性与特定BIPV；但单结理论效率低于叠层，且户外组件寿命、铅密封、均匀性和耐候仍是门槛。钙钛矿-硅叠层让宽带隙钙钛矿吸收蓝绿光、硅吸收红光，突破单结硅的Shockley–Queisser限制，是最有望规模翻盘的下一代路线；其死穴不是再提高小电池纪录，而是宽带隙钙钛矿在光/热/湿下的卤化物相分离、离子迁移与界面反应，铅离子的长期泄漏风险，以及平方米级薄膜的成分/厚度均匀性、针孔、良率和封装热管理。胜负判据是：在≥1 m²组件、标准IEC 61215/61730及现场25–30年等效发电条件下，稳定效率、铅浸出、湿热/紫外/热循环通过率、可量产良率和每瓦LCOE同时成立。实验室冠军效率只能证明物理上限，不能证明产业胜负。
- **硬数字**：Solar Cell Efficiency Tables v67（2026-01）与2025–26综述：单结钙钛矿已超过27%、钙钛矿/硅叠层超过34%（实验室认证/公开纪录口径，面积与认证细节须回到效率表，不可与量产组件混用）。2026年综述《Key Challenges for Commercializing Perovskite–Silicon Tandem Solar Cells》称认证PCE接近约35%，但正文被付费墙阻挡，仅检索摘要级证据，故本项稳定性量化进展标单源未验证。稳定性研究显示相分离由宽带隙混合卤化物中的PbI2晶界偏析等驱动，并提出晶界工程抑制；这些是2025–26研究进展，尚无可核验的统一25–30年户外寿命数字。未查到可信的2026量产良率、$/W与铅浸出同口径公开数据集。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://onlinelibrary.wiley.com/doi/10.1002/pip.70068）来源链接
  - [外]（出处：https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.202502696）来源链接
  - [外]（出处：https://onlinelibrary.wiley.com/doi/10.1002/cey2.70241?af=R）来源链接
  - [外]（出处：https://nature.com/articles/s41560-026-02161-z）来源链接
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC11137052/）来源链接
#### 4. 聚光光伏 CPV vs 常规平板：集中式与分布式的系统级兴衰
- **竞争逻辑**：CPV用透镜/反射镜把高DNI阳光聚到少量III-V多结电池，理论效率高、半导体用量少，看似能绕开硅片成本；但经济成立要求高直射辐照、近乎无云、精密双轴跟踪、散热与光学清洁，系统机械复杂度和运维成本高。分布式屋顶面积小、天空散射光占比高、结构载荷与维护约束强，CPV几乎没有优势；集中式地面电站在高DNI地区一度有机会。退场根因是硅组件价格和学习曲线下降太快，CPV尚未把高效率转成足够低的LCOE，领先厂商又在2015年退出，融资/质保/供应链随之收缩。判据：只能在DNI高且稳定、土地与维护条件合适的大型集中式项目中，以全系统效率、追踪器CAPEX/O&M、光学污染、清洗、失配/热点与25年可用率比较LCOE；不能拿CPV电池43%对硅组件20%作直接胜负判断。
- **硬数字**：NREL/Fraunhofer ISE 2016状态报告（optics.org转述并链接原始报告）：2012全球CPV新增约120 MW；2015新增约17 MW，而全球常规PV新增约60 GW；2015累计CPV约360 MW。2015 Soitec与Suncore退出，报告称行业陷入严重危机。Fraunhofer ISE 2016四结CPV mini-module认证/报告效率43.4%，但同期商业部署仍崩塌（实验室mini-module口径，非系统效率）。Nature Energy 2016综述明确高精度机械追踪器大型、笨重、建造维护昂贵，排除住宅市场。作为对照，CPV南非Touwsrivier电站44 MW，仅占其累计市场的重要单一项目。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://optics.org/news/7/2/35）来源链接
  - [外]（出处：https://www.ise.fraunhofer.de/en/publications/veroeffentlichungen-pdf-dateien-en/studien-und-konzeptpapiere/current-status-of-concentrator-photovoltaic-cpv-technology.pdf）来源链接
  - [外]（出处：https://nature.com/articles/nenergy201618）来源链接
  - [外]（出处：https://serdp-estcp.mil/projects/details/95ef08f7-73f3-4554-9693-0f0be9b5ce51）来源链接
#### 5. 第三代路线：热载流子、多激子、中间带与量子点谁最接近实用
- **竞争逻辑**：四者都在试图突破单结热化损失或Shockley–Queisser限制：热载流子要在载流子冷却前选择性提取并维持低熵；多激子（MEG/carrier multiplication）要把一个高能光子变成多个电子-空穴对且实际收集倍增电流；中间带要在主带隙内引入受控能带而不引入致命非辐射复合；量子点通过尺寸调带隙、强吸收和溶液加工提供平台，并可能展示MEG。当前最接近材料/器件验证与产业接口的是量子点，尤其铅卤钙钛矿量子点，因为其兼具可溶液加工、缺陷容忍和与钙钛矿工艺相近的稳定性/封装路径；但它仍不是已商业胜出的路线。其余三项最大瓶颈是：热载流子冷却时间ps量级、选择性接触与冷载流子注入难以兼顾；MEG的外量子效率>100%必须在完整器件电流中兑现而非瞬态光谱；中间带的电学占据、复合与光电流分离验证极难。最终判据是在AM1.5G标准光谱、稳定最大功率点与可重复大面积器件上实现超SQ认证效率，同时给出寿命、良率和$/W，而非仅材料级超快光谱。
- **硬数字**：2025 RSC综述《Moving beyond the Shockley–Queisser limit》把tandem、hot carrier extraction、carrier multiplication、intermediate band absorption、photon upconversion并列为突破路径（综述层级，未提供统一器件纪录）。2026量子点综述给出传统PbS/PbSe体系效率约18.1%量级，并指出钙钛矿量子点是新方向；这些数字来自综述/媒体转述，缺少同面积、同AM1.5G、同认证机构的2026横向纪录表，故不据此排名。热载流子理论需ps级提取、MEG需证明净外量子效率/电流增益、中间带需同时证明子带光电流与 Voc 增益；本项未取得四项在2026统一测试条件下的可直接比较硬数字，明确保留为研究判据而非商用排名。
- **状态**：未覆盖
- **出处**：
  - [外]（出处：https://pubs.rsc.org/en/content/articlepdf/2025/el/d5el00053j）来源链接
  - [外]（出处：https://mdpi.com/2072-666x/17/4/474）来源链接
  - [外]（出处：https://pubs.acs.org/doi/full/10.1021/acsenergylett.3c01983）来源链接
  - [外]（出处：https://europepmc.org/article/MED/42076250）来源链接
#### 6. 2000s泡沫与2010s过剩：政策、成本与技术路线如何共同筛选赢家
- **竞争逻辑**：2000年代欧洲固定上网电价创造确定性需求，硅料一度短缺、价格暴涨，资本于是涌向CdTe/CIGS/非晶硅等‘去硅化’路线，也在硅料端扩张多晶硅产能；随后金融危机、欧洲补贴退坡与硅料产能释放使价格暴跌，技术风险与财务杠杆共同出清。2010年代中国凭借规模化、垂直整合、设备国产化、低融资成本与制造学习曲线，把晶硅组件成本快速压低，PERC→TOPCon迭代进一步摊薄既有硅产业链沉没成本；高补贴/高固定电价曾短期保护高成本地区产能，但需求国削减补贴后，没有成本曲线和资产负债表优势的路线/厂商首先破产。历史结论：政策决定需求窗口与初始资本流向，成本曲线和制造生态决定谁能穿越过剩，技术迭代往往沿既有设备/供应链兼容路径发生，而不是在实验室里‘最高效者胜’。
- **硬数字**：2008年太阳能级多晶硅现货峰值约US$475/kg（pv magazine/Bernreuter历史市场回顾口径）；随后崩跌并在2010年代推动替代路线失去硅料成本理由。2011年Eurozone危机后欧洲太阳能补贴收缩，CSIS 2026报告指出2009–10中国厂商以债务快速扩产、约90%产出出口，2011需求冲击引发中国第一轮大规模洗牌（历史分析口径）。OECD 2022报告给出晶硅>95%全球产量，作为后来供应链筛选结果；ITRPV 17版给出2025全球电池产能约1.26 TW、全球组件出货约706 GW、安装约668 GW、均价约US$0.09/W（行业统计/预测口径，显示产能约为新增安装的两倍）。这些价格/份额跨年份，不构成因果效应估计。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://pv-magazine.com/2021/10/30/the-weekend-read-whats-next-for-polysilicon）来源链接
  - [外]（出处：https://bernreuter.com/files/data/newsroom/pdf-articles/magazine-reports/2024-05-pv-magazine-D%C3%A9j%C3%A0-vu-on-the-polysilicon-market.pdf）来源链接
  - [外]（出处：https://bloomberg.com/news/articles/2011-11-10/solar-costs-drop-so-suddenly-it-hurts-）来源链接
  - [外]（出处：https://csis-website-prod.s3.amazonaws.com/s3fs-public/2026-03/260312_Davidson_China_Solar_0.pdf）来源链接
  - [外]（出处：https://oecd.org/content/dam/oecd/en/publications/reports/2022/08/special-report-on-solar-pv-global-supply-chains_f884fe79/9e8b0121-en.pdf）来源链接
  - [外]（出处：https://thebatterymagazine.com/future-of-solar-module-topcon-hjt-and-perovskite）来源链接
### 光电传感与测量路线之争
#### 1. 车载LiDAR扫描架构：机械旋转 vs 半固态(MEMS/转镜) vs 纯固态(OPA/Flash/VCSEL)
- **竞争逻辑**：竞争逻辑不是'谁更先进'，而是车载量产的三硬约束：150–350 m主探测距离、车规可靠性(AEC-Q102)、单件成本。Nature Communications工业综述给出的三分类是：机械式=激光器/透镜/传感器整体运动；混合固态=仅MEMS或转镜运动；全固态=电学扫描、无运动部件。结论是纯机械式在L2/L3 ADAS中'has nearly phased out of existence'，混合固态成为 centre stage；原因是有运动件的机械总成在振动、温循、寿命、体积和成本上劣于只保留一维扫描镜的方案，而全固态OPA/Flash短期又达不到远距与量产良率。胜负判据：先过150–350 m与车规，再把BOM降到约$100；不过可靠性就出局，不过成本就无法从~0.5%乘用车渗透率跳到>10%。
- **硬数字**：主LiDAR需求距离150–350 m；机械式在L2/L3 ADAS近乎退出；LiDAR单价从>$10,000降到$500–$1,000，作者估约$100才能把渗透率从~0.5%推到>10%；1550 nm光纤激光虽眼安全功率上限高但InGaAs探测器/激光成本高、散热与可靠性风险大；905 nm EEL典型~200 m上限。口径：工业综述归纳的量产与成本判断，不是单厂实测。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.nature.com/articles/s41467-024-51975-6）来源链接
  - [外]（出处：https://www.nature.com/articles/s41467-025-62027-y）来源链接
  - [外]（出处：https://www.nature.com/articles/s41467-026-71867-1）来源链接
#### 2. 混合固态内部路线：905 nm EEL+二维MEMS vs 905 nm多结VCSEL+一维转镜
- **竞争逻辑**：第一代混合固态用EEL+2D MEMS，需多颗EEL拼接视场且要对激光源与MEMS做精密对准，电机数多、热与校准负担重。新路线用电扫描VCSEL阵列+一颗1D多边形/转镜：电机从2个降到1个，取消激光-MEMS精密对准；VCSEL的0.07 nm/°C本征温稳、圆斑、冗余发光单元、6英寸GaAs晶圆成本基础成为胜出判据，历史短板是功率密度/亮度，由多结堆叠补上。实验室/器件级验证不等于整车量产：多结AR-VCSEL是器件数据，Hesai AT128用Lumentum 905 nm 5结VCSEL才进入产品。
- **硬数字**：Robosense M1用5颗EEL模块覆盖120° FOV；新方案电机2→1；VCSEL温漂0.07 nm/°C；6结AR-VCSEL阵列2.6 mm长×85 µm发光宽，50 kHz/3 ns/50°C下峰值400 W、D86=16°；EEL LiDAR典型~200 m，6结AR-VCSEL>200 m，预测8–10结达300–400 m；分辨率判据Δx=4(BPP/D)R，200 m处10 cm分辨率、5 cm准直镜需~0.03°角分辨与BPP~6.25；AEC-Q102项目含1000 h HTOL、1000 h 85°C/85%RH、500 h LTOL；42颗AR-VCSEL阵列芯片全部通过6000 h HTOL(5 ns/600 kHz/85°C环境/~130°C结温/~50 W初始峰值，失效阈值>20%功率退化)，作者折算>300年车载使用；数万颗芯片FIT研究约30亿等效器…
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://www.nature.com/articles/s41467-024-51975-6）来源链接
#### 3. 直接ToF vs FMCW相干LiDAR：抗干扰/测速 vs 光源复杂度
- **竞争逻辑**：ToF靠短脉冲往返时间，链简单但易受环境光、多径和他车激光干扰，速度只能靠帧间差分。FMCW发线性调频连续波，回波与本振拍频编码距离，升降斜坡同时给出多普勒速度，故抗干扰、直接测速、距离分辨率高；代价是激光器相位噪声/线宽、啁啾线性度、输出功率和25 GHz级采集电子学。Nature评论明确：1%啁啾非线性对距离分辨率的损害等价于线宽放大5倍；对超窄线宽自注入锁激光，继续压线宽收益有限，改善线性度才有效。胜负判据不是处处FMCW赢，而是'每次点都要速度+强干扰环境'时FMCW赢；追求最低BOM的普通车载ToF仍占量产。
- **硬数字**：理想FMCW距离分辨率δR=c/2B；1%啁啾非线性≈线宽×5的分辨率损害；三角啁啾最大无模糊距离MUR=cT/4，f_max=βT/2；按25 GHz探测器带宽，啁啾率>10^17 Hz/s只对极短距有用；PIC FMCW因集成光源功率低，多数用途限几百米，航天场景≤1 km测高；已演示月球下降载荷FoV 25°×25°、1 km最大测距、500 m处5.8 mm点精度；航天PIC-FMCW整体TRL4–5，尚未验证振动/冲击/辐射。关键修正：2025原稿式(1)漏掉因子6，正确式δR=c√[(6√5 τ(2τ/T−1)σ_RMS)^2+(γ/β)^2]；不得引用修正前数值。口径：Nature评论+作者更正的模型和演示值。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.nature.com/articles/s41467-025-62027-y）来源链接
  - [外]（出处：https://www.nature.com/articles/s41467-026-71867-1）来源链接
#### 4. 纯固态OPA/Flash LiDAR的边缘化：有样机≠量产
- **竞争逻辑**：OPA/LCM(液晶)与Flash曾被当作'无运动件=车规天然赢家'，但判据是视场×距离×功率孔径积的净能量账。Nature工业综述判定OPA和LCM已有商用产品但未实现量产，其他固态转向方案仍在研究阶段；Flash VCSEL通常只做短距；可寻址VCSEL阵列才在逐步进入量产。FMCW独立来源进一步给出集成光子方案的TRL4–5、几百米限制、需要大收集孔径与密集数据处理，说明'全固态'在长距车载上被混合固态反超的原因：省掉机械件省不下光子功率、热与成本。
- **硬数字**：OPA、LCM：commercially available但未mass production；其他固态转向=research phase；Flash VCSEL=usually short range；混合固态VCSEL+1D转镜已把电机2→1并通过6000 h HTOL；PIC-FMCW航天TRL4–5、几百米级、≤1 km测高；主车载仍需150–350 m、成本目标~$100。口径：量产状态为工业综述判断，TRL为独立Nature评论判断；本次未取得OPA失败率或良率的量化字段，标为定性判据。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.nature.com/articles/s41467-024-51975-6）来源链接
  - [外]（出处：https://www.nature.com/articles/s41467-025-62027-y）来源链接
  - [外]（出处：https://www.nature.com/articles/s41467-026-71867-1）来源链接
#### 5. 光纤传感：FBG点式 vs 分布式Rayleigh/Brillouin/Raman vs 干涉型OFDR/phase-OTDR
- **竞争逻辑**：三条路线的物理分工由'空间分辨率—量程—被测量'三角决定。FBG是点式波长编码，应变~1 pm/µε、温度~10 pm/°C，1 mm–1 cm点空间分辨率，WDM/放大可达数米–100 km，但每个光栅>€50且解调仪>€5000，适合关键点的长期、高精度、多点复用监测。分布式Rayleigh(OFDR/phase-OTDR)靠 Rayleigh 相干/相位实现mm–cm级空间分辨，量程通常≤30 m(专门系统到2 km)、振动响应350–500 Hz，适合裂缝萌生、局部高分辨；Brillouin靠布里渊频移~10–11 GHz，背向散射比Rayleigh弱16–20 dB，声子寿命+SNR/频率估计折中把空间分辨率锁在0.2–3 m，但量程10–100 km，适合长距离应变/温度；Raman频移~13 THz，Stokes/anti-Stokes比测温，背散弱20/30 dB，Planck标定难、不能测应变，量程ROTDR 20+ km，适合分布式温度。干涉型OFDR/phase-OTDR本质是Rayleigh路线的高分辨子类：mm级分辨率以量程和采集时间为代价。胜负判据：点精度与…
- **硬数字**：FBG：应变~1 pm/µε、温度~10 pm/°C、点空间1 mm–1 cm、数米–100 km、>€50/栅+>€5000解调仪。Rayleigh：应变~0.5–1 µε、温度~0.05–0.1°C、空间1 mm–1 cm(或数m)、通常≤30 m/专用≤2 km、振动350–500 Hz。Brillouin：应变10–50 µε、温度~0.28–1.3°C、空间0.2–3 m、10–100 km、振动55–60 Hz、频移10–11 GHz(1550 nm约0.05–0.08 nm)、比Rayleigh弱16–20 dB。Raman：温度~0.1°C(ROFDR)~1.8°C(ROTDR)、空间~1 m(长距)/1 cm@3 m、≤10 km ROFDR或20+ km ROTDR、应变N/A、频移~13 THz(~100 nm@1500 nm)、Stokes/anti-Stokes弱…
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC12430957）来源链接
#### 6. 医学成像：共聚焦 vs OCT vs 超声的分辨率—穿透深度权衡
- **竞争逻辑**：竞争不是替代而是互补：散射随深度指数上升，分辨率与穿透深度不可同时最大化。共聚焦用针孔抑制离焦光，1 µm级细胞形态但只到~100–200 µm(综述表列~500 µm上限)；OCT用低相干干涉做2–10 µm的B-mode式层析，到1–2 mm(~2 mm)，看不到单个癌细胞形态；超声用MHz声学对比，150 µm分辨但可到~10 cm，能看深部范围与血管；CT/MRI再往全身。判据：要细胞学超浅层选共聚焦，要1–2 mm组织结构选OCT，要深部边界/血管选超声；line-field confocal OCT试图用~1 µm各向同性分辨填到~500 µm，是融合而非消灭原路线。
- **硬数字**：皮肤成像表：共聚焦1 µm/~500 µm；OCT 2–10 µm/~2 mm；超声150 µm/~10 cm；高分辨CT 300 µm/全身；MRI 1 mm/全身。正文口径：共聚焦可达100–200 µm@1 µm；OCT 1–2 mm@2–10 µm；line-field confocal OCT ~1 µm各向同性到~500 µm；RCM在2016年已有美国CPT计费码；超声7–15 MHz测BCC厚度与组织学ICC=0.9(25例)，70 MHz用于细节。口径： Frontiers in Medicine 2019综述汇总，ICC为25例小样本。
- **状态**：单源未验证
- **出处**：
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC6883721）来源链接
#### 7. 无创血糖光谱：NIR/PPG vs Raman vs 光声/光热 vs THz——为何难商用及FDA硬门槛
- **竞争逻辑**：四条光谱路线共享同一物理死结：葡萄糖在复杂皮肤基质中的吸收/散射特征被水、蛋白、脂质、温度、血流、肤色/黑色素与环境光淹没，且测到的是组织液而非血液，稀释与滞后使'相关性'不等于'可治疗决策的准确度'。NIR/PPG信号强、可穿戴化最好但特异性最差；Raman有分子指纹、特异性较强但信号弱需长积分与复杂算法；光声/光热(QCL 8–12 µm指纹区)能做深度门控、对血流层选择性更好，但热/黏滞损失、功率与标定难；THz(300 GHz–10 THz/3 mm–30 µm)只作用于表皮，穿透浅、矩阵效应大。FDA硬门槛是'不许把未验证的无创claims当血糖测量卖'：截至2024-02-21，任何声称无创测血糖的智能手表/戒指都未获authorized/cleared/approved，错误读数可致胰岛素过量、低血糖、昏迷甚至数小时内死亡；2025 MIT workshop也确认no noninvasive device has achieved FDA clearance for direct glucose measurement。
- **硬数字**：2023综述：筛243篇纳入124篇(54光学/37电磁/29纳米/4生理)；PPG研究5项，最低SEP 17.02 mg/dL，MARD 4.4321%–12.19%，Pearson r=0.91，100%点落CEG A–B(实验室/小样本，非FDA)；47个产品中无FDA批准，4个有CE(GlucoTrack/GWave/Glutrac/Egm1000)；NIR间歇产品10个、Raman 5个；ISO 15197:2013门槛：<100 mg/dL时≥95%在±15 mg/dL内，≥100 mg/dL时≥95%在±15%内；THz=300 GHz–10 THz(3 mm–30 µm)。2026 workshop：DiaMonTech MIR光热D-Base在36人单中心两轮，最佳算法MARD 20.7%/19.6%，3次有创校准可维持≥1周，D-Pocket原型30–50次/充电、计划…
- **状态**：已核验
- **出处**：
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC10674292）来源链接
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC13186910）来源链接
  - [外]（出处：https://www.fda.gov/medical-devices/safety-communications/do-not-use-smartwatches-or-smart-rings-measure-blood-glucose-levels-fda-safety-communication）来源链接
  - [外]（出处：https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-862/subpart-B/section-862.1355）来源链接
#### 8. 淘汰/边缘化路线复盘：被挤出的机械旋转、GlucoWatch/Pendra式无创、以及消费级'无创血糖'智能穿戴
- **竞争逻辑**：提炼出的通用判据是三条：①可靠性/成本硬约束先筛掉路线(机械旋转、未量产OPA)；②准确率必须达到可治疗决策的置信界而不是相关系数(GlucoWatch/Pendra因准确度与校准失败退出；早期PPG/NIR的r=0.91低SEP仍不够)；③监管允许的症状/claim边界决定商用资格(任何无创手表/戒指血糖claims在FDA处为零授权)。被替代不是因为原理错，而是更优路线在同一判据上给出可复算的更好数字：混合固态用单电机+VCSEL通过车规，微量/微创CGM用iCGM置信界达标。
- **硬数字**：机械LiDAR在L2/L3 ADAS近乎退出；OPA/LCM有商用但未量产；LiDAR成本>$10,000→$500–$1,000，~$100才是渗透率>10%的门槛；47个无创血糖产品中0个FDA批准、4个CE；GlucoWatch与Pendra因准确度/校准问题退出，Pendra上市后对所有用户失败且需复杂校准；ISO 15197最低95%在±15 mg/dL或±15%；FDA 2024-02-21确认无任何无创智能手表/戒指获授权；iCGM 70–180 mg/dL区间±15%需>70%且单侧95%置信，全程±20%需>87%。口径：综述+监管原文交叉，'退出/失败'为文献结论。
- **状态**：已核验
- **出处**：
  - [外]（出处：https://www.nature.com/articles/s41467-024-51975-6）来源链接
  - [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC10674292）来源链接
  - [外]（出处：https://www.fda.gov/medical-devices/safety-communications/do-not-use-smartwatches-or-smart-rings-measure-blood-glucose-levels-fda-safety-communication）来源链接
  - [外]（出处：https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-862/subpart-B/section-862.1355）来源链接
## 证据清单
| # | 路线主题 | 结论摘要 | 支撑 | 来源 |
| --- | --- | --- | --- | --- |
| 1 | 光模块与光互连路线之争 | 可插拔光模块 vs CPO（共封装光学）：从反复狼来了到2026兑现 | [外] | [来源](https://lumentum.com/sites/default/files/2026-06/elsfpreliability-wp-cl-ae.pdf) |
| 2 | 光模块与光互连路线之争 | 可插拔光模块 vs CPO（共封装光学）：从反复狼来了到2026兑现 | [外] | [来源](https://www.lumentum.com/en/blog/reliability-becomes-new-currency-how-cpo-rewriting-laser-performance) |
| 3 | 光模块与光互连路线之争 | 可插拔光模块 vs CPO（共封装光学）：从反复狼来了到2026兑现 | [外] | [来源](https://eps.ieee.org/wp-content/uploads/2025/11/Photonics_TC_Co-Packaged_Optics_Final.pdf) |
| 4 | 光模块与光互连路线之争 | 可插拔光模块 vs CPO（共封装光学）：从反复狼来了到2026兑现 | [外] | [来源](https://photonica.io/articles/pluggable-lpo-lro-cpo) |
| 5 | 光模块与光互连路线之争 | 可插拔光模块 vs CPO（共封装光学）：从反复狼来了到2026兑现 | [外] | [来源](https://lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377) |
| 6 | 光模块与光互连路线之争 | 可插拔光模块 vs CPO（共封装光学）：从反复狼来了到2026兑现 | [外] | [来源](https://newsletter.semianalysis.com/p/co-packaged-optics-cpo-book-scaling) |
| 7 | 光模块与光互连路线之争 | 可插拔光模块 vs CPO（共封装光学）：从反复狼来了到2026兑现 | [外] | [来源](https://datacenterdynamics.com/en/analysis/optical-illusion-is-co-packaged-optics-the-savior-the-data-center-industry-has-been-waiting-for) |
| 8 | 光模块与光互连路线之争 | 可插拔光模块 vs CPO（共封装光学）：从反复狼来了到2026兑现 | [外] | [来源](https://theregister.com/special-features/2025/11/22/copackaged-optics-have-officially-found-their-killer-app/2014010) |
| 9 | 光模块与光互连路线之争 | 硅光 vs InP vs VCSEL：中短距/长距的路线归属与物理经济判据 | [外] | [来源](https://lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377) |
| 10 | 光模块与光互连路线之争 | 硅光 vs InP vs VCSEL：中短距/长距的路线归属与物理经济判据 | [外] | [来源](https://lightcounting.com/newsletter/en/january-2026-optics-for-ai-clusters-366) |
| 11 | 光模块与光互连路线之争 | 硅光 vs InP vs VCSEL：中短距/长距的路线归属与物理经济判据 | [外] | [来源](https://lightcounting.com/research-note/november-2023-lumentum-is-back-in-intel-is-out-315) |
| 12 | 光模块与光互连路线之争 | 硅光 vs InP vs VCSEL：中短距/长距的路线归属与物理经济判据 | [外] | [来源](https://doi.org/10.1117/12.630237) |
| 13 | 光模块与光互连路线之争 | 硅光 vs InP vs VCSEL：中短距/长距的路线归属与物理经济判据 | [外] | [来源](https://trendforce.com/news/2026/08/06/news-inp-shortage-emerges-as-ai-optical-interconnect-bottleneck) |
| 14 | 光模块与光互连路线之争 | 硅光 vs InP vs VCSEL：中短距/长距的路线归属与物理经济判据 | [外] | [来源](https://cisco.com/c/dam/en/us/products/collateral/interfaces-modules/transceiver-modules/wp8350-hdr-mmf.pdf) |
| 15 | 光模块与光互连路线之争 | 硅光 vs InP vs VCSEL：中短距/长距的路线归属与物理经济判据 | [外] | [来源](https://blog.sumitomoelectriclightwave.com/vcsel-applications-for-ai-factory) |
| 16 | 光模块与光互连路线之争 | LPO（线性直驱） vs DSP 可插拔 vs CPO：功耗/成本/链路预算三方之争 | [外] | [来源](https://eps.ieee.org/wp-content/uploads/2026/03/Linear-Pluggable-Optics_V2-UPDATED.pdf) |
| 17 | 光模块与光互连路线之争 | LPO（线性直驱） vs DSP 可插拔 vs CPO：功耗/成本/链路预算三方之争 | [外] | [来源](https://blog.semtech.com/200g-lpo-power-reach-and-loss-real-numbers) |
| 18 | 光模块与光互连路线之争 | LPO（线性直驱） vs DSP 可插拔 vs CPO：功耗/成本/链路预算三方之争 | [外] | [来源](https://photonica.io/articles/pluggable-lpo-lro-cpo) |
| 19 | 光模块与光互连路线之争 | LPO（线性直驱） vs DSP 可插拔 vs CPO：功耗/成本/链路预算三方之争 | [外] | [来源](https://lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377) |
| 20 | 光模块与光互连路线之争 | CW 光源路线：外置激光源 ELS/ELSFP vs 片上集成激光 | [外] | [来源](https://photonica.io/articles/co-packaged-optics-light-sources) |
| 21 | 光模块与光互连路线之争 | CW 光源路线：外置激光源 ELS/ELSFP vs 片上集成激光 | [外] | [来源](https://lumentum.com/sites/default/files/2026-06/elsfpreliability-wp-cl-ae.pdf) |
| 22 | 光模块与光互连路线之争 | CW 光源路线：外置激光源 ELS/ELSFP vs 片上集成激光 | [外] | [来源](https://www.lumentum.com/en/blog/reliability-becomes-new-currency-how-cpo-rewriting-laser-performance) |
| 23 | 光模块与光互连路线之争 | CW 光源路线：外置激光源 ELS/ELSFP vs 片上集成激光 | [外] | [来源](https://eps.ieee.org/wp-content/uploads/2025/11/Photonics_TC_Co-Packaged_Optics_Final.pdf) |
| 24 | 光模块与光互连路线之争 | 光互连调制格式路线：NRZ vs PAM4 vs 相干（相干下沉） | [外] | [来源](https://oiforum.com/wp-content/uploads/OIF-400ZR-03.0.1.pdf) |
| 25 | 光模块与光互连路线之争 | 光互连调制格式路线：NRZ vs PAM4 vs 相干（相干下沉） | [外] | [来源](https://cdn.teledynelecroy.com/files/whitepapers/800ge-vs-1-6te.pdf) |
| 26 | 光模块与光互连路线之争 | 光互连调制格式路线：NRZ vs PAM4 vs 相干（相干下沉） | [外] | [来源](https://investor.marvell.com/_assets/_88edfb3f52300551f17c1e541972f365/marvell/news/2026-03-05_Marvell_Extends_ZR_ZR_Leadership_with_Industry_1010.pdf) |
| 27 | 光模块与光互连路线之争 | 光互连调制格式路线：NRZ vs PAM4 vs 相干（相干下沉） | [外] | [来源](https://ieee802.org/3/dv/public/2611/shrikhande_3dv_01a_2611.pdf) |
| 28 | 光模块与光互连路线之争 | 光互连调制格式路线：NRZ vs PAM4 vs 相干（相干下沉） | [外] | [来源](https://ieee802.org/3/dj/public/25_01/shrikhande_3dj_01_2501.pdf) |
| 29 | 光模块与光互连路线之争 | 光互连调制格式路线：NRZ vs PAM4 vs 相干（相干下沉） | [外] | [来源](https://adtran.com/en/products-and-services/open-optical-networking/pluggables-and-subsystems/coherent-zr-series/coherent-400zr-series) |
| 30 | 光模块与光互连路线之争 | 光互连调制格式路线：NRZ vs PAM4 vs 相干（相干下沉） | [外] | [来源](https://fibermall.com/blog/800g-in-data-center-pam4-or-coherent.htm) |
| 31 | 光模块与光互连路线之争 | 淘汰/边缘化路线复盘：LiDAR 机械→固态、硅光由看衰到翻盘 | [外] | [来源](https://lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377) |
| 32 | 光模块与光互连路线之争 | 淘汰/边缘化路线复盘：LiDAR 机械→固态、硅光由看衰到翻盘 | [外] | [来源](https://lightcounting.com/research-note/november-2023-lumentum-is-back-in-intel-is-out-315) |
| 33 | 光模块与光互连路线之争 | 淘汰/边缘化路线复盘：LiDAR 机械→固态、硅光由看衰到翻盘 | [外] | [来源](https://venturebeat.com/2021/05/24/intel-sees-bright-future-for-silicon-photonics-moving-information-at-light-speed-in-datacenters-and-beyond) |
| 34 | 光模块与光互连路线之争 | 淘汰/边缘化路线复盘：LiDAR 机械→固态、硅光由看衰到翻盘 | [外] | [来源](https://www.nature.com/articles/s41467-024-51975-6) |
| 35 | 光模块与光互连路线之争 | 淘汰/边缘化路线复盘：LiDAR 机械→固态、硅光由看衰到翻盘 | [外] | [来源](https://ouster.com/insights/blog/what-is-the-end-state-of-automotive-lidar) |
| 36 | 光模块与光互连路线之争 | 淘汰/边缘化路线复盘：LiDAR 机械→固态、硅光由看衰到翻盘 | [外] | [来源](https://blog.leddartech.com/velodyne-shift-toward-solid-state-lidar-for-automotive-applications) |
| 37 | 光模块与光互连路线之争 | 淘汰/边缘化路线复盘：LiDAR 机械→固态、硅光由看衰到翻盘 | [外] | [来源](https://ieeexplore.ieee.org/document/10234174) |
| 38 | 光模块与光互连路线之争 | 淘汰/边缘化路线复盘：LiDAR 机械→固态、硅光由看衰到翻盘 | [外] | [来源](https://ieeexplore.ieee.org/ielx7/5/8540482/08438526.pdf) |
| 39 | 光计算路线与商业化成败 | 全光计算 vs 光电混合：非线性必须靠电、无光存储是关键物理判据 | [外] | [来源](https://www.nature.com/articles/s41586-025-08786-6) |
| 40 | 光计算路线与商业化成败 | 全光计算 vs 光电混合：非线性必须靠电、无光存储是关键物理判据 | [外] | [来源](https://arstechnica.com/science/2025/01/getting-an-all-optical-ai-to-handle-non-linear-math) |
| 41 | 光计算路线与商业化成败 | 全光计算 vs 光电混合：非线性必须靠电、无光存储是关键物理判据 | [外] | [来源](https://news.mit.edu/2017/new-system-allows-optical-deep-learning-0612) |
| 42 | 光计算路线与商业化成败 | 创业公司路线分化：Lightmatter从光计算转向光互连，曦智双线并行 | [外] | [来源](https://www.eetimes.com/lightmatter-raises-400-million-series-d/) |
| 43 | 光计算路线与商业化成败 | 创业公司路线分化：Lightmatter从光计算转向光互连，曦智双线并行 | [外] | [来源](https://lightelligence.ai/products/photon-computing/pace2) |
| 44 | 光计算路线与商业化成败 | 创业公司路线分化：Lightmatter从光计算转向光互连，曦智双线并行 | [外] | [来源](https://lightelligence.ai/community/papers/9) |
| 45 | 光计算路线与商业化成败 | 光互连派：Ayar Labs / Celestial AI 靠CPO先兑现并被产业资本整合 | [外] | [来源](https://www.theregister.com/on-prem/2026/03/03/ayar-labs-raises-500m-to-mass-produce-cpo-chiplets/4889700) |
| 46 | 光计算路线与商业化成败 | 光互连派：Ayar Labs / Celestial AI 靠CPO先兑现并被产业资本整合 | [外] | [来源](https://datadeep.tech/photonic-neural-networks/) |
| 47 | 光计算路线与商业化成败 | 光互连派：Ayar Labs / Celestial AI 靠CPO先兑现并被产业资本整合 | [外] | [来源](https://siliconangle.com/2025/03/11/celestial-ai-raises-250m-optical-interconnect-technology) |
| 48 | 光计算路线与商业化成败 | 相干光计算 vs 强度(非相干)光计算 / 自由空间 vs 波导集成：精度与规模口径之争 | [外] | [来源](https://www.nature.com/articles/s41586-025-08786-6) |
| 49 | 光计算路线与商业化成败 | 相干光计算 vs 强度(非相干)光计算 / 自由空间 vs 波导集成：精度与规模口径之争 | [外] | [来源](https://media.au.tsinghua.edu.cn/info/1016/1231.htm) |
| 50 | 光计算路线与商业化成败 | 相干光计算 vs 强度(非相干)光计算 / 自由空间 vs 波导集成：精度与规模口径之争 | [外] | [来源](https://dx.doi.org/10.1126/science.adl1203) |
| 51 | 光计算路线与商业化成败 | 相干光计算 vs 强度(非相干)光计算 / 自由空间 vs 波导集成：精度与规模口径之争 | [外] | [来源](https://datadeep.tech/photonic-neural-networks/) |
| 52 | 光计算路线与商业化成败 | 自由空间全光生成式原型 LightGen：宣传口径与可核验口径存在落差 | [外] | [来源](https://www.chinadaily.com.cn/a/202512/20/WS6945ede4a310d6866eb2f9ad.html) |
| 53 | 光计算路线与商业化成败 | 自由空间全光生成式原型 LightGen：宣传口径与可核验口径存在落差 | [外] | [来源](https://scmp.com/news/china/science/article/3336918/chinese-team-builds-optical-chip-ai-100-times-faster-nvidias-market-leader) |
| 54 | 光计算路线与商业化成败 | 应用场景之争：组合优化(Ising/Max-cut)先于AI训练落地，训练仍电子主导 | [外] | [来源](https://www.nature.com/articles/s41586-025-08786-6) |
| 55 | 光计算路线与商业化成败 | 应用场景之争：组合优化(Ising/Max-cut)先于AI训练落地，训练仍电子主导 | [外] | [来源](https://media.au.tsinghua.edu.cn/info/1016/1231.htm) |
| 56 | 光计算路线与商业化成败 | 应用场景之争：组合优化(Ising/Max-cut)先于AI训练落地，训练仍电子主导 | [外] | [来源](https://datadeep.tech/photonic-neural-networks/) |
| 57 | 光计算路线与商业化成败 | 历史教训：2010s光计算泡沫退潮与2020s AI算力需求重启 | [外] | [来源](https://news.mit.edu/2017/new-system-allows-optical-deep-learning-0612) |
| 58 | 光计算路线与商业化成败 | 历史教训：2010s光计算泡沫退潮与2020s AI算力需求重启 | [外] | [来源](https://technologyreview.com/2016/11/18/155929/silicon-photonic-neural-network-unveiled) |
| 59 | 光计算路线与商业化成败 | 历史教训：2010s光计算泡沫退潮与2020s AI算力需求重启 | [外] | [来源](https://datadeep.tech/photonic-neural-networks/) |
| 60 | 光计算路线与商业化成败 | Luminous Computing现状：2023年光子团队裁员、退出计算类别 | [外] | [来源](https://venturebeat.com/ai/luminous-computing-which-is-developing-a-light-based-ai-accelerator-chip-raises-105m) |
| 61 | 光计算路线与商业化成败 | Luminous Computing现状：2023年光子团队裁员、退出计算类别 | [外] | [来源](https://datadeep.tech/photonic-neural-networks/) |
| 62 | 新型显示与成像路线之争 | Micro LED vs OLED vs LCD：量产胜出判据是像素级良率×转移节拍×晶粒成本，而非单点画质 | [外] | [来源](https://sid.org/Portals/sid/Files/SID-Digest/docs/59-3.pdf) |
| 63 | 新型显示与成像路线之争 | Micro LED vs OLED vs LCD：量产胜出判据是像素级良率×转移节拍×晶粒成本，而非单点画质 | [外] | [来源](https://microledassociation.com/wp-content/uploads/2023/02/MicroLED-yields-2023-02.pdf) |
| 64 | 新型显示与成像路线之争 | Micro LED vs OLED vs LCD：量产胜出判据是像素级良率×转移节拍×晶粒成本，而非单点画质 | [外] | [来源](https://electronicdesign.com/technologies/industrial/displays/article/21273604/kla-corp-microled-displays-how-to-achieve-a-999999-yield) |
| 65 | 新型显示与成像路线之争 | Micro LED vs OLED vs LCD：量产胜出判据是像素级良率×转移节拍×晶粒成本，而非单点画质 | [外] | [来源](https://insightmedia.info/microled-market-is-developing-but-challenges-remain) |
| 66 | 新型显示与成像路线之争 | Micro LED vs OLED vs LCD：量产胜出判据是像素级良率×转移节拍×晶粒成本，而非单点画质 | [外] | [来源](https://www.nature.com/articles/s41377-025-02027-1) |
| 67 | 新型显示与成像路线之争 | AR/VR近眼路线：Birdbath/自由曲面 vs 光波导（几何/衍射/全息）——赢在形态，卡在光效与制造 | [外] | [来源](https://vrarwiki.com/wiki/Birdbath_optics) |
| 68 | 新型显示与成像路线之争 | AR/VR近眼路线：Birdbath/自由曲面 vs 光波导（几何/衍射/全息）——赢在形态，卡在光效与制造 | [外] | [来源](https://paloaltooptics.com/blog/waveguide-vs-birdbath-vs-pancake-near-eye-architectures) |
| 69 | 新型显示与成像路线之争 | AR/VR近眼路线：Birdbath/自由曲面 vs 光波导（几何/衍射/全息）——赢在形态，卡在光效与制造 | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC11021499/) |
| 70 | 新型显示与成像路线之争 | AR/VR近眼路线：Birdbath/自由曲面 vs 光波导（几何/衍射/全息）——赢在形态，卡在光效与制造 | [外] | [来源](https://www.nature.com/articles/s41377-021-00658-8) |
| 71 | 新型显示与成像路线之争 | 衍射光波导内部：SRG vs VHG vs PVG——效率/均匀性/色彩/可量产性的三角取舍 | [外] | [来源](https://doi.org/10.1038/s41377-024-01537-8) |
| 72 | 新型显示与成像路线之争 | 衍射光波导内部：SRG vs VHG vs PVG——效率/均匀性/色彩/可量产性的三角取舍 | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC11021499/) |
| 73 | 新型显示与成像路线之争 | 衍射光波导内部：SRG vs VHG vs PVG——效率/均匀性/色彩/可量产性的三角取舍 | [外] | [来源](https://link.springer.com/article/10.1186/s43593-023-00057-z) |
| 74 | 新型显示与成像路线之争 | 图像传感器：CMOS vs CCD——集成度/功耗/成本压倒纯画质优势；BSI/堆叠式继续放大优势 | [外] | [来源](https://electronicsweekly.com/business/bye-bye-ccd-2010-10/) |
| 75 | 新型显示与成像路线之争 | 图像传感器：CMOS vs CCD——集成度/功耗/成本压倒纯画质优势；BSI/堆叠式继续放大优势 | [外] | [来源](https://edn.com/cmos-image-sensors-continue-march-to-dominance-over-ccds/) |
| 76 | 新型显示与成像路线之争 | 红外探测：制冷型InSb/HgCdTe vs 非制冷微测辐射热计——成本/SWaP/即开即用判定主流，性能高端留给定制冷 | [外] | [来源](https://infraredcore.com/cases/cooled-vs-uncooled-infrared-detectors-principles-performance-and-cost-comparison-56968.html) |
| 77 | 新型显示与成像路线之争 | 红外探测：制冷型InSb/HgCdTe vs 非制冷微测辐射热计——成本/SWaP/即开即用判定主流，性能高端留给定制冷 | [外] | [来源](https://www.irmodules.com/information/knowledge/cooled-mwir-vs-uncooled-lwir-a-buyer-s-guide-for-system-integrators/) |
| 78 | 新型显示与成像路线之争 | 红外探测：制冷型InSb/HgCdTe vs 非制冷微测辐射热计——成本/SWaP/即开即用判定主流，性能高端留给定制冷 | [外] | [来源](https://www.mordorintelligence.com/industry-reports/uncooled-infrared-imaging-market) |
| 79 | 新型显示与成像路线之争 | 被淘汰路线复盘：PDP vs LCD——尺寸/价格/功耗/产能的规模化判据 | [外] | [来源](https://www.cnet.com/home/smart-home/study-plasma-tv-panel-shipments-hit-record-high/) |
| 80 | 新型显示与成像路线之争 | 被淘汰路线复盘：PDP vs LCD——尺寸/价格/功耗/产能的规模化判据 | [外] | [来源](https://www.nbcnews.com/id/wbna36645703) |
| 81 | 新型显示与成像路线之争 | 被淘汰路线复盘：PDP vs LCD——尺寸/价格/功耗/产能的规模化判据 | [外] | [来源](https://www.twice.com/news/industry-reacts-panasonics-plasma-exit-49364) |
| 82 | 新型显示与成像路线之争 | 被淘汰路线复盘：PDP vs LCD——尺寸/价格/功耗/产能的规模化判据 | [外] | [来源](https://viewsonic.com/library/tech/dlp-vs-3lcd-projector-which-one-is-better/) |
| 83 | 新型显示与成像路线之争 | 量子点/有机图像传感器未覆盖：检索两轮到顶，未拿到可核验的量产良率/暗电流/成本数字 | [外] | [来源](https://www.nature.com/articles/s41566-025-01759-1) |
| 84 | 新型显示与成像路线之争 | 量子点/有机图像传感器未覆盖：检索两轮到顶，未拿到可核验的量产良率/暗电流/成本数字 | [外] | [来源](https://www.nature.com/articles/s44287-025-00199-x) |
| 85 | 新型显示与成像路线之争 | QWIP/II类超晶格红外路线未覆盖：未拿到与MCT/InSb可比的量产良率与成本-性能数字 | [外] | [来源](https://teledynevisionsolutions.com/learn/learning-center/scientific-imaging/infrared-detector-sensor-materials) |
| 86 | 新型显示与成像路线之争 | QWIP/II类超晶格红外路线未覆盖：未拿到与MCT/InSb可比的量产良率与成本-性能数字 | [外] | [来源](https://www.infraredcore.com/cases/cooled-vs-uncooled-infrared-detectors-principles-performance-and-cost-comparison-56968.html) |
| 87 | 新型显示与成像路线之争 | 早期LCoS失败判据未覆盖：Springer章节被客户端挑战拦截，未获得可核验的良率/成本/量产数据 | [外] | [来源](https://link.springer.com/article/10.1007/978-3-319-14346-0_126) |
| 88 | 新型显示与成像路线之争 | 早期LCoS失败判据未覆盖：Springer章节被客户端挑战拦截，未获得可核验的良率/成本/量产数据 | [外] | [来源](https://www.mdpi.com/2813-446x/3/4/25) |
| 89 | 新型显示与成像路线之争 | 早期LCoS失败判据未覆盖：Springer章节被客户端挑战拦截，未获得可核验的良率/成本/量产数据 | [外] | [来源](https://vrarwiki.com/wiki/Birdbath_optics) |
| 90 | 激光与光源路线之争 | 半导体激光器材料体系：InP vs GaAs vs GaN 的波长归属 | [外] | [来源](https://doi.org/10.1109/2944.954127) |
| 91 | 激光与光源路线之争 | 半导体激光器材料体系：InP vs GaAs vs GaN 的波长归属 | [外] | [来源](https://doi.org/10.1109/2944.788414) |
| 92 | 激光与光源路线之争 | 半导体激光器材料体系：InP vs GaAs vs GaN 的波长归属 | [外] | [来源](https://doi.org/10.1063/1.125643) |
| 93 | 激光与光源路线之争 | 半导体激光器材料体系：InP vs GaAs vs GaN 的波长归属 | [外] | [来源](https://doi.org/10.1002/andp.201500801) |
| 94 | 激光与光源路线之争 | 半导体激光器材料体系：InP vs GaAs vs GaN 的波长归属 | [外] | [来源](https://iopscience.iop.org/article/10.1088/1742-6596/2426/1/012008/pdf) |
| 95 | 激光与光源路线之争 | 硅基光源路线之争：异质集成 III-V vs 键合 vs 外延直接生长 vs 拉曼激光 | [外] | [来源](https://nature.com/articles/lsa2015131) |
| 96 | 激光与光源路线之争 | 硅基光源路线之争：异质集成 III-V vs 键合 vs 外延直接生长 vs 拉曼激光 | [外] | [来源](https://doi.org/10.1364/AOP.455976) |
| 97 | 激光与光源路线之争 | 硅基光源路线之争：异质集成 III-V vs 键合 vs 外延直接生长 vs 拉曼激光 | [外] | [来源](https://opg.optica.org/aop/abstract.cfm?uri=aop-14-3-404) |
| 98 | 激光与光源路线之争 | 硅基光源路线之争：异质集成 III-V vs 键合 vs 外延直接生长 vs 拉曼激光 | [外] | [来源](https://www.nature.com/articles/s41377-022-00982-7) |
| 99 | 激光与光源路线之争 | 硅基光源路线之争：异质集成 III-V vs 键合 vs 外延直接生长 vs 拉曼激光 | [外] | [来源](https://www.nature.com/articles/s41377-023-01128-z) |
| 100 | 激光与光源路线之争 | 硅基光源路线之争：异质集成 III-V vs 键合 vs 外延直接生长 vs 拉曼激光 | [外] | [来源](https://www.nature.com/articles/s41377-024-01389-2) |
| 101 | 激光与光源路线之争 | 光纤激光器 vs 固体激光器 vs 半导体激光器：工业加工/通信/医疗归属 | [外] | [来源](https://ipgphotonicsus.com/technology.html) |
| 102 | 激光与光源路线之争 | 光纤激光器 vs 固体激光器 vs 半导体激光器：工业加工/通信/医疗归属 | [外] | [来源](https://cdn.ipgphotonics.com/3694f393-6e4c-49e4-9374-b1400126ebba/IPG_YLS-SM-Series_DS_EN_LTR.pdf) |
| 103 | 激光与光源路线之争 | 超快激光器路线：钛宝石 vs 光纤 vs SESAM 可饱和吸收 | [外] | [来源](https://ieeexplore.ieee.org/document/9484726) |
| 104 | 激光与光源路线之争 | 超快激光器路线：钛宝石 vs 光纤 vs SESAM 可饱和吸收 | [外] | [来源](https://pubmed.ncbi.nlm.nih.gov/29716015/) |
| 105 | 激光与光源路线之争 | 超快激光器路线：钛宝石 vs 光纤 vs SESAM 可饱和吸收 | [外] | [来源](https://ieeexplore.ieee.org/document/1308612) |
| 106 | 激光与光源路线之争 | 窄线宽光源路线：外腔半导体 ECL vs 光纤激光 vs 硅光集成（2026） | [外] | [来源](https://nature.com/articles/s41377-026-02249-x) |
| 107 | 激光与光源路线之争 | 窄线宽光源路线：外腔半导体 ECL vs 光纤激光 vs 硅光集成（2026） | [外] | [来源](https://www.nature.com/articles/s41377-026-02249-x) |
| 108 | 激光与光源路线之争 | 窄线宽光源路线：外腔半导体 ECL vs 光纤激光 vs 硅光集成（2026） | [外] | [来源](https://arxiv.org/abs/2610.22596) |
| 109 | 激光与光源路线之争 | 窄线宽光源路线：外腔半导体 ECL vs 光纤激光 vs 硅光集成（2026） | [外] | [来源](https://arxiv.org/abs/2601.18609) |
| 110 | 激光与光源路线之争 | 淘汰路线复盘：染料激光器退场与气体激光器(He-Ne/CO2)份额萎缩 | [外] | [来源](https://spie.org/publications/fg12_p79-80_dye_lasers) |
| 111 | 激光与光源路线之争 | 淘汰路线复盘：染料激光器退场与气体激光器(He-Ne/CO2)份额萎缩 | [外] | [来源](https://doi.org/10.1364/OPN.13.5.000024) |
| 112 | 光伏电池路线之争 | 晶硅 vs CdTe/CIGS/非晶硅：成本、效率与产业链的路线筛选 | [外] | [来源](https://oecd.org/content/dam/oecd/en/publications/reports/2022/08/special-report-on-solar-pv-global-supply-chains_f884fe79/9e8b0121-en.pdf) |
| 113 | 光伏电池路线之争 | 晶硅 vs CdTe/CIGS/非晶硅：成本、效率与产业链的路线筛选 | [外] | [来源](https://gminsights.com/industry-analysis/solar-pv-module-market) |
| 114 | 光伏电池路线之争 | 晶硅 vs CdTe/CIGS/非晶硅：成本、效率与产业链的路线筛选 | [外] | [来源](https://firstsolar.com/Products/Series-7) |
| 115 | 光伏电池路线之争 | 晶硅 vs CdTe/CIGS/非晶硅：成本、效率与产业链的路线筛选 | [外] | [来源](https://osti.gov/biblio/3025381) |
| 116 | 光伏电池路线之争 | 晶硅 vs CdTe/CIGS/非晶硅：成本、效率与产业链的路线筛选 | [外] | [来源](https://cell.com/joule/fulltext/S2542-4351(25)00416-7) |
| 117 | 光伏电池路线之争 | PERC vs TOPCon vs HJT vs BC：效率溢价能否覆盖改线成本 | [外] | [来源](https://taiyangnews.info/technology/itrpv-expects-topcon-to-lead-as-bc-and-tandem-technologies-expand) |
| 118 | 光伏电池路线之争 | PERC vs TOPCon vs HJT vs BC：效率溢价能否覆盖改线成本 | [外] | [来源](https://jrsttechnology.com/knowledge/back-contact-bc-solar-cells-india) |
| 119 | 光伏电池路线之争 | PERC vs TOPCon vs HJT vs BC：效率溢价能否覆盖改线成本 | [外] | [来源](https://pv-magazine-india.com/2025/07/07/bringing-back-contact-to-the-foreground) |
| 120 | 光伏电池路线之争 | PERC vs TOPCon vs HJT vs BC：效率溢价能否覆盖改线成本 | [外] | [来源](https://infolink-group.com/energy-article/solar-topic-solar-back-contact-technology-industry-progress-outlook--xbc) |
| 121 | 光伏电池路线之争 | 单结钙钛矿 vs 钙钛矿-硅叠层：效率上限与可运营寿命的竞赛 | [外] | [来源](https://onlinelibrary.wiley.com/doi/10.1002/pip.70068) |
| 122 | 光伏电池路线之争 | 单结钙钛矿 vs 钙钛矿-硅叠层：效率上限与可运营寿命的竞赛 | [外] | [来源](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.202502696) |
| 123 | 光伏电池路线之争 | 单结钙钛矿 vs 钙钛矿-硅叠层：效率上限与可运营寿命的竞赛 | [外] | [来源](https://onlinelibrary.wiley.com/doi/10.1002/cey2.70241?af=R) |
| 124 | 光伏电池路线之争 | 单结钙钛矿 vs 钙钛矿-硅叠层：效率上限与可运营寿命的竞赛 | [外] | [来源](https://nature.com/articles/s41560-026-02161-z) |
| 125 | 光伏电池路线之争 | 单结钙钛矿 vs 钙钛矿-硅叠层：效率上限与可运营寿命的竞赛 | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC11137052/) |
| 126 | 光伏电池路线之争 | 聚光光伏 CPV vs 常规平板：集中式与分布式的系统级兴衰 | [外] | [来源](https://optics.org/news/7/2/35) |
| 127 | 光伏电池路线之争 | 聚光光伏 CPV vs 常规平板：集中式与分布式的系统级兴衰 | [外] | [来源](https://www.ise.fraunhofer.de/en/publications/veroeffentlichungen-pdf-dateien-en/studien-und-konzeptpapiere/current-status-of-concentrator-photovoltaic-cpv-technology.pdf) |
| 128 | 光伏电池路线之争 | 聚光光伏 CPV vs 常规平板：集中式与分布式的系统级兴衰 | [外] | [来源](https://nature.com/articles/nenergy201618) |
| 129 | 光伏电池路线之争 | 聚光光伏 CPV vs 常规平板：集中式与分布式的系统级兴衰 | [外] | [来源](https://serdp-estcp.mil/projects/details/95ef08f7-73f3-4554-9693-0f0be9b5ce51) |
| 130 | 光伏电池路线之争 | 第三代路线：热载流子、多激子、中间带与量子点谁最接近实用 | [外] | [来源](https://pubs.rsc.org/en/content/articlepdf/2025/el/d5el00053j) |
| 131 | 光伏电池路线之争 | 第三代路线：热载流子、多激子、中间带与量子点谁最接近实用 | [外] | [来源](https://mdpi.com/2072-666x/17/4/474) |
| 132 | 光伏电池路线之争 | 第三代路线：热载流子、多激子、中间带与量子点谁最接近实用 | [外] | [来源](https://pubs.acs.org/doi/full/10.1021/acsenergylett.3c01983) |
| 133 | 光伏电池路线之争 | 第三代路线：热载流子、多激子、中间带与量子点谁最接近实用 | [外] | [来源](https://europepmc.org/article/MED/42076250) |
| 134 | 光伏电池路线之争 | 2000s泡沫与2010s过剩：政策、成本与技术路线如何共同筛选赢家 | [外] | [来源](https://pv-magazine.com/2021/10/30/the-weekend-read-whats-next-for-polysilicon) |
| 135 | 光伏电池路线之争 | 2000s泡沫与2010s过剩：政策、成本与技术路线如何共同筛选赢家 | [外] | [来源](https://bernreuter.com/files/data/newsroom/pdf-articles/magazine-reports/2024-05-pv-magazine-D%C3%A9j%C3%A0-vu-on-the-polysilicon-market.pdf) |
| 136 | 光伏电池路线之争 | 2000s泡沫与2010s过剩：政策、成本与技术路线如何共同筛选赢家 | [外] | [来源](https://bloomberg.com/news/articles/2011-11-10/solar-costs-drop-so-suddenly-it-hurts-) |
| 137 | 光伏电池路线之争 | 2000s泡沫与2010s过剩：政策、成本与技术路线如何共同筛选赢家 | [外] | [来源](https://csis-website-prod.s3.amazonaws.com/s3fs-public/2026-03/260312_Davidson_China_Solar_0.pdf) |
| 138 | 光伏电池路线之争 | 2000s泡沫与2010s过剩：政策、成本与技术路线如何共同筛选赢家 | [外] | [来源](https://oecd.org/content/dam/oecd/en/publications/reports/2022/08/special-report-on-solar-pv-global-supply-chains_f884fe79/9e8b0121-en.pdf) |
| 139 | 光伏电池路线之争 | 2000s泡沫与2010s过剩：政策、成本与技术路线如何共同筛选赢家 | [外] | [来源](https://thebatterymagazine.com/future-of-solar-module-topcon-hjt-and-perovskite) |
| 140 | 光电传感与测量路线之争 | 车载LiDAR扫描架构：机械旋转 vs 半固态(MEMS/转镜) vs 纯固态(OPA/Flash/VCSEL) | [外] | [来源](https://www.nature.com/articles/s41467-024-51975-6) |
| 141 | 光电传感与测量路线之争 | 车载LiDAR扫描架构：机械旋转 vs 半固态(MEMS/转镜) vs 纯固态(OPA/Flash/VCSEL) | [外] | [来源](https://www.nature.com/articles/s41467-025-62027-y) |
| 142 | 光电传感与测量路线之争 | 车载LiDAR扫描架构：机械旋转 vs 半固态(MEMS/转镜) vs 纯固态(OPA/Flash/VCSEL) | [外] | [来源](https://www.nature.com/articles/s41467-026-71867-1) |
| 143 | 光电传感与测量路线之争 | 混合固态内部路线：905 nm EEL+二维MEMS vs 905 nm多结VCSEL+一维转镜 | [外] | [来源](https://www.nature.com/articles/s41467-024-51975-6) |
| 144 | 光电传感与测量路线之争 | 直接ToF vs FMCW相干LiDAR：抗干扰/测速 vs 光源复杂度 | [外] | [来源](https://www.nature.com/articles/s41467-025-62027-y) |
| 145 | 光电传感与测量路线之争 | 直接ToF vs FMCW相干LiDAR：抗干扰/测速 vs 光源复杂度 | [外] | [来源](https://www.nature.com/articles/s41467-026-71867-1) |
| 146 | 光电传感与测量路线之争 | 纯固态OPA/Flash LiDAR的边缘化：有样机≠量产 | [外] | [来源](https://www.nature.com/articles/s41467-024-51975-6) |
| 147 | 光电传感与测量路线之争 | 纯固态OPA/Flash LiDAR的边缘化：有样机≠量产 | [外] | [来源](https://www.nature.com/articles/s41467-025-62027-y) |
| 148 | 光电传感与测量路线之争 | 纯固态OPA/Flash LiDAR的边缘化：有样机≠量产 | [外] | [来源](https://www.nature.com/articles/s41467-026-71867-1) |
| 149 | 光电传感与测量路线之争 | 光纤传感：FBG点式 vs 分布式Rayleigh/Brillouin/Raman vs 干涉型OFDR/phase-OTDR | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC12430957) |
| 150 | 光电传感与测量路线之争 | 医学成像：共聚焦 vs OCT vs 超声的分辨率—穿透深度权衡 | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC6883721) |
| 151 | 光电传感与测量路线之争 | 无创血糖光谱：NIR/PPG vs Raman vs 光声/光热 vs THz——为何难商用及FDA硬门槛 | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC10674292) |
| 152 | 光电传感与测量路线之争 | 无创血糖光谱：NIR/PPG vs Raman vs 光声/光热 vs THz——为何难商用及FDA硬门槛 | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC13186910) |
| 153 | 光电传感与测量路线之争 | 无创血糖光谱：NIR/PPG vs Raman vs 光声/光热 vs THz——为何难商用及FDA硬门槛 | [外] | [来源](https://www.fda.gov/medical-devices/safety-communications/do-not-use-smartwatches-or-smart-rings-measure-blood-glucose-levels-fda-safety-communication) |
| 154 | 光电传感与测量路线之争 | 无创血糖光谱：NIR/PPG vs Raman vs 光声/光热 vs THz——为何难商用及FDA硬门槛 | [外] | [来源](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-862/subpart-B/section-862.1355) |
| 155 | 光电传感与测量路线之争 | 淘汰/边缘化路线复盘：被挤出的机械旋转、GlucoWatch/Pendra式无创、以及消费级&#x27;无创血糖&#x27;智能穿戴 | [外] | [来源](https://www.nature.com/articles/s41467-024-51975-6) |
| 156 | 光电传感与测量路线之争 | 淘汰/边缘化路线复盘：被挤出的机械旋转、GlucoWatch/Pendra式无创、以及消费级&#x27;无创血糖&#x27;智能穿戴 | [外] | [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC10674292) |
| 157 | 光电传感与测量路线之争 | 淘汰/边缘化路线复盘：被挤出的机械旋转、GlucoWatch/Pendra式无创、以及消费级&#x27;无创血糖&#x27;智能穿戴 | [外] | [来源](https://www.fda.gov/medical-devices/safety-communications/do-not-use-smartwatches-or-smart-rings-measure-blood-glucose-levels-fda-safety-communication) |
| 158 | 光电传感与测量路线之争 | 淘汰/边缘化路线复盘：被挤出的机械旋转、GlucoWatch/Pendra式无创、以及消费级&#x27;无创血糖&#x27;智能穿戴 | [外] | [来源](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-862/subpart-B/section-862.1355) |

## 口径与来源
本报告数据状态分三档：**已核验**＝多源交叉或一手论文/权威机构原文；**单源未验证**＝仅单一来源、未升级为定论；**未覆盖**＝两轮换词检索后仍无可引用一手出处。所有 URL 均为公开链接，标注 [外] 者来自公开网络一手资料；数字均标口径并区分理论极限与实测值。
## 来源分区
### 公开信息
- [外]（出处：https://lumentum.com/sites/default/files/2026-06/elsfpreliability-wp-cl-ae.pdf）来源1
- [外]（出处：https://www.lumentum.com/en/blog/reliability-becomes-new-currency-how-cpo-rewriting-laser-performance）来源2
- [外]（出处：https://eps.ieee.org/wp-content/uploads/2025/11/Photonics_TC_Co-Packaged_Optics_Final.pdf）来源3
- [外]（出处：https://photonica.io/articles/pluggable-lpo-lro-cpo）来源4
- [外]（出处：https://lightcounting.com/newsletter/en/may-2026-silicon-photonics-lpolro-and-npocpo-377）来源5
- [外]（出处：https://newsletter.semianalysis.com/p/co-packaged-optics-cpo-book-scaling）来源6
- [外]（出处：https://datacenterdynamics.com/en/analysis/optical-illusion-is-co-packaged-optics-the-savior-the-data-center-industry-has-been-waiting-for）来源7
- [外]（出处：https://theregister.com/special-features/2025/11/22/copackaged-optics-have-officially-found-their-killer-app/2014010）来源8
- [外]（出处：https://lightcounting.com/newsletter/en/january-2026-optics-for-ai-clusters-366）来源9
- [外]（出处：https://lightcounting.com/research-note/november-2023-lumentum-is-back-in-intel-is-out-315）来源10
- [外]（出处：https://doi.org/10.1117/12.630237）来源11
- [外]（出处：https://trendforce.com/news/2026/08/06/news-inp-shortage-emerges-as-ai-optical-interconnect-bottleneck）来源12
- [外]（出处：https://cisco.com/c/dam/en/us/products/collateral/interfaces-modules/transceiver-modules/wp8350-hdr-mmf.pdf）来源13
- [外]（出处：https://blog.sumitomoelectriclightwave.com/vcsel-applications-for-ai-factory）来源14
- [外]（出处：https://eps.ieee.org/wp-content/uploads/2026/03/Linear-Pluggable-Optics_V2-UPDATED.pdf）来源15
- [外]（出处：https://blog.semtech.com/200g-lpo-power-reach-and-loss-real-numbers）来源16
- [外]（出处：https://photonica.io/articles/co-packaged-optics-light-sources）来源17
- [外]（出处：https://oiforum.com/wp-content/uploads/OIF-400ZR-03.0.1.pdf）来源18
- [外]（出处：https://cdn.teledynelecroy.com/files/whitepapers/800ge-vs-1-6te.pdf）来源19
- [外]（出处：https://investor.marvell.com/_assets/_88edfb3f52300551f17c1e541972f365/marvell/news/2026-03-05_Marvell_Extends_ZR_ZR_Leadership_with_Industry_1010.pdf）来源20
- [外]（出处：https://ieee802.org/3/dv/public/2611/shrikhande_3dv_01a_2611.pdf）来源21
- [外]（出处：https://ieee802.org/3/dj/public/25_01/shrikhande_3dj_01_2501.pdf）来源22
- [外]（出处：https://adtran.com/en/products-and-services/open-optical-networking/pluggables-and-subsystems/coherent-zr-series/coherent-400zr-series）来源23
- [外]（出处：https://fibermall.com/blog/800g-in-data-center-pam4-or-coherent.htm）来源24
- [外]（出处：https://venturebeat.com/2021/05/24/intel-sees-bright-future-for-silicon-photonics-moving-information-at-light-speed-in-datacenters-and-beyond）来源25
- [外]（出处：https://www.nature.com/articles/s41467-024-51975-6）来源26
- [外]（出处：https://ouster.com/insights/blog/what-is-the-end-state-of-automotive-lidar）来源27
- [外]（出处：https://blog.leddartech.com/velodyne-shift-toward-solid-state-lidar-for-automotive-applications）来源28
- [外]（出处：https://ieeexplore.ieee.org/document/10234174）来源29
- [外]（出处：https://ieeexplore.ieee.org/ielx7/5/8540482/08438526.pdf）来源30
- [外]（出处：https://www.nature.com/articles/s41586-025-08786-6）来源31
- [外]（出处：https://arstechnica.com/science/2025/01/getting-an-all-optical-ai-to-handle-non-linear-math）来源32
- [外]（出处：https://news.mit.edu/2017/new-system-allows-optical-deep-learning-0612）来源33
- [外]（出处：https://www.eetimes.com/lightmatter-raises-400-million-series-d/）来源34
- [外]（出处：https://lightelligence.ai/products/photon-computing/pace2）来源35
- [外]（出处：https://lightelligence.ai/community/papers/9）来源36
- [外]（出处：https://www.theregister.com/on-prem/2026/03/03/ayar-labs-raises-500m-to-mass-produce-cpo-chiplets/4889700）来源37
- [外]（出处：https://datadeep.tech/photonic-neural-networks/）来源38
- [外]（出处：https://siliconangle.com/2025/03/11/celestial-ai-raises-250m-optical-interconnect-technology）来源39
- [外]（出处：https://media.au.tsinghua.edu.cn/info/1016/1231.htm）来源40
- [外]（出处：https://dx.doi.org/10.1126/science.adl1203）来源41
- [外]（出处：https://www.chinadaily.com.cn/a/202512/20/WS6945ede4a310d6866eb2f9ad.html）来源42
- [外]（出处：https://scmp.com/news/china/science/article/3336918/chinese-team-builds-optical-chip-ai-100-times-faster-nvidias-market-leader）来源43
- [外]（出处：https://technologyreview.com/2016/11/18/155929/silicon-photonic-neural-network-unveiled）来源44
- [外]（出处：https://venturebeat.com/ai/luminous-computing-which-is-developing-a-light-based-ai-accelerator-chip-raises-105m）来源45
- [外]（出处：https://sid.org/Portals/sid/Files/SID-Digest/docs/59-3.pdf）来源46
- [外]（出处：https://microledassociation.com/wp-content/uploads/2023/02/MicroLED-yields-2023-02.pdf）来源47
- [外]（出处：https://electronicdesign.com/technologies/industrial/displays/article/21273604/kla-corp-microled-displays-how-to-achieve-a-999999-yield）来源48
- [外]（出处：https://insightmedia.info/microled-market-is-developing-but-challenges-remain）来源49
- [外]（出处：https://www.nature.com/articles/s41377-025-02027-1）来源50
- [外]（出处：https://vrarwiki.com/wiki/Birdbath_optics）来源51
- [外]（出处：https://paloaltooptics.com/blog/waveguide-vs-birdbath-vs-pancake-near-eye-architectures）来源52
- [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC11021499/）来源53
- [外]（出处：https://www.nature.com/articles/s41377-021-00658-8）来源54
- [外]（出处：https://doi.org/10.1038/s41377-024-01537-8）来源55
- [外]（出处：https://link.springer.com/article/10.1186/s43593-023-00057-z）来源56
- [外]（出处：https://electronicsweekly.com/business/bye-bye-ccd-2010-10/）来源57
- [外]（出处：https://edn.com/cmos-image-sensors-continue-march-to-dominance-over-ccds/）来源58
- [外]（出处：https://infraredcore.com/cases/cooled-vs-uncooled-infrared-detectors-principles-performance-and-cost-comparison-56968.html）来源59
- [外]（出处：https://www.irmodules.com/information/knowledge/cooled-mwir-vs-uncooled-lwir-a-buyer-s-guide-for-system-integrators/）来源60
- [外]（出处：https://www.mordorintelligence.com/industry-reports/uncooled-infrared-imaging-market）来源61
- [外]（出处：https://www.cnet.com/home/smart-home/study-plasma-tv-panel-shipments-hit-record-high/）来源62
- [外]（出处：https://www.nbcnews.com/id/wbna36645703）来源63
- [外]（出处：https://www.twice.com/news/industry-reacts-panasonics-plasma-exit-49364）来源64
- [外]（出处：https://viewsonic.com/library/tech/dlp-vs-3lcd-projector-which-one-is-better/）来源65
- [外]（出处：https://www.nature.com/articles/s41566-025-01759-1）来源66
- [外]（出处：https://www.nature.com/articles/s44287-025-00199-x）来源67
- [外]（出处：https://teledynevisionsolutions.com/learn/learning-center/scientific-imaging/infrared-detector-sensor-materials）来源68
- [外]（出处：https://www.infraredcore.com/cases/cooled-vs-uncooled-infrared-detectors-principles-performance-and-cost-comparison-56968.html）来源69
- [外]（出处：https://link.springer.com/article/10.1007/978-3-319-14346-0_126）来源70
- [外]（出处：https://www.mdpi.com/2813-446x/3/4/25）来源71
- [外]（出处：https://doi.org/10.1109/2944.954127）来源72
- [外]（出处：https://doi.org/10.1109/2944.788414）来源73
- [外]（出处：https://doi.org/10.1063/1.125643）来源74
- [外]（出处：https://doi.org/10.1002/andp.201500801）来源75
- [外]（出处：https://iopscience.iop.org/article/10.1088/1742-6596/2426/1/012008/pdf）来源76
- [外]（出处：https://nature.com/articles/lsa2015131）来源77
- [外]（出处：https://doi.org/10.1364/AOP.455976）来源78
- [外]（出处：https://opg.optica.org/aop/abstract.cfm?uri=aop-14-3-404）来源79
- [外]（出处：https://www.nature.com/articles/s41377-022-00982-7）来源80
- [外]（出处：https://www.nature.com/articles/s41377-023-01128-z）来源81
- [外]（出处：https://www.nature.com/articles/s41377-024-01389-2）来源82
- [外]（出处：https://ipgphotonicsus.com/technology.html）来源83
- [外]（出处：https://cdn.ipgphotonics.com/3694f393-6e4c-49e4-9374-b1400126ebba/IPG_YLS-SM-Series_DS_EN_LTR.pdf）来源84
- [外]（出处：https://ieeexplore.ieee.org/document/9484726）来源85
- [外]（出处：https://pubmed.ncbi.nlm.nih.gov/29716015/）来源86
- [外]（出处：https://ieeexplore.ieee.org/document/1308612）来源87
- [外]（出处：https://nature.com/articles/s41377-026-02249-x）来源88
- [外]（出处：https://www.nature.com/articles/s41377-026-02249-x）来源89
- [外]（出处：https://arxiv.org/abs/2610.22596）来源90
- [外]（出处：https://arxiv.org/abs/2601.18609）来源91
- [外]（出处：https://spie.org/publications/fg12_p79-80_dye_lasers）来源92
- [外]（出处：https://doi.org/10.1364/OPN.13.5.000024）来源93
- [外]（出处：https://oecd.org/content/dam/oecd/en/publications/reports/2022/08/special-report-on-solar-pv-global-supply-chains_f884fe79/9e8b0121-en.pdf）来源94
- [外]（出处：https://gminsights.com/industry-analysis/solar-pv-module-market）来源95
- [外]（出处：https://firstsolar.com/Products/Series-7）来源96
- [外]（出处：https://osti.gov/biblio/3025381）来源97
- [外]（出处：https://cell.com/joule/fulltext/S2542-4351(25)00416-7）来源98
- [外]（出处：https://taiyangnews.info/technology/itrpv-expects-topcon-to-lead-as-bc-and-tandem-technologies-expand）来源99
- [外]（出处：https://jrsttechnology.com/knowledge/back-contact-bc-solar-cells-india）来源100
- [外]（出处：https://pv-magazine-india.com/2025/07/07/bringing-back-contact-to-the-foreground）来源101
- [外]（出处：https://infolink-group.com/energy-article/solar-topic-solar-back-contact-technology-industry-progress-outlook--xbc）来源102
- [外]（出处：https://onlinelibrary.wiley.com/doi/10.1002/pip.70068）来源103
- [外]（出处：https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.202502696）来源104
- [外]（出处：https://onlinelibrary.wiley.com/doi/10.1002/cey2.70241?af=R）来源105
- [外]（出处：https://nature.com/articles/s41560-026-02161-z）来源106
- [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC11137052/）来源107
- [外]（出处：https://optics.org/news/7/2/35）来源108
- [外]（出处：https://www.ise.fraunhofer.de/en/publications/veroeffentlichungen-pdf-dateien-en/studien-und-konzeptpapiere/current-status-of-concentrator-photovoltaic-cpv-technology.pdf）来源109
- [外]（出处：https://nature.com/articles/nenergy201618）来源110
- [外]（出处：https://serdp-estcp.mil/projects/details/95ef08f7-73f3-4554-9693-0f0be9b5ce51）来源111
- [外]（出处：https://pubs.rsc.org/en/content/articlepdf/2025/el/d5el00053j）来源112
- [外]（出处：https://mdpi.com/2072-666x/17/4/474）来源113
- [外]（出处：https://pubs.acs.org/doi/full/10.1021/acsenergylett.3c01983）来源114
- [外]（出处：https://europepmc.org/article/MED/42076250）来源115
- [外]（出处：https://pv-magazine.com/2021/10/30/the-weekend-read-whats-next-for-polysilicon）来源116
- [外]（出处：https://bernreuter.com/files/data/newsroom/pdf-articles/magazine-reports/2024-05-pv-magazine-D%C3%A9j%C3%A0-vu-on-the-polysilicon-market.pdf）来源117
- [外]（出处：https://bloomberg.com/news/articles/2011-11-10/solar-costs-drop-so-suddenly-it-hurts-）来源118
- [外]（出处：https://csis-website-prod.s3.amazonaws.com/s3fs-public/2026-03/260312_Davidson_China_Solar_0.pdf）来源119
- [外]（出处：https://thebatterymagazine.com/future-of-solar-module-topcon-hjt-and-perovskite）来源120
- [外]（出处：https://www.nature.com/articles/s41467-025-62027-y）来源121
- [外]（出处：https://www.nature.com/articles/s41467-026-71867-1）来源122
- [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC12430957）来源123
- [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC6883721）来源124
- [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC10674292）来源125
- [外]（出处：https://pmc.ncbi.nlm.nih.gov/articles/PMC13186910）来源126
- [外]（出处：https://www.fda.gov/medical-devices/safety-communications/do-not-use-smartwatches-or-smart-rings-measure-blood-glucose-levels-fda-safety-communication）来源127
- [外]（出处：https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-862/subpart-B/section-862.1355）来源128
