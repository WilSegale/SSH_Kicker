from DontEdit import *

# list the services that are on the computer
def service():
    subprocess.run(["service", "--status-all"])

    print("What service would you like to use etc(ssh, apache2)")

#checks if the user is on linux or not
if platform.system() == linux:
    service()
else:
    print("This program only works on Linux computers")