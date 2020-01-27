import subprocess

HOST="root@192.168.213.198"
COMMAND="ls / "
ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                      shell=False,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)

result = ssh.stdout.readlines()
print("RESULT : ")
for i in result:
   		print(i.decode("ascii"))