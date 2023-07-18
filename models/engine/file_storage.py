#!/usr/bin/python3
"""Contains the file storage class"""
import json
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
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    class_ = eval(class_name)
                    self.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass
