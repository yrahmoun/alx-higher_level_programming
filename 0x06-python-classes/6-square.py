#!/usr/bin/python3

""" make an empty class """


class Square:
    """ a class about a square """

    def __init__(self, size=0, position=(0, 0)):
        """ initialize attributes

        Args:
            size: represents size of square
            position: position of the square
        """

        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """ get the position of the square """

        return (self.__position)

    @position.setter
    def position(self, value):
        """ sets the position of the square """

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("Position must be a tuple of 2 positive integers")
        if not all(coord >= 0 for coord in value):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ finds the area of the square

        Returns the area"""

        return (self.__size ** 2)

    def my_print(self):
        """ prints a square """

        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")
                print("#" * self.__size)
