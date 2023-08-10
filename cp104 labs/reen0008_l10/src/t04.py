"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-11-22"
-------------------------------------------------------
"""
# Imports
from functions import customer_first 
filename ="customers.txt"
fh = open(filename, "r")
cust_result = customer_first(fh)
fh.close()

print(f"Find customer with earliest sign-in:\n{cust_result}")



