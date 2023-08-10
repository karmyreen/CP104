"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-11-22"
-------------------------------------------------------
"""
# Imports

def customer_first(fh):
    """
    -------------------------------------------------------
    Find the customer with the earliest sign-up date.
    Assumes file is not empty.
    Use: result = customer_first(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the earliest sign-in date (list)
    -------------------------------------------------------
    """
    
    line = fh.readline()
    result = line.strip().split(',')
    
    while line != "" : 
        
        
        processing2 = line.strip().split(',')
        if result[4] > processing2[4]: 
            result = processing2
        line = fh.readline()
        
            
    return result 




def append_max_num(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of fh. The number appended
    is the maximum of all the numbers currently in the file.
    Assumes file is not empty.
    Use: num = append_max_num(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    num = 0 
    
    
   
        
    for lines in fh:    
        if int(lines.strip()) > num:
            num = int(lines.strip()) 
        
    fh.write(f"\n{num:d}")
    return num 


def count_frequency_word(fh, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in fh.
    Case is significant - line in file must match word in case.
    Use: count = count_frequency_word(fh, word)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        word - the word to search for it in fh (str)
    Returns:
        count - the number of appearance of word in fh (int)
    ------------------------------------------------------
    """
    count = 0 
    for line in fh: 
        
        if line.strip() == word: 
            
            count = count + 1 
    return count 



def find_longest(fh):
    """
    -------------------------------------------------------
    Finds the last word with longest length in fh.
    Assumes file is not empty.
    Use: word = find_longest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the last word with the longest length in fh (str)
    ------------------------------------------------------
    """
   
    line1 = fh.readline() 
    word = line1.strip()
    largest = len(word)
    for line in fh:
        if largest <= len(line.strip()):
            word = line.strip()
            largest = len(word)
        
    return word 


def file_copy(fh_1, fh_2):
    """
    -------------------------------------------------------
    Copies the contents of fh_1 to fh_2.
    Any contents of fh_2 are overwritten.
    Use: file_copy(fh_1, fh_2)
    -------------------------------------------------------
    Parameters:
        fh_1 - source file (file handle - already open for reading)
        fh_2 - target file (file handle - already open for writing)
    Returns:
        None
    ------------------------------------------------------
    """
    line = fh_1.readline()
   
    
    while line != "":
       
        fh_2.write(line)
        line = fh_1.readline()
        
     
    
        
    return 
        
        
         
        
    
    
    
            
        
            
        
        
        
        
        
        
        
        