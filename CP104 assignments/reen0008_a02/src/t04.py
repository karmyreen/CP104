"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-10-05"
-------------------------------------------------------
"""
# Imports

pieces_of_cake = int(input("Number of pieces of cake: "))
num_of_ppl = int(input("Number of Party-Goers: "))

pieces_to_each_person = pieces_of_cake // num_of_ppl

leftovers = pieces_of_cake % num_of_ppl

print(f"""Each party-goer receives {pieces_to_each_person} pieces of cake 
Pieces of cake that won’t be distributed: {leftovers}""")

