# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 13:43:43 2021

@author: venka
"""

import flask
from flask import Flask,request,jsonify
import argparse
from argparse import ArgumentParser
import json
from gevent.pywsgi import WSGIServer
from flask_cors import CORS


app = Flask(__name__)

CORS(app)


@app.route("/",methods=['POST','GET'])
def hello():
    return "Hello world"


if __name__ == "__main__":
    port = 5001
    http_server = WSGIServer(("0.0.0.0",port),app)
    print("app runnning on {0}".format(port))
    http_server.serve_forever()