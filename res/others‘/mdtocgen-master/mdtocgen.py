#!/usr/bin/env python

# Copyright 2017 Paolo Smiraglia <paolo.smiraglia@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
