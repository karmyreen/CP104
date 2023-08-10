"""
-------------------------------------------------------
Assignment 2, Task 2 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-10-05"
-------------------------------------------------------
"""


# Imports

pos_num = int(input("Input positive integer: "))

last_number = pos_num % 10
first_number = pos_num // 10 
    
product = last_number * first_number 





print(f"The product of the digits of {pos_num} is {product}")


