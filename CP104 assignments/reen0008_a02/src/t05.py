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
#here are all the inputs , f means foundation 
f_length = float(input("Foundation length (m): "))
f_width = float(input("Foundation width (m): "))
f_height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
cost_of_concrete =  int(input("Cost of concrete ($/m^3): "))
cost_of_bricks = int(input("Cost of bricks ($/m^2): "))


concrete_needed = f_length * f_width  * f_height

cost_concrete = concrete_needed * cost_of_concrete 

bricks_for_wall = ((wall_height *f_length)*2) + ((wall_height *f_width)*2)

cost_brick = bricks_for_wall * cost_of_bricks

total_cost = cost_brick + cost_concrete
print(" ")

print(f"Concrete needed for foundation (m^3) {concrete_needed:,.2f}")
print(f"Cost of concrete:${cost_concrete:,.2f}")
print(f"Bricks needed for walls (m^2):{bricks_for_wall:,.2f}")
print(f"Cost of bricks:${cost_brick:,.2f}")
print(f"Total cost:${total_cost:,.2f}")





