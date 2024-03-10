#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for instantiation of the City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        c = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(c))
        self.assertNotIn("state_id", c.__dict__)

    def test_name_is_public_class_attribute(self):
        c = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(c))
        self.assertNotIn("name", c.__dict__)

    def test_two_cities_unique_ids(self):
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)

    def test_two_cities_different_created_at(self):
        c1 = City()
        sleep(0.05)
        c2 = City()
        self.assertLess(c1.created_at, c2.created_at)

    def test_two_cities_different_updated_at(self):
        c1 = City()
        sleep(0.05)
        c2 = City()
        self.assertLess(c1.updated_at, c2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        c = City()
        c.id = "123456"
        c.created_at = c.updated_at = dt
        cstr = c.__str__()
        self.assertIn("[City] (123456)", cstr)
        self.assertIn("'id': '123456'", cstr)
        self.assertIn("'created_at': " + dt_repr, cstr)
        self.assertIn("'updated_at': " + dt_repr, cstr)

    def test_args_unused(self):
        c = City(None)
        self.assertNotIn(None, c.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        c = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(c.id, "345")
        self.assertEqual(c.created_at, dt)
        self.assertEqual(c.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        c = City()
        sleep(0.05)
        first_updated_at = c.updated_at
        c.save()
        self.assertLess(first_updated_at, c.updated_at)

    def test_two_saves(self):
        c = City()
        sleep(0.05)
        first_updated_at = c.updated_at
        c.save()
        second_updated_at = c.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        c.save()
        self.assertLess(second_updated_at, c.updated_at)

    def test_save_with_arg(self):
        c = City()
        with self.assertRaises(TypeError):
            c.save(None)

    def test_save_updates_file(self):
        c = City()
        c.save()
        cid = "City." + c.id
        with open("file.json", "r") as f:
            self.assertIn(cid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        c = City()
        self.assertIn("id", c.to_dict())
        self.assertIn("created_at", c.to_dict())
        self.assertIn("updated_at", c.to_dict())
        self.assertIn("__class__", c.to_dict())

    def test_to_dict_contains_added_attributes(self):
        c = City()
        c.middle_name = "Holberton"
        c.my_number = 98
        self.assertEqual("Holberton", c.middle_name)
        self.assertIn("my_number", c.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        c = City()
        c_dict = c.to_dict()
        self.assertEqual(str, type(c_dict["id"]))
        self.assertEqual(str, type(c_dict["created_at"]))
        self.assertEqual(str, type(c_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        c = City()
        c.id = "123456"
        c.created_at = c.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(c.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        c = City()
        self.assertNotEqual(c.to_dict(), c.__dict__)

    def test_to_dict_with_arg(self):
        c = City()
        with self.assertRaises(TypeError):
            c.to_dict(None)


if __name__ == "__main__":
    unittest.main()
