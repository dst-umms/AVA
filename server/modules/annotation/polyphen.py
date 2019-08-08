#!/usr/bin/env python

#-----------------------
# @title: emv.py
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: May, 6, 2019
#-----------------------

import pandas as pd
import sys
import os
sys.path.append(os.path.abspath("/usr/local/bin/AVA"))
from server.utils.scripts.AAs import aa_1_to_3 as aa

def get_poly_info(poly_annot_file):
  df = pd.read_csv(poly_annot_file, header = 0, sep = ",")
  df.columns = ['Chrom', 'Position', 'Gene', 'CPosition', 'Reference', 'Alternate'
        , 'PPosition', 'PReference', 'PAlternate',
       'Prediction', 'DScore', 'HDivPrediction', 'HDivProb',
       'HVarPrediction', 'HVarProb']
  return df

def check_annotation(row, df, results):
  info = df.loc[(df.Chrom == 'chr' + row.Chrom) & (df.Position == row.Position) &
    (df.Reference == row.Reference) & (df.Alternate == row.Alternate)]
  if not info.empty:
    info = list(info.values[0])
    results.append([row.Chrom, info[1], info[4], 
      info[5], "c." + str(info[3]) + info[4]
      + ">" + info[5], "p." + aa[info[7].upper()].capitalize() + str(info[6]) + aa[info[8].upper()].capitalize(), 
      info[9], info[10], info[11], 
      info[12], info[13], info[14]])

def get_annotation(poly_info, variants):
  results = []
  variants.apply(lambda row: check_annotation(row, poly_info, results), axis = 1)  
  results = pd.DataFrame(results, columns = [
    "Chrom", "Start", "Ref", "Alt", "c.Polyphen", "p.Polyphen",
    "func.Polyphen", "dscore.Polyphen", "func_hdiv.Polyphen", "prob_hdiv.Polyphen",
    "func_hvar.Polyphen", "prob_hvar.Polyphen"
  ])
  return results

if __name__ == "__main__":
  variants = pd.read_csv(sys.argv[1], header = None, sep = "\t")
  variants.columns = ["Chrom", "Position", "Start_Alt", "Reference", "Alternate", "Gene", "RunID", "SpecID", "C.", "P._In", "Comments"]
  variants["Chrom"] = variants["Chrom"].astype(str)
  poly_info = get_poly_info(sys.argv[2])
  results = get_annotation(poly_info, variants) 
  results = results.fillna("-")
  print(results.to_csv(index = False, sep = "\t"))
