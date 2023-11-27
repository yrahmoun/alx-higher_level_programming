#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """defines unittests for max_integer([..])"""

    def test_ordered(self):
        """tests an ordered list"""
        ordered = [5, 6, 7, 8]
        self.assertEqual(max_integer(ordered), 8)

    def test_unordered(self):
        """tests an unordered list"""
        unordered = [4, 1, 8, 3]
        self.assertEqual(max_integer(unordered), 8)

    def test_max_at_start(self):
        """tests a list with max as first value"""
        max_at_start = [8, 3, 5, 1]
        self.assertEqual(max_integer(max_at_start), 8)

    def test_empty_list(self):
        """tests empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_floats(self):
        """tests a list of floats"""
        floats = [2.83, 7.53, 4.12, 10.55, -5.0]
        self.assertEqual(max_integer(floats), 10.55)

    def test_int_and_float(self):
        """tests a list of ints and floats"""
        ints_and_floats = [5, 5.8, 2.3, 12, 4]
        self.assertEqual(max_integer(ints_and_floats), 12)

    def test_string(self):
        """tests one string"""
        string = "abdwsh"
        self.assertEqual(max_integer(string), 'w')

    def test_strings(self):
        """tests a list of strings"""
        strings = ["test", "me", "please"]
        self.assertEqual(max_integer(strings), "test")

    def test_empty_string(self):
        """tests an empty string"""
        self.assertEqual(max_integer(""), None)

    def test_one_element(self):
        """Test a list with a single element."""
        one_element = [3]
        self.assertEqual(max_integer(one_element), 3)

if __name__ == '__main__':
    unittest.main()
