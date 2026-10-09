# A18: Pangkalan Bun forests and oil palm, CH4/N2O and WT (CIFOR), Central Kalimantan

**Status:** Public, but server unreachable from the cloud

**Data source:** [CIFOR Dataverse DATA.00201](https://doi.org/10.17528/CIFOR/DATA.00201)

**Paper:** Swails et al. 2021, Frontiers in Environmental Science 9, https://doi.org/10.3389/fenvs.2021.617828 (Open; downloaded to paper/)

> Data availability: 'The datasets presented in this study can be found in online repositories ... https://doi.org/10.17528/CIFOR/DATA.00201.'

**How the paper used the data:** Monthly CH4 and N2O fluxes with water table depth, soil moisture and temperature from January 2014 to September 2015 (no monitoring in July-August 2014) in three undrained forest plots (FOR-1 to FOR-3) and three smallholder oil palm plots (OP-2007, OP-2009, OP-2011). Dipwells were installed next to each gas collar (hummock and hollow in forest, near and far from palms in oil palm), 12 per plot. WT controlled monthly N2O variation in forest; CH4 was high in forest and negligible in oil palm. The study spans a normal (2014) and a strong El Nino year (2015).

- Plot coordinates (Swails 2021, Table 1): FOR-1 S 2 49.410 E 111 48.784; FOR-2 S 2 49.341 E 111 50.434; FOR-3 S 2 50.852 E 111 48.155; OP-2011 S 2 47.379 E 111 48.624; OP-2009 S 2 47.292 E 111 48.190; OP-2007 S 2 47.230 E 111 48.089 (about 10 km from Pangkalan Bun).
- Same plots and campaign as Swails et al. 2019 (INDEX A13-14 / your A14): the WT behind both papers is the same measurement.
- data.cifor.org refused connections from the cloud; run `python3 download_data.py A18` locally. The paper's supplement is saved in paper/: Table S3 gives plot-mean WT (cm, +/- SE): FOR-1 -24.0, FOR-2 -28.8, FOR-3 -16.7, OP-2007 -58.1, OP-2009 -58.0, OP-2011 -33.5.

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A18`.
