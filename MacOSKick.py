from DontEdit import *
import psutil
if os.geteuid() == ROOT:

    def get_ssh_pid():
        ssh_pids = []
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == 'sshd':  # 'sshd' is the SSH daemon process name
                ssh_pids.append(proc.info['pid'])
        return ssh_pids

    if __name__ == "__main__":
        ssh_pids = get_ssh_pid()
        if ssh_pids:
            print(f"SSH PID session numbers: {ssh_pids}")
            sshSessionsKill = input(">>> ")
            if sshSessionsKill == "y":
                for pid in ssh_pids:
                    try:
                        process = psutil.Process(pid)
                        process.terminate()
                        print(f"Process with PID {GREEN}{pid}{RESET} has been terminated.")
                    except psutil.NoSuchProcess:
                        print(f"Process with PID {RED}{pid}{RESET} does not exist.")
            else:
                print("SSH sessions will not be terminated.")  # User chose not to terminate SSH sessions terminated.
        else:
            print(f"{RED}No SSH sessions found.{RESET}")
else:
    print(f"{RED}PLASES USE ROOT{RESET}")