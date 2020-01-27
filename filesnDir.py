import subprocess
ssh = subprocess.Popen(["ls"],
                      shell=False,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
print(result)