This repository was created in order to help people create their own dictionaries for AOSP keyboard or for general use! Credits are given bellow for the repositories used in order to achieve this goal.

1)Find an language dump file from https://archive.org/ or http://opus.nlpl.eu/OpenSubtitles2018.php or http://opus.nlpl.eu/index.php

2)Edit sort.sh to match the file downloaded. For tar.gz files use "zcat", for bz2 use "bzcat" else try "cat". And run it with ./sort.sh (running this command will take LONG if the file size is big)

3)After the wordlist is created use the parser.pl with command perl parser.pl filename > newfilename

4)Spellchecking the wordlist is essential. There are many ways to do it but i would recommend using a python script because its less time consuming. 

5)Add header information in the new wordlist file

6)Edit run.sh file to fit the filenames and then use it with ./run.sh command to create the binary dictionary

Have Fun!

CREDITS: 

https://github.com/hermitdave/FrequencyWords for opensubtitles archive project! You can use the txt files provided here in content/2016  instead of downloading huge dump files for each languages.

Used http://opus.nlpl.eu/OpenSubtitles2018.php in order to create the wordlists.

https://github.com/linuxscout/yaraspell I used this repository for spellchecking the arabic wordlist!

https://github.com/androidtweak/dictionaries/tree/f936da825c1d172e83e3b8ed8ddc9c30bc168d57/tools for the original tools used!



