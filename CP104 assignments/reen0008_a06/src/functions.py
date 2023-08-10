"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-11-09"
-------------------------------------------------------
"""
# Imports

def winner():
    """
    -------------------------------------------------------
    Determines how many times blue and grey team appeared in the input 
    Use: blue, grey = winner()
    -------------------------------------------------------
    Parameters:
        none
    Returns:
       blue - how many times blue is inputed (int) 
       grey - how many times grey is inputed(int) 
    ------------------------------------------------------
    """
    
    
    blue = 0 
    grey = 0 
    blank = False 
    
    
    while blank  == False : 
        user = str(input("Winning team: "))
        if user == "grey":
            grey = grey + 1 
        
           
        elif user == "blue":
            blue = blue + 1 
            
        else:
            blank = True 
          
        
             
        
    return blue , grey 




def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    
    increment = 2
    prime = True 
   
    while increment < num: 
        
        if num % increment == 0 : 
            prime = False
            
        increment = increment + 1 
       
        
    return prime 



def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    ANNUAL = 12
    month = 0 
    balance = principal
    print(f"Principal:  ${principal:.2f}")
    print(f"Interest rate : {rate:.1f}%")
    print(f"Monthly payment: ${payment:.2f}")
    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")
    
    while balance!= 0 : 
        
        
        month = month + 1 
        if payment < balance:
            
            
            upper_part = balance/rate
            balance = balance + (upper_part/ ANNUAL) - payment 
            month_interest =  upper_part/ ANNUAL
           
            print(f"{month:>5d}{month_interest:>9.2f}{payment:>9.2f} {balance:>9.2f}")
        else:
            payment = balance 
            
            upper_part = balance/rate
            month_interest =  upper_part/ ANNUAL
            balance = 0 
            print(f"{month:>5d}{month_interest:>9.2f}{payment:>9.2f} {balance:>9.2f}")
    return 





def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """
    count = 0 
    
    while num > 0  : 
        count = count + 1 
        num = num // 10 
            
    return count



def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """
    factor = num -1 
    total = 0 
    
    while factor > 0  :
     
        if num % factor == 0 : 
            total = total + factor
            factor = factor - 1
        else: 
            factor = factor - 1
            
      
            
    return total
            
        
            
    
    
    
    














            
            
       
       
    
    
        
        