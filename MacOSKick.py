import subprocess

KickUser = input("Enter the username to kick: ")


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
        print(f"No active SSH sessions found for user: {username}")
        return

    for pid in ssh_pids:
        try:
            # Kill the SSH process by PID
            subprocess.check_call(['kill', '-9', pid])
            print(f"Terminated SSH session for user {username}, PID: {pid}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to terminate SSH session with PID {pid}: {e}")

# Example usage
kick_ssh_user(KickUser)