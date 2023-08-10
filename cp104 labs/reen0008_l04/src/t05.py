"""
-------------------------------------------------------
Lab 4, Task 5
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-10-03"
-------------------------------------------------------
"""
# Imports
from functions import right_triangle 

adj1 = float(input("Here is the adjacent side: "))
oppo1= float(input("Here is the opposite side: "))

hyp , cric, area  = right_triangle(adj1, oppo1)


print(f"({hyp:0.1f},{cric:0.1f},{area:0.1f})")
print(f"This is hypotenuse: {hyp:0.1f} ")
print("")
print(f"This the circumference of triangle: {cric:0.1f}")
print("")
print(f"This is area of triangle: {area:0.1f}")


