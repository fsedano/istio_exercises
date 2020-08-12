import time
import logging
import socket

from flask import Flask
from flask import jsonify
import requests
app = Flask(__name__)

@app.route('/healthz')
def healthz():
    ret = {'status':'ok-backend', 'node':socket.gethostname()}
    return ret

@app.route('/')
def root():
    r = requests.get('https://api.github.com/events')
    return jsonify(r.json())

@app.route('/data')
def data():
    return {'data':socket.gethostname()}

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")



