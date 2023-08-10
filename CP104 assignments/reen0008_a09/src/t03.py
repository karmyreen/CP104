"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-11-30"
-------------------------------------------------------
"""
# Imports

from functions import file_stats
name = "addresses.txt"
fh = open(name, "r")
ucount, lcount, dcount, wcount = file_stats(fh)
fh.close()

print(ucount, lcount, dcount, wcount)