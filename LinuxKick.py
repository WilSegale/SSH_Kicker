import os
import subprocess
from DontEdit import *
from DontEdit import KICK, nslookupCommand  # Ensure KICK and nslookupCommand are defined in DontEdit

os.system("who")

def start():
    def get_ssh_pids(username):
        try:
            # Get the list of all active SSH sessions for the user
            output = subprocess.check_output(['ps', '-u', username, '-o', 'pid,comm'], universal_newlines=True)
            ssh_pids = [line.split()[0] for line in output.splitlines() if 'sshd' in line]
            return ssh_pids
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving SSH PIDs: {e}")
            return []

    def kick_ssh_user(username):
        ssh_pids = get_ssh_pids(username)
        if not ssh_pids:
            print(f"[ {RED}FAIL{RESET} ] No active SSH sessions found for user: {username}")
            return

        for pid in ssh_pids:
            try:
                # Kill the SSH process by PID
                subprocess.check_call(['kill', '-9', pid])
                print(f"[ {GREEN}SUCCESS{RESET} ]Terminated SSH session for user {username}, PID: {pid}")
                os.system("poweroff")
            except subprocess.CalledProcessError as e:
                print(f"[ {RED}FAIL{RESET} ]Failed to terminate SSH session with PID {pid}: {e}")

    def lookup():
        lookupUser = input("Enter the IP to lookup: ")
        print(f"Looking up {GREEN}{lookupUser}...{RESET}")
        time.sleep(1)
        os.system(f"nslookup {lookupUser}")

    chooseOption = input("Would you like to Kick or lookup username? ")

    if chooseOption.lower() in KICK:
        KickUserCommand = input("Enter the username to kick: ")
        kick_ssh_user(KickUserCommand)  # Pass the correct variable here

    elif chooseOption.lower() in nslookupCommand:
        lookup()

    else:
        print(f"\n[ {RED}FAIL{RESET} ] Invalid option chosen. Please choose either 'Kick' or 'lookup'.")
        start()  # Restart the function if the input is invalid
start()