#!/usr/bin/env python3
"""Write DATA_SUMMARY.md, DATA_SUMMARY.xlsx and a README.md in every dataset folder.

All facts live in the DATASETS list below. Periods, time steps and value ranges were measured from the
downloaded files (2026-09-26); descriptions of methods and use come from the papers. Edit the list and
re-run (needs openpyxl) after adding new files, e.g. the FLUXNET-CH4 downloads.
"""
import os

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKED = "2026-09-26"

# status codes shown in the tables
DL = "Downloaded"
DLP = "Downloaded (part of the data)"
LOGIN = "Needs your login (FLUXNET)"
EMB = "Embargoed / on request"
UNREACH = "Public, but server unreachable from the cloud"
NODATA = "No public data"


def f(file, site, lat, lon, cover, content, wtd, start="", end="", step="", n="", miss="", rng="", note="", part=""):
    return dict(file=file, part=part, site=site, lat=lat, lon=lon, cover=cover, content=content, wtd=wtd,
                start=start, end=end, step=step, n=n, miss=miss, rng=rng, note=note)


NEG = "m; negative = below peat surface"
NEG_CM = "cm; negative = below peat surface"

DATASETS = [
    dict(
        id="A1", folder="A1_Mendaram_Cobb2019", name="Mendaram peat dome (undrained), Brunei",
        status=DL, license="CC-BY-4.0",
        links=[("PANGAEA collection", "https://doi.org/10.1594/PANGAEA.908215")],
        papers=[dict(cite="Cobb & Harvey 2019, Water Resources Research 55", doi="10.1029/2019WR025411",
                     access="Open (publisher author manuscript); Wiley blocks scripts, open in a browser",
                     da="Not read (Wiley blocked automated access). The PANGAEA README states the collection is the data used in this paper.",
                     da_dl="Yes")],
        how=("Four piezometers (Solinst Levelogger Edge, barometrically corrected, screened 1.30-1.45 m) logged water level every "
             "20 min for a year, together with throughfall from four tipping-bucket gauges. Combined with the peat-surface "
             "Laplacian from the flowtube geometry, the water-level and throughfall series were used to fit hillslope-scale "
             "hydraulic conductivity (transmissivity) and specific yield as functions of water-table height, for a 'scalar' "
             "model that treats a peatland subcatchment as one storage unit. The fitted K and Sy knots are published as "
             "PANGAEA 908209 and 908210."),
        notes=["The PANGAEA metadata query lists only 4 children; the 4 water-level series (908201, 908206-908208) were "
               "found from the collection page and added.",
               "README_Brunei_peat_swamp_data.pdf (dataset documentation, CC-BY) is downloaded but not committed because PDFs "
               "are git-ignored; download_data.py fetches it."],
        files=[
            f("PANGAEA_908201.tab", "Piezometer 'mdm trail 6'", 4.365371, 114.353709, "Undrained peat swamp forest (dome)",
              "Water level WL (m)", "Yes: m relative to the peat-surface datum of Cobb et al. 2017; + = above surface",
              "2012-02-06 22:20", "2013-01-30 02:40", "20 min", 25790, "0 %", "-0.305 / -0.014 / 0.190"),
            f("PANGAEA_908206.tab", "Piezometer 'mdm trail 7'", 4.368423, 114.354127, "Undrained peat swamp forest (dome)",
              "Water level WL (m)", "Yes: as above", "2012-02-06 22:20", "2013-01-30 02:40", "20 min", 25790, "0 %",
              "-0.294 / -0.014 / 0.179"),
            f("PANGAEA_908207.tab", "Piezometer 'mdm trail 8'", 4.371105, 114.354700, "Undrained peat swamp forest (dome)",
              "Water level WL (m)", "Yes: as above", "2012-02-06 22:20", "2013-01-30 02:40", "20 min", 25789, "0 %",
              "-0.309 / -0.014 / 0.184"),
            f("PANGAEA_908208.tab", "Piezometer 'mdm trail 10'", 4.375604, 114.354962, "Undrained peat swamp forest (dome)",
              "Water level WL (m)", "Yes: as above", "2012-02-06 22:20", "2013-01-30 02:40", "20 min", 25790, "0 %",
              "-0.350 / -0.014 / 0.195"),
            f("PANGAEA_908214.tab", "Throughfall gauges (centroid of 4)", 4.369827, 114.353973, "Undrained peat swamp forest",
              "Throughfall intensity (mm/h)", "No", "2012-02-06 22:20", "2013-01-30 02:40", "20 min", 25790),
            f("PANGAEA_908209.tab", "Dome (model result)", 4.369827, 114.353973, "", "Hydraulic conductivity K(WL) knots with 95% CI",
              "WL is the x-axis", step="3 knots"),
            f("PANGAEA_908210.tab", "Dome (model result)", 4.369827, 114.353973, "", "Specific yield Sy(WL) knots with 95% CI",
              "WL is the x-axis", step="6 knots"),
            f("PANGAEA_908211.tab", "Flowtube", 4.369827, 114.353973, "", "Flowtube area vs integrated normal gradient", "No"),
            f("README_Brunei_peat_swamp_data.pdf", "", "", "", "", "Dataset README (not committed; PDF)", "No"),
        ]),
    dict(
        id="A2", folder="A2_Mendaram_Hoyt2019", name="Mendaram water table + chamber CO2, Brunei",
        status=DL, license="CC-BY-4.0",
        links=[("Zenodo 3245335", "https://doi.org/10.5281/zenodo.3245335")],
        papers=[dict(cite="Hoyt et al. 2019, Global Change Biology 25", doi="10.1111/gcb.14702",
                     access="Preprint on HAL (hal-02333558) and DSpace@MIT; both block scripts, open in a browser",
                     da="Not read (full text blocked). The Zenodo record is titled 'Supplement to: Hoyt et al. (2019)'.",
                     da_dl="Yes")],
        how=("Automated chambers (root-cut to 30 cm, in sun and shade) measured peat CO2 efflux hourly. Mean daily heterotrophic "
             "respiration (Rhet) was linearly related to water-table depth and small and constant under flooding. That "
             "Rhet-WTD relationship, plus a DOC-WTD relationship, was applied to a 3-year, 20-min water-table record "
             "(Feb 2012 - Feb 2015) to upscale annual carbon export (Fig. 3). Period 1 (Jul-Nov 2012) data are in Fig. 2/S1, "
             "Period 2 (Nov 2013 - Mar 2014) in Figs. 4, 5, S2."),
        notes=["Site coordinates are not given in the files; the chambers are on the same Mendaram dome as A1 (about 4.37 N, 114.35 E).",
               "Zip archives are committed as downloaded; unzip them locally (the cloud copy was unpacked only for inspection)."],
        files=[
            f("Data_Period_1_CO2Flux_WT_AirTemp_Rainfall.zip", "Mendaram chambers", "~4.37", "~114.35", "Undrained PSF",
              "WaterTable_Period_1a.csv: WT at chamber-measurement times", "Yes: " + NEG,
              "2012-07-13 16:37", "2012-08-05 14:37", "1 h", 549, "0.4 %", "-0.298 / -0.204 / -0.115",
              part="WaterTable_Period_1a.csv"),
            f("Data_Period_1_CO2Flux_WT_AirTemp_Rainfall.zip", "Mendaram chambers", "~4.37", "~114.35", "Undrained PSF",
              "WaterTable_Period_1b.csv", "Yes: " + NEG, "2012-08-07 10:00", "2012-11-23 23:40", "20 min", 7818, "0 %",
              "-0.359 / -0.109 / 0.199", part="WaterTable_Period_1b.csv"),
            f("Data_Period_1_CO2Flux_WT_AirTemp_Rainfall.zip", "Chambers 1 (sun), 2-4 (shade)", "~4.37", "~114.35", "Undrained PSF",
              "Hourly CO2 flux (umol m-2 s-1); 1a: chambers 1, 4 (13 Jul - 5 Aug 2012); 1b: chambers 1-4 (7 Aug - 23 Nov 2012; ch. 2 ends 8 Oct)",
              "No", "2012-07-13", "2012-11-23", "1 h", part="CO2flux_Chamber*.csv (6 files)"),
            f("Data_Period_1_CO2Flux_WT_AirTemp_Rainfall.zip", "", "~4.37", "~114.35", "", "Daily means of CO2 flux, air T and WT (day of year 219-327, 2012)",
              "Yes (daily mean)", "2012-08-06", "2012-11-22", "1 d", 109, part="DailyMeans_Period_1b.csv"),
            f("Data_Period_1_CO2Flux_WT_AirTemp_Rainfall.zip", "", "~4.37", "~114.35", "", "Air temperature (10 min, 6 Jun 2012 - 21 Feb 2013); rain depth (10 min, 13 Jul - 23 Nov 2012)",
              "No", "2012-06-06", "2013-02-21", "10 min", part="AirTemp_Period_1extended.csv, RainDepth_Period_1.csv"),
            f("Data_Period_2_PeatTemp_AirTemp_WT.zip", "Mendaram chambers", "~4.37", "~114.35", "Undrained PSF",
              "WaterTable_Period_2.csv", "Yes: " + NEG, "2013-11-23 15:20", "2014-03-23 14:00", "20 min", 8628, "0.1 %",
              "-0.180 / 0.003 / 0.106", part="WaterTable_Period_2.csv"),
            f("Data_Period_2_PeatTemp_AirTemp_WT.zip", "", "~4.37", "~114.35", "", "Air temperature (20 min); peat temperature at surface/10/25 cm, sun and shade (10 min)",
              "No", "2013-11-24", "2014-03-23", "10-20 min", part="AirTemp_Period_2.csv, PeatTemperature_Tidbits_Period_2.csv"),
            f("Flux_Upscaling.zip", "Mendaram dome", "~4.37", "~114.35", "Undrained PSF",
              "UpscalingTimeseries_3yrs.csv: WT + modelled Rhet (hollows, dome) + DOC export", "Yes: " + NEG,
              "2012-02-06 12:00", "2015-02-06 11:40", "20 min", 78901, "0 %", "-0.347 / -0.037 / 0.184",
              part="UpscalingTimeseries_3yrs.csv"),
            f("Flux_Upscaling.zip", "", "", "", "", "Rhet-WT and DOC-WT relationships used for upscaling (WT -0.4 to 0.2 m)",
              "WT is the x-axis", part="Rhet_WT_Upscaling_Relationship.csv, DOC_WT_Upscaling_Relationship.csv"),
        ]),
    dict(
        id="A3", folder="A3_Palangkaraya_Hirano2024", name="Palangkaraya UF / DF / DB flux towers, Central Kalimantan",
        status=DL, license="CC BY 4.0",
        links=[("figshare (link given in the paper)", "https://figshare.com/s/6aefe20137486d0a6f62")],
        papers=[dict(cite="Hirano et al. 2024, Communications Earth & Environment 5:221", doi="10.1038/s43247-024-01387-7",
                     access="Gold OA (CC-BY); nature.com shows a bot check to scripts, open in a browser",
                     da="\"The CO2 flux, meteorology, and groundwater level data that support the findings of this study are available on figshare [https://figshare.com/s/6aefe20137486d0a6f62].\"",
                     da_dl="Yes")],
        how=("GWL was measured at a hollow next to each tower. The paper uses it (1) as a driver when gap-filling half-hourly "
             "NEE (marginal distribution sampling for daytime, a GWL look-up table for night-time), (2) to relate annual "
             "NEE, RE and GPP to annual mean GWL and to compare ENSO-drought, normal and wet years, and (3) to back-estimate "
             "monthly NEE from the 1997 canal excavation onward, using GWL estimated from a nearby record (Takahashi site, "
             "since 1993) and NEE-GWL regressions."),
        notes=["UF and DF GWL columns contain no missing values over 15 years, so they are probably gap-filled; the paper does not say.",
               "Coordinates are from Hirano 2024; Hirano et al. 2014 gives DF as 2.35 S, 114.14 E instead of 114.04 E.",
               "Flux columns (fNEE, fGPP, fRE) end in 2017; environmental data continue to Dec 2019 (UF) and Jan 2017 (DB)."],
        files=[
            f("CO2 flux data.zip", "UF: undrained forest (slightly drained by old logging ditches)", -2.32, 113.90, "Undrained PSF",
              "Half-hourly fNEE, fGPP, fRE, H, LE, radiation, PPFD, T, RH, VPD, GWL, precipitation", "Yes: " + NEG + " (hollow)",
              "2004-07-10 00:30", "2019-12-11 12:00", "30 min", 270360, "0 %", "-1.413 / -0.185 / 0.306",
              part="UF_fluxdata230802.csv"),
            f("CO2 flux data.zip", "DF: forest drained by Mega Rice Project canal", -2.35, 114.04, "Drained PSF",
              "as UF", "Yes: " + NEG + " (hollow)", "2001-11-28 00:30", "2017-06-06 11:00", "30 min", 272134, "0 %",
              "-1.774 / -0.488 / 0.027", part="DF_fluxdata230802.csv"),
            f("CO2 flux data.zip", "DB: drained, repeatedly burned (1997, 2002, 2009, 2014, 2015)", -2.34, 114.04, "Drained burnt ex-forest",
              "as UF", "Yes: " + NEG + " (hollow)", "2004-04-17 00:00", "2017-01-01 00:00", "30 min", 222817, "0.7 %",
              "-1.623 / -0.176 / 0.314", part="DB_fluxdata230802.csv"),
            f("CO2 flux data.zip", "UF, DF, DB", "", "", "", "Annual precipitation, mean GWL, RE, GPP, NEE, GPP0, Gs,ref per site",
              "Yes (annual mean)", "2002", "2017", "1 year", part="Annual CO2 fluxes.csv"),
        ]),
    dict(
        id="A4", folder="A4_Palangkaraya_DailyGWL", name="Palangkaraya daily groundwater level (UF, DF)",
        status=DL, license="CC BY 4.0",
        links=[("figshare 22321129", "https://doi.org/10.6084/m9.figshare.22321129.v1")],
        papers=[
            dict(cite="Hirano et al. 2014, Global Change Biology 21 (methods reference cited by the record)", doi="10.1111/gcb.12653",
                 access="Accepted manuscript (Hokkaido Univ. repository)",
                 da="Not applicable (the dataset post-dates the paper; the record cites it only for methods).", da_dl="n/a"),
            dict(cite="Hirano et al. 2012, Global Change Biology 18 (methods reference)", doi="10.1111/j.1365-2486.2012.02793.x",
                 access="Closed", da="Not applicable.", da_dl="n/a"),
            dict(cite="Ohkubo, Hirano & Kusin 2023, Journal of Hydrology 620 (probable companion paper, inferred)", doi="10.1016/j.jhydrol.2023.129523",
                 access="Free to read on ScienceDirect (bronze); blocks scripts",
                 da="Not read (ScienceDirect blocked). Link to this dataset is inferred from the same authors, sites and years, not confirmed.",
                 da_dl="Unknown")],
        how=("GWL (distance between ground and water surface) was logged every 30 min with a water-level logger (Sensor Technik "
             "DL/N or Keller DCX-22) within 5 m of each tower (Hirano 2014 methods); this file gives daily means. The figshare "
             "record only cites the 2012/2014 methods papers. The 2013-2018 period matches Ohkubo et al. 2023 (J. Hydrol.), "
             "which studies transpiration and evaporation in these forests, but that link is my inference."),
        notes=["These daily values are essentially the daily mean of A3's half-hourly GWL: mean absolute difference 0.2 cm (UF, "
               "1461 days) and 1.2 cm (DF, 1618 days). Use A3 if you need sub-daily data or the DB site."],
        files=[
            f("DailyGWL.xlsx", "UF (undrained forest)", -2.32, 113.90, "Undrained PSF", "Year, DOY, GWL (m)", "Yes: " + NEG,
              "2015-01-01", "2018-12-31", "1 d", 1461, "0 %", "-1.43 / -0.236 / 0.14", part="sheet UF"),
            f("DailyGWL.xlsx", "DF (drained forest)", -2.35, 114.04, "Drained PSF", "Year, DOY, GWL (m)", "Yes: " + NEG,
              "2013-01-01", "2017-06-06", "1 d", 1618, "0 %", "-1.62 / -0.466 / 0.00", part="sheet DF"),
        ]),
    dict(
        id="A5", folder="A5_FLUXNET-CH4_ID-Pag_Sakabe2018", name="FLUXNET-CH4 ID-Pag (Palangkaraya undrained forest)",
        status=LOGIN, license="CC-BY-4.0 (FLUXNET-CH4 Community Product)",
        links=[("FLUXNET site page", "https://fluxnet.org/sites/siteinfo/ID-Pag"), ("Data DOI", "https://doi.org/10.18140/FLX/1669643")],
        papers=[dict(cite="Sakabe et al. 2018, Global Change Biology 24", doi="10.1111/gcb.14410",
                     access="Free to read on Wiley (bronze); Wiley blocks scripts",
                     da="Not read (Wiley blocked automated access).", da_dl="Yes (via FLUXNET-CH4, login)")],
        how=("One year of eddy-covariance CH4 flux over the undrained forest (same tower as A3 UF). The forest was a small CH4 "
             "sink in the dry season and a source in the wet season, controlled by groundwater level; anaerobic incubations "
             "compared CH4 production in undrained, drained and burned soils (from the abstract)."),
        notes=["FLUXNET site metadata: -2.3200, 113.9000, elevation 30 m, AsiaFlux, EBF; FLUXNET-CH4 years 2016-2017.",
               "Whether the FLUXNET-CH4 file contains a WTD column for this site has to be checked after you download it."],
        files=[]),
    dict(
        id="A6", folder="A6_FLUXNET-CH4_MY-MLM_Tang2020", name="FLUXNET-CH4 MY-MLM (Maludam National Park), Sarawak",
        status=LOGIN, license="CC-BY-4.0 (FLUXNET-CH4 Community Product)",
        links=[("FLUXNET site page", "https://fluxnet.org/sites/siteinfo/MY-MLM"), ("Data DOI", "https://doi.org/10.18140/FLX/1669650")],
        papers=[dict(cite="Tang et al. 2020, Global Change Biology 26", doi="10.1111/gcb.15332", access="Closed",
                     da="Not read (closed access).", da_dl="Partly (FLUXNET-CH4 2014-2015 only)")],
        how=("Eddy-covariance CO2 exchange over a peat swamp forest in 2011-2014: the forest was a net CO2 source every year "
             "(183-632 g C m-2 yr-1); path analysis identified vapour-pressure deficit, not water table, as the main driver of "
             "GPP and RE (from the abstract)."),
        notes=["FLUXNET-CH4 covers only 2014-2015 for MY-MLM, not the 2011-2014 period of Tang 2020; the full record is "
               "held by the Sarawak Tropical Peat Research Institute.",
               "FLUXNET site metadata: 1.4536, 111.1495, AsiaFlux, EBF. C7 (Aeries 2023) has 2011-2015 water-table loggers in "
               "the same national park.",
               "Daily WT for this forest for 2011-2014 is public on figshare (doi:10.6084/m9.figshare.25299358) and half-hourly "
               "WT for Nov-Dec 2013 on Zenodo (doi:10.5281/zenodo.1161966); see EXPANDED_2006-2026 rows A15-A16."],
        files=[]),
    dict(
        id="A7", folder="A7_Kampar_Deshmukh2021", name="Kampar Peninsula intact vs degraded peatland, Riau",
        status=DL, license="CC-BY-4.0",
        links=[("Zenodo 4835696", "https://doi.org/10.5281/zenodo.4835696")],
        papers=[dict(cite="Deshmukh et al. 2021, Nature Geoscience 14", doi="10.1038/s41561-021-00785-2",
                     access="Accepted manuscript (Word) on figshare 15073734",
                     da="\"All data that support the findings of this study are archived on http://doi.org/10.5281/zenodo.4835696.\"",
                     da_dl="Yes")],
        how=("GWL was logged every 30 min (Solinst Levelogger 3001 in perforated PVC tubes anchored into the clay; 3 loggers at "
             "the intact site, 2 at the degraded site; datum = base of the hollows). Daily GWL is shown against cumulative "
             "rainfall and ET (Fig. 2) to explain drawdown in the 2019 positive-IOD/El Nino drought. NEE and CH4 are "
             "bin-averaged by GWL (Fig. 3, ED Fig. 2): the intact site approaches CO2 neutrality when hollows are flooded, while "
             "NEE at the degraded site is insensitive to GWL between -0.4 and -0.8 m. ED Fig. 3 compares GWL-NEE with literature."),
        notes=["The text reports degraded-site GWL for Oct 2016 - Sep 2020, but the published daily series (Fig. 2b) covers only "
               "Jun 2017 - May 2020."],
        files=[
            f("Deshmukh_Fig2.xlsx", "Intact peatland (IP) tower, mean of 3 loggers", 0.39520, 102.76455, "Intact PSF",
              "Daily GWL_IP and SD, cumulative rain, ET", "Yes: m; negative = below hollow surface", "2017-06-01", "2020-05-31", "1 d",
              1096, "0 %", "-0.781 / -0.274 / 0.188", part="Panel a"),
            f("Deshmukh_Fig2.xlsx", "Degraded peatland (DP) tower, mean of 2 loggers", 0.69949, 102.79331, "Degraded PSF",
              "Daily GWL_DP and SD, cumulative rain, ET", "Yes: as above", "2017-06-01", "2020-05-31", "1 d", 1096, "0 %",
              "-1.127 / -0.716 / -0.283", part="Panel b"),
            f("Deshmukh_Fig2.xlsx", "IP, DP", "", "", "", "Daily cumulative NEE and CH4 with uncertainty", "No",
              "2017-06-01", "2020-05-31", "1 d", part="Panels c, d"),
            f("Deshmukh_Fig1.xlsx", "Towers, subsidence poles, N2O points", "", "", "", "Coordinates (DMS)", "No"),
            f("Deshmukh_Fig3.xlsx", "IP, DP", "", "", "", "NEE and CH4 bin-averaged by GWL", "GWL is the x-axis"),
            f("Deshmukh_ED_Fig2.xlsx", "IP, DP", "", "", "", "NEE, Reco, GPP by GWL bin; GPP-PPFD above/below a GWL threshold", "GWL is the x-axis"),
            f("Deshmukh_ED_Fig3.xlsx", "Literature sites", "", "", "", "Compilation of GWL vs NEE from other studies", "Yes (site means)"),
            f("Deshmukh_ED_Fig1.xlsx", "IP, DP, Pekanbaru", "", "", "", "Monthly rainfall 2016-2020; Jul-Sep rainfall 1991-2020 with SOI and DMI", "No",
              "1991", "2020", "1 month"),
            f("Deshmukh_ED_Fig4.xlsx", "IP, DP", "", "", "", "Soil N2O fluxes by month", "No", "2019-06", "2020-05", "~monthly"),
            f("Deshmukh_ED_Fig5.xlsx", "IP", 0.39520, 102.76455, "", "Daily PPFD, Tair, VPD, soil T", "No", "2017-06-01", "2020-05-31", "1 d"),
            f("Deshmukh_ED_Fig6.xlsx", "DP", 0.69949, 102.79331, "", "Daily PPFD, Tair, VPD, soil T", "No", "2016-10-01", "2020-09-30", "1 d"),
        ]),
    dict(
        id="A8", folder="A8_Kampar_Deshmukh2023", name="Kampar Peninsula Acacia plantation / degraded / intact, Riau",
        status=DL, license="CC-BY-4.0",
        links=[("Zenodo 7500659 (index link)", "https://doi.org/10.5281/zenodo.7500659"),
               ("Zenodo 7728463 (cited in the paper)", "https://doi.org/10.5281/zenodo.7728463")],
        papers=[dict(cite="Deshmukh et al. 2023, Nature 616", doi="10.1038/s41586-023-05860-9",
                     access="Hybrid OA (CC-BY); also in PMC (PMC10132972)",
                     da="\"All data that support the findings of this study are archived on Zenodo at 10.5281/zenodo.7728463.\"",
                     da_dl="Yes")],
        how=("GWL loggers (Solinst Levelogger 3001, every 30 min, perforated PVC anchored in clay): 4 around the plantation "
             "tower, 1 at the degraded site, 6 at the intact site; annual means average 11, 4 and 15 locations. GWL is the main "
             "explanatory variable for CO2, CH4 and N2O across the three land covers, and the paper places its sites on "
             "literature GWL-flux relationships (Fig. 3, ED Fig. 3c). ED Fig. 2a shows daily intact-site GWL (mean of 3 "
             "piezometers spanning 12 km) against the 90-day mean of rainfall minus ET."),
        notes=["Two Zenodo versions are kept: data/ holds 7500659 (the index link), data/zenodo_7728463_v03/ the version the "
               "paper cites. The daily GWL series is identical in both; v03 expands the diel ET panels of ED Fig. 2.",
               "Only the intact-site GWL is published as a daily series; plantation and degraded-site GWL appear only as annual "
               "means (ED Table 2 in the paper).",
               "Fig. 1 file gives the Acacia tower at 0 30'57\"N, 102 02'11\"E, about 70 km west of the other towers; "
               "Deshmukh et al. 2020 (GCB, doi:10.1111/gcb.15019) gives the same position, so the coordinate is correct."],
        files=[
            f("Deshmukh_ED_Fig. 2.xlsx", "Intact site (mean of 3 piezometers over 12 km)", 0.39520, 102.76455, "Intact PSF",
              "Daily GWL and 90-day (rain - ET)", "Yes: " + NEG, "2017-06-01", "2022-05-30", "1 d", 1825, "0 %",
              "-0.87 / -0.236 / 0.20", part="Panel a (identical in zenodo_7728463_v03/)"),
            f("Deshmukh_ED_Fig. 2.xlsx", "Intact site", "", "", "", "Diel ET in dry and wet season", "No", part="Panels b, c"),
            f("Deshmukh_ED_Fig. 1.xlsx", "Acacia, degraded, intact", "", "", "", "Daily cumulative net CO2 and CH4 with uncertainty", "No",
              "2016-10-01", "2022-05-31", "1 d"),
            f("Deshmukh_ED_Fig. 3.xlsx", "3 sites + literature", "", "", "", "Quarterly soil N2O; literature GWL vs N2O", "Yes (literature site means)"),
            f("Deshmukh_Fig. 1.xlsx", "Towers, subsidence poles, N2O points", "", "", "",
              "Coordinates (DMS): intact 0.3952 N 102.7645 E; degraded 0.6995 N 102.7933 E; Acacia 0.5159 N 102.0364 E (see note)", "No"),
            f("Deshmukh_Fig. 2.xlsx", "3 sites", "", "", "", "GHG balance table", "No"),
            f("Deshmukh_Fig. 3.xlsx", "Literature sites", "", "", "", "GWL vs net CO2 and CH4 from eddy-covariance studies", "Yes (site means)"),
        ]),
    dict(
        id="A9", folder="A9_Jambi_KubuRaya_Taufik2022", name="8 BRGM automatic stations, Batanghari (Jambi) and Kubu Raya (West Kalimantan)",
        status=DL, license="CC BY-NC-ND (Data in Brief article licence)",
        links=[("Data in Brief attachment mmc1.xlsx (via Europe PMC PMC8847808)", "https://doi.org/10.1016/j.dib.2022.107903")],
        papers=[
            dict(cite="Taufik et al. 2022, Data in Brief 41:107903", doi="10.1016/j.dib.2022.107903",
                 access="Gold OA; ScienceDirect blocks scripts, full text read via Europe PMC",
                 da="\"Data available within the article and within Supplementary files\"", da_dl="Yes"),
            dict(cite="Taufik et al. 2022, Agricultural and Forest Meteorology 312:108738 (research article using the data)",
                 doi="10.1016/j.agrformet.2021.108738", access="Closed", da="Not read (closed access).", da_dl="Yes (via Data in Brief)")],
        how=("Groundwater table was measured in a slotted 2-inch PVC well at each station, logged every 10 min, averaged to daily "
             "values in R, and recalibrated against manual readings every 3 months. In Taufik et al. 2022 (AFM) the daily GWT "
             "feeds a 'water table factor' in an improved drought-fire risk model; the water-retention curves ('wrc' sheet) give "
             "how much the water table re-wets the surface peat."),
        notes=["'BRG' stations belong to the peat restoration agency BRG/BRGM, i.e. they are SiPALAGA stations (B1).",
               "Coordinates are published only for BRG6 and BRG18; the others appear only on the map in Fig. 1.",
               "% missing = share of days without data between each station's first and last record."],
        files=[
            f("mmc1.xlsx", "BRG3, Batanghari", "", "", "Peatland (see paper Fig. 1)", "Daily groundwater table (m)", "Yes: " + NEG,
              "2018-04-08", "2019-08-27", "1 d", 507, "0 %", "-1.68 / -0.948 / -0.488", part="sheet gwt"),
            f("mmc1.xlsx", "BRG4, Batanghari", "", "", "", "Daily groundwater table (m)", "Yes: " + NEG,
              "2018-04-08", "2018-12-28", "1 d", 265, "0 %", "-0.959 / -0.66 / -0.301", part="sheet gwt"),
            f("mmc1.xlsx", "BRG5, Batanghari", "", "", "", "Daily groundwater table (m)", "Yes: " + NEG,
              "2018-04-11", "2019-12-31", "1 d", 544, "13.7 %", "-1.325 / -0.495 / 0.015", part="sheet gwt"),
            f("mmc1.xlsx", "BRG6, Batanghari", -1.44281, 103.96930, "", "Daily groundwater table (m)", "Yes: " + NEG,
              "2018-04-11", "2019-10-07", "1 d", 545, "0 %", "-1.514 / -0.544 / 0.17", part="sheet gwt"),
            f("mmc1.xlsx", "BRG17, Kubu Raya", "", "", "", "Daily groundwater table (m)", "Yes: " + NEG,
              "2018-04-12", "2019-06-20", "1 d", 435, "5.6 %", "-0.794 / -0.418 / -0.245", part="sheet gwt"),
            f("mmc1.xlsx", "BRG18, Kubu Raya", -0.27979, 109.51923, "", "Daily groundwater table (m)", "Yes: " + NEG,
              "2018-04-12", "2018-12-31", "1 d", 264, "0 %", "-0.85 / -0.375 / 0.046", part="sheet gwt"),
            f("mmc1.xlsx", "BRG19, Kubu Raya", "", "", "", "Daily groundwater table (m)", "Yes: " + NEG,
              "2018-04-12", "2019-11-14", "1 d", 535, "14.9 %", "-1.54 / -1.123 / -0.732", part="sheet gwt"),
            f("mmc1.xlsx", "BRG20, Kubu Raya", "", "", "", "Daily groundwater table (m)", "Yes: " + NEG,
              "2018-04-13", "2019-12-31", "1 d", 440, "29.9 %", "-1.32 / -0.698 / -0.379", part="sheet gwt"),
            f("mmc1.xlsx", "BRG6, BRG18", "", "", "", "Modelled water-retention curves (van Genuchten), top- and sub-soil", "No", part="sheet wrc"),
        ]),
    dict(
        id="A11", folder="A11_SUSTAINPEAT_JovaniSancho2023", name="48 smallholder plots (SUSTAINPEAT), Selangor and West/Central Kalimantan",
        status=DL, license="CC-BY-4.0",
        links=[("Nottingham repository doi:10.17639/nott.7296", "https://doi.org/10.17639/nott.7296")],
        papers=[dict(cite="Jovani-Sancho et al. 2023, Global Change Biology 29", doi="10.1111/gcb.16747",
                     access="Hybrid OA (CC-BY); accepted version on NERC NORA",
                     da="\"The data that support the findings of this study are openly available in the Nottingham Research Data Management Repository at https://doi.org/10.17639/nott.7296.\"",
                     da_dl="Yes")],
        how=("WTD was read manually in a perforated PVC dipwell (2 m long, 1.5 m in the peat) next to each plot at every monthly "
             "gas-sampling visit. It was a fixed effect in mixed models of CH4 and N2O, and was used to fit an exponential "
             "CH4-WTD model (net CH4 emission starts around WTD -25 to -30 cm) and sigmoidal/linear N2O-WTD models; Fig. 2 "
             "shows seasonal WTD by land use."),
        notes=["Plot coordinates are not published (only region names and a map); regions: NS = North Selangor, SS = South "
               "Selangor, WK = West Kalimantan, CK = Central Kalimantan.",
               "Two sampling methods are mixed in the file: 'vial' (static chambers, GC) and 'LGR' (dynamic chamber, Los Gatos)."],
        files=[
            f("CH4_and_N2O_emissions_SUSTAINPEAT_data_paper.xlsx", "4 regions x forest / oil palm / tree crop / cropland x 3 subsites",
              "", "", "Forest, oil palm, tree plantation, cropland",
              "CH4, N2O (ug m-2 h-1), air T, soil T10, WTD, total dissolved N", "Yes: " + NEG_CM,
              "2018-03-21", "2019-04-01", "Monthly visits (20-32 dates per region)", "1303 of 1336 rows", "2.5 %",
              "-136 / -37.5 / 16.1 cm", part="sheet data (codes in sheet metadata)"),
        ]),
    dict(
        id="A12", folder="A12_Sebungan_McCalmont2021", name="Sebungan / Sabaju oil-palm flux towers, Sarawak",
        status=EMB, license="All rights reserved (Exeter record)",
        links=[("Exeter dataset doi:10.24378/exe.3143 (files embargoed)", "https://doi.org/10.24378/exe.3143")],
        papers=[dict(cite="McCalmont et al. 2021, Global Change Biology 27", doi="10.1111/gcb.15544",
                     access="Hybrid OA (CC-BY); PDF fetched from figshare 29777714",
                     da="\"The data that support the findings of this study are available from the corresponding author upon reasonable request.\"",
                     da_dl="No")],
        how=("Two eddy-covariance towers: OPnew (converted from logged forest in 2016) and OPmature. WTD was measured with a "
             "submersible pressure transducer (Omega PX709GW) in a 0.05 m porous pipe to 2.5 m depth. Night-time NEE (taken as "
             "Reco) was related to WTD in 0.01 m bins using measured (not gap-filled) data; mean WTD was 0.54 m (OPnew) and "
             "0.26 m (OPmature), which the authors use to argue their mature-plantation emissions are conservative."),
        notes=["The Exeter record (52.6 MB) is embargoed: 'permission from a third-party is required before access can be granted'.",
               "Periods: OPnew Sep 2016 - Jan 2020; OPmature May 2017 - Jan 2020 (Apr-Aug 2019 excluded after a sensor fault).",
               "Coordinates: OPnew (Sabaju) 3 09.615'N 113 25.163'E = 3.1603, 113.4194; OPmature (Sebungan) 3 09.965'N "
               "113 21.198'E = 3.1661, 113.3533. The index coordinate is OPmature."],
        files=[]),
    dict(
        id="A13-14", folder="A13-14_CIFOR_CentralKalimantan_Swails2019", name="CIFOR Central Kalimantan: primary forest vs oil palm",
        status=UNREACH, license="CIFOR Dataverse (terms not readable from the cloud)",
        links=[("CIFOR Dataverse doi:10.17528/CIFOR/DATA.00061", "https://doi.org/10.17528/CIFOR/DATA.00061")],
        papers=[
            dict(cite="Hergoualc'h et al. 2017, Biogeochemistry 135:203-220 (the paper DATA.00061 belongs to)", doi="10.1007/s10533-017-0363-4",
                 access="Hybrid OA (CC-BY); Springer blocks scripts, open in a browser",
                 da="Not read (Springer bot check). The CIFOR record is titled 'Replication Data for: ... Biogeochemistry 135(3): 203-220'.",
                 da_dl="Yes (CIFOR Dataverse)"),
            dict(cite="Swails et al. 2019, Biogeochemistry 142 (the paper named in the index)", doi="10.1007/s10533-018-0519-x",
                 access="Closed", da="Not read (closed access).", da_dl="Unknown")],
        how=("Hergoualc'h 2017: total and heterotrophic soil respiration over 13 months in trenched vs control plots in a primary "
             "peat swamp forest and two oil palm plantations (planted 2007 and 2012). Swails 2019 (same group, closed) relates "
             "soil respiration to climatic drivers in the same kind of forest vs oil palm comparison. The CIFOR record contains "
             "three databases: DBCollar (monthly and/or daily data per respiration collar), DBSoilMoisture, DBLitterfall; "
             "whether DBCollar includes WTD could not be checked."),
        notes=["data.cifor.org dropped every TLS connection from the cloud, so nothing was downloaded. Run "
               "`python3 download_data.py A13` on your computer; it resolves the files through the Dataverse API.",
               "The index links DATA.00061 to Swails 2019, but the record belongs to Hergoualc'h et al. 2017.",
               "Other CIFOR records from this group (not in the index): DATA.00201, 00290, 00291, 00330, 00331."],
        files=[]),
    dict(
        id="B1", folder="B1_SiPALAGA_BRGM", name="SiPALAGA water-level network (BRGM), Indonesia",
        status=NODATA, license="Portal / request",
        links=[("SiPALAGA portal", "https://sipalaga.brgm.go.id")],
        papers=[dict(cite="Mleczko et al. 2025, Remote Sensing of Environment (use case)", doi="10.1016/j.rse.2025.115009",
                     access="Hybrid OA (CC-BY); ScienceDirect blocks scripts",
                     da="Not read (ScienceDirect blocked).", da_dl="Unknown")],
        how=("Mleczko et al. compare Sentinel-1 SBAS InSAR ground displacement with GWL and peat-surface elevation from local "
             "monitoring networks in Central Kalimantan (2017-2022) and show the InSAR results depend on the hydrological state "
             "(from the abstract)."),
        notes=["sipalaga.brgm.go.id returned HTTP 403 from its own server to the cloud request; try it from your browser.",
               "A9 is a published subset: 8 BRG stations with daily data for 2018-2019."],
        files=[]),
    dict(
        id="B2", folder="B2_SiMATAG_KLHK", name="SiMATAG-0.4m compliance points (KLHK), Indonesia",
        status=NODATA, license="Not public",
        links=[("KLHK press release", "https://ppid.menlhk.go.id/berita/siaran-pers/4915/menteri-lhk-luncurkan-simatag-04m-untuk-monitoring-keberhasilan-pemulihan-gambut")],
        papers=[], how="Government compliance monitoring system; no research paper or public data.", notes=[], files=[]),
    dict(
        id="C1", folder="C1_SouthSumatra_Hooijer2024", name="South Sumatra rewetting trial (257 dams)",
        status=EMB, license="",
        links=[("Paper", "https://doi.org/10.1038/s41598-024-60462-3")],
        papers=[dict(cite="Hooijer et al. 2024, Scientific Reports 14:10721", doi="10.1038/s41598-024-60462-3",
                     access="Gold OA (CC-BY); also PMC11087581",
                     da="\"The datasets analyzed during the study are available from the corresponding author on reasonable request.\"",
                     da_dl="No")],
        how=("Monthly groundwater table depth and subsidence in PVC dipwells anchored in the mineral subsoil along a 4.2 km "
             "transect from the main road canal into forest (from Jan 2016; 20 dipwells after quality screening; short gaps "
             "filled from neighbours or by interpolation), grouped into six 700 m zones. Used to show the water-table gradient "
             "after canal blocking and its link to subsidence and forest regrowth; LiDAR canal water depth on four dates "
             "extends this spatially."),
        notes=["Supplementary Table 2 (in the SI PDF, not committed) gives per-dipwell mean GWD and subsidence, not time series.",
               "This site is one of the four calibration records of D1."],
        files=[]),
    dict(
        id="C3", folder="C3_PulauPadang_Ismail2021", name="Pulau Padang land-use units, Riau",
        status=NODATA, license="",
        links=[("Paper", "https://doi.org/10.2166/nh.2021.062")],
        papers=[dict(cite="Ismail et al. 2021, Hydrology Research 52(6):1372", doi="10.2166/nh.2021.062",
                     access="Gold OA (CC BY-NC-ND); IWA blocks scripts, open in a browser",
                     da="Not read (IWA blocked automated access).", da_dl="Unknown")],
        how=("Water table and precipitation monitored at several stations on Padang Island; analyses WTD recession rates near "
             "plantation drainage (up to 3.5 cm/day, WTD to -1.8 m) versus village farm drains, and specific yield by depth "
             "(from the abstract)."),
        notes=[], files=[]),
    dict(
        id="C5", folder="C5_EastKalimantan_Asyhari2024", name="Muara Siran undrained peatland, East Kalimantan",
        status=DLP, license="CC-BY-4.0",
        links=[("Zenodo 10427000", "https://doi.org/10.5281/zenodo.10427000")],
        papers=[dict(cite="Asyhari et al. 2024, Scientific Reports 14", doi="10.1038/s41598-024-62233-6",
                     access="Gold OA (CC-BY); also PMC11106321",
                     da="\"All data that support the findings of this study are archived on 10.5281/zenodo.10427000.\"",
                     da_dl="Partly (manual water depth yes, hourly logger GWL no)")],
        how=("CO2 and CH4 chamber fluxes (10 chambers per site, about 3 visits a month) with water level read manually at each "
             "chamber at the same time; an hourly Keller DCX-22 logger at each plot centre and a river logger (Siran River) "
             "track continuous water levels (Fig. 2). Water level is used to explain flux seasonality, e.g. CH4 rising as "
             "water fell from >1 m above the surface (Dec 2022) to near the surface (Jan 2023)."),
        notes=["The index rated C5 as 'figures only'; the paper's Data availability points to this Zenodo record.",
               "The hourly logger series of Fig. 2 are not in the archive.",
               "Site codes in the file are PPSF and DPSF; the paper text uses PPSF and SPSF.",
               "Sign: positive WaterDepth_cm = water above the peat surface (inferred from the flooding >1 m described in the paper)."],
        files=[
            f("GHG_Flux_Data.xlsx", "PPSF (10 chambers)", "", "", "Undrained peat swamp forest",
              "WaterDepth_cm, CO2 and CH4 flux (Mg CO2(e) ha-1 yr-1)", "Yes: cm; + = above surface (inferred)",
              "2022-10-27", "2023-09-23", "~3 visits/month (36 dates)", 360, "0 %", "-26 / 19.0 / 56 cm", part="sheet All Data"),
            f("GHG_Flux_Data.xlsx", "DPSF (10 chambers)", "", "", "Peat swamp forest (see paper)",
              "as above", "Yes: as above", "2022-10-27", "2023-09-23", "~3 visits/month (36 dates)", 360, "0 %",
              "-6 / 37.3 / 153 cm", part="sheet All Data"),
        ]),
    dict(
        id="C6", folder="C6_Sarawak_Kiew2025", name="Sarawak forest-to-oil-palm conversion flux tower",
        status=EMB, license="",
        links=[("Paper", "https://doi.org/10.1016/j.agrformet.2025.110956")],
        papers=[dict(cite="Kiew et al. 2025, Agricultural and Forest Meteorology 378:110956", doi="10.1016/j.agrformet.2025.110956",
                     access="Accepted manuscript on DSpace (Univ. of Tartu, CC-BY)",
                     da="\"The data utilized in this study are owned by the State Government of Sarawak. Access to these data is restricted and requires official approval from the government.\"",
                     da_dl="No")],
        how=("Half-hourly GWL at the tower (2011-2019), partly gap-filled with a neural network using GWL from a forest about "
             "10 km away. Night-time NEE correlated negatively with GWL before conversion, with air temperature and VPD during "
             "conversion, and GWL again became the strongest control after conversion; Table 3 gives annual GWL."),
        notes=["Monthly GWL ranged from -139.2 to +4.6 cm; mean -19.2, -102.1 and -105.3 cm before, during and after conversion."],
        files=[]),
    dict(
        id="C7", folder="C7_Sarawak_Aeries2023", name="Maludam National Park, 4 forest-type plots, Sarawak",
        status=NODATA, license="",
        links=[("Paper", "https://doi.org/10.58915/aset.v2i2.331")],
        papers=[dict(cite="Aeries et al. 2023, Advanced and Sustainable Technologies 2(2)", doi="10.58915/aset.v2i2.331",
                     access="Diamond OA (CC BY-NC-SA)", da="No data availability statement in the paper.", da_dl="No")],
        how=("Two piezometers per plot with HOBO U20 water-level loggers (plus one barometric logger) logging every 30 min from "
             "2011 to 2015; monthly means are used for seasonal patterns, WT-precipitation regressions and Mann-Kendall trends."),
        notes=["Plots: MA 1.43095 N 111.13113 E (mixed peat swamp); MB 1.45348 N 111.14924 E (Alan batu); MC 1.46330 N "
               "111.15796 E (Alan bunga); MD 1.48162 N 111.17366 E (padang Alan). Same national park as the MY-MLM tower (A6)."],
        files=[]),
    dict(
        id="C8-9", folder="C8-9_NorthSelangor_LoParish2022_Ledger2023", name="North Selangor peat swamp forest, Malaysia",
        status=DLP, license="CC-BY (Frontiers supplementary material)",
        links=[("Ledger 2023 supplementary DataSheet1/2", "https://doi.org/10.3389/fenvs.2023.1182100")],
        papers=[
            dict(cite="Lo & Parish 2022, Archives of Agriculture Research and Technology 3", doi="10.54026/aart/1029",
                 access="Gold OA, but the publisher's TLS certificate has expired; open in a browser at your own risk",
                 da="Not read (publisher certificate expired).", da_dl="Unknown"),
            dict(cite="Ledger et al. 2023, Frontiers in Environmental Science 11:1182100", doi="10.3389/fenvs.2023.1182100",
                 access="Gold OA (CC-BY)",
                 da="\"The original contributions presented in the study are included in the article/Supplementary Material, further inquiries can be directed to the corresponding author.\"",
                 da_dl="Yes")],
        how=("Lo & Parish 2022: monthly groundwater table on transects Dec 2013 - Dec 2016 in logged-over forest, degraded open "
             "land and smallholder oil palm, and the effect of drains (from the abstract). Ledger 2023: peat surface oscillation "
             "at 14 sites (288 subsidence poles, 3 time-lapse cameras); water table from piezometers read manually with the "
             "poles and logged automatically at two camera sites; used to show that oscillation magnitude depends on peat "
             "condition and water-table range."),
        notes=["The index rated C8-9 as 'figures only'; Ledger 2023's supplement contains the raw water-table data.",
               "Lo & Parish 2022 data (2013-2016) remain unavailable."],
        files=[
            f("Ledger2023_DataSheet1.XLSX", "13 of 14 sites (F2-F8, B5, B12, B13, OP14-OP18; F3 has none)", "see DataSheet2", "",
              "Recovering / degraded forest, fire-affected scrubland, smallholder oil palm",
              "Manual water table (m) read with the subsidence poles", "Yes: " + NEG,
              "2018-08-15", "2020-02-06", "5 occasions", 52, "", "-1.14 / -0.389 / 0.208", part="sheet Jul18Jan20_m_tidy"),
            f("Ledger2023_DataSheet1.XLSX", "Site 6, degraded forest (camera + logger)", 3.43868, 101.27982, "Degraded forest",
              "Adjusted water table level (cm, m) and camera peat-surface elevation", "Yes: cm; negative = below peat surface",
              "2019-04-20", "2020-01-20", "1 d (12:00 reading)", 276, "", "-117.0 / -28.6 / 32.3 cm", part="sheet Automated_datasets"),
            f("Ledger2023_DataSheet1.XLSX", "Site 13, fire-affected scrubland (camera + logger)", 3.46602, 101.43712, "Fire-affected scrubland",
              "Water table relative to peat surface (cm, m) and camera peat-surface elevation", "Yes: as above",
              "2019-04-11", "2020-01-20", "1 d (12:00 reading)", 285, "", "-17.2 / 7.6 / 24.6 cm", part="sheet Automated_datasets"),
            f("Ledger2023_DataSheet1.XLSX", "14 sites", "", "", "", "Subsidence poles, surface oscillation, bulk density, Rock-Eval", "No",
              "2018-08", "2020-02", "monthly/irregular", part="other sheets"),
            f("Ledger2023_DataSheet2.XLSX", "14 sites", "3.44-3.70", "101.07-101.44", "", "Site coordinates (X = lon, Y = lat), land cover, peat depth and properties", "No",
              part="Supplementary tables 3-4"),
        ]),
    dict(
        id="C10-11", folder="C10-11_TimelapseCamera_Evans2021", name="Time-lapse camera WTD, Central Kalimantan",
        status=EMB, license="",
        links=[("Paper", "https://doi.org/10.3389/fenvs.2021.630752")],
        papers=[dict(cite="Evans et al. 2021, Frontiers in Environmental Science 9:630752", doi="10.3389/fenvs.2021.630752",
                     access="Gold OA (CC-BY)",
                     da="\"The raw data supporting the conclusions of this article will be made available by the authors, without undue reservation.\"",
                     da_dl="No (on request)")],
        how=("Eight time-lapse 'peat cameras' in forest, burned, agricultural and oil-palm sites between Palangka Raya and the "
             "Sebangau/Kahayan rivers (1.88-2.35 S, 113.47-114.10 E) recorded peat surface motion and WTD, 3-hourly and "
             "hourly from late Feb 2020; camera WTD was checked against pressure transducers (Feb-Jun 2020) and manual "
             "subsidence poles; annual subsidence was taken between Jan 2019 and Jan 2020."),
        notes=["The index says 'Central Kalimantan, South Sumatra'; the paper covers Central Kalimantan only."],
        files=[]),
    dict(
        id="C12", folder="C12_Badas_Lupascu2020", name="Badas burnt vs intact peat swamp forest, Brunei",
        status=NODATA, license="",
        links=[("Paper", "https://doi.org/10.1111/gcb.15195")],
        papers=[dict(cite="Lupascu et al. 2020, Global Change Biology 26", doi="10.1111/gcb.15195", access="Closed",
                     da="Not read (closed access).", da_dl="Unknown")],
        how=("Water table and soil temperature monitored continuously from June 2017 to January 2019 in an intact and a "
             "repeatedly burnt forest; higher, longer-lasting water tables in the burnt area explain its higher CH4 efflux "
             "(from the abstract)."),
        notes=[], files=[]),
    dict(
        id="D1", folder="D1_SEA_WTD_model_Hooijer2026", name="SE Asia forested-peatland WTD model maps",
        status=DL, license="CC BY 4.0",
        links=[("Mendeley Data 69mbg22fxf", "https://doi.org/10.17632/69mbg22fxf")],
        papers=[dict(cite="Hooijer & Vernimmen 2026, Scientific Reports", doi="10.1038/s41598-026-64641-2",
                     access="Gold OA (CC-BY); also PMC13503653",
                     da="\"The rainfall and WTD maps presented in this paper are available online in GIS format (https://doi.org/10.17632/69mbg22fxf). ... updated maps can be shared by the authors upon reasonable request.\"",
                     da_dl="Yes (summary maps; daily series on request)")],
        how=("A simple water-balance model driven by GPM IMERG satellite rainfall produces 25 years of indicative daily WTD for "
             "forested peat, calibrated on four long-term records: Sarawak (Busman et al. 2023, 8 y), Riau (A8, 6 y), Central "
             "Kalimantan (A3, 16 y) and South Sumatra (C1, 5 y). Daily results are summarised into maps of hydrological regime "
             "(annual mean and minimum WTD, days below -0.5 m) to discuss variable WTD targets for restoration."),
        notes=["The published files are 10 summary GeoTIFFs, not daily grids; the index's 'daily, ~25 y' describes the model, "
               "not the download."],
        files=[
            f("Fig4a_WTD_annual_mean.tif", "SE Asia forested peat", "-6.1 to 7.4", "95.0 to 119.3", "Modelled natural PSF",
              "Annual mean WTD (m); EPSG:4326, 243 x 135 cells, 2797 peat cells", "Yes: " + NEG, "2000", "2024", "0.1 deg grid",
              2797, "", "-5.63 / -0.15 / -0.04"),
            f("Fig4b_WTD_min_overall_2000_2024.tif", "as above", "", "", "", "Minimum WTD over 2000-2024 (m)", "Yes: " + NEG,
              "2000", "2024", "0.1 deg grid", 2797, "", "-10.42 / -0.90 / -0.27"),
            f("Fig4c_WTD_annual_mean_min.tif", "as above", "", "", "", "Mean annual minimum WTD (m)", "Yes: " + NEG,
              "2000", "2024", "0.1 deg grid", 2797, "", "-6.10 / -0.44 / -0.16"),
            f("Fig4d_WTD_annual_mean_days_below_min0p5m.tif", "as above", "", "", "", "Mean days per year with WTD below -0.5 m", "Derived",
              "2000", "2024", "0.1 deg grid", 2797, "", "0 / 23.6 / 341 days"),
            f("Fig4e_WTD_longest_period_overall_wtd_below_0p5m_2000_2024.tif", "as above", "", "", "", "Longest period with WTD below -0.5 m (days)", "Derived",
              "2000", "2024", "0.1 deg grid", 2797, "", "0 / 103 / 366 days"),
            f("Fig2a-e_GPM_*.tif (5 files)", "as above", "", "", "", "GPM IMERG rainfall statistics (annual mean/min, 91-day minimum, dry-period length)", "No",
              "2000", "2024", "0.1 deg grid"),
        ]),
]

