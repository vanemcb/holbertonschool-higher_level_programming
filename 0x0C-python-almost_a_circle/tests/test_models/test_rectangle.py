""" Module to test Class Rectangle """
import unittest

import models.rectangle
from models.rectangle import Rectangle


class TestClassRectangle(unittest.TestCase):

    def test_docstring_module(self):
        comments_mod = models.rectangle.__doc__
        self.assertTrue(len(comments_mod.splitlines()) > 0)

    def test_docstring_class(self):
        comments_class = Rectangle.__doc__
        self.assertTrue(len(comments_class.splitlines()) > 0)

    def test_shebang(self):
        with open("models/rectangle.py", "r") as file:
            first_line = file.readline()
        self.assertEqual(first_line, '#!/usr/bin/python3\n')

    def test_pep8_style(self):
        import os
        with os.popen("pep8 models/base.py") as mod_file:
            self.assertEqual(mod_file.read(), "")

    def test_init_rectangle(self):
        r1 = Rectangle(63, 20, 3, 4, 56)
        self.assertEqual(r1.width, 63)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 56)

        r2 = Rectangle(10, 15)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 15)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(20, 50)
        self.assertEqual(r3.width, 20)
        self.assertEqual(r3.height, 50)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_setter_getter(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        r1.width = 7
        r1.height = 8
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.height, 8)

    def test_errors(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("5", 4)

        with self.assertRaises(TypeError):
            r2 = Rectangle(5, "4")

        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 4)

        with self.assertRaises(ValueError):
            r4 = Rectangle(-9, 4)

        with self.assertRaises(ValueError):
            r5 = Rectangle(5, 0)

        with self.assertRaises(ValueError):
            r6 = Rectangle(5, -11)

        with self.assertRaises(ValueError):
            r7 = Rectangle(5, 4, 2, -9)

        with self.assertRaises(ValueError):
            r8 = Rectangle(5, 4, -2, 9)

    def test_area(self):
        r1 = Rectangle(3, 5)
        self.assertEqual(r1.area(), 15)

        r2 = Rectangle(2, 50)
        self.assertEqual(r2.area(), 100)

        r3 = Rectangle(20, 3, 8, 9, 23)
        self.assertEqual(r3.area(), 60)
