#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return
    my_string = list(my_string)
    for c in my_string:
        if c in 'cC':
            my_string.remove(c)
    my_string = ''.join(my_string)
    return my_string
