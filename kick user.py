import subprocess
import os
import sys

# Color variables
BRIGHT = '\033[1m'
GREEN = "\033[92m"
RED = "\033[91m"
ORANGE = "\033[38;2;255;165;0m"
RESET = "\033[0m"

ROOT = 0

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

if __name__ == "__main__":
    # Check if the script is run with sudo privileges
    if os.geteuid() != ROOT:
        print(f"{ORANGE}This script requires sudo privileges to run.{RESET}")
        sys.exit(1)
    else:
        who = subprocess.check_output(['who']).decode('utf-8')
        print(who)

        nslookupOrKick = input("Do you want to nslookup or kick a user? (nslookup/kick): ")
        
        if nslookupOrKick == "nslookup":
            nslookup = input("Enter the domain to lookup: ")
            subprocess.run(['nslookup', nslookup])
            sys.exit(0)  # Exit after nslookup

        print("Enter the IP address of the user you want to kick off:")
        ip_address = input(">>> ")

        # Add input validation if needed

        kick_user(ip_address)
