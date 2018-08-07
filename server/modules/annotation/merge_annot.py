#!/usr/bin/env python

#-----------------------
# @title: merge_annot.py
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: Aug, 7, 2018
#-----------------------

import pandas as pd
import sys

if __name__ == "__main__":
  gnomad = pd.read_csv(sys.argv[1], header = 0, sep = "\t")
  ald = pd.read_csv(sys.argv[2], header = 0, sep = "\t")
  results = pd.merge(gnomad, ald, on = ["Chrom", "Start", "Ref", "Alt"], how = "left")
  results = results.fillna("-")
  print(results.to_csv(index = False, sep = "\t"))
