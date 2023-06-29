#!/usr/bin/env python3

import re
import codecs

text = codecs.open('/Users/ryanshenefield/Downloads/test.txt', 'r', encoding='utf-8').read()
a = re.sub(r'"order"[\s\S]*?},', '},', text)
with open('/Users/ryanshenefield/Downloads/newtest.txt', 'w', encoding='utf-8') as f0:
    f0.write(a)