"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-11-03"
-------------------------------------------------------
"""
# Imports



def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """
    product = 1 
    
    for i in range(1, num + 1, 1):
        product = product * i 
      
    
    return product  

def calories_burned(per_minute, minutes):
    """
    -------------------------------------------------------
    Calculates how many calories are burned every 5 minutes given number
    of calories burned in a minute 
    Use: calories_burned(per_minute, minutes))
    -------------------------------------------------------
    Parameters:
        per_minute - number of calories burned in a minute(float)
        minutes - number of minutes (float) 
    Returns:
        none
    ------------------------------------------------------
    """
    
    for i in range(5, minutes + 5 , 5 ):
        cal_in_five = per_minute * i 
        print(f" {i:>2d}:{cal_in_five:6.1f}")
    
    return 





def open_triangle(num_rows):
    """
    -------------------------------------------------------
    Prints a triangle made up of # with a empty center 
    
    Use: open_triangle(num_rows)
    -------------------------------------------------------
    Parameters:
       num_rows - number of rows of the triangle you want (int)
    Returns:
        none
    ------------------------------------------------------
    """
    symbol = '#'
    for i in range(1, num_rows+1, 1 ):
        print(symbol + ' ' * (i-1) + symbol )
        
        
    return 



def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    space = "   "
    for g in range(start, stop+1):
        if g == start:
            print(f"{space}{g:>4}", end = " ")
        else:
            print(f"{g:>4}", end = " ")
    print() 
    print( space + "-----" * stop)
    
    for i in range( start, stop+1):
        print(f"{i:d}|", end = " ")
        
        for j in range(start, stop +1):
            
    
            print(f"{i*j:4d}", end=" ")
        print()
        
    
    return
    
    
    
   
    
    
    
  
        
    
   


def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0 
    for i in range(start, (count * increment) + start  , increment):
        
        total = total + i 
        
    
    return total 





'''
    for i in range( start, stop): 
        print(f"    {i}" + ' '*4, end =" ")
        print(f"-------------------------")
        for j in range(start, stop):
            print(f"    {j}|    ",(i * j) , ' '*4 ) 
            
'''

'''
    for g in range(start, stop+1):
        print(f"{g:4d}", end = " ")
    print()
    print("-------------------------")
    
    for i in range( start, stop+1):
        
        
        for j in range(start, stop +1):
            
    
            print(f"{i*j:4d}", end=" ")
        print()
        
        
        
        
    space = "       "
    line = "----"
    
   
    for i in range(start, stop + 1):
        if i == start:
            print(f"{space}{i:>4}", end = "")
        else:
            print(f"{i:>4}", end = "")
    
    print()
    
    print(f"{space}{line*stop}")
    
    for i in range(start, stop + 1):
        print(f"{i:>4} | ", end = "")
        
        for j in range(start, stop +1):
            print(f"{i*j:>4}", end = "")
            
        print()
        
        
        
        
           
'''
    
    
    



