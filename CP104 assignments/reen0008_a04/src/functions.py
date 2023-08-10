"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-10-29"
-------------------------------------------------------
"""
# Imports


def day_of_week(day_number):
    """
    -------------------------------------------------------
    Determines what day of the week from the user input between 1 and 7 
    Use: day = day_of_week(day_number)
    -------------------------------------------------------
    Parameters:
        day_number - numeric day (int > 0, int <= 7 )
        
    Returns:
        day - Returns a name of day if valid integer or displays error (str) 
    -------------------------------------------------------
    """
    day = ' '
    if day_number == 1: 
        day = 'Monday'
    elif day_number == 2: 
        day = 'Tuesday'
    elif day_number == 3: 
        day = 'Wednesday'
    elif day_number == 4: 
        day = 'Thursday'
    elif day_number == 5: 
        day = 'Friday'
    elif day_number == 6:
        day = 'Saturday'
    elif day_number == 7: 
        day = 'Sunday'
    else : 
        day = 'Error'
    return day 



def pollution_level(aqi):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level = pollution_level(aqi)
    -------------------------------------------------------
    Parameters:
        aqi - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """
    
    if aqi <0: 
        level = 'Error'
    elif aqi <= 50: 
        level = 'Good'
    elif aqi <= 100: 
        level = 'Moderate'
    elif aqi <= 150: 
        level = 'Unhealthy for Sensitive Groups'
    elif aqi <= 200: 
        level = 'Unhealthy'
    elif aqi <= 300: 
        level = 'Very Unhealthy'
    else: 
        level = 'Hazardous'
    return level





def product_largest(v1, v2, v3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    v1, v2, and v3.
    Use: product = product_largest(v1, v2, v3)
    -------------------------------------------------------
    Parameters:
        v1 - a number (float)
        v2 - a number (float)
        v3 - a number (float)
    Returns:
        product - the product of the two largest values of
            v1, v2, and v3 (float)
    ------------------------------------------------------
    """
    
    if v1 > v3 and v2 > v3: 
        product = v1 * v2 
    elif v1 > v2: 
        product = v1 * v3 
    else: 
        product = v3 * v2 
        
    return product 



def rgb_mix(rgb1, rgb2):
    """
    -------------------------------------------------------
    Determines the secondary colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: colour = rgb_mix(rgb1, rgb2)
    -------------------------------------------------------
    Parameters:
        rgb1 - a primary RGB colour (str)
        rgb2 - a primary RGB colour (str)
    Returns:
        colour - a secondary RGB colour (str)
    -------------------------------------------------------
    """
    if rgb1 == 'red' and rgb2  == 'blue' or rgb1 == 'blue' and rgb2 == 'red':
        colour = 'fuchsia'
        
   
    elif rgb1 == 'green' and rgb2 == 'blue' or rgb1 == 'blue' and rgb2 == 'green':
        colour = 'aqua'
        
    elif rgb1 == 'red' and rgb2 == 'green' or rgb1 == 'green' and rgb2 == 'red':
        colour = 'yellow'
        
    elif rgb1 == 'red' and rgb2 == 'red':
        colour = 'red'
        
    elif rgb1 == 'blue' and rgb2 == 'blue':
        colour = 'blue'
        
    elif rgb1 == 'green' and rgb2 == 'green':
        colour = 'green'
    else :
        colour = 'Error'
    return colour 
        
    
    
    
    
    
def yee_ha(number):
    
    """
    -------------------------------------------------------
    Determines if a number can be evenly divided by 3, 7, or both evenly

    Use: answer = yee_haw(number) 
    -------------------------------------------------------
    Parameters:
        number - the value that is going to be divided (int > 0 ) 
    Returns:
        answer-  Tells if it can be divided or tells it is not message  (str)
    -------------------------------------------------------
    """
    
    if number % 3== 0  and number % 7 == 0: 
        answer = 'Yee Ha'
    elif number % 7 == 0 : 
        answer = 'Ha'
    elif number % 3 == 0 : 
        answer = 'Yee'
    else: 
        answer = 'Nada'
    return answer 
        
        
    
    
    
