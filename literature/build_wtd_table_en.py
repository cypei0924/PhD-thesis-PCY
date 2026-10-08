# -*- coding: utf-8 -*-
"""Generate the English SE Asian peatland WTD dataset inventory (CSV + Markdown).

English counterpart of build_wtd_table.py; keep the two in sync when editing rows.
"""
import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent

COLS = [
    "ID", "Category", "Site / dataset", "Country", "Province / state",
    "Latitude", "Longitude", "Coordinate source", "Land use / condition",
    "Period", "Temporal resolution", "Method / accuracy", "Sites / wells",
    "Availability", "Data link", "Source publication(s)", "Publication link(s)",
    "Verification / notes",
]

R = []
def row(**kw):
    R.append([kw.get(c, "") for c in COLS])

# ---------------- A: in situ, openly downloadable ----------------
row(**{
    "ID": "A1", "Category": "In situ · open",
    "Site / dataset": "Mendaram peat dome hydrologic data (PANGAEA dataset series)",
    "Country": "Brunei", "Province / state": "Belait (Ulu Mendaram Conservation Area)",
    "Latitude": "4.367", "Longitude": "114.350",
    "Coordinate source": "Literature (4°22′N, 114°21′E)",
    "Land use / condition": "Pristine, undrained peat swamp forest (peat dome, ~40 km²)",
    "Period": "2012–2013 (dataset title)",
    "Temporal resolution": "Continuous logger (interval: see dataset)",
    "Method / accuracy": "Solinst Levelogger Edge pressure transducers + Barologger barometric correction (manufacturer spec ±0.05% FS); also Ks, Sy and throughfall",
    "Sites / wells": "4 dipwells + 4 rain gauges",
    "Availability": "A – open (PANGAEA)",
    "Data link": "https://doi.org/10.1594/PANGAEA.908215",
    "Source publication(s)": "Cobb & Harvey 2019, WRR; Cobb et al. 2017, PNAS",
    "Publication link(s)": "https://doi.org/10.1029/2019WR025411 ; https://doi.org/10.1073/pnas.1701090114",
    "Verification / notes": "Dataset entry and instruments verified; licence not checked",
})
row(**{
    "ID": "A2", "Category": "In situ · open",
    "Site / dataset": "Mendaram water table + CO2 + temperature time series",
    "Country": "Brunei", "Province / state": "Belait (Ulu Mendaram)",
    "Latitude": "4.367", "Longitude": "114.350",
    "Coordinate source": "Same as A1 (literature)",
    "Land use / condition": "Undrained peat swamp forest",
    "Period": "WTD: 2012-02-06 to 2015-02-06",
    "Temporal resolution": "Continuous logger",
    "Method / accuracy": "Same logger network as A1",
    "Sites / wells": "See dataset",
    "Availability": "A – open (Zenodo)",
    "Data link": "https://zenodo.org/records/3245335",
    "Source publication(s)": "Hoyt et al. 2019, GCB",
    "Publication link(s)": "https://doi.org/10.1111/gcb.14702",
    "Verification / notes": "Period verified",
})
row(**{
    "ID": "A3", "Category": "In situ · open",
    "Site / dataset": "Palangkaraya flux sites UF/DF/DB (CO2 flux + meteorology + groundwater level)",
    "Country": "Indonesia", "Province / state": "Central Kalimantan",
    "Latitude": "UF −2.32; DB −2.34; DF ≈−2.34",
    "Longitude": "UF 113.90; DB 114.04; DF ≈114.04",
    "Coordinate source": "UF from FLUXNET-CH4 metadata; DB from literature; DF approximated (three sites lie within 15 km of each other)",
    "Land use / condition": "UF: largely undrained forest; DF: heavily drained forest; DB: drained and burnt",
    "Period": "c. 2002–2017 (12–15 years per site; per-site dates in SI)",
    "Temporal resolution": "Flux half-hourly; groundwater level daily or finer",
    "Method / accuracy": "Water level logger (model: see paper)",
    "Sites / wells": "3 sites",
    "Availability": "A – open (figshare share link)",
    "Data link": "https://figshare.com/s/6aefe20137486d0a6f62",
    "Source publication(s)": "Hirano et al. 2024, Communications Earth & Environment",
    "Publication link(s)": "https://doi.org/10.1038/s43247-024-01387-7",
    "Verification / notes": "Data link verified; per-site years to be checked in SI",
})
row(**{
    "ID": "A4", "Category": "In situ · open",
    "Site / dataset": "DailyGWL.xlsx: daily groundwater level, undrained/drained peat swamp forest, Palangkaraya",
    "Country": "Indonesia", "Province / state": "Central Kalimantan",
    "Latitude": "≈−2.3", "Longitude": "≈113.9–114.0",
    "Coordinate source": "Regional approximation (same area as A3)",
    "Land use / condition": "Undrained PSF; drained PSF",
    "Period": "Undrained 2015–2018; drained 2013–2017",
    "Temporal resolution": "Daily",
    "Method / accuracy": "Water level logger",
    "Sites / wells": "2 sites",
    "Availability": "A – open (figshare)",
    "Data link": "https://figshare.com/articles/dataset/DailyGWL_xlsx/22321129/1",
    "Source publication(s)": "Hirano group data; probably used by Koupaei-Abyazani et al. 2024 (IN-undrained / IN-drained sites)",
    "Publication link(s)": "https://doi.org/10.1029/2024JG008116",
    "Verification / notes": "Data and period verified; linked paper not confirmed",
})
row(**{
    "ID": "A5", "Category": "In situ · open",
    "Site / dataset": "FLUXNET-CH4 ID-Pag (Palangkaraya undrained forest)",
    "Country": "Indonesia", "Province / state": "Central Kalimantan",
    "Latitude": "−2.32", "Longitude": "113.90",
    "Coordinate source": "Dataset metadata",
    "Land use / condition": "Undrained peat swamp forest",
    "Period": "2016–2017",
    "Temporal resolution": "Half-hourly / daily (FLUXNET format)",
    "Method / accuracy": "Eddy covariance (EC) flux; check after download whether a WTD variable is included",
    "Sites / wells": "1 tower",
    "Availability": "A – open (FLUXNET-CH4, CC-BY 4.0)",
    "Data link": "https://doi.org/10.18140/FLX/1669643",
    "Source publication(s)": "Sakabe et al. 2018, GCB; Delwiche et al. 2021, ESSD",
    "Publication link(s)": "https://doi.org/10.1111/gcb.14410 ; https://doi.org/10.5194/essd-13-3607-2021",
    "Verification / notes": "Coordinates and years verified",
})
row(**{
    "ID": "A6", "Category": "In situ · open",
    "Site / dataset": "FLUXNET-CH4 MY-MLM (Maludam National Park)",
    "Country": "Malaysia", "Province / state": "Sarawak (Betong)",
    "Latitude": "1.4536", "Longitude": "111.1495",
    "Coordinate source": "Dataset metadata",
    "Land use / condition": "Primary peat swamp forest (peat ~8 m thick)",
    "Period": "FLUXNET-CH4 subset years: see data page; CO2 and water table at the same site 2011–2014 (Tang 2020)",
    "Temporal resolution": "Half-hourly",
    "Method / accuracy": "EC flux + groundwater level",
    "Sites / wells": "1 tower",
    "Availability": "A – open (FLUXNET-CH4 subset); full 2011–2014 record on request from Sarawak TROPI",
    "Data link": "https://doi.org/10.18140/FLX/1669650",
    "Source publication(s)": "Tang et al. 2018, GRL; Tang et al. 2020, GCB",
    "Publication link(s)": "https://doi.org/10.1029/2017GL076457 ; https://doi.org/10.1111/gcb.15332",
    "Verification / notes": "Coordinates verified; FLUXNET-CH4 subset years not verified",
})
row(**{
    "ID": "A7", "Category": "In situ · open",
    "Site / dataset": "Kampar Peninsula: intact vs degraded forest (EC + groundwater level)",
    "Country": "Indonesia", "Province / state": "Riau",
    "Latitude": "≈0.3", "Longitude": "≈102.8",
    "Coordinate source": "Regional approximation (tower coordinates in paper SI)",
    "Land use / condition": "Intact peat forest; degraded forest",
    "Period": "Mid-2017 to mid-2020",
    "Temporal resolution": "Half-hourly (EC); continuous groundwater level",
    "Method / accuracy": "Water level logger (model: see paper)",
    "Sites / wells": "2 towers",
    "Availability": "A – open (Zenodo)",
    "Data link": "https://doi.org/10.5281/zenodo.4835696",
    "Source publication(s)": "Deshmukh et al. 2021, Nature Geoscience",
    "Publication link(s)": "https://doi.org/10.1038/s41561-021-00785-2",
    "Verification / notes": "Zenodo record and period verified",
})
row(**{
    "ID": "A8", "Category": "In situ · open",
    "Site / dataset": "Kampar Peninsula: Acacia plantation / degraded forest / intact forest",
    "Country": "Indonesia", "Province / state": "Riau",
    "Latitude": "≈0.3", "Longitude": "≈102.8",
    "Coordinate source": "Regional approximation (tower coordinates in paper SI)",
    "Land use / condition": "Acacia crassicarpa plantation; degraded forest; intact forest",
    "Period": "2016-10 to 2022-05 (plantation EC to 2021-05; intact forest EC from 2017-06)",
    "Temporal resolution": "Half-hourly (EC); continuous groundwater level",
    "Method / accuracy": "Water level logger",
    "Sites / wells": "3 towers",
    "Availability": "A – open (Zenodo)",
    "Data link": "https://zenodo.org/records/7500659",
    "Source publication(s)": "Deshmukh et al. 2023, Nature; Deshmukh et al. 2020, GCB",
    "Publication link(s)": "https://doi.org/10.1038/s41586-023-05860-9 ; https://doi.org/10.1111/gcb.15019",
    "Verification / notes": "Verified",
})
row(**{
    "ID": "A9", "Category": "In situ · open",
    "Site / dataset": "Indonesian peatland groundwater table + water retention dataset (8 stations)",
    "Country": "Indonesia", "Province / state": "Jambi (Batanghari); West Kalimantan (Kubu Raya)",
    "Latitude": "Batanghari ≈−1.7; Kubu Raya ≈−0.4",
    "Longitude": "Batanghari ≈103.1; Kubu Raya ≈109.4",
    "Coordinate source": "Regional approximation (per-station coordinates in the paper's table)",
    "Land use / condition": "Human-modified / degraded peatland",
    "Period": "2018–2019",
    "Temporal resolution": "Daily",
    "Method / accuracy": "Automatic stations (groundwater level, rainfall, soil moisture)",
    "Sites / wells": "8 stations",
    "Availability": "A – open (Data in Brief supplement, Excel)",
    "Data link": "https://www.sciencedirect.com/science/article/pii/S2352340922001159",
    "Source publication(s)": "Taufik et al. 2022, Data in Brief 41 (doi:10.1016/j.dib.2022.107903)",
    "Publication link(s)": "https://pubmed.ncbi.nlm.nih.gov/35198682/",
    "Verification / notes": "Station count and period verified; DOI taken from search summary",
})
row(**{
    "ID": "A10", "Category": "In situ · open (related variable)",
    "Site / dataset": "Sumatra peat moisture dataset (21 stations)",
    "Country": "Indonesia", "Province / state": "Three provinces in Sumatra",
    "Latitude": "See paper", "Longitude": "See paper",
    "Coordinate source": "—",
    "Land use / condition": "Human-modified peatland",
    "Period": "2018–2019",
    "Temporal resolution": "Daily",
    "Method / accuracy": "Soil moisture content (not WTD); stations linked to SiPALAGA",
    "Sites / wells": "21 stations",
    "Availability": "A – open (Data in Brief)",
    "Data link": "https://www.sciencedirect.com/science/article/pii/S2352340923000070",
    "Source publication(s)": "Taufik et al. 2023, Data in Brief (doi:10.1016/j.dib.2023.108889)",
    "Publication link(s)": "https://pubmed.ncbi.nlm.nih.gov/36817731/",
    "Verification / notes": "Moisture only; for WTD, request the same stations' water levels from SiPALAGA",
})
row(**{
    "ID": "A11", "Category": "In situ · open",
    "Site / dataset": "SUSTAINPEAT smallholder systems, 48 sites (GHG + manual WTD)",
    "Country": "Malaysia; Indonesia",
    "Province / state": "North & South Selangor; West & Central Kalimantan",
    "Latitude": "See dataset", "Longitude": "See dataset",
    "Coordinate source": "In dataset",
    "Land use / condition": "Forest, tree plantation, oil palm, cropland",
    "Period": "Malaysia 2018-03 to 2019-02; Indonesia 2018-05 to 2019-04",
    "Temporal resolution": "Monthly (manual)",
    "Method / accuracy": "Manual dipwell readings (typically about ±1 cm)",
    "Sites / wells": "48 sites in 4 regions",
    "Availability": "A – open (University of Nottingham RDMC)",
    "Data link": "https://rdmc.nottingham.ac.uk/handle/internal/10505",
    "Source publication(s)": "Jovani-Sancho et al. 2023, GCB",
    "Publication link(s)": "https://doi.org/10.1111/gcb.16747",
    "Verification / notes": "Verified",
})
row(**{
    "ID": "A12", "Category": "In situ · open (WTD content unconfirmed)",
    "Site / dataset": "Sebungan oil palm plantation EC site",
    "Country": "Malaysia", "Province / state": "Sarawak (Sebauh, Bintulu district)",
    "Latitude": "3.166", "Longitude": "113.353",
    "Coordinate source": "Published Sebungan plantation coordinates (3°9.965′N, 113°21.198′E); same tower position not confirmed",
    "Land use / condition": "Logged peat swamp forest converted to oil palm (planted 2006; peat ~4 m)",
    "Period": "Multi-year, see paper",
    "Temporal resolution": "Half-hourly",
    "Method / accuracy": "EC + groundwater level",
    "Sites / wells": "1 tower",
    "Availability": "A/B (University of Exeter ORE data entry)",
    "Data link": "https://ore.exeter.ac.uk/repository/handle/10871/124993",
    "Source publication(s)": "McCalmont et al. 2021, GCB",
    "Publication link(s)": "https://doi.org/10.1111/gcb.15544",
    "Verification / notes": "Data entry exists; whether it contains a WTD field still to be checked",
})
row(**{
    "ID": "A13", "Category": "In situ · open",
    "Site / dataset": "CIFOR SWAMP: Central Kalimantan primary peat forest + 2 oil palm plantations",
    "Country": "Indonesia", "Province / state": "Central Kalimantan",
    "Latitude": "See paper", "Longitude": "See paper",
    "Coordinate source": "—",
    "Land use / condition": "Primary PSF; oil palm",
    "Period": "13 months (see paper)",
    "Temporal resolution": "Monthly / daily (per respiration collar)",
    "Method / accuracy": "Manual dipwell WTD alongside soil respiration",
    "Sites / wells": "3 land uses",
    "Availability": "A – open (CIFOR Dataverse)",
    "Data link": "https://data.cifor.org/dataset.xhtml?persistentId=doi:10.17528/CIFOR/DATA.00061&version=1.0",
    "Source publication(s)": "Hergoualc'h et al. 2017, Biogeochemistry 135:203–220",
    "Publication link(s)": "https://doi.org/10.1007/s10533-017-0363-4",
    "Verification / notes": "Dataset verified; WTD field name to be confirmed",
})
row(**{
    "ID": "A14", "Category": "In situ · open (locate in repository)",
    "Site / dataset": "Central Kalimantan forest vs smallholder oil palm (soil respiration + WTD)",
    "Country": "Indonesia", "Province / state": "Central Kalimantan",
    "Latitude": "See paper", "Longitude": "See paper",
    "Coordinate source": "—",
    "Land use / condition": "Undrained forest; drained oil palm",
    "Period": "2014-01 to 2015-09 (includes 2015 El Niño)",
    "Temporal resolution": "Monthly",
    "Method / accuracy": "Manual dipwells",
    "Sites / wells": "Several plots",
    "Availability": "A/B (CIFOR SWAMP GHG Dataverse)",
    "Data link": "https://data.cifor.org/dataverse.xhtml?alias=swamp-GHGs",
    "Source publication(s)": "Swails et al. 2019, Biogeochemistry 142:37–51; Swails et al. 2019, MASGC (GRACE)",
    "Publication link(s)": "https://doi.org/10.1007/s10533-018-0519-x ; https://doi.org/10.1007/s11027-018-9822-z",
    "Verification / notes": "Papers and period verified; specific data entry still to be located",
})

