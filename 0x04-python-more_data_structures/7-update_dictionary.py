#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for a_key in a_dictionary:
        if a_key == key:
            a_dictionary[a_key] = value
        if key not in a_dictionary:
            a_dictionary[key] = value
        return a_dictionary
