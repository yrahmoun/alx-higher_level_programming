#!/usr/bin/python3
""" module for the Base class """
import json


class Base:
    """ base of all other classes """

    __nb_objects = 0
    def __init__(self, id=None):
        """ initializes the class a new base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)
