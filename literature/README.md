# literature/

Public water-table-depth (WTD) data for Southeast Asian peatlands, downloaded from the datasets listed in
`INDEX.md`, with one folder per dataset.

- **`DATA_SUMMARY.md` / `DATA_SUMMARY.xlsx`**: what each file contains (site, coordinates, period, time step,
  WTD range and sign), how the original paper used the data, each paper's data-availability statement, and
  corrections to `INDEX.md`. Start here.
- **`EXPANDED_2006-2026.md` / `.xlsx`**: sites and datasets found when the search was widened to 2006-2026 (not
  downloaded), including sites from the last 10 years that `INDEX.md` missed and the 87 SE Asian water-level sites
  compiled by Apers et al. 2022. Regenerate with `build_expanded.py`.
- **`<ID>_<site>_<paper>/data/`**: the downloaded files, unchanged (zip archives are kept as zips).
- **`<ID>_<site>_<paper>/README.md`**: the same information for that dataset.
- **`<ID>_<site>_<paper>/paper/`**: papers and supplementary PDFs. Git-ignored, because the repository is public.

Scripts (Python 3.8+):

| Script | What it does | Needs |
|---|---|---|
| `download_data.py [IDs]` | Re-downloads all public data; skips files already present | standard library |
| `download_papers.py [IDs]` | Downloads open-access papers and supplements into `paper/`; prints links that publishers block | standard library |
| `build_summary.py` | Regenerates `DATA_SUMMARY.*` and the folder READMEs from the facts listed inside it | `openpyxl` |

Example: `python3 download_papers.py A3 C9` downloads only those two datasets' papers.
