"""
-------------------------------------------------------
Functions Library
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-10-21"
-------------------------------------------------------
"""
# Imports
from random import randint

SQUARE_FEET_PER_ACRE = 43560

def feet_to_acres(square_footage):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = feet_to_acres(square_footage)
    -------------------------------------------------------
    Parameters:
        square_footage - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    
    footage = square_footage 
    
    acres = footage / SQUARE_FEET_PER_ACRE
    
    return acres 



def mow_lawn(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = mow_lawn(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time - time required to mow the lawn in minutes (float)
    ------------------------------------------------------
    """
    
    area = (width) * (length) 
    
    time = area / 4 
    return time 





def date_extract(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extract(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    
    year = (date_number % 1000000 ) % 10000
    month = (date_number // 1000000) 
    day =(date_number  % 1000000) //10000
   
  
    
    return year, month, day





def multiply_fractions(num1, denom1, num2, denom2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: numerator, denominator, product = multiply_fractions(num1, denom1, num2, denom2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of the first fraction (int)
        denom1 - denominator of the first fraction (int)
        num2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        numerator - numerator of the resulting fraction (int)
        denominator - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """
    
    
    numerator = num1 * num2
    denominator = denom1 * denom2
    product = numerator /denominator
    return numerator, denominator, product 


def math_quiz():
    
    """
    -------------------------------------------------------
    Displays two random numbers betwen 0 to 999 and adds it, with display of answer and user answer 
    Use: math_quiz()
    -------------------------------------------------------
    Parameters:
        
    Returns:
       
    ------------------------------------------------------
    """
    num1 = randint(0,999)
    num2= randint(0,999)
    product = num1 + num2
  
    print(f"{num1:5d}")
    print(f"+ {num2:3d}")
   
    
    ans = int(input("Your Answer: "))
    print("")
    print(f"Your answer:{ans:8d}")
    print(f"Expected: {product:10d}")
    return 
    



