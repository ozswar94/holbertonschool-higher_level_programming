#!/usr/bin/python3

import sys

if __name__ == "__main__":
    nb = 0

    for i in range(1, len(sys.argv)):
        nb += int(sys.argv[i])

    print("{:d}".format(nb))
