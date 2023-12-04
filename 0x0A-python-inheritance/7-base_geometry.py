#!/usr/bin/python3
""" module for BaseGeometry class """


class BaseGeometry:
    """ properties of the classs """

    def area(self):
        """calculates the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates a vlaue """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
