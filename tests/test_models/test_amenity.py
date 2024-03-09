#!/usr/bin/python3

"""
Testing predicted Output from classes.
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_attributes(self):
        """verify that the attributes of Amenity are present and initialized."""
        # Create an instance of Amenity
        amenity = Amenity()

        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertEqual(amenity.name, "")

    def test_inheritance(self):
        """ensure that Amenity inherits from BaseModel."""
        # Create an instance of Amenity
        amenity = Amenity()

        self.assertIsInstance(amenity, BaseModel)

    def test_to_dict_method(self):
        """validate that the to_dict method returns the expected dictionary."""
        # Create an instance of User
        amenity = Amenity()

        amenity_dict = amenity.to_dict()

        self.assertEqual(amenity_dict['__class__'], 'Amenity')


if __name__ == '__main__':
    unittest.main()
