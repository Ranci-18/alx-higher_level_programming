#!/usr/bin/python3
"""defining a class"""


import json
import os
import csv


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
        """Method returns json string from a dictionary list"""
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

    @classmethod
    def load_from_file(cls):
        """Method returns a list of instances"""
        j_file = cls.__name__ + ".json"

        if os.path.exists(j_file) is False:
            return []
        with open(j_file, 'r') as file:
            dct_str = file.read()

        dct_lst = cls.from_json_string(dct_str)

        return [cls.create(**dct) for dct in dct_lst]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method serializes data to csv format"""
        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if cls.__name__ == 'Rectangle':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width,
                                     obj.height, obj.x, obj.y])
            else:
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Method deserializes from csv file"""
        filename = cls.__name__ + ".csv"

        lst_obj = []
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if cls.__name__ == 'Rectangle':
                    dct = {'id': int(row[0]), 'width': int(row[1]),
                           'height': int(row[2]), 'x': int(row[3]),
                           'y': int(row[4])}
                elif cls.__name__ == 'Square':
                    dct = {'id': int(row[0]), 'size': int(row[1]),
                           'x': int(row[2]), 'y': int(row[3])}
                obj = cls.create(**dct)
                lst_obj.append(obj)
        return lst_obj
