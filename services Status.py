from DontEdit import *

# list the services that are on the computer
def service():
    try:
        subprocess.run(["service", "--status-all"])
        
        # asks the user what service they want to use
        print("What service would you like to use (ssh, apache2, bluetooth, etc...)")
        
        # gets the service that the user inputs
        services = input(">>> ")
        print("Would you like to (start, stop, restart or --full-restart) the service")
        
        # gets the settings that the user inputs for the service that the user inputs
        settings = input(">>> ")
        
        # starts the service that the user inputs
        subprocess.run(["service", services, settings])
        print("Would you like to check the status of the service again?")
        check = input(">>> ")
        
        # if the user inputs yes then it will check the status of the service
        if check in yes:
            subprocess.run(["service", services, "status"])
        else:
            print("Exiting the program")
    
    except KeyboardInterrupt:
        print("Exiting the program")
        sys.exit(0)

#checks if the user is on linux or not
if platform.system() == linux:
    service()
else:
    print("This program only works on Linux computers")