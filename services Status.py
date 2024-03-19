from DontEdit import *

# list the services that are on the computer
def service():
    subprocess.run(["service", "--status-all"])

    print("What service would you like to use (ssh, apache2, bluetooth, etc...)")

    services = input(">>> ")
    print("Would you like to (start, stop, restart, status, --full-restart) the service")
    settings = input(">>> ")
    subprocess.run(["service", services, settings])
    print("Would you like to check the status of the service again?")
    check = input(">>> ")

    if check == "yes":
        subprocess.run(["service", services, "status"])
    else:
        print("Thank you for using this program")
#checks if the user is on linux or not
if platform.system() == linux:
    service()
else:
    print("This program only works on Linux computers")