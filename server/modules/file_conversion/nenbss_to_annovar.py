#!/usr/bin/env python

#-------------------------
# @author: Mahesh Vangala
# @email: vangalamaheshh@gmail.com
# @date: July, 8, 2018
#-------------------------

import pandas as pd
import re
import sys
from server.utils.scripts.AAs import aa_3_to_1, aa_1_to_3 

class NenbssToAnnovar():
  
  gaa_file = "/usr/local/bin/AVA/server/utils/seqs/GAA.fa"
  idua_file = "/usr/local/bin/AVA/server/utils/seqs/IDUA.fa"
  abcd1_file = "/usr/local/bin/AVA/server/utils/seqs/ABCD1.fa"

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

  def __format_pdot(self, p_dot):
    match_obj = re.search("p\.(\D+)(\d+)\[(\w+),(\w+)\]", p_dot)
    if not match_obj:
      match_obj = re.search("p\.(\D+)(\d+)(\D+)", p_dot)
      if not match_obj:
        raise "Error in parsing p dot from " + p_dot
      (ref, pos, alt) = match_obj.groups()
      ref = ref.upper() if len(ref) == 3 else aa_1_to_3[ref.upper()]
      alt = alt.upper() if len(alt) == 3 else aa_1_to_3[alt.upper()]
      return 'p.' + ref + pos + alt
    (ref, pos, r, a) = match_obj.groups()
    (ref, pos, r, a) = (ref.upper(), pos, r.upper(), a.upper())
    alt = a if ref == r else r
    return 'p.' + ref + pos + alt

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

  def __get_ref_and_alt_bases(self, var_info, base_info, gene_seq, zygosity):
    ins_info = var_info.split("INS")
    del_info = var_info.split("DEL")
    zygosity = "Homozygous" if str(zygosity).upper() == "YES" else "Heterozygous"
    if len(ins_info) > 1: # then it's insertion
      return (gene_seq[base_info - 1].upper(), ins_info[1], var_info, zygosity)
    elif len(del_info) > 1: # then it's deletion
      return (del_info[1], gene_seq[base_info - 1].upper(), var_info, zygosity)
    else:
      (ref, alt) = var_info[-3:].split('>')
      (alt, zygosity) = (alt, "Homozygous") if alt in ['A', 'G', 'C', 'T'] else (self.__get_iupac_base(alt, ref), "Heterozygous")
      return (ref, alt, var_info[:-1] + alt, zygosity)

  def nenbss_to_annovar(self, nenbss_file):
    df = pd.read_csv(nenbss_file, header = 0, sep = ",")
    header = list(df.columns)
    header[3] = "Specimen ID"
    df.columns = header
    annovar_info = []
    for index in df.index:
      gene_name = self.re_obj.search(df["Project Name"][index]).group(1) 
      gene_seq = None
      run_name = df["Project Name"][index]
      spec_name = df["Specimen ID"][index]
      c_dot = 'c' + re.split('\s+|:|;|,|\(', df["Variant ID"][index])[0].upper()[1:]
      p_dot = re.search("(p\.\S+)", df["Variant ID"][index])
      p_dot = self.__format_pdot(p_dot.group(1)) if p_dot else '.' 
      if gene_name.upper() in ['MPS1', 'IDUA']:
        (chrom, start, end) = self.idua_chr_info.split(':')
        gene_name = "IDUA"
        gene_seq = self.idua_gene_info
      elif gene_name.upper() in ['ALD18', 'ABCD1']:
        (chrom, start, end) = self.abcd1_chr_info.split(':')
        gene_name = "ABCD1"
        gene_seq = self.abcd1_gene_info
      elif gene_name.upper() in ['POMPE18', 'GAA']:
        (chrom, start, end) = self.gaa_chr_info.split(':')
        gene_name = "GAA"
        gene_seq = self.gaa_gene_info
      else:
        raise "Only POMPE (GAA), ALD (ABCD1) and MPS1 (IDUA) are supported. " + gene_name + " is not valid."
      base_info = df["Base Position"][index]
      if chrom == 'X' and base_info >= 13713: #see below comments about where this number comes from
        # A single base deletion happened at “13714” position (1-based counting).
        # We need to account for this by subtracting one more from this point on.
        if base_info == 13713: #this is exact position of base deletion, raise an error since we don't know how to deal with this
          raise "FATAL: The nucleotide at 13713 position is a deletion in ChrX."
        else:
          base_info = base_info - 1
      (ref, alt, c_dot, zygosity) = self.__get_ref_and_alt_bases(c_dot, base_info, gene_seq, df["Homozygous"][index])
      base_pos = int(start) + int(base_info) - 1 # 1 because the string is 0 based
      annovar_info.append([str(chrom), str(base_pos), ref, alt, gene_name, run_name, spec_name, c_dot, p_dot, zygosity, 'comments: '])
      #  ';'.join([str(val) for val in df[df.index == index].values[0]])])
    result_df = pd.DataFrame(annovar_info, columns = [
      "Chromosome", "Position", "Reference", "Alternate", "Gene", "Run_ID", "Specimen_ID", "C", "P", "Zygosity", "Comments"
    ])
    return result_df


if __name__ == "__main__":
  n = NenbssToAnnovar()
  print(pd.DataFrame(n.nenbss_to_annovar(sys.argv[1])).to_json(orient = 'records')) 
