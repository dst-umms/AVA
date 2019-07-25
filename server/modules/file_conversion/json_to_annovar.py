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
  df["Chromosome"] = df["Chromosome"].astype(str)
  df.loc[df.Reference == '.', "Reference"] = '-'
  df.loc[df.Alternate == '.', "Alternate"] = '-'
  header = ["Chromosome", "Position", "Position", "Reference", "Alternate", "Gene", "Run_ID", "Specimen_ID", "C", "P", "Comments"]
  new_df = df[header]
  print(new_df.to_csv(sep = "\t", index = None, header = None)) 
