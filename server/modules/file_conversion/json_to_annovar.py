#!/usr/bin/env python

#-------------------------
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: April, 9, 2019 
#-------------------------

import pandas as pd
import json
import sys

if __name__ == "__main__":
  json_file = sys.argv[1]
  d = json.loads(open(json_file, 'r').read())
  print(pd.DataFrame.from_dict(d, orient = 'columns').to_csv(sep = "\t", index = None, header = None)) 
