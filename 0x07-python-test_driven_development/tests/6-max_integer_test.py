#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(None, max_integer([]))
        self.assertEqual(9, max_integer([4, 5, 6, 9]))
        self.assertEqual(None, max_integer())
        self.assertEqual(4, max_integer([4]))
        self.assertNotEqual(8, max_integer([10, 2, 7, 8]))
