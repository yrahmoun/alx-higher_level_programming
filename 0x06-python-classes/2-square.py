#!/usr/bin/python3

""" make an empty class """


class Square:
    """ a class about a square """

    def __init__(self, size=0):
        """ initialize attributes

        Args:
            size: represents size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
