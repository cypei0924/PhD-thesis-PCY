"""Facts for the EXPANDED_2006-2026 entries (A15-A22, B4-B13, C15-C59, D9-D14) and the October 2026 additions
(A23, A34, C60-C65, D4, D15), read by build_summary.py.

Same structure as DATASETS in build_summary.py. Periods, time steps and value ranges of downloaded files were measured
from the files (2026-10-09); coordinates, methods and uses come from the papers (full text where it could be
downloaded, otherwise the abstract, as stated per paper).

Also here, for your table SEA_peatland_WTD_datasets.xlsx:
- DUPLICATES: your rows that repeat an existing entry;
- TABLE_FIXES: cell corrections from reading the papers and files; format_expanded.py writes them into
  EXPANDED_2006-2026.xlsx and write_updates.py lists them against your table in UPDATES_2026-10.xlsx;
- CHECKED_NOT_ADDED: datasets and reports found by the search that were checked and left out, with the reason.
"""

DL = "Downloaded"
DLP = "Downloaded (part of the data)"
EMB = "Embargoed / on request"
UNREACH = "Public, but server unreachable from the cloud"
NODATA = "No public data"
ELSEWHERE = "Data already in this repository"

NEG = "m; negative = below peat surface"
NEG_CM = "cm; negative = below peat surface"

OPEN = "Open; downloaded to paper/"
ABS = "Abstract only (closed access or the publisher blocked the download); full text not read"
BLOCKED = "Open access, but the publisher blocked the download; abstract only"


def f(file, site, lat, lon, cover, content, wtd, start="", end="", step="", n="", miss="", rng="", note="", part=""):
    return dict(file=file, part=part, site=site, lat=lat, lon=lon, cover=cover, content=content, wtd=wtd,
                start=start, end=end, step=step, n=n, miss=miss, rng=rng, note=note)


def p(cite, doi, access, da, da_dl):
    return dict(cite=cite, doi=doi, access=access, da=da, da_dl=da_dl)


def dms(d, m, s=0.0, neg=False):
    v = round(d + m / 60 + s / 3600, 4)
    return -v if neg else v


EXPANDED = [
    # ------------------------------------------------------------------ A: public repositories
    dict(
        id="A15", folder="A15_Maludam_Naman_Tang2020_Nishina2023",
        name="Maludam undrained peat swamp forest and Naman oil palm, daily WT, Sarawak",
        status=DL, license="CC BY 4.0",
        links=[("figshare (Melling & Wong 2024)", "https://doi.org/10.6084/m9.figshare.25299358")],
        papers=[
            p("Tang et al. 2020, Global Change Biology 26", "10.1111/gcb.15332", ABS,
              "Not read (closed). Koupaei-Abyazani et al. 2024 (D10) state that the Malaysian WT data are in Melling & Wong 2024 on figshare.",
              "Yes (figshare)"),
            p("Nishina et al. 2023, Science of the Total Environment 870", "10.1016/j.scitotenv.2023.162062", BLOCKED,
              "Not read.", "Yes (figshare)"),
        ],
        how=("Tang 2020 measured eddy-covariance CO2 exchange at the Maludam (MY-MLM) tower for 4 years (2011-2014) and found "
             "the forest a net CO2 source every year (183-632 g C m-2 yr-1); the daily WT file is the water table behind that "
             "record. Nishina 2023 monitored dissolved N2O in the drainage of oil palm plantations on peat near Sibu (dry and "
             "wet season surveys). Koupaei-Abyazani 2024 (D10) used both daily series (as 'MA-undrained' 2011-2014 and "
             "'MA-converted' 2018-2019) to validate Landsat OPTRAM water-table estimates."),
        notes=["Coordinates from Koupaei-Abyazani et al. 2024, Table 1: MA-undrained 1.4536 N, 111.1494 E; MA-converted "
               "2.1860 N, 111.8459 E.",
               "The figshare page blocks scripts with a bot check; the files were saved with a headless browser. "
               "download_data.py may print FAILED for them; open the figshare link in a browser instead.",
               "The converted-site file starts on 2018-03-01, one month earlier than the 2018/04 in your Sheet1 (A4)."],
        files=[
            f("MA_undrained_daily_WT_data.xlsx", "Maludam NP, MY-MLM tower area", 1.4536, 111.1494,
              "Undrained peat swamp forest (logged before 2000, protected since)", "Daily mean WT (cm)",
              "Yes: " + NEG_CM + " (positive = standing water)", "2011-01-01", "2014-12-31", "1 d", 1461, "0 %",
              "-39.0 / -2.9 / 23.7"),
            f("MA_converted_daily_WT_data.xlsx", "Naman oil palm plantation, Sibu", 2.1860, 111.8459,
              "Oil palm converted from peat swamp forest", "Daily mean WT (cm)", "Yes: " + NEG_CM,
              "2018-03-01", "2019-05-31", "1 d", 454, "0.7 %", "-101.3 / -57.6 / -16.0"),
        ]),
    dict(
        id="A16", folder="A16_Maludam_Tang2018", name="Maludam (MY-MLM) tower, half-hourly CH4 flux and WT, Sarawak",
        status=DL, license="CC-BY-4.0",
        links=[("Zenodo 1161966", "https://doi.org/10.5281/zenodo.1161966")],
        papers=[p("Tang et al. 2018, Geophysical Research Letters 45", "10.1029/2017GL076457", BLOCKED,
                  "Not read. The Zenodo record is titled 'Methane flux data from a tropical peat swamp forest in Sarawak, Malaysia'.",
                  "Yes (Zenodo)")],
        how=("Eddy-covariance CH4 flux over a 2-month wet-season period (Nov-Dec 2013): mean daily FCH4 about 0.024 g C m-2 d-1. "
             "A linear model showed air temperature controlled FCH4 before the water table reached the surface, and water "
             "table alone explained about 20 % of FCH4 variability once standing water emerged (abstract)."),
        notes=["Same tower and forest as A6 and A15; this file adds a half-hourly WT record for Nov-Dec 2013, which is not in "
               "the daily A15 file at sub-daily resolution.",
               "WT sign is inferred from the values (mean +5.3 cm in the wet season, standing water in the paper)."],
        files=[
            f("CH4Data.xlsx", "Maludam NP, MY-MLM tower", 1.4536, 111.1494, "Undrained peat swamp forest",
              "Sheet CH4_TROPI: radiation, Ta, RH, VPD, wind, Tsoil, VWC, WT (cm), u*, H, LE, CH4 flux, NEE",
              "Yes: " + NEG_CM + " (positive = standing water)", "2013-11-01 00:00", "2013-12-31 23:30", "30 min", 2928,
              "0 %", "-10.2 / 5.3 / 28.4", part="CH4_TROPI"),
        ]),
    dict(
        id="A17", folder="A17_Jambi_Smallholdings_WarrenThomas2022",
        name="Oil palm smallholdings and Sungai Buluh protected forest, Jambi",
        status=DL, license="CC0-1.0",
        links=[("Dryad", "https://doi.org/10.5061/dryad.rr4xgxd9v")],
        papers=[p("Warren-Thomas et al. 2022, Journal of Applied Ecology 59", "10.1111/1365-2664.14135", OPEN,
                  "'Data available via the Dryad Digital Repository https://doi.org/10.5061/dryad.rr4xgxd9v.'", "Yes")],
        how=("Water tables were read manually every fortnight (August 2018 - August 2019) in a dipwell at each of 41 smallholder "
             "oil palm plots (3 sites) and 21 plots in the adjacent Sungai Buluh Peat Protection Forest; four LevelSCOUT loggers "
             "(15 min) in one dipwell per site were a sense-check. Plot indices (12-month mean, max depth, number of readings "
             "below 40 cm) were tested as predictors of bird diversity, vegetation structure and oil palm yield. Mean water "
             "tables were -52 to -3 cm on farms and -3 to +15 cm in the forest; no trade-off between wetness and yield or birds "
             "was detected."),
        notes=["Coordinates are not given in the files or the paper (map only); the study area is in Jambi, next to the Sungai "
               "Buluh Peat Protection Forest.",
               "The README warns that sudden pressure drops mean a sensor was lifted out of the dipwell; the -210 cm minima "
               "in every logger series are such artefacts and should be removed.",
               "The per-plot manual summaries are in Oil_palm_yields_predictors.csv for 33 farms (the paper's yield models "
               "also used n = 33); the raw fortnightly readings and the forest plots' manual data are not in the dataset.",
               "Dryad blocks scripts (bot check and a token for its API); the files were saved with a headless browser."],
        files=[
            f("Water_tables_loggers.csv", "Forest logger (Sungai Buluh)", "", "", "Protected peat swamp forest",
              "Logger depth to water (cm) and water temperature", "Yes: " + NEG_CM + " (column ..._neg)",
              "2018-08-28 02:00", "2019-07-14 14:15", "15 min", 30770, "0 %", "-210.2 / -24.2 / 35.8", part="Site = Forest"),
            f("Water_tables_loggers.csv", "Oil palm Site 1 logger", "", "", "Smallholder oil palm", "As above",
              "Yes: " + NEG_CM, "2018-09-08 01:43", "2019-07-14 14:13", "15 min", 29715, "0 %", "-210.2 / -12.6 / 23.8",
              part="Site = Site 1"),
            f("Water_tables_loggers.csv", "Oil palm Site 2 logger", "", "", "Smallholder oil palm", "As above",
              "Yes: " + NEG_CM, "2018-08-28 02:00", "2019-07-14 14:15", "15 min", 30770, "0 %", "-210.3 / -57.0 / -12.3",
              part="Site = Site 2"),
            f("Water_tables_loggers.csv", "Oil palm Site 3 logger", "", "", "Smallholder oil palm", "As above",
              "Yes: " + NEG_CM, "2018-09-10 01:05", "2019-07-14 14:05", "15 min", 29525, "0 %", "-210.3 / -76.2 / -0.7",
              part="Site = Site 3"),
            f("Oil_palm_yields_predictors.csv", "33 oil palm plots (PLO, PRO, SWO)", "", "", "Smallholder oil palm",
              "Per-plot WT summaries from fortnightly manual readings (Wat_min/max/mean/SD_cm, n = 24 readings), yield, vegetation, management",
              "Plot means only", "2018-08", "2019-08", "fortnightly (summarised)", 33),
            f("Rainfall.csv", "Sites 1 and 2", "", "", "", "Daily manual rainfall (mm)", "No"),
            f("README.txt", "", "", "", "", "Dataset README (variables, sensor notes)", "No"),
            f("Bird_*.csv (5 files), Oil_palm_yields_predictors_description.csv", "", "", "", "",
              "Bird counts, species list, traits; variable descriptions", "No"),
        ]),
    dict(
        id="A18", folder="A18_CentralKalimantan_Swails2021",
        name="Pangkalan Bun forests and oil palm, CH4/N2O and WT (CIFOR), Central Kalimantan",
        status=UNREACH, license="",
        links=[("CIFOR Dataverse DATA.00201", "https://doi.org/10.17528/CIFOR/DATA.00201")],
        papers=[p("Swails et al. 2021, Frontiers in Environmental Science 9", "10.3389/fenvs.2021.617828", OPEN,
                  "'The datasets presented in this study can be found in online repositories ... https://doi.org/10.17528/CIFOR/DATA.00201.'",
                  "Yes (CIFOR Dataverse; not reachable from the cloud)")],
        how=("Monthly CH4 and N2O fluxes with water table depth, soil moisture and temperature from January 2014 to September "
             "2015 (no monitoring in July-August 2014) in three undrained forest plots (FOR-1 to FOR-3) and three smallholder "
             "oil palm plots (OP-2007, OP-2009, OP-2011). Dipwells were installed next to each gas collar (hummock and hollow "
             "in forest, near and far from palms in oil palm), 12 per plot. WT controlled monthly N2O variation in forest; "
             "CH4 was high in forest and negligible in oil palm. The study spans a normal (2014) and a strong El Nino year (2015)."),
        notes=["Plot coordinates (Swails 2021, Table 1): FOR-1 S 2 49.410 E 111 48.784; FOR-2 S 2 49.341 E 111 50.434; FOR-3 "
               "S 2 50.852 E 111 48.155; OP-2011 S 2 47.379 E 111 48.624; OP-2009 S 2 47.292 E 111 48.190; OP-2007 S 2 "
               "47.230 E 111 48.089 (about 10 km from Pangkalan Bun).",
               "Same plots and campaign as Swails et al. 2019 (INDEX A13-14 / your A14): the WT behind both papers is the "
               "same measurement.",
               "data.cifor.org refused connections from the cloud; run `python3 download_data.py A18` locally. The paper's "
               "supplement is saved in paper/: Table S3 gives plot-mean WT (cm, +/- SE): FOR-1 -24.0, FOR-2 -28.8, FOR-3 -16.7, "
               "OP-2007 -58.1, OP-2009 -58.0, OP-2011 -33.5."],
        files=[]),
    dict(
        id="A19", folder="A19_Jambi_CIFOR_Comeau2016",
        name="Berbak primary forest, drained forest and oil palm (CIFOR), Jambi",
        status=UNREACH, license="",
        links=[("CIFOR DATA.00290 (Swails 2023)", "https://doi.org/10.17528/CIFOR/DATA.00290"),
               ("CIFOR DATA.00330 / 00331 (Swails 2026)", "https://doi.org/10.17528/CIFOR/DATA.00330"),
               ("CIFOR DATA.00316 (Hergoualc'h 2026)", "https://doi.org/10.17528/CIFOR/DATA.00316")],
        papers=[
            p("Swails et al. 2023, Biogeochemistry 167", "10.1007/s10533-023-01070-7", OPEN,
              "'The datasets generated and analyzed during the current study are available in the Dataverse repository, https://doi.org/10.17528/CIFOR/DATA.00290.'",
              "Yes (CIFOR Dataverse; not reachable from the cloud)"),
            p("Swails et al. 2026, Geoderma", "10.1016/j.geoderma.2026.118030", BLOCKED,
              "Not read; CIFOR DATA.00330 (raw) and DATA.00331 (summary) carry this paper's title.", "Yes (CIFOR Dataverse)"),
            p("Hergoualc'h et al. 2026, Royal Society Open Science", "10.1098/rsos.252443", BLOCKED,
              "Not read; CIFOR DATA.00316 is titled 'Supporting summary data of the paper Hergoualc'h et al. (2026)'.",
              "Yes (CIFOR Dataverse)"),
            p("Comeau et al. 2016, Geoderma 268", "10.1016/j.geoderma.2016.01.016", ABS, "Not read (closed; no abstract available).", "n/a"),
        ],
        how=("Swails 2023: monthly N2O and CH4 fluxes, water table depth (2 m PVC dipwell next to each collar), soil moisture and "
             "temperature from October 2011 to March 2013 in a primary forest (Berbak National Park), a logged and drained "
             "forest and an oil palm plantation, plus intensive sampling after two fertilisation events; N2O fell "
             "logarithmically and CH4 rose as the water table approached the surface in the forests. Swails 2026: monthly "
             "total and heterotrophic soil respiration with environmental variables over 2012-2013 at the same three sites. "
             "Hergoualc'h 2026: monthly fluxes for a year and daily for a month after two fertilisations in an oil palm "
             "N-fertiliser trial on peat (abstract)."),
        notes=["Coordinates (Swails 2023): primary forest 1 27 S, 104 21 E (core of Berbak NP, 2 km from the Batang Hari); "
               "drained forest and oil palm about 60 km WSW, 1 39 S, 103 52 E.",
               "The CIFOR record descriptions for DATA.00290 and 00330/00331 are copy-paste errors (they describe Congo/Cameroon "
               "and food-system data); the titles identify the papers.",
               "The trial in Hergoualc'h 2026 and Comeau 2016 is probably at the same Jambi oil palm site; not confirmed from "
               "full text.",
               "data.cifor.org refused connections from the cloud; run `python3 download_data.py A19` locally."],
        files=[]),
    dict(
        id="A20", folder="A20_CentralKalimantan_SWAMP_CIFOR", name="CIFOR SWAMP peatland GHG datasets, Central Kalimantan",
        status=UNREACH, license="",
        links=[("CIFOR DATA.ZORCAF", "https://data.cifor.org/dataset.xhtml?persistentId=doi:10.17528/CIFOR/DATA.ZORCAF"),
               ("CIFOR DATA.F5DM1Y", "https://data.cifor.org/dataset.xhtml?persistentId=doi:10.17528/CIFOR/DATA.F5DM1Y")],
        papers=[],
        how="No paper identified. The record titles (2015 SWAMP surveys at Katingan and Tanjung Puting) come from the earlier search.",
        notes=["doi.org reports that neither 10.17528/CIFOR/DATA.ZORCAF nor .F5DM1Y exists, and Crossref has no record; these "
               "may be unregistered draft identifiers. Treat this entry as unconfirmed until the records open locally.",
               "data.cifor.org refused connections from the cloud; `python3 download_data.py A20` tries the Dataverse API locally."],
        files=[]),
    dict(
        id="A21", folder="A21_NorthSelangor_Cooper2020",
        name="North Selangor forest-to-oil-palm conversion stages, GHG and WT, Malaysia",
        status=DLP, license="CC BY 4.0",
        links=[("Nature Communications supplementary files", "https://doi.org/10.1038/s41467-020-14298-w")],
        papers=[p("Cooper et al. 2020, Nature Communications 11", "10.1038/s41467-020-14298-w", OPEN,
                  "'All data are available on request from the authors. The source data underlying Figs. 1-3 are provided as a "
                  "Source Data file; additional data are in Supplementary Data 1 file.'", "Partly (WT at sampling; rest on request)")],
        how=("CO2, CH4 and N2O fluxes in four conversion stages (secondary forest, drained forest, young and mature oil palm) "
             "in North Selangor Peat Swamp Forest; sampling repeated three times in the 2014 wet season (Oct-Dec; annual "
             "fluxes from Nov-Dec 2014), 150 sampling points at 20 sites. Water table was read in dipwells at each plot at the "
             "time of gas sampling and used to test whether WT explained the fluxes; monthly WT over two years at two "
             "secondary-forest locations is described but not published. Conversion raised CO2 and N2O and lowered CH4."),
        notes=["Plot coordinates are not given in the paper.",
               "Cooper2020_SourceData.xlsx 'Basic data' and Cooper2020_SupplementaryData1.xlsx hold the same plot table "
               "(not byte-identical); 'Water Table / cm Time 1' has 20 values ('PLUS 10' = +10 cm)."],
        files=[
            f("Cooper2020_SourceData.xlsx", "20 plots, 4 conversion classes", "", "", "Secondary forest, drained forest, young and mature oil palm",
              "Per-sampling GHG means, soil moisture/temperature; WT at sampling time (Time 1); Fig. 1-2 data",
              "Yes: " + NEG_CM + " (single readings)", "2014-10", "2014-12", "per sampling (5 per class)", 20, "",
              "-60 / -16.0 / 30", part="Basic data"),
            f("Cooper2020_SupplementaryData1.xlsx", "As above", "", "", "", "Same plot table as 'Basic data'", "Yes (as above)"),
        ]),
    dict(
        id="A22", folder="A22_Badas_Canal_Somers", name="Badas drainage canal: culvert water levels and canal/porewater chemistry, Brunei",
        status=DL, license="CC BY 4.0",
        links=[("HydroShare", "https://doi.org/10.4211/hs.3953b24e0238467980a226c72cfc360e")],
        papers=[p("Somers et al. 2023, JGR Biogeosciences 128", "10.1029/2022JG007194", BLOCKED,
                  "Not read; the HydroShare resource says it 'accompanies a manuscript submission' and the MATLAB README links it to this study.",
                  "Yes (HydroShare)")],
        how=("An isotope-enabled model of methane and DIC transport, degassing and oxidation along a 5 km canal across a "
             "disturbed peat dome, fitted to porewater and canal-water concentrations and d13C (Jan and Aug 2020): about 70 % "
             "of the methane entering the canal is oxidised in it. The culvert logger levels were used to calculate streamflow."),
        notes=["The loggers measure canal water level at two culverts (CUL-1, CUL-2), not the peat water table.",
               "HydroShare point coverage: 4.5619 N, 114.3367 E; period 2020-01-01 to 2020-08-31 (the logger files run to Dec 2020).",
               "The Dec2020 file names are swapped: 'Culvert1_..._Dec2020' has Location CUL-2 in its header and "
               "'Culvert2_..._Dec2020' has CUL-1.",
               "Subfolders were flattened into file names (Compensated_Levelogger_files_*, Matlab_Model_Code_*)."],
        files=[
            f("Compensated_Levelogger_files_Cul_1-May_19_2020-Compensated.csv", "CUL-1", 4.5619, 114.3367, "Drainage canal",
              "Barometrically compensated level (m) and temperature", "No (canal level)", "2020-01-24 13:00", "2020-05-19 12:30",
              "15 min", 11135, "", "0.003 / 0.174 / 0.237 m"),
            f("Compensated_Levelogger_files_Cul_2-May_19_2020-Compensated.csv", "CUL-2", 4.5619, 114.3367, "Drainage canal",
              "As above", "No (canal level)", "2020-01-24 13:00", "2020-05-19 13:00", "15 min", 11137, "", "0.013 / 0.141 / 0.210 m"),
            f("Compensated_Levelogger_files_Culvert1_Compensated_June2020.csv", "CUL-1", 4.5619, 114.3367, "Drainage canal",
              "As above", "No (canal level)", "2020-05-28 15:15", "2020-06-10 14:00", "15 min", 1244, "", "0.224 / 0.464 / 0.830 m"),
            f("Compensated_Levelogger_files_Culvert2_compensated_June2020.csv", "CUL-2", 4.5619, 114.3367, "Drainage canal",
              "As above", "No (canal level)", "2020-05-28 15:15", "2020-06-10 14:00", "15 min", 1244, "", "0.118 / 0.367 / 0.738 m"),
            f("Compensated_Levelogger_files_Culvert1_Compensated_Dec2020.csv", "CUL-2 (per header)", 4.5619, 114.3367, "Drainage canal",
              "As above", "No (canal level)", "2020-06-10 15:15", "2020-12-16 14:45", "15 min", 18143, "", "0.112 / 0.309 / 1.431 m"),
            f("Compensated_Levelogger_files_Culvert2_compensated_Dec2020.csv", "CUL-1 (per header)", 4.5619, 114.3367, "Drainage canal",
              "As above", "No (canal level)", "2020-06-10 15:15", "2020-12-16 14:45", "15 min", 18143, "", "0.220 / 0.424 / 1.563 m"),
            f("*.xle (6 files)", "", "", "", "", "Solinst raw logger files matching the CSVs", "No"),
            f("13C-DIC_CH4-Jan_2020.xlsx, 13C-DIC_CH4_Badas_Aug_2020.xlsx, Major_ions_Badas_Jan_2020_corrected.xlsx", "Canal and porewater",
              4.5619, 114.3367, "", "Dissolved CH4, CO2, d13C; major ions", "No", "2020-01", "2020-08"),
            f("Matlab_Model_Code_* (25 files)", "", "", "", "", "Model code and field-data copies", "No"),
        ]),
]

