#!/usr/bin/python3
""" Student """


class Student:
    """
    Class Student

    Attributes:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of student
    """
    def __init__(self, first_name, last_name, age):
        """constructor of class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return class in format dictionary"""
        if not attrs:
            return self.__dict__
        dict_json = {}
        for ele in attrs:
            if ele in self.__dict__:
                dict_json[ele] = self.__dict__[ele]
        return dict_json
