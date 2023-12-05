#!/usr/bin/python3
""" module for Student class """


class Student:
    """ defines a student """

    def __init__(self, first_name, last_name, age):
        """initializes a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns a dictionary representation """
        return self.__dict__
