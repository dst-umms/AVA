#!/usr/bin/env python

#vim: syntax on
#vim: set tabstop=2 expandtab

import sys
import re

def convert_to_csv(info):
  for line in info[1:]: #[0] has header
    line = line.strip()
    matchobj = re.search("\d+\s+(.+?)\s+(\w+\smutation)\s+(.+?)\s+(.+?)\s{2,}(\S+\s\S+)\s+(.+?)\s{2,}[A-Z]\s+", line)
    if matchobj:
      sys.stdout.write(','.join(matchobj.groups()) + '\n')
    else:
      sys.stderr.write(line + '\n')

if __name__ == '__main__':
  infile = sys.argv[1]
  convert_to_csv(open(infile, 'r').readlines())
