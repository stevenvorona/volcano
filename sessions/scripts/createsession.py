import sys
import os
phonenumber = sys.argv[1]
print "createsession.py printed this phone number ->" + phonenumber
#creates group
os.system("sudo rm -r sessions/" + phonenumber + ".txt")
os.system("touch sessions/" + phonenumber + ".txt")

#creates preferences sheet for group
os.system("sudo rm -r sessions/"+phonenumber+"prefs.txt")
os.system("touch sessions/"+phonenumber+"prefs.txt")

os.system("sudo rm -r sessions/"+phonenumber+"stack.txt")
os.system("touch sessions/"+phonenumber+"stack.txt")
