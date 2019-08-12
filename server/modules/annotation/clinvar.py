#!/usr/bin/env python

#-----------------------
# @title: clinvar.py
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: Aug, 28, 2018
#-----------------------

import pandas as pd
import vcf
import sys
import re
from collections import defaultdict

def get_clinvar_info(clinvar_annot_file):
  vcf_reader = vcf.Reader(open(clinvar_annot_file, 'r'))
  d = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(dict))))
  re_obj = re.compile(".+\|(.+)")
  for row in vcf_reader:
    alt_list = list(row.ALT)
    hgvs_list = list(row.INFO["CLNHGVS"])
    sig_list = list(row.INFO["CLNSIG"]) if "CLNSIG" in row.INFO else []
    mc_list = [re_obj.search(x).group(1) for x in list(row.INFO["MC"])] if "MC" in row.INFO else [] 
    rs_list = ['rs' + str(rs_num) for rs_num in list(row.INFO["RS"])] if "RS" in row.INFO else []
    clnvc = row.INFO["CLNVC"] if "CLNVC" in row.INFO.keys() else None
    for idx in range(0, len(alt_list)):
      d[row.CHROM][row.POS][row.REF][repr(alt_list[idx])] = {
        "CLNHGVS": hgvs_list[idx] if hgvs_list else None 
        , "CLNSIG": sig_list[idx] if sig_list else None
        , "MC": mc_list[idx] if mc_list else None
        , "RS": rs_list[idx] if rs_list else None
        , "CLNVC": clnvc
      }
  return d

def add_clinvar_info(clinvar_info, variants):
  info = []
  for index, row in variants.iterrows():
    try:
      d = clinvar_info[row["Chrom"]][row["Position"]][row["Reference"]][row["Alternate"]]
      cur_info = [row["Chrom"], row["Position"], row["Reference"], row["Alternate"], d["CLNHGVS"], d["CLNSIG"], d["MC"], d["RS"], 
        d["CLNVC"]]
      info.append(cur_info)
    except KeyError:
      pass
  df = pd.DataFrame(info, columns = ["Chrom", "Start", "Ref", "Alt", "clinvar.HGVS", "clinvar.SIG", "clinvar.MC", "clinvar.RS", 
    "clinvar.VC"])
  return df

if __name__ == "__main__":
  variants = pd.read_csv(sys.argv[1], header = None, sep = "\t")
  variants.columns = ["Chrom", "Position", "Start_Alt", "Reference", "Alternate", "Gene", "RunID", "SpecID", "C.", "P.", "Comments"]
  variants["Chrom"] = variants["Chrom"].astype(str)
  clinvar_info = get_clinvar_info(sys.argv[2])
  results = add_clinvar_info(clinvar_info, variants)
  results = results.fillna("-")
  print(results.to_csv(index = False, sep = "\t"))
