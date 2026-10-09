# D11: Canal water depth from LiDAR (Central Kalimantan 2011) and SE Asia canal map

**Status:** Downloaded (part of the data)

**Data source:** [Mendeley 7nnf495jbw (Vernimmen 2020)](https://doi.org/10.17632/7nnf495jbw), [Stanford SDR yj761xk5815 (Dadap 2021 canals)](https://doi.org/10.25740/yj761xk5815); licence CC BY 4.0

**Paper:** Vernimmen et al. 2020, Water 12, https://doi.org/10.3390/w12051486 (Open access, but the publisher blocked the download; abstract only)

> Data availability: Not read (MDPI blocked); the Mendeley record states it is the map 'as published in Vernimmen et al. 2020'.

**Paper:** Dadap et al. 2021, AGU Advances 2, https://doi.org/10.1029/2020AV000321 (Open access, but the publisher blocked the download; abstract only)

> Data availability: Not read; the canal map is on the Stanford Digital Repository (CC BY-ND 3.0).

**How the paper used the data:** Vernimmen: canal water-table depth (CWD) from airborne LiDAR (minimum of a 100 m grid on a 1 m DTM vs median surface), validated against 145 field measurements (within 0.25 m for 86 %). Dadap: CNN-mapped drainage canals and roads (5 m, from 2017 Planet imagery) across Borneo, Sumatra and Peninsular Malaysia, related to fire and carbon emissions.

- The Stanford canal map is a canal mask (not WTD) and was not downloaded; its file list is only shown by a browser.

## Files in `data/`

- `CWD_100.0m_CentralKalimantan_UTM50S_DrySeason2011.tif`: Canal water depth below surrounding surface (m), 100 m grid, dry season 2011. 2011 (dry season) to , one map. 

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py D11`.
