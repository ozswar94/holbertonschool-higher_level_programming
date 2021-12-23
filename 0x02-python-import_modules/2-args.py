#!/usr/bin/python3

import sys

if __name__ == "__main__":
    nb_argv = len(sys.argv)

    if nb_argv == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(nb_argv - 1))

    for i in range(1, nb_argv):
        print("{:d}: {:s}".format(i, sys.argv[i]))
