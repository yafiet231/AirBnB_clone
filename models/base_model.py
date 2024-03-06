#!/usr/bin/python3

"""
Base_model: This module(ifile) defines BaseModel class for HBnB project.

Class: BaseModel which is a base model for classes with same/common
attributes and methods in the HBnB project and defines all common
attributes/methods for other classes.
"""
from datetime import datetime
from models import storage
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes to create an instance for the BaseModel class.
        """
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) !=0 :
            if "__class__" in kwargs:
                del kwargs["__class__"]
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     tformat)
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     tformat)

            # Assign the values to keys
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
            storage.save()

    def __str__(self):
        """
        Prints a string representation of the instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute`updated_at`
        with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of `__dict__` of the
        instance
        """
        bm_dict = self.__dict__.copy()
        bm_dict['__class__'] = self.__class__.__name__
        bm_dict['created_at'] = self.created_at.isoformat()
        bm_dict['updated_at'] = self.updated_at.isoformat()
        return bm_dict
