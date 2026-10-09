#!/usr/bin/env python3
"""Download the open-access papers (and supplements) behind each dataset or site into literature/<folder>/paper/.

Usage (Python 3.8+, standard library only):
    python3 download_papers.py            # all papers
    python3 download_papers.py A3 C9      # only folders whose name starts with these IDs

PDFs are git-ignored because the repository is public; this script is how you get them locally.
For each paper the candidate links are tried in order and the first one that returns a real PDF is kept.
Closed-access papers have no candidates and are only listed. Nothing is ever deleted.
Some publishers (Wiley, ScienceDirect) block scripts; the script prints the link for those so you can
save the PDF from a browser instead.
"""
import os
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36"

# folder -> list of (file name, DOI, [candidate PDF urls]); an empty list means closed access
PAPERS = {
    "A1_Mendaram_Cobb2019": [
        ("CobbHarvey2019_WRR.pdf", "10.1029/2019WR025411", [
            "https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2019WR025411",
            "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2019WR025411"]),
        ("Cobb2017_PNAS.pdf", "10.1073/pnas.1701090114", [
            "https://europepmc.org/articles/PMC5495247?pdf=render",
            "https://www.pnas.org/doi/pdf/10.1073/pnas.1701090114"]),
    ],
    "A2_Mendaram_Hoyt2019": [
        ("Hoyt2019_GCB_preprint.pdf", "10.1111/gcb.14702", [
            "https://hal.science/hal-02333558/document",
            "https://dspace.mit.edu/bitstream/handle/1721.1/141006/Hoyt_et_al_GCB_Revised_Manuscript_with_Figures.pdf"]),
    ],
    "A3_Palangkaraya_Hirano2024": [
        ("Hirano2024_CommsEE.pdf", "10.1038/s43247-024-01387-7", [
            "https://www.nature.com/articles/s43247-024-01387-7.pdf"]),
    ],
    "A4_Palangkaraya_DailyGWL": [
        ("Hirano2014_GCB_accepted.pdf", "10.1111/gcb.12653", [
            "https://eprints.lib.hokudai.ac.jp/repo/huscap/all/65234/Final%20MS_GCB15-1.pdf"]),
        ("Hirano2012_GCB.pdf", "10.1111/j.1365-2486.2012.02793.x", []),
        # probable companion paper of DailyGWL.xlsx (same group, sites and years; bronze open access)
        ("Ohkubo2023_JHydrol.pdf", "10.1016/j.jhydrol.2023.129523", [
            "https://www.sciencedirect.com/science/article/pii/S0022169423004651/pdfft?isDTMRedir=true&download=true"]),
    ],
    "A5_FLUXNET-CH4_ID-Pag_Sakabe2018": [
        ("Sakabe2018_GCB.pdf", "10.1111/gcb.14410", [
            "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/gcb.14410"]),
    ],
    "A6_FLUXNET-CH4_MY-MLM_Tang2020": [
        ("Tang2020_GCB.pdf", "10.1111/gcb.15332", []),
    ],
    "A7_Kampar_Deshmukh2021": [
        # the open copy is the accepted manuscript as a Word file
        ("Deshmukh2021_NatGeo_accepted.docx", "10.1038/s41561-021-00785-2", [
            "https://figshare.com/ndownloader/files/28985250"]),
    ],
    "A8_Kampar_Deshmukh2023": [
        ("Deshmukh2023_Nature.pdf", "10.1038/s41586-023-05860-9", [
            "https://www.nature.com/articles/s41586-023-05860-9.pdf",
            "https://europepmc.org/articles/PMC10132972?pdf=render"]),
    ],
    "A9_Jambi_KubuRaya_Taufik2022": [
        ("Taufik2022_DataInBrief.pdf", "10.1016/j.dib.2022.107903", [
            "https://europepmc.org/articles/PMC8847808?pdf=render"]),
        ("Taufik2022_AFM.pdf", "10.1016/j.agrformet.2021.108738", []),
    ],
    "A11_SUSTAINPEAT_JovaniSancho2023": [
        ("JovaniSancho2023_GCB.pdf", "10.1111/gcb.16747", [
            "https://europepmc.org/articles/PMC10946781?pdf=render",
            "https://nora.nerc.ac.uk/id/eprint/535568/1/N535568JA.pdf",
            "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/gcb.16747"]),
    ],
    "A12_Sebungan_McCalmont2021": [
        ("McCalmont2021_GCB.pdf", "10.1111/gcb.15544", [
            "https://figshare.com/ndownloader/files/56809550",
            "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/gcb.15544"]),
    ],
    "A13-14_CIFOR_CentralKalimantan_Swails2019": [
        ("Hergoualch2017_Biogeochemistry.pdf", "10.1007/s10533-017-0363-4", [
            "https://link.springer.com/content/pdf/10.1007/s10533-017-0363-4.pdf"]),
        ("Swails2019_Biogeochemistry.pdf", "10.1007/s10533-018-0519-x", []),
    ],
    "B1_SiPALAGA_BRGM": [
        ("Mleczko2025_RSE.pdf", "10.1016/j.rse.2025.115009", [
            "https://www.sciencedirect.com/science/article/pii/S0034425725004134/pdfft?isDTMRedir=true&download=true"]),
    ],
    "C1_SouthSumatra_Hooijer2024": [
        ("Hooijer2024_SciRep.pdf", "10.1038/s41598-024-60462-3", [
            "https://www.nature.com/articles/s41598-024-60462-3.pdf"]),
        ("41598_2024_60462_MOESM1_ESM.pdf", "10.1038/s41598-024-60462-3", [
            "https://static-content.springer.com/esm/art%3A10.1038%2Fs41598-024-60462-3/MediaObjects/41598_2024_60462_MOESM1_ESM.pdf"]),
    ],
    "C3_PulauPadang_Ismail2021": [
        ("Ismail2021_HydrolRes.pdf", "10.2166/nh.2021.062", [
            "https://iwaponline.com/hr/article-pdf/52/6/1372/982018/nh0521372.pdf"]),
    ],
    "C5_EastKalimantan_Asyhari2024": [
        ("Asyhari2024_SciRep.pdf", "10.1038/s41598-024-62233-6", [
            "https://www.nature.com/articles/s41598-024-62233-6.pdf"]),
    ],
    "C6_Sarawak_Kiew2025": [
        ("Kiew2025_AFM_accepted.pdf", "10.1016/j.agrformet.2025.110956", [
            "https://dspace.ut.ee/bitstreams/faf14c63-3724-4fd8-80af-f127ba09c187/download"]),
    ],
    "C7_Sarawak_Aeries2023": [
        ("Aeries2023_ASET.pdf", "10.58915/aset.v2i2.331", [
            "https://ejournal.unimap.edu.my/index.php/aset/article/download/331/242"]),
    ],
    "C8-9_NorthSelangor_LoParish2022_Ledger2023": [
        ("LoParish2022_AART.pdf", "10.54026/aart/1029", [
            "https://www.corpuspublishers.com/assets/articles/aart-v3-22-1029.pdf"]),
        ("Ledger2023_FrontEnvSci.pdf", "10.3389/fenvs.2023.1182100", [
            "https://www.frontiersin.org/articles/10.3389/fenvs.2023.1182100/pdf",
            "https://nora.nerc.ac.uk/id/eprint/535603/1/Ledger%20et%20al.%202023_Front_Env_Sci_Malaysia%20Peat.pdf"]),
        ("Ledger2023_SupplementaryMaterial_Table1.DOCX", "10.3389/fenvs.2023.1182100", [
            "https://www.frontiersin.org/api/v4/articles/1182100/file/Table1.DOCX/1182100_supplementary-materials_tables_1_docx/1"]),
    ],
    "C10-11_TimelapseCamera_Evans2021": [
        ("Evans2021_FrontEnvSci.pdf", "10.3389/fenvs.2021.630752", [
            "https://www.frontiersin.org/articles/10.3389/fenvs.2021.630752/pdf"]),
    ],
    "C12_Badas_Lupascu2020": [
        ("Lupascu2020_GCB.pdf", "10.1111/gcb.15195", []),
    ],
    "D1_SEA_WTD_model_Hooijer2026": [
        ("Hooijer2026_SciRep.pdf", "10.1038/s41598-026-64641-2", [
            "https://www.nature.com/articles/s41598-026-64641-2.pdf"]),
    ],
    # ---- EXPANDED_2006-2026.xlsx (IDs continue SEA_peatland_WTD_datasets.xlsx)
    "A15_Maludam_Naman_Tang2020_Nishina2023": [
        ("Tang2020_GCB.pdf", "10.1111/gcb.15332", []),
        ("Nishina2023_STOTEN.pdf", "10.1016/j.scitotenv.2023.162062", []),
    ],
    "A16_Maludam_Tang2018": [
        ("Tang2018_GRL.pdf", "10.1029/2017gl076457", [
            "https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2017GL076457",
            "https://scholarworks.montana.edu/bitstreams/049b2df9-1eee-450f-a200-fb7ee6fae912/download"]),
    ],
    "A17_Jambi_Smallholdings_WarrenThomas2022": [
        ("WarrenThomas2022_JApplEcol.pdf", "10.1111/1365-2664.14135", [
            "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/1365-2664.14135",
            "https://eprints.whiterose.ac.uk/id/eprint/183680/7/Journal_of_Applied_Ecology_2022_Warren_Thomas_No_evidence_for_trade_offs_between_bird_diversity_yield_and_water.pdf",
            "https://pure.iiasa.ac.at/id/eprint/17865/1/Journal%20of%20Applied%20Ecology%20-%202022%20-%20Warren%E2%80%90Thomas%20-%20No%20evidence%20for%20trade%E2%80%90offs%20between%20bird%20diversity%20%20yield%20and%20water.pdf"]),
    ],
    "A18_CentralKalimantan_Swails2021": [
        ("Swails2021_FrontEnvironSci.pdf", "10.3389/fenvs.2021.617828", [
            "https://www.frontiersin.org/articles/10.3389/fenvs.2021.617828/pdf"]),
        ("Swails2021_SupplementaryMaterial_DataSheet1.docx", "10.3389/fenvs.2021.617828", [
            "https://public-pages-files-2025.frontiersin.org/articles/617828/file/Data_Sheet_1.docx/617828_supplementary-materials_datasheets_1_docx/1"]),
    ],
    "A19_Jambi_CIFOR_Comeau2016": [
        ("Comeau2016_Geoderma.pdf", "10.1016/j.geoderma.2016.01.016", []),
        # papers behind CIFOR DATA.00290 / 00330-00331 / 00316 (found from the dataset titles)
        ("Swails2023_Biogeochemistry.pdf", "10.1007/s10533-023-01070-7", [
            "https://link.springer.com/content/pdf/10.1007/s10533-023-01070-7.pdf",
            "https://nora.nerc.ac.uk/id/eprint/535883/1/N535883JA.pdf",
            "https://hal.science/hal-05180977/document"]),
        ("Swails2026_Geoderma.pdf", "10.1016/j.geoderma.2026.118030", [
            "https://www.sciencedirect.com/science/article/pii/S0016706126003587/pdf"]),
        ("Hergoualch2026_RSOS.pdf", "10.1098/rsos.252443", [
            "https://europepmc.org/articles/PMC13561043?pdf=render",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC13561043/pdf/rsos.252443.pdf"]),
    ],
    "A22_Badas_Canal_Somers": [
        ("Somers2023_JGRBiogeosciences.pdf", "10.1029/2022jg007194", [
            "https://hal.science/hal-04050057v1/file/JGR%20Biogeosciences%20-%202023%20-%20Somers%20-%20Processes%20Controlling%20Methane%20Emissions%20From%20a%20Tropical%20Peatland%20Drainage%20Canal.pdf",
            "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2022JG007194"]),
    ],
    "A21_NorthSelangor_Cooper2020": [
        ("Cooper2020_NatCommun.pdf", "10.1038/s41467-020-14298-w", [
            "https://europepmc.org/articles/PMC6972824?pdf=render",
            "https://www.nature.com/articles/s41467-020-14298-w.pdf",
            "https://researchonline.ljmu.ac.uk/id/eprint/12208/9/Greenhouse%20gas%20emissions%20resulting%20from%20conversion%20of%20peat%20swamp%20forest%20to%20oil%20palm%20plantation.pdf"]),
    ],
    # A23: Putra2021_HydrolProcess.pdf and Putra2023_MiresPeat.pdf are in C19_Sebangau_Putra2021/paper/
    "A34_Bengkalis_Kagawa2026": [
        ("Kagawa2026_Biogeosciences.pdf", "10.5194/bg-23-2119-2026", [
            "https://bg.copernicus.org/articles/23/2119/2026/bg-23-2119-2026.pdf"]),
    ],
    "B4_Palangkaraya_UF_Sulaiman2023": [
        ("Sulaiman2023_SciRep.pdf", "10.1038/s41598-023-27393-x", [
            "https://europepmc.org/articles/PMC9849340?pdf=render",
            "https://www.nature.com/articles/s41598-023-27393-x.pdf",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC9849340/pdf/41598_2023_Article_27393.pdf"]),
    ],
    # B5: Apers2022_JAMES.pdf (10.1029/2021ms002784) is in D9_PEATCLSM_Trop_Apers2022/paper/
    # B6: Hikouei2023_STOTEN.pdf (10.1016/j.scitotenv.2022.159701) is in D12_ML_GWL_Hikouei2023/paper/
    "B6_KFCP_ExMRP_Putra2018": [
        ("Putra2018_IOPEES.pdf", "10.1088/1755-1315/149/1/012027", [
            "https://iopscience.iop.org/article/10.1088/1755-1315/149/1/012027/pdf"]),
        ("Putra2019_IOPEES.pdf", "10.1088/1755-1315/284/1/012021", [
            "https://iopscience.iop.org/article/10.1088/1755-1315/284/1/012021/pdf"]),
    ],
    "B8_APRIL_Riau_Hooijer2012_Evans2019": [
        ("Hooijer2012_BG.pdf", "10.5194/bg-9-1053-2012", [
            "https://bg.copernicus.org/articles/9/1053/2012/bg-9-1053-2012.pdf"]),
        ("Evans2019_Geoderma.pdf", "10.1016/j.geoderma.2018.12.028", [
            "https://www.sciencedirect.com/science/article/pii/S0016706118315635/pdf",
            "http://nora.nerc.ac.uk/id/eprint/522239/1/N522239JA.pdf"]),
    ],
    "B9_SESAME_Pratama2020_Irfan": [
        ("Pratama2020_IOPMSE.pdf", "10.1088/1757-899x/796/1/012037", [
            "https://iopscience.iop.org/article/10.1088/1757-899x/796/1/012037/pdf"]),
        ("Irfan2020_JPhysConfSer.pdf", "10.1088/1742-6596/1568/1/012028", [
            "https://iopscience.iop.org/article/10.1088/1742-6596/1568/1/012028/pdf"]),
        ("Irfan2023_JGSE.pdf", "10.26599/jgse.2023.9280008", [
            "https://www.sciopen.com/article_pdf/1640541329525784578.pdf"]),
        ("Irfan2026_AIPConfProc.pdf", "10.1063/5.0337576", []),
    ],
    "B10_KuanKreng_Khampeera2018": [
        ("Khampeera2018_WalailakJSciTech.pdf", "10.48048/wjst.2018.2723", []),
    ],
    "B11_UMinhThuong_Thai2024": [
        ("Thai2024_Sustainability.pdf", "10.3390/su16020620", [
            "https://www.mdpi.com/2071-1050/16/2/620/pdf?version=1704905467",
            "https://repo.uni-hannover.de/bitstreams/8ff66b9e-3df8-486d-9b51-43d7303d5e7e/download"]),
    ],
    # B13: Apers2022_JAMES.pdf (10.1029/2021ms002784) is in D9_PEATCLSM_Trop_Apers2022/paper/
    "B13_SIPALAGA_Apers2022": [
        ("Putra2025_IJEMS.pdf", "10.26554/ijems.2025.9.2.46-55", []),
        ("Hein2022_RegEnvChange.pdf", "10.1007/s10113-022-01979-z", [
            "https://link.springer.com/content/pdf/10.1007/s10113-022-01979-z.pdf"]),
    ],
    "C15_Palangkaraya_Jauhiainen2008": [
        ("Jauhiainen2008_Ecology.pdf", "10.1890/07-2038.1", []),
    ],
    "C16_BlockC_Sebangau_Wosten2006": [
        ("Wosten2006_IJWRD.pdf", "10.1080/07900620500405973", []),
        ("Wosten2008_Catena.pdf", "10.1016/j.catena.2007.07.010", []),
        ("Jaenicke2010_MASGC.pdf", "10.1007/s11027-010-9214-5", [
            "https://link.springer.com/content/pdf/10.1007/s11027-010-9214-5.pdf"]),
        ("Jaenicke2011_JEM.pdf", "10.1016/j.jenvman.2010.09.029", []),
        ("Ritzema2014_Catena.pdf", "10.1016/j.catena.2013.10.009", []),
    ],
    "C17_Sebangau_Kononen2016_Lampela2017": [
        ("Kononen2016_WetlEcolManag.pdf", "10.1007/s11273-016-9498-7", []),
        ("Lampela2017_ForEcolManag.pdf", "10.1016/j.foreco.2016.12.004", []),
    ],
    "C18_Sebangau_AirHitam_Taufik2019": [
        ("Taufik2019_Geoderma.pdf", "10.1016/j.geoderma.2019.04.001", [
            "https://www.sciencedirect.com/science/article/pii/S0016706118313338/pdf",
            "https://edepot.wur.nl/475945"]),
    ],
    "C19_Sebangau_Putra2021": [
        ("Putra2021_HydrolProcess.pdf", "10.1002/hyp.14174", [
            "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/hyp.14174"]),
        ("Putra2023_MiresPeat.pdf", "10.19189/map.2022.omb.sta.2407", [
            "https://www.mires-and-peat.net/article/128776.pdf",
            "https://eprints.whiterose.ac.uk/197355/1/map_29_03.pdf"]),
    ],
    "C20_TumbangNusa_BudiSantosa2020": [
        ("Budi2020_JurnalGalam.pdf", "10.20886/glm.2020.1.1.27-40", [
            "https://ejournal.forda-mof.org/ejournal-litbang/index.php/GLM/article/download/6008/5107"]),
    ],
    "C21_Jabiren_Firmansyah2020": [
        ("Firmansyah2020_Agritech.pdf", "10.30595/agritech.v22i2.8000", [
            "http://jurnalnasional.ump.ac.id/index.php/AGRITECH/article/download/8000/3669"]),
    ],
    "C22_TimelapseCamera_Sulaeman2022": [
        ("Sulaeman2022_IOPEES.pdf", "10.1088/1755-1315/1025/1/012011", [
            "https://iopscience.iop.org/article/10.1088/1755-1315/1025/1/012011/pdf",
            "https://nora.nerc.ac.uk/id/eprint/536760/1/N536760JA.pdf"]),
    ],
    "C23_CentralKalimantan_Yulianti2024": [
        ("Yulianti2024_IOPEES.pdf", "10.1088/1755-1315/1421/1/012005", [
            "https://nora.nerc.ac.uk/id/eprint/538639/1/N538639JA.pdf",
            "https://iopscience.iop.org/article/10.1088/1755-1315/1421/1/012005/pdf"]),
    ],
    "C24_CentralKalimantan_Treby2026": [
        ("Treby2026_Pedosphere.pdf", "10.1016/j.pedsph.2026.02.009", []),
        ("Treby2026_SSRN.pdf", "10.2139/ssrn.7163970", []),
    ],
    "C25_ExMRP_CanalBlocking_Suwito2022": [
        ("Suwito2022_IOPEES.pdf", "10.1088/1755-1315/1018/1/012027", [
            "https://iopscience.iop.org/article/10.1088/1755-1315/1018/1/012027/pdf"]),
    ],
    "C26_Palangkaraya_Itoh2017": [
        ("Itoh2017_STOTEN.pdf", "10.1016/j.scitotenv.2017.07.132", [
            "https://ars.els-cdn.com/content/image/1-s2.0-S0048969717318351-fx1_lrg.jpg",
            "https://repository.kulib.kyoto-u.ac.jp/bitstreams/ff6e321e-d714-4bbc-9a1b-bef9c9eddfb4/download"]),
    ],
    "C27_Kampar_Suryatmojo2019": [
        ("Suryatmojo2019_IOPEES.pdf", "10.1088/1755-1315/361/1/012034", [
            "https://iopscience.iop.org/article/10.1088/1755-1315/361/1/012034/pdf"]),
    ],
    "C28_Siak_Maryani2020": [
        ("Maryani2020_IOPEES.pdf", "10.1088/1755-1315/533/1/012012", [
            "https://iopscience.iop.org/article/10.1088/1755-1315/533/1/012012/pdf"]),
    ],
    "C29_Siak_Basuki2021": [
        ("Basuki2021_IOPEES.pdf", "10.1088/1755-1315/648/1/012029", [
            "https://iopscience.iop.org/article/10.1088/1755-1315/648/1/012029/pdf"]),
    ],
    "C30_Siak_Gasib_Lutfi2021": [
        ("Wasilul2021_IOPEES.pdf", "10.1088/1755-1315/756/1/012028", [
            "https://iopscience.iop.org/article/10.1088/1755-1315/756/1/012028/pdf"]),
    ],
    "C31_Siak_CanalBlocking_Safitri2024": [
        ("Safitri2024_IOPEES.pdf", "10.1088/1755-1315/1315/1/012058", [
            "https://iopscience.iop.org/article/10.1088/1755-1315/1315/1/012058/pdf"]),
    ],
    "C32_SungaiTohor_Silviana2020_Malik2022": [
        ("Silviana2020_IOPMSE.pdf", "10.1088/1757-899x/796/1/012041", [
            "https://iopscience.iop.org/article/10.1088/1757-899X/796/1/012041/pdf"]),
        ("Malik2022_IOPEES.pdf", "10.1088/1755-1315/1041/1/012047", [
            "https://iopscience.iop.org/article/10.1088/1755-1315/1041/1/012047/pdf"]),
    ],
    "C33_Riau_Rewetting_Lestari2022": [
        ("Lestari2022_Forests.pdf", "10.3390/f13040505", [
            "https://www.mdpi.com/1999-4907/13/4/505/pdf?version=1648188927"]),
    ],
    "C34_Kampar_Nardi2021": [
        ("Nardi2021_JPSL.pdf", "10.29244/jpsl.11.3.442-452", [
            "https://journal.ipb.ac.id/index.php/jpsl/article/download/37386/22586"]),
    ],
    "C35_Bengkalis_Sutikno2026": [
        ("Sutikno2026_JDMLM.pdf", "10.15243/jdmlm.2026.131.9163", [
            "https://jdmlm.ub.ac.id/index.php/jdmlm/article/download/17389/1856"]),
    ],
    "C36_Riau_Acacia_Jauhiainen2012": [
        ("Jauhiainen2012_BG.pdf", "10.5194/bg-9-617-2012", [
            "https://figshare.com/articles/journal_contribution/Carbon_dioxide_emissions_from_an_Acacia_plantation_on_peatland_in_Sumatra_Indonesia/10108496",
            "https://bg.copernicus.org/articles/9/617/2012/bg-9-617-2012.pdf"]),
    ],
    "C37_Kampar_Deshmukh2020": [
        ("Deshmukh2020_GCB.pdf", "10.1111/gcb.15019", [
            "https://europepmc.org/articles/PMC7155032?pdf=render",
            "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/gcb.15019",
            "http://nora.nerc.ac.uk/id/eprint/527284/1/N527284JA.pdf"]),
    ],
    "C38_Riau_Coconut_Fawzi2024": [
        ("Fawzi2024_Heliyon.pdf", "10.1016/j.heliyon.2024.e26661", [
            "https://europepmc.org/articles/PMC10912239?pdf=render",
            "https://www.cell.com/heliyon/pdf/S2405-8440(24)02692-6.pdf",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC10912239/pdf/main.pdf"]),
    ],
    # C39: Comeau2016_Geoderma.pdf (10.1016/j.geoderma.2016.01.016) is in A19_Jambi_CIFOR_Comeau2016/paper/
    "C39_Sumatra_Plantations_Dariah2013": [
        ("Dariah2013_MASGC.pdf", "10.1007/s11027-013-9515-6", []),
        ("Husnain2014_MASGC.pdf", "10.1007/s11027-014-9550-y", []),
    ],
    "C40_Rubber_Wakhid2017": [
        ("Wakhid2017_STOTEN.pdf", "10.1016/j.scitotenv.2017.01.035", [
            "https://ars.els-cdn.com/content/image/1-s2.0-S0048969717300360-fx1_lrg.jpg",
            "https://eprints.lib.hokudai.ac.jp/repo/huscap/all/72327/RevisedMS_Jabiren2.pdf"]),
    ],
    "C41_TanjungJabung_Khasanah2019": [
        ("Khasanah2019_MASGC.pdf", "10.1007/s11027-018-9803-2", [
            "https://europepmc.org/articles/PMC6320748?pdf=render",
            "https://link.springer.com/content/pdf/10.1007%2Fs11027-018-9803-2.pdf"]),
    ],
    "C42_SouthSumatra_Khakim2022": [
        ("Khakim2022_GES.pdf", "10.24057/2071-9388-2021-137", [
            "https://ges.rgo.ru/jour/article/download/2495/641"]),
        ("Maryani2021_IOPEES.pdf", "10.1088/1755-1315/810/1/012023", [
            "https://iopscience.iop.org/article/10.1088/1755-1315/810/1/012023/pdf"]),
    ],
    "C43_WestKalimantan_Astiani2018": [
        ("Astiani2018_Biodiversitas.pdf", "10.13057/biodiv/d190221", []),
        ("Herawati2018_MATEC.pdf", "10.1051/matecconf/201819503016", [
            "https://www.matec-conferences.org/articles/matecconf/pdf/2018/54/matecconf_icrmce2018_03016.pdf",
            "https://www.matec-conferences.org/10.1051/matecconf/201819503016/pdf"]),
        ("Nusantara2023_JIlmuLingkungan.pdf", "10.14710/jil.21.4.781-788", [
            "https://ejournal.undip.ac.id/index.php/ilmulingkungan/article/download/48032/pdf"]),
        ("Nahda2025_BIOWebConf.pdf", "10.1051/bioconf/202516703013", [
            "https://www.bio-conferences.org/articles/bioconf/pdf/2025/18/bioconf_icosia2024_03013.pdf",
            "https://www.bio-conferences.org/10.1051/bioconf/202516703013/pdf"]),
    ],
    "C44_WestKalimantan_Novita2024": [
        ("Novita2024_STOTEN.pdf", "10.1016/j.scitotenv.2024.175829", []),
    ],
    "C45_SouthKalimantan_Wakhid2021": [
        ("Wakhid2021_MiresPeat.pdf", "10.19189/map.2021.omb.sta.2159", []),
    ],
    "C46_WestAceh_Handayani2010": [
        # OpenAlex's PDF link for this DOI (article/download/116/115) serves a different paper (Purwantono et al. 2011)
        ("Handayani2010_JTropSoils.pdf", "10.5400/jts.2010.15.3.255", []),
    ],
    "C47_Badas_Suhip2024": [
        ("Suhip2024_MiresPeat.pdf", "10.19189/map.2023.cm.sc.2332104", [
            "https://www.mires-and-peat.net/article/128750.pdf",
            "https://www.dora.lib4ri.ch/eawag/dload/eawag:33794/PDF/view"]),
    ],
    "C48_Damit_Hoyt2019": [
        ("Hoyt2019_GCB.pdf", "10.1111/gcb.14702", [
            "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/gcb.14702"]),
    ],
    "C49_Maludam_Busman2023": [
        ("Busman2023_STOTEN.pdf", "10.1016/j.scitotenv.2022.159973", []),
    ],
    "C50_Sarawak_Imran2022": [
        ("Imran2022_EnvironResCommun.pdf", "10.1088/2515-7620/ac6295", [
            "https://iopscience.iop.org/article/10.1088/2515-7620/ac6295/pdf"]),
    ],
    "C51_Sarawak_Wong2018_Kiew2020": [
        ("Wong2018_AFM.pdf", "10.1016/j.agrformet.2018.03.025", []),
        ("Kiew2020_AFM.pdf", "10.1016/j.agrformet.2020.108189", []),
        ("Ishikura2018_AGEE.pdf", "10.1016/j.agee.2017.11.025", [
            "https://www.sciencedirect.com/science/article/pii/S0167880917305224",
            "https://eprints.lib.hokudai.ac.jp/repo/huscap/all/76746/Manuscript_accepted%20supplementary_materials%20.pdf"]),
        ("Ishikura2019_Ecosystems.pdf", "10.1007/s10021-019-00376-8", []),
        ("Sangok2017_STOTEN.pdf", "10.1016/j.scitotenv.2017.02.165", []),
    ],
    "C52_Sarawak_Cook2018": [
        ("Cook2018_BG_supplement.pdf", "10.5194/bg-15-7435-2018", [
            "https://bg.copernicus.org/articles/15/7435/2018/bg-15-7435-2018-supplement.pdf"]),
        ("Cook2018_BG.pdf", "10.5194/bg-15-7435-2018", [
            "https://bg.copernicus.org/articles/15/7435/2018/bg-15-7435-2018.pdf",
            "http://eprints.gla.ac.uk/175119/7/175119.pdf",
            "http://nora.nerc.ac.uk/id/eprint/522050/1/N522050JA.pdf",
            "https://oro.open.ac.uk/58542/1/58542.pdf",
            "https://wrap.warwick.ac.uk/120273/1/WRAP-fluvial-organic-carbon-fluxes-oil-palm-plantations-tropical-peatland-2018.pdf"]),
    ],
    "C53_Bintulu_Basri2024": [
        ("Basri2024_SSRN.pdf", "10.2139/ssrn.4767267", []),
    ],
    "C54_Malaysia_Azizan2021": [
        ("Azizan2021_Water.pdf", "10.3390/w13233372", [
            "https://www.mdpi.com/2073-4441/13/23/3372/pdf?version=1638347754"]),
    ],
    "C55_Johor_Katimon2012": [
        ("Katimon2012_JTeknologi.pdf", "10.11113/jt.v38.487", []),
        ("Shamsuddin2021_JWARP.pdf", "10.4236/jwarp.2021.1312052", [
            "http://www.scirp.org/journal/PaperDownload.aspx?paperID=113808"]),
    ],
    "C56_Bacho_Nagano2013": [
        ("Nagano2013_MiresPeat.pdf", "10.19189/001c.128481", [
            "https://www.mires-and-peat.net/article/128481.pdf"]),
    ],
    "C57_Leyte_Decena2021": [
        ("Decena2021_MiresPeat.pdf", "10.19189/map.2021.bg.sta.2287", []),
    ],
    # C58: Apers2022_JAMES.pdf (10.1029/2021ms002784) is in D9_PEATCLSM_Trop_Apers2022/paper/
    # C59: Apers2022_JAMES.pdf (10.1029/2021ms002784) is in D9_PEATCLSM_Trop_Apers2022/paper/
    "C60_CentralKalimantan_Cassiophea2025": [
        ("Cassiophea2025_IOPEES.pdf", "10.1088/1755-1315/1542/1/012023", [
            "https://iopscience.iop.org/article/10.1088/1755-1315/1542/1/012023/pdf"]),
    ],
    "C61_KFCP_Hikouei2025": [
        # closed; the University of the Sunshine Coast repository lists it (research.usc.edu.au, output 991101946302621)
        ("Hikouei2025_GroundwSustDev.pdf", "10.1016/j.gsd.2025.101413", []),
    ],
    # C62: no DOI; read the article page https://ejournal.brin.go.id/ijreses/article/view/13780
    "C63_SungaiTohor_Sutikno2019": [
        ("Sutikno2019_MATEC.pdf", "10.1051/matecconf/201927606003", [
            "https://www.matec-conferences.org/10.1051/matecconf/201927606003/pdf"]),
    ],
    "C64_Jambi_Putra2024": [
        ("Putra2024_JTropSilvic.pdf", "10.29244/j-siltrop.15.01.65-69", [
            "https://journal.ipb.ac.id/index.php/jsilvik/article/download/55265/28060"]),
    ],
    "C65_CentralKalimantan_Sekarano2026": [
        # SSRN preprint; SSRN serves PDFs only in a browser: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7439436
        ("Sekarano2026_SSRN.pdf", "10.2139/ssrn.7439436", []),
    ],
    "D4_SEA_GWL_monthly_Hirano2025": [
        ("Hirano2025_AGUAdvances.pdf", "10.1029/2025AV001861", [
            "https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2025AV001861",
            "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2025AV001861"]),
    ],
    "D9_PEATCLSM_Trop_Apers2022": [
        ("Apers2022_JAMES.pdf", "10.1029/2021ms002784", [
            "https://europepmc.org/articles/PMC9285420?pdf=render",
            "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2021MS002784",
            "http://nora.nerc.ac.uk/id/eprint/532323/1/N532323JA.pdf",
            "https://lirias.kuleuven.be/retrieve/cf1f6b55-e91e-4b03-8cc3-cdff83f985e5"]),
    ],
    "D10_OPTRAM_KoupaeiAbyazani2024": [
        ("KoupaeiAbyazani2024_JGRBiogeoscience.pdf", "10.1029/2024jg008116", [
            "https://hal.science/hal-05182131/document",
            "http://agritrop.cirad.fr/609820/1/Koupaei%E2%80%90Abyazani%20et%20al%2024%20Tropical%20Peatland%20Water%20Table%20Estimations%20From%20Space%281%29.pdf",
            "https://lirias.kuleuven.be/retrieve/25bcdfa8-ae96-4248-b84f-fa7c700c6bc0",
            "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2024jg008116"]),
    ],
    "D11_CanalWTD_Vernimmen2020_Dadap2021": [
        ("Vernimmen2020_Water.pdf", "10.3390/w12051486", [
            "https://www.mdpi.com/2073-4441/12/5/1486/pdf?version=1590152132"]),
        ("Dadap2021_AGUAdvances.pdf", "10.1029/2020av000321", [
            "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2020AV000321"]),
    ],
    "D12_ML_GWL_Hikouei2023": [
        ("Hikouei2023_STOTEN.pdf", "10.1016/j.scitotenv.2022.159701", []),
    ],
    "D14_CIFOR_WTD_Compilation_Couwenberg": [
        ("Couwenberg2010_GCB.pdf", "10.1111/j.1365-2486.2009.02016.x", []),
        ("Couwenberg2013_MiresPeat.pdf", "10.19189/001c.128487", [
            "https://www.mires-and-peat.net/article/128487.pdf"]),
        ("Hergoualch2014_MASGC.pdf", "10.1007/s11027-013-9511-x", []),
        ("Carlson2015_ERL.pdf", "10.1088/1748-9326/10/7/074006", [
            "https://iopscience.iop.org/article/10.1088/1748-9326/10/7/074006/pdf"]),
        ("Prananto2020_GCB.pdf", "10.1111/gcb.15147", []),
        ("Swails2024_Biogeochemistry.pdf", "10.1007/s10533-023-01110-2", [
            "https://link.springer.com/content/pdf/10.1007/s10533-023-01110-2.pdf"]),
    ],
}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/pdf,*/*"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def save_pdf(name, doi, urls, paper_dir):
    dest = os.path.join(paper_dir, name)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        print("   exists:", os.path.relpath(dest, HERE))
        return True
    if not urls:
        print("   closed access, not downloaded: https://doi.org/%s" % doi)
        return False
    for url in urls:
        try:
            body = fetch(url)
        except Exception as e:
            print("   %s -> %s" % (url, e))
            time.sleep(1)
            continue
        if name.lower().endswith(".pdf"):
            if body[:2] == b"PK":
                # figshare returns a zip of the item; keep the first PDF inside it
                import io
                import zipfile
                z = zipfile.ZipFile(io.BytesIO(body))
                pdfs = [n for n in z.namelist() if n.lower().endswith(".pdf")]
                body = z.read(pdfs[0]) if pdfs else b""
            if body[:5] != b"%PDF-":
                print("   %s -> not a PDF (bot check or landing page)" % url)
                continue
        elif not body or body.lstrip()[:1] == b"<":
            print("   %s -> got a web page instead of the file" % url)
            continue
        os.makedirs(paper_dir, exist_ok=True)
        with open(dest, "wb") as fh:
            fh.write(body)
        print("   ok: %s (%d bytes) from %s" % (os.path.relpath(dest, HERE), len(body), url))
        return True
    print("   FAILED: save it from a browser into %s: https://doi.org/%s" % (os.path.relpath(paper_dir, HERE), doi))
    return False


def main(ids):
    for folder, papers in PAPERS.items():
        tag = folder.split("_")[0]  # e.g. "A3", "C8-9"
        if ids and not any(i == tag or tag.startswith(i + "-") for i in ids):
            continue
        print(folder)
        for name, doi, urls in papers:
            save_pdf(name, doi, urls, os.path.join(HERE, folder, "paper"))


if __name__ == "__main__":
    main(sys.argv[1:])
