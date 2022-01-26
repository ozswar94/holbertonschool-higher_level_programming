#!/usr/bin/python3
""" text_indentation """


def text_indentation(text):
    """ print text indent

    Args:
        text (str): text print

    Raises:
        TypeError: If 'text' is not a str
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print("{:s}".format(text[i]), end="")
        if text[i] in ".?:":
            print("\n\n", end="")
            if i + 1 < len(text):
                while text[i + 1] == ' ':
                    i += 1
        i += 1