# ---------------- B: networks / portals ----------------
row(**{
    "ID": "B1", "Category": "Monitoring network · portal",
    "Site / dataset": "SiPALAGA (BRG/BRGM real-time peatland water level monitoring network)",
    "Country": "Indonesia",
    "Province / state": "7 priority restoration provinces (Riau, Jambi, South Sumatra, West Kalimantan, Central Kalimantan, South Kalimantan, Papua)",
    "Latitude": "Per station", "Longitude": "Per station",
    "Coordinate source": "Portal station metadata (station IDs such as BRG_621103_05)",
    "Land use / condition": "Restoration areas, concessions, community land",
    "Period": "c. 2017/2018 to present",
    "Temporal resolution": "Logged every 10 min, uploaded hourly; commonly distributed as daily min/mean/max",
    "Method / accuracy": "Automatic water level (TMAT) + soil moisture + rainfall + meteorology",
    "Sites / wells": "About 142 units by December 2018",
    "Availability": "B – portal (access and historical downloads change with the agency; test it yourself or request from BRGM)",
    "Data link": "https://ptpsw.bppt.go.id/index.php/produk/93-sipalaga",
    "Source publication(s)": "Examples of use: RSE 2025 (Central Kalimantan SBAS-InSAR); Sci Rep 2025 (L-band InSAR restoration assessment); Taufik 2022/2023",
    "Publication link(s)": "https://www.sciencedirect.com/science/article/pii/S0034425725004134 ; https://www.nature.com/articles/s41598-025-08390-8",
    "Verification / notes": "Station count and frequency from a 2019 Mongabay report: https://www.mongabay.co.id/2019/01/28/brg-kembangkan-sistem-pemantauan-muka-air-gambut/",
})
row(**{
    "ID": "B2", "Category": "Monitoring network · not public",
    "Site / dataset": "SiMATAG-0.4m (KLHK peatland groundwater level information system)",
    "Country": "Indonesia", "Province / state": "National peatland area (concessions + community land)",
    "Latitude": "Per point", "Longitude": "Per point",
    "Coordinate source": "In system",
    "Land use / condition": "Mainly plantations / concessions",
    "Period": "Launched 2019 to present",
    "Temporal resolution": "Periodic manual/automatic (updated through a mobile app)",
    "Method / accuracy": "TMAT compliance monitoring (0.4 m threshold)",
    "Sites / wells": "9,603 observation points",
    "Availability": "C – not public (regulatory data; requires collaboration with KLHK)",
    "Data link": "https://ppid.menlhk.go.id/berita/siaran-pers/4915/menteri-lhk-luncurkan-simatag-04m-untuk-monitoring-keberhasilan-pemulihan-gambut",
    "Source publication(s)": "KLHK press release 2019",
    "Publication link(s)": "https://www.menlhk.go.id/site/single_post/2151",
    "Verification / notes": "Point count verified",
})
row(**{
    "ID": "B3", "Category": "Database · registration",
    "Site / dataset": "AsiaFlux database (Palangkaraya PDF and other peat sites)",
    "Country": "Indonesia and others", "Province / state": "Central Kalimantan",
    "Latitude": "See site page", "Longitude": "See site page",
    "Coordinate source": "Database",
    "Land use / condition": "Peat forest / degraded forest",
    "Period": "See site page",
    "Temporal resolution": "Half-hourly",
    "Method / accuracy": "Flux + meteorology (some sites include groundwater level)",
    "Sites / wells": "—",
    "Availability": "B – download after registration",
    "Data link": "https://db.cger.nies.go.jp/asiafluxdb/?page_id=16",
    "Source publication(s)": "Hirano et al. (several papers)",
    "Publication link(s)": "https://doi.org/10.1111/gcb.12653",
    "Verification / notes": "Whether WTD is in the database must be checked site by site",
})

