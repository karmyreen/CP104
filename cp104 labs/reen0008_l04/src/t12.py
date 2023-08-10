"""
-------------------------------------------------------
Lab 4 , Task 12
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-10-03"
-------------------------------------------------------
"""
# Imports

from functions import c_to_f
celsius = float(input("Input the degrees in celsius: "))

fahrenheit = c_to_f(celsius)
print(f"Here is the temperature in Fahrenheit: {fahrenheit:0.0f}")

