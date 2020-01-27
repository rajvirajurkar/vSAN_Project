import subprocess
 
HOST="root@192.168.213.198"
COMMAND="ls /usr/bin"

ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                      shell=False,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
   error = ssh.stderr.readlines()
   #print "ERROR: %s" % error
   print("ERROR: %s" % error)
else:
   #print "RESULT : \n%s" % result
   print("RESULT : \n")
   result.sort()
   for i in result:
   		print(i.decode("ascii"))