# ---------------- C: published, data on request ----------------
# Tuple order: ID, site, country, province, lat, lon, coord source, land use, period,
# resolution, method, sites, availability, data link, publication, publication link, notes
C = [
    ("C1", "South Sumatra large-scale rewetting trial (257 dams, 4,800 ha)", "Indonesia", "South Sumatra (coastal peat)",
     "See paper Fig. 1", "See paper Fig. 1", "—", "Retired Acacia plantation + adjacent PSF",
     "7.5 years of monitoring (see paper)", "Dipwell network (frequency: see paper)",
     "Water table raised from about −0.6 m to about −0.3 m; paired subsidence poles", "Many dipwells",
     "C – figures in paper (see Data availability statement)", "—",
     "Hooijer et al. 2024, Scientific Reports", "https://doi.org/10.1038/s41598-024-60462-3", "Verified"),
    ("C2", "APRIL/RAPP plantation subsidence + water table network (Kampar, Pulau Padang)", "Indonesia", "Riau",
     "≈0.3–1.1", "≈102.3–102.8", "Regional approximation", "Acacia plantations, conservation forest",
     "c. 2007–2020 (long-term)", "Monthly/quarterly manual + some loggers",
     "Dipwells + subsidence poles (hundreds to over a thousand)", ">1,000 subsidence points",
     "C – company data (requires collaboration with APRIL/UKCEH)", "—",
     "Evans et al. 2019, Geoderma 338; Evans et al. 2022, Geoderma",
     "https://www.researchgate.net/publication/330075630 ; https://www.sciencedirect.com/science/article/pii/S0016706122004074",
     "Period approximate"),
    ("C3", "Pulau Padang water level stations across land-use units", "Indonesia", "Riau (Kepulauan Meranti)",
     "≈1.1", "≈102.3", "Regional approximation", "Large plantations, village-scale drainage, PSF",
     "See paper", "Logger (multiple stations)",
     "Plantation WTD down to −1.8 m; recession rate up to 3.5 cm/day", "Multiple stations",
     "C – paper", "—",
     "Ismail et al. 2021, Hydrology Research 52(6):1372; 2026 J. Hydrol. Reg. Stud. (MIKE SHE modelling)",
     "https://iwaponline.com/hr/article/52/6/1372/84954/Water-table-variations-on-different-land-use-units ; https://www.sciencedirect.com/science/article/pii/S2214581826000832",
     "Verified"),
    ("C4", "Tebing Tinggi Island canal-blocking dipwells", "Indonesia", "Riau (Kepulauan Meranti)",
     "≈0.9", "≈102.7", "Regional approximation", "Drained peatland / canal-blocked restoration area",
     "See paper", "See paper", "Dipwells on 3 transects at 1/51/101/201 m from the canal", "8 dipwells",
     "C – paper", "—", "Sutikno et al. 2020, IOP Conf. Ser. MSE 933",
     "https://iopscience.iop.org/article/10.1088/1757-899X/933/1/012052", "Verified"),
    ("C5", "East Kalimantan undrained peat swamp forest (CO2/CH4 + fluvial DOC)", "Indonesia", "East Kalimantan",
     "See paper", "See paper", "—", "Undrained PSF",
     "2022-10 to 2023-09", "See paper", "WTD measured alongside fluxes", "See paper",
     "C – paper", "—", "Asyhari et al. 2024, Scientific Reports",
     "https://doi.org/10.1038/s41598-024-62233-6", "Verified"),
    ("C6", "Sarawak secondary peat forest → oil palm conversion EC site", "Malaysia", "Sarawak (Sri Aman Division)",
     "See paper", "See paper", "—", "Secondary PSF, later converted to oil palm",
     "From 2010; 9 years of CO2 flux", "Half-hourly", "EC + groundwater level", "1 tower",
     "C – paper (Sarawak TROPI / Hokkaido University)", "—",
     "Kiew et al. 2018, AFM; Kiew et al. 2025, AFM; Hirano et al. 2025, AGU Advances",
     "https://www.sciencedirect.com/science/article/abs/pii/S0168192317303428 ; https://www.sciencedirect.com/science/article/abs/pii/S0168192325005751 ; https://doi.org/10.1029/2025AV001861",
     "Verified"),
    ("C7", "Sarawak peat catchment, 4 stations (MA–MD)", "Malaysia", "Sarawak",
     "See paper", "See paper", "—", "Peat swamp catchment",
     "2011–2015", "Monthly (analysis scale)", "Water table + precipitation", "4 stations",
     "C – paper", "—", "Aeries & Katimon et al. 2023, ASET (UniMAP)",
     "https://ejournal.unimap.edu.my/index.php/aset/article/view/331", "Verified"),
    ("C8", "North Selangor peat swamp forest groundwater monitoring", "Malaysia", "Selangor (North Selangor PSF / Raja Musa)",
     "≈3.7", "≈101.3", "Regional approximation", "PSF / degraded forest",
     "2013-12 to 2016-12", "Monthly (manual)", "Manual dipwells", "See paper",
     "C – paper", "—", "Lo & Parish 2022",
     "https://www.corpuspublishers.com/assets/articles/aart-v3-22-1029.pdf", "Verified"),
    ("C9", "North Selangor, 4 peat condition classes (cameras + dipwells)", "Malaysia", "Selangor",
     "≈3.7", "≈101.3", "Regional approximation", "Degraded forest, burnt scrub, recovering forest, smallholder oil palm",
     "See paper", "Sub-daily (camera)", "Time-lapse cameras + subsidence poles", "Multiple stations",
     "C – paper", "—", "Ledger et al. 2023, Front. Environ. Sci.",
     "https://doi.org/10.3389/fenvs.2023.1182100", "Verified"),
    ("C10", "Central Kalimantan peat camera system (surface motion + WTD)", "Indonesia", "Central Kalimantan",
     "See paper", "See paper", "—", "Forest, burnt area, agriculture, oil palm",
     "About 2 years", "Sub-daily", "Low-cost time-lapse cameras; WTD quality comparable to pressure transducers", "4 land-cover types",
     "C – paper", "—", "Evans et al. 2021, Front. Environ. Sci.",
     "https://doi.org/10.3389/fenvs.2021.630752", "Verified"),
    ("C11", "South Sumatra + Central Kalimantan time-lapse cameras (peat motion and WTD)", "Indonesia", "South Sumatra; Central Kalimantan",
     "See paper", "See paper", "—", "4 land-cover types",
     "About 1 year", "Every 2 hours (synchronised with water level logger)", "Camera + water level logger (R² 0.74–0.95)", "4 stations",
     "C – paper", "—", "IOP Conf. Ser. EES 1025 (2022); see also IOP EES 1421 (2024) (forest vs burnt area)",
     "https://iopscience.iop.org/article/10.1088/1755-1315/1025/1/012011 ; https://iopscience.iop.org/article/10.1088/1755-1315/1421/1/012005",
     "Verified"),
    ("C12", "Badas peat dome: burnt vs intact PSF", "Brunei", "Belait (Badas)",
     "≈4.6", "≈114.4", "Regional approximation", "Burnt area / intact PSF / disturbed peat",
     "See paper", "See paper", "Dipwells / piezometers", "See paper",
     "C – paper", "—",
     "Lupascu et al. 2020, GCB; Mires and Peat (Badas groundwater monitoring)",
     "https://doi.org/10.1111/gcb.15195 ; https://www.mires-and-peat.net/article/128750-groundwater-monitoring-geophysical-and-hydrochemical-assessment-of-highly-disturbed-peat-deposits-at-badas-brunei-darussalam.pdf",
     "Verified"),
    ("C13", "Mendaram dipwells + IMERG rainfall parameterisation", "Brunei", "Belait",
     "4.367", "114.350", "Same as A1", "Undrained PSF",
     "See paper", "Logger", "4 Levelogger dipwells", "4",
     "B/C (raw data: see A1)", "https://doi.org/10.1594/PANGAEA.908215",
     "Hydrological Processes 2025 (hyp.70209)",
     "https://doi.org/10.1002/hyp.70209", "Verified"),
    ("C14", "Pekan (Pahang) canal-blocking restoration dipwells", "Malaysia", "Pahang",
     "≈3.3", "≈103.3", "Regional approximation", "Drained / canal-blocked PSF",
     "Mid-2010s (approx.)", "Monthly", "Simple PVC tube wells (manual)", "112 tube wells + 16 canal gauges",
     "C – conference abstract", "—", "IPC 2016 abstract A-065",
     "https://peatlands.org/assets/uploads/2019/06/ipc16p467-471a065kasih.simon_.etal_.pdf",
     "Period approximate"),
]
for c in C:
    R.append([c[0], "In situ · paper / on request"] + list(c[1:]))

