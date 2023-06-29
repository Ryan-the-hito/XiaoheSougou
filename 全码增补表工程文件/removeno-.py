#!/usr/bin/env python3

import codecs

text = codecs.open('/Users/ryanshenefield/Downloads/newtest.txt', 'r', encoding='utf-8').read()
textline = text.split('},')
while '' in textline:
    textline.remove('')
newline = []
for i in range(len(textline)):
    if '-' in textline[i]:
        newline.append(textline[i])
newtext = '\n'.join(newline)
with open('/Users/ryanshenefield/Downloads/newnewtest.txt', 'w', encoding='utf-8') as f0:
    f0.write(newtext)