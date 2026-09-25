# -*- coding: utf-8 -*-
"""Generate the SE Asian peatland WTD dataset inventory (CSV + Markdown)."""
import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent

COLS = [
    "ID", "类别", "站点/数据集", "国家", "省/州", "纬度", "经度", "坐标来源",
    "土地利用/状态", "数据时段", "时间分辨率", "测量方式/精度", "站点/井数",
    "可获取性", "数据链接", "原始文献", "文献链接", "核实状态/备注",
]

R = []
def row(**kw):
    R.append([kw.get(c, "") for c in COLS])

# ---------------- A: in situ, openly downloadable ----------------
row(ID="A1", 类别="原位·公开", **{
    "站点/数据集": "Mendaram 泥炭穹水文数据（PANGAEA 数据集系列）",
    "国家": "文莱", "省/州": "Belait（Ulu Mendaram 保护区）",
    "纬度": "4.367", "经度": "114.350", "坐标来源": "文献（4°22′N, 114°21′E）",
    "土地利用/状态": "原始、未排水泥炭沼泽林（泥炭穹，~40 km²）",
    "数据时段": "2012–2013（数据集标题）",
    "时间分辨率": "自记连续（间隔见数据集）",
    "测量方式/精度": "Solinst Levelogger Edge 压力式水位计 + Barologger 气压校正（厂商标称 ±0.05% FS）；另附 Ks、Sy、穿透雨",
    "站点/井数": "4 口测井 + 4 个雨量计",
    "可获取性": "A 公开（PANGAEA）",
    "数据链接": "https://doi.org/10.1594/PANGAEA.908215",
    "原始文献": "Cobb & Harvey 2019, WRR；Cobb et al. 2017, PNAS",
    "文献链接": "https://doi.org/10.1029/2019WR025411 ; https://doi.org/10.1073/pnas.1701090114",
    "核实状态/备注": "数据集条目、仪器已核实；许可证未打开核实",
})
row(ID="A2", 类别="原位·公开", **{
    "站点/数据集": "Mendaram 地下水位 + CO2 + 温度时间序列",
    "国家": "文莱", "省/州": "Belait（Ulu Mendaram）",
    "纬度": "4.367", "经度": "114.350", "坐标来源": "同 A1（文献）",
    "土地利用/状态": "未排水泥炭沼泽林",
    "数据时段": "WTD：2012-02-06 至 2015-02-06",
    "时间分辨率": "连续自记",
    "测量方式/精度": "同 A1 水位计网络",
    "站点/井数": "见数据集",
    "可获取性": "A 公开（Zenodo）",
    "数据链接": "https://zenodo.org/records/3245335",
    "原始文献": "Hoyt et al. 2019, GCB",
    "文献链接": "https://doi.org/10.1111/gcb.14702",
    "核实状态/备注": "时段已核实",
})
row(ID="A3", 类别="原位·公开", **{
    "站点/数据集": "Palangkaraya 三个通量站 UF/DF/DB（CO2 通量 + 气象 + 地下水位）",
    "国家": "印尼", "省/州": "中加里曼丹 Central Kalimantan",
    "纬度": "UF −2.32；DB −2.34；DF ≈−2.34", "经度": "UF 113.90；DB 114.04；DF ≈114.04",
    "坐标来源": "UF 取自 FLUXNET-CH4 元数据；DB 取自文献；DF 按“三站相距 15 km 以内”近似",
    "土地利用/状态": "UF 基本未排水林；DF 重度排水林；DB 排水后火烧迹地",
    "数据时段": "约 2002–2017（每站 12–15 年，逐站起止见 SI）",
    "时间分辨率": "通量半小时；地下水位日值及以上",
    "测量方式/精度": "自记水位计（型号见原文）",
    "站点/井数": "3 站",
    "可获取性": "A 公开（figshare 分享链接）",
    "数据链接": "https://figshare.com/s/6aefe20137486d0a6f62",
    "原始文献": "Hirano et al. 2024, Communications Earth & Environment",
    "文献链接": "https://doi.org/10.1038/s43247-024-01387-7",
    "核实状态/备注": "数据链接已核实；逐站年份需查 SI",
})
row(ID="A4", 类别="原位·公开", **{
    "站点/数据集": "DailyGWL.xlsx：Palangkaraya 未排水/排水泥炭林日地下水位",
    "国家": "印尼", "省/州": "中加里曼丹",
    "纬度": "≈−2.3", "经度": "≈113.9–114.0", "坐标来源": "区域近似（同 A3）",
    "土地利用/状态": "未排水 PSF；排水 PSF",
    "数据时段": "未排水 2015–2018；排水 2013–2017",
    "时间分辨率": "日",
    "测量方式/精度": "自记水位计",
    "站点/井数": "2 站",
    "可获取性": "A 公开（figshare）",
    "数据链接": "https://figshare.com/articles/dataset/DailyGWL_xlsx/22321129/1",
    "原始文献": "Hirano 课题组数据；疑似被 Koupaei-Abyazani et al. 2024（IN-undrained/IN-drained 站）使用",
    "文献链接": "https://doi.org/10.1029/2024JG008116",
    "核实状态/备注": "数据与时段已核实；关联论文待核实",
})
row(ID="A5", 类别="原位·公开", **{
    "站点/数据集": "FLUXNET-CH4 ID-Pag（Palangkaraya 未排水林）",
    "国家": "印尼", "省/州": "中加里曼丹",
    "纬度": "−2.32", "经度": "113.90", "坐标来源": "数据集元数据",
    "土地利用/状态": "未排水泥炭沼泽林",
    "数据时段": "2016–2017",
    "时间分辨率": "半小时/日（FLUXNET 格式）",
    "测量方式/精度": "EC 通量；是否含 WTD 变量需下载后确认",
    "站点/井数": "1 塔",
    "可获取性": "A 公开（FLUXNET-CH4，CC-BY 4.0）",
    "数据链接": "https://doi.org/10.18140/FLX/1669643",
    "原始文献": "Sakabe et al. 2018, GCB；Delwiche et al. 2021, ESSD",
    "文献链接": "https://doi.org/10.1111/gcb.14410 ; https://doi.org/10.5194/essd-13-3607-2021",
    "核实状态/备注": "坐标、年份已核实",
})
row(ID="A6", 类别="原位·公开", **{
    "站点/数据集": "FLUXNET-CH4 MY-MLM（Maludam 国家公园）",
    "国家": "马来西亚", "省/州": "砂拉越 Sarawak（Betong）",
    "纬度": "1.4536", "经度": "111.1495", "坐标来源": "数据集元数据",
    "土地利用/状态": "原始泥炭沼泽林（泥炭厚约 8 m）",
    "数据时段": "FLUXNET-CH4 子集年份见数据页；同站 CO2 与水位 2011–2014（Tang 2020）",
    "时间分辨率": "半小时",
    "测量方式/精度": "EC 通量 + 地下水位",
    "站点/井数": "1 塔",
    "可获取性": "A 公开（FLUXNET-CH4 子集）；完整 2011–2014 数据需向 Sarawak TROPI 申请",
    "数据链接": "https://doi.org/10.18140/FLX/1669650",
    "原始文献": "Tang et al. 2018, GRL；Tang et al. 2020, GCB",
    "文献链接": "https://doi.org/10.1029/2017GL076457 ; https://doi.org/10.1111/gcb.15332",
    "核实状态/备注": "坐标已核实；FLUXNET-CH4 子集年份未核实",
})
row(ID="A7", 类别="原位·公开", **{
    "站点/数据集": "Kampar 半岛：原始林 vs 退化林（EC + 地下水位）",
    "国家": "印尼", "省/州": "廖内 Riau",
    "纬度": "≈0.3", "经度": "≈102.8", "坐标来源": "区域近似（塔位坐标见原文 SI）",
    "土地利用/状态": "原始泥炭林；退化林",
    "数据时段": "2017 年中至 2020 年中",
    "时间分辨率": "半小时（EC）；地下水位连续",
    "测量方式/精度": "自记水位计（型号见原文）",
    "站点/井数": "2 塔",
    "可获取性": "A 公开（Zenodo）",
    "数据链接": "https://doi.org/10.5281/zenodo.4835696",
    "原始文献": "Deshmukh et al. 2021, Nature Geoscience",
    "文献链接": "https://doi.org/10.1038/s41561-021-00785-2",
    "核实状态/备注": "Zenodo 与时段已核实",
})
row(ID="A8", 类别="原位·公开", **{
    "站点/数据集": "Kampar 半岛：金合欢种植园 / 退化林 / 原始林",
    "国家": "印尼", "省/州": "廖内 Riau",
    "纬度": "≈0.3", "经度": "≈102.8", "坐标来源": "区域近似（塔位坐标见原文 SI）",
    "土地利用/状态": "Acacia crassicarpa 种植园；退化林；原始林",
    "数据时段": "2016-10 至 2022-05（种植园 EC 至 2021-05；原始林 EC 自 2017-06）",
    "时间分辨率": "半小时（EC）；地下水位连续",
    "测量方式/精度": "自记水位计",
    "站点/井数": "3 塔",
    "可获取性": "A 公开（Zenodo）",
    "数据链接": "https://zenodo.org/records/7500659",
    "原始文献": "Deshmukh et al. 2023, Nature；Deshmukh et al. 2020, GCB",
    "文献链接": "https://doi.org/10.1038/s41586-023-05860-9 ; https://doi.org/10.1111/gcb.15019",
    "核实状态/备注": "已核实",
})
row(ID="A9", 类别="原位·公开", **{
    "站点/数据集": "印尼泥炭地下水位 + 持水特性数据集（8 站）",
    "国家": "印尼", "省/州": "占碑 Jambi（Batanghari）；西加里曼丹（Kubu Raya）",
    "纬度": "Batanghari ≈−1.7；Kubu Raya ≈−0.4", "经度": "Batanghari ≈103.1；Kubu Raya ≈109.4",
    "坐标来源": "区域近似（逐站坐标见原文表格）",
    "土地利用/状态": "人为改造/退化泥炭地",
    "数据时段": "2018–2019",
    "时间分辨率": "日",
    "测量方式/精度": "自动监测站（地下水位、雨量、土壤湿度）",
    "站点/井数": "8 站",
    "可获取性": "A 公开（Data in Brief 附件，Excel）",
    "数据链接": "https://www.sciencedirect.com/science/article/pii/S2352340922001159",
    "原始文献": "Taufik et al. 2022, Data in Brief 41（doi:10.1016/j.dib.2022.107903）",
    "文献链接": "https://pubmed.ncbi.nlm.nih.gov/35198682/",
    "核实状态/备注": "站数、时段已核实；DOI 取自检索摘要",
})
row(ID="A10", 类别="原位·公开（相关变量）", **{
    "站点/数据集": "苏门答腊泥炭含水量数据集（21 站）",
    "国家": "印尼", "省/州": "苏门答腊 3 个省",
    "纬度": "见原文", "经度": "见原文", "坐标来源": "—",
    "土地利用/状态": "人为改造泥炭地",
    "数据时段": "2018–2019",
    "时间分辨率": "日",
    "测量方式/精度": "土壤含水量（不是 WTD）；站点与 SiPALAGA 相关",
    "站点/井数": "21 站",
    "可获取性": "A 公开（Data in Brief）",
    "数据链接": "https://www.sciencedirect.com/science/article/pii/S2352340923000070",
    "原始文献": "Taufik et al. 2023, Data in Brief（doi:10.1016/j.dib.2023.108889）",
    "文献链接": "https://pubmed.ncbi.nlm.nih.gov/36817731/",
    "核实状态/备注": "只含含水量；如需 WTD，应向 SiPALAGA 申请同站水位",
})
row(ID="A11", 类别="原位·公开", **{
    "站点/数据集": "SUSTAINPEAT 小农户系统 48 个样点（GHG + 手测 WTD）",
    "国家": "马来西亚；印尼", "省/州": "雪兰莪北部/南部；西加里曼丹、中加里曼丹",
    "纬度": "见数据集", "经度": "见数据集", "坐标来源": "数据集内",
    "土地利用/状态": "森林、树木种植园、油棕、农田",
    "数据时段": "马来西亚 2018-03 至 2019-02；印尼 2018-05 至 2019-04",
    "时间分辨率": "月（人工）",
    "测量方式/精度": "人工测井读数（通常约 ±1 cm）",
    "站点/井数": "48 个样点、4 个区域",
    "可获取性": "A 公开（诺丁汉大学 RDMC）",
    "数据链接": "https://rdmc.nottingham.ac.uk/handle/internal/10505",
    "原始文献": "Jovani-Sancho et al. 2023, GCB",
    "文献链接": "https://doi.org/10.1111/gcb.16747",
    "核实状态/备注": "已核实",
})
row(ID="A12", 类别="原位·公开（待确认含 WTD）", **{
    "站点/数据集": "Sebungan 油棕种植园 EC 站",
    "国家": "马来西亚", "省/州": "砂拉越（Bintulu 区 Sebauh）",
    "纬度": "3.166", "经度": "113.353",
    "坐标来源": "文献报告的 Sebungan 种植园坐标（3°9.965′N, 113°21.198′E），是否为同一塔位待核实",
    "土地利用/状态": "由择伐泥炭林转为油棕（2006 年种植，泥炭约 4 m）",
    "数据时段": "多年，见原文",
    "时间分辨率": "半小时",
    "测量方式/精度": "EC + 地下水位",
    "站点/井数": "1 塔",
    "可获取性": "A/B（埃克塞特大学 ORE 数据条目）",
    "数据链接": "https://ore.exeter.ac.uk/repository/handle/10871/124993",
    "原始文献": "McCalmont et al. 2021, GCB",
    "文献链接": "https://doi.org/10.1111/gcb.15544",
    "核实状态/备注": "数据条目存在；是否含 WTD 字段待打开确认",
})
row(ID="A13", 类别="原位·公开", **{
    "站点/数据集": "CIFOR SWAMP：中加里曼丹原始泥炭林 + 2 个油棕园",
    "国家": "印尼", "省/州": "中加里曼丹",
    "纬度": "见原文", "经度": "见原文", "坐标来源": "—",
    "土地利用/状态": "原始 PSF；油棕",
    "数据时段": "13 个月（见原文）",
    "时间分辨率": "月 / 日（每个呼吸环）",
    "测量方式/精度": "人工测井 WTD，与土壤呼吸配套",
    "站点/井数": "3 个土地利用",
    "可获取性": "A 公开（CIFOR Dataverse）",
    "数据链接": "https://data.cifor.org/dataset.xhtml?persistentId=doi:10.17528/CIFOR/DATA.00061&version=1.0",
    "原始文献": "Hergoualc'h et al. 2017, Biogeochemistry 135:203–220",
    "文献链接": "https://doi.org/10.1007/s10533-017-0363-4",
    "核实状态/备注": "数据集已核实；WTD 字段名待确认",
})
row(ID="A14", 类别="原位·公开（需在库中查找）", **{
    "站点/数据集": "中加里曼丹森林 vs 小农户油棕（土壤呼吸 + WTD）",
    "国家": "印尼", "省/州": "中加里曼丹",
    "纬度": "见原文", "经度": "见原文", "坐标来源": "—",
    "土地利用/状态": "未排水林；排水油棕",
    "数据时段": "2014-01 至 2015-09（含 2015 厄尔尼诺）",
    "时间分辨率": "月",
    "测量方式/精度": "人工测井",
    "站点/井数": "多个样地",
    "可获取性": "A/B（CIFOR SWAMP GHG Dataverse）",
    "数据链接": "https://data.cifor.org/dataverse.xhtml?alias=swamp-GHGs",
    "原始文献": "Swails et al. 2019, Biogeochemistry 142:37–51；Swails et al. 2019, MASGC（GRACE）",
    "文献链接": "https://doi.org/10.1007/s10533-018-0519-x ; https://doi.org/10.1007/s11027-018-9822-z",
    "核实状态/备注": "论文与时段已核实；具体数据条目待查",
})

