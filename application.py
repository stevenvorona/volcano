from __future__ import print_function
import sys
import json
import requests

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/phoneSignup', methods = ['POST'])
def addNewPhoneNumber():
    print(request.data,file=sys.stderr)
    data = request.form
    print(data.items(),file=sys.stderr)
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
