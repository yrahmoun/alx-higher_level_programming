#!/usr/bin/python3
""" module for Student class """


class Student:
    """ defines a student """

    def __init__(self, first_name, last_name, age):
        """initializes a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns a dictionary representation """
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces attributes """
        for key, value in json.items():
            setattr(self, key, value)
