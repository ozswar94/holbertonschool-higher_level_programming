#!/usr/bin/python3
def print_square(size):
    """ print square with #

    Args:
        size (int): size of square

    Raises:
        TypeError: If 'size' is not an int
        ValueError: If 'size' < 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
