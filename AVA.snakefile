#!/usr/bin/env python
#vim: syntax=python tabstop=2 expandtab

def get_intervar_input(wildcards):
  if config["file_format"] == 'vcf':
    return "input/{proj_name}.vcf".format(proj_name = config["proj_name"])
  else:
    return "input/{proj_name}.txt".format(proj_name = config["proj_name"])
    

rule target:
  input:
    #"output/{proj_name}.hg19_multianno.txt.intervar".format(proj_name = config["proj_name"])
    "output/{proj_name}.gnomad.tsv".format(proj_name = config["proj_name"])
    , "output/{proj_name}.ald.tsv".format(proj_name = config["proj_name"])
    , "output/{proj_name}.final.tsv".format(proj_name = config["proj_name"])

rule convert_nenbss_to_annovar:
  input:
    expand("input/{proj_name}.csv", proj_name = config["proj_name"])    
  output:
    "input/{proj_name}.txt"
  shell:
    "/usr/local/bin/miniconda3/bin/python /usr/local/bin/AVA/server/modules/file_conversion/nenbss_to_annovar.py "
    "{input} 1>{output}"

rule run_intervar:
  input:
    get_intervar_input
  output:
    "output/{proj_name}.hg19_multianno.txt.intervar"
  params:
    intervar_out = lambda wildcards : "output/{proj_name}".format(proj_name = wildcards.proj_name),
    file_format = "AVinput" if config["file_format"] in ["txt", "csv"] else "VCF"
  shell:
    ". activate INTERVAR && "
    "/usr/local/bin/Intervar/Intervar.py -b hg19 -i {input} --input_type {params.file_format} -o {params.intervar_out} "
    "-t /usr/local/bin/Intervar/intervardb --table_annovar=/usr/local/bin/annovar/table_annovar.pl "
    "--convert2annovar=/usr/local/bin/annovar/convert2annovar.pl --annotate_variation=/usr/local/bin/annovar/annotate_variation.pl "
    "-d /usr/local/bin/annovar/humandb "

rule get_gnomad_annotation:
  input:
    get_intervar_input
    , "/usr/local/bin/AVA/server/utils/db/gnomad/gnomad_2018_08_01.csv"
  output:
    "output/{proj_name}.gnomad.tsv"
  shell:
    "/usr/local/bin/miniconda3/bin/python /usr/local/bin/AVA/server/modules/annotation/gnomad.py "
    "{input} 1>{output}"

rule get_ald_annotation:
  input:
    get_intervar_input
    , "/usr/local/bin/AVA/server/utils/db/abcd1_ald/result.db"
  output:
    "output/{proj_name}.ald.tsv"
  shell:
    "/usr/local/bin/miniconda3/bin/python /usr/local/bin/AVA/server/modules/annotation/ald.py "
    "{input} 1>{output}"

rule merge_annotation:
  input:
    expand("output/{proj_name}.{ext}", proj_name = config["proj_name"], ext = ["gnomad.tsv", "ald.tsv"])
  output:
    "output/{proj_name}.final.tsv"
  shell:
    "/usr/local/bin/miniconda3/bin/python /usr/local/bin/AVA/server/modules/annotation/merge_annot.py "
    "{input} 1>{output}"
