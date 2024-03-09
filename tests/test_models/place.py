#!/usr/bin/python3

"""
Tests predicted Output from classes.
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_attributes(self):
        """check if the attributes of Place are present and initialized."""
        # Create an instance of Place
        place = Place()

        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_inheritance(self):
        """check if place derives from BaseModel."""
        # Create an instance of Place
        place = Place()

        # Check if Place derives from BaseModel
        self.assertIsInstance(place, BaseModel)

    def test_to_dict_method(self):
        """Check if the to_dict method returns the predicted dictionary."""
        # Create an instance of Place
        place = Place()

        place_dict = place.to_dict()

        self.assertEqual(place_dict['__class__'], 'Place')


if __name__ == '__main__':
    unittest.main()
