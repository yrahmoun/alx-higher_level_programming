#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    new_list = list(a_dictionary.values())
    max_value = new_list[0]
    for val in new_list:
        if val > max_value:
            max_value = val
    for key in a_dictionary:
        if a_dictionary[key] == max_value:
            return key
