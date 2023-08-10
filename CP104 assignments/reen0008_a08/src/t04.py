"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-11-23"
-------------------------------------------------------
"""
# Imports
from functions import is_valid_isbn
isbn_num = str(input("Input a isbn: "))
valid = is_valid_isbn(isbn_num)

print(valid)