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
