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
    """Defines the serializes and deserializes JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add in __objects obj with key <obj_class_name>.id"""
        obj_cl_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_cl_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        ob_dict = FileStorage.__objects
        obj_dict = {obj: ob_dict[obj].to_dict() for obj in ob_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """If it exists deserialize the JSON file __file_path to __objects."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for ob in obj_dict.values():
                    cls_name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(cls_name)(**ob))
        except FileNotFoundError:
            return
