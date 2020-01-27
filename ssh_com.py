import subprocess
 
HOST="rahul@192.168.213.196"
COMMAND="df -h"

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
   print("RESULT : \n%s" % result)
