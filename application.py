import json
import requests

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/phoneSignup', methods = ['POST'])
def addNewPhoneNumber():
    data = request.form
    print(data, file=sys.stderr)
    users = [
        {
            'name': 'exampleUser',
            'display_name': 'Jane Doe',
            'email': 'user@example.com'
        }
    ]
    return json.dumps(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
