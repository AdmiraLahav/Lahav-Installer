import subprocess
import sys

def launch():
    #sys.executable lets the program run python files
    subprocess.Popen([sys.executable, "PRINT.py"])
if __name__ == '__main__':
    launch()