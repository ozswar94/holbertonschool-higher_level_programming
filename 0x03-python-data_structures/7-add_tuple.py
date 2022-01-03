#!/usr/bin/python
def add_tuple(tuple_a=(), tuple_b=()):
    size_tuple_a = len(tuple_a)
    size_tuple_b = len(tuple_b)
    somme = [0, 0]
    for i in range(len(tuple_a)):
        somme[i] += tuple_a[i]
    for i in range(len(tuple_b)):
        somme[i] += tuple_b[i]
    somme = tuple(somme)
    return somme