# ---------------- D: syntheses / gridded products ----------------
D = [
    ("D1", "SE Asian forested peatland WTD maps (IMERG-driven, ~25 years daily)", "Southeast Asia", "Regional",
     "Grid", "Grid", "Grid resolution 10 km", "Undrained PSF (model)",
     "c. 2000–2025", "Daily", "Calibrated with dipwell records from undrained PSF in 4 regions (wells up to 2,200 m from major canals)", "—",
     "A – open (Mendeley Data)", "https://doi.org/10.17632/69mbg22fxf",
     "Hooijer & Vernimmen 2026, Scientific Reports 16:26515",
     "https://doi.org/10.1038/s41598-026-64641-2", "Verified"),
    ("D2", "PEATCLSM_Trop (land surface model output for natural/drained tropical peat)", "Pan-tropical (incl. SE Asia)", "Regional",
     "Grid", "Grid", "Grid resolution 9 km", "Natural + drained peat",
     "See dataset", "Daily", "Evaluated against site water levels and EC evapotranspiration; site list in paper", "—",
     "A – open (Zenodo)", "https://doi.org/10.5281/zenodo.6011689",
     "Apers et al. 2022, JAMES", "https://doi.org/10.1029/2021MS002784",
     "Site table not checked (full text not accessible)"),
    ("D3", "OPTRAM remote-sensing WTD retrieval (Landsat)", "Malaysia, Indonesia, Peru", "Sarawak; Central Kalimantan",
     "See paper", "See paper", "—", "Drained / undrained / degraded / converted",
     "See paper", "Landsat revisit", "Validated against in situ WTD at 6 sites", "6 sites",
     "C – paper", "—", "Koupaei-Abyazani et al. 2024, JGR-Biogeosciences",
     "https://doi.org/10.1029/2024JG008116", "Verified"),
    ("D4", "GSMaP-driven regional groundwater level maps + CO2/CH4 emissions", "Southeast Asia", "~180,000 km² of peat",
     "Grid", "Grid", "—", "Multiple land uses",
     "See paper", "Monthly", "Calibrated with Palangkaraya and Sarawak sites", "—",
     "C – paper (see SI)", "—",
     "Hirano et al. 2025, AGU Advances; Cochrane et al. 2026, AGU Advances",
     "https://doi.org/10.1029/2025AV001861 ; https://doi.org/10.1029/2025AV002260", "Verified"),
    ("D5", "Synthesis of 16 SE Asian EC sites (112 site-years, incl. peat sites)", "Southeast Asia", "—",
     "See paper", "See paper", "—", "Primary forest → secondary forest → plantation",
     "Multi-year", "Half-hourly", "Flux synthesis (WTD not available at every site)", "16 sites",
     "C – paper", "—", "Hanggara et al. 2026, GCB",
     "https://doi.org/10.1111/gcb.70753", "Verified"),
    ("D6", "Harmonized peatland dataset for Indonesia v0.1 (+ EPIC-simulated monthly WTD 2001–2010)", "Indonesia", "National",
     "Grid", "Grid", "Grid resolution 0.25°", "Peat types / simulated WTD",
     "2001–2010 (simulated)", "Monthly", "Model output, not observations", "—",
     "A – open (Zenodo)", "https://zenodo.org/records/6998052",
     "IIASA (Balkovič et al.)", "https://pure.iiasa.ac.at/id/eprint/18393/",
     "Exact Zenodo record holding the simulated WTD not confirmed"),
    ("D7", "Meta-analysis of tropical peat drainage vs CO2/N2O (site-mean WTD)", "Pan-tropical (mostly SE Asia)", "—",
     "See supplement", "See supplement", "—", "Multiple land uses",
     "Literature compilation", "Site mean", "From literature", "Many sites",
     "A/C (supplementary material)", "—", "Prananto et al. 2020, GCB",
     "https://doi.org/10.1111/gcb.15147", "Verified"),
    ("D8", "SMAP peat soil moisture neural network (WTD proxy)", "Southeast Asia", "—",
     "Grid", "Grid", "Grid resolution 9–36 km", "—",
     "2015 onwards", "Daily", "Soil moisture, not WTD", "—",
     "A – open (Zenodo code and data)", "https://zenodo.org/records/6740137",
     "Dadap et al. 2022, ERL", "https://doi.org/10.1088/1748-9326/ac7969", "Verified"),
]
for d in D:
    R.append([d[0], "Synthesis / gridded product"] + list(d[1:]))

