#!/usr/bin/python3

"""
test_city: This module defines unittest test for city class.
Test_City: This class defines test case for the class city.
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class Test_Cityc(unittest.TestCase):
    """Defines test cases for the City class."""

    def test_attributes(self):
        """Check whether the attributes of City are exist and initialized
           to default values
        """
        city = City()

        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_inheritance_from_BaseModel(self):
        """Check whether City inherits from BaseModel."""
        city = City()

        self.assertIsInstance(city, BaseModel)


if __name__ == '__main__':
    unittest.main()
