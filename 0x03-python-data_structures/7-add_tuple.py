#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    somme = [0, 0]
    size = 0
    for i in range(len(tuple_a)):
        if size < 2:
            somme[i] += tuple_a[i]
            size += 1
    size = 0
    for i in range(len(tuple_b)):
        if size < 2:
            somme[i] += tuple_b[i]
            size += 1
    somme = tuple(somme)
    return somme
