#!/usr/bin/env python

#-----------------------
# @title: sift.py
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: Jun, 17, 2019
#-----------------------

import pandas as pd
import sys
from server.utils.scripts.AAs import aa_1_to_3 as aa

def get_sift_info(sift_annot_file):
  df = pd.read_csv(sift_annot_file, header = 0, sep = ",")
  df.columns = ["Chrom", "Position", "Reference", "Alternate", "AAPos", "AA1", "AA2", "Region", "Func", "RSID", "Score"]
  df.Chrom = df.Chrom.str[3:] # remove chr letters
  df["P."] = "p." + df["AAPos"].astype("str") + aa[df["AA1"].upper()] + ">" + aa[df["AA2"].upper()] 
  return df

if __name__ == "__main__":
  variants = pd.read_csv(sys.argv[1], header = None, sep = "\t")
  variants.columns = ["Chrom", "Position", "Start_Alt", "Reference", "Alternate", "Gene", "RunID", "SpecID", "C.", "P.In", "Comments"]
  variants["Chrom"] = variants["Chrom"].astype(str)
  sift_info = get_sift_info(sys.argv[2])
  variants_with_annot = pd.merge(sift_info, variants, on = ["Chrom", "Position", "Reference", "Alternate"], how = "inner")
  results = variants_with_annot[["Chrom", "Position", "Reference", "Alternate", "P.", "Func", "RSID", "Score"]]
  results = results.fillna("-")
  results.columns = ["Chrom", "Start", "Ref", "Alt", "p.SIFT", "func.SIFT", "rs.SIFT", "score.SIFT"]
  print(results.to_csv(index = False, sep = "\t"))
