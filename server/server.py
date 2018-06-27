#!/usr/bin/env python
#vim: syntax=python tabstop=2 expandtab

#---------------------------
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: Jun, 11, 2018
#---------------------------

from flask import Flask, request
from werkzeug import secure_filename
import requests
import json
import os
import subprocess
from datetime import datetime

#------  GLOBALS  --------#



#------------------------#
#    Flask methods       #
#------------------------#
app = Flask(__name__)

@app.route("/server")
def hello():
  return "Hello World!"

@app.route("/server/UploadVariantFile", methods = ['PUT', 'POST'])
def upload_file():
  data_file = request.files["VariantFile"]
  proj_name = data_file.filename.replace(' ', '_')
  proj_name = proj_name.replace('.txt', '') if proj_name[-4:] == '.txt' else proj_name
  file_name = secure_filename(proj_name + '.txt')
  dir_path = "/usr/local/bin/analysis/input"
  os.makedirs(dir_path, exist_ok = True)
  data_file.save(dir_path + '/' + file_name)
  cmd = """snakemake -p --latency-wait 60 -s /usr/local/bin/AVA/AVA.snakefile \
            --config proj_name={proj_name} >{log_file} 2>&1""".format(
          proj_name = proj_name,
          log_file = "/usr/local/bin/analysis/" + proj_name + ".log"
        )
  #subprocess.Popen([cmd], shell = True, executable = '/bin/bash') 
  return json.dumps({
    "message": "success", 
    "file": proj_name,
    "error": None
  }), 200
    
@app.route("/server/GetJson", methods = ['POST'])
def get_json():
  return json.dumps({"data": [{"name": "mahesh", "email": "mahesh", "phone": "mahesh"}, {"name": "mahesh", "email": "mahesh", "phone": "mahesh"}]}), 200