EXPANDED += [
    # ------------------------------------------------------------------ B: networks, portals, on request
    dict(
        id="B4", folder="B4_Palangkaraya_UF_Sulaiman2023", name="Sebangau (Palangkaraya UF) daily GWL 1993-2019, Central Kalimantan",
        status=EMB, license="",
        links=[("Paper (BRIN release planned)", "https://doi.org/10.1038/s41598-023-27393-x")],
        papers=[p("Sulaiman et al. 2023, Scientific Reports 13", "10.1038/s41598-023-27393-x", OPEN,
                  "'The monthly in situ groundwater level and rainfall data sets will be publicly available two years after the "
                  "completion of the collaborative Japan-Indonesia Collaboration Research of Tropical Peatland project through the "
                  "National Research and Innovation Agency (BRIN).'", "No (planned release via BRIN)")],
        how=("A monitoring station in Sebangau National Park (2.321002 S, 113.901161 E) recorded daily GWL with a pressure sensor "
             "from 1 September 1993 to 12 December 2019. GWL and rainfall anomalies were compared with Nino3.4, the Dipole Mode "
             "Index, SST and Ekman transport: GWL dropped 1.0-1.5 m in the 1997/98 and 2015 El Ninos and the 2019 positive IOD, "
             "and dry-season minima deepened from about -0.9 to -1.0 m before 2010 to -1.3 to -1.4 m after 2015. GWL is proposed "
             "as an alert indicator for El Nino and IOD+ events."),
        notes=["Same location as the Palangkaraya UF tower (A3, A4), extending that record back to 1993.",
               "The statement promises monthly (not daily) data."],
        files=[]),
    dict(
        id="B5", folder="B5_SATREPS_Apers2022", name="SATREPS Japan-Indonesia peat monitoring sites (11 sites)",
        status=NODATA, license="",
        links=[("SATREPS 'fire2015' page (offline)", "http://kalimantan88.sakura.ne.jp/fire2015/fire2015home.html")],
        papers=[p("Apers et al. 2022, JAMES 14", "10.1029/2021MS002784", "Open; saved in D9_PEATCLSM_Trop_Apers2022/paper/",
                  "'Groundwater level and eddy covariance data used for evaluation are available at the sources indicated in "
                  "Table B1.' For SATREPS: 'publicly available, frequently updated water level data ... that was manually digitized'.",
                  "No (portal offline)")],
        how=("Apers et al. digitised the SATREPS water-level graphs for 11 sites (natural and drained, 2012-2020) and used them, "
             "with the other Table B1 sites, to evaluate PEATCLSM_Trop water levels (see D9)."),
        notes=["kalimantan88.sakura.ne.jp no longer resolves (DNS), so the graphs cannot be re-digitised; the site list with "
               "coordinates and years is in EXPANDED_2006-2026.xlsx (B5)."],
        files=[]),
    dict(
        id="B6", folder="B6_KFCP_ExMRP_Putra2018", name="KFCP dipwell network, ex-Mega Rice Project Blocks A and E, Central Kalimantan",
        status=NODATA, license="",
        links=[("Paper", "https://doi.org/10.1088/1755-1315/149/1/012027")],
        papers=[
            p("Putra et al. 2018, IOP Conf. Ser.: Earth Environ. Sci. 149", "10.1088/1755-1315/149/1/012027", OPEN,
              "No data availability statement (IOP proceedings).", "No"),
            p("Putra et al. 2019, IOP Conf. Ser.: Earth Environ. Sci. 284", "10.1088/1755-1315/284/1/012021", OPEN,
              "No data availability statement.", "No"),
            p("Hikouei et al. 2023, Science of the Total Environment 857", "10.1016/j.scitotenv.2022.159701",
              "See D12_ML_GWL_Hikouei2023", "See D12.", "n/a"),
        ],
        how=("Putra 2018: monthly GWL (blow-straw method) from 300 dipwells of the Kalimantan Forests and Climate Partnership "
             "(KFCP) in northern Block A and southern Block E of the ex-Mega Rice Project, January 2010 - January 2013, compared "
             "with TRMM rainfall and MODIS hotspots to find a critical GWL for fire. Putra 2019 extended the analysis to "
             "2010-2017 and estimated hydraulic conductivity from the 2010-2012 data."),
        notes=["Dipwell coordinates are only shown on maps (Putra 2018, Fig. 1)."],
        files=[]),
    dict(
        id="B7", folder="B7_Sabangau_BNF", name="Borneo Nature Foundation hydrological monitoring, Sabangau",
        status=NODATA, license="",
        links=[("BNF project page", "https://borneonaturefoundation.org/conservation/hydrological-monitoring-for-protecting-peatlands/")],
        papers=[],
        how="No paper. The project page describes dam and dipwell monitoring in the Sabangau forest; no data files are linked.",
        notes=["The page (checked 2026-10-09) has no data downloads; contact BNF for the dipwell records."],
        files=[]),
    dict(
        id="B8", folder="B8_APRIL_Riau_Hooijer2012_Evans2019", name="APRIL plantation subsidence and WT network, Riau (and Jambi oil palm)",
        status=NODATA, license="",
        links=[("Hooijer 2012", "https://doi.org/10.5194/bg-9-1053-2012"), ("Evans 2019", "https://doi.org/10.1016/j.geoderma.2018.12.028")],
        papers=[
            p("Hooijer et al. 2012, Biogeosciences 9", "10.5194/bg-9-1053-2012", OPEN, "No data availability section (2012).", "No"),
            p("Evans et al. 2019, Geoderma 338", "10.1016/j.geoderma.2018.12.028", OPEN,
              "No data statement; 'Supplementary data to this article can be found online' (Supplementary Table 1 summarises the "
              "322 poles used).", "Partly (per-pole summary in the Elsevier supplement)"),
        ],
        how=("Hooijer 2012: subsidence and water table depth in perforated PVC tubes at 125 locations in Acacia plantation "
             "(Riau, around 0.595 N, 102.334 E) and 42 in oil palm (around 1.566 S, 103.601 E, Jambi), plus adjacent forest; "
             "a 2-year series per transect was selected from September 2007 - August 2010, oil palm July 2009 - June 2010 at "
             "2-weekly intervals. Mean WTD was related to subsidence and carbon loss. Evans 2019: 447 subsidence poles with "
             "WTD read on each visit in APRIL Acacia plantations and forest, 2010-2016 (322 poles with at least 3 years); mean "
             "WTD per pole explained subsidence rates."),
        notes=["The oil palm part of Hooijer 2012 is in Jambi, not Riau.",
               "Company (APRIL) monitoring data; the per-pole mean WTD table (Evans 2019 Supplementary Table 1) can be saved from "
               "the Elsevier article page in a browser."],
        files=[]),
    dict(
        id="B9", folder="B9_SESAME_Pratama2020_Irfan", name="SESAME telemetry stations (BRG/Midori), Riau and South Sumatra",
        status=NODATA, license="",
        links=[("Pratama 2020", "https://doi.org/10.1088/1757-899X/796/1/012037")],
        papers=[
            p("Pratama et al. 2020, IOP Conf. Ser.: Mater. Sci. Eng. 796", "10.1088/1757-899X/796/1/012037", OPEN,
              "No data availability statement.", "No"),
            p("Irfan et al. 2020, J. Phys.: Conf. Ser. 1568", "10.1088/1742-6596/1568/1/012028", OPEN, "No data availability statement.", "No"),
            p("Irfan et al. 2023, Journal of Groundwater Science and Engineering 11", "10.26599/JGSE.2023.9280008", OPEN,
              "No data availability statement.", "No"),
            p("Irfan et al. 2026, AIP Conf. Proc.", "10.1063/5.0337576", ABS, "Not read (closed; no abstract available).", "n/a"),
        ],
        how=("Pratama 2020: rainfall and GWL from the SESAME station in Dompas village (Bengkalis, Riau; operating since April "
             "2018) were used to fit a daily water-balance model of GWL (data April 2018 - June 2019). Irfan 2020: GWL and soil "
             "moisture at four South Sumatra SESAME stations, SR1 (2.911 S, 105.082 E), SR2 (2.677 S, 105.143 E), LR1 (3.143 S, "
             "105.184 E) and LR2 (3.458 S, 104.921 E), 1 July 2017 - 5 August 2019, regressed GWL on soil moisture. Irfan 2023: "
             "stations OKI-1 (3.478628 S, 104.9651 E) and OKI-2 (3.392495 S, 104.9775 E), dry seasons (Jul-Oct) of 2019 (IOD+) "
             "and 2020 (La Nina); lowest GWL -1.14 m in 2019 and -0.44 m in 2020."),
        notes=["OKI-1 and OKI-2 have the same coordinates as SIPALAGA stations IN_BRG_160224_02 and IN_BRG_160224_01 (Cinta "
               "Jaya) in Apers 2022 Table B1 (B13); they are probably the same stations.",
               "SESAME records every 10 min (Khakim 2022, C42)."],
        files=[]),
    dict(
        id="B10", folder="B10_KuanKreng_Khampeera2018", name="Kuan Kreng peat swamp (Bor Lor, Thale Noi), Nakhon Si Thammarat, Thailand",
        status=NODATA, license="",
        links=[("Paper", "https://doi.org/10.48048/wjst.2018.2723")],
        papers=[p("Khampeera et al. 2018, Walailak Journal of Science and Technology 15", "10.48048/wjst.2018.2723", OPEN,
                  "No data availability statement; water-level data came from the Pak Phanang Fire Control Station.", "No")],
        how=("Drought indices (SPI, NDDI, standardised water-level index SWI and water-table level WTL) for the Kuan Kreng peat "
             "swamp (7 37'-8 26' N, 99 41'-100 22' E). Hydrological drought used monthly means from 50 water-level monitoring "
             "stations in the Bor Lor and Thale Noi non-hunting zones, focusing on 2010 (El Nino) and 2012; water levels fell "
             "below the surface for 4 months in 2012."),
        notes=["Station coordinates are not listed."],
        files=[]),
    dict(
        id="B11", folder="B11_UMinhThuong_Thai2024", name="U Minh Thuong National Park groundwater monitoring, Vietnam",
        status=EMB, license="",
        links=[("Paper", "https://doi.org/10.3390/su16020620")],
        papers=[p("Thai et al. 2024, Sustainability 16", "10.3390/su16020620", OPEN,
                  "'These database are by ourself ... can share by authors group, MDPI journal.'", "On request")],
        how=("Peat volume, carbon and Melaleuca regrowth after the 2002 fire in the 8,038 ha core zone, related to the inundation "
             "regime; uses 'inherited groundwater level monitoring data from 2002-2021' and water-level changes 2012-2022."),
        notes=["Well locations and measurement frequency are not described."],
        files=[]),
    dict(
        id="B12", folder="B12_Pahang_PPRP", name="Pahang Peatland Restoration Project (SE Pahang peat swamp forest), Malaysia",
        status=NODATA, license="",
        links=[("PPRP website", "https://pprp.my/")],
        papers=[],
        how="No paper found. The project website describes restoration and water-level monitoring but links no data.",
        notes=["Checked 2026-10-09: no data downloads on pprp.my."],
        files=[]),
    dict(
        id="B13", folder="B13_SIPALAGA_Apers2022", name="SIPALAGA stations listed by Apers 2022 (59 stations)",
        status=NODATA, license="",
        links=[("SIPALAGA portal (BRGM)", "https://sipalaga.brgm.go.id")],
        papers=[
            p("Apers et al. 2022, JAMES 14", "10.1029/2021MS002784", "Open; saved in D9_PEATCLSM_Trop_Apers2022/paper/",
              "SIPALAGA 'real-time (daily, hourly or sub-hourly) water level data'; sites manually quality-checked and classed "
              "natural or drained from Google Earth.", "Portal only"),
            p("Putra et al. 2025, Indonesian Journal of Environmental Management and Sustainability 9", "10.26554/ijems.2025.9.2.46-55",
              OPEN, "No data availability statement; data 'obtained from 39 monitoring stations operated under SIPALAGA'.", "No"),
            p("Hein et al. 2022, Regional Environmental Change 22", "10.1007/s10113-022-01979-z", OPEN,
              "'We downloaded from the website of the Peat Restoration Agency ... (https://sipalaga.brg.go.id) the daily water levels "
              "of 167 water monitoring stations, over the complete year 2019.'", "Portal (then public)"),
        ],
        how=("Hein 2022 downloaded daily water levels of 167 SIPALAGA stations for 2019 and averaged the 25 oil palm stations in "
             "East Sumatra (mean drainage depth 81 +/- 50 cm; 10 of 25 at 60 cm or less) to drive a subsidence and flood-risk model. "
             "Apers 2022 used 59 SIPALAGA stations (2019-2020) to evaluate PEATCLSM_Trop (D9). Putra 2025 analysed daily rainfall "
             "and peat water level at 39 SIPALAGA stations in Riau's peat hydrological units (Rokan, Siak, Kampar, ...), "
             "October 2018 - December 2020; dry-period water tables reached -0.6 to -0.8 m."),
        notes=["sipalaga.brgm.go.id returns a Cloudflare block page to the cloud; try it from your browser.",
               "Two South Sumatra stations (Cinta Jaya, IN_BRG_160224_01/_02) match the coordinates of Irfan 2023's OKI-1/OKI-2 (B9)."],
        files=[]),
]

