# A19: Berbak primary forest, drained forest and oil palm (CIFOR), Jambi

**Status:** Public, but server unreachable from the cloud

**Data source:** [CIFOR DATA.00290 (Swails 2023)](https://doi.org/10.17528/CIFOR/DATA.00290), [CIFOR DATA.00330 / 00331 (Swails 2026)](https://doi.org/10.17528/CIFOR/DATA.00330), [CIFOR DATA.00316 (Hergoualc'h 2026)](https://doi.org/10.17528/CIFOR/DATA.00316)

**Paper:** Swails et al. 2023, Biogeochemistry 167, https://doi.org/10.1007/s10533-023-01070-7 (Open; downloaded to paper/)

> Data availability: 'The datasets generated and analyzed during the current study are available in the Dataverse repository, https://doi.org/10.17528/CIFOR/DATA.00290.'

**Paper:** Swails et al. 2026, Geoderma, https://doi.org/10.1016/j.geoderma.2026.118030 (Open access, but the publisher blocked the download; abstract only)

> Data availability: Not read; CIFOR DATA.00330 (raw) and DATA.00331 (summary) carry this paper's title.

**Paper:** Hergoualc'h et al. 2026, Royal Society Open Science, https://doi.org/10.1098/rsos.252443 (Open access, but the publisher blocked the download; abstract only)

> Data availability: Not read; CIFOR DATA.00316 is titled 'Supporting summary data of the paper Hergoualc'h et al. (2026)'.

**Paper:** Comeau et al. 2016, Geoderma 268, https://doi.org/10.1016/j.geoderma.2016.01.016 (Abstract only (closed access or the publisher blocked the download); full text not read)

> Data availability: Not read (closed; no abstract available).

**How the paper used the data:** Swails 2023: monthly N2O and CH4 fluxes, water table depth (2 m PVC dipwell next to each collar), soil moisture and temperature from October 2011 to March 2013 in a primary forest (Berbak National Park), a logged and drained forest and an oil palm plantation, plus intensive sampling after two fertilisation events; N2O fell logarithmically and CH4 rose as the water table approached the surface in the forests. Swails 2026: monthly total and heterotrophic soil respiration with environmental variables over 2012-2013 at the same three sites. Hergoualc'h 2026: monthly fluxes for a year and daily for a month after two fertilisations in an oil palm N-fertiliser trial on peat (abstract).

- Coordinates (Swails 2023): primary forest 1 27 S, 104 21 E (core of Berbak NP, 2 km from the Batang Hari); drained forest and oil palm about 60 km WSW, 1 39 S, 103 52 E.
- The CIFOR record descriptions for DATA.00290 and 00330/00331 are copy-paste errors (they describe Congo/Cameroon and food-system data); the titles identify the papers.
- The trial in Hergoualc'h 2026 and Comeau 2016 is probably at the same Jambi oil palm site; not confirmed from full text.
- data.cifor.org refused connections from the cloud; run `python3 download_data.py A19` locally.

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A19`.
