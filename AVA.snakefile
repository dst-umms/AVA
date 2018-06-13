#!/usr/bin/env python
#vim: syntax=python tabstop=2 expandtab

rule target:
  input:
    "/usr/local/bin/analysis/{proj_name}/{proj_name}.intervar".format(proj_name = config["proj_name"])


rule run_intervar:
  input:
    expand("/usr/local/bin/analysis/input/{proj_name}.txt", proj_name = lambda wildcards: wildcards.proj_name)
  output:
    "/usr/local/bin/analysis/{proj_name}/{proj_name}.intervar"
  params:
    intervar_out = lambda wildcards : "/usr/local/bin/analysis/{proj_name}/{proj_name}".format(proj_name = wildcards.proj_name)
  shell:
    "source activate INTERVAR "
    "cd /usr/local/bin/Intervar "
    "./Intervar.py -i {input} --input-type AVinput "
