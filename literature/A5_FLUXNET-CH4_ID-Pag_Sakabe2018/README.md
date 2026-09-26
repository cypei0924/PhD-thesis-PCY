# A5: FLUXNET-CH4 ID-Pag (Palangkaraya undrained forest)

**Status:** Needs your login (FLUXNET)

**Data source:** [FLUXNET site page](https://fluxnet.org/sites/siteinfo/ID-Pag), [Data DOI](https://doi.org/10.18140/FLX/1669643); licence CC-BY-4.0 (FLUXNET-CH4 Community Product)

**Paper:** Sakabe et al. 2018, Global Change Biology 24, https://doi.org/10.1111/gcb.14410 (Free to read on Wiley (bronze); Wiley blocks scripts)

> Data availability: Not read (Wiley blocked automated access).

**How the paper used the data:** One year of eddy-covariance CH4 flux over the undrained forest (same tower as A3 UF). The forest was a small CH4 sink in the dry season and a source in the wet season, controlled by groundwater level; anaerobic incubations compared CH4 production in undrained, drained and burned soils (from the abstract).

- FLUXNET site metadata: -2.3200, 113.9000, elevation 30 m, AsiaFlux, EBF; FLUXNET-CH4 years 2016-2017.
- Whether the FLUXNET-CH4 file contains a WTD column for this site has to be checked after you download it.

## Adding the FLUXNET-CH4 files

Sign in at https://fluxnet.org, open the site page linked above, request the FLUXNET-CH4 product (CC-BY-4.0), and save the downloaded zip unchanged into `data/` in this folder. Commit it and tell Claude, who will check it and update DATA_SUMMARY.

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A5`.
