#!/usr/bin/env python
#vim: syntax=python tabstop=2 expandtab

rule target:
  input:
    "/usr/local/bin/analysis/{proj_name}/{proj_name}.intervar".format(proj_name = config["proj_name"])


rule run_intervar:
  input:
    expand("/usr/local/bin/analysis/input/{proj_name}.txt", proj_name = config["proj_name"])
  output:
    "/usr/local/bin/analysis/{proj_name}/{proj_name}.intervar"
  params:
    intervar_out = lambda wildcards : "/usr/local/bin/analysis/{proj_name}/{proj_name}".format(proj_name = wildcards.proj_name)
  shell:
    "source activate INTERVAR && "
    "/usr/local/bin/Intervar/Intervar.py -b hg19 -i {input} --input_type AVinput -o {params.intervar_out} "
    "-t /usr/local/bin/Intervar/intervardb --table_annovar=/usr/local/bin/annovar/table_annovar.pl "
    "--convert2annovar=/usr/local/bin/annovar/convert2annovar.pl --annotate_variation=/usr/local/bin/annovar/annotate_variation.pl "
    "-d /usr/local/bin/annovar/humandb "
