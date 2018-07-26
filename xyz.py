import os
import subprocess
os.system("cd /home/gowtham/Desktop/testgit")
"""
a=os.popen("git status -s")
#print a.read()
print a.close()
"""
abc = subprocess.check_output("echo 'hello'",shell=True)
print "works"+abc



"""
fo = open('/home/gowtham/Desktop/testgit/notes','a')

write("abc")
fo.close()
"""