EXPANDED += [
    # ------------------------------------------------------------------ C: sites only in papers
    dict(id="C15", folder="C15_Palangkaraya_Jauhiainen2008", name="Palangkaraya drained forest and burnt site before/after canal dams",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1890/07-2038.1")],
         papers=[p("Jauhiainen et al. 2008, Ecology 89", "10.1890/07-2038.1", ABS, "Not read (closed).", "n/a")],
         how=("CO2 and CH4 fluxes and water tables in a drained peat swamp forest and a deforested burnt area before and after dams "
              "were built in drainage canals (2004-2007); annual minimum water tables were higher after damming (abstract)."),
         notes=["Coordinates from Apers 2022 Table B1: burnt site 2.3381 S, 114.0297 E; drained forest 2.345 S, 114.0367 E."], files=[]),
    dict(id="C16", folder="C16_BlockC_Sebangau_Wosten2006", name="Sebangau / Block C (and Air Hitam Laut, Jambi) hydrological modelling",
         status=NODATA, license="", links=[("Jaenicke 2010", "https://doi.org/10.1007/s11027-010-9214-5")],
         papers=[
             p("Wosten et al. 2006, Int. J. Water Resour. Dev. 22", "10.1080/07900620500405973", ABS, "Not read.", "n/a"),
             p("Wosten et al. 2008, Catena 73", "10.1016/j.catena.2007.07.010", ABS, "Not read.", "n/a"),
             p("Jaenicke et al. 2010, Mitig. Adapt. Strateg. Glob. Change 15", "10.1007/s11027-010-9214-5", OPEN,
               "No data statement; the test-site groundwater record was provided by Prof. H. Takahashi (Hokkaido University).", "No"),
             p("Jaenicke et al. 2011, J. Environ. Manage. 92", "10.1016/j.jenvman.2010.09.029", ABS, "Not read.", "n/a"),
             p("Ritzema et al. 2014, Catena 114", "10.1016/j.catena.2013.10.009", ABS, "Not read.", "n/a"),
         ],
         how=("Jaenicke 2010 calibrated and validated a SIMGRO groundwater model against a dipwell at a test site (2.323 S, "
              "113.903 E; daily, within 0.10 m) and simulated daily groundwater-level rise from dam construction in the Sebangau "
              "catchment for 2006-2008 (about +20 cm in the dry season). Wosten 2006 modelled groundwater and flooding in the "
              "Air Hitam Laut watershed (Jambi), not Block C."),
         notes=["The Jaenicke 2010 test-site dipwell is the long-term Hokkaido station later published by Sulaiman 2023 (B4).",
                "Most of this entry is modelling; measured series appear only as calibration data."], files=[]),
    dict(id="C17", folder="C17_Sebangau_Kononen2016_Lampela2017", name="Sebangau logged forest and restored area",
         status=NODATA, license="", links=[("Kononen 2016", "https://doi.org/10.1007/s11273-016-9498-7")],
         papers=[p("Kononen et al. 2016, Wetlands Ecol. Manage. 24", "10.1007/s11273-016-9498-7", ABS, "Not read (closed).", "n/a"),
                 p("Lampela et al. 2017, For. Ecol. Manage. 386", "10.1016/j.foreco.2016.12.004", ABS, "Not read (closed).", "n/a")],
         how="Water-table records used as site descriptors (per Apers 2022 Table B1; full text not read).",
         notes=["Coordinates from Apers 2022 Table B1: logged forest 2.3214 S, 113.8953 E (2013); restored area 2.3217 S, 114.0181 E (2012-2013)."],
         files=[]),
    dict(id="C18", folder="C18_Sebangau_AirHitam_Taufik2019", name="Upper Sebangau forest and Air Hitam (Jambi) groundwater simulations",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1016/j.geoderma.2019.04.001")],
         papers=[p("Taufik et al. 2019, Geoderma 347", "10.1016/j.geoderma.2019.04.001", OPEN,
                   "No data statement; observed groundwater depths used for inverse modelling are shown in Annex I.", "No")],
         how=("SWAP simulations of daily groundwater table depth for 1980-2015 at the Sebangau Forest and Air Hitam (Jambi), "
              "with water-retention curves for fibric, hemic and sapric peat; the fibric curve was obtained by inverse modelling "
              "of observed groundwater depths (Annex I). Drought (80th-percentile threshold) and fire hazard were then assessed."),
         notes=["The series in this paper are simulated; the observed calibration data (2000-2008 Sebangau, 2003-2004 Air Hitam per "
                "Apers Table B1) are only plotted."], files=[]),
    dict(id="C19", folder="C19_Sebangau_Putra2021", name="Sebangau forested, ditch-blocked and drained sites (see A23 for the data)",
         status=ELSEWHERE, license="", links=[("Data: see A23 (Leeds 10.5518/960)", "https://doi.org/10.5518/960")],
         papers=[p("Putra et al. 2021, Hydrological Processes 35", "10.1002/hyp.14174", BLOCKED,
                   "Data at the University of Leeds repository, https://doi.org/10.5518/960 (listed as 'IsReferencedBy' this paper).", "Yes (A23)"),
                 p("Putra et al. 2023, Mires and Peat 29", "10.19189/MaP.2022.OMB.StA.2407", OPEN,
                   "No separate statement; uses the same loggers (180-min intervals) and rainfall (30-min).", "Yes (A23)")],
         how=("Water levels at 13 logger wells and 4 ditch loggers, plus manual wells, in a forested, a ditch-blocked and a drained "
              "site in Sebangau National Park, 22 August 2019 - 17 January 2020, to test the effect of ditch dams on water-level "
              "dynamics (Putra 2021) and water-table responses to storms (Putra 2023)."),
         notes=["Your A23 is the same study with the data link; the data are summarised under A23."], files=[]),
    dict(id="C20", folder="C20_TumbangNusa_BudiSantosa2020", name="Tumbang Nusa burnt-peat transect, Central Kalimantan",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.20886/glm.2020.1.1.27-40")],
         papers=[p("Budi Santosa et al. 2020, Jurnal Galam 1", "10.20886/glm.2020.1.1.27-40", ABS,
                   "Not read; the journal's site now redirects to an unrelated domain.", "n/a")],
         how=("Water table at 17 points spaced 250 m along a 4 km transect from the river edge into secondary forest, across areas "
              "burnt in 1997, 2003, 2006 and 2009, related to precipitation and land elevation (abstract)."),
         notes=[], files=[]),
    dict(id="C21", folder="C21_Jabiren_Firmansyah2020", name="Jabiren ex-ICCTF plot, Central Kalimantan",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.30595/agritech.v22i2.8000")],
         papers=[p("Firmansyah et al. 2020, Agritech 22", "10.30595/agritech.v22i2.8000", ABS, "Not read (download blocked).", "n/a")],
         how="Groundwater level along a transect over 7 months (50-150 cm below the surface) and peat subsidence over 10 months (abstract).",
         notes=[], files=[]),
    dict(id="C22", folder="C22_TimelapseCamera_Sulaeman2022", name="Time-lapse camera peat motion and WT, 4 land covers (South Sumatra, Central Kalimantan)",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1088/1755-1315/1025/1/012011")],
         papers=[p("Sulaeman et al. 2022, IOP Conf. Ser.: Earth Environ. Sci. 1025", "10.1088/1755-1315/1025/1/012011", OPEN,
                   "No data availability statement.", "No")],
         how=("Wingscapes time-lapse cameras photographed a subsidence pole and an adjacent dipwell every 3 hours for about a year at "
              "four sites: forest and oil palm in a South Sumatra peat hydrological unit, coconut (Kahayan-Sebangau PHU) and shrub "
              "(Kapuas-Barito PHU) in Central Kalimantan; peat motion was related to WTD (R2 0.74-0.95)."),
         notes=["This is the 'South Sumatra' part of your C10-C11 camera entries."], files=[]),
    dict(id="C23", folder="C23_CentralKalimantan_Yulianti2024", name="Forest and burnt area (KHDTK Tumbang Nusa), Raspberry Pi cameras + loggers",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1088/1755-1315/1421/1/012005")],
         papers=[p("Yulianti et al. 2024, IOP Conf. Ser.: Earth Environ. Sci. 1421", "10.1088/1755-1315/1421/1/012005", OPEN,
                   "No data availability statement.", "No")],
         how=("Water level loggers in dipwells recorded WTD every 2 hours (transmitted online) alongside Raspberry Pi time-lapse "
              "cameras, December 2022 - June 2023, to relate daily WTD to peat surface motion in forest and burnt peat."),
         notes=[], files=[]),
    dict(id="C24", folder="C24_CentralKalimantan_Treby2026", name="Intact and degraded peat, Central Kalimantan",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1016/j.pedsph.2026.02.009")],
         papers=[p("Treby et al. 2026, Pedosphere", "10.1016/j.pedsph.2026.02.009", ABS, "Not read (closed, no abstract).", "n/a"),
                 p("Treby et al. 2026, SSRN preprint", "10.2139/ssrn.7163970", ABS, "Not read.", "n/a")],
         how="WTD and soil water in an intact and a historically drained area, 2024/08-2025/11 (from the earlier search; not re-checked).",
         notes=[], files=[]),
    dict(id="C25", folder="C25_ExMRP_CanalBlocking_Suwito2022", name="Ex-MRP Blocks E and B canal blocking, Central Kalimantan",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1088/1755-1315/1018/1/012027")],
         papers=[p("Suwito et al. 2022, IOP Conf. Ser.: Earth Environ. Sci. 1018", "10.1088/1755-1315/1018/1/012027", OPEN,
                   "No data availability statement.", "No")],
         how=("Spot water-level readings on 14 and 28 February 2020 (wettest month) and in August 2020 (driest) at six locations "
              "(Tuanan I, Tuanan II-Katunjung, Camp Release, Bagantung, Kanal Primer, Mantangai Hulu) under four conditions "
              "(large, medium, small and no canal block); values are tabulated in the paper."),
         notes=[], files=[]),
    dict(id="C26", folder="C26_Palangkaraya_Itoh2017", name="Palangkaraya UF/DF/DB trenching chambers and hourly GWL",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1016/j.scitotenv.2017.07.132")],
         papers=[p("Itoh et al. 2017, Science of the Total Environment 609", "10.1016/j.scitotenv.2017.07.132", OPEN,
                   "No data statement found in the accepted manuscript.", "No")],
         how=("Hourly GWL (pressure sensor in PVC pipes) from January 2014 to December 2015 at UF (2.32 S, 113.90 E), DF (2.35 S, "
              "114.04 E) and DB (2.34 S, 114.04 E), used to upscale peat decomposition: mean GWL -0.23/-0.39 m (UF), -0.55/-0.59 "
              "m (DF), -0.22/-0.62 m (DB) in 2014/2015; 2015 minima -1.43 to -1.62 m."),
         notes=["Same three tower sites as A3 (whose files hold half-hourly GWL for the same period)."], files=[]),
    dict(id="C27", folder="C27_Kampar_Suryatmojo2019", name="Zamrud NP forest, burnt peat and mixed plantation (Siak, Kampar Peninsula landscape)",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1088/1755-1315/361/1/012034")],
         papers=[p("Suryatmojo et al. 2019, IOP Conf. Ser.: Earth Environ. Sci. 361", "10.1088/1755-1315/361/1/012034", OPEN,
                   "No data availability statement.", "No")],
         how=("Automatic GWL sensors and mini weather stations for 4 months (rain events of April-June 2018) in primary forest "
              "(Zamrud National Park), an ex-fire site and a community mixed plantation in Sungai Rawa village, Siak; GWL rise per "
              "rain event was analysed."),
         notes=["Coordinates (Maryani 2020, same stations): forest 0 42 54 S, 102 13 35 E; burnt 0 52 16 S, 102 20 22 E; mixed "
                "plantation 0 52 35 S, 102 20 41 E. The sites are in Siak regency, not Kampar."], files=[]),
    dict(id="C28", folder="C28_Siak_Maryani2020", name="Same stations as C27, July-December 2018",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1088/1755-1315/533/1/012012")],
         papers=[p("Maryani et al. 2020, IOP Conf. Ser.: Earth Environ. Sci. 533", "10.1088/1755-1315/533/1/012012", OPEN,
                   "No data availability statement.", "No")],
         how=("Automatic water-level and rainfall recorders, July-December 2018, at the three Sungai Rawa/Zamrud stations; GWL rise "
              "per rain event tabulated for 37 events."),
         notes=["Continuation of C27 at the same stations."], files=[]),
    dict(id="C29", folder="C29_Siak_Basuki2021", name="Dosan and Dayun villages, Siak (your A32)",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1088/1755-1315/648/1/012029")],
         papers=[p("Basuki et al. 2021, IOP Conf. Ser.: Earth Environ. Sci. 648", "10.1088/1755-1315/648/1/012029", OPEN,
                   "No data availability statement.", "No")],
         how=("Groundwater table measured with a stick in shallow wells at 0, 10, 25 and 50 m from canals in natural forest, mixed "
              "agriculture, shrub/ex-burnt, Acacia regrowth and oil palm plots, December 2017 - May 2019 (monthly plotted); mean "
              "-55 cm (Dosan) and -66 cm (Dayun); subsidence January 2018 - August 2019."),
         notes=["Your A32 is the same study."], files=[]),
    dict(id="C30", folder="C30_Siak_Gasib_Lutfi2021", name="Koto village, Gasib (Siak) oil palm blocks",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1088/1755-1315/756/1/012028")],
         papers=[p("Lutfi et al. 2021, IOP Conf. Ser.: Earth Environ. Sci. 756", "10.1088/1755-1315/756/1/012028", BLOCKED, "Not read.", "n/a")],
         how="Peat subsidence and groundwater level in four blocks (shrub L1; oil palm D1, D8, D31 aged 15, 10, 20 years); WT followed monthly rainfall (abstract).",
         notes=[], files=[]),
    dict(id="C31", folder="C31_Siak_CanalBlocking_Safitri2024", name="Bunsur village (Sungai Apit, Siak) canal blocking transects",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1088/1755-1315/1315/1/012058")],
         papers=[p("Safitri et al. 2024, IOP Conf. Ser.: Earth Environ. Sci. 1315", "10.1088/1755-1315/1315/1/012058", OPEN,
                   "No data availability statement.", "No")],
         how=("Manual GWL (measuring stick) in wells 5, 100, 400 and 900 m from blocked and unblocked canals under oil palm, rubber, "
              "sago, shrub and paludiculture, April 2022 - March 2023; mean -26.7 cm near blocked vs -58.7 cm near unblocked canals."),
         notes=[], files=[]),
    dict(id="C32", folder="C32_SungaiTohor_Silviana2020_Malik2022", name="Sungai Tohor (Tebing Tinggi Island) rewetting",
         status=NODATA, license="", links=[("Silviana 2020", "https://doi.org/10.1088/1757-899X/796/1/012041")],
         papers=[p("Silviana et al. 2020, IOP Conf. Ser.: Mater. Sci. Eng. 796", "10.1088/1757-899X/796/1/012041", OPEN, "No data statement.", "No"),
                 p("Malik et al. 2022, IOP Conf. Ser.: Earth Environ. Sci. 1041", "10.1088/1755-1315/1041/1/012047", OPEN, "No data statement.", "No")],
         how=("Silviana: 66 monitoring wells (33 unburnt, 33 burnt), read twice a month, February-June 2019, plus the SESAME station. "
              "Malik: daily levels from one logger for a year in Sungai Tohor and one in Kundur, reported as elevations (8.78-9.72 m), not depths."),
         notes=["Same island as your C4 (Sutikno 2020) and the new C63 (Sutikno 2019)."], files=[]),
    dict(id="C33", folder="C33_Riau_Rewetting_Lestari2022", name="Riau rewetted vs drained (reforested, oil palm, rubber)",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.3390/f13040505")],
         papers=[p("Lestari et al. 2022, Forests 13", "10.3390/f13040505", BLOCKED, "Not read (MDPI blocked the download).", "n/a")],
         how="Heterotrophic respiration, CH4 and N2O before and after rewetting deforested peat that was reforested, planted with oil palm or rubber (abstract).",
         notes=[], files=[]),
    dict(id="C34", folder="C34_Kampar_Nardi2021", name="Kampar Peninsula conservation forest (Pelalawan)",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.29244/jpsl.11.3.442-452")],
         papers=[p("Nardi et al. 2021, JPSL 11", "10.29244/jpsl.11.3.442-452", OPEN, "No data availability statement.", "No")],
         how=("Solinst Levelogger 3001 recording every 30 min (January-December 2020; mean -0.32 +/- 0.18 m) plus manual "
              "piezometer readings at three conservation-forest points at each N2O sampling; GWL entered the N2O regression models."),
         notes=[], files=[]),
    dict(id="C35", folder="C35_Bengkalis_Sutikno2026", name="Bengkalis Island drained, undrained inland and coastal sites",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.15243/jdmlm.2026.131.9163")],
         papers=[p("Sutikno et al. 2026, J. Degraded Mining Lands Manage. 13", "10.15243/jdmlm.2026.131.9163", BLOCKED, "Not read.", "n/a")],
         how="Empirical daily GWL model driven by GPM rainfall, calibrated on in-situ GWL at three sites (October 2023 - April 2025) (abstract).",
         notes=["Same island as A34 (Kagawa 2026, coastal peat)."], files=[]),
    dict(id="C36", folder="C36_Riau_Acacia_Jauhiainen2012", name="Acacia plantation CO2 transects, Sumatra (your A29)",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.5194/bg-9-617-2012")],
         papers=[p("Jauhiainen et al. 2012, Biogeosciences 9", "10.5194/bg-9-617-2012", OPEN, "No data availability section (2012).", "No")],
         how=("Water table monitored monthly or quarterly in perforated PVC tubes at the CO2 points along 8 transects (A-H, 700 m "
              "long, up to 28 km apart) on one Acacia plantation dome, April 2007 - April 2009; average WTD about 0.8 m; Table 2 "
              "gives WT statistics per transect."),
         notes=["Your A29 is the same study.", "Transect coordinates are not given."], files=[]),
    dict(id="C37", folder="C37_Kampar_Deshmukh2020", name="Kampar natural forest and Acacia flux towers (CH4)",
         status=EMB, license="", links=[("Paper", "https://doi.org/10.1111/gcb.15019")],
         papers=[p("Deshmukh et al. 2020, Global Change Biology 26", "10.1111/gcb.15019", OPEN,
                   "'The data that support the findings of this study are available from the corresponding author upon reasonable request.'", "On request")],
         how=("Eddy-covariance CH4 with GWL logged every 30 min (Solinst Levelogger 3001) near each tower plus fortnightly readings "
              "at PVC poles within 3 km, October 2016 - May 2019 (Acacia) and June 2017 - May 2019 (forest)."),
         notes=["Tower coordinates: forest 0 23 42.735 N, 102 45 52.382 E; Acacia 0 30 57.221 N, 102 02 11.090 E.",
                "Daily GWL for the intact site is public in A7/A8 (Deshmukh 2021/2023)."], files=[]),
    dict(id="C38", folder="C38_Riau_Coconut_Fawzi2024", name="Coconut plantation with 'Water Management Trinity', eastern Sumatra",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1016/j.heliyon.2024.e26661")],
         papers=[p("Fawzi et al. 2024, Heliyon 10", "10.1016/j.heliyon.2024.e26661", BLOCKED, "Not read.", "n/a")],
         how="Weekly CO2 over 6 months with water-table depth; managed annual mean WTD -45 to -51 cm since 1986 (abstract).",
         notes=[], files=[]),
    dict(id="C39", folder="C39_Sumatra_Plantations_Dariah2013", name="Oil palm / Acacia chamber studies (Jambi, Riau)",
         status=NODATA, license="", links=[("Dariah 2013", "https://doi.org/10.1007/s11027-013-9515-6")],
         papers=[p("Dariah et al. 2014, Mitig. Adapt. Strateg. Glob. Change 19", "10.1007/s11027-013-9515-6", ABS, "Not read (closed).", "n/a"),
                 p("Husnain et al. 2014, Mitig. Adapt. Strateg. Glob. Change 19", "10.1007/s11027-014-9550-y", ABS, "Not read (closed).", "n/a"),
                 p("Comeau et al. 2016, Geoderma 268", "10.1016/j.geoderma.2016.01.016", "See A19", "See A19.", "n/a")],
         how="WT at chamber points in oil palm and Acacia plantations (titles only; not read).", notes=[], files=[]),
    dict(id="C40", folder="C40_Rubber_Wakhid2017", name="Jabiren rubber plantation, Central Kalimantan",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1016/j.scitotenv.2017.01.035")],
         papers=[p("Wakhid et al. 2017, Science of the Total Environment 581-582", "10.1016/j.scitotenv.2017.01.035", OPEN,
                   "No data statement in the accepted manuscript.", "No")],
         how=("Hourly GWL (June 2014 - December 2015) and monthly chamber CO2 (December 2014 - December 2015) in an 8-year-old "
              "rubber plantation at 2 29 50 S, 114 11 20 E; annual soil respiration was computed from hourly GWL; minimum GWL "
              "-1.71 m in 2015 vs -1.35 m in 2014."),
         notes=[], files=[]),
    dict(id="C41", folder="C41_TanjungJabung_Khasanah2019", name="Smallholder mosaic, Tanjung Jabung Barat, Jambi",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1007/s11027-018-9803-2")],
         papers=[p("Khasanah & van Noordwijk 2019, Mitig. Adapt. Strateg. Glob. Change 24", "10.1007/s11027-018-9803-2", OPEN,
                   "No data availability statement.", "No")],
         how=("Subsidence every 6 months (November 2012 - May 2015) at four points per transect in a logged-over forest and four "
              "smallholder land uses; water-table depth at the points was related to subsidence rates."),
         notes=[], files=[]),
    dict(id="C42", folder="C42_SouthSumatra_Khakim2022", name="KHG Sugihan-Saleh SESAME stations and Sriwijaya botanical garden, South Sumatra",
         status=NODATA, license="", links=[("Khakim 2022", "https://doi.org/10.24057/2071-9388-2021-137")],
         papers=[p("Khakim et al. 2022, Geography, Environment, Sustainability 15", "10.24057/2071-9388-2021-137", OPEN, "No data statement.", "No"),
                 p("Maryani & Novriadhy 2021, IOP Conf. Ser.: Earth Environ. Sci. 810", "10.1088/1755-1315/810/1/012023", OPEN, "No data statement.", "No")],
         how=("Khakim: two SESAME stations recording groundwater level every 10 minutes (2015-2018) used with satellite soil "
              "moisture and hotspots; WT fell about 1.53 m in October 2015. Maryani: water-level depth vs vegetation composition "
              "in degraded peat at the Sriwijaya Wetland Botanical Garden."),
         notes=[], files=[]),
    dict(id="C43", folder="C43_WestKalimantan_Astiani2018", name="West Kalimantan canal-blocking and oil palm studies (Kubu Raya, Mempawah)",
         status=NODATA, license="", links=[("Astiani 2018", "https://doi.org/10.13057/biodiv/d190221")],
         papers=[p("Astiani et al. 2018, Biodiversitas 19", "10.13057/biodiv/d190221", OPEN, "No data statement.", "No"),
                 p("Herawati et al. 2018, MATEC Web Conf. 195", "10.1051/matecconf/201819503016", BLOCKED, "Not read.", "n/a"),
                 p("Nusantara et al. 2023, Jurnal Ilmu Lingkungan 21", "10.14710/jil.21.4.781-788", OPEN, "No data statement.", "No"),
                 p("Nahda et al. 2025, BIO Web Conf. 167", "10.1051/bioconf/202516703013", BLOCKED, "Not read.", "n/a")],
         how=("Astiani: weekly water table at dammed canals on bare burnt peat (March-December 2016) with CO2 (February 2016 - "
              "February 2017). Nusantara: 3 piezometers in each of 3 oil palm blocks (250/500/750 m), read morning and afternoon, "
              "1-30 September 2021, Kubu village. Herawati: Wajok Hilir canal blocks (abstract). Nahda: Limbung burnt peat, "
              "September-December 2023 (abstract)."),
         notes=["Nusantara's period is September 2021 (the earlier row said 2021/08-2021/10)."], files=[]),
    dict(id="C44", folder="C44_WestKalimantan_Novita2024", name="Rewetted vs drained oil palm, West Kalimantan",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1016/j.scitotenv.2024.175829")],
         papers=[p("Novita et al. 2024, Science of the Total Environment 952", "10.1016/j.scitotenv.2024.175829", BLOCKED, "Not read.", "n/a")],
         how="Rewetting oil palm on peat as a climate-mitigation option (abstract fragment only).", notes=[], files=[]),
    dict(id="C45", folder="C45_SouthKalimantan_Wakhid2021", name="Young smallholder oil palm near Banjarmasin, South Kalimantan",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.19189/map.2021.omb.sta.2159")],
         papers=[p("Wakhid et al. 2021, Mires and Peat 27", "10.19189/map.2021.omb.sta.2159", OPEN, "No data availability statement.", "No")],
         how=("GWL read manually once a month in perforated PVC pipes in three plots with monthly soil CO2 (September 2018 - "
              "March 2020) at 3 24 19.0 S, 114 46 11 E; GWL stayed below the surface all year."),
         notes=[], files=[]),
    dict(id="C46", folder="C46_WestAceh_Handayani2010", name="West Aceh oil palm on peat (WT depth vs CO2)",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.5400/jts.2010.15.3.255")],
         papers=[p("Handayani et al. 2010, Journal of Tropical Soils 15", "10.5400/jts.2010.15.3.255", ABS,
                   "Not read: the PDF link that OpenAlex lists for this DOI serves a different article (Purwantono et al. 2011, "
                   "J. Trop. Soils 16:17-24); that file is kept in paper/ renamed WRONG_PAPER_*.", "n/a")],
         how="Effect of water-table depth on CO2 emission in an oil palm plantation on West Aceh peat (title only).", notes=[], files=[]),
    dict(id="C47", folder="C47_Badas_Suhip2024", name="Badas peat dome piezometers, Brunei",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.19189/map.2023.cm.sc.2332104")],
         papers=[p("Suhip et al. 2024, Mires and Peat 31", "10.19189/map.2023.cm.sc.2332104", OPEN, "No data availability statement.", "No")],
         how=("13 piezometers (peat and underlying sand, in pairs on two transects plus a lagoon well) with Solinst Leveloggers "
              "at 20-min intervals, August 2020 - January 2021, with a tipping-bucket gauge, topographic and seismic surveys; "
              "max/min/median heads are tabulated."),
         notes=["Same dome as A22 and your C12."], files=[]),
    dict(id="C48", folder="C48_Damit_Hoyt2019", name="Damit dome (Hoyt 2019), Brunei",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1111/gcb.14702")],
         papers=[p("Hoyt et al. 2019, Global Change Biology 25", "10.1111/gcb.14702", "Preprint copies exist (see A2); not re-downloaded",
                   "See A2.", "n/a")],
         how="Apers 2022 Table B1 lists a 2012 water-level record at Damit dome (4.405 N, 114.363 E) from Hoyt 2019; it is not in the A2 Zenodo files.",
         notes=[], files=[]),
    dict(id="C49", folder="C49_Maludam_Busman2023", name="Maludam NP three forest types, 8 years",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1016/j.scitotenv.2022.159973")],
         papers=[p("Busman et al. 2023, Science of the Total Environment 858", "10.1016/j.scitotenv.2022.159973", BLOCKED, "Not read.", "n/a")],
         how="Soil CO2 and CH4 with groundwater level and other variables over eight years in three forest types (abstract).",
         notes=["Probably the same plots as C50 (Imran 2022)."], files=[]),
    dict(id="C50", folder="C50_Sarawak_Imran2022", name="Maludam NP: MPS, Alan Batu, Alan Bunga sites",
         status=EMB, license="", links=[("Paper", "https://doi.org/10.1088/2515-7620/ac6295")],
         papers=[p("Imran et al. 2022, Environmental Research Communications 4", "10.1088/2515-7620/ac6295", OPEN,
                   "'The data that support the findings of this study are available upon reasonable request from the authors.'", "On request")],
         how=("HOBO U20 loggers in two piezometers per site recorded every 30 min (processed to monthly means), February 2011 - "
              "December 2020, with peat surface level and rainfall; WT and surface fell to their lowest in 2019."),
         notes=["Coordinates: MPS 1 25 51.2 N, 111 07 52.0 E; Alan Batu 1 27 12.7 N, 111 08 57.4 E; Alan Bunga 1 27 47.9 N, 111 09 29.0 E."],
         files=[]),
    dict(id="C51", folder="C51_Sarawak_Wong2018_Kiew2020", name="Sarawak flux towers and chamber sites (Sibu, Maludam)",
         status=NODATA, license="", links=[("Ishikura 2018", "https://doi.org/10.1016/j.agee.2017.11.025")],
         papers=[p("Wong et al. 2018, Agric. For. Meteorol. 256", "10.1016/j.agrformet.2018.03.025", ABS, "Not read (closed).", "n/a"),
                 p("Kiew et al. 2020, Agric. For. Meteorol. 295", "10.1016/j.agrformet.2020.108189", ABS, "Not read (closed).", "n/a"),
                 p("Ishikura et al. 2018, Agric. Ecosyst. Environ. 254", "10.1016/j.agee.2017.11.025", OPEN, "No data statement.", "No"),
                 p("Ishikura et al. 2019, Ecosystems 22", "10.1007/s10021-019-00376-8", ABS, "Not read (closed).", "n/a"),
                 p("Sangok et al. 2017, Science of the Total Environment 587", "10.1016/j.scitotenv.2017.02.165", ABS, "Not read (closed).", "n/a")],
         how=("Ishikura 2018: half-hourly GWL from a piezometer (gap-filled with a tank model) with automated chambers in an oil "
              "palm plantation at 2 11 N, 111 50 E (Sibu), May 2014 - 2016. The other papers are the Sarawak EC towers and "
              "chamber studies (not read)."),
         notes=["The Sibu oil palm site is the 'MA-converted' site of A15."], files=[]),
    dict(id="C52", folder="C52_Sarawak_Cook2018", name="Sebungan and Sabaju oil palm estates, Sarawak",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.5194/bg-15-7435-2018")],
         papers=[p("Cook et al. 2018, Biogeosciences 15", "10.5194/bg-15-7435-2018", OPEN, "'Data are available in Cook (2018).' (PhD thesis)", "Thesis only")],
         how=("Water-table depth by dipmeter in a cluster of three dipwells per estate at each sampling visit (about weekly), "
              "August 2015 - September 2016, at Sebungan and Sabaju 1, 3 and 4; mean, min, max and % time deeper than 60 cm per "
              "site are reported; WT controlled DOC export."),
         notes=["Same estates as your A12. The supplement (saved in paper/) has rating curves and flux tables, not WT."], files=[]),
    dict(id="C53", folder="C53_Bintulu_Basri2024", name="Bintulu oil palm and peat swamp forest, soil respiration",
         status=NODATA, license="", links=[("Preprint", "https://doi.org/10.2139/ssrn.4767267")],
         papers=[p("Basri et al. 2024, SSRN preprint", "10.2139/ssrn.4767267", ABS, "Not read.", "n/a")],
         how="Long-term soil respiration and environmental drivers (from the earlier search; not re-checked).", notes=[], files=[]),
    dict(id="C54", folder="C54_Malaysia_Azizan2021", name="Drained oil palm, rewetted and natural forest, Malaysia",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.3390/w13233372")],
         papers=[p("Azizan et al. 2021, Water 13", "10.3390/w13233372", BLOCKED, "Not read (MDPI blocked).", "n/a")],
         how="Biweekly CO2, CH4 and N2O (July 2017 - December 2018) with continuous environmental variables at OP, RF and NF (abstract).",
         notes=[], files=[]),
    dict(id="C55", folder="C55_Johor_Katimon2012", name="Johor: Parit Madirono catchment and Ayer Hitam North Forest Reserve",
         status=NODATA, license="", links=[("Shamsuddin 2021", "https://doi.org/10.4236/jwarp.2021.1312052")],
         papers=[p("Katimon et al. 2012, Jurnal Teknologi 38", "10.11113/jt.v38.487", ABS, "Not read.", "n/a"),
                 p("Shamsuddin et al. 2021, J. Water Resour. Prot. 13", "10.4236/jwarp.2021.1312052", OPEN, "No data statement.", "No")],
         how=("Shamsuddin: Van Essen Cera-Diver loggers in wells W2 and W4 from June 2015 and W6 from May 2016, manual tube wells "
              "W1, W3, W5, and divers in drains before/after check dams (December 2016, 2017) in Ayer Hitam North FR, Muar; monthly "
              "averages for 2016 are plotted. Katimon: hydrology of a drained catchment (abstract in Malay)."),
         notes=[], files=[]),
    dict(id="C56", folder="C56_Bacho_Nagano2013", name="Bacho (Narathiwat), To Daeng and Nakhon Si Thammarat, Thailand",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.19189/001c.128481")],
         papers=[p("Nagano et al. 2013, Mires and Peat 11", "10.19189/001c.128481", OPEN, "No data statement.", "No")],
         how=("Water table recorded at each monthly subsidence observation at Bacho 1-5 (6 29 N, 101 45 E) from July 1983 to "
              "January 2006 (WT -116 to -54 cm in the 1987 fires); HOBO U20 water level with continuous CO2 at Nakhon Si "
              "Thammarat 2006-2009; To Daeng (6 12 N, 101 56 E) undrained forest spot measurements."),
         notes=["The longest WT record found for Thailand; per-point periods are tabulated in the paper."], files=[]),
    dict(id="C57", folder="C57_Leyte_Decena2021", name="Leyte Sab-a Basin peatland, Philippines",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.19189/map.2021.bg.sta.2287")],
         papers=[p("Decena et al. 2021, Mires and Peat 27", "10.19189/map.2021.bg.sta.2287", OPEN, "No data statement.", "No")],
         how="Peat cores (1 m) from forest, grassland and cultivated areas analysed for water content, bulk density, porosity and nutrients; no water-table series.",
         notes=["No WT measurements: keep only as a Philippines lead."], files=[]),
    dict(id="C58", folder="C58_Papua_Asmat", name="Asmat (Papua) survey and Sumber Mulya SIPALAGA station",
         status=NODATA, license="", links=[("ResearchGate 379805559", "https://www.researchgate.net/publication/379805559")],
         papers=[], how="Spot GWL survey in Asmat (ResearchGate, not downloadable by script) and one SIPALAGA station in Merauke (see B13).",
         notes=["Sumber Mulya (IN_BRG_910111_01, 8.205 S, 140.216 E) is also listed in B13."], files=[]),
    dict(id="C59", folder="C59_Apers2022_Unpublished", name="Apers 2022 'unpublished' smallholder sites (Raja Musa, Hampangen, Teluk Empening)",
         status=NODATA, license="", links=[("Apers 2022", "https://doi.org/10.1029/2021MS002784")],
         papers=[p("Apers et al. 2022, JAMES 14", "10.1029/2021MS002784", "Open; saved in D9_PEATCLSM_Trop_Apers2022/paper/",
                   "Listed as 'unpublished' in Table B1.", "No")],
         how="Used as evaluation sites for PEATCLSM_Trop (D9).",
         notes=["The coordinates fall inside the SUSTAINPEAT (A11) regions; probably SUSTAINPEAT logger wells."], files=[]),
]

