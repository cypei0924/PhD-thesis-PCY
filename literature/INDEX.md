# SE Asian peatland water-table-depth (WTD) datasets — index

This is the starting table from the literature search, carried over as it was. Coordinates marked "≈" are regional estimates.
Every field is re-checked against the downloaded files and the original papers in `DATA_SUMMARY.md` / `DATA_SUMMARY.xlsx`;
where the two disagree, trust the summary.

Availability: **A** = public repository, direct download; **B** = portal or on request; **C** = only in the paper's figures/tables, contact authors.

| ID | Site / dataset | Location | Lat, Lon | Period | Resolution / accuracy | Avail. | Data · Paper | Folder |
|---|---|---|---|---|---|---|---|---|
| A1 | Mendaram peat dome (undrained) | Brunei, Belait | 4.367, 114.350 | 2012–2013 | Logged; Solinst Levelogger + barometric correction (±0.05% FS); 4 wells | A | [PANGAEA](https://doi.org/10.1594/PANGAEA.908215) · [Cobb & Harvey 2019](https://doi.org/10.1029/2019WR025411) | `A1_Mendaram_Cobb2019` |
| A2 | Mendaram water level + CO2 | Brunei | as A1 | 2012-02 – 2015-02 | Continuous | A | [Zenodo](https://zenodo.org/records/3245335) · [Hoyt 2019](https://doi.org/10.1111/gcb.14702) | `A2_Mendaram_Hoyt2019` |
| A3 | Palangkaraya: undrained forest UF / drained forest DF / burnt DB | Indonesia, Central Kalimantan | UF −2.32, 113.90; DB −2.34, 114.04; DF ≈ DB | ~2002–2017 (12–15 y per site) | Fluxes half-hourly; WTD at least daily | A | [figshare](https://figshare.com/s/6aefe20137486d0a6f62) · [Hirano 2024](https://doi.org/10.1038/s43247-024-01387-7) | `A3_Palangkaraya_Hirano2024` |
| A4 | Palangkaraya daily groundwater level | as A3 | ≈−2.3, 113.9–114.0 | undrained 2015–2018; drained 2013–2017 | Daily | A | [figshare](https://figshare.com/articles/dataset/DailyGWL_xlsx/22321129/1) | `A4_Palangkaraya_DailyGWL` |
| A5 | FLUXNET-CH4 ID-Pag | as A3 | −2.32, 113.90 | 2016–2017 | Half-hourly | A (login) | [data](https://doi.org/10.18140/FLX/1669643) · [Sakabe 2018](https://doi.org/10.1111/gcb.14410) | `A5_FLUXNET-CH4_ID-Pag_Sakabe2018` |
| A6 | FLUXNET-CH4 MY-MLM (Maludam) | Malaysia, Sarawak | 1.4536, 111.1495 | 2011–2014 (Tang 2020) | Half-hourly | A (login; full record from TROPI) | [data](https://doi.org/10.18140/FLX/1669650) · [Tang 2020](https://doi.org/10.1111/gcb.15332) | `A6_FLUXNET-CH4_MY-MLM_Tang2020` |
| A7 | Kampar intact vs degraded forest | Indonesia, Riau | ≈0.3, 102.8 | mid-2017 – mid-2020 | Fluxes half-hourly; WTD continuous | A | [Zenodo](https://doi.org/10.5281/zenodo.4835696) · [Deshmukh 2021](https://doi.org/10.1038/s41561-021-00785-2) | `A7_Kampar_Deshmukh2021` |
| A8 | Kampar Acacia plantation / degraded / intact forest | Indonesia, Riau | ≈0.3, 102.8 | 2016-10 – 2022-05 | as A7 | A | [Zenodo](https://zenodo.org/records/7500659) · [Deshmukh 2023](https://doi.org/10.1038/s41586-023-05860-9) | `A8_Kampar_Deshmukh2023` |
| A9 | 8 automatic stations (Batanghari, Kubu Raya) | Indonesia, Jambi & West Kalimantan | ≈−1.7, 103.1; ≈−0.4, 109.4 | 2018–2019 | Daily | A (paper attachment) | [Taufik 2022](https://www.sciencedirect.com/science/article/pii/S2352340922001159) | `A9_Jambi_KubuRaya_Taufik2022` |
| A11 | 48 smallholder plots (SUSTAINPEAT) | Malaysia, Selangor; Indonesia, West & Central Kalimantan | see dataset | 2018–2019 | Monthly manual (~±1 cm) | A | [Nottingham RDMC](https://rdmc.nottingham.ac.uk/handle/internal/10505) · [Jovani-Sancho 2023](https://doi.org/10.1111/gcb.16747) | `A11_SUSTAINPEAT_JovaniSancho2023` |
| A12 | Sebungan oil-palm flux site | Malaysia, Sarawak | 3.166, 113.353 | multi-year | Half-hourly | A/B (WTD content unconfirmed) | [Exeter ORE](https://ore.exeter.ac.uk/repository/handle/10871/124993) · [McCalmont 2021](https://doi.org/10.1111/gcb.15544) | `A12_Sebungan_McCalmont2021` |
| A13–14 | CIFOR Central Kalimantan: primary forest vs oil palm | Indonesia, Central Kalimantan | see paper | 13 months; 2014-01 – 2015-09 | Monthly manual | A | [CIFOR Dataverse](https://data.cifor.org/dataset.xhtml?persistentId=doi:10.17528/CIFOR/DATA.00061&version=1.0) · [Swails 2019](https://doi.org/10.1007/s10533-018-0519-x) | `A13-14_CIFOR_CentralKalimantan_Swails2019` |
| B1 | SiPALAGA network (BRGM) | Indonesia, 7 provinces | per station (e.g. BRG_621103_05) | ~2018 – present | 10-min logging, hourly upload; ~142 stations by end-2018 | B | [use case, RSE 2025](https://www.sciencedirect.com/science/article/pii/S0034425725004134) | `B1_SiPALAGA_BRGM` |
| B2 | SiMATAG-0.4m (KLHK) | Indonesia, national | per point | 2019 – present | 9,603 compliance points | C (not public) | [KLHK](https://ppid.menlhk.go.id/berita/siaran-pers/4915/menteri-lhk-luncurkan-simatag-04m-untuk-monitoring-keberhasilan-pemulihan-gambut) | `B2_SiMATAG_KLHK` |
| C1 | South Sumatra rewetting trial (257 dams) | Indonesia, South Sumatra | see paper | 7.5 y monitoring | Dipwell network | C | [Hooijer 2024](https://doi.org/10.1038/s41598-024-60462-3) | `C1_SouthSumatra_Hooijer2024` |
| C3 | Pulau Padang land-use units | Indonesia, Riau | ≈1.1, 102.3 | see paper | Multiple loggers | C | [Ismail 2021](https://iwaponline.com/hr/article/52/6/1372/84954/Water-table-variations-on-different-land-use-units) | `C3_PulauPadang_Ismail2021` |
| C5 | East Kalimantan undrained forest | Indonesia | see paper | 2022-10 – 2023-09 | Concurrent with fluxes | C | [Asyhari 2024](https://doi.org/10.1038/s41598-024-62233-6) | `C5_EastKalimantan_Asyhari2024` |
| C6 | Sarawak secondary forest → oil palm flux site | Sri Aman | see paper | from 2010, 9 y | Half-hourly | C | [Kiew 2025](https://www.sciencedirect.com/science/article/abs/pii/S0168192325005751) | `C6_Sarawak_Kiew2025` |
| C7 | Sarawak catchment, 4 stations | Sarawak | see paper | 2011–2015 | Monthly analysis | C | [Aeries 2023](https://ejournal.unimap.edu.my/index.php/aset/article/view/331) | `C7_Sarawak_Aeries2023` |
| C8–9 | North Selangor peat swamp forest | Malaysia | ≈3.7, 101.3 | 2013-12 – 2016-12, plus camera | Monthly / sub-daily | C | [Lo & Parish 2022](https://www.corpuspublishers.com/assets/articles/aart-v3-22-1029.pdf) · [Ledger 2023](https://doi.org/10.3389/fenvs.2023.1182100) | `C8-9_NorthSelangor_LoParish2022_Ledger2023` |
| C10–11 | Time-lapse camera WTD | Central Kalimantan, South Sumatra | see paper | 1–2 y | ≤2-hourly | C | [Evans 2021](https://doi.org/10.3389/fenvs.2021.630752) | `C10-11_TimelapseCamera_Evans2021` |
| C12 | Badas burnt vs intact forest | Brunei | ≈4.6, 114.4 | see paper | Dipwells | C | [Lupascu 2020](https://doi.org/10.1111/gcb.15195) | `C12_Badas_Lupascu2020` |
| D1 | SE Asia natural peat forest WTD maps (model) | Regional | 10 km grid | ~25 y | Daily | A | [Mendeley Data](https://doi.org/10.17632/69mbg22fxf) · [Hooijer 2026](https://doi.org/10.1038/s41598-026-64641-2) | `D1_SEA_WTD_model_Hooijer2026` |

**Gaps (no public continuous WTD series found, 2016–2026):** Thailand (Kuan Kreng), Vietnam (U Minh), Philippines (Leyte Sab-a, Agusan), Malaysia Sabah (Klias).
