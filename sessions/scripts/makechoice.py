import sys
import os
import random
import time
hostphonenumber = sys.argv[1]

f = open("sessions/"+ hostphonenumber+"choice.txt","a")
f.write(str(random.randrange(0,9)))
f.close()