# ---------------- B: networks / portals ----------------
row(ID="B1", 类别="监测网络·门户", **{
    "站点/数据集": "SiPALAGA（BRG/BRGM 泥炭地下水位实时监测网）",
    "国家": "印尼",
    "省/州": "7 个优先恢复省（廖内、占碑、南苏门答腊、西加里曼丹、中加里曼丹、南加里曼丹、巴布亚）",
    "纬度": "逐站", "经度": "逐站", "坐标来源": "门户站点信息（站号如 BRG_621103_05）",
    "土地利用/状态": "恢复区、特许经营区、社区土地",
    "数据时段": "约 2017/2018 至今",
    "时间分辨率": "每 10 分钟记录、每小时上传；对外常见为日最小/平均/最大",
    "测量方式/精度": "自动水位（TMAT）+ 土壤湿度 + 雨量 + 气象",
    "站点/井数": "截至 2018 年 12 月约 142 台",
    "可获取性": "B 门户（可访问性和历史数据下载随机构调整；需自行测试或向 BRGM 申请）",
    "数据链接": "https://ptpsw.bppt.go.id/index.php/produk/93-sipalaga",
    "原始文献": "应用例：RSE 2025（中加里曼丹 SBAS-InSAR）；Sci Rep 2025（L 波段 InSAR 评估恢复）；Taufik 2022/2023",
    "文献链接": "https://www.sciencedirect.com/science/article/pii/S0034425725004134 ; https://www.nature.com/articles/s41598-025-08390-8",
    "核实状态/备注": "站数与频率取自 Mongabay 2019 报道：https://www.mongabay.co.id/2019/01/28/brg-kembangkan-sistem-pemantauan-muka-air-gambut/",
})
row(ID="B2", 类别="监测网络·非公开", **{
    "站点/数据集": "SiMATAG-0.4m（KLHK 泥炭地下水位信息系统）",
    "国家": "印尼", "省/州": "全国泥炭区（特许经营区 + 社区土地）",
    "纬度": "逐点", "经度": "逐点", "坐标来源": "系统内",
    "土地利用/状态": "种植园/特许经营区为主",
    "数据时段": "2019 年上线至今",
    "时间分辨率": "定期人工/自动（通过 App 更新）",
    "测量方式/精度": "TMAT 合规监测（阈值 0.4 m）",
    "站点/井数": "9,603 个观测点",
    "可获取性": "C 不公开（监管数据，需与 KLHK 合作）",
    "数据链接": "https://ppid.menlhk.go.id/berita/siaran-pers/4915/menteri-lhk-luncurkan-simatag-04m-untuk-monitoring-keberhasilan-pemulihan-gambut",
    "原始文献": "KLHK 新闻稿 2019",
    "文献链接": "https://www.menlhk.go.id/site/single_post/2151",
    "核实状态/备注": "点数已核实",
})
row(ID="B3", 类别="数据库·注册", **{
    "站点/数据集": "AsiaFlux 数据库（Palangkaraya PDF 等泥炭站）",
    "国家": "印尼等", "省/州": "中加里曼丹",
    "纬度": "见站点页", "经度": "见站点页", "坐标来源": "数据库",
    "土地利用/状态": "泥炭林 / 退化林",
    "数据时段": "见站点页",
    "时间分辨率": "半小时",
    "测量方式/精度": "通量 + 气象（部分含地下水位）",
    "站点/井数": "—",
    "可获取性": "B 注册后下载",
    "数据链接": "https://db.cger.nies.go.jp/asiafluxdb/?page_id=16",
    "原始文献": "Hirano et al.（多篇）",
    "文献链接": "https://doi.org/10.1111/gcb.12653",
    "核实状态/备注": "WTD 是否在数据库中需逐站确认",
})