EXPANDED += [
    # ------------------------------------------------------------------ D: compilations and products
    dict(id="D9", folder="D9_PEATCLSM_Trop_Apers2022", name="PEATCLSM_Trop simulations 2000-2019, SE Asia part (your D2)",
         status=DLP, license="CC-BY-4.0", links=[("Zenodo 6011689", "https://doi.org/10.5281/zenodo.6011689")],
         papers=[p("Apers et al. 2022, JAMES 14", "10.1029/2021MS002784", OPEN,
                   "'Groundwater level and eddy covariance data used for evaluation are available at the sources indicated in "
                   "Table B1. Full simulation output is accessible on a Zenodo data repository (Apers et al., 2022).'", "Yes (Zenodo)")],
         how=("NASA GEOS Catchment model (CLSM) and its natural and drained tropical peat versions (PEATCLSM_Trop,Nat/Drain) run at "
              "9 km (EASEv2) for 2000-2019 over SE Asia, the Congo Basin and Central/South America; simulated water level zbar "
              "was evaluated against the water-level sites of Table B1 (B5, B13, C15-C18, C48, C59 and INDEX A1-A3)."),
         notes=["Only the SE Asia (SEA) 20-year mean and standard deviation maps were downloaded (about 15 MB each). The daily "
                "image stacks daily_images_PEATSEA_N/_D and _CLSMSEA (7.1-7.3 GB each) exceed the 5 GB limit and were not fetched; "
                "the Congo (CO) and South America (CSA) files were skipped.",
                "Each file holds 23 variables; zbar (m, negative downwards) is the water level. 39,525 peat cells on a 266 x 643 "
                "grid, 11.4 S - 7.4 N, 95.0-154.9 E. Read with GDAL/rasterio as netcdf:<file>:zbar.",
                "PEATCLSM_Trop-Simulations_doc.pdf (data description) is in data/ but not committed (PDF)."],
         files=[
             f("daily_mean_PEATSEA_N.nc", "SE Asia peat grid (natural version)", "-11.4 to 7.4", "95.0 to 154.9", "Peat (PEATMAP + De Lannoy 2014)",
               "20-year mean of 23 land-surface variables incl. zbar", "Yes (model): " + NEG, "2000-01-01", "2019-12-31", "20-year mean", 39525, "",
               "-7.05 / -1.16 / 1.19 (zbar, m)"),
             f("daily_mean_PEATSEA_D.nc", "SE Asia peat grid (drained version)", "-11.4 to 7.4", "95.0 to 154.9", "Peat",
               "As above", "Yes (model): " + NEG, "2000-01-01", "2019-12-31", "20-year mean", 39525, "", "-7.05 / -1.24 / 1.19 (zbar, m)"),
             f("daily_mean_CLSMSEA.nc", "SE Asia grid (default CLSM)", "-11.4 to 7.4", "95.0 to 154.9", "Peat",
               "As above", "Yes (model): " + NEG, "2000-01-01", "2019-12-31", "20-year mean", 39525, "", "-7.05 / -1.22 / 1.25 (zbar, m)"),
             f("daily_std_PEATSEA_N.nc, daily_std_PEATSEA_D.nc, daily_std_CLSMSEA.nc", "As above", "", "", "",
               "20-year standard deviation of the same variables", "Yes (model, SD)", "2000-01-01", "2019-12-31", "20-year SD", 39525, "",
               "SD of zbar 0.03-2.30 m (PEATSEA_N)"),
         ]),
    dict(id="D10", folder="D10_OPTRAM_KoupaeiAbyazani2024", name="OPTRAM satellite WT estimates (your D3)",
         status=ELSEWHERE, license="", links=[("Paper", "https://doi.org/10.1029/2024JG008116")],
         papers=[p("Koupaei-Abyazani et al. 2024, JGR Biogeosciences 129", "10.1029/2024JG008116", OPEN,
                   "'In situ water table data was used with permission from Takashi Hirano, Lulie Melling, Guan Xhuan Wong, and "
                   "Kristell Hergoualc'h ... Data for the Indonesian sites are available in Hirano, 2023 "
                   "(https://doi.org/10.6084/m9.figshare.22321129.v1). Data for the Malaysian sites are available in Melling & Wong, "
                   "2024 (https://doi.org/10.6084/m9.figshare.25299358.v1).' Code: github.com/koupsci/OPTRAM_code_updated.",
                   "Yes (A4, A15)")],
         how=("Landsat OPTRAM moisture indices were related to in situ WT at IN-undrained (2.32 S, 113.90 E; 2015-2018), IN-drained "
              "(2.35 S, 114.04 E; 2013-2017), MA-undrained (1.4536 N, 111.1494 E; 2011-2014), MA-converted (2.1860 N, 111.8459 E; "
              "2018-2019) and two Peruvian sites."),
         notes=["The SE Asian in situ data are A4 (DailyGWL.xlsx) and A15 (Melling & Wong 2024), both downloaded."], files=[]),
    dict(id="D11", folder="D11_CanalWTD_Vernimmen2020_Dadap2021", name="Canal water depth from LiDAR (Central Kalimantan 2011) and SE Asia canal map",
         status=DLP, license="CC BY 4.0", links=[("Mendeley 7nnf495jbw (Vernimmen 2020)", "https://doi.org/10.17632/7nnf495jbw"),
                                                 ("Stanford SDR yj761xk5815 (Dadap 2021 canals)", "https://doi.org/10.25740/yj761xk5815")],
         papers=[p("Vernimmen et al. 2020, Water 12", "10.3390/w12051486", BLOCKED, "Not read (MDPI blocked); the Mendeley record states it is the map 'as published in Vernimmen et al. 2020'.", "Yes (Mendeley)"),
                 p("Dadap et al. 2021, AGU Advances 2", "10.1029/2020AV000321", BLOCKED, "Not read; the canal map is on the Stanford Digital Repository (CC BY-ND 3.0).", "Yes (Stanford SDR)")],
         how=("Vernimmen: canal water-table depth (CWD) from airborne LiDAR (minimum of a 100 m grid on a 1 m DTM vs median surface), "
              "validated against 145 field measurements (within 0.25 m for 86 %). Dadap: CNN-mapped drainage canals and roads (5 m, "
              "from 2017 Planet imagery) across Borneo, Sumatra and Peninsular Malaysia, related to fire and carbon emissions."),
         notes=["The Stanford canal map is a canal mask (not WTD) and was not downloaded; its file list is only shown by a browser."],
         files=[f("CWD_100.0m_CentralKalimantan_UTM50S_DrySeason2011.tif", "Central Kalimantan (UTM 50S)", "", "", "Drained peat",
                  "Canal water depth below surrounding surface (m), 100 m grid, dry season 2011", "Canal depth (m, positive down)",
                  "2011 (dry season)", "", "one map", 93158, "", "0.05 / 1.25 / 8.82")]),
    dict(id="D12", folder="D12_ML_GWL_Hikouei2023", name="Machine-learning GWL of a degraded Central Kalimantan peat dome (KFCP dipwells)",
         status=NODATA, license="", links=[("Hikouei 2023", "https://doi.org/10.1016/j.scitotenv.2022.159701")],
         papers=[p("Hikouei et al. 2023, Science of the Total Environment 857", "10.1016/j.scitotenv.2022.159701", BLOCKED, "Not read.", "n/a"),
                 p("Hikouei et al. 2025, Groundwater for Sustainable Development 29", "10.1016/j.gsd.2025.101413", ABS,
                   "The authors state they do not have permission to share the data.", "No")],
         how=("Hikouei 2023: random forest and XGBoost models of GWL in a Central Kalimantan peat dome (XGBoost R2 0.998 near canals; "
              "elevation and precipitation most important). Hikouei 2025: a MODFLOW model calibrated on monthly manual readings "
              "from 265 dipwells (2011-2019), with XGBoost analysis of its errors."),
         notes=["The 265 dipwells are the KFCP network of B6, extended to 2019."], files=[]),
    dict(id="D13", folder="D13_Kalimantan_FireRisk_Mahdiyasa", name="Kalimantan peatland fire-risk table (WT height, land cover, fires)",
         status=DL, license="CC-BY-4.0", links=[("Zenodo 17907349", "https://doi.org/10.5281/zenodo.17907349")],
         papers=[],
         how="No paper confirmed; the same author published peatland fire-risk models in 2025-2026 (e.g. Mahdiyasa et al. 2025, Ecological Informatics, 'Peatfr').",
         notes=["No dates in the file: Water Table Height has only 340 distinct values, so it is a coarse gridded or modelled field "
                "sampled at about 0.009 deg (1 km) points, not a measurement."],
         files=[f("Kalimantan Tropical Peatland Data.csv", "58,245 points in Kalimantan", "-3.48 to 1.72", "108.86 to 118.58",
                  "Farmland / forest / shrub / plantation flags", "Water Table Height (m), distance to human activities, land cover, fire occurrence",
                  "Yes (static): m; negative = below surface", "", "", "static", 58245, "0 %", "-1.89 / -0.65 / 0.23")]),
    dict(id="D14", folder="D14_CIFOR_WTD_Compilation_Couwenberg", name="Meta-analyses with site-level WT (incl. CIFOR DATA.00291)",
         status=UNREACH, license="", links=[("CIFOR DATA.00291 (Swails 2024)", "https://doi.org/10.17528/CIFOR/DATA.00291")],
         papers=[p("Couwenberg et al. 2010, Global Change Biology 16", "10.1111/j.1365-2486.2009.02016.x", ABS, "Not read (closed).", "n/a"),
                 p("Couwenberg & Hooijer 2013, Mires and Peat 12", "10.19189/001c.128487", OPEN, "No data statement.", "No"),
                 p("Hergoualc'h & Verchot 2014, Mitig. Adapt. Strateg. Glob. Change 19", "10.1007/s11027-013-9511-x", ABS, "Not read (closed).", "n/a"),
                 p("Carlson et al. 2015, Environmental Research Letters 10", "10.1088/1748-9326/10/7/074006", OPEN,
                   "Databases 1-2 (59 sites from 12 studies with WT and carbon loss) are in the supplementary material.", "Yes (supplement)"),
                 p("Prananto et al. 2020, Global Change Biology 26", "10.1111/gcb.15147", ABS, "Not read (closed).", "n/a"),
                 p("Swails et al. 2024, Biogeochemistry 167", "10.1007/s10533-023-01110-2", OPEN, "Replication data: CIFOR DATA.00291.", "Yes (CIFOR; unreachable from the cloud)")],
         how=("Literature syntheses of WT depth and peat CO2/CH4/N2O or subsidence; Carlson 2015 fitted WT-carbon loss relations "
              "for 59 plantation sites; Swails 2024 reviewed undrained degraded vs undegraded forests in SE Asia and Latin America."),
         notes=["CIFOR DATA.00291 is the replication data of Swails 2024 (its Crossref description is a copy-paste error)."], files=[]),
]

