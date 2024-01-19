#!/usr/bin/env python3

import codecs

text = codecs.open('/Users/ryanshenefield/Downloads/ciku.txt', 'r', encoding='utf-8').read()

text = text.replace('iong', 's')
text = text.replace('uang', 'l')
text = text.replace('iang', 'l')

text = text.replace('ong', 's')
text = text.replace('uai', 'k')
text = text.replace('ing', 'k')
text = text.replace('uan', 'r')
text = text.replace('ian', 'm')
text = text.replace('iao', 'n')
text = text.replace('ang', 'h')
text = text.replace('eng', 'g')

text = text.replace('ou', 'z')
text = text.replace('un', 'y')
text = text.replace('ua', 'x')
text = text.replace('ia', 'x')
text = text.replace('ei', 'w')
text = text.replace('ui', 'v')
text = text.replace('ue', 't')
text = text.replace('ve', 't')
text = text.replace('iu', 'q')
text = text.replace('ie', 'p')
text = text.replace('uo', 'o')
text = text.replace('an', 'j')
text = text.replace('en', 'f')
text = text.replace('ai', 'd')
text = text.replace('ao', 'c')
text = text.replace('in', 'b')
text = text.replace('zh', 'v')
text = text.replace('sh', 'u')

text = text.replace("'o'", "'oo'")
text = text.replace("\to'", "\too'")
text = text.replace("'o\n", "'oo\n")

text = text.replace("'e'", "'ee'")
text = text.replace("\te'", "\tee'")
text = text.replace("'e\n", "'ee\n")

text = text.replace("'a'", "'aa'")
text = text.replace("\ta'", "\taa'")
text = text.replace("'a\n", "'aa\n")

text = text.replace("'h'", "'ah'")
text = text.replace("\th'", "\tah'")
text = text.replace("'h\n", "'ah\n")

text = text.replace("'g'", "'eg'")
text = text.replace("\tg'", "\teg'")
text = text.replace("'g\n", "'eg\n")

text = text.replace("'d'", "'ai'")
text = text.replace("\td'", "\tai'")
text = text.replace("'d\n", "'ai\n")

text = text.replace("'j'", "'an'")
text = text.replace("\tj'", "\tan'")
text = text.replace("'j\n", "'an\n")

text = text.replace("'c'", "'ao'")
text = text.replace("\tc'", "\tao'")
text = text.replace("'c\n", "'ao\n")

text = text.replace("'w'", "'ei'")
text = text.replace("\tw'", "\tei'")
text = text.replace("'w\n", "'ei\n")

text = text.replace("'f'", "'en'")
text = text.replace("\tf'", "\ten'")
text = text.replace("'f\n", "'en\n")

text = text.replace("'z'", "'ou'")
text = text.replace("\tz'", "\tou'")
text = text.replace("'z\n", "'ou\n")

with open('/Users/ryanshenefield/Downloads/ciku2.txt', 'w', encoding='utf-8') as f0:
    f0.write(text)