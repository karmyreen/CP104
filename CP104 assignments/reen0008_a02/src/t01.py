"""
-------------------------------------------------------
Assignment 2, Task 1 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-10-05"
-------------------------------------------------------
"""
# Imports


total_sales = int(input("Here is total sales: $ "))

ANNUL_TAX = 18.5

final_amount = total_sales*( (ANNUL_TAX/100) )



print("Projected Tax Report")
print("--------------------------")
print(f"Total Sales:  $ {total_sales:,.2f}")
print(f"Annul Tax:    % {ANNUL_TAX:.2f}")
print("--------------------------")
print(f"Tax:          $  {final_amount:>8,.2f}")
