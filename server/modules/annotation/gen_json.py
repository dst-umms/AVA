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

VERSION_INFO = {
  "gnomad": {
    "VersionName": "v2",
    "VersionId": "2019_04_19"
  }, "ald": {
    "VersionName": "v1",
    "VersionId": "2018_07_26"
  } , "clinvar": {
    "VersionName": "v1",
    "VersionId": "2018_07_01"
  }, "dbsnp": {
    "VersionName": "v1",
    "VersionId": "2018_04_23"
  }, "exac": {
    "VersionName": "v1",
    "VersionId": "2018_09_11"
  }, "emv": {
    "VersionName": "v1",
    "VersionId": "2019_05_06"
  }, "polyphen": {
    "VersionName": "v1",
    "VersionId": "2019_05_07"
  }
}

def get_facts(info):
  facts = []
  sources = ['P.gnomad', 'C.gnomad', 'FUNC.gnomad', 'AF.gnomad', 'RS.gnomad', 'C.ald', 'P.ald', 'EXON.ald', \
            'REMARK.ald', 'HGVS.clinvar', 'SIG.clinvar', 'MC.clinvar', 'RS.clinvar', 'RS.dbsnp', 'AF.dbsnp', 'P.exac', \
            'C.exac', 'FUNC.exac', 'AF.exac', 'RS.exac', 'C.emv', 'P.emv', 'SIG.emv', 'REVIEW_DATE.emv',
            "C.polyphen", "P.polyphen",
            "FUNC.polyphen", "DSCORE.polyphen", "FUNC_HDIV.polyphen", "PROB_HDIV.polyphen",
            "FUNC_HVAR.polyphen", "PROB_HVAR.polyphen"            
          ]
  for source in sources:
    if not info[source] == '-':
      facts.append({
        "FactLabel": source
        , "Name": source.split(".")[0]
        , "FactValue": info[source]
        , "FactSource": {
          "Name": source.split(".")[1]
          , "VersionId": VERSION_INFO[source.split(".")[1]]["VersionId"]
          , "VersionName": VERSION_INFO[source.split(".")[1]]["VersionName"]
        }
      })
  return facts

def format_variant(info):
  if not len(info["Ref"]) == len(info["Alt"]) == 1:
    #raise "Only support single base substituions at the moment."
    pass
  variant = {
    "VariantLabel": info["Chrom"] + "_" + str(info["Start"]) + "_" + info["Ref"] + ">" + info["Alt"]
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
  content.columns = ["Chrom", "Start", "Ref", "Alt", "P.gnomad", "C.gnomad", "FUNC.gnomad", "AF.gnomad", "RS.gnomad", "Gene", 
                    "RunID", "SpecID", "C.", "Comments", \
                    "C.ald", "P.ald", "EXON.ald", "REMARK.ald", "HGVS.clinvar", "SIG.clinvar", "MC.clinvar", "RS.clinvar", "RS.dbsnp", \
                    "AF.dbsnp", "P.exac", "C.exac", "FUNC.exac", "AF.exac", "RS.exac", "C.emv", "P.emv" \
  , "SIG.emv", "REVIEW_DATE.emv", "C.polyphen", "P.polyphen",
    "FUNC.polyphen", "DSCORE.polyphen", "FUNC_HDIV.polyphen", "PROB_HDIV.polyphen",
    "FUNC_HVAR.polyphen", "PROB_HVAR.polyphen"]
  content["Chrom"] = content["Chrom"].astype(str)
  variants = list(content.apply(lambda row: format_variant(row), axis = 1))
  print(json.dumps({ 
    "Variants": variants
  }))  

if __name__ == "__main__":
  main(sys.argv[1])
