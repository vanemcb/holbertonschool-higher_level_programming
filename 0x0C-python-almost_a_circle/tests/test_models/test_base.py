#!/usr/bin/python3
""" Module to test Class Base """
import unittest

from models.base import Base


class TestClassBase(unittest.TestCase):

    def test_docstring_module(self):
        pass

    def test_docstring_class(self):
        pass

    def test_shebang(self):
        pass

    def test_pep8_style(self):
        import os
        string = os.popen("base.py").read()
        self.assertTrue(string == "")


