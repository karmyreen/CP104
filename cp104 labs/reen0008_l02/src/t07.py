"""
-------------------------------------------------------
[Lab 2, task 7]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-09-19"
-------------------------------------------------------
"""

numflyers = int(input("Number of flyers : "))
numvolunteers = int(input("number of volunteers: "))

flyers_per_volunteer = numflyers // numvolunteers
leftover = numflyers % numvolunteers

print("Flyers per person: ", flyers_per_volunteer)
print()
print("Flyers leftover: ", leftover)
# Imports