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
from functions import find_longest 
filename = "words.txt"
fh = open(filename, "r+")
result = find_longest(fh)
fh.close() 

print(f"'{result}' is the last longest word")
