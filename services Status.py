from DontEdit import *
import sys
import time
def service():
    print("Starting service")
    while True:
        time.sleep(1)
        print("Service running")
if platform.system() == linux:
    service()
else:
    print("This program only works on Linux computers")

