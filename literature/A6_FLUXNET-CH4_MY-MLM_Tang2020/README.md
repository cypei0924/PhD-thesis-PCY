# A6: FLUXNET-CH4 MY-MLM (Maludam National Park), Sarawak

**Status:** Needs your login (FLUXNET)

**Data source:** [FLUXNET site page](https://fluxnet.org/sites/siteinfo/MY-MLM), [Data DOI](https://doi.org/10.18140/FLX/1669650); licence CC-BY-4.0 (FLUXNET-CH4 Community Product)

**Paper:** Tang et al. 2020, Global Change Biology 26, https://doi.org/10.1111/gcb.15332 (Closed)

> Data availability: Not read (closed access).

**How the paper used the data:** Eddy-covariance CO2 exchange over a peat swamp forest in 2011-2014: the forest was a net CO2 source every year (183-632 g C m-2 yr-1); path analysis identified vapour-pressure deficit, not water table, as the main driver of GPP and RE (from the abstract).

- FLUXNET-CH4 covers only 2014-2015 for MY-MLM, not the 2011-2014 period of Tang 2020; the full record is held by the Sarawak Tropical Peat Research Institute.
- FLUXNET site metadata: 1.4536, 111.1495, AsiaFlux, EBF. C7 (Aeries 2023) has 2011-2015 water-table loggers in the same national park.
- Daily WT for this forest for 2011-2014 is public on figshare (doi:10.6084/m9.figshare.25299358) and half-hourly WT for Nov-Dec 2013 on Zenodo (doi:10.5281/zenodo.1161966); see EXPANDED_2006-2026 rows A15-A16.

## Adding the FLUXNET-CH4 files

Sign in at https://fluxnet.org, open the site page linked above, request the FLUXNET-CH4 product (CC-BY-4.0), and save the downloaded zip unchanged into `data/` in this folder. Commit it and tell Claude, who will check it and update DATA_SUMMARY.

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A6`.
