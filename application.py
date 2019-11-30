from __future__ import print_function
import sys
import json
import requests
import os

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
    phoneNumber = request.args.get('hostphonenumber')
    prefBinary = request.args.get('preferences')
    #POST friend phone number to http://api/joinGroup?hostphonenumber=hashedHostID
    data=request.data
    print(request.data,file=sys.stderr)
    print("addprefs.py using this this phone number ->" + phoneNumber, file=sys.stderr)
    os.system("sudo python sessions/scripts/addprefs.py " + hostPhoneNumber  + " " + phoneNumber + " " + prefBinary)
    #write friend phone number into file
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
