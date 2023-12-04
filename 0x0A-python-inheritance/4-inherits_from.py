#!/usr/bin/python3
""" module for nherits from """


def inherits_from(obj, a_class):
    """ checks if object is inherited """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