# ---------------------------------------------------------------------- October 2026 additions
# Rows you added to SEA_peatland_WTD_datasets.xlsx (A23) or that the new search found (A34, C60-C65, D15, and data for your D4).
EXPANDED += [
    dict(id="A23", folder="A23_Sebangau_Putra2021", name="Sebangau forested, ditch-blocked and drained sites: water levels, rainfall, PET (Leeds)",
         status=DL, license="CC BY 4.0", links=[("University of Leeds 10.5518/960", "https://doi.org/10.5518/960")],
         papers=[p("Putra et al. 2021, Hydrological Processes 35", "10.1002/hyp.14174", BLOCKED,
                   "Repository record lists this paper and Putra's 2021 Leeds thesis as the users of the data.", "Yes"),
                 p("Putra et al. 2023, Mires and Peat 29", "10.19189/MaP.2022.OMB.StA.2407", "Open; saved in C19_Sebangau_Putra2021/paper/",
                   "Uses the same loggers.", "Yes")],
         how=("Six-month hydrological monitoring (22 Aug 2019 - 17 Jan 2020) at three sites in Sebangau National Park: Forested (6 "
              "vented loggers, 3-hourly), Blocked (4 well loggers, 2 ditch loggers, 7 manual wells) and Drained (3 well loggers, "
              "2 ditch loggers, 7 manual wells), plus two weather stations (rainfall, PET by Penman-Monteith). Putra 2021 compared "
              "water-level dynamics with and without ditch dams; Putra 2023 analysed water-table responses to individual storms."),
         notes=["Logger files give ABSOLUTE water level (cm) relative to a local site benchmark, not depth below the surface; "
                "the manual files give water table from the surface (cm). Convert loggers with the well surface elevations in the papers.",
                "Coordinates: Forested benchmark (well AL0) 2.3894 S, 113.4524 E; Blocked and Drained are 2.7-3.5 km from the "
                "Tumbang Nusa camp gauge (2.3556 S, 114.0896 E) (Putra 2023).",
                "forested_rainfall.csv holds 149 daily rows followed by 5-minute records under the same header.",
                "Related public files not downloaded: temperature data on figshare (doi:10.6084/m9.figshare.14900181, MIT) and DigiBog "
                "model files (doi:10.5518/1053). Your C19 is the same study."],
         files=[
             f("forested_auto_wl_AL0.csv, _AL1.csv, _AL5.csv", "Forested wells AL0, AL1, AL5", -2.3894, 113.4524, "Forested peatland",
               "Absolute water level (cm, local benchmark)", "Level, not depth", "2019-08-23 15:00", "2020-01-18 06:00", "3 h", 3520, "0-2 %",
               "-119.2 / -82.0 / -34.7 (cm, 3 wells)"),
             f("forested_auto_wl_BL1.csv, _BL5.csv, _BR2.csv", "Forested wells BL1, BL5, BR2", "~-2.39", "~113.45", "Forested peatland",
               "As above", "Level, not depth", "2019-11-08 12:00", "2020-01-18 06:00", "3 h", 1701, "0 %", "-81.5 / -59.3 / -33.7"),
             f("blocked_auto_wl_BB1.csv, _BB2.csv, _BB3.csv, _CA2.csv", "Blocked wells", "~-2.36", "~114.09", "Drained peat with ditch dams",
               "As above", "Level, not depth", "2019-09-01 18:00", "2020-01-14 12:00", "3 h", 3822, "0-6.8 %", "-90.8 / -50.1 / 28.6"),
             f("blocked_auto_wl_DS.csv, _US.csv", "Blocked ditch loggers (downstream, upstream)", "~-2.36", "~114.09", "Ditch",
               "Ditch water level (cm, benchmark)", "Ditch level", "2019-10-30 06:00", "2020-01-14 11:30", "30 min", 7197, "0 %", "-134.0 / -37.6 / 31.5"),
             f("drained_auto_wl_AA1.csv, _AA2.csv, _AA3.csv", "Drained wells", "~-2.36", "~114.09", "Drained peat, no dams",
               "As above", "Level, not depth", "2019-08-31 21:00", "2020-01-25 09:00", "3 h", 3119, "5-11 %", "-128.8 / -83.7 / -6.7"),
             f("drained_auto_wl_BD.csv, _SD.csv", "Drained ditch loggers", "~-2.36", "~114.09", "Ditch",
               "Ditch water level (cm, benchmark)", "Ditch level", "2019-10-30 06:00", "2020-01-15 23:00", "30 min", 7462, "0 %", "-166.3 / -87.0 / -20.7"),
             f("forested_man_wl.csv", "6 forested wells", -2.3894, 113.4524, "Forested peatland", "Manual WT from surface (cm)",
               "Yes: " + NEG_CM, "2019-08-23", "2020-01-18", "12 readings", 12, "", "-65.6 / -35.5 / 26.0"),
             f("blocked_man_wl.csv", "12 blocked points (BB1-3, CA1-7, DS, US)", "~-2.36", "~114.09", "Drained peat with ditch dams",
               "Manual WT from surface (cm)", "Yes: " + NEG_CM, "2019-09-11", "2019-12-12", "visits", 50, "", "-98.7 / -46.6 / 126.0"),
             f("drained_man_wl.csv", "12 drained points (AA1-3, BC, R1-7, SC)", "~-2.36", "~114.09", "Drained peat",
               "Manual WT from surface (cm)", "Yes: " + NEG_CM, "2019-09-11", "2019-12-13", "visits", 45, "", "-137.0 / -80.8 / 3.0"),
             f("forested_rainfall.csv, drained_blocked_rainfall.csv, forested_PET.csv, drained_blocked_PET.csv, readme.txt", "Two weather stations",
               "", "", "", "Rainfall (daily; forest also 5-min), daily PET (mm)", "No", "2019-08-22", "2020-01-18", "1 d / 5 min"),
         ]),
    dict(id="A34", folder="A34_Bengkalis_Kagawa2026", name="Bengkalis Island coastal peat: channel water level, surveys, weather (Riau)",
         status=DLP, license="CC-BY-4.0", links=[("Zenodo 19159832", "https://doi.org/10.5281/zenodo.19159832")],
         papers=[p("Kagawa et al. 2026, Biogeosciences 23", "10.5194/bg-23-2119-2026", OPEN,
                   "'The data for this paper is made available online at https://doi.org/10.5281/zenodo.19159833 (Kagawa et al., 2026).' "
                   "(19159833 and 19159832 are two DOIs of the same Zenodo record.)", "Yes (Zenodo)")],
         how=("Estimates particulate organic carbon export to the sea from coastal erosion and peat mass movements (PMMs, peat "
              "landslides) on Bengkalis Island, using RTK-GNSS surveys, peat cores, DTMs and satellite land-cover series. A HOBO U-20 "
              "logger in a PVC well recorded the CHANNEL water level behind a weir at WP1 (1 December 2014 - 31 January 2015): the "
              "level fell from 9.124 m to 7.896 m within 10 minutes on 27 December 2014, dating the weir breach that triggered a PMM."),
         notes=["WP1 is a waterway (channel) gauge, not a peat dipwell, and its values are ELEVATIONS (m above the survey datum; weir "
                "crest 9.00 m), not depths. No peat water-table series is in the dataset.",
                "The 2013 water-level survey and RTK files use UTM 48N; the transect lies at about 1.59-1.61 N, 102.02 E (north-west coast).",
                "Zenodo rate-limited this container: 8 of 33 files (metadata, carbon stocks, peat mass movement area-volume, vegetation and wind-wave tables) are missing; "
                "run `python3 download_data.py A34` locally. The partial error pages were renamed *.FAILED_403.html (git-ignored).",
                "Same island as C35 (Sutikno 2026) and the B9 SESAME station at Dompas."],
         files=[
             f("Water_level_WP1.csv", "Channel gauge WP1 (behind a weir)", "~1.6", "~102.0", "Waterway in coastal peat (mass-movement area)",
               "Channel water level (m, elevation)", "Channel level, not peat WTD", "2014-12-01 00:00", "2015-01-31 23:50", "10 min", 8927,
               "0 %", "6.47 / 7.67 / 9.17 m"),
             f("Water_level_24-08-2013.csv", "30 points along the survey line", "1.59-1.60", "102.02", "Coastal peat",
               "UTM N, E and water-level elevation (m) on one day", "Level (one survey)", "2013-08-24", "2013-08-24", "one survey", 30, "", "7.07-8.28 m"),
             f("Precipitation_Selat_Baru.csv", "Selat Baru", "", "", "", "Daily precipitation (mm)", "No", "2014-12-01", "2015-01-31", "1 d", 62),
             f("RTK_GNSS_*.csv (7), elevations of DTM.csv, peat core analysis_P1-P4.csv", "Survey lines and cores", "", "", "",
               "Ground elevations 2013-2016, DTM profile, peat properties", "No"),
             f("Perapat Tunggal_2018/2021_10minutes_csv.csv, Selatbaru_2018/2021_10minutes_csv.csv, Meteorological observations.csv", "Two stations",
               "", "", "", "10-min wind; monthly max wind and rainfall 2018-2021", "No", "2018-01", "2021-12"),
             f("Cumulative coastline retreat..., Landsat/Sentinel NDVI tables, vegetation-cover series", "", "", "", "", "Remote-sensing tables", "No"),
         ]),
    dict(id="D4", folder="D4_SEA_GWL_monthly_Hirano2025", name="Monthly GWL, NEE and peat decomposition by province and land use, 2011-2020 (your D4)",
         status=DL, license="CC BY 4.0", links=[("figshare 30761072 (Hirano 2025)", "https://doi.org/10.6084/m9.figshare.30761072")],
         papers=[p("Hirano et al. 2025, AGU Advances 6", "10.1029/2025AV001861", BLOCKED,
                   "Not read; the figshare record (T. Hirano, December 2025) matches the paper's scope (CO2 and CH4 from SE Asian peatlands, "
                   "GWL from satellite antecedent precipitation).", "Yes (figshare, probable)")],
         how=("The paper estimates spatio-temporal GWL from satellite antecedent precipitation and uses GWL-flux relations to "
              "compute net CO2 and CH4 emissions of about 180,000 km2 of SE Asian peatland under undrained forest, drained forest and "
              "plantation (abstract and press release)."),
         notes=["Values are modelled province means, not measurements: one sheet per variable and land use (Precipitation; GWL_, "
                "NEECO2_, NEECH4_, SoilRH_ for UndrainedPSF, DrainedPSF and MP), columns = 13 Indonesian provinces, 13 Malaysian "
                "states and Brunei.",
                "figshare blocks scripts; the file was saved with a headless browser."],
         files=[
             f("MonthlyData250816.xlsx", "Province / state means (27 regions)", "", "", "Undrained PSF", "Monthly GWL (m)",
               "Yes (model): " + NEG, "2011-01", "2020-12", "1 month", 120, "3 of 27 regions empty", "-1.07 / -0.16 / 0.09", part="GWL_UndrainedPSF"),
             f("MonthlyData250816.xlsx", "As above", "", "", "Drained PSF", "Monthly GWL (m)", "Yes (model): " + NEG, "2011-01", "2020-12",
               "1 month", 120, "5 of 27 regions empty", "-1.62 / -0.48 / -0.05", part="GWL_DrainedPSF"),
             f("MonthlyData250816.xlsx", "As above", "", "", "Plantation (MP)", "Monthly GWL (m)", "Yes (model): " + NEG, "2011-01", "2020-12",
               "1 month", 120, "0", "-1.34 / -0.61 / -0.39", part="GWL_MP"),
             f("MonthlyData250816.xlsx", "As above", "", "", "", "Monthly precipitation; NEE CO2 (Mg CO2 ha-1 month-1), NEE CH4, soil heterotrophic respiration",
               "No", "2011-01", "2020-12", "1 month", part="Precipitation, NEECO2_*, NEECH4_*, SoilRH_*"),
         ]),
    dict(id="D15", folder="D15_SouthSumatra_GWL_model_Irfan2026", name="Modelled 1-km GWL maps for South Sumatra peat units, wet and dry windows 2019",
         status=DL, license="CC-BY-4.0 (scripts MIT)", links=[("Zenodo 23008826", "https://doi.org/10.5281/zenodo.23008826")],
         papers=[],
         how=("A Ridge regression of Sentinel-1, GPM and SMAP predictors, calibrated on field GWL (BRGM SIPALAGA stations), was "
              "applied in Google Earth Engine to 23 scenes per window; scenes were aggregated to 1 km and median-composited. The "
              "accompanying article (Irfan et al., submitted to Science of the Total Environment) is not yet published."),
         notes=["The SIPALAGA field data used for calibration are NOT included (provider's access conditions).",
                "Same research group as B9 (Irfan 2020/2023) and C42 (Khakim 2022)."],
         files=[
             f("A09_FINAL_GWL_WET_1KM_KHG_SUMSEL.tif", "South Sumatra peat units (KHG), 20,921 cells", "", "", "All peat",
               "Modelled GWL, 1-13 April 2019 (m, EPSG:32748, 1 km)", "Yes (model): " + NEG, "2019-04-01", "2019-04-13", "composite", 20921, "",
               "-2.14 / -0.16 / 0.81"),
             f("A09_FINAL_GWL_DRY_1KM_KHG_SUMSEL.tif", "As above", "", "", "All peat", "Modelled GWL, 13-25 November 2019",
               "Yes (model): " + NEG, "2019-11-13", "2019-11-25", "composite", 20921, "", "-2.99 / -0.90 / 0.24"),
             f("A09_FINAL_DRYING_*.tif, A09_*UNCERTAINTY*.tif, A09_DRYING_BOOTSTRAP_*.tif, *.zip, *.csv, README.md", "", "", "", "",
               "Drying magnitude, bootstrap uncertainty, QA tables, model coefficients, GEE scripts", "Derived"),
         ]),
]