GAPS = ("No public continuous WTD series was found for Thailand (Kuan Kreng), Vietnam (U Minh), the Philippines "
        "(Leyte Sab-a, Agusan) or Sabah (Klias); these rows of the index have no folder.")

CORRECTIONS = [
    ("A1", "Water-level series", "4 wells (implied in one dataset)", "4 separate PANGAEA datasets (908201, 908206-908208), each with its own coordinates; 20-min steps"),
    ("A3", "DF coordinates", "'DF approx. same as DB'", "DF 2.35 S, 114.04 E (Hirano 2024); Hirano 2014 gives 114.14 E"),
    ("A3", "Data link", "figshare private link", "Link works (article 23826825, one 16.5 MB zip); GWL is half-hourly, not 'at least daily'"),
    ("A6", "Period in FLUXNET-CH4", "2011-2014", "FLUXNET-CH4 has 2014-2015 only; 2011-2014 is the paper's record"),
    ("A8", "Zenodo record", "7500659", "The paper cites 7728463 (v03); both downloaded, GWL identical"),
    ("A8", "WTD content", "Kampar GWL for 3 sites", "Only intact-site daily GWL is published; other sites only as annual means"),
    ("A8", "Acacia tower coordinate", "(not given)", "0.5159 N, 102.0364 E; confirmed by Deshmukh et al. 2020"),
    ("A12", "Availability", "A/B", "Not downloadable: Exeter files embargoed, paper says 'on request'"),
    ("A13-14", "Paper behind the CIFOR DOI", "Swails 2019", "DATA.00061 is the replication data of Hergoualc'h et al. 2017"),
    ("C5", "Availability", "C (figures only)", "Zenodo 10427000 (CC-BY) has manual water depth per chamber visit; hourly logger data not archived"),
    ("C8-9", "Availability", "C (figures only)", "Ledger 2023 supplement has manual and logger water tables and site coordinates"),
    ("C10-11", "Location", "Central Kalimantan, South Sumatra", "Central Kalimantan only"),
    ("D1", "Resolution", "Daily, ~25 y", "Download holds 10 summary GeoTIFFs (0.1 deg, 2000-2024); daily series only on request"),
]


