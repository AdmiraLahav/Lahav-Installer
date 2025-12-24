import requests
#[url+username+repo]/raw/refs/heads/main[folder+file_name]

#also       raw.githubusercontent.com/AdmiraLahav/Lahav-Samples/main/internet_access/cloner.py
file_url = "https://github.com/AdmiraLahav/Lahav-Samples/raw/refs/heads/main/internet_access/cloner.py"
output_file_name = "file.txt"

with requests.get(file_url, stream=True, timeout=10) as requests_var:
    requests_var.raise_for_status()
    with open(output_file_name, "wb") as file:
        for chunk in requests_var.iter_content(chunk_size=8192):
            file.write(chunk)
