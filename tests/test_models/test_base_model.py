#!/usr/bin/python3
"""This module defines unittests for BaseModel class
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_save(unittest.TestCase):
    """Defines the Unittests test cases for save method of the
    BaseModel class.
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_a_save(self):
        p = BaseModel()
        sleep(0.05)
        first_updated_at = p.updated_at
        p.save()
        self.assertLess(first_updated_at, p.updated_at)

    def test_two_saves(self):
        p = BaseModel()
        sleep(0.05)
        first_updated_at = p.updated_at
        p.save()
        second_updated_at = p.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        p.save()
        self.assertLess(second_updated_at, p.updated_at)

    def test_save_w_arg(self):
        p = BaseModel()
        with self.assertRaises(TypeError):
            p.save(None)

    def test_save_updates_file(self):
        p = BaseModel()
        p.save()
        pid = "BaseModel." + p.id
        with open("file.json", "r") as f:
            self.assertIn(pid, f.read())


class TestBaseModel_instantiation(unittest.TestCase):
    """Defines unittests test cases for creation instance of the
    BaseModel class.
    """

    def test_no_args_instantiates(self):
        # Check with no arguments
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objs(self):
        # Check whether the new instance stored in object
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_is_id_public(self):
        # Check id is public instance and string
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_datetime(self):
        # Check datetime of creation
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_datetime(self):
        # Checks datetime of updates
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_models_unique_ids(self):
        # Checks for each models have unique id
        p1 = BaseModel()
        p2 = BaseModel()
        self.assertNotEqual(p1.id, p2.id)

    def test_models_diff_created_at(self):
        # Checks creation of two models differently
        p1 = BaseModel()
        sleep(0.05)
        p2 = BaseModel()
        self.assertLess(p1.created_at, p2.created_at)

    def test_models_diff_updated_at(self):
        # Checks update of two models differently
        p1 = BaseModel()
        sleep(0.05)
        p2 = BaseModel()
        self.assertLess(p1.updated_at, p2.updated_at)

    def test_str_representation(self):
        # Checks for string representations of instances
        dt = datetime.today()
        dt_rep = repr(dt)
        p = BaseModel()
        p.id = "123456"
        p.created_at = p.updated_at = dt
        pstr = p.__str__()
        self.assertIn("[BaseModel] (123456)", pstr)
        self.assertIn("'id': '123456'", pstr)
        self.assertIn("'created_at': " + dt_rep, pstr)
        self.assertIn("'updated_at': " + dt_rep, pstr)

    def test_unused_args(self):
        # Checks for unsused arguments
        p = BaseModel(None)
        self.assertNotIn(None, p.__dict__.values())

    def test_instantiation_w_kwargs(self):
        # checks creation of instance with kwargs
        dt = datetime.today()
        dt_iso = dt.isoformat()
        p = BaseModel(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(p.id, "123")
        self.assertEqual(p.created_at, dt)
        self.assertEqual(p.updated_at, dt)

    def test_instantiation_w_None_kwargs(self):
        # Check for none kwargs from user
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_w_args_and_kwargs(self):
        # Checks creation of instances with both args and kwargs
        dt = datetime.today()
        dt_iso = dt.isoformat()
        p = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(p.id, "345")
        self.assertEqual(p.created_at, dt)
        self.assertEqual(p.updated_at, dt)


class TestBaseModel_to_dict(unittest.TestCase):
    """Define the Unittests for test cases to_dict method of the
    BaseModel class.
    """

    def test_to_dict_type(self):
        # check fo the to_dict type
        p = BaseModel()
        self.assertTrue(dict, type(p.to_dict()))

    def test_to_dict_holds_correct_keys(self):
        # checks whether the dict contains valid values
        p = BaseModel()
        self.assertIn("id", p.to_dict())
        self.assertIn("created_at", p.to_dict())
        self.assertIn("updated_at", p.to_dict())
        self.assertIn("__class__", p.to_dict())

    def test_to_dict_added_attributes(self):
        # Check whether the to _dict conatins new attributes
        p = BaseModel()
        p.name = "Alx"
        p.my_number = 78
        self.assertIn("name", p.to_dict())
        self.assertIn("my_number", p.to_dict())

    def test_to_dict_datetime_are_strs(self):
        # Checks the datetime of the instance are strings
        p = BaseModel()
        p_dict = p.to_dict()
        self.assertEqual(str, type(p_dict["created_at"]))
        self.assertEqual(str, type(p_dict["updated_at"]))

    def test_to_dict_result(self):
        # Checks the output of to_dict
        dt = datetime.today()
        p = BaseModel()
        p.id = "123456"
        p.created_at = p.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(p.to_dict(), tdict)

    def test_contrast_to_dict_under_dict(self):
        p = BaseModel()
        self.assertNotEqual(p.to_dict(), p.__dict__)

    def test_to_dict_w_arg(self):
        p = BaseModel()
        with self.assertRaises(TypeError):
            p.to_dict(None)


if __name__ == "__main__":
    unittest.main()
