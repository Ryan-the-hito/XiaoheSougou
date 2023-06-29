#!/usr/bin/env python3
import codecs

text = codecs.open("/Users/ryanshenefield/Downloads/test.txt", 'r', encoding='utf-8').read()
textline = text.split('\n')
while '' in textline:
    textline.remove('')
newline = []
for i in range(len(textline)):
    part = textline[i].split(',')[0]
    if len(part) == 4:
        newline.append(textline[i])
newtext = '\n'.join(newline)
with open("/Users/ryanshenefield/Downloads/newtext.txt", 'w', encoding='utf-8') as f0:
    f0.write(newtext)