from tkinter import messagebox
import tkinter as tk
import subprocess
import os
import sys


BRIGHT = '\033[1m'
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Check if the script is run with sudo privileges
if os.geteuid() != 0:
    print("This script requires sudo privileges to run.")
    print("Please run the script again with sudo.")
    sys.exit(1)
else:
    who = subprocess.check_output(['who']).decode('utf-8')
    print(who)
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
        # Get the PID of the SSH session associated with the given IP address
        pid = get_ssh_pid(ip_address)
        if pid:
            try:
                # Terminate the SSH session
                subprocess.run(['sudo', 'kill', pid])
                print(f"SSH session associated with {BRIGHT}{GREEN}{ip_address}{RESET} has been terminated.")
                print(f"We have kicked {BRIGHT}{GREEN}{UserToKick}{RESET} off your computer")
            except subprocess.CalledProcessError:
                print(f"[ {RED}FAIL{RESET} ]: Unable to terminate SSH session for IP address {ip_address}")
        else:
            print(f"[ {RED}FAIL{RESET} ] No active SSH session found for IP address {ip_address}")

    if __name__ == "__main__":
        # Replace '192.168.1.100' with the IP address of the user you want to kick off
        UserToKick = input("Input the IP: ")
        
        kick_user(UserToKick)

