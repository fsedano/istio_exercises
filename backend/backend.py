import time
import logging
import socket

from flask import Flask, request
from flask import jsonify
import requests
import random
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

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
    x = random.randint(0,10)
    logging.info(request.headers)
    #if x < 5:
    #    time.sleep(x)
    #if x < 2:
    #    logging.error("FAILING!!!!")
    #    return {'error':'fail'},500
    #else:
    return {'data':socket.gethostname(),'delay':x}

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")



