#!/usr/bin/env python

#-----------------------
# @title: emv.py
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: May, 6, 2019
#-----------------------

import pandas as pd
import sys

def get_emv_info(emv_annot_file):
  df = pd.read_csv(emv_annot_file, header = 0, sep = ",")
  df.columns = ["Order", "Gene", "_", "Exon", "Nuc", "Prot", "Class", "Review", "Alias"]
  df = df.where((pd.notnull(df)), None)
  df.loc[df["Review"] == "**"]["Review"] = "06/15/2012"
  df["C."] = df.apply(lambda x: x["Nuc"].split(":")[1], 1)
  df["P."] = df.apply(lambda x: x["Prot"].split("|")[0].strip() if x["Prot"] else "None", 1)
  df = df[["Gene", "C.", "P.", "Class", "Review"]] 
  return df

if __name__ == "__main__":
  variants = pd.read_csv(sys.argv[1], header = None, sep = "\t")
  variants.columns = ["Chrom", "Position", "Start_Alt", "Reference", "Alternate", "Gene", "RunID", "SpecID", "C.", "Comments"]
  variants["Chrom"] = variants["Chrom"].astype(str)
  emv_info = get_emv_info(sys.argv[2])
  variants_with_annot = pd.merge(emv_info, variants, on = ["Gene", "C."], how = "inner")
  results = variants_with_annot[["Chrom", "Position", "Reference", "Alternate", 
    "C.", "P.", "Class", "Review"]]
  results = results.fillna("-")
  results.columns = ["Chrom", "Start", "Ref", "Alt", "c.EMV", "p.EMV", "class.EMV", "review.EMV"]
  print(results.to_csv(index = False, sep = "\t"))
