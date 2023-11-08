#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    index = 0
    for i in new_list:
        if i == search:
            new_list[index] = replace
        index += 1
    return new_list
