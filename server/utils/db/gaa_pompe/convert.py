#!/usr/bin/env python

#vim: syntax on
#vim: set tabstop=2 expandtab

import sys
import re

def convert_to_csv(info):
  for line in info[1:]: #[0] has header
    line = line.strip()
    matchobj = re.search("(.+?)\s+(c\..+?)\s+([p|r]\..+?)\s+(.+?)\s+(\d.+?)\s+(.+)", line)
    if matchobj:
      sys.stdout.write(','.join(matchobj.groups()) + '\n')
    else:
      matchobj = re.search("(.+?)\s+(c\..+?)\s+(.+?)\s{2,}(.+?)\s+(\d+)\s+(.+)", line)
      if matchobj:
        sys.stdout.write(','.join(matchobj.groups()) + '\n')
      else:
        matchobj = re.search("(.+?)\s+(c\..+?)\s+(splice site|splice defect|\?)\s+(.+?)\s+(\d+)\s+(.+)", line)
        if matchobj:
          sys.stdout.write(','.join(matchobj.groups()) + '\n')
        else:
          matchobj = re.search("(.+?)\s+\[(c\..+?)\]\s+(p\..+?)\s+(.+?)\s+(\d+)\s+(.+)", line)
          if matchobj:
            (loc, cdot, pdot, func, year, source) = matchobj.groups()
            for ind_cdot in cdot.split(';'):
              sys.stdout.write(','.join([loc, ind_cdot, pdot, func, year, source]) + '\n')
          else:
            sys.stderr.write(line + '\n')

if __name__ == '__main__':
  infile = sys.argv[1]
  convert_to_csv(open(infile, 'r').readlines())
