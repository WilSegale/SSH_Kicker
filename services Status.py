from DontEdit import *
import sys
import time
def service():
    x = subprocess.run(["service", "--status-all"])

    for i in len(x):
        print(i)

if platform.system() == linux:
    service()
else:
    print("This program only works on Linux computers")