#!/usr/bin/python3

"""
Testing predicted Output from classes.
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
        """Test cases for the Review class."""

    def test_attributes(self):
        """check if the attributes of Review are present and initialized."""
        # Create an instance of Review
        review = Review()

        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_inheritance(self):
        """check if Review inherits from BaseModel."""
        # Create an instance of Review
        review = Review()

        self.assertIsInstance(review, BaseModel)

    def test_to_dict_method(self):
        """check if the to_dict method returns the expected dictionary."""
        # Create an instance of Review
        review = Review()

        review_dict = review.to_dict()

        self.assertEqual(review_dict['__class__'], 'Review')


if __name__ == '__main__':
    unittest.main()
