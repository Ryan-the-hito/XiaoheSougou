#!/usr/bin/env python3

import re
import codecs

text = codecs.open('/Users/ryanshenefield/Downloads/NewFile.txt', 'r', encoding='utf-8').read()
textlist = text.split("\n")
while '' in textlist:
    textlist.remove('')
for i in range(len(textlist)):
    celllist = textlist[i].split(",")
    textlist[i] = celllist[1] + '\t' + celllist[0] + '\t' + '1'
a = '\n'.join(textlist)
#a = re.sub(r'"order"[\s\S]*?},', '},', text)
with open('/Users/ryanshenefield/Downloads/NewFile2.txt', 'w', encoding='utf-8') as f0:
    f0.write(a)