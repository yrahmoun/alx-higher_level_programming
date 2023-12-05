#!/usr/bin/python3
"""module for class_to_json"""


def class_to_json(obj):
    """returns the dictionary represntation for JSON serialization of an object"""
    return obj.__dict__
