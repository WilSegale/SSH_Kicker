from DontEdit import *

def NSLOOKUP():
    nslookup = input("Enter the domain to lookup: ")
    output_file="nslookup.txt"

    try:
        with open(output_file, 'a') as f:
            subprocess.run(['nslookup', nslookup], stdout=f, text=True, check=True)
            subprocess.run(['nslookup', nslookup])

        print(f"nslookup output saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        
def get_ssh_pid(ip_address):
    try:
        # Get the PID of the SSH session associated with the given IP address
        pid_info = subprocess.check_output(['netstat', '-tnpa']).decode('utf-8')
        for line in pid_info.split('\n'):
            if 'ESTABLISHED' in line and ip_address in line:
                pid = line.split()[6].split('/')[0]
                return pid
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve PID for IP address", ip_address)
    return None   

def kick_user(ip_address):
    pid = get_ssh_pid(ip_address)
    if pid:
        try:
            # Terminate the SSH session
            subprocess.run(['sudo', 'kill', pid])
            print(f"SSH session associated with {BRIGHT}{GREEN}{ip_address}{RESET} has been terminated.")
            with open("KICKED_USERS.txt", "a") as kicked_users_file:
                print(f"We have kicked {BRIGHT}{GREEN}{ip_address}{RESET} off your computer")
                print(f"We have kicked {BRIGHT}{GREEN}{ip_address}{RESET} off your computer", file=kicked_users_file)
        except subprocess.CalledProcessError:
            print(f"[ {RED}FAIL{RESET} ]: Unable to terminate SSH session for IP address {ip_address}")
    else:
        print(f"[ {RED}FAIL{RESET} ] No active SSH session found for IP address {ip_address}")

def main():
    # Check if the script is run with sudo privileges
    if os.geteuid() != ROOT:
        print(f"{ORANGE}This script requires sudo privileges to run.{RESET}")
        sys.exit(1)
    else:
        who = subprocess.check_output(['who']).decode('utf-8')
        print(who)

        nslookupOrKick = input("Do you want to nslookup or kick a user? (nslookup/kick): ")

        # looks for the user to input nslookup in the prompt
        if nslookupOrKick in nslookupCommand:
            NSLOOKUP()
            sys.exit(0)  # Exit after nslookup
        # looks for the user to input kick in the prompt
        elif nslookupOrKick in KICK:
            print("Enter the IP address of the user you want to kick off:")
            ip_address = input(">>> ")

            # Add input validation if needed

            kick_user(ip_address)
        else:
            print(f"[ {RED}ERROR{RESET} ] I don't understand what you meant by '{nslookupOrKick}'. Please try again.")

if __name__ == "__main__":
    main()
