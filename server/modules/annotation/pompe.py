#!/usr/bin/env python

#-----------------------
# @title: pompe.py
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: May, 28, 2019
#-----------------------

import pandas as pd
import sys

def get_pompe_info(pompe_annot_file):
  df = pd.read_csv(pompe_annot_file, header = None, sep = ',')
  df.columns = ["Exon", "C.", "p.POMPE", "func.POMPE", "year.POMPE", "source.POMPE"]
  df["Chrom"] = "17"
  return df

if __name__ == "__main__":
  variants = pd.read_csv(sys.argv[1], header = None, sep = "\t")
  variants.columns = ["Chrom", "Position", "Start_Alt", "Reference", "Alternate", "Gene", "RunID", "SpecID", "C.", "Comments"]
  variants["Chrom"] = variants["Chrom"].astype(str)
  pompe_info = get_pompe_info(sys.argv[2])
  variants_with_annot = pd.merge(pompe_info, variants, on = ["Chrom", "C."], how = "inner")
  results = variants_with_annot[["Chrom", "Position", "Reference", "Alternate", 
    "C.", "p.POMPE", "func.POMPE", "year.POMPE", "source.POMPE"]]
  results = results.fillna("-")
  results.columns = ["Chrom", "Start", "Ref", "Alt", "c.POMPE", "p.POMPE", "func.POMPE", "year.POMPE", "source.POMPE"]
  print(results.to_csv(index = False, sep = "\t"))
