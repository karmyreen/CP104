"""
-------------------------------------------------------
Functions module 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-10-03"
-------------------------------------------------------
"""


from math import pi , sqrt

# Imports

def circumference(radius):
    """
    -------------------------------------------------------
    Calculates and returns circumference of a circle.
    Use: circ = circumference(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        circ - circumference of a circle (float)
    ------------------------------------------------------
    """
    
    circ = 2*pi*radius
    return circ





def right_triangle(adjacent, opposite):
    """
    -------------------------------------------------------
    Calculates and returns the hypotenuse, circumference, and
    area of a right triangle given two non-hypotenuse sides.
    Use: hyp, circ, area = right_triangle(adjacent, opposite)
    -------------------------------------------------------
    Parameters:
        adjacent - length of side right triangle (float > 0)
        opposite - length of side right triangle (float > 0)
    Returns:
        hyp - hypotenuse of the triangle (float)
        circ - circumference of the triangle (float)
        area - area of the triangle (float)
    ------------------------------------------------------
    """
    
    adj = adjacent 
    oppo = opposite 
    hyp = sqrt(adj**2 + oppo**2)
    circ = hyp + adj + oppo
    area = (oppo * adj)  / 2 
    
    return hyp, circ, area


def computer_costs(computer_cost, computers_bought, commission_percent):
    """
    -------------------------------------------------------
    Calculates purchase costs of computers
    Use: pre_commission_cost, total_cost = computer_costs(computer_cost,
        computers_bought, commission_percent)
    -------------------------------------------------------
    Parameters:
        computer_cost - per unit cost (float >= 0)
        computers_bought - units bought (int >= 0)
        commission_percent - wholesaler commission (float >= 0)
    Returns:
        pre_commission_cost - cost before commission (float)
        total_cost - cost after commission (float)
    -------------------------------------------------------
    """
    
    pre_commission_cost = computer_cost * computers_bought
     
    total_cost = pre_commission_cost *  (1 +  commission_percent/100  )
    
    return  pre_commission_cost, total_cost





def c_to_f(celsius):
    """
    -------------------------------------------------------
    Converts temperatures in celsius to fahrenheit.
    Use: fahrenheit = c_to_f(celsius)
    -------------------------------------------------------
    Parameters:
        celsius - temperature in celsius (int >= -273)
    Returns:
        fahrenheit - equivalent to celsius (float)
    -------------------------------------------------------
    """
    
    F_CONSTANT = 32
    fahrenheit = (9/5 * celsius + F_CONSTANT)
    
    return fahrenheit 



def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts total seconds into days, hours, minutes, and seconds.
    Use: days, hours, minutes, seconds = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """
    SECONDS = 60 
    days = initial_seconds // ((SECONDS*SECONDS)*24)
    initial_seconds = initial_seconds % ((SECONDS*SECONDS)*24)
    hours = initial_seconds // (SECONDS*SECONDS)
    initial_seconds = initial_seconds % (SECONDS*SECONDS)
    minutes = initial_seconds// SECONDS 
    initial_seconds = initial_seconds % SECONDS
    seconds = initial_seconds
    
    return days, hours, minutes, seconds 



def f_to_c(fahrenheit):
    
    """
    -------------------------------------------------------
    Converts temperatures in celsius to fahrenheit.
    Use: celsius = f_to_c(fahrenheit)
    -------------------------------------------------------
    Parameters:
        fahrenheit - temperature in celsius (int >= -273)
    Returns:
        celsius - equivalent to celsius (float)
    -------------------------------------------------------
    """
    
    C_CONSTANT = 32
    celsius = (5/9 * (fahrenheit - C_CONSTANT))
    
    return celsius


    
    
