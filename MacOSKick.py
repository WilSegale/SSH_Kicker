import os
import sys
import subprocess
import time
import platform

# Define constants
ROOT = 0
nslookupCommand = ["nslookup", "lookup"]
KICK = ["kick"]
yes = ["yes", "y"]
RED = '\033[91m'
RESET = '\033[0m'

# Function to check if SSH is enabled on macOS
def is_ssh_enabled():
    try:
        output = subprocess.check_output(["launchctl", "list"]).decode("utf-8")
        return "com.openssh.sshd" in output
    except subprocess.CalledProcessError:
        return False

# Function to check if SSH is enabled on Linux
def is_ssh_enabled_linux():
    try:
        output = subprocess.check_output(["systemctl", "status", "ssh"]).decode("utf-8")
        return "active (running)" in output
    except subprocess.CalledProcessError:
        return False

# Function to perform an nslookup and save the output to a file
def NSLOOKUP():
    nslookup = input("Enter the domain to lookup: ")
    output_file = "nslookup.txt"

    try:
        with open(output_file, 'a') as f:
            subprocess.run(['nslookup', nslookup], stdout=f, text=True, check=True)
            subprocess.run(['nslookup', nslookup])
        print(f"nslookup output saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Function to get the PID of an SSH session associated with an IP address
# Function to get the PID of an SSH session associated with an IP address on macOS
def get_ssh_pid(ip_address):
    try:
        # Use 'netstat' to find active connections and grep the specific IP
        connection_info = subprocess.check_output(['netstat', '-anv']).decode('utf-8')
        for line in connection_info.split('\n'):
            if 'ESTABLISHED' in line and ip_address in line:
                # The second-to-last column contains the PID/Program name
                local_port = line.split()[3].split('.')[1]  # Extract the local port number
                # Now use 'ps' to match the SSH process with the local port
                pid_info = subprocess.check_output(['ps', '-ax']).decode('utf-8')
                for process in pid_info.split('\n'):
                    if 'sshd' in process and local_port in process:
                        pid = process.split()[0]  # PID is the first column in 'ps' output
                        return pid
    except subprocess.CalledProcessError:
        print(f"Error: Unable to retrieve PID for IP address {ip_address}")
    return None

# Function to kick a user off the computer by terminating their SSH session
def kick_user(ip_address):
    pid = get_ssh_pid(ip_address)
    if pid:
        try:
            subprocess.run(['sudo', 'kill', pid])
            print(f"SSH session associated with {ip_address} has been terminated.")
            with open("KICKED_USERS.txt", "a") as kicked_users_file:
                print(f"We have kicked {ip_address} off your computer")
                print(f"We have kicked {ip_address} off your computer", file=kicked_users_file)
                time.sleep(2)

                if platform.system().lower() == "darwin":  # macOS is 'Darwin'
                    print("Do you want to turn off ssh (yes/no)? ")
                    ssh = input(">>> ").strip().lower()
                    if ssh in yes:
                        subprocess.run(['sudo', 'launchctl', 'unload', '/System/Library/LaunchDaemons/ssh.plist'])
                        time.sleep(2)
                        subprocess.run(['sudo', 'launchctl', 'list'])
                    else:
                        print("Ok SSH will still run")
                else:
                    sys.exit(1)
        except subprocess.CalledProcessError:
            print(f"[ {RED}FAIL{RESET} ] Unable to terminate SSH session for IP address {ip_address}")
    else:
        print(f"[ {RED}FAIL{RESET} ] No active SSH session found for IP address {ip_address}")

# Main function
def main():
    if os.geteuid() != ROOT:
        print("This script requires sudo privileges to run.")
        sys.exit(1)
    else:
        who = subprocess.check_output(['who']).decode('utf-8')
        print(who)

        nslookupOrKick = input("Do you want to nslookup or kick a user? (nslookup/kick): ").strip().lower()

        if nslookupOrKick in nslookupCommand:
            NSLOOKUP()
            sys.exit(0)
        
        elif nslookupOrKick in KICK:
            ip_address = input("Enter the IP address of the user you want to kick off: ")
            kick_user(ip_address)

        else:
            print("I don't understand what you meant. Please try again.")

# Script execution
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting program...")
