#!/usr/bin/env python3

import re
import codecs

text = codecs.open('/Users/ryanshenefield/Downloads/newnewnewtest.txt', 'r', encoding='utf-8').read()
textline = text.split('\n\n')
while '' in textline:
    textline.remove('')
newline = []
for i in range(len(textline)):
    pattern = re.compile(r'"fly_code":"(.*?)"')
    result = pattern.findall(textline[i])
    pattern2 = re.compile(r'"character":"(.*?)"')
    result2 = pattern2.findall(textline[i])
    for x in range(len(result)):
        addline = result[x] + ',1=' + result2[0]
        newline.append(addline)
newtext = '\n'.join(newline)
with open('/Users/ryanshenefield/Downloads/waitinglist.txt', 'w', encoding='utf-8') as f0:
    f0.write(newtext)