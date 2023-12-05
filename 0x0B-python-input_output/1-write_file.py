#!/usr/bin/python3
""" module for write_file """


def write_file(filename="", text=""):
    """ writes to file """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
