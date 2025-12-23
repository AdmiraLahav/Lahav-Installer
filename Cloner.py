import subprocess

repo_url = input("Input url")
target_dir = "cloned_repo"
#git clone the repo
subprocess.run([
    "git", "clone", repo_url, target_dir
], check=True)
#open explorer and change dir to the cloned repo
subprocess.run(["explorer.exe",f"{target_dir}"])
