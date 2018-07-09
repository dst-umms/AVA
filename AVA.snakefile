#!/usr/bin/env python
#vim: syntax=python tabstop=2 expandtab

def get_intervar_input(wildcards):
  if config["file_format"] == 'vcf':
    return "input/{proj_name}.vcf".format(proj_name = config["proj_name"])
  else:
    return "input/{proj_name}.txt".format(proj_name = config["proj_name"])
    

rule target:
  input:
    "output/{proj_name}.hg19_multianno.txt.intervar".format(proj_name = config["proj_name"])

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
