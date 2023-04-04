#!/usr/bin/python3
"""writing a function that returns the addition of two ints/floats"""


def add_integer(a b=98):
    """Function takes in two ints/floats

    Args: 
        a
        b
    
    Raises:
        TypeErrors if not int/float
    
    Returns:
        a + b
    """
    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    
    return a + b