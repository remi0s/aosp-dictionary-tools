cat el_full.txt | tail -n +2 | awk '{print " word="$1", f="$2}' > el_wordlist.combined

# unix timestamp
date +%s
