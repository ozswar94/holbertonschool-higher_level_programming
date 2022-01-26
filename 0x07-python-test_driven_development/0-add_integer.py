#!/usr/bin/python3
""" add_integer """


def add_integer(a, b=98):
    """ return a + b

    Args:
        a (int): first arg
        b (int): seconde arg

    Raises:
        TypeError: If 'a' is not a int or float
        TypeError: If 'b' is not a int or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
