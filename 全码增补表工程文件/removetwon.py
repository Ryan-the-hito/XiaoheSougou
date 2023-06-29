#!/usr/bin/env python3

import re
import codecs

text = codecs.open('/Users/ryanshenefield/Downloads/newnewtest.txt', 'r', encoding='utf-8').read()
a = re.sub(r'\n\n', '', text)
with open('/Users/ryanshenefield/Downloads/newnewnewtest.txt', 'w', encoding='utf-8') as f0:
    f0.write(a)