GAPS = [
    ("Thailand", "Kuan Kreng (Nakhon Si Thammarat / Phatthalung / Songkhla); To Daeng (Princess Sirindhorn PSF)",
     "Only DEM-based hydrology and fire-prevention studies and UNDP project documents; no public continuous WTD time series found",
     "https://zenodo.org/records/14869357"),
    ("Vietnam", "U Minh Thuong / U Minh Ha (Ca Mau, Kien Giang)",
     "Only flooding and water quality studies, plus regional groundwater (not peat water table) monitoring wells; no public peat WTD data found",
     "https://www.researchgate.net/publication/343310013_Effect_of_flooding_on_peatland_in_U_Minh_Thuong_National_Park_Vietnam"),
    ("Philippines", "Leyte Sab-a Basin; Agusan Marsh (Caimpugan)",
     "Only qualitative land-use comparisons of water table and one-off sampling",
     "https://www.mires-and-peat.net/article/128855-effects-of-land-use-conversion-on-selected-physico-chemical-properties-of-peat-in-the-leyte-sab-a-basin-peatland-philippines/attachment/263082.pdf"),
    ("Sabah (Malaysia)", "Klias / Binsuluk",
     "Only restoration projects and biodiversity surveys; no WTD time series from the past decade found",
     "https://gec.org.my/reference-project/biodiversity-data-collection-in-klias-forest-reserve-and-binsuluk-forest-reserve-restoration-area-in-beaufort-sabah/"),
]


