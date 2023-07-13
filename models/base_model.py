#!/usr/bin/python3
"""Defines the base model that defines all common methods for other classes"""
import uuid
from datetime import datetime


class BaseModel:
    """Represents the base model of the airbnb project"""
    def __init__(self, *args, **kwargs):
        """Initializes a base model

        Args:
        *args (any): unused
        **kwargs (dict): dictionary of attributes
        """
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, tformat)
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the class"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """returns a dictionary with all keys/values of __dict__"""
        ndict = self.__dict__.copy()
        ndict["created_at"] = self.created_at.isoformat()
        ndict["updated_at"] = self.updated_at.isoformat()
        ndict["__class__"] = self.__class__.__name__
        return ndict
