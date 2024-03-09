#!/usr/bin/python3

"""
test_user: This module defines unittest for user class.
Test_userc: This class defines test case for user class.
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class Test_Userc(unittest.TestCase):
    """Defines test cases for the User class."""

    def test_inheritance(self):
        """Check whether the User class inherits from BaseModel class."""
        user = User()

        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """Check whether the attributes of User are exist and initialized."""
        user = User()

        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_to_dict_method(self):
        """Check if the to_dict method returns the expected dictionary
           and the keys and values in the dictionary are correct
        """
        user = User()

        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')


if __name__ == '__main__':
    unittest.main()
