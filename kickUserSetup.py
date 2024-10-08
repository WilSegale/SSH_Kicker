from DontEdit import *
try:
    # Check the existence of each file
    file_paths = ["LinuxKick.py", "MacOSKick.py"]

    # Get the operating system name

    print("Do you give me permision to check your computer os (YES/NO)")
    CHECK_USER_ANSWER = input(">>> ")

    def check_OS():
        #sees if hte user has already run the program before
        for file_path in file_paths:
            if not os.path.exists(file_path):
                print(f"Program already run")
                sys.exit(1)
        # if the user chooces yes it will run the program
        if CHECK_USER_ANSWER in yes:
            print("Ok let me run a quick scan")
            print("Please wait...")
            #makes the loading bar visible
            def print_loading_bar(iterations, delay=0.1, width=40):
                """
                Prints a loading bar with green dots to visualize progress.
                
                Args:
                    iterations (int): Total number of iterations.
                    delay (float, optional): Delay between updates in seconds. Default is 0.1 seconds.
                    width (int, optional): Width of the loading bar. Default is 40 characters.
                """
                for loadingBar in range(iterations + 1):
                    progress = loadingBar / iterations  # Calculate the progress ratio
                    bar_length = int(progress * width)  # Calculate the number of dots for the current progress
                    bar = GREEN + '•' * bar_length + RESET + ' ' * (width - bar_length)  # Construct the loading bar string
                    percentage = int(progress * 100)  # Calculate the percentage of completion
                    
                    # Print the loading bar and percentage, replacing the line each iteration
                    print(f'\rLoading [{bar}] {percentage} % ', end='', flush=False)
                    
                    time.sleep(delay)  # Pause to control the update rate
            print_loading_bar(50)
            print("\nDONE")
            # Get the operating system name
            if os_name == Mac:
                print("You are using MacOS.",
                      "So I will remove the Linux veriosn of the program.")  
                subprocess.run(["rm", "-rf", "LinuxKick.py"])
        
            elif os_name == linux:
                print("You are using Linux.",
                      "So I will remove the MAC veriosn of the program.")
                subprocess.run(["rm", "-rf", "MacOSKick.py"])
            else:
                print("I don't know your OS")
        
        # if the user chooces no it will not run the program
        elif CHECK_USER_ANSWER in no:
            print("Ok I will not run the program")
            sys.exit(1)
        
        # if the user askes for help it will tell the user how to use the porgram
        elif CHECK_USER_ANSWER in help:
            print("You can only answer yes or no")
            print("If you don't know how to use the program please ask me")
            # exit the program
            sys.exit(1)
        else:
            print("Please enter a valid answer")
            sys.exit(1)
    check_OS()
except KeyboardInterrupt:
    print("\nYou pressed Ctrl+C")
    sys.exit(1)