def md_escape(s):
    return str(s).replace("|", "/")


def coord(lat, lon):
    if lat == "" and lon == "":
        return ""
    return "%s, %s" % (lat, lon)


def write_md():
    L = []
    L.append("# SE Asian peatland water-table data: what was downloaded\n")
    L.append("Checked %s. Periods, time steps, counts and value ranges below were measured from the downloaded files; "
             "methods and uses come from the papers. `INDEX.md` is the original search table; where they disagree, this "
             "file is the checked version (see *Corrections*).\n" % CHECKED)
    L.append("WTD sign convention: unless stated otherwise, negative = water table below the peat surface. "
             "Value ranges are min / mean / max.\n")

    L.append("## At a glance\n")
    L.append("| ID | Dataset | Status | WTD series in the download | Period (from files) | Resolution |")
    L.append("|---|---|---|---|---|---|")
    for d in DATASETS:
        w = [x for x in d["files"] if str(x["wtd"]).startswith("Yes:")]  # real series, not literature means
        starts = [x["start"] for x in w if x["start"]]
        ends = [x["end"] for x in w if x["end"]]
        period = "%s to %s" % (min(starts)[:10], max(ends)[:10]) if starts else "-"
        steps = sorted({x["step"] for x in w if x["step"]})
        L.append("| %s | %s | %s | %s | %s | %s |" % (
            d["id"], md_escape(d["name"]), d["status"],
            ("%d grids" if any("grid" in x["step"] for x in w) else "%d series") % len(w) if w else "none",
            period, md_escape("; ".join(steps)) if steps else "-"))
    L.append("\n" + GAPS + "\n")

    L.append("## What you still need to do\n")
    L.append("1. **FLUXNET-CH4 (A5, A6)**: sign in at fluxnet.org, request the FLUXNET-CH4 files for ID-Pag and MY-MLM "
             "(CC-BY-4.0), put the zips in `A5_.../data/` and `A6_.../data/`, commit them, and tell me; I will check them and "
             "update this summary.")
    L.append("2. **CIFOR (A13-14)**: data.cifor.org refused connections from the cloud. On your computer run "
             "`python3 download_data.py A13`.")
    L.append("3. **Papers**: PDFs are not committed (public repository). Run `python3 download_papers.py`; links that "
             "publishers block for scripts are printed so you can save them from a browser.")
    L.append("4. **Embargoed / on request**: A12, C1, C6, C10-11 (see the next section). No emails were sent.\n")

    L.append("## Data availability check: papers whose data you cannot download\n")
    L.append("| ID | Paper | What the paper says | Downloadable? |")
    L.append("|---|---|---|---|")
    for d in DATASETS:
        for p in d["papers"]:
            if p["da_dl"] not in ("Yes",) and not p["da_dl"].startswith("Yes") and p["da_dl"] != "n/a":
                L.append("| %s | %s ([doi](https://doi.org/%s)) | %s | %s |" % (
                    d["id"], md_escape(p["cite"]), p["doi"], md_escape(p["da"]), md_escape(p["da_dl"])))
    L.append("")

    L.append("## Corrections to INDEX.md\n")
    L.append("| ID | Field | Index said | Checked |")
    L.append("|---|---|---|---|")
    for c in CORRECTIONS:
        L.append("| %s | %s | %s | %s |" % tuple(md_escape(x) for x in c))
    L.append("")

    L.append("## Dataset details\n")
    for d in DATASETS:
        L.append("### %s: %s\n" % (d["id"], d["name"]))
        L.append("- **Folder:** `%s/`" % d["folder"])
        L.append("- **Status:** %s" % d["status"])
        L.append("- **Data source:** " + ", ".join("[%s](%s)" % (a, b) for a, b in d["links"]) +
                 ("; licence " + d["license"] if d["license"] else ""))
        for p in d["papers"]:
            L.append("- **Paper:** %s, [doi:%s](https://doi.org/%s). Access: %s." % (p["cite"], p["doi"], p["doi"], p["access"]))
            L.append("  - Data availability: %s" % p["da"])
        L.append("- **How the paper used the data:** " + d["how"])
        for n in d["notes"]:
            L.append("- " + n)
        if d["files"]:
            L.append("\n| File | Part | Site / station | Lat, Lon | Content | WTD | Start | End | Step | N | Missing | Range |")
            L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
            for x in d["files"]:
                L.append("| %s |" % " | ".join(md_escape(v) for v in (
                    "`%s`" % x["file"], x["part"], x["site"], coord(x["lat"], x["lon"]), x["content"], x["wtd"],
                    x["start"], x["end"], x["step"], x["n"], x["miss"], x["rng"])))
        L.append("")

    L.append("## Folder layout\n")
    L.append("```\nliterature/\n  INDEX.md             original search table\n  DATA_SUMMARY.md/.xlsx  this summary\n"
             "  download_data.py     re-downloads all public data (stdlib only)\n"
             "  download_papers.py   downloads the open-access papers and supplements\n"
             "  build_summary.py     regenerates this summary and the folder READMEs\n"
             "  <ID>_<site>_<paper>/\n    README.md  data/  paper/ (git-ignored)\n```\n")
    L.append("Git-ignored (kept only where they were downloaded): `*.pdf`, `*/paper/`, `*/data/_large/` (files over "
             "100 MB; none so far), `*/data/_unzipped/`.\n")
    with open(os.path.join(HERE, "DATA_SUMMARY.md"), "w") as fh:
        fh.write("\n".join(L))