# ---------------- C: published, data on request ----------------
C = [
    ("C1", "南苏门答腊大尺度复湿试验（257 座坝，4,800 ha）", "印尼", "南苏门答腊（沿海泥炭）",
     "见原文图 1", "见原文图 1", "—", "退役金合欢种植园 + 相邻 PSF",
     "7.5 年监测（见原文）", "测井网络（频率见原文）",
     "水位从约 −0.6 m 升到约 −0.3 m；配套沉降杆", "大量测井",
     "C 论文图表（Data availability 见原文）", "—",
     "Hooijer et al. 2024, Scientific Reports", "https://doi.org/10.1038/s41598-024-60462-3", "已核实"),
    ("C2", "APRIL/RAPP 种植园沉降 + 水位网络（Kampar、Pulau Padang）", "印尼", "廖内",
     "≈0.3–1.1", "≈102.3–102.8", "区域近似", "金合欢种植园、保护林",
     "约 2007–2020（长期）", "月/季人工 + 部分自记",
     "测井 + 沉降杆（数百至上千个）", ">1000 个沉降点",
     "C 企业数据（需与 APRIL/UKCEH 合作）", "—",
     "Evans et al. 2019, Geoderma 338；Evans et al. 2022, Geoderma",
     "https://www.researchgate.net/publication/330075630 ; https://www.sciencedirect.com/science/article/pii/S0016706122004074",
     "时段为约数"),
    ("C3", "Pulau Padang 不同土地利用单元水位站", "印尼", "廖内（Kepulauan Meranti）",
     "≈1.1", "≈102.3", "区域近似", "大型种植园、村庄小尺度排水、PSF",
     "见原文", "自记（多站）",
     "种植园 WTD 深至 −1.8 m，退水速率最高 3.5 cm/d", "多站",
     "C 论文", "—",
     "Ismail et al. 2021, Hydrology Research 52(6):1372；2026 年 J. Hydrol. Reg. Stud. MIKE SHE 建模",
     "https://iwaponline.com/hr/article/52/6/1372/84954/Water-table-variations-on-different-land-use-units ; https://www.sciencedirect.com/science/article/pii/S2214581826000832",
     "已核实"),
    ("C4", "Tebing Tinggi 岛堵渠试验测井", "印尼", "廖内（Kepulauan Meranti）",
     "≈0.9", "≈102.7", "区域近似", "排水泥炭地 / 堵渠恢复区",
     "见原文", "见原文", "3 条横断面上的测井，距渠 1/51/101/201 m", "8 口测井",
     "C 论文", "—", "Sutikno et al. 2020, IOP Conf. Ser. MSE 933",
     "https://iopscience.iop.org/article/10.1088/1757-899X/933/1/012052", "已核实"),
    ("C5", "东加里曼丹未排水泥炭沼泽林（CO2/CH4 + 河流 DOC）", "印尼", "东加里曼丹",
     "见原文", "见原文", "—", "未排水 PSF",
     "2022-10 至 2023-09", "见原文", "WTD 与通量同步观测", "见原文",
     "C 论文", "—", "Asyhari et al. 2024, Scientific Reports",
     "https://doi.org/10.1038/s41598-024-62233-6", "已核实"),
    ("C6", "砂拉越次生泥炭林 → 油棕转换 EC 站", "马来西亚", "砂拉越（Sri Aman 省）",
     "见原文", "见原文", "—", "次生 PSF，后转为油棕",
     "2010 起；9 年 CO2 通量", "半小时", "EC + 地下水位", "1 塔",
     "C 论文（Sarawak TROPI/北海道大学）", "—",
     "Kiew et al. 2018, AFM；Kiew et al. 2025, AFM；Hirano et al. 2025, AGU Advances",
     "https://www.sciencedirect.com/science/article/abs/pii/S0168192317303428 ; https://www.sciencedirect.com/science/article/abs/pii/S0168192325005751 ; https://doi.org/10.1029/2025AV001861",
     "已核实"),
    ("C7", "砂拉越泥炭汇水区 4 站（MA–MD）", "马来西亚", "砂拉越",
     "见原文", "见原文", "—", "泥炭沼泽汇水区",
     "2011–2015", "月（分析尺度）", "水位 + 降水", "4 站",
     "C 论文", "—", "Aeries & Katimon et al. 2023, ASET（UniMAP）",
     "https://ejournal.unimap.edu.my/index.php/aset/article/view/331", "已核实"),
    ("C8", "北雪兰莪泥炭沼泽林地下水位监测", "马来西亚", "雪兰莪（North Selangor PSF / Raja Musa）",
     "≈3.7", "≈101.3", "区域近似", "PSF / 退化林",
     "2013-12 至 2016-12", "月（人工）", "人工测井", "见原文",
     "C 论文", "—", "Lo & Parish 2022",
     "https://www.corpuspublishers.com/assets/articles/aart-v3-22-1029.pdf", "已核实"),
    ("C9", "北雪兰莪 4 类泥炭状况（相机 + 测井）", "马来西亚", "雪兰莪",
     "≈3.7", "≈101.3", "区域近似", "退化林、火烧灌丛、恢复林、小农户油棕",
     "见原文", "亚日（相机）", "延时相机 + 沉降杆", "多站",
     "C 论文", "—", "Ledger et al. 2023, Front. Environ. Sci.",
     "https://doi.org/10.3389/fenvs.2023.1182100", "已核实"),
    ("C10", "中加里曼丹泥炭相机系统（地表运动 + WTD）", "印尼", "中加里曼丹",
     "见原文", "见原文", "—", "森林、火烧迹地、农地、油棕",
     "约 2 年", "亚日", "低成本延时相机；WTD 精度与压力传感器相当", "4 类土地覆盖",
     "C 论文", "—", "Evans et al. 2021, Front. Environ. Sci.",
     "https://doi.org/10.3389/fenvs.2021.630752", "已核实"),
    ("C11", "南苏门答腊 + 中加里曼丹延时相机（泥炭运动与 WTD）", "印尼", "南苏门答腊；中加里曼丹",
     "见原文", "见原文", "—", "4 种土地覆盖",
     "约 1 年", "每 2 小时（与水位记录仪同步）", "相机 + 水位记录仪（R² 0.74–0.95）", "4 站",
     "C 论文", "—", "IOP Conf. Ser. EES 1025 (2022)；另见 IOP EES 1421 (2024)（森林 vs 火烧迹地）",
     "https://iopscience.iop.org/article/10.1088/1755-1315/1025/1/012011 ; https://iopscience.iop.org/article/10.1088/1755-1315/1421/1/012005",
     "已核实"),
    ("C12", "Badas 泥炭穹：火烧 vs 完整 PSF", "文莱", "Belait（Badas）",
     "≈4.6", "≈114.4", "区域近似", "火烧迹地 / 完整 PSF / 受扰动泥炭",
     "见原文", "见原文", "测井 / 测压管", "见原文",
     "C 论文", "—",
     "Lupascu et al. 2020, GCB；Mires and Peat（Badas 地下水监测）",
     "https://doi.org/10.1111/gcb.15195 ; https://www.mires-and-peat.net/article/128750-groundwater-monitoring-geophysical-and-hydrochemical-assessment-of-highly-disturbed-peat-deposits-at-badas-brunei-darussalam.pdf",
     "已核实"),
    ("C13", "Mendaram 测井 + IMERG 降水参数化", "文莱", "Belait",
     "4.367", "114.350", "同 A1", "未排水 PSF",
     "见原文", "自记", "4 口 Levelogger 测井", "4",
     "B/C（原始数据见 A1）", "https://doi.org/10.1594/PANGAEA.908215",
     "Hydrological Processes 2025（hyp.70209）",
     "https://doi.org/10.1002/hyp.70209", "已核实"),
    ("C14", "Pekan（彭亨）堵渠恢复区测井", "马来西亚", "彭亨 Pahang",
     "≈3.3", "≈103.3", "区域近似", "排水 / 堵渠 PSF",
     "约 2010 年代中期", "月", "PVC 简易测井（人工）", "112 根测管 + 16 个渠道水尺",
     "C 会议摘要", "—", "IPC 2016 摘要 A-065",
     "https://peatlands.org/assets/uploads/2019/06/ipc16p467-471a065kasih.simon_.etal_.pdf",
     "时段为约数"),
]
for c in C:
    R.append(list(c[:1]) + ["原位·论文/需申请"] + list(c[1:]))

