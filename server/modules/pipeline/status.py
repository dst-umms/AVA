#!/usr/bin/env python
#-----------------
# @author: Mahesh Vangala
# @email: <vangalamaheshh@gmail.com>
# @date: Oct, 25, 2018
#-----------------

import re

status = {
  "dbsnp": None,
  "clinvar": None,
  "gnomad": None,
  "exac": None,
  "ald": None 
}

def pipeline_status(log_file):
  cur_step = None
  with open(log_file, "r") as fh:
    for line in fh:
      step = re.search("get_(\w+)_annotation", line)
      done = re.search("finished", line, re.IGNORECASE)
      error = re.search("error", line, re.IGNORECASE)
      if step:
        cur_step = step.group(1)
      elif done:
        status[cur_step] = 'complete'
        cur_step = None
      elif error:
        status[cur_step] = 'error'
        cur_step = None
  if cur_step:
    status[cur_step] = 'running'
  return status
      
