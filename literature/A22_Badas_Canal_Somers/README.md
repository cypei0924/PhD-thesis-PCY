# A22: Badas drainage canal: culvert water levels and canal/porewater chemistry, Brunei

**Status:** Downloaded

**Data source:** [HydroShare](https://doi.org/10.4211/hs.3953b24e0238467980a226c72cfc360e); licence CC BY 4.0

**Paper:** Somers et al. 2023, JGR Biogeosciences 128, https://doi.org/10.1029/2022JG007194 (Open access, but the publisher blocked the download; abstract only)

> Data availability: Not read; the HydroShare resource says it 'accompanies a manuscript submission' and the MATLAB README links it to this study.

**How the paper used the data:** An isotope-enabled model of methane and DIC transport, degassing and oxidation along a 5 km canal across a disturbed peat dome, fitted to porewater and canal-water concentrations and d13C (Jan and Aug 2020): about 70 % of the methane entering the canal is oxidised in it. The culvert logger levels were used to calculate streamflow.

- The loggers measure canal water level at two culverts (CUL-1, CUL-2), not the peat water table.
- HydroShare point coverage: 4.5619 N, 114.3367 E; period 2020-01-01 to 2020-08-31 (the logger files run to Dec 2020).
- The Dec2020 file names are swapped: 'Culvert1_..._Dec2020' has Location CUL-2 in its header and 'Culvert2_..._Dec2020' has CUL-1.
- Subfolders were flattened into file names (Compensated_Levelogger_files_*, Matlab_Model_Code_*).

## Files in `data/`

- `Compensated_Levelogger_files_Cul_1-May_19_2020-Compensated.csv`: Barometrically compensated level (m) and temperature. 2020-01-24 13:00 to 2020-05-19 12:30, 15 min. 
- `Compensated_Levelogger_files_Cul_2-May_19_2020-Compensated.csv`: As above. 2020-01-24 13:00 to 2020-05-19 13:00, 15 min. 
- `Compensated_Levelogger_files_Culvert1_Compensated_June2020.csv`: As above. 2020-05-28 15:15 to 2020-06-10 14:00, 15 min. 
- `Compensated_Levelogger_files_Culvert2_compensated_June2020.csv`: As above. 2020-05-28 15:15 to 2020-06-10 14:00, 15 min. 
- `Compensated_Levelogger_files_Culvert1_Compensated_Dec2020.csv`: As above. 2020-06-10 15:15 to 2020-12-16 14:45, 15 min. 
- `Compensated_Levelogger_files_Culvert2_compensated_Dec2020.csv`: As above. 2020-06-10 15:15 to 2020-12-16 14:45, 15 min. 
- `*.xle (6 files)`: Solinst raw logger files matching the CSVs. 
- `13C-DIC_CH4-Jan_2020.xlsx, 13C-DIC_CH4_Badas_Aug_2020.xlsx, Major_ions_Badas_Jan_2020_corrected.xlsx`: Dissolved CH4, CO2, d13C; major ions. 2020-01 to 2020-08, . 
- `Matlab_Model_Code_* (25 files)`: Model code and field-data copies. 

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py A22`.
