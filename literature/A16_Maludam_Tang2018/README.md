# A16: Maludam (MY-MLM) tower, half-hourly CH4 flux and WT, Sarawak

**Status:** Downloaded

**Data source:** [Zenodo 1161966](https://doi.org/10.5281/zenodo.1161966); licence CC-BY-4.0

**Paper:** Tang et al. 2018, Geophysical Research Letters 45, https://doi.org/10.1029/2017GL076457 (Open access, but the publisher blocked the download; abstract only)

> Data availability: Not read. The Zenodo record is titled 'Methane flux data from a tropical peat swamp forest in Sarawak, Malaysia'.

**How the paper used the data:** Eddy-covariance CH4 flux over a 2-month wet-season period (Nov-Dec 2013): mean daily FCH4 about 0.024 g C m-2 d-1. A linear model showed air temperature controlled FCH4 before the water table reached the surface, and water table alone explained about 20 % of FCH4 variability once standing water emerged (abstract).

- Same tower and forest as A6 and A15; this file adds a half-hourly WT record for Nov-Dec 2013, which is not in the daily A15 file at sub-daily resolution.
- WT sign is inferred from the values (mean +5.3 cm in the wet season, standing water in the paper).

## Files in `data/`

- `CH4Data.xlsx` (CH4_TROPI): Sheet CH4_TROPI: radiation, Ta, RH, VPD, wind, Tsoil, VWC, WT (cm), u*, H, LE, CH4 flux, NEE. 2013-11-01 00:00 to 2013-12-31 23:30, 30 min. WTD: Yes: cm; negative = below peat surface (positive = standing water)

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A16`.
