"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-10-21"
-------------------------------------------------------
"""
# Imports
from functions import  date_extract

date_num = int(input("What is the date number(MMDDYYYY): " ))


year, month, day  = date_extract(date_num)




print(f"{year}/{month:02d}/{day:02d}")
