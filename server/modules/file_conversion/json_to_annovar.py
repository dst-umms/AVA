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
  df = pd.DataFrame.from_dict(d, orient = 'columns')
  df.columns = ["Chrom", "Position", "Start_Alt", "Reference", "Alternate", "Gene", "Comments"]
  df["Chrom"] = df["Chrom"].astype(str)
  df.loc[df.Reference == '.', "Reference"] = '-'
  df.loc[df.Alternate == '.', "Alternate"] = '-'
  print(df.to_csv(sep = "\t", index = None, header = None)) 
