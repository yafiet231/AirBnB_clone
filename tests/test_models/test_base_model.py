#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

 Testing expected Output from classes.
   Check if the id attribute is not None.
   Create an instance of BaseModel.
   Check if __str__ method returns the expected string representation.
   Get the dictionary representation of the instance.
   Check if the keys and values in the dictionary are correct.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage
from unittest.mock import patch
from io import StringIO
import json
import os


class TestBaseModel(unittest.TestCase):
    """Testing the BaseModel class."""

    def setUp(self):
        """Sets up test cases."""
        self.tearDown()
        storage._FileStorage__objects = {}
        
    def tearDown(self):
        """Resets FileStorage data."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_instanstiation(self):
        """Testing an instance creation and errors."""

        base_model = BaseModel()
        self.assertEqual(str(type(base_model)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(base_model, BaseModel)
        self.assertIsNotNone(base_model.id)

        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_datetime(self):
        """Testing datetime."""
        base_model = BaseModel()
        date_now = datetime.now()
        diff = base_model.updated_at - base_model.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = base_model.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_str_method(self):
        """Testing the expected string output."""
        base_model = BaseModel()
        expected_str = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_str)

    def test_save(self):
        """Testing the save method."""
        base_model = BaseModel()
        with patch('models.storage') as mock_storage:
            base_model.save()
            self.assertTrue(mock_storage.save.called)

        base_model.save()
        key = "{}.{}".format(type(base_model).__name__, base_model.id)
        d = {key: base_model.to_dict()}
        self.assertTrue(os.path.isfile(storage._FileStorage__file_path))
        with open(storage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, "fdg3d")
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_to_dict_method(self):
        """Testing for expected dictionary type output."""

        base_model = BaseModel()
        model_dict = base_model.to_dict()
        self.assertEqual(model_dict['__class__'],
                         'BaseModel')
        self.assertEqual(model_dict['id'],
                         base_model.id)
        self.assertEqual(model_dict['created_at'],
                         base_model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         base_model.updated_at.isoformat())

        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, "egfdh")
        msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()
