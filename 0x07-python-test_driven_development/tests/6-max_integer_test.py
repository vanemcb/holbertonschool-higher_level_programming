#!/usr/bin/python3
"""Module to test the function max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def list_empty(self):
        self.assertEqual(max_integer([]), None)

    def max_end(self):
        list_num = [4, 8, 20]
        self.assertEqual(max_integer(list_num), 20)
