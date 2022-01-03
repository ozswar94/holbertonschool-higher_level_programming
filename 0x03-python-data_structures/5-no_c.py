#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return my_string
    my_string = list(my_string)
    for i in range(len(my_string)):
        if my_string[i] in 'cC':
            my_string[i] = ''
    my_string = ''.join(my_string)
    return my_string
