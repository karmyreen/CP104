"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-11-16"
-------------------------------------------------------
"""
# Imports


def list_factors(num):
    """
    -------------------------------------------------------
    Gets a list of factors that make up that number.
    Use: a = list_positives()
    -------------------------------------------------------
    Parameters: num - the number the function is determining its factors (int) 
    Returns:
        a - A list of factors (list of int)
    ------------------------------------------------------
    """
    
    a = []
    i = 1
    
    while i < num: 
        if num % i == 0 : 
            a.append(i)
            i = i + 1 
        else: 
            i = i + 1 
    return a



def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    
    numbers= []
    
    user = int(input("Enter a positive value: "))
    
    while user != 0 : 
        if user > 0 : 
            numbers.append(user)
        user = int(input("Enter a positive value: "))
    
    return numbers


def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    locations = []
    for i in range(len(values)):
        if values[i] == target: 
            locations.append(i)
    return locations  



def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """
    newlist = []

    for i in range(len(minuend)):
        
           
        if minuend[i] not in subtrahend:
            newlist.append(minuend[i])
        
        
    minuend.clear()       
    for i in newlist:
        minuend.append(i)
    
    return 


def is_sorted(values):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = is_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    
    
    l_value = values[0]
    in_order = True
    index = 0

    while in_order and index < (len(values) - 1):
        l_value = values[index]
        index = index + 1 
        if values[index] < l_value:
            in_order = False
        
    if in_order == True:
        index = -1

    return in_order, index
    



                
      
             


            
        
    