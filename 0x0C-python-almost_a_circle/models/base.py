#!/usr/bin/python3
""" the base module """
import json


class Base():
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization of id """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ representation of Json string list dictionaries """
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writ representation of Json string of lists objects """
        filename = cls.__name__ + ".json"
        j_list = [o.to_dictionary() for o in list_objs]
        j_str = cls.to_json_string(j_list)

        with open(filename, "w") as f:
            f.write(j_str)

    @staticmethod
    def from_json_string(json_string):
        """ json string representation """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ already set attributes of an instance """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                read_data = f.read()
                dict_list = cls.from_json_string(read_data)
                return [cls.create(**dict_1i) for dict_li in dict_list]
        except FileNotFoundError:
            return []
