#!/usr/bin/python3
""" module for the Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ represents a rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes a new square """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ gets set the size """
        return self.width

    @size.setter
    def size(self, value):
        """ sets the size """
        self.width = value
        self.height = value

    def __str__(self):
        """ returns a string representation of the square """
        square = "[Square] (" + str(self.id) + ") "
        square += str(self.x) + "/" + str(self.y) + " - "
        square += str(self.width)
        return square

    def update(self, *args, **kwargs):
        """updates the attributes"""
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of the Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
