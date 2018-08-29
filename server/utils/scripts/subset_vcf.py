#!/usr/bin/env python

#-------------------------
# @author: Mahesh Vangala
# @date: Aug, 29, 2019
# @title: subset_vcf.py
#-------------------------

import sys

def print_subset_vcf(vcf_file, chrom_list):
  with open(vcf_file, 'r') as fh:
    for line in fh:
      if line[0] == '#' or line[0] in chrom_list:
        print(line, end = "")

if __name__ == '__main__':
  print_subset_vcf(sys.argv[1], ['4', 'X', '17'])
