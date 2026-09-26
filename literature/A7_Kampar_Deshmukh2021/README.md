# A7: Kampar Peninsula intact vs degraded peatland, Riau

**Status:** Downloaded

**Data source:** [Zenodo 4835696](https://doi.org/10.5281/zenodo.4835696); licence CC-BY-4.0

**Paper:** Deshmukh et al. 2021, Nature Geoscience 14, https://doi.org/10.1038/s41561-021-00785-2 (Accepted manuscript (Word) on figshare 15073734)

> Data availability: "All data that support the findings of this study are archived on http://doi.org/10.5281/zenodo.4835696."

**How the paper used the data:** GWL was logged every 30 min (Solinst Levelogger 3001 in perforated PVC tubes anchored into the clay; 3 loggers at the intact site, 2 at the degraded site; datum = base of the hollows). Daily GWL is shown against cumulative rainfall and ET (Fig. 2) to explain drawdown in the 2019 positive-IOD/El Nino drought. NEE and CH4 are bin-averaged by GWL (Fig. 3, ED Fig. 2): the intact site approaches CO2 neutrality when hollows are flooded, while NEE at the degraded site is insensitive to GWL between -0.4 and -0.8 m. ED Fig. 3 compares GWL-NEE with literature.

- The text reports degraded-site GWL for Oct 2016 - Sep 2020, but the published daily series (Fig. 2b) covers only Jun 2017 - May 2020.

## Files in `data/`

- `Deshmukh_Fig2.xlsx` (Panel a): Daily GWL_IP and SD, cumulative rain, ET. 2017-06-01 to 2020-05-31, 1 d. WTD: Yes: m; negative = below hollow surface
- `Deshmukh_Fig2.xlsx` (Panel b): Daily GWL_DP and SD, cumulative rain, ET. 2017-06-01 to 2020-05-31, 1 d. WTD: Yes: as above
- `Deshmukh_Fig2.xlsx` (Panels c, d): Daily cumulative NEE and CH4 with uncertainty. 2017-06-01 to 2020-05-31, 1 d. 
- `Deshmukh_Fig1.xlsx`: Coordinates (DMS). 
- `Deshmukh_Fig3.xlsx`: NEE and CH4 bin-averaged by GWL. 
- `Deshmukh_ED_Fig2.xlsx`: NEE, Reco, GPP by GWL bin; GPP-PPFD above/below a GWL threshold. 
- `Deshmukh_ED_Fig3.xlsx`: Compilation of GWL vs NEE from other studies. WTD: Yes (site means)
- `Deshmukh_ED_Fig1.xlsx`: Monthly rainfall 2016-2020; Jul-Sep rainfall 1991-2020 with SOI and DMI. 1991 to 2020, 1 month. 
- `Deshmukh_ED_Fig4.xlsx`: Soil N2O fluxes by month. 2019-06 to 2020-05, ~monthly. 
- `Deshmukh_ED_Fig5.xlsx`: Daily PPFD, Tair, VPD, soil T. 2017-06-01 to 2020-05-31, 1 d. 
- `Deshmukh_ED_Fig6.xlsx`: Daily PPFD, Tair, VPD, soil T. 2016-10-01 to 2020-09-30, 1 d. 

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A7`.
