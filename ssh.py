import subprocess
 
HOST="vmware@103.19.212.1"
COMMAND="df -h"

ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                      shell=False,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
   error = ssh.stderr.readlines()
   print "ERROR: %s" % error
else:
   print "RESULT : \n%s" % result
