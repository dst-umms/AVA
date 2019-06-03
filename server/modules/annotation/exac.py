#!/usr/bin/env python

#-----------------------
# @title: exac.py
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: Sep, 11, 2018
#-----------------------

import pandas as pd
import sys

def get_exac_info(exac_annot_file):
  df = pd.read_csv(exac_annot_file, header = 0, sep = ",")
  return df

if __name__ == "__main__":
  variants = pd.read_csv(sys.argv[1], header = None, sep = "\t")
  variants.columns = ["Chrom", "Position", "Start_Alt", "Reference", "Alternate", "Gene", "RunID", "SpecID", "C.", "P._In", "Comments"]
  variants["Chrom"] = variants["Chrom"].astype(str)
  variants["Position"] = variants["Position"].astype(str)
  exac_info = get_exac_info(sys.argv[2])
  variants.loc[variants.Reference == '-', "Reference"] = '.'
  variants.loc[variants.Alternate == '-', "Alternate"] = '.'
  results = pd.merge(exac_info, variants, on = ["Chrom", "Position", "Reference", "Alternate"], how = "right") 
  results = results[["Chrom", "Position", "Reference", "Alternate", "Protein Consequence", 
    "Transcript Consequence", "Annotation", "Allele Frequency", "RSID"]] 
  results.columns = ["Chrom", "Start", "Ref", "Alt", "p.ExAC", "c.ExAC", "func.ExAC", "AF.ExAC", "rs.ExAC"]
  results = results.fillna("-")
  print(results.to_csv(index = False, sep = "\t"))
