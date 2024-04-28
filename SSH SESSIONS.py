import subprocess

def get_active_ssh_sessions():
    try:
        # Run the 'netstat' command to get information about active sessions
        result = subprocess.run(["netstat", "-ano"], capture_output=True, text=True)
        # Filter the output to only show SSH sessions
        ssh_sessions = [line for line in result.stdout.split('\n') if ':22' in line and 'ESTABLISHED' in line]
        return '\n'.join(ssh_sessions)
    except Exception as e:
        print("Error:", e)
        return None

# Usage
active_sessions = get_active_ssh_sessions()
if active_sessions:
    print("Active SSH sessions:")
    print(active_sessions)
else:
    print("Unable to retrieve active SSH sessions.")
