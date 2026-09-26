# A9: 8 BRGM automatic stations, Batanghari (Jambi) and Kubu Raya (West Kalimantan)

**Status:** Downloaded

**Data source:** [Data in Brief attachment mmc1.xlsx (via Europe PMC PMC8847808)](https://doi.org/10.1016/j.dib.2022.107903); licence CC BY-NC-ND (Data in Brief article licence)

**Paper:** Taufik et al. 2022, Data in Brief 41:107903, https://doi.org/10.1016/j.dib.2022.107903 (Gold OA; ScienceDirect blocks scripts, full text read via Europe PMC)

> Data availability: "Data available within the article and within Supplementary files"

**Paper:** Taufik et al. 2022, Agricultural and Forest Meteorology 312:108738 (research article using the data), https://doi.org/10.1016/j.agrformet.2021.108738 (Closed)

> Data availability: Not read (closed access).

**How the paper used the data:** Groundwater table was measured in a slotted 2-inch PVC well at each station, logged every 10 min, averaged to daily values in R, and recalibrated against manual readings every 3 months. In Taufik et al. 2022 (AFM) the daily GWT feeds a 'water table factor' in an improved drought-fire risk model; the water-retention curves ('wrc' sheet) give how much the water table re-wets the surface peat.

- 'BRG' stations belong to the peat restoration agency BRG/BRGM, i.e. they are SiPALAGA stations (B1).
- Coordinates are published only for BRG6 and BRG18; the others appear only on the map in Fig. 1.
- % missing = share of days without data between each station's first and last record.

## Files in `data/`

- `mmc1.xlsx` (sheet gwt): Daily groundwater table (m). 2018-04-08 to 2019-08-27, 1 d. WTD: Yes: m; negative = below peat surface
- `mmc1.xlsx` (sheet gwt): Daily groundwater table (m). 2018-04-08 to 2018-12-28, 1 d. WTD: Yes: m; negative = below peat surface
- `mmc1.xlsx` (sheet gwt): Daily groundwater table (m). 2018-04-11 to 2019-12-31, 1 d. WTD: Yes: m; negative = below peat surface
- `mmc1.xlsx` (sheet gwt): Daily groundwater table (m). 2018-04-11 to 2019-10-07, 1 d. WTD: Yes: m; negative = below peat surface
- `mmc1.xlsx` (sheet gwt): Daily groundwater table (m). 2018-04-12 to 2019-06-20, 1 d. WTD: Yes: m; negative = below peat surface
- `mmc1.xlsx` (sheet gwt): Daily groundwater table (m). 2018-04-12 to 2018-12-31, 1 d. WTD: Yes: m; negative = below peat surface
- `mmc1.xlsx` (sheet gwt): Daily groundwater table (m). 2018-04-12 to 2019-11-14, 1 d. WTD: Yes: m; negative = below peat surface
- `mmc1.xlsx` (sheet gwt): Daily groundwater table (m). 2018-04-13 to 2019-12-31, 1 d. WTD: Yes: m; negative = below peat surface
- `mmc1.xlsx` (sheet wrc): Modelled water-retention curves (van Genuchten), top- and sub-soil. 

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A9`.
