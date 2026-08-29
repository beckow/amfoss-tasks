Level 1
sector_C devil_fruit_6.txt is an executable
find . -executable
the flag: ONE_PIECE{GITO_GITO_NO_AWAKENING}

Level 2
i switched the branch to whiskey_peak_investigation
then i found the hidden vault baroque works cache
there i exported awakening signature 
and i got 2 files
using diff of those two files
Fi got this
the flag: BAROQUE_DIAL{SPLIT_TIMELINE_MISDIRECTION}

Level 3
i printed the names of all files and found out one stands out, its not named report its named agent manifest
inside it i found the earlier flag in base64
and i got this too

PONEGLYPH_FRAGMENT_I = "KjY2MjF4bW0lKzYqNyBsIS0vbTAtJTcnL"

Level 4
went back to canonical timeline
opened water 7 found the filetype of the file, then i extracted the tar file, then i extracted the zip file in it and found this in a secretlinkfile
PONEGLYPH_FRAGMENT_II="SwnbzptDiM3JSpvFiMuJ28PJzAlJ28VIzA="

Level 5
concatenated the ponenglyph fragments and put them in the python3 file and i got a github repo 
https://github.com/rogueone-x/Laugh-Tale-Merge-War

Level 6
using commit clashes between the two branches, i found the passcode
TheGrandLineRemembers

FLAG{The_Grand_Line_Remembers_Your_Commit}
