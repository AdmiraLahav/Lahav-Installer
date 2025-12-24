import requests
#[url+username+repo]/raw/refs/heads/main[folder+file_name]
url = "https://github.com/AdmiraLahav/Lahav-Samples/raw/refs/heads/main/internet_access/cloner.py"
out = "file.txt"

with requests.get(url, stream=True, timeout=10) as r:
    r.raise_for_status()
    with open(out, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
