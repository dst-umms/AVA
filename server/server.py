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
import time
import subprocess
import re
import pandas as pd
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
  subprocess.Popen([cmd], shell = True, executable = '/bin/bash')
  retries = 2
  for retry in range(retries):
    if not os.path.isfile(dir_path + '/' + proj_name + '.log'):    
      time.sleep(2)
  if os.path.isfile(dir_path + '/' + proj_name + '.log'):
    return json.dumps({
      "success": "true",
      "error": None,
      "file": proj_name
    }), 200
  else:
    return json.dumps({
      "success": "false",
      "error": "pipeline launch failed",
      "file": proj_name
    }), 200
    
@app.route("/server/GetJson", methods = ['GET'])
def get_json():
  proj_name = request.args["proj_name"]
  out_file = "/usr/local/bin/analysis/{proj_name}/{proj_name}.hg19_multianno.txt.intervar".format(
    proj_name = proj_name
  )
  final_array = []
  with open(out_file, 'r') as fh:
    keys = fh.readline()
    keys = keys.strip()
    keys = keys.split("\t")
    keys.append("id")
    index = 1
    for values in fh:
      values = values.strip()
      values = values.split("\t")
      values.append(index)
      index += 1
      values[0], values[1], values[2] = int(values[0]), int(values[1]), int(values[2])
      final_array.append(dict(zip(keys, values)))
  return json.dumps(final_array), 200
      

@app.route('/server/PipelineStatus', methods = ['POST'])
def get_status():
  proj_name = request.form["proj_name"]
  log_file = "/usr/local/bin/analysis/" + proj_name + ".log"
  pipe_status = [re.findall(r'\((\d+)%\)', line) for line in open(log_file, 'r')][-1] or 1 
  return json.dumps({
    "status": pipe_status,
    "proj_name": proj_name
  }), 200
  




