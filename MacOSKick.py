<<<<<<< HEAD
from DontEdit import *
# Function to check if SSH is enabled on macOS
def is_ssh_enabled():
    try:
        output = subprocess.check_output(["launchctl", "list"]).decode("utf-8")
        return "com.openssh.sshd" in output
    except subprocess.CalledProcessError:
        return False
=======
from DontEdit import *  # Import everything from the module DontEdit
import psutil  # Import psutil for process and system information utilities
import os  # Import os for interacting with the operating system

# Check if the current user is root (root has euid 0)
try:
    if os.geteuid() == ROOT:  # Assuming ROOT is defined as 0 or in DontEdit module
>>>>>>> parent of 2750c42 (upda)

        # Function to retrieve all active SSH connections
        def get_ssh_connections():
            ssh_info = []  # List to store information about SSH connections
            # Iterate over all processes
            for proc in psutil.process_iter(['pid', 'name']):
                # Check if the process is the SSH daemon (sshd)
                if proc.info['name'] == 'sshd':
                    # Get network connections for this process
                    connections = proc.connections(kind='inet')
                    # Check for established connections
                    for conn in connections:
                        if conn.status == psutil.CONN_ESTABLISHED:
                            # Append SSH connection info including PID, local, and remote address
                            ssh_info.append({
                                'pid': proc.info['pid'],
                                'local_address': conn.laddr,
                                'remote_address': conn.raddr
                            })
            return ssh_info  # Return the list of SSH connections

        if __name__ == "__main__":
            # Get the list of active SSH sessions
            ssh_sessions = get_ssh_connections()
            if ssh_sessions:
                print(f"Active SSH sessions:")
                # Print out the PID, local, and remote addresses for each SSH session
                for session in ssh_sessions:
                    print(f"PID: {session['pid']}, Local: {session['local_address']}, Remote: {session['remote_address']}")
                
                # Ask the user if they want to terminate the SSH sessions
                print("Do you want to terminate these SSH sessions? (y/n/help/nslookup/who)")
                ssh_sessions_kill = input(">>> ")  # Get user input

                # If the user types 'y', terminate the SSH sessions
                if ssh_sessions_kill == "y" or ssh_sessions_kill in KICK:
                    for session in ssh_sessions:
                        try:
                            # Try to terminate the process by its PID
                            process = psutil.Process(session['pid'])
                            process.terminate()
                            print(f"Process with PID {GREEN}{session['pid']}{RESET} and the remote connection {GREEN}{session['remote_address']}{RESET} has been terminated.")
                        except psutil.NoSuchProcess:
                            # If the process no longer exists, inform the user
                            print(f"Process with PID {RED}{session['pid']}{RESET} does not exist.")
                
                # If the user chooses 'n', exit without terminating the SSH sessions
                elif ssh_sessions_kill == "n":
                    print("SSH sessions will not be terminated.")

<<<<<<< HEAD
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
=======
                # If the user types 'help', show the available options
                elif ssh_sessions_kill == "help":
                    print("Options: y (terminate), n (do not terminate), nslookup (run nslookup command), who (show connected users).")
                
                # If the user types 'nslookup', run the nslookup command
                elif ssh_sessions_kill in nslookupCommand:
                    try:
                        print("To exit this command just type CTRL-C")
                        os.system("nslookup")
                        
                        pass
                    except KeyboardInterrupt:
                        get_ssh_connections()
                # If the user types 'who', run the who command to see logged-in users
                elif ssh_sessions_kill in connected:
                    try:
                        print("To exit this command just type CTRL-C")
                        os.system("who")
                        pass
                    except KeyboardInterrupt:
                        get_ssh_connections()

                # If the user input is invalid, do nothing and print a message
>>>>>>> parent of 2750c42 (upda)
                else:
                    print("\nInvalid input. SSH sessions will not be terminated.")
            else:
                # If no SSH sessions are found, print an appropriate message
                print(f"{RED}\nNo SSH sessions found.{RESET}")
    else:
        # If the user is not running the script as root, print an error message
        print(f"{RED}\nPLEASE USE ROOT PRIVILEGES{RESET}")

<<<<<<< HEAD
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
=======
# If the user presses CTRL-C, handle it gracefully
except KeyboardInterrupt:
    print("\nExiting program...")
    exit()
>>>>>>> parent of 2750c42 (upda)
