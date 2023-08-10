"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-09-27"
-------------------------------------------------------
"""


# Imports

principle = float(input("Principle: $"))
interest = float(input("Interest in %:"))
years = int(input("Number of years: "))
compound_interest_year = int(input("Number of times interest compounded per year: "))

decimal_interest = interest / 100 

in_bracket = 1 + (decimal_interest/compound_interest_year )
exponent = compound_interest_year * years 

formula = principle*(in_bracket)**exponent 

print(f"Balance: ${formula}")


