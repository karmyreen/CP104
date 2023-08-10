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
from functions import file_head

num = int(input("Number of lines to print: "))
fh = open("functions.py", "r")
file_head(fh, num)
fh.close()