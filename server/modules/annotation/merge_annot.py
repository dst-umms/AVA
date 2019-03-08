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
  clinvar = pd.read_csv(sys.argv[3], header = 0, sep = "\t")
  dbsnp = pd.read_csv(sys.argv[4], header = 0, sep = "\t")
  exac = pd.read_csv(sys.argv[5], header = 0, sep = "\t")
  results = pd.merge(gnomad, ald, on = ["Chrom", "Start", "Ref", "Alt"], how = "left")
  results = pd.merge(results, clinvar, on = ["Chrom", "Start", "Ref", "Alt"], how = "left") 
  results = pd.merge(results, dbsnp, on = ["Chrom", "Start", "Ref", "Alt"], how = "left")
  results = pd.merge(results, exac, on = ["Chrom", "Start", "Ref", "Alt"], how = "left")
  results = results.drop_duplicates().fillna("-")
  print(results.to_csv(index = False, sep = "\t"))
