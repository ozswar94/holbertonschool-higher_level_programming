#!/usr/bin/python3
""" say_my_name """


def say_my_name(first_name, last_name=""):
    """ print name

    Args:
        first_name (str): first arg
        last_name (str): seconde arg

    Raises:
        TypeError: If 'first_namr' or 'last_name' is not a str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
