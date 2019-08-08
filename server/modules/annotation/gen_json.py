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
import yaml

SOURCE_INFO = yaml.safe_load(open("/usr/local/bin/AVA/server/utils/version/sources.yaml"))
FACT_INFO = yaml.safe_load(open("/usr/local/bin/AVA/server/utils/version/facts.yaml"))
VERSION_INFO = dict()
for source_obj in SOURCE_INFO["sources"]:
  VERSION_INFO[source_obj["SourceName"].lower()] = {
    "VersionName": source_obj["VersionName"],
    "VersionId": source_obj["VersionId"]
  }

def get_facts(info):
  facts = []
  for source_obj in SOURCE_INFO["sources"]:
    source_name = source_obj["SourceName"].lower()
    for fact_obj in FACT_INFO["facts"]:
      fact_name = fact_obj["FactName"].upper()
      col_name = fact_name + '.' + source_name
      if col_name in info and not info[col_name] == '-':
        facts.append({
          "FactLabel": col_name
          , "Name": fact_name
          , "FactValue": info[col_name]
          , "FactSource": {
            "Name": source_name
            , "VersionId": VERSION_INFO[source_name]["VersionId"]
            , "VersionName": VERSION_INFO[source_name]["VersionName"]
          }
        })
  return facts

def format_variant(info):
  if not len(info["Ref"]) == len(info["Alt"]) == 1:
    #raise "Only support single base substituions at the moment."
    pass
  variant = {
    "VariantLabel": info["Gene"].upper() + ':' + info["C."]
    , "C.": info["C."]
    , "RunID": info["RunID"]
    , "SpecID": info["SpecID"]
    , "Name": info["Ref"] + ">" + info["Alt"]
    , "Position": {
      "StartPosition": info["Start"]
    }
    , "Chromosome": {
      "ChromosomeLabel": info["Chrom"]
    }
    , "Gene": {
      "GeneName": info["Gene"]
      , "Chromosome": {
        "ChromosomeLabel": info["Chrom"]
      }
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
          "FactLabel": "FUNC.gnomad"
        }]
      }
    }]
  }
  variant["Facts"] = get_facts(info)
  return variant

def main(in_file):
  content = pd.read_csv(in_file, sep = "\t", header = 0)
  content.columns = ["Chrom", "Start", "Ref", "Alt", "P.gnomad", "C.gnomad", "MC.gnomad", "AF.gnomad", "RS.gnomad", "Gene", 
                    "RunID", "SpecID", "C.", "Comments", \
                    "C.ald", "P.ald", "LOCATION.ald", "FUNC.ald", "HGVS.clinvar", "FUNC.clinvar", "MC.clinvar", "RS.clinvar", "RS.dbsnp", \
                    "AF.dbsnp", "P.exac", "C.exac", "MC.exac", "AF.exac", "RS.exac", "C.emv", "P.emv" \
                    , "FUNC.emv", "REVIEW_DATE.emv", "C.polyphen", "P.polyphen",
                    "FUNC.polyphen", "DSCORE.polyphen", "FUNC_HDIV.polyphen", "PROB_HDIV.polyphen",
                    "FUNC_HVAR.polyphen", "PROB_HVAR.polyphen", "C.pompe", "P.pompe", "FUNC.pompe", "YEAR.pompe", "SOURCE.pompe",
                    "P.mps1", "MTYPE.mps1", "FUNC.mps1", "AUTHOR.mps1", "PAPER.mps1", "P.sift", "MC.sift", "RS.sift", "SCORE.sift"]
  content["Chrom"] = content["Chrom"].astype(str)
  variants = list(content.apply(lambda row: format_variant(row), axis = 1))
  print(json.dumps({ 
    "Variants": variants
  }))  

if __name__ == "__main__":
  main(sys.argv[1])
