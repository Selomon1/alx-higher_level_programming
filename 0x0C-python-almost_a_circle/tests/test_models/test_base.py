#!/usr/bin/python3
""" unitest for Base class """

import unitest
import models.base as base


class TestBase(unitest.TestBase):
    """ TestBase classs """
    def test_module_doc(self):
        """ documentation test """
        self.assertIsNotNone(base.__doc__)
        self.assertGreater(len(base.__doc__), 0)

    def test_class_doc(self):
        """ class documentation test """
        self.assertIsNotNone(base.Base.__doc__)
        self.assertGreater(len(base.Base.__doc__), 0)

    def test_method_doc(self):
        """ method documentation test """
        self.assertIsNotNone(base.Base.__init__.__doc__)
        self.assertGreater(len(base.Base.__init__.__doc__), 0)

    def test_to_json_string_doc(self):
        """ static method documentation test """
        self.assertIsNotNone(base.Base.to_json_string.__doc__)
        self.assertGreater(len(base.Base.to_json_string.__doc__), 0)

    def setup_test_case(self):
        """set up by resetting the __nb_objects to 0 test """
        base.Base._Base__nb_objects = 0

    def test_id_if_none(self):
        """ to test if id is None """
        i1 = base.Base(None)
        i2 = base.Base()
        self.assertEqual(i1.id, i2.id - 1)
    
    def test_id_for_incr(self):
        """ to test if id incremented by 1 """
        i1 = base.Base()
        i2 = base.Base()
        self.assertEqual(i1.id, i2.id - 1)

    def test_for_args(self):
        """ to test for more than 1 id """
        with self.assertRaises(TypeError):
            base.Base(3, 8)

    def test_for_bool(self):
        """ boolean value test """
        self.assertEqual(base.Base(True).id, True)

    def test_for_str(self):
        """ string test """
        self. assertEqual(base.Base("hello").id, "hello")

    def test_private_attr(self):
        """ accessing private attribute test """
        with self.assertRaises(AttributeError):
            base.Base(5).__nb_objects


class TestBase_to_json_string(unitest.TestCase):
    """ the to_json_string method test """
    def test_to_json_string_emp(self):
        """ the to_json_string with empty list test """
        emp_str = base.Base.to_json_string([])
        self.assertIsInstance(emp_str, str)
        self.assertEqual(emp_str, "[]")

    def test_to_json_str_no_args(self):
        """ the to_json_string without an argument test """
        with self.assertRaises(TypeError):
            base.Base.to_json_string()

    def test_to_json_string_none(self):
        """ the to_json_string with none """
        self.assertEqual(base.Base.to_json_string(None), "[]")

    def test_to_json_string_no_args(self):
        """ the to_json_string with more than one argument test """
        with self.assertRaises(TypeError):
            base.Base.to_json_string([], 5)

class TestBase_from_json_string(unitest.TestCase):
    """ the from_json_string to the method test """
    def test_from_json_string_none(self):
        """ from_json_string with None test """
        self.assertEqual(base.Base.from_json_string(None), [])

    def test_from_json_string_args(self):
        """ from_json_string with more than 1 argument test """
        with self.assertRaises(TypeError):
            base.Base.from_json_string([], 5)

    def test_from_json_string_no_args(self):
        """ from_json_string without arguments test """
        with self.assertRaises(TypeError):
            base.Base.from_json_string()


if __name__ == "__main__":
    unitest.main()
