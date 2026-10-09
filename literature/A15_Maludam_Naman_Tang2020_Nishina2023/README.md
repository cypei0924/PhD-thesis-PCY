# A15: Maludam undrained peat swamp forest and Naman oil palm, daily WT, Sarawak

**Status:** Downloaded

**Data source:** [figshare (Melling & Wong 2024)](https://doi.org/10.6084/m9.figshare.25299358); licence CC BY 4.0

**Paper:** Tang et al. 2020, Global Change Biology 26, https://doi.org/10.1111/gcb.15332 (Abstract only (closed access or the publisher blocked the download); full text not read)

> Data availability: Not read (closed). Koupaei-Abyazani et al. 2024 (D10) state that the Malaysian WT data are in Melling & Wong 2024 on figshare.

**Paper:** Nishina et al. 2023, Science of the Total Environment 870, https://doi.org/10.1016/j.scitotenv.2023.162062 (Open access, but the publisher blocked the download; abstract only)

> Data availability: Not read.

**How the paper used the data:** Tang 2020 measured eddy-covariance CO2 exchange at the Maludam (MY-MLM) tower for 4 years (2011-2014) and found the forest a net CO2 source every year (183-632 g C m-2 yr-1); the daily WT file is the water table behind that record. Nishina 2023 monitored dissolved N2O in the drainage of oil palm plantations on peat near Sibu (dry and wet season surveys). Koupaei-Abyazani 2024 (D10) used both daily series (as 'MA-undrained' 2011-2014 and 'MA-converted' 2018-2019) to validate Landsat OPTRAM water-table estimates.

- Coordinates from Koupaei-Abyazani et al. 2024, Table 1: MA-undrained 1.4536 N, 111.1494 E; MA-converted 2.1860 N, 111.8459 E.
- The figshare page blocks scripts with a bot check; the files were saved with a headless browser. download_data.py may print FAILED for them; open the figshare link in a browser instead.
- The converted-site file starts on 2018-03-01, one month earlier than the 2018/04 in your Sheet1 (A4).

## Files in `data/`

- `MA_undrained_daily_WT_data.xlsx`: Daily mean WT (cm). 2011-01-01 to 2014-12-31, 1 d. WTD: Yes: cm; negative = below peat surface (positive = standing water)
- `MA_converted_daily_WT_data.xlsx`: Daily mean WT (cm). 2018-03-01 to 2019-05-31, 1 d. WTD: Yes: cm; negative = below peat surface

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A15`.
