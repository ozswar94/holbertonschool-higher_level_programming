#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dict = sorted(a_dictionary.keys())
    for item in a_dict:
        print("{:s}: {}".format(item, a_dictionary[item]))
