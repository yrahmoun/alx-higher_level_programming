#!/usr/bin/python3
"""module for the subclass Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define a square"""

    def __init__(self, size):
        """ initialize a square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """returns the  representation of a square"""
        string = "[Square] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
