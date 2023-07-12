#!/usr/bin/python3
"""Defines the base model that defines all common methods for other classes"""
import uuid
from datetime import datetime


class BaseModel:
    """Represents the base model of the airbnb project"""
    def __init__(self):
        """Initializes a base model"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the class"""
        clsname = self.__class__.__name__
        print("[{}] ({}) {}".format(clsname, self.id, self.__dict__))

    def save(self):
        """updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary with all keys/values of __dict__"""
