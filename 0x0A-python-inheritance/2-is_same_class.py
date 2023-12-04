#!/usr/bin/python3
""" module for is_some_class """


def is_same_class(obj, a_class):
    """ checks  if the object is exactly an instance of the specified class """
    return (type(obj) == a_class)
