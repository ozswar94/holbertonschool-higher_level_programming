#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    nb_max = my_list[0]
    for nb in my_list:
        if nb > nb_max:
            nb_max = nb
    return nb_max
