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
from functions import mow_lawn 
width = float(input("What is width (m): "))
length = float(input("What is length (m): "))
speed = float(input("what is the speed (m^2/minute): "))

time = mow_lawn(width, length, speed)

print(f"Mowing the lawn takes {time:.0f} minutes")