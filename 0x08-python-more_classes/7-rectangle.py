#!/usr/bin/python3
""" module for the rectangle method """


class Rectangle:
    """ defines a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """returns the prinable representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = ""
        for row in range(self.__height):
            rect += str(self.print_symbol) * self.__width
            if row < self.height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """returns the string representation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """prints a message for every deletion of an object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
