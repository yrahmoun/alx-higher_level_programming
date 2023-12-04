#!/usr/bin/python3
""" module for rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defines a rectangle """

    def __init__(self, width, height):
        """Intialize a rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the  representation of a Rectangle"""
        string = "[Rectangle] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
