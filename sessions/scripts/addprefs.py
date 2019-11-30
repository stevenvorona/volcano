import sys
import os
hostphonenumber = sys.argv[1]
phonenumber = sys.argv[2]
preferences = sys.argv[3]

f = open("sessions/"+ hostphonenumber+"prefs.txt","a")
f.write(phonenumber+"\n"+preferences+"\n")
f.close()
