#!/usr/bin/python3
"""This module defines the Unittest test cases for the HBNBCommand console.
"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from io import StringIO
from unittest.mock import patch
import console
import os
import unittest


class TestHBNBCommand(unittest.TestCase):
    """
    Define test case for the HBNBCommand console.
    """
    def setUp(self):
        """Sets up test cases."""
        self.tearDown()
        self.input = console.HBNBCommand()
        storage._FileStorage__objects = {}
        self.classes = ["BaseModel", "User", "Place", "State",
                        "City", "Amenity", "Review"]

    def tearDown(self):
        """Resets FileStorage data."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_docstrings(self):
        """
    Check documentation for the strings.

    This method tests the presence of docstrings for various components:
    - Module docstring
    - Class docstring
    - Method docstrings for specific methods

    If any docstring is missing, the test will fail.
    """
        test_cases = [
            ("module doc", console.__doc__),
            ("class doc", self.input.__doc__),
            ("method docs", [
                self.input.default,
                self.input.dict_update,
                self.input.do_EOF,
                self.input.do_quit,
                self.input.emptyline,
                self.input.do_create,
                self.input.do_show,
                self.input.do_destroy,
                self.input.do_all,
                self.input.do_count,
                self.input.do_update,
            ]),
        ]
        for case_name, case in test_cases:
            with self.subTest(case_name):
                if isinstance(case, list):
                    for method in case:
                        self.assertIsNot(method.__doc__)
                else:
                    self.assertIsNot(case)

    def test_do_quit(self):
        """Checks quit commandto exit a console."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.input.onecmd("quit"))
        self.assertEqual(f.getvalue(), '')

    def test_do_EOF(self):
        """Checks EOF commmand, end of file."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(self.input.onecmd("EOF"))
        self.assertEqual(f.getvalue(), '\n')

    def test_emptyline(self):
        """Checks empty line command."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.input.onecmd("\n")
        self.assertEqual(f.getvalue(), '')

    def test_do_create(self):
        """Check the create command.
        and handle for errors.
        """
        for class_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd(f"create {class_name}")
            usrid = f.getvalue()[:-1]
            self.assertTrue(len(usrid) > 0)
            key = (f"{class_name}.{usrid}")

            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd(f"all {class_name}")
            self.assertTrue(usrid in f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("create")
        self.assertEqual(f.getvalue()[:-1], "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("create srhbk")
        self.assertEqual(f.getvalue()[:-1], "** class doesn't exist **")

    def test_do_show(self):
        """Checks show for all classes.
        and handle error.
        """
        for class_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd(f"create {class_name}")
            usrid = f.getvalue().strip()
            self.assertTrue(len(usrid) > 0)

            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd(f"show {class_name} {usrid}")
            strn = f.getvalue().strip()
            self.assertTrue(usrid in strn)

        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("show")
        self.assertEqual(f.getvalue()[:-1], "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd(".show()")
        self.assertEqual(f.getvalue()[:-1], "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("show amtss4")
        self.assertEqual(f.getvalue()[:-1], "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("fkstr7.show()")
        self.assertEqual(f.getvalue()[:-1], "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("show BaseModel")
        self.assertEqual(f.getvalue()[:-1], "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("show BaseModel 12345379359")
        self.assertEqual(f.getvalue()[:-1], "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd('BaseModel.show("12345479053237890")')
        self.assertEqual(f.getvalue()[:-1], "** no instance found **")

    def test_do_destroy(self):
        """Check destroy command."""
        for class_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd("create {}".format(class_name))
            usrid = f.getvalue()[:-1]
            self.assertTrue(len(usrid) > 0)
            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd("destroy {} {}".format(class_name, usrid))
            s = f.getvalue()[:-1]
            self.assertTrue(len(s) == 0)
            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd(".all()")
            self.assertFalse(usrid in f.getvalue())

            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd("create {}".format(class_name))
            usrid = f.getvalue()[:-1]
            self.assertTrue(len(usrid) > 0)
            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd('{}.destroy("{}")'.format(class_name, usrid))
            s = f.getvalue()[:-1]
            self.assertTrue(len(s) == 0)
            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd(".all()")
            self.assertFalse(usrid in f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("destroy")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "** class name missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("destroy dfrs3f")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "** class doesn't exist **")
        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("destroy BaseModel")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "** instance id missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("destroy BaseModel 453grt657msg")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd(".destroy()")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "** class name missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("bgdf7.destroy()")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd('BaseModel.destroy("453grt657msg")')
        message = f.getvalue()[:-1]
        self.assertEqual(message, "** no instance found **")

    def test_do_all(self):
        """Check all command."""
        for class_name in self.classes:
            usrid = self.create_class(class_name)
            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd("all")
            s = f.getvalue()[:-1]
            self.assertTrue(len(s) > 0)
            self.assertIn(usrid, s)
            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd("all {}".format(class_name))
            s = f.getvalue()[:-1]
            self.assertTrue(len(s) > 0)
            self.assertIn(usrid, s)

            usrid = self.create_class(class_name)
            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd("{}.all()".format(class_name))
            s = f.getvalue()[:-1]
            self.assertTrue(len(s) > 0)
            self.assertIn(usrid, s)

        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("all bhsty5ks")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("bhsty5ks.all()")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "** class doesn't exist **")

    def test_do_update(self):
        """Check update command."""
        for class_name in self.classes:
            attr = "foostr"
            val = "fooval"
            usrid = self.create_class(class_name)
            input = f'{class_name}.update("{usrid}", "{attr}", "{val}")'

            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd(input)
            s = f.getvalue()
            self.assertEqual(len(s), 0)
            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd('{}.show("{}")'.format(class_name, usrid))
            s = f.getvalue()
            self.assertIn(attr, s)
            self.assertIn(val, s)

    def test_do_count(self):
        """check count command."""
        for class_name in self.classes:
            for i in range(22):
                usrid = self.create_class(class_name)
            with patch('sys.stdout', new=StringIO()) as f:
                self.input.onecmd("{}.count()".format(class_name))
            s = f.getvalue()[:-1]
            self.assertTrue(len(s) > 0)
            self.assertEqual(s, "22")

        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("bhsty5ks.count()")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "** class doesn't exist **")
        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd(".count()")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "** class name missing **")

    def create_class(self, class_name):
        """Make a class for console tests."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.input.onecmd("create {}".format(class_name))
        usrid = f.getvalue()[:-1]
        self.assertTrue(len(usrid) > 0)
        return usrid


if __name__ == '__main__':
    unittest.main()
