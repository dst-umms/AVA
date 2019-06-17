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
  emv = pd.read_csv(sys.argv[6], header = 0, sep = "\t")
  polyphen = pd.read_csv(sys.argv[7], header = 0, sep = "\t")
  pompe = pd.read_csv(sys.argv[8], header = 0, sep = "\t")
  mps = pd.read_csv(sys.argv[9], header = 0, sep = "\t")
  sift = pd.read_csv(sys.argv[10], header = 0, sep = "\t")
  gnomad["Chrom"] = gnomad["Chrom"].astype(str)
  ald["Chrom"] = ald["Chrom"].astype(str)
  clinvar["Chrom"] = clinvar["Chrom"].astype(str)
  dbsnp["Chrom"] = dbsnp["Chrom"].astype(str)
  exac["Chrom"] = exac["Chrom"].astype(str)
  emv["Chrom"] = emv["Chrom"].astype(str)
  polyphen["Chrom"] = polyphen["Chrom"].astype(str)
  pompe["Chrom"] = pompe["Chrom"].astype(str)
  mps["Chrom"] = mps["Chrom"].astype(str)
  sift["Chrom"] = sift["Chrom"].astype(str)
  results = pd.merge(gnomad, ald, on = ["Chrom", "Start", "Ref", "Alt"], how = "left")
  results = pd.merge(results, clinvar, on = ["Chrom", "Start", "Ref", "Alt"], how = "left") 
  results = pd.merge(results, dbsnp, on = ["Chrom", "Start", "Ref", "Alt"], how = "left")
  results = pd.merge(results, exac, on = ["Chrom", "Start", "Ref", "Alt"], how = "left")
  results = pd.merge(results, emv, on = ["Chrom", "Start", "Ref", "Alt"], how = "left")
  results = pd.merge(results, polyphen, on = ["Chrom", "Start", "Ref", "Alt"], how = "left")
  results = pd.merge(results, pompe, on = ["Chrom", "Start", "Ref", "Alt"], how = "left")
  results = pd.merge(results, mps, on = ["Chrom", "Start", "Ref", "Alt"], how = "left")
  results = pd.merge(results, sift, on = ["Chrom", "Start", "Ref", "Alt"], how = "left")
  results = results.drop_duplicates().fillna("-")
  print(results.to_csv(index = False, sep = "\t"))
