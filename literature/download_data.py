#!/usr/bin/env python3
"""Download the public WTD datasets listed in INDEX.md and EXPANDED_2006-2026.xlsx into literature/<folder>/data/.

Usage (from anywhere, Python 3.8+, standard library only):
    python3 download_data.py            # everything
    python3 download_data.py A3 D1      # only folders whose name starts with these IDs

Files that already exist with the expected size are skipped, so re-running is safe.
Nothing is ever deleted. Files over 100 MB go to data/_large/ (git-ignored); files over 5 GB are listed, not fetched.
Datasets that need a login (FLUXNET-CH4) or are embargoed are listed but not fetched.
"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36"
LARGE = 100 * 1024 * 1024
HUGE = 5 * 1024 ** 3

# folder -> list of sources; each source is resolved to (filename, url, size or None)
MANIFEST = {
    "A1_Mendaram_Cobb2019": [
        ("pangaea", "10.1594/PANGAEA.908201"),  # water level, piezometer mdm trail 6
        ("pangaea", "10.1594/PANGAEA.908206"),  # water level, mdm trail 7
        ("pangaea", "10.1594/PANGAEA.908207"),  # water level, mdm trail 8
        ("pangaea", "10.1594/PANGAEA.908208"),  # water level, mdm trail 10
        ("pangaea", "10.1594/PANGAEA.908209"),  # hydraulic conductivity
        ("pangaea", "10.1594/PANGAEA.908210"),  # specific yield
        ("pangaea", "10.1594/PANGAEA.908211"),  # flowtube geometry
        ("pangaea", "10.1594/PANGAEA.908214"),  # throughfall time series
        ("url", "README_Brunei_peat_swamp_data.pdf", "https://store.pangaea.de/Publications/Cobb-Harvey_2019/README.pdf"),
    ],
    "A2_Mendaram_Hoyt2019": [("zenodo", "3245335")],
    "A3_Palangkaraya_Hirano2024": [
        ("url", "CO2 flux data.zip", "https://figshare.com/ndownloader/files/41809308?private_link=6aefe20137486d0a6f62"),
    ],
    "A4_Palangkaraya_DailyGWL": [("figshare", "22321129")],
    "A5_FLUXNET-CH4_ID-Pag_Sakabe2018": [("manual", "FLUXNET-CH4 requires a fluxnet.org login; see README.md")],
    "A6_FLUXNET-CH4_MY-MLM_Tang2020": [("manual", "FLUXNET-CH4 requires a fluxnet.org login; see README.md")],
    "A7_Kampar_Deshmukh2021": [("zenodo", "4835696")],
    # 7500659 is the record linked in the index; the published paper cites 7728463 (v.03, revised ED Fig. 2)
    "A8_Kampar_Deshmukh2023": [("zenodo", "7500659"), ("zenodo", "7728463", "zenodo_7728463_v03")],
    # ScienceDirect blocks scripts; the same attachment is served by Europe PMC
    "A9_Jambi_KubuRaya_Taufik2022": [("epmc_supp", "PMC8847808", "mmc1.xlsx")],
    "A11_SUSTAINPEAT_JovaniSancho2023": [("dspace7", "https://repository.nottingham.ac.uk/server/api", "e1aaeadc-7df2-4cdb-8e78-a0139a3a6a9d")],
    "A12_Sebungan_McCalmont2021": [("manual", "Exeter ORE doi:10.24378/exe.3143 is embargoed (third-party permission required)")],
    "A13-14_CIFOR_CentralKalimantan_Swails2019": [
        ("dataverse", "https://data.cifor.org", "doi:10.17528/CIFOR/DATA.00061"),
    ],
    # the index listed C5 as figure-only, but the paper's Data availability points to this Zenodo record
    "C5_EastKalimantan_Asyhari2024": [("zenodo", "10427000")],
    # Ledger et al. 2023 supplementary data (Frontiers, CC-BY): manual + logger water table, site coordinates
    "C8-9_NorthSelangor_LoParish2022_Ledger2023": [
        ("url", "Ledger2023_DataSheet1.XLSX", "https://www.frontiersin.org/api/v4/articles/1182100/file/DataSheet1.XLSX/1182100_supplementary-materials_datasheets_1_xlsx/1"),
        ("url", "Ledger2023_DataSheet2.XLSX", "https://www.frontiersin.org/api/v4/articles/1182100/file/DataSheet2.XLSX/1182100_supplementary-materials_datasheets_2_xlsx/1"),
    ],
    "D1_SEA_WTD_model_Hooijer2026": [("mendeley", "69mbg22fxf")],
    # ---- EXPANDED_2006-2026.xlsx (IDs continue SEA_peatland_WTD_datasets.xlsx)
    "A15_Maludam_Naman_Tang2020_Nishina2023": [("figshare", "25299358")],
    "A16_Maludam_Tang2018": [("zenodo", "1161966")],
    "A17_Jambi_Smallholdings_WarrenThomas2022": [("dryad", "10.5061/dryad.rr4xgxd9v")],
    # data.cifor.org refused connections from the cloud workspace; run this locally
    "A18_CentralKalimantan_Swails2021": [("dataverse", "https://data.cifor.org", "doi:10.17528/CIFOR/DATA.00201")],
    "A19_Jambi_CIFOR_Comeau2016": [
        ("dataverse", "https://data.cifor.org", "doi:10.17528/CIFOR/DATA.00330"),
        ("dataverse", "https://data.cifor.org", "doi:10.17528/CIFOR/DATA.00331"),
        ("dataverse", "https://data.cifor.org", "doi:10.17528/CIFOR/DATA.00290"),
        ("dataverse", "https://data.cifor.org", "doi:10.17528/CIFOR/DATA.00316"),
    ],
    "A20_CentralKalimantan_SWAMP_CIFOR": [
        ("dataverse", "https://data.cifor.org", "doi:10.17528/CIFOR/DATA.ZORCAF"),
        ("dataverse", "https://data.cifor.org", "doi:10.17528/CIFOR/DATA.F5DM1Y"),
    ],
    "A21_NorthSelangor_Cooper2020": [
        ("url", "Cooper2020_SupplementaryData1.xlsx", "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-020-14298-w/MediaObjects/41467_2020_14298_MOESM2_ESM.xlsx"),
        ("url", "Cooper2020_SourceData.xlsx", "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-020-14298-w/MediaObjects/41467_2020_14298_MOESM4_ESM.xlsx"),
    ],
    "A22_Badas_Canal_Somers": [("hydroshare", "3953b24e0238467980a226c72cfc360e")],
    # only the SE Asia files (SEA) and the documentation; the daily SEA image files are 7.6-7.8 GB each
    "D9_PEATCLSM_Trop_Apers2022": [("zenodo", "6011689", "", r"SEA|_doc")],
    "D13_Kalimantan_FireRisk_Mahdiyasa": [("zenodo", "17907349")],
    "D14_CIFOR_WTD_Compilation_Couwenberg": [("dataverse", "https://data.cifor.org", "doi:10.17528/CIFOR/DATA.00291")],
    # ---- rows added in SEA_peatland_WTD_datasets.xlsx after EXPANDED (your A23-A33); only A23 has new public data
    "A23_Sebangau_Putra2021": [("eprints", "https://archive.researchdata.leeds.ac.uk/832/")],
    # ---- found in the October 2026 search (new rows for your table)
    "A34_Bengkalis_Kagawa2026": [("zenodo", "19159832")],
    # figshare answers scripts with a bot check; if this fails, save MonthlyData250816.xlsx from the browser
    "D4_SEA_GWL_monthly_Hirano2025": [("figshare", "30761072")],
    "D11_CanalWTD_Vernimmen2020_Dadap2021": [("mendeley", "7nnf495jbw")],
    "D15_SouthSumatra_GWL_model_Irfan2026": [("zenodo", "23008826")],
}


def get(url, timeout=120):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=timeout)


def get_json(url):
    with get(url) as r:
        return json.load(r)


def resolve(src):
    kind = src[0]
    if kind == "url":
        return [(src[1], src[2], None)]
    if kind == "zenodo":
        d = get_json("https://zenodo.org/api/records/" + src[1])
        files = [(f["key"], f["links"]["self"], f["size"]) for f in d["files"]]
        if len(src) > 3:
            import re
            files = [f for f in files if re.search(src[3], f[0])]
        return files
    if kind == "dryad":
        base = "https://datadryad.org"
        d = get_json(base + "/api/v2/datasets/" + urllib.parse.quote("doi:" + src[1], safe=""))
        v = get_json(base + d["_links"]["stash:version"]["href"] + "/files")
        return [(f["path"], base + f["_links"]["stash:download"]["href"], f["size"]) for f in v["_embedded"]["stash:files"]]
    if kind == "eprints":
        # EPrints repositories (e.g. Leeds) list each file as <record>/<n>/<name> on the landing page
        import re
        with get(src[1]) as r:
            page = r.read().decode("utf8", "replace")
        links = sorted(set(re.findall(r'href="(%s\d+/[^"/]+)"' % re.escape(src[1]), page)))
        return [(urllib.parse.unquote(u.rsplit("/", 1)[1]), u, None) for u in links]
    if kind == "hydroshare":
        d = get_json("https://www.hydroshare.org/hsapi/resource/%s/files/" % src[1])
        return [(f["url"].split("/data/contents/")[1], f["url"].replace("http://", "https://"), f["size"]) for f in d["results"]]
    if kind == "figshare":
        d = get_json("https://api.figshare.com/v2/articles/" + src[1])
        return [(f["name"], f["download_url"], f["size"]) for f in d["files"]]
    if kind == "mendeley":
        d = get_json("https://data.mendeley.com/public-api/datasets/" + src[1])
        return [(f["filename"], f["content_details"]["download_url"], f["size"]) for f in d["files"]]
    if kind == "pangaea":
        pid = src[1].split("PANGAEA.")[1]
        return [("PANGAEA_%s.tab" % pid, "https://doi.pangaea.de/%s?format=textfile" % src[1], None)]
    if kind == "dspace7":
        api, uuid = src[1], src[2]
        d = get_json("%s/core/items/%s/bundles?embed=bitstreams" % (api, uuid))
        out = []
        for b in d["_embedded"]["bundles"]:
            if b["name"] != "ORIGINAL":
                continue
            for s in b["_embedded"]["bitstreams"]["_embedded"]["bitstreams"]:
                out.append((s["name"], s["_links"]["content"]["href"], s["sizeBytes"]))
        return out
    if kind == "dataverse":
        base, pid = src[1], src[2]
        d = get_json("%s/api/datasets/:persistentId/?persistentId=%s" % (base, pid))
        out = []
        for f in d["data"]["latestVersion"]["files"]:
            df = f["dataFile"]
            name = df.get("originalFileName") or df["filename"]
            if f.get("restricted"):
                print("   restricted, skipped:", name)
                continue
            out.append((name, "%s/api/access/datafile/%s?format=original" % (base, df["id"]), None))
        return out
    if kind == "epmc_supp":
        return [(src[2], "https://www.ebi.ac.uk/europepmc/webservices/rest/%s/supplementaryFiles" % src[1], "zip-member")]
    if kind == "manual":
        print("   manual:", src[1])
        return []
    raise ValueError(kind)


def download_zip_member(name, url, data_dir):
    import io
    import zipfile
    dest = os.path.join(data_dir, name)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        print("   exists:", os.path.relpath(dest, HERE))
        return
    os.makedirs(data_dir, exist_ok=True)
    with get(url, timeout=300) as r:
        z = zipfile.ZipFile(io.BytesIO(r.read()))
    with open(dest, "wb") as fh:
        fh.write(z.read(name))
    print("   ok: %s (%d bytes)" % (os.path.relpath(dest, HERE), os.path.getsize(dest)))


def download(name, url, size, data_dir):
    if size and size > HUGE:
        print("   over 5 GB, not fetched: %s (%.1f GB) %s" % (name, size / 1024 ** 3, url))
        return
    dest_dir = os.path.join(data_dir, "_large") if size and size > LARGE else data_dir
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, name.replace("/", "_"))
    if os.path.exists(dest) and os.path.getsize(dest) > 0 and (size is None or os.path.getsize(dest) == size):
        print("   exists:", os.path.relpath(dest, HERE))
        return
    tmp = dest + ".part"
    for attempt in range(4):
        try:
            with get(url, timeout=300) as r, open(tmp, "wb") as fh:
                while True:
                    chunk = r.read(1 << 20)
                    if not chunk:
                        break
                    fh.write(chunk)
            got = os.path.getsize(tmp)
            if got == 0 or (size and got != size):
                # figshare sometimes answers scripts with an empty bot-check page
                raise IOError("got %d bytes, expected %s" % (got, size))
            os.replace(tmp, dest)
            if got > LARGE and "_large" not in dest:
                print("   NOTE %s is over 100 MB; move it to data/_large/ before committing" % name)
            print("   ok: %s (%d bytes)" % (os.path.relpath(dest, HERE), got))
            return
        except Exception as e:
            print("   attempt %d failed for %s: %s" % (attempt + 1, name, e))
            time.sleep(2 ** (attempt + 1))
    print("   FAILED:", name, "- open this link in a browser and save the file into", os.path.relpath(dest_dir, HERE))
    print("          ", url)


def main(ids):
    for folder, sources in MANIFEST.items():
        tag = folder.split("_")[0]  # e.g. "A3", "C8-9"
        if ids and not any(i == tag or tag.startswith(i + "-") for i in ids):
            continue
        print(folder)
        for src in sources:
            data_dir = os.path.join(HERE, folder, "data")
            if src[0] == "zenodo" and len(src) > 2 and src[2]:
                data_dir = os.path.join(data_dir, src[2])
            try:
                files = resolve(src)
            except Exception as e:
                print("   could not resolve %s: %s" % (src, e))
                continue
            for name, url, size in files:
                if size == "zip-member":
                    download_zip_member(name, url, data_dir)
                else:
                    download(name, url, size, data_dir)


if __name__ == "__main__":
    main(sys.argv[1:])
