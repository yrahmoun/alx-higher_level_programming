#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev_value = 0
    for i in roman_string:
        if roman[i] > prev_value:
            res += roman[i] - 2 * prev_value
        else:
            res += roman[i]
        prev_value = roman[i]
    return res
