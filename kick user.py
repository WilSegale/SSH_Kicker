from DontEdit import *
try:
    # Function to perform an nslookup and save the output to a file
    def NSLOOKUP():
        # Prompt the user to enter the domain to lookup
        nslookup = input("Enter the domain to lookup: ")
        # Output file name
        output_file = "nslookup.txt"

        try:
            # Open the file in append mode
            with open(output_file, 'a') as f:
                # Run the nslookup command and redirect its output to the file
                subprocess.run(['nslookup', nslookup], stdout=f, text=True, check=True)
                # Run nslookup again and print its output to the console
                subprocess.run(['nslookup', nslookup])

            # Print a message indicating where the output has been saved
            print(f"nslookup output saved to {output_file}")
        except subprocess.CalledProcessError as e:
            # Print an error message if nslookup command fails
            print(f"Error: {e}")

    def Kick():
        # Prompt the user to enter the IP address of the user to kick
        print("Enter the IP address of the user you want to kick off:")
        ip_address = input(">>> ")

        # Call the kick_user function
        kick_user(ip_address)

    # Function to get the PID of an SSH session associated with an IP address

    def get_ssh_pid(ip_address):
        try:
            # Get the PID of the SSH session associated with the given IP address
            pid_info = subprocess.check_output(['netstat', '-tnpa']).decode('utf-8')
            for line in pid_info.split('\n'):
                if 'ESTABLISHED' in line and ip_address in line:
                    pid = line.split()[6].split('/')[0]
                    return pid
        except subprocess.CalledProcessError:
            # Print an error message if unable to retrieve PID
            print("Error: Unable to retrieve PID for IP address", ip_address)
        return None   

    # Function to kick a user off the computer by terminating their SSH session
    def kick_user(ip_address):
        pid = get_ssh_pid(ip_address)
        if pid:
            try:
                # Terminate the SSH session
                subprocess.run(['sudo', 'kill', pid])
                # Print a message indicating successful termination
                print(f"SSH session associated with {BRIGHT}{GREEN}{ip_address}{RESET} has been terminated.")
                # Log the kicked user to a file
                with open("KICKED_USERS.txt", "a") as kicked_users_file:
                    print(f"We have kicked {BRIGHT}{GREEN}{ip_address}{RESET} off your computer")
                    print(f"We have kicked {BRIGHT}{GREEN}{ip_address}{RESET} off your computer", file=kicked_users_file)
                    time.sleep(2)
                    print("Do you want to turn off ssh (yes/no)")
                    ssh = input(">>> ")
                    if ssh in yes:
                        subprocess.run(['sudo', 'service', 'ssh', 'stop'])
                        time.sleep(2)
                        subprocess.run(['sudo', 'service', 'ssh', 'status'])
                    else:
                        print("Ok SSH will still run")
            except subprocess.CalledProcessError:
                # Print an error message if unable to terminate SSH session
                print(f"[ {RED}FAIL{RESET} ]: Unable to terminate SSH session for IP address {ip_address}")
        else:
            # Print a message if no active SSH session is found for the IP address
            print(f"[ {RED}FAIL{RESET} ] No active SSH session found for IP address {ip_address}")

    # Main function to control the flow of the script
    def main():
        # Check if the script is run with sudo privileges
        if os.geteuid() != ROOT:
            # Print a message if sudo privileges are required
            print(f"{ORANGE}This script requires sudo privileges to run.{RESET}")
            sys.exit(1)
        else:
            # Get the current users logged in
            who = subprocess.check_output(['who']).decode('utf-8')
            print(who)

            # Prompt the user to choose between nslookup and kicking a user
            nslookupOrKick = input("Do you want to nslookup or kick a user? (nslookup/kick): ")

            # Look for the user to input nslookup in the prompt
            if nslookupOrKick in nslookupCommand:
                # Call the NSLOOKUP function
                NSLOOKUP()
                sys.exit(0)  # Exit after nslookup
        
            # Look for the user to input kick in the prompt
            elif nslookupOrKick in KICK:
                Kick()
            else:
                # Print an error message if the input is not recognized
                print(f"[ {RED}ERROR{RESET} ] I don't understand what you meant by '{nslookupOrKick}'. Please try again.")

    if __name__ == "__main__":
        # Call the main function when the script is executed
        main()
except KeyboardInterrupt:
    print("\nExiting program...")