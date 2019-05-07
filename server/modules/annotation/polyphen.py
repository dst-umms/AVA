#!/usr/bin/env python

#-----------------------
# @title: emv.py
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: May, 6, 2019
#-----------------------

import pandas as pd
import sys

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
  if info:
    info.append([row.Chrom, row.Position, row.Reference, row.Alternate, 
      "c." + df.CPosition + df.Reference + ">" + df.Alternate, 
      "p." + df.PPosition + df.PReference + ">" + df.PAlternate, df.Prediction,
      df.DScore, df.HDivPrediction, df.HDivProb, df.HVarPrediction, df.HVarProb ])


def get_annotation(poly_info, variants):
  results = []
  for index in variants.index:
    df.apply(lambda row: check_annotation(row, poly_info, results), axis = 1)  
  results = pd.DataFrame(results, columns = [
    "Chrom", "Start", "Ref", "Alt", "c.Polyphen", "p.Polyphen",
    "func.Polyphen", "dscore.Polyphen", "func_hdiv.Polyphen", "prob_hdiv.Polyphen",
    "func_hvar.Polyphen", "prob_hvar.Polyphen"
  ])
  return results

if __name__ == "__main__":
  variants = pd.read_csv(sys.argv[1], header = None, sep = "\t")
  variants.columns = ["Chrom", "Position", "Start_Alt", "Reference", "Alternate", "Gene", "RunID", "SpecID", "C.", "Comments"]
  variants["Chrom"] = variants["Chrom"].astype(str)
  poly_info = get_poly_info(sys.argv[2])
  results = get_annotation(poly_info, variants) 
  results = results.fillna("-")
  print(results.to_csv(index = False, sep = "\t"))
