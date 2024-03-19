from DontEdit import *
import sys
import time
def service():
    subprocess.run("service", "--status-all")

    for i in range(subprocess.run("service","--status-all")):
        print(i)
        time.sleep(1)
        sys.stdout.write("\r")
        sys.stdout.write(str(i))
        sys.stdout.flush()


if platform.system() == linux:
    service()
else:
    print("This program only works on Linux computers")