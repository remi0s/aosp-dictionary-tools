zcat OpenSubtitles2018.el.gz | grep -v '<[a-z]*\s' | grep -v '&[a-z0-9]*;' | tr '[:punct:][:blank:][:digit:]' '\n' | tr '[:upper:]' '[:lower:]' | grep -v '[[:upper:]]' | uniq | sort -f | uniq -c | sort -nr | head -150000 | tail -n +2 | awk '{print " word="$2", f="$1}' > el_wordlist.combined

# unix timestamp
date +%s


zcat OpenSubtitles2018.ar.gz | grep -v '<[a-z]*\s' | grep -v '&[a-z0-9]*;' | tr '[:punct:][:blank:][:digit:]' '\n' | tr '[:upper:]' '[:lower:]' | grep -v '[[:upper:]]' | uniq | sort -f | uniq -c | sort -nr | head -150000 | tail -n +2 | awk '{print " word="$2", f="$1}' > ar_wordlist.combined

# unix timestamp
date +%s
