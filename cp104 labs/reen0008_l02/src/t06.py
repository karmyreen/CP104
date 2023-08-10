"""
-------------------------------------------------------
[Lab 2, task 6]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-09-19"
-------------------------------------------------------
"""

m_p = int(input("Mortgage Principal amount ($): "))
years = int(input("Number of Years: "))
interest = float(input("Yearly Interest Rate (%): "))

month_num = years * 12 
interest_month = interest/ 12 # so 5/12 
decimal_rate = interest_month/100



top =  decimal_rate * (1+ decimal_rate)**month_num
bottom = (1+decimal_rate)**month_num - 1 
total = m_p * ( top/bottom)

print("here is total: $", total)

# Imports