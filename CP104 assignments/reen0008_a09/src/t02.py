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
from functions import file_integers


name ="numbers.txt"

fh = open(name,"r")

result = file_integers(fh)


print(result)

fh.close()

