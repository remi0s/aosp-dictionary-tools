# for this script to work you will need copy the function inside yaraspell/spelldict.py file from https://github.com/linuxscout/yaraspell repo
# all credits to linuxscout/yaraspell

def mainly():
    import sys

    reload(sys)
    sys.setdefaultencoding('utf8')

    def file_len(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1
   
    speller = spelldict()
    

    delims = "=",","

    regexPattern = '|'.join(map(re.escape, delims))
    f = open('ar_wordlist.combined', 'a')
    with open('new_ar_wordlist.combined') as fp:
        for line in fp:
            word = re.split(regexPattern,line)[1]
            exists = speller.lookup(word)
            # if exists:
            #     print word.encode("utf8"), "correct"
            # else:
            #     print word.encode("utf8"), "misspelled"
            if exists:
                f.write(line)


    f.close()

    print file_len("new_ar_wordlist.combined")-file_len("ar_wordlist.combined"), "corrections"