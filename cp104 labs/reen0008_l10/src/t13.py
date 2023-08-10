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
from functions import file_copy
n = 0 
filename = "words.txt"
filename2 = "new_words.txt"
fh_1 = open(filename, "r+")
fh_2 = open(filename2, "r+")

file_copy(fh_1,fh_2)
fh_1.close()
fh_2.close()
print("Copying 'words.txt' to 'new_words.txt'")