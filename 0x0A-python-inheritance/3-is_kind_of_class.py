#!/usr/bin/python3
""" module for is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """ checks if the object is an instance or inherited instance of a class """
    return (isinstance(obj, a_class))
