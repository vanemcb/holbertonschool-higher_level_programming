""" Module to test Class Base """
import unittest
import models.base


class TestClassBase(unittest.TestCase):

    def test_docstring_module(self):
        comments_mod = models.base.__doc__
        self.assertTrue(len(comments_mod.splitlines()) > 0)

    def test_docstring_class(self):
        comments_class = models.base.Base.__doc__
        self.assertTrue(len(comments_class.splitlines()) > 0)

    def test_shebang(self):
        with open("models/base.py", "r") as file:
            first_line = file.readline()
        self.assertEqual(first_line, '#!/usr/bin/python3\n')

    def test_pep8_style(self):
        import os
        with os.popen("pep8 models/base.py") as mod_file:
            self.assertEqual(mod_file.read(), "")

    def test_id(self):
        base1 = models.base.Base()
        self.assertEqual(base1.id, 1)

        base2 = models.base.Base(None)
        self.assertEqual(base2.id, 2)

        base3 = models.base.Base(460)
        self.assertEqual(base3.id, 460)

        base4 = models.base.Base()
        self.assertEqual(base4.id, 3)
