#!/usr/bin/python3
"""Module to test the function max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_list_empty(self):
        self.assertIsNone(max_integer([]))

    def test_max_end(self):
        list_num = [4, 8, 20]
        self.assertEqual(max_integer(list_num), 20)

    def test_max_deginning(self):
        list_num = [20, 4, -1, 8]
        self.assertEqual(max_integer(list_num), 20)

    def test_max_middle(self):
        list_num = [4, 36, 102, -8, 20]
        self.assertEqual(max_integer(list_num), 102)

    def test_negative_numbers(self):
        list_num = [-4, -8, -20]
        self.assertEqual(max_integer(list_num), -4)

    def test_one_element(self):
        list_num = [6]
        self.assertEqual(max_integer(list_num), 6)
