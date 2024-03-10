#!/usr/bin/python3
"""This module defines unittests for class review.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_save(unittest.TestCase):
    """Defines Unittests, test cases for save method of the Review class."""

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
        # Checks review for save and update one class
        review = Review()
        sleep(0.05)
        first_updated_at = review.updated_at
        review.save()
        self.assertLess(first_updated_at, review.updated_at)

    def test_more_saves(self):
        # Checks review for saves and update of two class
        review = Review()
        sleep(0.05)
        first_updated_at = review.updated_at
        review.save()
        second_updated_at = review.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        review.save()
        self.assertLess(second_updated_at, review.updated_at)

    def test_save_w_arg(self):
        # Checks saving review with argument
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)

    def test_save_updates_file(self):
        # Checks save and update review
        review = Review()
        review.save()
        reviewid = "Review." + review.id
        with open("file.json", "r") as f:
            self.assertIn(reviewid, f.read())


class TestReview_instantiation(unittest.TestCase):
    """Defines Unittests test cases for instantiation of the Review class."""

    def test_no_args_instantiates(self):
        # Checks the creation of instance without args
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objs(self):
        # Checks the storage of new created instance in storage
        self.assertIn(Review(), models.storage.all().values())

    def test_is_id_str(self):
        # Checks whether the is is string type
        self.assertEqual(str, type(Review().id))

    def test_created_at_datetime(self):
        # Checks the datetime of creation
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_datetime(self):
        # Checks the datetime of updates
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attributes(self):
        # Checks the place id for its public class attribute
        review = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(review))
        self.assertNotIn("place_id", review.__dict__)

    def test_user_id_is_public_class_attribute(self):
        # Checks the user id for its public class attribute
        review = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(review))
        self.assertNotIn("user_id", review.__dict__)

    def test_text_is_public_class_attribute(self):
        # Checks the text for its public class attribute
        review = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(review))
        self.assertNotIn("text", review.__dict__)

    def test_two_reviews_unique_ids(self):
        # Checks reviews have different unique ids
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_two_reviews_diff_created_at(self):
        # Checks for creation of two reviews differently
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.created_at, review2.created_at)

    def test_two_reviews_different_updated_at(self):
        # Checks for updating of two reviews differently
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.updated_at, review2.updated_at)

    def test_str_representation(self):
        # Checks for string representation of objects
        dt = datetime.today()
        dt_rep = repr(dt)
        review = Review()
        review.id = "123456"
        review.created_at = review.updated_at = dt
        reviewstr = review.__str__()
        self.assertIn("[Review] (123456)", reviewstr)
        self.assertIn("'id': '123456'", reviewstr)
        self.assertIn("'created_at': " + dt_rep, reviewstr)
        self.assertIn("'updated_at': " + dt_rep, reviewstr)

    def test_args_unused(self):
        # Checks for unused arguments
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_instantiation_w_kwargs(self):
        # Checks creation and update of objects with kwargs
        dt = datetime.today()
        dt_iso = dt.isoformat()
        review = Review(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(review.id, "123")
        self.assertEqual(review.created_at, dt)
        self.assertEqual(review.updated_at, dt)

    def test_instantiation_None_kwargs(self):
        # Checks creation and update of objects without kwargs
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_to_dict(unittest.TestCase):
    """Defines the Unittests, test cases for to_dict method
    of the Review class.
    """

    def test_to_dict_type(self):
        # Checks for type , of dict type
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_holds_correct_keys(self):
        # Checks for whether the dict contains correct keys
        review = Review()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("__class__", review.to_dict())

    def test_to_dict_added_attributes(self):
        # Check whether the dict contains new added objects
        review = Review()
        review.middle_name = "Alx"
        review.my_num = 79
        self.assertEqual("Alx", review.middle_name)
        self.assertIn("my_num", review.to_dict())

    def test_to_dict_datetime_are_strs(self):
        # Check for the date time for to_dict are strings
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(str, type(review_dict["id"]))
        self.assertEqual(str, type(review_dict["created_at"]))
        self.assertEqual(str, type(review_dict["updated_at"]))

    def test_to_dict_result(self):
        # Checks the output of the to_dict
        dt = datetime.today()
        review = Review()
        review.id = "123"
        review.created_at = review.updated_at = dt
        tdict = {
            'id': '123',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(review.to_dict(), tdict)

    def test_contrast_to_dict_under_dict(self):
        # Checks dictionary of under dictionary
        review = Review()
        self.assertNotEqual(review.to_dict(), review.__dict__)

    def test_to_dict_w_arg(self):
        # Checks dict with argument
        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict(None)


if __name__ == "__main__":
    unittest.main()
