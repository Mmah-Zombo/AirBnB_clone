#!/usr/bin/python3
"""Contains the file storage class"""
import json
import os


class FileStorage:
    "the file storage class"
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
        with open("file.json", "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path) as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    class_obj = eval(class_name)
                    instance = class_obj(**obj_data)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
