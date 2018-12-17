#!/usr/bin/env python

#-----------------------
# @title: gnomad.py
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: Aug, 6, 2018
#-----------------------

import pandas as pd
import sys
import json

def get_facts(info):
  facts = []
  sources = ['p.gnomad', 'c.gnomad', 'func.gnomad', 'AF.gnomad', 'rs.gnomad']
  for source in sources:
    if not info[source] == '-':
      facts.append({
        "FactLabel": source
        , "Name": source.split(".")[0]
        , "FactValue": info[source]
        , "FactSource": {
          "Name": source.split(".")[1]
        }
      })
  return facts

def format_variant(info):
  if not len(info["Ref"]) == len(info["Alt"]) == 1:
    #raise "Only support single base substituions at the moment."
    pass
  variant = {
    "VariantLabel": info["Chrom"] + "_" + str(info["Start"]) + "_" + info["Ref"] + ">" + info["Alt"]
    , "Name": info["Ref"] + ">" + info["Alt"]
    , "Position": {
      "StartPosition": info["Start"]
    }
    , "Chromosome": {
      "ChromosomeLabel": info["Chrom"]
    }
    , "Interpretations": [{
      "Classification": {
        "ClassificationLabel": "TBD"
      }
      , "Interpreter": {
        "InterpreterName": "AVA"
        , "InterpreterType": "Software-Automation"
      }
      , "Evidence": {
        "Facts": [{
          "FactLabel": "func.gnomad"
        }]
      }
    }]
  }
  variant["Facts"] = get_facts(info)
  return variant

def main(in_file):
  content = pd.read_csv(in_file, sep = "\t", header = 0)
  variants = list(content.apply(lambda row: format_variant(row), axis = 1))
  print(json.dumps({ 
    "Variants": variants
  }))  

if __name__ == "__main__":
  main(sys.argv[1])
