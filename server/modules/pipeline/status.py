#!/usr/bin/env python
#-----------------
# @author: Mahesh Vangala
# @email: <vangalamaheshh@gmail.com>
# @date: Oct, 25, 2018
#-----------------

import re

def pipeline_status(log_file):
  status = {
    "dbsnp": None,
    "clinvar": None,
    "gnomad": None,
    "exac": None,
    "ald": None,
    "emv": None,
    "polyphen": None,
    "pompe": None
  }
  cur_step = None
  with open(log_file, "r") as fh:
    for line in fh:
      step = re.search("rule\s+get_(\w+)_annotation", line)
      if step:
        _, _, _, _, _, _ = fh.readline(), fh.readline(), fh.readline(), fh.readline(), \
          fh.readline(), fh.readline()
        line = fh.readline()
        done = re.search("finished", line, re.IGNORECASE)
        error = re.search("error", line, re.IGNORECASE)
        cur_step = step.group(1)
        if done:
          status[cur_step] = 'complete'
          cur_step = None
        elif error:
          status[cur_step] = 'error'
          cur_step = None
  if cur_step:
    status[cur_step] = 'running'
  return status
      