# ---------------- D: syntheses / gridded products ----------------
D = [
    ("D1", "东南亚林地泥炭 WTD 图（IMERG 驱动，约 25 年逐日）", "东南亚", "区域",
     "格网", "格网", "格网分辨率 10 km", "未排水 PSF（模型）",
     "约 2000–2025", "日", "由 4 个区域未排水 PSF 测井记录率定（测井最远距大渠 2200 m）", "—",
     "A 公开（Mendeley Data）", "https://doi.org/10.17632/69mbg22fxf",
     "Hooijer & Vernimmen 2026, Scientific Reports 16:26515",
     "https://doi.org/10.1038/s41598-026-64641-2", "已核实"),
    ("D2", "PEATCLSM_Trop（天然/排水热带泥炭陆面模型输出）", "泛热带（含东南亚）", "区域",
     "格网", "格网", "格网分辨率 9 km", "天然 + 排水泥炭",
     "见数据集", "日", "用站点水位与 EC 蒸散评估；站点清单见原文", "—",
     "A 公开（Zenodo）", "https://doi.org/10.5281/zenodo.6011689",
     "Apers et al. 2022, JAMES", "https://doi.org/10.1029/2021MS002784",
     "站点表未能打开全文核对"),
    ("D3", "OPTRAM 遥感反演 WTD（Landsat）", "马来西亚、印尼、秘鲁", "砂拉越；中加里曼丹",
     "见原文", "见原文", "—", "排水/未排水/退化/转换",
     "见原文", "Landsat 重访", "用 6 个站点原位 WTD 验证", "6 站",
     "C 论文", "—", "Koupaei-Abyazani et al. 2024, JGR-Biogeosciences",
     "https://doi.org/10.1029/2024JG008116", "已核实"),
    ("D4", "GSMaP 驱动的区域地下水位图 + CO2/CH4 排放", "东南亚", "约 18 万 km² 泥炭",
     "格网", "格网", "—", "多土地利用",
     "见原文", "月", "用 Palangkaraya 与砂拉越站点率定", "—",
     "C 论文（见 SI）", "—",
     "Hirano et al. 2025, AGU Advances；Cochrane et al. 2026, AGU Advances",
     "https://doi.org/10.1029/2025AV001861 ; https://doi.org/10.1029/2025AV002260", "已核实"),
    ("D5", "东南亚 16 个 EC 站综合（112 站年，含泥炭站）", "东南亚", "—",
     "见原文", "见原文", "—", "原始林 → 次生林 → 种植园",
     "多年", "半小时", "通量综合（WTD 不一定都有）", "16 站",
     "C 论文", "—", "Hanggara et al. 2026, GCB",
     "https://doi.org/10.1111/gcb.70753", "已核实"),
    ("D6", "印尼泥炭统一数据集 v0.1（+ EPIC 模拟月 WTD 2001–2010）", "印尼", "全国",
     "格网", "格网", "格网分辨率 0.25°", "泥炭类型 / 模拟 WTD",
     "2001–2010（模拟）", "月", "模型输出，不是观测", "—",
     "A 公开（Zenodo）", "https://zenodo.org/records/6998052",
     "IIASA（Balkovič 等）", "https://pure.iiasa.ac.at/id/eprint/18393/",
     "WTD 模拟结果所在的具体 Zenodo 条目待核实"),
    ("D7", "热带泥炭排水与 CO2/N2O 的 meta 分析（站点平均 WTD）", "泛热带（以东南亚为主）", "—",
     "见补充材料", "见补充材料", "—", "多土地利用",
     "文献汇编", "站点平均", "来自文献", "多站",
     "A/C（补充材料）", "—", "Prananto et al. 2020, GCB",
     "https://doi.org/10.1111/gcb.15147", "已核实"),
    ("D8", "SMAP 泥炭土壤湿度神经网络（WTD 代理变量）", "东南亚", "—",
     "格网", "格网", "格网分辨率 9–36 km", "—",
     "2015 起", "日", "土壤湿度，不是 WTD", "—",
     "A 公开（Zenodo 代码与数据）", "https://zenodo.org/records/6740137",
     "Dadap et al. 2022, ERL", "https://doi.org/10.1088/1748-9326/ac7969", "已核实"),
]
for d in D:
    R.append(list(d[:1]) + ["汇编/格网产品"] + list(d[1:]))

