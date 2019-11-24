import sys
import os
phonenumber = sys.argv[1]
print "createsession.py printed this phone number ->" + phonenumber
os.system("touch sessions/" + phonenumber + ".txt")
