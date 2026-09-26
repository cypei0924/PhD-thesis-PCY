# A13-14: CIFOR Central Kalimantan: primary forest vs oil palm

**Status:** Public, but server unreachable from the cloud

**Data source:** [CIFOR Dataverse doi:10.17528/CIFOR/DATA.00061](https://doi.org/10.17528/CIFOR/DATA.00061); licence CIFOR Dataverse (terms not readable from the cloud)

**Paper:** Hergoualc'h et al. 2017, Biogeochemistry 135:203-220 (the paper DATA.00061 belongs to), https://doi.org/10.1007/s10533-017-0363-4 (Hybrid OA (CC-BY); Springer blocks scripts, open in a browser)

> Data availability: Not read (Springer bot check). The CIFOR record is titled 'Replication Data for: ... Biogeochemistry 135(3): 203-220'.

**Paper:** Swails et al. 2019, Biogeochemistry 142 (the paper named in the index), https://doi.org/10.1007/s10533-018-0519-x (Closed)

> Data availability: Not read (closed access).

**How the paper used the data:** Hergoualc'h 2017: total and heterotrophic soil respiration over 13 months in trenched vs control plots in a primary peat swamp forest and two oil palm plantations (planted 2007 and 2012). Swails 2019 (same group, closed) relates soil respiration to climatic drivers in the same kind of forest vs oil palm comparison. The CIFOR record contains three databases: DBCollar (monthly and/or daily data per respiration collar), DBSoilMoisture, DBLitterfall; whether DBCollar includes WTD could not be checked.

- data.cifor.org dropped every TLS connection from the cloud, so nothing was downloaded. Run `python3 download_data.py A13` on your computer; it resolves the files through the Dataverse API.
- The index links DATA.00061 to Swails 2019, but the record belongs to Hergoualc'h et al. 2017.
- Other CIFOR records from this group (not in the index): DATA.00201, 00290, 00291, 00330, 00331.

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A13`.
