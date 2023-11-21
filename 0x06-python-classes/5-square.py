#!/usr/bin/python3

""" make an empty class """


class Square:
    """ a class about a square """

    def __init__(self, size=0):
        """ initialize attributes

        Args:
            size: represents size of square
        """

        self.__size = size

    @property
    def size(self):
        """get the value of the size"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the value of the size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ finds the area of the square

        Returns the area"""

        return (self.__size ** 2)

    def my_print(self):
        """ prints a square """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
