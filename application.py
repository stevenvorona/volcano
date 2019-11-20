from __future__ import print_function
import sys
import json
import requests

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
    print(hostPhoneNumber,file=sys.stderr)
    data = request.data
    #return style: POST route of http://api/joinGroup?hostphonenumber=hashedHostID
    return json.dumps(data)

@app.route('/joinGroup', methods = ['POST'])
def createGroup():
    hostPhoneNumber = request.args.get('hostphonenumber')
    #POST friend phone number to http://api/joinGroup?hostphonenumber=hashedHostID
    print(request.data,file=sys.stderr)
    #friend phone number is a component of data
    print(hostPhoneNumber,file=sys.stderr)
    #write friend phone number into file
    data = request.data
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
