import subprocess
    
    
service = 'service --status-all'

p =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
(output, err) = p.communicate()
output = output.decode('utf-8')

print(output)