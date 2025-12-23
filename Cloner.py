import subprocess

repo_url = "https://github.com/AdmiraLahav/AdmiraLahav.github.io.git"
target_dir = "cloned_repo"

subprocess.run([
    "git", "clone", repo_url, target_dir
], check=True)

subprocess.run(["explorer.exe",f"{target_dir}"])
