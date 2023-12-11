#!/usr/bin/python3
""" module for the Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ represents a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes a bew rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ gets the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the value of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ gets the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ gets the value of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets the value of x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ gets the value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the value of y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ calculates the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ displays the rectangle """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """returns the printable representation of the rectangle"""
        rect = "[Rectangle] (" + str(self.id) + ") "
        rect += str(self.x) + "/" + str(self.y) + " - "
        rect += str(self.width) + "/" + str(self.height)
        return rect

    def update(self, *args, **kwargs):
        """updates the attributes"""
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of the rectangle"""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
