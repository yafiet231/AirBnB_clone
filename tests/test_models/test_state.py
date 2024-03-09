#!/usr/bin/python3

"""
test_state: This module defines unittest for state class.
Test_Statec: This class defines the test cases of class state.
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class Test_Statec(unittest.TestCase):
    """Defines the test cases for the State class."""

    def test_attributes(self):
        """Check whether the attributes of State are exist and initialized
        to the defualt values.
        """
        state = State()

        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertEqual(state.name, "")

    def test_inheritance(self):
        """Check whether the State inherits from BaseModel."""
        state = State()

        self.assertIsInstance(state, BaseModel)


if __name__ == '__main__':
    unittest.main()