def write_csv():
    p = OUT / "SEA_peatland_WTD_datasets_EN.csv"
    with p.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(COLS)
        w.writerows(R)
    return p


def md_link(s):
    out = []
    for u in (x.strip() for x in s.split(" ; ") if x.strip()):
        if u.startswith("http"):
            label = u.replace("https://doi.org/", "doi:") if "doi.org" in u else "link"
            out.append(f"[{label}]({u})")
        else:
            out.append(u)
    return "<br>".join(out) if out else "—"


def esc(s):
    return s.replace("|", "\\|")


def write_md():
    idx = {c: i for i, c in enumerate(COLS)}
    lines = [
        "# Inventory of water table depth (WTD) data for Southeast Asian peatlands (literature 2016–2026)\n",
        "> Compiled 2026-09-25. The CSV in this folder (`SEA_peatland_WTD_datasets_EN.csv`) has all 18 fields.\n",
        "**Availability grades**: A = open repository, direct download; B = portal / registration / on request; C = only in paper figures, contact authors or agency.\n",
        "**Coordinates**: values marked \"literature/metadata\" come from the paper or dataset; values with \"≈\" are regional approximations and should be replaced with coordinates from the paper's SI or dataset metadata before use.\n",
        "**Accuracy**: temporal resolution and measurement method are listed. Instrument specs are given only where the paper names the model (e.g. Solinst Levelogger Edge, ±0.05% FS); manual dipwell readings are typically about ±1 cm (rule of thumb).\n",
    ]
    sections = [
        ("A. In situ observations: openly downloadable", "A"),
        ("B. National / regional monitoring networks and databases", "B"),
        ("C. In situ observations: published, data on request", "C"),
        ("D. Syntheses, remote sensing and gridded products (for validation or interpolation; not in situ)", "D"),
    ]
    head = "| ID | Site / dataset | Country · province | Lat, lon (source) | Land use | Period | Resolution / accuracy | Availability | Data link | Source publication(s) |"
    sep = "|---|---|---|---|---|---|---|---|---|---|"
    for title, pre in sections:
        lines += [f"\n## {title}\n", head, sep]
        for r in R:
            if not r[0].startswith(pre):
                continue
            g = lambda c: esc(r[idx[c]])
            la, lo = g("Latitude").split("; "), g("Longitude").split("; ")
            if len(la) > 1 and len(la) == len(lo):
                pairs = []
                for a, b in zip(la, lo):
                    name, _, va = a.strip().rpartition(" ")
                    _, _, vb = b.strip().rpartition(" ")
                    pairs.append(f"{name} ({va}, {vb})")
                coord = "; ".join(pairs) + f" ({g('Coordinate source')})"
            else:
                coord = f"{g('Latitude')}, {g('Longitude')} ({g('Coordinate source')})"
            res = f"{g('Temporal resolution')}; {g('Method / accuracy')}; {g('Sites / wells')}"
            lit = f"{g('Source publication(s)')}<br>{md_link(r[idx['Publication link(s)']])}"
            note = g("Verification / notes")
            if note:
                lit += f"<br>*{note}*"
            lines.append(
                f"| {g('ID')} | {g('Site / dataset')} | {g('Country')} · {g('Province / state')} | {coord} | "
                f"{g('Land use / condition')} | {g('Period')} | {res} | {g('Availability')} | "
                f"{md_link(r[idx['Data link']])} | {lit} |"
            )

    lines += [
        "\n## E. Data gaps (no public continuous WTD found in the past decade of literature)\n",
        "| Country / region | Peatland | Status | Reference |",
        "|---|---|---|---|",
    ]
    for g in GAPS:
        lines.append(f"| {g[0]} | {g[1]} | {g[2]} | [link]({g[3]}) |")

    lines += [
        "\n## Recommendations\n",
        "1. **High-frequency open data for modelling or calibration**: A1/A2 (Mendaram, Brunei, undrained dome), A3/A4/A5 (Palangkaraya disturbance gradient), A7/A8 (Kampar, Riau, three land uses), A9 (8 daily stations in Jambi + West Kalimantan). Together they cover undrained, drained, burnt and plantation conditions.",
        "2. **Widest spatial coverage**: B1 SiPALAGA (~142 stations, hourly). Test whether the portal is reachable or request data formally from BRGM; papers such as RSE 2025 and Sci Rep 2025 cite specific station IDs (e.g. BRG_621103_05) that can be followed up.",
        "3. **Monthly manual readings across many land uses**: A11 (48 sites in Malaysia + Indonesia) suits WTD–GHG relationship analysis.",
        "4. **Natural WTD baseline for undrained PSF**: D1 (Hooijer & Vernimmen 2026) provides 10 km daily WTD maps, useful as a restoration reference.",
        "5. **Fields to complete before citing**: coordinates marked \"≈\", FLUXNET-CH4 subset years in A6, whether A12 contains WTD, and the site table for D2. The compilation environment could not open publisher or repository full texts, so these fields were checked only against search summaries.",
    ]
    p = OUT / "SEA_peatland_WTD_datasets_EN.md"
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return p


if __name__ == "__main__":
    print(write_csv())
    print(write_md())
    print(len(R), "rows")