GAPS = [
    ("泰国", "Kuan Kreng（洛坤/博他仑/宋卡）、To Daeng（Princess Sirindhorn PSF）", "只找到 DEM 水文/防火研究和 UNDP 项目文件，未见公开的连续 WTD 时间序列", "https://zenodo.org/records/14869357"),
    ("越南", "U Minh Thuong / U Minh Ha（金瓯、坚江）", "只有洪水与水质研究，以及区域地下水（非泥炭潜水）监测井；未见泥炭 WTD 公开数据", "https://www.researchgate.net/publication/343310013_Effect_of_flooding_on_peatland_in_U_Minh_Thuong_National_Park_Vietnam"),
    ("菲律宾", "Leyte Sab-a Basin、Agusan Marsh（Caimpugan）", "只有土地利用与水位高低的定性对比和一次性采样", "https://www.mires-and-peat.net/article/128855-effects-of-land-use-conversion-on-selected-physico-chemical-properties-of-peat-in-the-leyte-sab-a-basin-peatland-philippines/attachment/263082.pdf"),
    ("马来西亚沙巴", "Klias / Binsuluk", "只有恢复项目与生物多样性调查，未见近十年 WTD 时序", "https://gec.org.my/reference-project/biodiversity-data-collection-in-klias-forest-reserve-and-binsuluk-forest-reserve-restoration-area-in-beaufort-sabah/"),
]


