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
from functions import append_max_num 
filename = "numbers.txt"
fh = open(filename, "r+")

result = append_max_num(fh)
fh.close() 

print(f"{result} is appended")

