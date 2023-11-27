#!/usr/bin/python3
""" module for text_indentation method """

def text_indentation(text):
    """ prints a text with 2 new lines after certain characters
    Aegs:
        text: text to print
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in text:
        print(c, end='')
        if c in ".:?":
            print("\n")
