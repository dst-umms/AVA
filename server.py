#!/usr/bin/env python
#vim: syntax=python tabstop=2 expandtab

#---------------------------
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: Jun, 11, 2018
#---------------------------

from flask import Flask, request

import requests
import json
import os
from datetime import datetime

#------  GLOBALS  --------#



#------------------------#
#    Flask methods       #
#------------------------#
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/RunPipeline", methods = ['POST'])
def run_pipeline():
  data = request.get_json(force = True)
  return json.dumps({
    "message": "success", 
    "error": None
  }), 200
    

