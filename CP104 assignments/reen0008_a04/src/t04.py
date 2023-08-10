"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-10-29"
-------------------------------------------------------
"""
# Imports
from functions import rgb_mix
colour1 = str(input("Enter a colour (in lowercase): "))
colour2 = str(input("Enter a colour (in lowercase): "))
colour1 = colour1.lower()
colour2 = colour2.lower()

colour= rgb_mix(colour1, colour2)

print(colour)

