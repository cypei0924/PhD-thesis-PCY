#!/usr/bin/env python3
"""Download the open-access papers (and supplements) behind each dataset into literature/<folder>/paper/.

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
