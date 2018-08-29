#!/usr/bin/env python

#-----------------------
# @title: dbsnp.py
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: Aug, 29, 2018
#-----------------------

import pandas as pd
import vcf
import sys
import re
from collections import defaultdict

def get_dbsnp_info(dbsnp_annot_file, variant_info):
  vcf_reader = vcf.Reader(open(dbsnp_annot_file, 'r'))
  d = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(dict))))
  chrom_list = list(variant_info.Chrom.drop_duplicates())
  pos_list = list(variant_info.Position.drop_duplicates())
  for row in vcf_reader:
    if row.CHROM in chrom_list and row.POS in pos_list:
      alt_list = list(row.ALT)
      caf_list = list(row.INFO["CAF"]) if "CAF" in row.INFO else []
      rs_id = 'rs' + str(row.INFO["RS"]) if "RS" in row.INFO else None
      for idx in range(0, len(alt_list)):
        d[row.CHROM][row.POS][row.REF][repr(alt_list[idx])] = {
          "CAF": caf_list[idx] if caf_list else None
          , "RS": rs_id
        }
  return d

def add_dbsnp_info(dbsnp_info, variants):
  info = []
  for index, row in variants.iterrows():
    try:
      d = dbsnp_info[row["Chrom"]][row["Position"]][row["Reference"]][row["Alternate"]]
      cur_info = [row["Chrom"], row["Position"], row["Reference"], row["Alternate"], d["RS"], d["CAF"]]
      info.append(cur_info)
    except KeyError:
      pass
  df = pd.DataFrame(info, columns = ["Chrom", "Start", "Ref", "Alt", "dbsnp.RS", "dbsnp.AF"])
  return df

if __name__ == "__main__":
  variants = pd.read_csv(sys.argv[1], header = None, sep = "\t")
  variants.columns = ["Chrom", "Position", "Start_Alt", "Reference", "Alternate", "Comments"]
  dbsnp_info = get_dbsnp_info(sys.argv[2], variants)
  results = add_dbsnp_info(dbsnp_info, variants)
  results = results.fillna("-")
  print(results.to_csv(index = False, sep = "\t"))
