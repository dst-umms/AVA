#!/usr/bin/env python

#-------------------------
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: July, 8, 2018
#-------------------------

import pandas as pd
import re
import sys

class NenbssToAnnovar():
  
  gaa_file = "../../utils/seqs/GAA.fa"
  idua_file = "../../utils/seqs/IDUA.fa"
  abcd1_file = "../../utils/seqs/ABCD1.fa"

  iupac = {
    'R': ['A', 'G'],
    'Y': ['C', 'T'],
    'K': ['G', 'T'],
    'M': ['A', 'C'],
    'S': ['G', 'C'],
    'W': ['A', 'T']
    #, 'B': ['C', 'G', 'T']
    #, 'D': ['A', 'G', 'T']
    #, 'H': ['A', 'C', 'T']
    #, 'V': ['A', 'C', 'G']
  }

  def __init__(self):
    (self.gaa_chr_info, self.gaa_gene_info) = self.__get_fasta_seq(NenbssToAnnovar.gaa_file)
    (self.idua_chr_info, self.idua_gene_info) = self.__get_fasta_seq(NenbssToAnnovar.idua_file)
    (self.abcd1_chr_info, self.abcd1_gene_info) = self.__get_fasta_seq(NenbssToAnnovar.abcd1_file)
    self.re_obj = re.compile(r'(\w+)-')

  def __get_fasta_seq(self, fa_file):
    chr_info, gene_info = None, None
    with open(fa_file, 'r') as fh:
      chr_info = ':'.join(re.search("range=chr(.+):(\d+)-(\d+)", fh.readline()).groups())
      gene_info = fh.read()
      gene_info = gene_info.replace('\n', '')
    if not (chr_info or gene_info):
      raise "Error in getting chromosome and/or fasta sequence"
    return (chr_info, gene_info.upper())

  def __get_iupac_base(self, iupac_base, ref):
    iupac = NenbssToAnnovar.iupac
    if iupac_base in iupac.keys():
      result = ''.join(set(iupac[iupac_base]) - set([ref]))
      return result
      if len(result) > 1:
        raise str(len(result)) + ' bases found for given IUPAC code: ' + iupac_base + ' --> ' + result
      else:
        return result
    else:
      raise iupac_base + ' not found in iupac table: ' + ','.join(iupac.keys())

  def nenbss_to_annovar(self, nenbss_file):
    df = pd.read_csv(nenbss_file, header = 0, sep = ",")
    annovar_info = []
    for index in df.index:
      gene_name = self.re_obj.search(df["Project Name"][0]).group(1) 
      if gene_name.upper() == 'MPS1':
        gene_info = self.idua_gene_info
        (chrom, start, end) = self.idua_chr_info.split(':')
      (var_info, base_info) = df[["Variant ID", "Base Position"]][df.index == index].values[0]
      (ref, alt_iupac) = [this_base.upper() for this_base in var_info[-3:].split('>')]
      alt = alt_iupac if (alt_iupac in ['A', 'G', 'C', 'T']) else self.__get_iupac_base(alt_iupac, ref) 
      annovar_info.append([str(chrom), str(int(start) + int(base_info) - 1), str(int(start) + int(base_info) - 1), ref, alt, 'comments: ' + 
        ';'.join([str(val) for val in df[df.index == index].values[0]])])
    return annovar_info


if __name__ == "__main__":
  n = NenbssToAnnovar()
  print(pd.DataFrame(n.nenbss_to_annovar(sys.argv[1])).to_csv(sep = "\t", index = None, header = None)) 
