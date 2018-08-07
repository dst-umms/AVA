#!/usr/bin/env python

#-----------------------
# @title: ald.py
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: Aug, 7, 2018
#-----------------------

import pandas as pd
import sys

def get_ald_info(ald_annot_file):
  df = pd.read_csv(ald_annot_file, header = 0, sep = "\t")
  df.columns = ["Position", "Variant", "Consequence", "Exon", "Remark"]
  df["Chrom"] = "X"
  return df

if __name__ == "__main__":
  variants = pd.read_csv(sys.argv[1], header = None, sep = "\t")
  ald_info = get_ald_info(sys.argv[2])
  variants.columns = ["Chrom", "Position", "Start_Alt", "Reference", "Alternate", "Comments"]
  variants_with_annot = pd.merge(ald_info, variants, on = ["Chrom", "Position"], how = "inner")
  results = variants_with_annot[["Chrom", "Position", "Reference", "Alternate", 
    "Variant", "Consequence", "Exon", "Remark"]]
  results = results.fillna("-")
  results.columns = ["Chrom", "Start", "Ref", "Alt", "c.ALD", "p.ALD", "Exon.ALD", "Remark.ALD"]
  print(results.to_csv(index = False, sep = "\t"))
