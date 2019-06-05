#!/usr/bin/env python

#-----------------------
# @title: gnomad.py
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: Aug, 6, 2018
#-----------------------

import pandas as pd
import sys

def get_gnomad_info(gnomad_annot_file):
  df = pd.read_csv(gnomad_annot_file, header = 0, sep = ",")
  return df

if __name__ == "__main__":
  variants = pd.read_csv(sys.argv[1], header = None, sep = "\t")
  variants.columns = ["Chrom", "Position", "Start_Alt", "Reference", "Alternate", "Gene", "RunID", "SpecID", "C.", "P._In", "Comments"]
  variants["Chrom"] = variants["Chrom"].astype(str)
  gnomad_info = get_gnomad_info(sys.argv[2])
  variants.loc[variants.Reference == '-', "Reference"] = '.'
  variants.loc[variants.Alternate == '-', "Alternate"] = '.'
  results = pd.merge(gnomad_info, variants, on = ["Chrom", "Position", "Reference", "Alternate"], how = "right") 
  results = results[["Chrom", "Position", "Reference", "Alternate", "Protein Consequence", 
    "Transcript Consequence", "Annotation", "Allele Frequency", "RSID", "Gene", "RunID", "SpecID", "C.", "Comments"]] 
  results.columns = ["Chrom", "Start", "Ref", "Alt", "p.gnomad", "c.gnomad", "func.gnomad", "AF.gnomad", "rs.gnomad", "Gene", 
    "RunID", "SpecID", "C.", "Comments"]
  results = results.fillna("-")
  print(results.to_csv(index = False, sep = "\t"))
