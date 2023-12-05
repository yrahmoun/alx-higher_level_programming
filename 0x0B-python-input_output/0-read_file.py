#!/usr/bin/python3
""" module for read_file """


def read_file(filename=""):
    """ reads a file """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
