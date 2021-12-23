#!/usr/bin/python3

import sys

nb = 0

for i in range(1, len(sys.argv)):
    nb += int(sys.argv[i])

print("{:d}".format(nb))
