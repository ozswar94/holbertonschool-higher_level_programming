#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for tab in matrix:
        for nb in tab:
            if not isinstance(nb, int):
                return
    for tab in matrix:
        if len(tab) == 0:
            print()
            return
        for i in range(0, len(tab) - 1):
            print("{:d}".format(tab[i]), end=' ')
        print("{:d}".format(tab[len(tab) - 1]))
