#!/usr/bin/python3
"""Contains the file storage class"""

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                from models.base_model import BaseModel
                from models.user import User  # Import User class
                classes = {"BaseModel": BaseModel, "User": User}
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    class_ = classes[class_name]
                    obj = class_(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
