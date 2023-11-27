#!/usr/bin/python3
""" integer addition """


def add_integer(a, b=98):
    """ adds two integers or floats

    Args:
        a: argument one
        b: argument two

    Returns:
        sum of arguments
    """
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
