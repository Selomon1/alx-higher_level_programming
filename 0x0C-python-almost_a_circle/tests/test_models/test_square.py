#!/usr/bin/python3
""" square class module """
import unitest
import models.square as sq
import models.base as base


class TestSquare(unitest.TestCase):
    """ Square class test """
    def test_module_doc(self):
        """ documentation module test """
        self.assertIsNotNone(sq.__doc__)
        self.assertGreater(len(sq.__doc__), 0)

    def test_class_doc(self):
        """ class documentation test """
        self.assertIsNotNone(sq.__doc__)
        self.assertGreater(len(sq.__doc__), 0)

    def test_init_doc(self):
        """ initialization comentation test """
        self.assertIsNotNone(sq.Square.__init__.__doc__)
        self.assertGreater(len(sq.Square.__init__.__doc__), 0)

    def test_update_doc(self):
        """ update documentation test """
        self.assertIsNotNone(sq.Square.update.__doc__)
        self.assertGreater(len(sq.Square.update.__doc__), 0)

    def test_to_dictionary_doc(self):
        """ the to_dictionary documentation testing """
        self.assertIsNotNone(sq.Square.to_dictionary.__doc__)
        self.assertGreater(len(sq.Square.to_dictionary.__doc__), 0)

    def test_square_base(self):
        """ test if square is an instance of base """
        self. assertIsInstance(sq.Square(20), base.Base)

    def test_square_with_no_arg(self):
        """ Square without argument test """
        with self.assertRaises(TypeError):
            sq.Square()

    def test_1_arg(self):
        """ Square with one argument testing """
        s1 = sq.Square(20)
        s2 = sq.Square(21)
        self.assertEqual(s1.id, s2.id - 1)

    def test_2_arg(self):
        """ Square with two arguments test """
        s1 = sq.Square(20, 4)
        s2 = sq.Square(4, 20)
        self.assertEqual(s1.id, s2.id - 1)

    def test_3_arg(self):
        """ Square withith 3 arguments test """
        s1 = sq.Square(20, 4, 4)
        s2 = sq.Square(4, 4, 20)
        self.assertEqual(s1.id, s2.id - 1)

    def test_4_arg(self):
        """ Square with 4 arguments tes """
        self.assertEqual(9, sq.Square(20, 4, 4, 9).id)

    def test_more_than_4(self):
        """ access to private attributes of sixe """
        with self.assertRaises(TypeError):
            sq.Square(2, 3, 4, 5, 6)

    def test_size_priv_attr(self):
        """ access private attribute testing """
        with self.assertRaises(AttributeError):
            print(sq.Square(3, 5, 8, 9).__size)

    def test_size_none(self):
        """ size with none testing """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.Square(None)

    def test_size_str(self):
        """ size with string """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.Square("hello")

    def test_size_float(self):
        """ sixe with float test """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.Square(7.8)

    def test_size_list(self):
        """ size with list test """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.Square([4, 5, 6])

    def test_x_none(self):
        """ x with none test """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.Square(4, None)

    def test_x_str(self):
        """ x with string testing """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.Square(7, "hello")

    def test_x_float(self):
        """ x with float test """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.Square(4, 6.7)

    def test_x_list(self):
        """ x with list test """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.Square(4, [4, 5, 6])

    def test_y_none(self):
        """ y with none test """
        with self.assertRaisesRegex(Typeerror, "y must be an integer"):
            sq.Square(4, 5, None)

    def test_y_str(self):
        """ y with string test """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.Square(4, 5, "hello")

    def test_y_float(self):
        """ y with float test """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.Square(4, 5, 7.8)

    def test_y_list(self):
        """ y with list test """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.Square(4, 5, [6, 7, 8])

    def test_area(self):
        """ area test """
        s1 = sq.Square(7, 0, 0, [4])
        s1.size = 23
        s1.x = 7
        s1.y = 20
        self.assertEqual("[Square] (78) 7/9 - 5", str(s1))

    def test_update_arg(self):
        """ update arg method of square class """
        s1 = sq.Square(20, 30, 40, 50)
        s1.update(78, 3, 4, 5)
        s1.update(5, 4, 3, 78)
        self.assertEqual("[Square] (5) 3/78 - 4", str(s1))

    def test_update_kwargs(self):
        """ kwargs method square class test """
        s1 = sq.Square(20, 30, 40, 50)
        s1.update(id=78, x=1)
        s1.update(y=4, x-24, size=2)
        self.assertEqual("[Square] (78) 24/4 - 2", str(s1))

    def test_to_dictionary(self):
        """ to_dictionary method square class test """
        s1 = sq.Square(20, 3, 1, 1)
        res = {'id': 1, 'x': 3, 'size': 20, 'y': 1}
        self.assertDictEqual(res, s1.to_dictionary())


if __name__ = "__main__":
    unitest.main()
