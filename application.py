from __future__ import print_function
import sys
import json
import requests
import os
import time
import random

from flask import Flask
from flask import request

import mysql.connector

app = Flask(__name__)

@app.route('/phoneSignup', methods = ['POST'])
def addNewPhoneNumber():
    print(request.data,file=sys.stderr)
    data = request.data
    return json.dumps(data)

@app.route('/createGroup', methods = ['POST'])
def createGroup():
    #host posts phone number to /createGroup, function hashes it to ID, creates file in session directory headed with ID, return hashed ID
    print(request.data,file=sys.stderr)
    hostPhoneNumber = request.args.get('hostphonenumber')
    print("group created under host phone" + hostPhoneNumber,file=sys.stderr)
    data = request.data
    os.system("python sessions/scripts/createsession.py "+hostPhoneNumber)
    groupUrl = "/joinGroup?host="+hostPhoneNumber
    #return style: POST route of http://api/joinGroup?hostphonenumber=hashedHostID
    return json.dumps(groupUrl);

@app.route('/joinGroup', methods = ['POST'])
def joinGroup():
    hostPhoneNumber = request.args.get('hostphonenumber')
    friendPhoneNumber = request.args.get('friendphonenumber')
    #POST friend phone number to http://api/joinGroup?hostphonenumber=hashedHostID
    print(request.data,file=sys.stderr)
    os.system("sudo python sessions/scripts/addtosession.py " + hostPhoneNumber + " " +  friendPhoneNumber)
    print("Added friend to group session file with numnber: " + friendPhoneNumber,file=sys.stderr);
    #friend phone number is a component of data
    print(hostPhoneNumber,file=sys.stderr)
    #write friend phone number into file
    data = request.data
    return json.dumps(data)

@app.route('/getUserCount', methods = ['POST'])
def getUserCount():
    hostPhoneNumber = request.args.get('hostphonenumber')
    #POST friend phone number to http://api/joinGroup?hostphonenumber=hashedHostID
    print(request.data,file=sys.stderr)
    print("getusercount.py using this this phone number ->" + hostPhoneNumber, file=sys.stderr)

    count = 0
    thefile = open("sessions/"+ hostPhoneNumber+".txt","rb")
    while 1:
        buffer = thefile.read(8192*1024)
        if not buffer: break
        count += buffer.count('\n')
    thefile.close(  )
    #friend phone number is a component of data
    print(count,file=sys.stderr)
    #write friend phone number into file
    return json.dumps(count)

@app.route('/receivePrefs', methods = ['POST'])
def receivePrefs():
    hostPhoneNumber = request.args.get('hostphonenumber')
    phoneNumber = request.args.get('phonenumber')
    #prefBinary = request.args.get('preferences')
    data=request.data
    print(request.data,file=sys.stderr)
    print("addprefs.py using this this host phone number ->" + hostPhoneNumber, file=sys.stderr)
    #os.system("sudo python sessions/scripts/addprefs.py " + hostPhoneNumber  + " " + phoneNumber + " " + prefBinary)
    os.system("sudo python sessions/scripts/addprefs.py " + hostPhoneNumber  + " " + phoneNumber)
    #write friend phone number into file
    return json.dumps(data)

@app.route('/receiveStack', methods = ['POST'])
def receiveStack():
    hostPhoneNumber = request.args.get('hostphonenumber')
    phoneNumber = request.args.get('phonenumber')
    #prefBinary = request.args.get('preferences')
    data=request.data
    print(request.data,file=sys.stderr)
    print("addtostack.py using this this host phone number ->" + hostPhoneNumber, file=sys.stderr)
    #os.system("sudo python sessions/scripts/addprefs.py " + hostPhoneNumber  + " " + phoneNumber + " " + prefBinary)
    os.system("sudo python sessions/scripts/addtostack.py " + hostPhoneNumber  + " " + phoneNumber)
    #write friend phone number into file
    return json.dumps(data)

@app.route('/checkComplete', methods = ['GET'])
def checkComplete():
    hostPhoneNumber = request.args.get('hostphonenumber')
    #POST friend phone number to http://api/joinGroup?hostphonenumber=hashedHostID
    data=request.data
    print(request.data,file=sys.stderr)
    print("addprefs.py using this this phone number ->" + phoneNumber, file=sys.stderr)
    os.system("sudo python sessions/scripts/addprefs.py " + hostPhoneNumber  + " " + phoneNumber + " " + prefBinary)
    #write friend phone number into file
    return json.dumps(data)

@app.route('/checkSymmetry', methods = ['POST'])
def checkSymmetry():
    hostPhoneNumber = request.args.get('hostphonenumber')
    myPhoneNumber = request.args.get('phonenumber')
    print("checking count symmetry on: " + hostPhoneNumber, file=sys.stderr)
    while(True):
        countBase = 1
        countSubmitted = 0
        thefile = open("sessions/"+ hostPhoneNumber+".txt","rb")
        while 1:
            buffer = thefile.read(8192*1024)
            if not buffer: break
            countBase += buffer.count('\n')
        thefile.close(  )
        #friend phone number is a component of data
        print("OG file has: " + str(countBase),file=sys.stderr)

        countCurrent = 0
        thefile = open("sessions/"+ hostPhoneNumber+"prefs.txt","rb")
        while 1:
            buffer = thefile.read(8192*1024)
            if not buffer: break
            countCurrent += buffer.count('\n')
        thefile.close(  )
        if(countCurrent == countBase*2):
            break
        time.sleep(0.25)
    return json.dumps("worked")

@app.route('/checkStackComplete', methods = ['POST'])
def checkStackComplete():
    hostPhoneNumber = request.args.get('hostphonenumber')
    myPhoneNumber = request.args.get('phonenumber')
    print("checking count card stack on: " + hostPhoneNumber, file=sys.stderr)
    while(True):
        countBase = 1
        countSubmitted = 0
        thefile = open("sessions/"+ hostPhoneNumber+".txt","rb")
        while 1:
            buffer = thefile.read(8192*1024)
            if not buffer: break
            countBase += buffer.count('\n')
        thefile.close(  )
        #friend phone number is a component of data
        print("OG file has: " + str(countBase),file=sys.stderr)

        countCurrent = 0
        thefile = open("sessions/"+ hostPhoneNumber+"stack.txt","rb")
        while 1:
            buffer = thefile.read(8192*1024)
            if not buffer: break
            countCurrent += buffer.count('\n')
        thefile.close(  )
        if(countCurrent == countBase*2):
            break
        time.sleep(0.25)
    if hostPhoneNumber == myPhoneNumber:
        os.system("sudo touch sessions/" + hostPhoneNumber + "choice.txt")
        os.system("sudo python sessions/scripts/makechoice.py " + hostPhoneNumber)
        f = open("sessions/"+ hostPhoneNumber+"choice.txt","rb")
        movieRng = f.readline()
        print("Selected movie has index: " + movieRng,file=sys.stderr)
        f.close()
        return json.dumps(movieRng)
    return json.dumps("worked")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
