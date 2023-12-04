#!/usr/bin/python3
""" module for my_list """


class MyList(list):
    """ subclass of list """
    def print_sorted(self):
        """ prints a sorted list """
        print(sorted(self))
