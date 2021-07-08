def celsius_to_fahr(temp_celsius):
    """Converts Celsius temperatures to fahranheit
    
    Parameters
    --------
    
    temp_celsius: int | float
        Input temperature value in celsius (should be a number)
    
    Returns
    --------
    
    Temperature in Fahranheit (float)
    
    """
    return 9/5 * temp_celsius + 32


def kelvins_to_celsius(temp_kelvins):
    """Converts Kelvins temperature to celsius
    
    Parameters
    --------
    
    temp_kelvins: int | float
        Input temperature in kelvins (should be a number)
        
    Returns
    -------
    
    Temperature in celsius (float)
    
    """
    return temp_kelvins - 273.15

def fahr_to_celsius(temp_fahr):
    """Function to convert temperatures from fahranhiet to celsius
    
    Parameters
    --------
    
    temp_fahr: int | float
        Input temperature in fahranheit (should be a number)
        
    Returns
    ------
    
    Temperature in celsius (float)
    
    """
    return (temp_fahr -32)/(1.8)

def kelvins_to_fahr(temp_kelvins):
    """Converts temperature from kelvins to fahranheit
    
    Parameters
    --------
    
    temp_kelvins: int | float
        Input temperature in kelvins (should be a number)
        
    Required module and functions
    -------
    
    Module: 
    temp_converter
    
    Functions:
    kelvins_to_celsius
    celsius_to fahr
    
    Returns
    -------
    Temperature in Fahranheit (float)
    
    """
    temp_celsius = kelvins_to_celsius(temp_kelvins)
    temp_fahr = celsius_to_fahr(temp_celsius)
    return temp_fahr
