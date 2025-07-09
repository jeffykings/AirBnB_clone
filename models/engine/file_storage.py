#!/usr/bin/python3

""" contains a class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """a  class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return type(self).__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"

        type(self).__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        temp_dict = {}
        for key, value in type(self).__objects.items():
            temp_dict[key] = value.to_dict()

        with open(type(self).__file_path, mode="w",
                  encoding="utf-8") as write_file:
            json.dump(temp_dict, write_file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file
        doesn’t exist, no
        exception should be raised)
        """
        try:
            with open(type(self).__file_path, mode="r",
                      encoding="utf-8") as read_file:
                obj_dict = json.load(read_file)
                for key, value in obj_dict.items():
                    type(self).__objects[key] = BaseModel(**value)

        except FileNotFoundError:
            pass
