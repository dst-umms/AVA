#!/usr/bin/env python
#vim: syntax=python tabstop=2 expandtab

rule target:
  input:
    "/usr/local/bin/analysis/{proj_name}/{proj_name}.txt".format(proj_name = config["proj_name"])


rule copy_text:
  input:
    "/usr/local/bin/analysis/input/{proj_name}.txt".format(proj_name = config["proj_name"])
  output:
    "/usr/local/bin/analysis/{proj_name}/{proj_name}.txt".format(proj_name = config["proj_name"])
  shell:
    "sleep 20 && cat {input} 1>{output}"
