from math import log2

def calculate_log2(number):
    """
    Calculate the logarithm base 2 of a given number.
    
    This function takes a positive number as input and returns
    its log base 2 value.
    """
    return log2(number)


print(calculate_log2(1024))   
print(calculate_log2(8))      
print(calculate_log2(64))     
print(calculate_log2(1))      

help(calculate_log2)
