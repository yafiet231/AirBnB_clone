#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import unittest
from models.engine.file_storage import FileStorage
from models.engine.file_storage import classes
from models.base_model import BaseModel
from models.user import User
import os
import json


class TestFileStorage(unittest.TestCase):
    """test case for the fileStorage class."""

    def setUp(self):
        """prepare the FileStorage instance for each test."""
        self.storage = FileStorage()
        self.tearDown()
        self.classes = ["BaseModel", "User", "Place", "State",
                        "City", "Amenity", "Review"]

    def tearDown(self):
        """Restore fileStorage data."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        self.storage._FileStorage__objects.clear()
        if os.path.isfile(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test__init__(self):
        """Tests the __init__ """

        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), msg)


        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        msg = "FileStorage() takes no arguments"
        self.assertEqual(str(e.exception), msg)

    def test_instanstiation(self):
        """tests instance creation and errors"""
        self.assertEqual(type(self.storage).__name__, "FileStorage")

    def test_new(self):
        """tests adding new objects to the storage."""
        for classname in self.classes:
            cls = classes[classname]
            o = cls()
            self.storage.new(o)
            key = "{}.{}".format(type(o).__name__, o.id)
            self.assertTrue(key in FileStorage._FileStorage__objects)
            self.assertEqual(FileStorage._FileStorage__objects[key], o)


        self.tearDown()
        with self.assertRaises(TypeError) as e:
            self.storage.new()
        msg = "new() missing 1 required positional argument: 'obj'"
        self.assertEqual(str(e.exception), msg)


        self.tearDown()
        base_model = BaseModel()
        with self.assertRaises(TypeError) as e:
            self.storage.new(base_model, 98)
        msg = "new() takes 2 positional arguments but 3 were given"
        self.assertEqual(str(e.exception), msg)
 
    def test_all(self):
        """tests all() the operations."""
        for classname in self.classes:
            self.tearDown()
            self.assertEqual(self.storage.all(), {})
            o = classes[classname]()
            self.storage.new(o)
            key = "{}.{}".format(type(o).__name__, o.id)
            self.assertTrue(key in self.storage.all())
            self.assertEqual(self.storage.all()[key], o)

        with self.assertRaises(TypeError) as e:
            FileStorage.all()
        msg = "all() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            FileStorage.all(self, 0)
        msg = "all() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_save(self):
        """Tests save() operaions."""
        for classname in self.classes:
            self.tearDown()
            cls = classes[classname]
            o = cls()
            self.storage.new(o)
            key = "{}.{}".format(type(o).__name__, o.id)
            self.storage.save()
            self.assertTrue(os.path.isfile
                            (self.storage._FileStorage__file_path))
            d = {key: o.to_dict()}
            with open(self.storage._FileStorage__file_path,
                      "r", encoding="utf-8") as f:
                self.assertEqual(len(f.read()), len(json.dumps(d)))
                f.seek(0)
                self.assertEqual(json.load(f), d)

        with self.assertRaises(TypeError) as e:
            FileStorage.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_reload(self):
        """Tests reload() method."""
        for classname in self.classes:
            self.tearDown()
            self.storage.reload()
            self.assertEqual(self.storage._FileStorage__objects, {})
            cls = classes[classname]
            o = cls()
            self.storage.new(o)
            key = "{}.{}".format(type(o).__name__, o.id)
            self.storage.save()
            self.storage.reload()
            self.assertEqual(o.to_dict(), self.storage.all()[key].to_dict())


            self.tearDown()
            self.storage.reload()
            self.assertEqual(FileStorage._FileStorage__objects, {})
            cls = classes[classname]
            o = cls()
            self.storage.new(o)
            key = "{}.{}".format(type(o).__name__, o.id)
            self.storage.save()
            o.name = "Anything"
            self.storage.reload()
            self.assertNotEqual(o.to_dict(), self.storage.all()[key].to_dict())


        self.tearDown()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload()
        msg = "reload() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)


        self.tearDown()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload(self, 0)
        msg = "reload() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_save_reload(self):
        """Test saving and reloading objects from file."""
        obj1 = BaseModel()
        obj2 = User()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertIn('BaseModel.{}'.format(obj1.id), all_objs)
        self.assertIn('User.{}'.format(obj2.id), all_objs)


if __name__ == '__main__':
    unittest.main()