def write_xlsx():
    wb = Workbook()
    head_font = Font(bold=True, color="FFFFFF")
    head_fill = PatternFill("solid", fgColor="305496")

    def sheet(ws, header, rows, widths):
        ws.append(header)
        for c in ws[1]:
            c.font, c.fill = head_font, head_fill
            c.alignment = Alignment(wrap_text=True, vertical="top")
        for r in rows:
            ws.append(r)
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w
        for row in ws.iter_rows(min_row=2):
            for c in row:
                c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.freeze_panes = "C2"
        ws.auto_filter.ref = ws.dimensions

    ws = wb.active
    ws.title = "Files"
    rows = []
    for d in DATASETS:
        for x in d["files"]:
            rows.append([d["id"], d["folder"] + "/data/" + x["file"], x["part"], x["site"], x["lat"], x["lon"], x["cover"],
                         x["content"], x["wtd"], x["start"], x["end"], x["step"], x["n"], x["miss"], x["rng"],
                         d["license"], d["links"][0][1] if d["links"] else "",
                         "; ".join("https://doi.org/" + p["doi"] for p in d["papers"]), d["how"]])
    sheet(ws, ["ID", "File", "Part / sheet / member", "Site / station", "Lat", "Lon", "Land cover", "Content",
               "WTD (unit; sign)", "Start", "End", "Time step", "N (WTD values)", "Missing", "WTD min / mean / max",
               "Licence", "Data source", "Paper(s)", "How the paper used the data"], rows,
          [7, 42, 26, 30, 10, 10, 22, 40, 26, 17, 17, 16, 10, 9, 20, 16, 30, 30, 70])

    ws = wb.create_sheet("Datasets")
    rows = [[d["id"], d["name"], d["status"], d["folder"], ", ".join(b for a, b in d["links"]), d["license"],
             len(d["files"]), " | ".join(d["notes"])] for d in DATASETS]
    sheet(ws, ["ID", "Dataset", "Status", "Folder", "Data link(s)", "Licence", "File rows", "Notes"], rows,
          [7, 40, 26, 38, 45, 20, 9, 90])

    ws = wb.create_sheet("Data availability")
    rows = [[d["id"], p["cite"], "https://doi.org/" + p["doi"], p["access"], p["da"], p["da_dl"]]
            for d in DATASETS for p in d["papers"]]
    sheet(ws, ["ID", "Paper", "DOI", "Paper access", "Data availability statement", "Data downloadable?"], rows,
          [7, 45, 35, 40, 80, 22])

    ws = wb.create_sheet("Corrections")
    sheet(ws, ["ID", "Field", "Index said", "Checked"], [list(c) for c in CORRECTIONS], [8, 25, 35, 80])
    wb.save(os.path.join(HERE, "DATA_SUMMARY.xlsx"))


