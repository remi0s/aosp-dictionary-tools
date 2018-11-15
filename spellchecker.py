#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# def find(substr, infile, outfile,line_to_write):
#     lines = filter(lambda x: substr in x, open(infile))
#     if len(lines) > 0:
#         open(outfile, 'a').writelines(line_to_write)


delims = "=", ",", "\n"
regexPattern = '|'.join(map(re.escape, delims))
words = []
with open('Greek.dic') as fp:
    for line in fp:
        word = re.split(regexPattern, line)[0]

        words.append(word)


print "finished dict"

f = open('new_el2_wordlist.combined', 'a')
with open('new_el_wordlist.combined') as fp:
    for line in fp:
        word = re.split(regexPattern, line)[1]
        if words.__contains__(word):
            f.write(line)
        # print word
        # find(word, 'Greek.dic', 'new_el2_wordlist.combined',line)
f.close()

print "DONE"

print file_len("new_el2_wordlist.combined")
print file_len("new_el_wordlist.combined")
print "Corrected ", file_len("new_el_wordlist.combined")-file_len("new_el2_wordlist.combined"), " words\n"
