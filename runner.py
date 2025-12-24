import subprocess
import sys

def launch():
    #sys.executable lets the program run python files
    A=subprocess.Popen([sys.executable, "PRINT.py"])
    return A

if __name__ == '__main__':
    launch()