"""
-------------------------------------------------------
Assignment 2, Task 3 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-10-05"
-------------------------------------------------------
"""
# Imports

num = int(input("Enter date in DDMMYYYY: " ) )
year = (num % 1000000)   % 10000 
month = (num % 1000000) //10000
day = (num // 1000000) 





print(f"The reformatted version: {year}/{month:02d}/{day:02d}")


