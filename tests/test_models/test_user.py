#!/usr/bin/python3
"""This module defines unittests for class user.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_save(unittest.TestCase):
    """Defines Unittests test cases for save method of the  class."""

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

    def test_a_save(self):
        u = User()
        sleep(0.05)
        first_updated_at = u.updated_at
        u.save()
        self.assertLess(first_updated_at, u.updated_at)

    def test_two_saves(self):
        u = User()
        sleep(0.05)
        first_updated_at = u.updated_at
        u.save()
        second_updated_at = u.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        u.save()
        self.assertLess(second_updated_at, u.updated_at)

    def test_save_w_arg(self):
        u = User()
        with self.assertRaises(TypeError):
            u.save(None)

    def test_save_updates_file(self):
        u = User()
        u.save()
        uid = "User." + u.id
        with open("file.json", "r") as f:
            self.assertIn(uid, f.read())


class TestUser_instantiation(unittest.TestCase):
    """ Defines Unittests test clases for instantiation of the User class."""

    def test_no_args_instantiates(self):
        # Checks for creation of instances of the user
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objs(self):
        # Checks whether the new instance created stored in storage
        self.assertIn(User(), models.storage.all().values())

    def test_is_id_str(self):
        # Checks whether the id string
        self.assertEqual(str, type(User().id))

    def test_created_at_datetime(self):
        # Checks the datetime of creation
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_datetime(self):
        # Checks the datetime of update
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_str(self):
        # Checks email if it is string
        self.assertEqual(str, type(User.email))

    def test_password_is_str(self):
        # Checks password if it is string
        self.assertEqual(str, type(User.password))

    def test_first_name_is_str(self):
        # Checks name if it is string
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        # Checks name if it is string
        self.assertEqual(str, type(User.last_name))

    def test_users_unique_ids(self):
        # Checks user id unique
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    def test_two_users_diff_created_at(self):
        # Check creation two user at different
        u1 = User()
        sleep(0.05)
        u2 = User()
        self.assertLess(u1.created_at, u2.created_at)

    def test_two_users_diff_updated_at(self):
        # Checks for updating two users differently
        u1 = User()
        sleep(0.05)
        u2 = User()
        self.assertLess(u1.updated_at, u2.updated_at)

    def test_str_representation(self):
        # Checks for string representation
        dt = datetime.today()
        dt_rep = rep(dt)
        u = User()
        u.id = "123456"
        u.created_at = u.updated_at = dt
        ustr = u.__str__()
        self.assertIn("[User] (123456)", ustr)
        self.assertIn("'id': '123456'", ustr)
        self.assertIn("'created_at': " + dt_rep, usstr)
        self.assertIn("'updated_at': " + dt_rep, usstr)

    def test_args_unused(self):
        # Checks for unused args
        u = User(None)
        self.assertNotIn(None, u.__dict__.values())

    def test_instantiation_w_kwargs(self):
        # Checks for kwargs
        dt = datetime.today()
        dt_iso = dt.isoformat()
        u = User(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(u.id, "123")
        self.assertEqual(u.created_at, dt)
        self.assertEqual(u.updated_at, dt)

    def test_instantiation_w_None_kwargs(self):
        # Checks for none kwargs
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)



class TestUser_to_dict(unittest.TestCase):
    """Defines the Unittests test cases for to_dict method of the User class."""

    def test_to_dict_type(self):
        # Checks the type of to_dict
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_holds_correct_keys(self):
        # Checks the to_dict contains valid values 
        u = User()
        self.assertIn("id", u.to_dict())
        self.assertIn("created_at", u.to_dict())
        self.assertIn("updated_at", u.to_dict())
        self.assertIn("__class__", u.to_dict())

    def test_to_dict_added_attributes(self):
        # Checks the new added attributes
        u = User()
        u.middle_name = "Alx"
        u.my_num = 79
        self.assertEqual("Alx", u.middle_name)
        self.assertIn("my_num", u.to_dict())

    def test_to_dict_strs(self):
        # Checks the type of to_dict
        u = User()
        u_dict = u.to_dict()
        self.assertEqual(str, type(u_dict["id"]))
        self.assertEqual(str, type(u_dict["created_at"]))
        self.assertEqual(str, type(u_dict["updated_at"]))

    def test_to_dict_result(self):
        dt = datetime.today()
        us = User()
        us.id = "123456"
        u.created_at = u.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(u.to_dict(), tdict)

    def test_contrast_to_dict_under_dict(self):
        u = User()
        self.assertNotEqual(u.to_dict(), u.__dict__)

    def test_to_dict_with_arg(self):
        u = User()
        with self.assertRaises(TypeError):
            u.to_dict(None)


if __name__ == "__main__":
    unittest.main()
