from DontEdit import *

# Function to check if SSH is enabled on Windows
if platform.system() == windows:

    def is_ssh_enabled_windows():
        try:
            output = subprocess.check_output("sc query sshd").decode("utf-8")
            return "RUNNING" in output.upper()
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
        except subprocess.CalledProcessError as error:
            print(f"Error: {error}")

    # Function to get the PID of an SSH session associated with an IP address
    def get_ssh_pid(ip_address):
        try:
            pid_info = subprocess.check_output(['netstat', '-ano']).decode('utf-8')
            for line in pid_info.split('\n'):
                if 'ESTABLISHED' in line and ip_address in line:
                    pid = line.split()[4]
                    return pid
        except subprocess.CalledProcessError:
            print("Error: Unable to retrieve PID for IP address", ip_address)
        return None   

    # Function to kick a user off the computer by terminating their SSH session
    def kick_user(ip_address):
        pid = get_ssh_pid(ip_address)
        if pid:
            try:
                subprocess.run(['taskkill', '/F', '/PID', pid])
                print(f"SSH session associated with {ip_address} has been terminated.")
                with open("KICKED_USERS.txt", "a") as kicked_users_file:
                    print(f"We have kicked {ip_address} off your computer")
                    print(f"We have kicked {ip_address} off your computer", file=kicked_users_file)
                    time.sleep(2)
                    print("Do you want to turn SSH only to localusers? (yes/no)")
                    ssh = input(">>> ")
                    if ssh.lower() == 'yes':
                        subprocess.run(["Enable-PSRemoting"," -Force"])
                    else:
                        print("SSH will still run.")
            except subprocess.CalledProcessError:
                print(f"[ {RED}FAIL{RESET} ] Unable to terminate SSH session for IP address {ip_address}")
        else:
            print(f"[ {RED}FAIL{RESET} ] No active SSH session found for IP address {ip_address}")

    # Main function
    def main():

        who = subprocess.check_output(['tasklist']).decode('utf-8')  # Windows equivalent of 'who'
        print(f"{who}")

        nslookupOrKick = input("Do you want to nslookup or kick a user? (nslookup/kick): ")

        if nslookupOrKick.lower() == 'nslookup':
            NSLOOKUP()
            sys.exit(0)
        
        elif nslookupOrKick.lower() == 'kick':
            ip_address = input("Enter the IP address of the user you want to kick off: ")
            kick_user(f"{ip_address}")
        else:
            print("I don't understand what you meant. Please try again.")

    # Script execution
    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print("\nExiting program...")
else:
    print("This script only works on Windows")
    sys.exit(1)