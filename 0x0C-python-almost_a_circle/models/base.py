#!/usr/bin/python3
""" module for the Base class """
import json


class Base:
    """ base of all classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json reprisentation"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON representation json_string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != []:
            if cls.__name__ == "Rectangle":
                inst = cls(1,1)
            else:
                inst = cls(1)
            inst.update(**dictionary)
            return inst

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances from a JSON file """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                json_string = f.read()
                obj_dicts = Base.from_json_string(json_string)
                return [cls.create(**obj_dict) for obj_dict in obj_dicts]
        except FileNotFoundError:
            return []

