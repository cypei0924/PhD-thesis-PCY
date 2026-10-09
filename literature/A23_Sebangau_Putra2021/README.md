# A23: Sebangau forested, ditch-blocked and drained sites: water levels, rainfall, PET (Leeds)

**Status:** Downloaded

**Data source:** [University of Leeds 10.5518/960](https://doi.org/10.5518/960); licence CC BY 4.0

**Paper:** Putra et al. 2021, Hydrological Processes 35, https://doi.org/10.1002/hyp.14174 (Open access, but the publisher blocked the download; abstract only)

> Data availability: Repository record lists this paper and Putra's 2021 Leeds thesis as the users of the data.

**Paper:** Putra et al. 2023, Mires and Peat 29, https://doi.org/10.19189/MaP.2022.OMB.StA.2407 (Open; saved in C19_Sebangau_Putra2021/paper/)

> Data availability: Uses the same loggers.

**How the paper used the data:** Six-month hydrological monitoring (22 Aug 2019 - 17 Jan 2020) at three sites in Sebangau National Park: Forested (6 vented loggers, 3-hourly), Blocked (4 well loggers, 2 ditch loggers, 7 manual wells) and Drained (3 well loggers, 2 ditch loggers, 7 manual wells), plus two weather stations (rainfall, PET by Penman-Monteith). Putra 2021 compared water-level dynamics with and without ditch dams; Putra 2023 analysed water-table responses to individual storms.

- Logger files give ABSOLUTE water level (cm) relative to a local site benchmark, not depth below the surface; the manual files give water table from the surface (cm). Convert loggers with the well surface elevations in the papers.
- Coordinates: Forested benchmark (well AL0) 2.3894 S, 113.4524 E; Blocked and Drained are 2.7-3.5 km from the Tumbang Nusa camp gauge (2.3556 S, 114.0896 E) (Putra 2023).
- forested_rainfall.csv holds 149 daily rows followed by 5-minute records under the same header.
- Related public files not downloaded: temperature data on figshare (doi:10.6084/m9.figshare.14900181, MIT) and DigiBog model files (doi:10.5518/1053). Your C19 is the same study.

## Files in `data/`

- `forested_auto_wl_AL0.csv, _AL1.csv, _AL5.csv`: Absolute water level (cm, local benchmark). 2019-08-23 15:00 to 2020-01-18 06:00, 3 h. 
- `forested_auto_wl_BL1.csv, _BL5.csv, _BR2.csv`: As above. 2019-11-08 12:00 to 2020-01-18 06:00, 3 h. 
- `blocked_auto_wl_BB1.csv, _BB2.csv, _BB3.csv, _CA2.csv`: As above. 2019-09-01 18:00 to 2020-01-14 12:00, 3 h. 
- `blocked_auto_wl_DS.csv, _US.csv`: Ditch water level (cm, benchmark). 2019-10-30 06:00 to 2020-01-14 11:30, 30 min. 
- `drained_auto_wl_AA1.csv, _AA2.csv, _AA3.csv`: As above. 2019-08-31 21:00 to 2020-01-25 09:00, 3 h. 
- `drained_auto_wl_BD.csv, _SD.csv`: Ditch water level (cm, benchmark). 2019-10-30 06:00 to 2020-01-15 23:00, 30 min. 
- `forested_man_wl.csv`: Manual WT from surface (cm). 2019-08-23 to 2020-01-18, 12 readings. WTD: Yes: cm; negative = below peat surface
- `blocked_man_wl.csv`: Manual WT from surface (cm). 2019-09-11 to 2019-12-12, visits. WTD: Yes: cm; negative = below peat surface
- `drained_man_wl.csv`: Manual WT from surface (cm). 2019-09-11 to 2019-12-13, visits. WTD: Yes: cm; negative = below peat surface
- `forested_rainfall.csv, drained_blocked_rainfall.csv, forested_PET.csv, drained_blocked_PET.csv, readme.txt`: Rainfall (daily; forest also 5-min), daily PET (mm). 2019-08-22 to 2020-01-18, 1 d / 5 min. 

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A23`.
