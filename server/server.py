#!/usr/bin/env python
#vim: syntax=python tabstop=2 expandtab

#---------------------------
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: Jun, 11, 2018
#---------------------------

from flask import Flask, request
from flask_cors import CORS
from werkzeug import secure_filename
import requests
import json
import os
import time
import subprocess
import re
from modules.pipeline import status
#------  GLOBALS  --------#



#------------------------#
#    Flask methods       #
#------------------------#
app = Flask(__name__)
CORS(app)

@app.route("/server")
def hello():
  return "Hello World!"

@app.route("/server/UploadVariantFile", methods = ['PUT', 'POST'])
def upload_file():
  data_file = request.files["variant-file"]
  proj_name = request.form['proj-name']
  file_format = request.form['file-format']
  file_name = secure_filename(proj_name + '.' + file_format)
  dir_path = "/usr/local/bin/analysis/" + proj_name
  os.makedirs(dir_path + "/input", exist_ok = True)
  data_file.save(dir_path + '/input/' + file_name)
  log_file = dir_path + "/" + proj_name + ".log"
  cmd = """snakemake -p --latency-wait 60 -s /usr/local/bin/AVA/AVA.snakefile \
            --config proj_name={proj_name} file_format={file_format} --directory {work_dir} \
            >{log_file} 2>&1
        """.format(
          proj_name = proj_name,
          file_format = file_format,
          work_dir = dir_path,
          log_file = log_file
        )
  if os.path.isfile(log_file) and not re.findall('error', open(log_file, 'r').read(), re.IGNORECASE):
    return json.dumps({
      "success": "true",
      "error": None,
      "file": proj_name
    }), 200
  subprocess.Popen([cmd], shell = True, executable = '/bin/bash')
  retries = 2
  for retry in range(retries):
    if not os.path.isfile(log_file):    
      time.sleep(2)
  if os.path.isfile(log_file):
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
    
@app.route("/server/GetVariantInfo", methods = ['GET', 'POST'])
def get_json():
  if request.method == 'POST':
    return json.dumps({"success": "true"}), 200
  proj_name = request.args["proj-name"]
  out_file = "/usr/local/bin/analysis/{proj_name}/output/{proj_name}.final.json".format(
    proj_name = proj_name
  )
  return open(out_file, 'r').read(), 200
      

@app.route('/server/PipelineStatus', methods = ['POST'])
def get_status():
  proj_name = request.form["proj-name"]
  log_file = "/usr/local/bin/analysis/{proj_name}/{proj_name}.log".format(proj_name = proj_name)
  if os.path.isfile(log_file):
    pipe_status = status.pipeline_status(log_file) 
    return json.dumps({
      "data": pipe_status,
      "proj_name": proj_name,
      "error": None
    }), 200
  else:
    return json.dumps({
      "data": None,
      "error": "Variant Pipeline doesn't exist for project: " + proj_name,
      "proj_name": proj_name
    }), 200
  


