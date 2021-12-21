#!/usr/bin/python3

i = 0
j = 1

while i < 9:
    while j < 10:
        if i < j:
            print("{:d}{:d}".format(i, j), end='')
            if i < 8:
                print(', ', end='')
            else:
                print('\n', end='')
        j += 1
    i += 1
    j = 0
