# C8-9: North Selangor peat swamp forest, Malaysia

**Status:** Downloaded (part of the data)

**Data source:** [Ledger 2023 supplementary DataSheet1/2](https://doi.org/10.3389/fenvs.2023.1182100); licence CC-BY (Frontiers supplementary material)

**Paper:** Lo & Parish 2022, Archives of Agriculture Research and Technology 3, https://doi.org/10.54026/aart/1029 (Gold OA, but the publisher's TLS certificate has expired; open in a browser at your own risk)

> Data availability: Not read (publisher certificate expired).

**Paper:** Ledger et al. 2023, Frontiers in Environmental Science 11:1182100, https://doi.org/10.3389/fenvs.2023.1182100 (Gold OA (CC-BY))

> Data availability: "The original contributions presented in the study are included in the article/Supplementary Material, further inquiries can be directed to the corresponding author."

**How the paper used the data:** Lo & Parish 2022: monthly groundwater table on transects Dec 2013 - Dec 2016 in logged-over forest, degraded open land and smallholder oil palm, and the effect of drains (from the abstract). Ledger 2023: peat surface oscillation at 14 sites (288 subsidence poles, 3 time-lapse cameras); water table from piezometers read manually with the poles and logged automatically at two camera sites; used to show that oscillation magnitude depends on peat condition and water-table range.

- The index rated C8-9 as 'figures only'; Ledger 2023's supplement contains the raw water-table data.
- Lo & Parish 2022 data (2013-2016) remain unavailable.

## Files in `data/`

- `Ledger2023_DataSheet1.XLSX` (sheet Jul18Jan20_m_tidy): Manual water table (m) read with the subsidence poles. 2018-08-15 to 2020-02-06, 5 occasions. WTD: Yes: m; negative = below peat surface
- `Ledger2023_DataSheet1.XLSX` (sheet Automated_datasets): Adjusted water table level (cm, m) and camera peat-surface elevation. 2019-04-20 to 2020-01-20, 1 d (12:00 reading). WTD: Yes: cm; negative = below peat surface
- `Ledger2023_DataSheet1.XLSX` (sheet Automated_datasets): Water table relative to peat surface (cm, m) and camera peat-surface elevation. 2019-04-11 to 2020-01-20, 1 d (12:00 reading). WTD: Yes: as above
- `Ledger2023_DataSheet1.XLSX` (other sheets): Subsidence poles, surface oscillation, bulk density, Rock-Eval. 2018-08 to 2020-02, monthly/irregular. 
- `Ledger2023_DataSheet2.XLSX` (Supplementary tables 3-4): Site coordinates (X = lon, Y = lat), land cover, peat depth and properties. 

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py C8`.
