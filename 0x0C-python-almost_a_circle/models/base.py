#!/usr/bin/python3
"""defining a class"""


import json


class Base:
    """Class Base
    Attributes:
        private class attribute
        id
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """instantiation of class object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method saves list object to a file"""
        if list_objs is None:
            mty_lst = []
            with open('Rectangle.json', 'w') as R:
                json.dump(mty_lst, R)
        else:
            j_list = []
            for obj in list_objs:
                j_string = Base.to_json_string(obj.to_dictionary())
                j_list.append(json.loads(j_string))
            with open('Rectangle.json', 'w') as R:
                json.dump(j_list, R)

    @staticmethod
    def from_json_string(json_string):
        """Method returns the python object/dictionary list"""
        if json_string is None:
            mty_list = []
            return json.loads(json.dumps(mty_list))
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method returns instance with attributes set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        else:
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy