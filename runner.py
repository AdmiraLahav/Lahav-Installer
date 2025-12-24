import subprocess
import sys

def launch():
    subprocess.Popen([sys.executable, "PRINT.py"])
if __name__ == '__main__':
    launch()