EXPANDED += [
    dict(id="C60", folder="C60_CentralKalimantan_Cassiophea2025",
         name="Five IoT WTD stations (RePEAT, CIMTROP forest, Ruslan Canal, KHDTK, KM 16), Central Kalimantan",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1088/1755-1315/1542/1/012023")],
         papers=[p("Cassiophea et al. 2025, IOP Conf. Ser.: Earth Environ. Sci. 1542", "10.1088/1755-1315/1542/1/012023", OPEN,
                   "No data availability statement; WTD is shown only in figures.", "No")],
         how=("Custom IoT stations (pressure transducer in a 2-3 m perforated PVC well, solar power, LTE upload) recorded WTD at hourly "
              "to daily intervals from November 2024 to April 2025 at RePEAT (rehabilitated reference), CIMTROP Lab Forest (little "
              "disturbed), Ruslan Canal (Sebangau NP, canal-blocked), KHDTK (forest under restoration) and KM 16 (restored shrubland); "
              "monthly manual readings with a water-level meter checked the sensors. Daily WTD was correlated with NASA POWER "
              "temperature, humidity and rainfall and with monthly soil samples (Ksat, bulk density, porosity): WTD responded weakly to "
              "daily rain, KM 16 stayed ponded (+20 to +40 cm) and KHDTK ranged from -40 to +25 cm."),
         notes=["Coordinates not given (map only, Fig. 1).",
                "Positive WTD = water above the surface in this paper.",
                "Co-author A. J. Jovani-Sancho (SUSTAINPEAT, A11); KHDTK is the Tumbang Nusa forest of your C20/C23."], files=[]),
    dict(id="C61", folder="C61_KFCP_Hikouei2025", name="KFCP dipwell network 2011-2019, Central Kalimantan (MODFLOW + XGBoost)",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1016/j.gsd.2025.101413")],
         papers=[p("Hikouei et al. 2025, Groundwater for Sustainable Development 29", "10.1016/j.gsd.2025.101413", ABS,
                   "The authors do not have permission to share the data.", "No")],
         how="A MODFLOW groundwater model of a degraded peat dome calibrated on monthly manual readings from 265 dipwells (2011-2019); XGBoost explained the residuals.",
         notes=["Extends B6 (KFCP, 300 dipwells 2010-2017) to 2019; same lead author as D12."], files=[]),
    dict(id="C62", folder="C62_Riau_Rokan_Yananto2021", name="SIPALAGA stations near the Rokan River, Riau (Sentinel-1 GWL model)",
         status=NODATA, license="", links=[("Article page", "https://ejournal.brin.go.id/ijreses/article/view/13780")],
         papers=[],
         how=("Groundwater levels 'measured using the Sipalaga instrument' in Acacia plantations near the Rokan River, Riau, were "
              "regressed on Sentinel-1 backscatter (VV linear model, r = -0.648) (article page; Int. J. Remote Sens. Earth Sci. 18(2), "
              "Yananto, Sartohadi, Marhaento, Awaluddin)."),
         notes=["No DOI shown; stations, period and time step not stated on the page."], files=[]),
    dict(id="C63", folder="C63_SungaiTohor_Sutikno2019", name="Canal block transect (5 dipwells, 20-220 m), Tebing Tinggi Island, Riau",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.1051/matecconf/201927606003")],
         papers=[p("Sutikno et al. 2019, MATEC Web of Conferences 276", "10.1051/matecconf/201927606003", BLOCKED,
                   "Not read.", "n/a")],
         how=("GWL monitored in five dipwells at 20, 70, 120, 170 and 220 m perpendicular to a canal block; rewetting raised the "
              "water table up to about 170 m from the canal (abstract and secondary reports)."),
         notes=["Same group and island as your C4 (Sutikno 2020) and C32."], files=[]),
    dict(id="C64", folder="C64_Jambi_Putra2024", name="Tangkit Baru and Pematang Rahim villages, Jambi: submersible sensors vs manual",
         status=NODATA, license="", links=[("Paper", "https://doi.org/10.29244/j-siltrop.15.01.65-69")],
         papers=[p("Putra et al. 2024, Journal of Tropical Silviculture 15", "10.29244/j-siltrop.15.01.65-69", OPEN,
                   "No data availability statement; GWL readings are shown in figures and on a Telkom IoT dashboard.", "No")],
         how=("September - November 2023: one IoT station per village (submersible pressure sensor read by an ESP32 microcontroller, "
              "sent to the Telkom IoT server) in a dipwell, compared with manual measuring-stick readings in the same dipwell; GPM "
              "daily rainfall from NASA. No significant difference between the methods (t-test, p > 0.05; offsets 0.1-1 cm); GWL rose "
              "with rain at Tangkit Baru but fell at Pematang Rahim."),
         notes=["Tangkit Baru (Sungai Gelam, Muaro Jambi): drained pineapple farms with 11 canals 1-2 m deep. Pematang Rahim (Mendahara "
                "Ulu, Tanjung Jabung Timur): next to the Sungai Buluh peat protection forest of A17. Coordinates not given (map only)."],
         files=[]),
    dict(id="C65", folder="C65_CentralKalimantan_Sekarano2026", name="26 GWL stations in Pulang Pisau and Palangka Raya (Sentinel-2 + LSTM), Central Kalimantan",
         status=NODATA, license="", links=[("Preprint", "https://doi.org/10.2139/ssrn.7439436")],
         papers=[p("Sekarano et al. 2026, SSRN preprint", "10.2139/ssrn.7439436", ABS, "Not read.", "n/a")],
         how=("21,954 GWL observations from 26 quality-controlled stations (December 2018 - December 2022) combined with Sentinel-2 "
              "bands and moisture indices; LSTM reached R2 0.89 and RMSE about 0.13 m and mapped the 2019 dry-season drawdown (abstract)."),
         notes=["Station network not named in the abstract; with BRIN (Sulaiman) and Hirano as co-authors it is probably SIPALAGA "
                "(your A25/A27, B1)."], files=[]),
]