def write_csv():
    p = OUT / "SEA_peatland_WTD_datasets.csv"
    with p.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(COLS)
        w.writerows(R)
    return p


def md_link(s):
    parts = [x.strip() for x in s.split(" ; ") if x.strip()]
    out = []
    for i, u in enumerate(parts, 1):
        if u.startswith("http"):
            label = u.replace("https://doi.org/", "doi:") if "doi.org" in u else "链接"
            out.append(f"[{label}]({u})")
        else:
            out.append(u)
    return "<br>".join(out) if out else "—"


def esc(s):
    return s.replace("|", "\\|")


def write_md():
    idx = {c: i for i, c in enumerate(COLS)}
    lines = []
    lines.append("# 东南亚泥炭地地下水位埋深（WTD）数据清单（2016–2026 文献）\n")
    lines.append("> 整理日期：2026-09-25。CSV 为全字段版本（同目录 `SEA_peatland_WTD_datasets.csv`）。\n")
    lines.append("**可获取性等级**：A = 公开仓库可直接下载；B = 门户/注册/需申请；C = 仅见于论文图表，需联系作者或机构。\n")
    lines.append("**坐标**：写明“文献/元数据”的为原文或数据集给出的值；带“≈”的是区域近似值，写论文前请用原文 SI 或数据集元数据替换。\n")
    lines.append("**精度**：列出时间分辨率和测量方式。仪器标称精度只在原文写明型号时给出，例如 Solinst Levelogger Edge 为 ±0.05% FS；人工测井一般约 ±1 cm（经验值）。\n")

    sections = [
        ("A. 原位观测：公开可下载", "A"),
        ("B. 国家/区域监测网络与数据库", "B"),
        ("C. 原位观测：已发表，数据需申请", "C"),
        ("D. 汇编、遥感与格网产品（可用于验证或插值，不是原位观测）", "D"),
    ]
    head = "| ID | 站点/数据集 | 国家 · 省/州 | 纬度, 经度（来源） | 土地利用 | 时段 | 分辨率 / 精度 | 可获取性 | 数据链接 | 原始文献 |"
    sep = "|---|---|---|---|---|---|---|---|---|---|"
    for title, pre in sections:
        lines.append(f"\n## {title}\n")
        lines.append(head)
        lines.append(sep)
        for r in R:
            if not r[0].startswith(pre):
                continue
            g = lambda c: esc(r[idx[c]])
            la, lo = g('纬度').split('；'), g('经度').split('；')
            if len(la) > 1 and len(la) == len(lo):
                pairs = []
                for a, b in zip(la, lo):
                    name, _, va = a.strip().rpartition(' ')
                    _, _, vb = b.strip().rpartition(' ')
                    pairs.append(f"{name} ({va}, {vb})")
                coord = "；".join(pairs) + f"（{g('坐标来源')}）"
            else:
                coord = f"{g('纬度')}, {g('经度')}（{g('坐标来源')}）"
            res = f"{g('时间分辨率')}；{g('测量方式/精度')}；{g('站点/井数')}"
            lit = f"{g('原始文献')}<br>{md_link(r[idx['文献链接']])}"
            note = g("核实状态/备注")
            lit_full = lit + (f"<br>*{note}*" if note else "")
            lines.append(
                f"| {g('ID')} | {g('站点/数据集')} | {g('国家')} · {g('省/州')} | {coord} | {g('土地利用/状态')} | {g('数据时段')} | {res} | {g('可获取性')} | {md_link(r[idx['数据链接']])} | {lit_full} |"
            )

    lines.append("\n## E. 数据空白（近十年文献中未找到公开的连续 WTD）\n")
    lines.append("| 国家/地区 | 泥炭地 | 现状 | 参考 |")
    lines.append("|---|---|---|---|")
    for g in GAPS:
        lines.append(f"| {g[0]} | {g[1]} | {g[2]} | [链接]({g[3]}) |")

    lines.append("\n## 使用建议\n")
    lines.append("1. **高频、开放、能直接用来建模或率定**：A1/A2（文莱 Mendaram，未排水穹顶）、A3/A4/A5（Palangkaraya 扰动梯度）、A7/A8（Riau Kampar 三种土地利用）、A9（占碑 + 西加里曼丹 8 站日值）。这几套覆盖了未排水、排水、火烧、种植园四类状态。")
    lines.append("2. **空间覆盖最广**：B1 SiPALAGA（约 142 站，小时级）。需要自己测试门户能否访问，或正式向 BRGM 申请；RSE 2025、Sci Rep 2025 等论文已用到具体站号（如 BRG_621103_05），可顺着这些站号查。")
    lines.append("3. **多土地利用的月尺度手测**：A11（48 个样点，马来西亚 + 印尼）适合做 WTD 与 GHG 的关系分析。")
    lines.append("4. **未排水 PSF 的“自然 WTD 基线”**：D1（Hooijer & Vernimmen 2026）给出 10 km 逐日 WTD 图，适合作为恢复目标的参考。")
    lines.append("5. **写论文前必须补的信息**：带“≈”的坐标、A6 中 FLUXNET-CH4 子集的年份、A12 是否含 WTD、D2 的站点表。本次运行环境无法打开出版社和数据仓库全文，这些字段只核到检索摘要这一层。")
    p = OUT / "SEA_peatland_WTD_datasets.md"
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return p


if __name__ == "__main__":
    print(write_csv())
    print(write_md())
    print(len(R), "rows")
