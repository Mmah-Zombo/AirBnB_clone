#!/usr/bin/python3
"""Contains the file storage class"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """the file storage class

    Attributes:
    __file_path (str): the path to the file and its name
    __objects (str): a dictionary of instatiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        obj_class_name = obj.__class_.__name__
        k = "{}.{}".format(obj_class_name, obj.id)
        self.__objects[k] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()

        with open("file.json", "w") as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as fname:
                l_json = json.load(fname)
                for key, val in l_json.items():
                    FileStorage.__objects[key] = eval(
                        val['__class__'])(**val)