# ---------------------------------------------------------------------- your table
# Rows of SEA_peatland_WTD_datasets.xlsx (October 2026 upload) that repeat an existing entry. (your ID, same as, note)
DUPLICATES = [
    ("A23", "C19", "Same study (Putra et al. 2021); A23 adds the public Leeds data. Keep A23, mark C19 as replicate."),
    ("A24", "B4", "Same paper and station (Sulaiman et al. 2023); no public data (BRIN release promised)."),
    ("A25", "B1, B13", "SIPALAGA network; Hein et al. 2022 used 167 stations for 2019 (25 oil palm stations in East Sumatra)."),
    ("A26", "B13", "Putra et al. 2025 is the second paper of B13 (39 Riau stations)."),
    ("A27", "B1", "Mleczko et al. 2025 (RSE) is the use-case paper already cited in B1."),
    ("A28", "A15, A4 rows 9-10", "Melling & Wong 2024 figshare = the data file of A15 (already downloaded)."),
    ("A29", "C36", "Same paper (Jauhiainen et al. 2012)."),
    ("A30", "B8, C2", "Same paper (Hooijer et al. 2012)."),
    ("A31", "B8, C2", "Same paper (Evans et al. 2019); C2 already cites it."),
    ("A32", "C29", "Same paper (Basuki et al. 2021)."),
    ("A33", "B2", "Same system (SiMATAG-0.4m, KLHK)."),
    ("D9", "D2", "Same model output (PEATCLSM_Trop, Zenodo 6011689); D9 adds the list of 87 evaluation sites."),
    ("D10", "D3", "Same paper (Koupaei-Abyazani et al. 2024)."),
]

# Cell corrections for your table and EXPANDED_2006-2026.xlsx: (ID, row, column, new value, source[, only]).
# row: text found in the site, province, land-use or method cell of one of the ID's rows ('' = the first row; a leading
# '*' = every row containing the rest, '*' alone = every row). Column "Colour" sets the fill (the value starts with a
# legend label); column "New row" adds a row (value = the 12 cells from "Site / dataset" to "Wells").
# only: "table" = your table only, "expanded" = EXPANDED_2006-2026.xlsx only (where the two differ).
TABLE_FIXES = [
    ("A15", "Naman", "Period", "2018/03/01-2019/05/31", "data file (MA_converted_daily_WT_data.xlsx)"),
    ("A15", "", "Data link", "https://doi.org/10.6084/m9.figshare.25299358", "Koupaei-Abyazani 2024 data statement"),
    ("A15", "", "Colour", "replicate (= your A28: the same public figshare file)", "figshare 25299358"),
    ("A17", "", "Temporal resolution", "15 min loggers, 1 per site (plot readings fortnightly, published only as 12-month plot summaries)",
     "Warren-Thomas 2022 methods; Dryad files"),
    ("A17", "", "Period", "2018/08-2019/08 (manual); 2018/08/28-2019/07/14 (loggers)", "Dryad file"),
    ("A17", "", "Source", "approximated (paper and dataset give no coordinates)", "paper, Dryad README", "table"),
    ("A17", "*", "Latitude", "Not given (paper map only)", "paper, Dryad README", "expanded"),
    ("A17", "*", "Longitude", "Not given (paper map only)", "paper, Dryad README", "expanded"),
    ("A18", "Undrained", "Latitude", "FOR-1 -2.8235; FOR-2 -2.8224; FOR-3 -2.8475", "Swails 2021, Table 1"),
    ("A18", "Undrained", "Longitude", "FOR-1 111.8131; FOR-2 111.8406; FOR-3 111.8026", "Swails 2021, Table 1"),
    ("A18", "Oil palm", "Latitude", "OP-2011 -2.7897; OP-2009 -2.7882; OP-2007 -2.7872", "Swails 2021, Table 1"),
    ("A18", "Oil palm", "Longitude", "OP-2011 111.8104; OP-2009 111.8032; OP-2007 111.8015", "Swails 2021, Table 1"),
    ("A18", "Undrained", "Period", "2014/01-2015/09 (no monitoring Jul-Aug 2014)", "Swails 2021, Figs 2-3"),
    ("A18", "Oil palm", "Period", "2014/01-2015/09 (no monitoring Jul-Aug 2014)", "Swails 2021"),
    ("A18", "", "Colour", "replicate (same plots and campaign as your A14)", "Swails 2021 cites Swails 2019 for the physical variables"),
    ("A19", "", "Source publication(s)", "Swails et al. 2023, Biogeochemistry (DATA.00290); Swails et al. 2026, Geoderma (DATA.00330/00331); Hergoualc'h et al. 2026, R. Soc. Open Sci. (DATA.00316); Comeau et al. 2016", "Crossref titles of the CIFOR records"),
    ("A19", "", "Publication link(s)", "https://doi.org/10.1007/s10533-023-01070-7 ; https://doi.org/10.1016/j.geoderma.2026.118030 ; https://doi.org/10.1098/rsos.252443 ; https://doi.org/10.1016/j.geoderma.2016.01.016", "Crossref"),
    ("A19", "", "Method / accuracy", "WTD in 2 m PVC dipwells next to each collar, monthly (+ daily after fertilisation)", "Swails 2023 methods"),
    ("A19", "", "Period", "2011/10-2013/03 (Swails 2023); 2012-2013 (Swails 2026)", "Swails 2023, 2026"),
    ("A19", "", "New row", ("Berbak National Park primary forest", "Indonesia", "Jambi (Berbak NP)", -1.45, 104.35,
                            "literature (1 27 S, 104 21 E)", "Primary peat swamp forest", "2011/10-2013/03", "Monthly",
                            "WTD in 2 m PVC dipwell next to each collar", 1, ""), "Swails 2023"),
    ("A19", "", "New row", ("Logged and drained forest", "Indonesia", "Jambi", -1.65, 103.8667, "literature (about 1 39 S, 103 52 E)",
                            "Logged, drained peat swamp forest", "2011/10-2013/03", "Monthly", "As above", 1, ""), "Swails 2023"),
    ("A20", "", "Data link", "DOIs not registered (doi.org: 'DOI does not exist'); check data.cifor.org locally", "doi.org, Crossref"),
    ("A21", "*", "Period", "2014/10-2014/12 (three wet-season campaigns)", "Cooper 2020 methods"),
    ("A21", "*", "Temporal resolution", "At each GHG sampling (5 per class); monthly at 2 forest dipwells (not published)", "Cooper 2020 methods; Source Data"),
    ("A21", "*", "Latitude", "Not given in paper", "Cooper 2020"),
    ("A21", "*", "Longitude", "Not given in paper", "Cooper 2020"),
    ("A22", "", "Source publication(s)", "Somers et al. 2023, JGR Biogeosciences 128", "Crossref"),
    ("A22", "", "Publication link(s)", "https://doi.org/10.1029/2022JG007194", "Crossref"),
    ("A22", "", "Period", "2020/01/24-2020/12/16 (culvert loggers)", "HydroShare files"),
    ("A22", "", "Temporal resolution", "15 min", "HydroShare files"),
    ("A23", "", "Latitude", "Forested -2.3894; Blocked/Drained about -2.36", "Putra 2023"),
    ("A23", "", "Longitude", "Forested 113.4524; Blocked/Drained about 114.09", "Putra 2023"),
    ("A23", "", "Period", "2019/08/23-2020/01/25 (loggers); manual 2019/09-2020/01", "Leeds files"),
    ("A23", "", "Temporal resolution", "3-hourly (well loggers); 30 min (ditch loggers); manual visits", "Leeds files"),
    ("A23", "", "Wells", "13 well loggers (6 forest, 4 blocked, 3 drained) + 4 ditch loggers + 30 manual points", "Leeds files"),
    ("A23", "", "Method / accuracy", "Vented In-Situ Level TROLL 500 (wells); Diver + barologger (ditches); logger values are levels relative to a site benchmark", "Putra 2023; Leeds readme"),
    ("A24", "", "Wells", "1 station (pressure sensor)", "Sulaiman 2023"),
    ("A24", "", "Data link", "None public; monthly data to be released via BRIN", "Sulaiman 2023 data statement"),
    ("A24", "", "Colour", "replicate (= B4)", ""),
    ("A25", "", "Method / accuracy", "Daily water levels of 167 SIPALAGA stations for 2019 downloaded by Hein et al.; 25 oil palm stations (East Sumatra) used: mean drainage 81 +/- 50 cm", "Hein 2022"),
    ("A25", "", "Latitude", "See B13 (59 stations with coordinates, Apers 2022 Table B1)", ""),
    ("A26", "", "Publication link(s)", "https://doi.org/10.26554/ijems.2025.9.2.46-55", "Crossref"),
    ("A26", "", "Wells", "39 stations (one sensor each)", "Putra 2025"),
    ("A26", "", "Latitude", "Map only (Putra 2025, Fig. 2)", "Putra 2025"),
    ("A27", "", "Source publication(s)", "Mleczko et al. 2025, Remote Sensing of Environment", "Crossref"),
    ("A27", "", "Publication link(s)", "https://doi.org/10.1016/j.rse.2025.115009", "Crossref"),
    ("A27", "", "Period", "2017-2022 (SAR period)", "Mleczko 2025 abstract"),
    ("A27", "", "Sites", "8 (not verified: full text blocked)", ""),
    ("A28", "", "Latitude", "Undrained 1.4536; converted 2.1860", "Koupaei-Abyazani 2024, Table 1"),
    ("A28", "", "Longitude", "Undrained 111.1494; converted 111.8459", "Koupaei-Abyazani 2024, Table 1"),
    ("A28", "", "Period", "2011/01/01-2014/12/31 (undrained); 2018/03/01-2019/05/31 (converted)", "data files"),
    ("A29", "", "Province / state", "Riau (Kampar Peninsula, APRIL Acacia plantation)", "Jauhiainen 2012"),
    ("A29", "", "Period", "2007/04-2009/04", "Jauhiainen 2012"),
    ("A29", "", "Temporal resolution", "Monthly or quarterly manual", "Jauhiainen 2012"),
    ("A29", "", "Sites", "8 transects, 144 locations", "Jauhiainen 2012"),
    ("A30", "", "Latitude", "Acacia about 0.595; oil palm about -1.566", "Hooijer 2012, Table 1"),
    ("A30", "", "Longitude", "Acacia about 102.334; oil palm about 103.601", "Hooijer 2012, Table 1"),
    ("A30", "", "Period", "2007/09-2010/08 (Acacia); 2009/07-2010/06 (oil palm)", "Hooijer 2012"),
    ("A30", "", "Temporal resolution", "Repeated manual; 2-weekly in oil palm", "Hooijer 2012"),
    ("A30", "", "Sites", "125 Acacia + 42 oil palm locations + drained forest", "Hooijer 2012"),
    ("A31", "", "Period", "2010-2016", "Evans 2019"),
    ("A31", "", "Temporal resolution", "Manual WTD at each pole visit", "Evans 2019"),
    ("A31", "", "Sites", "312 records analysed (447 poles; 322 with >= 3 years)", "Evans 2019"),
    ("A32", "", "Period", "2017/12-2019/05", "Basuki 2021"),
    ("A32", "", "Temporal resolution", "Monthly (metal measuring stick)", "Basuki 2021"),
    ("A32", "", "Province / state", "Riau (Siak: Dosan and Dayun villages)", "Basuki 2021"),
    ("A33", "", "Sites", "9,603 compliance points (KLHK, 2019); '~11,000' not confirmed", "KLHK press release 2019"),
    ("B5", "", "Data link", "http://kalimantan88.sakura.ne.jp/ (offline: host no longer resolves)", "checked 2026-10-09"),
    ("B6", "", "Period", "2010-2017 (Putra 2019); 2011-2019 (Hikouei 2025)", "Putra 2019; Hikouei 2025"),
    ("B6", "", "Wells", "300 dipwells (265 in Hikouei 2025)", "Putra 2018/2019; Hikouei 2025"),
    ("B8", "", "Province / state", "Riau (Acacia); Jambi (oil palm, Hooijer 2012)", "Hooijer 2012"),
    ("B9", "SR1", "Latitude", -2.911, "Irfan 2020"), ("B9", "SR1", "Longitude", 105.082, "Irfan 2020"),
    ("B9", "SR2", "Latitude", -2.677, "Irfan 2020"), ("B9", "SR2", "Longitude", 105.143, "Irfan 2020"),
    ("B9", "LR1", "Latitude", -3.143, "Irfan 2020"), ("B9", "LR1", "Longitude", 105.184, "Irfan 2020"),
    ("B9", "LR2", "Latitude", -3.458, "Irfan 2020"), ("B9", "LR2", "Longitude", 104.921, "Irfan 2020"),
    ("B9", "*River", "Period", "2017/07/01-2019/08/05", "Irfan 2020 (all four stations)"),
    ("B9", "Dompas", "Period", "2018/04-2019/06", "Pratama 2020"),
    ("B10", "", "Temporal resolution", "Monthly means (50 stations)", "Khampeera 2018"),
    ("B10", "", "Period", "2010 and 2012 analysed", "Khampeera 2018"),
    ("C19", "", "Data link", "https://doi.org/10.5518/960 (see A23)", "Leeds repository"),
    ("C19", "", "Colour", "replicate (= A23)", ""),
    ("C22", "", "Temporal resolution", "3-hourly camera images", "Sulaeman 2022"),
    ("C25", "", "Period", "2020/02/14, 2020/02/28 and 2020/08 (spot readings)", "Suwito 2022"),
    ("C26", "*", "Temporal resolution", "Hourly GWL (2014/01-2015/12)", "Itoh 2017 (all three plots)"),
    ("C27", "primary", "Province / state", "Riau (Siak: Zamrud NP)", "Maryani 2020"),
    ("C27", "primary", "Latitude", -0.715, "Maryani 2020 (0 42 54 S)"), ("C27", "primary", "Longitude", 102.2264, "Maryani 2020 (102 13 35 E)"),
    ("C27", "ex-fire", "Latitude", -0.8711, "Maryani 2020"), ("C27", "ex-fire", "Longitude", 102.3394, "Maryani 2020"),
    ("C27", "mixed", "Latitude", -0.8764, "Maryani 2020"), ("C27", "mixed", "Longitude", 102.3447, "Maryani 2020"),
    ("C27", "*", "Period", "2018 (4-month logger record; rain events analysed 2018/04/08-2018/06/08)", "Suryatmojo 2019"),
    ("C28", "primary", "Latitude", -0.715, "Maryani 2020"), ("C28", "primary", "Longitude", 102.2264, "Maryani 2020"),
    ("C28", "burnt", "Latitude", -0.8711, "Maryani 2020"), ("C28", "burnt", "Longitude", 102.3394, "Maryani 2020"),
    ("C28", "mixed", "Latitude", -0.8764, "Maryani 2020"), ("C28", "mixed", "Longitude", 102.3447, "Maryani 2020"),
    ("C27", "ex-fire", "Province / state", "Riau (Siak: Sungai Rawa village, Sungai Apit)", "Suryatmojo 2019; Maryani 2020"),
    ("C27", "mixed", "Province / state", "Riau (Siak: Sungai Rawa village, Sungai Apit)", "Suryatmojo 2019; Maryani 2020"),
    ("C28", "primary", "Province / state", "Riau (Siak: Zamrud NP)", "Maryani 2020"),
    ("C28", "burnt", "Province / state", "Riau (Siak: Sungai Rawa village, Sungai Apit)", "Maryani 2020"),
    ("C28", "mixed", "Province / state", "Riau (Siak: Sungai Rawa village, Sungai Apit)", "Maryani 2020"),
    ("C29", "*", "Period", "2017/12-2019/05", "Basuki 2021"),
    ("C29", "*", "Temporal resolution", "Monthly (metal measuring stick)", "Basuki 2021"),
    ("C31", "", "Province / state", "Riau (Siak: Bunsur village)", "Safitri 2024"),
    ("C31", "", "Period", "2022/04-2023/03", "Safitri 2024"),
    ("C32", "", "Temporal resolution", "Twice monthly at 66 wells (2019/02-06); daily logger (1 year, Malik 2022)", "Silviana 2020; Malik 2022"),
    ("C34", "", "Temporal resolution", "30 min logger + manual at each N2O sampling", "Nardi 2021"),
    ("C36", "", "Province / state", "Riau (Kampar Peninsula)", "Jauhiainen 2012"),
    ("C36", "", "Period", "2007/04-2009/04", "Jauhiainen 2012"),
    ("C37", "natural", "Period", "2017/06-2019/05", "Deshmukh 2020"),
    ("C37", "Acacia", "Period", "2016/10-2019/05", "Deshmukh 2020"),
    ("C37", "*", "Temporal resolution", "30 min GWL logger + fortnightly manual GWL", "Deshmukh 2020"),
    ("C40", "", "Province / state", "Central Kalimantan (Jabiren)", "Wakhid 2017"),
    ("C40", "", "Latitude", -2.4972, "Wakhid 2017 (2 29 50 S)"), ("C40", "", "Longitude", 114.1889, "Wakhid 2017 (114 11 20 E)"),
    ("C40", "", "Period", "2014/06-2015/12 (GWL); 2014/12-2015/12 (CO2)", "Wakhid 2017"),
    ("C40", "", "Temporal resolution", "Hourly GWL", "Wakhid 2017"),
    ("C42", "", "Temporal resolution", "10 min (SESAME)", "Khakim 2022"),
    ("C43", "Kubu village", "Period", "2021/09/01-2021/09/30", "Nusantara 2023"),
    ("C43", "Kubu Raya", "Period", "2016/03-2016/12 (weekly)", "Astiani 2018"),
    ("C45", "", "Latitude", -3.4053, "Wakhid 2021 (3 24 19 S)"), ("C45", "", "Longitude", 114.7697, "Wakhid 2021 (114 46 11 E)"),
    ("C47", "", "Period", "2020/08-2021/01", "Suhip 2024"),
    ("C47", "", "Temporal resolution", "20 min", "Suhip 2024"),
    ("C47", "", "Wells", "13 piezometers (peat and sand) on 2 transects", "Suhip 2024"),
    ("C50", "", "Latitude", "MPS 1.4309; Alan Batu 1.4535; Alan Bunga 1.4633", "Imran 2022, Table 1"),
    ("C50", "", "Longitude", "MPS 111.1311; Alan Batu 111.1493; Alan Bunga 111.1581", "Imran 2022, Table 1"),
    ("C50", "", "Period", "2011/02-2020/12", "Imran 2022"),
    ("C50", "", "Temporal resolution", "30 min loggers (published as monthly means)", "Imran 2022"),
    ("C50", "", "Colour", "on request", "Imran 2022 data statement"),
    ("C51", "automated chambers", "Latitude", 2.1833, "Ishikura 2018 (2 11 N, 111 50 E)"),
    ("C52", "", "Temporal resolution", "About weekly (dipmeter)", "Cook 2018"),
    ("C52", "", "Period", "2015/08-2016/09", "Cook 2018"),
    ("C55", "Ayer Hitam", "Temporal resolution", "Cera-Diver loggers (W2, W4 from 2015/06; W6 from 2016/05) + manual wells", "Shamsuddin 2021"),
    ("C56", "", "Latitude", 6.4833, "Nagano 2013 (Bacho 6 29 N)"), ("C56", "", "Longitude", 101.75, "Nagano 2013 (101 45 E)"),
    ("C56", "", "Period", "1983/07-2006/01 (monthly)", "Nagano 2013"),
    ("C57", "", "Method / accuracy", "No water-table measurements (peat cores only)", "Decena 2021"),
    ("D4", "", "Data link", "https://doi.org/10.6084/m9.figshare.30761072 (monthly province means 2011-2020)", "figshare (Hirano, Dec 2025)"),
    ("D11", "", "Data link", "https://doi.org/10.17632/7nnf495jbw ; https://doi.org/10.25740/yj761xk5815", "Mendeley; Stanford SDR"),
    ("D12", "", "Source publication(s)", "Hikouei et al. 2023, STOTEN; Hikouei et al. 2025, Groundwater for Sustainable Development", "Crossref"),
    ("D14", "", "Data link", "https://doi.org/10.17528/CIFOR/DATA.00291 (replication data of Swails et al. 2024)", "Crossref"),
    # second pass: cells still 'See paper' although the paper was read in full ("Not given" = the paper does not state it)
    ("B9", "Dompas", "Latitude", "Not given in paper (Dompas village, Bengkalis)", "Pratama 2020"),
    ("B9", "Dompas", "Longitude", "Not given in paper", "Pratama 2020"),
    ("B9", "", "New row", ("SESAME station OKI-1 (Ogan Komering Ilir)", "Indonesia", "South Sumatra (OKI)", -3.4786, 104.9651, "literature",
                           "Hemic peat close to canals", "2019-2020", "Sub-daily / daily", "SESAME automatic GWL sensor", 1, ""), "Irfan 2023"),
    ("B9", "", "New row", ("SESAME station OKI-2 (Ogan Komering Ilir)", "Indonesia", "South Sumatra (OKI)", -3.3925, 104.9775, "literature",
                           "Hemic peat dome", "2019-2020", "Sub-daily / daily", "SESAME automatic GWL sensor", 1, ""), "Irfan 2023"),
    ("B11", "", "Temporal resolution", "Not given in paper (park monitoring records 2002-2021)", "Thai 2024"),
    ("C16", "", "Temporal resolution", "Not given in Jaenicke 2010 (dipwell series used to calibrate a daily model)", "Jaenicke 2010; other papers not read"),
    ("C16", "", "Sites", "Jaenicke 2010: 1 calibration dipwell at -2.323, 113.903 (other papers not read)", "Jaenicke 2010, Fig. 3"),
    ("C18", "*", "Temporal resolution", "Observed series in Annex I of the paper; SWAP model daily", "Taufik 2019"),
    ("C19", "Forested", "Latitude", -2.3894, "Putra 2023 (benchmark at well AL0)"),
    ("C19", "Forested", "Longitude", 113.4524, "Putra 2023 (benchmark at well AL0)"),
    ("C19", "Blocked", "Latitude", "≈-2.36 (3.5 km from Tumbang Nusa camp, -2.3556)", "Putra 2023"),
    ("C19", "Blocked", "Longitude", "≈114.09 (Tumbang Nusa camp 114.0896)", "Putra 2023"),
    ("C19", "Drained", "Latitude", "≈-2.36 (2.7 km from Tumbang Nusa camp, -2.3556)", "Putra 2023"),
    ("C19", "Drained", "Longitude", "≈114.09 (Tumbang Nusa camp 114.0896)", "Putra 2023"),
    ("C19", "*", "Temporal resolution", "3-hourly (well loggers); 30 min (ditch loggers)", "Putra 2023; Leeds files (A23)"),
    ("C22", "", "Latitude", "Not given in paper", "Sulaeman 2022"), ("C22", "", "Longitude", "Not given in paper", "Sulaeman 2022"),
    ("C23", "*", "Latitude", "Not given in paper", "Yulianti 2024"), ("C23", "*", "Longitude", "Not given in paper", "Yulianti 2024"),
    ("C25", "", "Latitude", "Not given in paper (Blocks E and B of the ex-MRP)", "Suwito 2022"), ("C25", "", "Longitude", "Not given in paper", "Suwito 2022"),
    ("C25", "", "Temporal resolution", "Manual, 2nd and 4th week of February and August 2020", "Suwito 2022"),
    ("C27", "*", "Temporal resolution", "Automatic GWL sensor (interval not stated)", "Suryatmojo 2019"),
    ("C28", "*", "Temporal resolution", "Automatic water-level recorder (interval not stated)", "Maryani 2020"),
    ("C29", "Dosan", "Latitude", "Not given in paper (map only)", "Basuki 2021"), ("C29", "Dosan", "Longitude", "Not given in paper (map only)", "Basuki 2021"),
    ("C31", "", "Latitude", "Not given in paper (map only)", "Safitri 2024"), ("C31", "", "Longitude", "Not given in paper (map only)", "Safitri 2024"),
    ("C31", "", "Temporal resolution", "Twice a month (manual measuring stick)", "Safitri 2024"),
    ("C31", "", "Sites", "Transects in oil palm, rubber, sago and shrub; wells 5, 100, 400 and 900 m from blocked and unblocked canals", "Safitri 2024"),
    ("C32", "", "Latitude", "Not given in paper (map only)", "Silviana 2020; Malik 2022"), ("C32", "", "Longitude", "Not given in paper (map only)", "Silviana 2020; Malik 2022"),
    ("C36", "", "Latitude", 0.4353, "Jauhiainen 2012 (N 0 26 06.9)"), ("C36", "", "Longitude", 101.8837, "Jauhiainen 2012 (E 101 53 01.4)"),
    ("C41", "", "Latitude", "Not given in paper", "Khasanah 2019"), ("C41", "", "Longitude", "Not given in paper", "Khasanah 2019"),
    ("C41", "", "Temporal resolution", "Monthly (PVC tubes 2 m from the subsidence points)", "Khasanah 2019"),
    ("C42", "Sugihan", "Latitude", "Not given in paper", "Khakim 2022"), ("C42", "Sugihan", "Longitude", "Not given in paper", "Khakim 2022"),
    ("C42", "Sugihan", "Sites", "2 SESAME stations (NBL2, BS2)", "Khakim 2022"),
    ("C42", "revegetati", "Latitude", -3.1634, "Maryani 2021"), ("C42", "revegetati", "Longitude", 104.5461, "Maryani 2021"),
    ("C42", "revegetati", "Period", "2020/09/02-2020/10/07", "Maryani 2021"),
    ("C42", "revegetati", "Temporal resolution", "Every 7 days (manual)", "Maryani 2021"),
    ("C42", "revegetati", "Sites", "1 observation box (3 x 3 m)", "Maryani 2021"),
    ("C43", "Kubu Raya bare", "Latitude", "Not given in paper", "Astiani 2018"), ("C43", "Kubu Raya bare", "Longitude", "Not given in paper", "Astiani 2018"),
    ("C43", "Kubu Raya bare", "Temporal resolution", "Weekly", "Astiani 2018"),
    ("C43", "Kubu Raya bare", "Sites", 1, "Astiani 2018"),
    ("C43", "Kubu Raya bare", "Wells", "12 piezometers", "Astiani 2018"),
    ("C43", "Kubu village", "Latitude", "Not given in paper", "Nusantara 2023"), ("C43", "Kubu village", "Longitude", "Not given in paper", "Nusantara 2023"),
    ("C43", "Kubu village", "Wells", "9 piezometers (3 blocks x 250, 500, 750 m)", "Nusantara 2023"),
    ("C51", "automated chambers", "Longitude", 111.8333, "Ishikura 2018 (2 11 N, 111 50 E)"),
    ("C55", "Ayer Hitam", "Latitude", 2.0574, "Shamsuddin 2021"), ("C55", "Ayer Hitam", "Longitude", 102.8061, "Shamsuddin 2021"),
    ("C55", "Ayer Hitam", "Period", "From 2015/06 (W2, W4; W6 from 2016/05); 2016 analysed", "Shamsuddin 2021"),
    ("C57", "", "Latitude", "Not given in paper (map only)", "Decena 2021"), ("C57", "", "Longitude", "Not given in paper (map only)", "Decena 2021"),
    ("C57", "", "Period", "2020/11-2021/02 (core sampling)", "Decena 2021"),
    ("C57", "", "Sites", "11 peat cores", "Decena 2021"),
    ("D10", "", "Latitude", "IN-undrained -2.32; IN-drained -2.35; MA-undrained 1.4536; MA-converted 2.1860 (+ 2 Peru sites)", "Koupaei-Abyazani 2024, Table 1"),
    ("D10", "", "Longitude", "IN-undrained 113.90; IN-drained 114.04; MA-undrained 111.1494; MA-converted 111.8459", "Koupaei-Abyazani 2024, Table 1"),
    ("D10", "", "Period", "IN-undrained 2015-2018; IN-drained 2013-2017; MA-undrained 2011-2014; MA-converted 2018-2019", "Koupaei-Abyazani 2024"),
    ("D10", "", "Sites", "4 in SE Asia + 2 in Peru", "Koupaei-Abyazani 2024, Table 1"),
]


