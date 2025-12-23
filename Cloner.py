import subprocess
def setup():
    repo_url = input("Input url of the repo: \n")
    target_dir = "cloned_repo"
    return repo_url,target_dir
#git clone the repo
def clone(repo_url,target_dir):
    subprocess.run([
        "git", "clone", repo_url, target_dir
    ], check=True)
#open explorer and change dir to the cloned repo
def explorer(target_dir):
    subprocess.run(["explorer.exe",f"{target_dir}"])


#pretty janky stuff, like Main(){} in C#
# you cannot use paramaters defined outside yoour def, thats why we firstly use return and vars
#and then we say, use these vars in this def
#after this we call clone() with the vars we stored, and explorer() again with the vars we stored
if __name__ == '__main__':
    repo_url,target_dir = setup()
    clone(repo_url,target_dir)
    explorer(target_dir)