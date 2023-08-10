"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-11-22"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency_word
word = "Exercise"
filename = "words.txt"
fh = open(filename, "r+")
count = count_frequency_word(fh,word)
fh.close()

print(f"'Exercise' appears {count} time(s)")

