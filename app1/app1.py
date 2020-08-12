import time
import logging
import socket

from flask import Flask, request, jsonify

import requests
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route('/healthz')
def healthz():
    ret = {'status':'ok', 'node':socket.gethostname()}
    return ret

@app.route('/')
def root():
    r = requests.get('https://api.github.com/events')
    return jsonify(r.json())

@app.route('/data')
def data():
    logging.info(request.headers)
    try:
        r = requests.get('http://backend/data')
        r.raise_for_status()
        ret = dict(r.json())
        ret['v'] = 21
        return jsonify(ret)
    except requests.exceptions.HTTPError as err:
        return {'status':'fail2'}, 500
    except requests.exceptions.ConnectionError as e:
        return {'status':'fail'},500

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")



