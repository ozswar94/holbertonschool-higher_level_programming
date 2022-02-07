#!/usr/bin/python3
""" Base class """
import json


class Base:
    """
    class Base is a geomtry class base
    Attributes:
        id (int): number of instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor of Base class """
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return JSON representation of an object(string) """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        tmp = []
        if list_objs and len(list_objs):
            for items in list_objs:
                tmp.append(items.to_dictionary())
        inf = cls.to_json_string(tmp)
        with open(str(cls.__name__) + ".json", 'w') as json_file:
            json_file.write(inf)

    @staticmethod
    def from_json_string(json_string):
        if json_string and len(json_string):
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
