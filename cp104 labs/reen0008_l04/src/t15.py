"""
-------------------------------------------------------
Lab 4, Task 15
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-10-03"
-------------------------------------------------------
"""
# Imports
from functions import time_split


initial_secs = int(input("Input the initial amount of seconds"))
                   
days, hours, minutes, seconds = time_split(initial_secs)

print(f"({days},{hours},{minutes},{seconds}) ")
print(f" number of days: {days} number of hours: {hours} number of minutes {minutes} number of seconds {seconds} " )



