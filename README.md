This repository was created in order to help people create their own dictionaries for AOSP keyboard or for general use! Credits are given bellow for the repositories used in order to achieve this goal.

1)Find an language dump file from https://archive.org/ or http://opus.nlpl.eu/OpenSubtitles2018.php or http://opus.nlpl.eu/index.php 

OR the easier way:

 Use this (https://github.com/hermitdave/FrequencyWords/tree/master/content/2016) gitrepository to download the language wordlist needed
 then use ./freq_words_parser.sh command to make the wordlist in the format needed for AOSP.
 
 Skip step 2) if you used this method!
 

2)Edit sort.sh to match the file downloaded. For tar.gz files use "zcat", for bz2 use "bzcat" else try "cat". And run it with ./sort.sh (running this command will take LONG if the file size is big)

3)After the wordlist is created use the parser.pl with command perl parser.pl filename > newfilename

4)Spellchecking the wordlist is essential. There are many ways to do it but i would recommend using a python script because its less time consuming. You can find plenty of dictionaries on credits [5]

5)Add header information in the new wordlist file at the first row. The header should be similar to the following, but you should change the values to match your locale. 

'dictionary=main:el,locale=el,description=Greek dict created from OpenSubtitles by Rafail Mastoras,date=1542122459,version=1'

6)Edit run.sh file to fit the filenames and then use it with ./run.sh command to create the binary dictionary

Have Fun!

CREDITS: 

[1] https://github.com/hermitdave/FrequencyWords for opensubtitles archive project! You can use the txt files provided here in content/2016  instead of downloading huge dump files for each languages.

[2] Used http://opus.nlpl.eu/OpenSubtitles2018.php in order to create the wordlists.

[3] https://github.com/linuxscout/yaraspell I used this repository for spellchecking the arabic wordlist!

[4] https://github.com/androidtweak/dictionaries/tree/f936da825c1d172e83e3b8ed8ddc9c30bc168d57/tools for the original tools used!

[5] https://github.com/titoBouzout/Dictionaries used for greek spellcheck!



