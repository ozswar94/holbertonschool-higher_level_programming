#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        print("{:s}".format(text[i]), end="")
        if text[i] in ".?:":
            print("\n\n", end="")
