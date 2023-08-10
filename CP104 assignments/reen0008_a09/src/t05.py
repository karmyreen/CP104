"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-11-30"
-------------------------------------------------------
"""
# Imports
from functions import student_info 

students = open("students.txt", "r")
l_id, h_id, avg = student_info(students)
students.close()

print(f"'{l_id}', '{h_id}', {avg:.2f}")