# B1: SiPALAGA water-level network (BRGM), Indonesia

**Status:** No public data

**Data source:** [SiPALAGA portal](https://sipalaga.brgm.go.id); licence Portal / request

**Paper:** Mleczko et al. 2025, Remote Sensing of Environment (use case), https://doi.org/10.1016/j.rse.2025.115009 (Hybrid OA (CC-BY); ScienceDirect blocks scripts)

> Data availability: Not read (ScienceDirect blocked).

**How the paper used the data:** Mleczko et al. compare Sentinel-1 SBAS InSAR ground displacement with GWL and peat-surface elevation from local monitoring networks in Central Kalimantan (2017-2022) and show the InSAR results depend on the hydrological state (from the abstract).

- sipalaga.brgm.go.id returned HTTP 403 from its own server to the cloud request; try it from your browser.
- A9 is a published subset: 8 BRG stations with daily data for 2018-2019.

Full details: `../DATA_SUMMARY.md`. Papers go in `paper/` (git-ignored); run `../download_papers.py B1`.
