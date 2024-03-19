from DontEdit import *
import sys
import time
def service():
    subprocess.run("sudo","service","--list")

if platform.system() == linux:
    service()
else:
    print("This program only works on Linux computers")

