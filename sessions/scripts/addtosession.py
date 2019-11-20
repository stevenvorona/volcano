import sys
import os
hostphonenumber = sys.argv[0]
friendphonenumber = sys.argv[1]
with open(hostphonenumber + ".txt", mode = 'w') as file:
    file.write(friendphonenumber)
