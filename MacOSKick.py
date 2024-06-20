import platform
import subprocess
import os
import sys

# Define constants for colored output
BRIGHT = "\033[1m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

# Define command keywords
nslookupCommand = ["nslookup"]
KICK = ["kick"]

# Function to check if SSH is enabled on macOS
def is_ssh_enabled():
    try:
        output = subprocess.check_output(["launchctl", "list"]).decode("utf-8")
        return "com.openssh.sshd" in output
    except subprocess.CalledProcessError:
        return False

# Function to perform an nslookup and save the output to a file
def NSLOOKUP():
    nslookup = input("Enter the domain to lookup: ")
    output_file = "nslookup.txt"

    try:
        with open(output_file, 'a') as f:
            subprocess.run(['nslookup', nslookup], stdout=f, text=True, check=True)
        print(f"nslookup output saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Function to get the PID of an SSH session associated with an IP address
def get_ssh_pid(ip_address):
    try:
        pid_info = subprocess.check_output(['netstat', '-tnpa']).decode('utf-8')
        for line in pid_info.split('\n'):
            if 'ESTABLISHED' in line and ip_address in line:
                pid = line.split()[6].split('/')[0]
                return pid
    except subprocess.CalledProcessError:
        print(f"Error: Unable to retrieve PID for IP address {ip_address}")
    return None   

# Function to kick a user off the computer by terminating their SSH session
def kick_user(ip_address):
    pid = get_ssh_pid(ip_address)
    if pid:
        try:
            subprocess.run(['sudo', 'kill', pid], check=True)
            print(f"SSH session associated with {ip_address} has been terminated.")
            with open("KICKED_USERS.txt", "a") as kicked_users_file:
                print(f"We have kicked {BRIGHT}{GREEN}{ip_address}{RESET} off your computer")
                print(f"We have kicked {ip_address} off your computer", file=kicked_users_file)
        except subprocess.CalledProcessError:
            print(f"{RED}FAIL{RESET} Unable to terminate SSH session for IP address {ip_address}")
    else:
        print(f"{RED}FAIL{RESET} No active SSH session found for IP address {ip_address}")

# Main function
def main():
    if os.geteuid() != 0:  # Check if the script is run with root privileges
        print(f"{RED}This script requires sudo privileges to run.{RESET}")
        sys.exit(1)
    
    who = subprocess.run(['who'], capture_output=True, text=True)
    connected = who.stdout
    
    # Check if there are any SSH sessions
    if 'pts/' in connected:
        print("There are SSH sessions active.")
        nslookupOrKick = input("Do you want to nslookup or kick a user? (nslookup/kick): ")

        if nslookupOrKick in nslookupCommand:
            NSLOOKUP()
        
        elif nslookupOrKick in KICK:
            ip_address = input("Enter the IP address of the user you want to kick off: ")
            kick_user(ip_address)

        else:
            print("I don't understand what you meant. Please try again.")
    else:
        print("There are no SSH sessions active.")

# Script execution
if __name__ == "__main__":
    if platform.system() == "Darwin":
        try:
            main()
        except KeyboardInterrupt:
            print("\nExiting program...")
    else:
        print("This script only works on macOS")
        sys.exit(1)