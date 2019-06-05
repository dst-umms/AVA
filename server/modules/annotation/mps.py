#!/usr/bin/env python

#-----------------------
# @title: mps.py
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: Jun, 5, 2019
#-----------------------

import pandas as pd
import sys

def get_mps_info(mps_annot_file):
  df = pd.read_csv(mps_annot_file, header = None, sep = ",")
  df.columns = ["Exon", "MType", "p.", "Func", "Author", "Paper"]
  df["P."] = "p." + df["p."]
  df["Gene"] = "IDUA" 
  return df

if __name__ == "__main__":
  variants = pd.read_csv(sys.argv[1], header = None, sep = "\t")
  variants.columns = ["Chrom", "Position", "Start_Alt", "Reference", "Alternate", "Gene", "RunID", "SpecID", "C.", "P.", "Comments"]
  variants["Chrom"] = variants["Chrom"].astype(str)
  mps_info = get_mps_info(sys.argv[2])
  variants_with_annot = pd.merge(mps_info, variants, on = ["Gene", "P."], how = "inner")
  results = variants_with_annot[["Chrom", "Position", "Reference", "Alternate", "P.", "MType", "Func", "Author", "Paper"]]
  results = results.fillna("-")
  results.columns = ["Chrom", "Start", "Ref", "Alt", "p.MPS1", "mtype.MPS1", "func.MPS1", "author.MPS1", "paper.MPS1"]
  print(results.to_csv(index = False, sep = "\t"))
