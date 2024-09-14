from DontEdit import *  # Import everything from the module DontEdit
import psutil  # Import psutil for process and system information utilities
import os  # Import os for interacting with the operating system

# Check if the current user is root (root has euid 0)

try:
    if os.geteuid() == ROOT:

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
                print("Do you want to terminate these SSH sessions? (y/n/help/exit/nslookup/who)")
                ssh_sessions_kill = input(">>> ")  # Get user input

                # If the user types 'y', terminate the SSH sessions
                if ssh_sessions_kill == "y":
                    for session in ssh_sessions:
                        try:
                            # Try to terminate the process by its PID
                            process = psutil.Process(session['pid'])
                            process.terminate()
                            print(f"Process with PID {GREEN}{session['pid']}{RESET} has been terminated.")
                        except psutil.NoSuchProcess:
                            # If the process no longer exists, inform the user
                            print(f"Process with PID {RED}{session['pid']}{RESET} does not exist.")
                
                # If the user chooses 'n', exit without terminating the SSH sessions
                elif ssh_sessions_kill == "n":
                    print("SSH sessions will not be terminated.")
                    exit()  # Exit the program

                # If the user types 'help', show the available options
                elif ssh_sessions_kill == "help":
                    print("Options: y (terminate), n (do not terminate), exit (quit program), nslookup (run nslookup command).")
                
                # If the user types the nslookup command, run it to resolve hostnames/IP addresses
                elif ssh_sessions_kill == nslookupCommand:
                    os.system("nslookup")

                # If the user types 'who', run the 'who' command to see logged-in users and SSH connections
                elif ssh_sessions_kill == connected:
                    os.system("who")
                    exit()
                # If the user input is invalid, do nothing and print a message
                else:
                    print("Invalid input. SSH sessions will not be terminated.")
            else:
                # If no SSH sessions are found, print an appropriate message
                print(f"{RED}No SSH sessions found.{RESET}")
    else:
        # If the user is not running the script as root, print an error message
        print(f"{RED}PLEASE USE ROOT PRIVILEGES{RESET}")

# if the user uses CTRL-C it will exit softly
except KeyboardInterrupt:
    print("Exiting program...")
    exit()