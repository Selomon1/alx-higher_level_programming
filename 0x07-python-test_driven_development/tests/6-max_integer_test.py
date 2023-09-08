#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Testing TestCase for the max_integer function """

    def test_normali(self):
        """ Test normal lists of positive integers """
        result = max_integer([4, 7, 9, 3, 1])
        self.assertEqual(result, 9)

    def  test_negative(self):
        """ Test normal lists of negative integers """
        result = max_integer([-6, -9, -2, -12])
        self.assertEqual(result, -2)

    def test_empty(self):
        """ Test empty list """
        result = max_integer([])
        self.assertEqual(result, None)

    def test_max_equal(self):
        """ Test list of integers with equal max """
        result = max_integer([9, 6, 12, 1, 12])
        self.assertEqual(result, 12)

    def test_float(self):
        """ Test list of float """
        result = max_integer([2.5, 0.33, 0.67, 7.9])
        self.assertEqual(result, 7.9)

    def test_one_list(self):
        """ Test only one list """
        result = max_integer([17])
        self.assertEqual(result, 17)

    def test_string(self):
        """ Test string in the list """
        with self.assertRaises(TypeError):
            result = max_integer([4, '7', 'So', 9])

    def test_non(self):
        """ Test list including None """
        with self.assertRaises(TypeError):
            result = max_integer([None, 4.5, '4', 'x'])
    def test_Zero(self):
        """ Test list of zero """
        result = max_integer([0, 0, 0, 0, 0])
        self.assertEqual(result, 0)

    def test_int_float(self):
        " Test list of integer and float """
        result = max_integer([2.4, 6, 7.8, 3])
        self.assertEqual(result, 7.8)

    def test_sets(self):
        with self.assertRaises(TypeError):
            result = max_integer({2, 3}, {5, 6})


if __name__ == '__main__':
    unittest.main()
