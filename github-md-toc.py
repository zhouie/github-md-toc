#!/usr/bin/env python

import re
import sys

tablen = 4
if len(sys.argv) == 3:
    tablen = int(sys.argv[2])

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

for line in lines:
    matches = re.findall(r'(^#{1,6}) (.*)', line)
    if matches:
        h_level = len(matches[0][0])
        h_title = matches[0][1].strip()
        indent = ' ' * (tablen * (h_level - 1))
        md_link = re.sub(r' ', '-', re.sub(r'[^\d\w ]', '', h_title)).lower()
        print(('%s*%s[%s](#%s)') % (indent, ' ' * tablen, h_title, md_link))
