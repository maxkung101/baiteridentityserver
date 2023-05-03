#!/usr/bin/env python3
from flask import Flask, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix
import subprocess, random

app = Flask(__name__)
app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route('/')
def baiterIdentity():
        #returns a fake identity and a fake card number
        heading = random.randint(2, 5)
        message = str(heading)
        title = ""
        if heading == 3:
                title = title + "American Express"
                message = message + str(random.randint(0, 9)) + str(random.randint(0, 9))
        elif heading == 4:
                title = title + "Visa"
                message = message + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
        else:
                title = title + "Mastercard"
                message = message + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
        message = message + " " + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + " " + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + " " + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
        try:
                output = subprocess.check_output(['rig'])
                output_str = output.decode('utf-8')
                return jsonify({'errorCode' : 'none', 'title' : title, 'message' : message, 'output_str' : output_str})
        except subprocess.CalledProcessError as e:
                return jsonify({'errorCode' : 'Called Process Error', 'title' : 'Failed', 'message' : e.output.decode('utf-8'), 'output_str' : e.output.decode('utf-8')}), e.returncode

@app.errorhandler(404)
def invalid_route(e):
        #returns an invalid route
        return jsonify({'errorCode' : 404, 'title' : 'Error code 404', 'message' : 'Route not found'})

if __name__ == '__main__':
        app.run(port=8080, debug=True)