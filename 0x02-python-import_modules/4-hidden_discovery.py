#!/usr/bin/python3

import hidden_4

for mod in dir(hidden_4):
    if "__" not in mod:
        print("{:s}".format(mod))
