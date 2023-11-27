#!/usr/bin/python3
""" module for rectangle class """


class Rectangle:
    """ defines a rectangle """

    def __init__(self, width=0, height=0):
        """ initializes the rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ gets the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the value of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height of the rectangle """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ sets the value of height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
