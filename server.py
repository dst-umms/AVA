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

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/UploadVariantFile", methods = ['PUT', 'POST'])
def upload_file():
  data_file = request.files["VariantFile"]
  proj_name = request.form["ProjectName"]
  file_name = secure_filename(proj_name + '.txt')
  dir_path = "/usr/local/bin/analysis/input"
  os.makedirs(dir_path, exist_ok = True)
  data_file.save(dir_path + '/' + file_name)
  cmd = """snakemake -s /usr/local/bin/AVA/AVA.snakefile \
            --config proj_name={proj_name} >{log_file} 2>&1""".format(
          proj_name = proj_name,
          log_file = "/usr/local/bin/analysis/" + proj_name + ".log"
        )
  subprocess.Popen([cmd], shell = True) 
  return json.dumps({
    "message": "success", 
    "error": None
  }), 200
    

