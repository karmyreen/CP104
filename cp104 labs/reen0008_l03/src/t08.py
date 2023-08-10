"""
-------------------------------------------------------
Lab 3, Task 8 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-09-27"
-------------------------------------------------------
"""

dirt = float(input("Enter amount of dirt (m^3): "))
gravel = float(input("Enter amount of gravel (m^3): "))
sand = float(input("Enter amount of sand (m^3): "))

total = (dirt + gravel + sand )

print("materials   Cubic Meters")
print(f"Dirt         {dirt:5.1f}")
print(f"Gravel       {gravel:5.1f}")
print(f"Sand         {sand:5.1f}")
print(f"Total        {total:5.1f}")
# Imports