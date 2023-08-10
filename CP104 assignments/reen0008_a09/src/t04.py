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

from functions import number_lines

fh_in = open("wilde.txt", "r")
fh_out = open("wilde_numbered.txt", "w")
number_lines(fh_in, fh_out)
fh_in.close()
fh_out.close()