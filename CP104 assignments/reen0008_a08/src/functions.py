"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-11-23"
-------------------------------------------------------
"""
# Imports


def add_spaces(string):
    """
    -------------------------------------------------------
    Create a new string with added space between words. Words start
    with upper-case characters.
    Use: new_string = add_spaces(string)
    -------------------------------------------------------
    Parameters:
        string - string that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. string has at least one
            character (str)
    Returns:
        new_string - new string in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    
    new_string = " "
    first = string[0]
    second_string = string[1:]
    for i in second_string:
       
        if  i.isupper():
            new_string = new_string.lower() + " "
        new_string = new_string.lower()+ i
    
    new_string = first + new_string[1: len(new_string)-1] +   new_string[len(new_string) - 1 ].lower()
     
    return new_string 




def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', add 'ies'
        - otherwise add 's'
    Use: plural = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        plural - a plural version of string (str)
    -------------------------------------------------------
    """
    plural = ""
    if string.endswith("s") or string.endswith("sh") or string.endswith("ch"):
        plural = string + "es" 
    elif string.endswith("y") and not string.endswith("ay") and not string.endswith("oy"):
        plural = string[:len(string)-1] + "ies"
    else: 
        plural = string + "s"
    
        
    return plural 



def common_ending(string1, string2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(string1, string2)
    -------------------------------------------------------
    Parameters:
        string1 - first string for ending comparison (str)
        string2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of string1 and string2 (str)
    -------------------------------------------------------
    """
    common = ""
    i = 0 
    
    while i < len(string1) and not  string2.endswith(string1[i:]) :  
            i = i + 1 
    if i != len(string1):
        common = string1[i:]
    if i == len(string1):
        common = "no common ending"
        
    
          
            
    return common 



def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    
    valid = True 
    if len(isbn) != 17: 
        valid = False  
   
    new_isbn = isbn.split("-")
    
    if len(new_isbn) != 5:
        valid = False 
        
    i = 0 
    
    while i < len(new_isbn) and valid:   
        if not new_isbn[i].isdigit()  : 
            valid = False 
       
        if new_isbn[0] != '978' and  new_isbn[0] != '979':
            valid = False  
        if len(new_isbn[4]) != 1 : 
            valid = False  
        i = i + 1 
            
    return valid 

def is_word_chain(word_list):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = is_word_chain(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if word_list is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    word_chain = False 
    i = 1 
    while i < len(word_list):
        f_word = word_list[i-1][-1]
        s_word = word_list[i][0]
        if f_word.lower()  == s_word.lower():
            word_chain = True
        i = i + 1 
        
    return word_chain  
        
    
        
    
        