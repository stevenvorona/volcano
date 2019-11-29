import sys
import os
phonenumber = sys.argv[1]
print "getusercount.py using this this phone number ->" + phonenumber

count = 0
thefile = open("sessions/"+ phonenumber+".txt","rb")
while 1:
    buffer = thefile.read(8192*1024)
    if not buffer: break
    count += buffer.count('\n')
thefile.close(  )
print count
