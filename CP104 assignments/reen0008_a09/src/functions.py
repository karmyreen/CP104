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

def file_head(fh, linecount):
    """
    -------------------------------------------------------
    Prints first linecount lines of fh. Line numbering starts at 0.
    If length of file is shorter than linecount, stops printing after
    last line of file.
    Use: file_head(fh, linecount)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
        linecount - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    
    i = 0 
  
    line = fh.readline().strip()
        
    while  i < linecount and line != "" :
        print(line)
        line = fh.readline().strip()
     
        i = i + 1 
        
    return 



def file_integers(fh):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: numbers = file_integers(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process ( (file handle - open for reading)
    Returns:
        numbers - a list of integers from fh (list of int)
    -------------------------------------------------------
    """
    
    numbers = []
    
    
    for i in fh: 
        line = i.strip().split(",")
        for j in line: 
            if j.isdigit() and int(j) > 0:
                numbers.append(int(j))
                
                
        
   
            
    return numbers 




def file_stats(fh):
    """
    -------------------------------------------------------
    Evaluates the contents of a file.
    Use: ucount, lcount, dcount, wcount = file_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        ucount - The number of uppercase letters in the file (int)
        lcount - The number of lowercase letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of whitespace characters in the file (int)
    -------------------------------------------------------
    """
    
    
    ucount = 0 
    lcount = 0 
    dcount = 0 
    wcount = 0
    
  
    for line in fh: 
        for i in line: 
            if i.isupper():
                ucount = ucount + 1 
            if i.islower():
                lcount = lcount + 1 
            if i.isdigit():
                dcount = dcount + 1 
            if i.isspace(): 
                wcount = wcount + 1 
    return ucount, lcount, dcount, wcount 




def number_lines(fh_in, fh_out):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_out contain contents
    of fh_in where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: number_lines(fh_in, fh_out)
    -------------------------------------------------------
    Parameters:
        fh_in - file to read (file - open for reading)
        fh_out - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    
    count = 0 
    for line in fh_in:
        
        fh_out.write(f"[{count}] {line}")
        count = count + 1 
    return 



def student_info(students):
    """
    -------------------------------------------------------
    Get information from a file of students and grades.
    Use: l_id, h_id, avg = student_info(students)
    -------------------------------------------------------
    Parameters:
        students - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    
    
    line = students.readline().strip().split(",")
    l_id = line[2] 
    h_id = line[2]
    low_mark = int(line[3])
    high_mark = int(line[3])
    avg = 0 
    count = 0
    
    while line != [""]:
      
        avg = avg + float(line[3])
        count = count + 1
       
         
        if int(line[3]) < low_mark : 
            l_id = line[2]
            
        if int(line[3]) > high_mark: 
            h_id = line[2] 
        
        line = students.readline().strip().split(",")
        
      
       
        
            
    avg = avg / count
    
    return l_id, h_id, avg 
        
            
    
        
        

        
            
      
             
       
        
    
                
    
    
    
    
        
        