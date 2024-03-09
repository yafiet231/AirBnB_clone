#!/usr/bin/python3

"""File_storage: This module defines the BaseModel class for HBnB project.
Class: FileStorage: That serializes instances to a JSON file and deserializes
JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Serializes and deserializes JSON file
       Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of objects.
    """
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
         Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        my_dict = {}
        for key, obj in self.__objects.items():
            my_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                des_obj = json.load(f)
                for key, obj_dict in my_dict.items():
                    class_name = obj_dict['__class__']
                    self.__objects[key] = class_dict[class_name](**obj_dict)
        except FileNotFoundError:
            pass
