#!/usr/bin/python3
"""Module to test the function max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def list_empty(self):
        self.assertIsNone(max_integer([]))