# Found by the October 2026 search, checked, and not added: (item, link, what it is, why it was left out)
CHECKED_NOT_ADDED = [
    ("Melling & Wong 2023, figshare 22355035", "https://doi.org/10.6084/m9.figshare.22355035",
     "'Groundwater level data for two peatland sites in Malaysia'", "28 + 18 single-day values on Landsat dates; a subset of the 2024 files in A15 (your A28)"),
    ("Hirano 2023, figshare 23820780", "https://doi.org/10.6084/m9.figshare.23820780",
     "Eddy fluxes, meteorology and groundwater at three Central Kalimantan peatlands (CC BY 4.0)",
     "Probably the data you already have in A3: same author and description, one zip of nearly the same size (16,485,156 vs "
     "16,486,299 bytes); not downloaded"),
    ("JapanFlux2024 (Ueyama et al. 2025, ESSD 17, 3807)", "https://essd.copernicus.org/articles/17/3807/2025/",
     "Harmonised flux data incl. the Palangkaraya towers (CC BY 4.0, no login)", "No water-table variable; adds only fluxes for A3/A5"),
    ("Sebangau temperature data, figshare 14900181", "https://doi.org/10.6084/m9.figshare.14900181",
     "Peat temperature at the A23 sites (MIT licence)", "No water table"),
    ("DigiBog model files, Leeds 10.5518/1053", "https://doi.org/10.5518/1053",
     "Model inputs, settings and outputs for typical Sebangau conditions", "Model output, not measurements"),
    ("Rian Fitra et al. 2026, Zenodo 22183066", "https://doi.org/10.5281/zenodo.22183066",
     "South Sumatra peat-fire case-control data with Sentinel-1 backscatter", "No water-table measurements"),
    ("GEMS-GER, Zenodo 16735830", "https://zenodo.org/records/16735830",
     "Machine-learning benchmark of weekly groundwater levels at 3,000+ German wells", "Not peat, not SE Asia (only a template for ML-ready data)"),
    ("South Sumatra peat portal: TMAT observation points", "https://datagambut.sumselprov.go.id/layers/geonode:tp_tmat_perkebunan",
     "GeoNode layers of plantation (perkebunan) and HTI compliance points for the 0.4 m water-table rule (metadata Nov 2022)",
     "Point locations only, no water-table values; part of SiMATAG (B2, your A33)"),
    ("KLHK SiMATAG press release, 18 June 2019",
     "https://mail.ppkl.menlhk.go.id/website/filebox/600/190618152629Press%20Release%20SiMATAG%2018%20Juni%202019%20REV.docx",
     "9,603 compliance points, updated through a mobile app", "Not public; used to check your A33 count"),
    ("Greer et al. 2005, Hydrological assessment of the Klias Forest Reserve", "https://agris.fao.org/search/fr/records/64738d3dce9437aa76fed7d1",
     "Monitoring programme from October 2002 (Sabah)", "Before 2006; report not online, no data"),
    ("BGR/NAWAPI Technical Note TN-IV-01 (2021)", "https://www.bgr.bund.de/EN/Themen/Wasser/Projekte/abgeschlossen/TZ/Vietnam/techn_noteIV-01_en.pdf",
     "Groundwater-level monitoring at the U Minh well group, Mekong Delta", "Aquifer wells, not the peat water table (context for B11)"),
    ("PeatDataHub (PEAT-ECR)", "https://peatecr.com/p-e-a-t-resources/peatdata/",
     "Planned global network of peat site metadata and WTD; contributors set access", "No open tropical WTD series found"),
    ("ACIAR SLAM/2020/118 final report (2024)", "https://www.aciar.gov.au/publication/slam-2020-118-final-report",
     "Eddy covariance and soil-water sensors on a regenerating degraded peatland, Indonesia", "Project report; no water-table data released"),
    ("GEC rewetting projects (Raja Musa, Pekan)", "https://gec.org.my/wp-content/uploads/2024/01/2015_gec_infosheet_fcp-rmfr_02.pdf",
     "Canal blocking in Raja Musa and Pekan forest reserves, Malaysia", "Project sheets only; no published water-table series (see B12)"),
]
