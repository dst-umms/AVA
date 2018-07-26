#!/usr/bin/env python
import re

content = open('abcd1_ald.db', 'r').read().split('\n')
info, process_info = [], []
for item in content[1:]:
  if item[0:2] == '15':
    info.append(item)
  else:
    info[len(info)-1] += item

for item in info:
  # with c. and p.
  match_obj = re.search('(15\d+)\s+(c\..+)\s+(p\..+)\s+(exon\s+\d+|\d.\s+UTR|IVS\s+\d+)\s+(.+)', item)
  if match_obj:
    chr_pos = match_obj.group(1)
    c_dot = match_obj.group(2)
    p_dot = match_obj.group(3) or '-'
    func = match_obj.group(4) or '-'
    desc = match_obj.group(5) or '-' 
    process_info.append('\t'.join([chr_pos, c_dot, p_dot, func, desc]))
  else:
    match_obj = re.search('(15\d+)\s+(c\..+)\s+(exon\s+\d+|\d.\s+UTR|IVS\s+\d+)\s+(.+)', item)
    if match_obj:
      chr_pos = match_obj.group(1)
      c_dot = match_obj.group(2)
      p_dot = '-'
      func = match_obj.group(3) or '-'
      desc = match_obj.group(4) or '-'
      process_info.append('\t'.join([chr_pos, c_dot, p_dot, func, desc]))
    else:
      print('\t'.join(item.split(' ')) + '\n')

with open('result.db', 'w') as ofh:
  ofh.write('\t'.join(["Chromosome_position", "Variant", "Consequence", "Exon", "Remark"]) + '\n')
  for val in process_info:
    ofh.write(val + '\n')
