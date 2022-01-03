#!/usr/bin/python3

def max_integer(my_list=[]):
    nb_max = 0
    if len(my_list) == 0:
        return None
    for nb in my_list:
        if nb > nb_max:
            nb_max = nb
    return nb_max
