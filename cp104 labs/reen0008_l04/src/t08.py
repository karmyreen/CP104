"""
-------------------------------------------------------
Lab 4, Task 8
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-10-03"
-------------------------------------------------------
"""
# Imports
from functions import computer_costs

computer_cost = float(input("Cost of one computer: "))
num_computer = int(input("The number of computers bought: "))
commission = float(input("The commission in decimal: ") )


pre_commission_cost, total_cost = computer_costs( computer_cost, num_computer, commission)

print(f" ({pre_commission_cost:0.2f},{total_cost:0.2f})")

print(f"This is pre-commission cost: {pre_commission_cost:0.2f}")
print(f"This total cost with commission cost: {total_cost:0.2f}")