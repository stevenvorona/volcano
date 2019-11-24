import sys
import os
hostphonenumber = sys.argv[1]
friendphonenumber = sys.argv[2]

f = open("sessions/"+ hostphonenumber+".txt","a")
f.write(friendphonenumber+"\n")
f.close()
