"""
-------------------------------------------------------
Task 1, Assignment 3 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-10-21"
-------------------------------------------------------
"""
# Imports
from functions import feet_to_acres 

footage = float(input("What is the square footage: "))

acres = feet_to_acres(footage)

print(f"{acres:.2f} acres is equivalent to {footage:,.2f} square feet")


