from DontEdit import *
import psutil
import os

if os.geteuid() == ROOT:  # Check for root privileges

    def get_ssh_connections():
        ssh_info = []
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == 'sshd':  # 'sshd' is the SSH daemon process name
                connections = proc.connections(kind='inet')
                for conn in connections:
                    if conn.status == psutil.CONN_ESTABLISHED:
                        ssh_info.append({
                            'pid': proc.info['pid'],
                            'local_address': conn.laddr,
                            'remote_address': conn.raddr
                        })
        return ssh_info

    if __name__ == "__main__":
        ssh_sessions = get_ssh_connections()
        if ssh_sessions:
            print(f"Active SSH sessions:")
            for session in ssh_sessions:
                print(f"PID: {session['pid']}, Local: {session['local_address']}, Remote: {session['remote_address']}")
            
            print("Do you want to terminate these SSH sessions? (y/n)")
            ssh_sessions_kill = input(">>> ")
            if ssh_sessions_kill == "y":
                for session in ssh_sessions:
                    try:
                        process = psutil.Process(session['pid'])
                        process.terminate()
                        print(f"Process with PID {GREEN}{session['pid']}{RESET} has been terminated.")
                    except psutil.NoSuchProcess:
                        print(f"Process with PID {RED}{session['pid']}{RESET} does not exist.")
            else:
                print("SSH sessions will not be terminated.")
        else:
            print(f"{RED}No SSH sessions found.{RESET}")
else:
    print(f"{RED}PLEASE USE ROOT PRIVILEGES{RESET}")