#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    New_dict = {}
    for i in a_dictionary:
        New_value = (a_dictionary.get(i)) * 2
        New_dict.update({i: New_value})
    return (New_dict)