def write_readmes():
    for d in DATASETS:
        path = os.path.join(HERE, d["folder"])
        os.makedirs(path, exist_ok=True)
        L = ["# %s: %s\n" % (d["id"], d["name"]), "**Status:** %s\n" % d["status"]]
        L.append("**Data source:** " + ", ".join("[%s](%s)" % (a, b) for a, b in d["links"]) +
                 ("; licence " + d["license"] if d["license"] else "") + "\n")
        for p in d["papers"]:
            L.append("**Paper:** %s, https://doi.org/%s (%s)\n" % (p["cite"], p["doi"], p["access"]))
            L.append("> Data availability: %s\n" % p["da"])
        L.append("**How the paper used the data:** %s\n" % d["how"])
        for n in d["notes"]:
            L.append("- " + n)
        if d["id"] in ("A5", "A6"):
            L.append("\n## Adding the FLUXNET-CH4 files\n")
            L.append("Sign in at https://fluxnet.org, open the site page linked above, request the FLUXNET-CH4 product "
                     "(CC-BY-4.0), and save the downloaded zip unchanged into `data/` in this folder. Commit it and tell "
                     "Claude, who will check it and update DATA_SUMMARY.")
        if d["files"]:
            L.append("\n## Files in `data/`\n")
            for x in d["files"]:
                L.append("- `%s`%s: %s. %s%s" % (x["file"], " (%s)" % x["part"] if x["part"] else "", x["content"],
                                                  "%s to %s, %s. " % (x["start"], x["end"], x["step"]) if x["start"] else "",
                                                  "WTD: " + x["wtd"] if str(x["wtd"]).startswith("Yes") else ""))
        L.append("\nFull details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py %s`.\n" % d["id"].split("-")[0])
        with open(os.path.join(path, "README.md"), "w") as fh:
            fh.write("\n".join(L))


if __name__ == "__main__":
    write_md()
    write_xlsx()
    write_readmes()
    print("wrote DATA_SUMMARY.md, DATA_SUMMARY.xlsx and %d folder READMEs" % len(DATASETS))
