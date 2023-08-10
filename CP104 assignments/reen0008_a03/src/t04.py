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
# Import
from functions import multiply_fractions

num1= int(input("Input first numerator: "))
num2= int(input("Input second numerator: "))
denom1 = int(input("Input first denominator: "))
denom2 = int(input("Input second denominator: "))

num, denom, product = multiply_fractions(num1,num2,denom1,denom2)\


print(f"Result: {num:d}/{denom:d} = {product:.3f}")
