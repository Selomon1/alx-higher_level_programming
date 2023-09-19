#!/usr/bin/python3
""" rectangle class module """


import unitest
import models.base as base
import models.rectangle as rec


class Testrectangle(unitest.TestCase):
    """ rectangle class test """
    def test_module_doc(self):
        """ documentation module test """
        self.assertIsNotNone(rec.__doc__)
        self.assertGreater(len(rec.__doc__), 0)

    def test_class_doc(self):
        """ documentation class test """
        self.assertIsNotNone(rec.Rectangle.__doc__)
        self.assertGreater(len(rec.Rectangle.__doc__), 0)

    def test_init_met_doc(self):
        """ initialization documentation test """
        self.assertIsNotNone(rec.Rectangle.__init__.__doc__)
        self.assertGreater(len(rec.Rectangle.__init__.__doc__), 0)

    def test_area_doc(self):
        """ area method test """
        self.assertIsNotNone(rec.Rectangle.area.__doc__)
        self.assertGreater(len(rec.Rectangle.area.__doc__), 0)

    def test_update_doc(self):
        """ update method test """
        self.assertIsNotNone(rec.Rectangle.update.__doc__)
        self.assertGreater(len(rec.Rectangle.update.__doc__), 0)

    def test_to_dictionary_doc(self):
        """ dictionary method test """
        self.assertIsNotNone(rec.Rectangle.to_dictionary.__doc__)
        self.assertGreater(len(rec.Rectangle.to_dictionary.__doc__), 0)

    def test_display_doc(self):
        """ display documentation test """
        self.assertIsNotNone(rec.Rectangle.display.__doc__)
        self.assertGreater(len(rec.Rectangle.display.__doc__), 0)

    def setup_test(self):
        """ reset id """
        base.Base._Base__nb_objects = 0

    def test_rectangle_base(self):
        """ rectangle if it is instance of base testing """
        self.assertIsInstance(rec.Rectangle(3, 2), base.Base)

    def test_with_no_arg(self):
        """ rectangle with no arument test """
        with self.assetRaises(TypeError):
            rec.Rectangle()

    def test_with_more_args(self):
        """ 1 and more than 1 arguments testing """
        r1 = rec.Rectangle(3, 2)
        r2 = rec.Rectangle(2, 3)
        r3 = rec.Rectangle(4, 4, 8)
        r4 = rec.Rectangle(8, 8, 4)
        r5 = rec.Rectangle(1, 2, 3, 4)
        r6 = rec.Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r3.id, r4.id - 1)
        self.assertEqual(r5.id, r6.id - 1)
        self.assertEqual(9, rec.Rectangle(3, 2, 0, 0, 9).id)

    def test_width_priv(self):
        """ access to private width test """
        with self.assertRaises(AttributeError):
            print(rec.Rectangle(3, 3, 0, 0, 1).__width)

    def test_height_priv(self):
        """ access to private height test """
        with self.assertRaises(AttributeError):
            print(rec.Rectangle(3, 3, 0, 0, 1).__height)

    def test_x_priv(self):
        """ access private x test """
        with self.assertRaises(AttributeError):
            print(rec.Rectangle(3, 3, 0, 0, 1).__x)

    def test_y_priv(self):
        """ access private y test """
        with self.assertRaises(AttributeError):
            print(rec.Rectangle(3, 3, 0, 0, 1).__y)
    
    def test_wid_none(self):
        """ width with None test """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.Rectangle(None, 3)

    def test_wid_str(self):
        """ with with string argument test """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.Rectangle("hello", 3)

    def test_wid_float(self):
        """ width arg with float test """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.Rectangle(3.5, 7)

    def test_wid_list(self):
        """ width with list argument """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.Rectangle([4, 7, 8], 3)

    def test_wid_dict(self):
        """ width with dictionary argument test """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.Rectangle({"a": 4, "c": 5}, 5)

    def test_wid_tuple(self):
        """ width with tuple argument test """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.Rectangle((4, 5, 6), 5)

    def test_heig_none(self):
        """ height with None argument """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.Rectangle(4, None)

    def test_heig_str(self):
        """ height with string argument test """
        with self.assertRaisesRegex(TypeError, "height must be an Integer"):
            rec.Rectangle(4, "hello")

    def test_heig_float(self):
        """ height with float argument test """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.Rectangle(5, 7.8)

    def test_heig_list(self):
        """ height with list argument test """
        with self.assertRaisesRegex(TypeError, "height must be  an integer"):
            rec.Rectangle(5, [4, 5, 6])

    def test_heig_dict(self):
        """ height with dictionary test """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.Rectangle(5, {"a": 3, "c": 4})

    def test_heig_tuple(self):
        """ height with tuple argument test """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.Rectangle(5, (4, 5, 6))

    def test_x_none(self):
        """ x argument with none test """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.Rectangle(4, 5, None)

    def test_x_str(self):
        """ x argument with string test """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.Rectangle(4, 5, "hello", 7)

    def test_x_float(self):
        """ x argument with float test """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.Rectangle(4, 5, 6.7, 8)

    def test_x_list(self):
        """ x argument with list testing """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.Rectangle(4, 5, [6, 7, 8], 9)

    def test_x_dict(self):
        """ x argument with dictionary testing """
        with self.assertRaisesRegex9TypeError, "x must be an integer"):
            rec.Rectangle(5, 6, {"a": 7, "c": 8}, 9)

    def test_x_tuple(self):
        """ x argument with tuple testing """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.Rectangle(4, 5, (6, 7, 8), 3)

    def test_y_none(self):
        """ y argument with none testing """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.Rectangle(4, 5, 6, None)

    def test_y_str(self):
        """ y argument with string testing """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.Rectangle(4, 5, 6, "hello")
    
    def test_y_float(self):
        """ y argument with float testing """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.Rectangle(4, 5, 6, 7.6)

    def test_y_list(self):
        """ y argument with list testing """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.Rectangle(4, 5, 6, [7, 8, 9])

    def test_y_dict(self):
        """ y argument with dictionary testing """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.Rectangle(4, 5, 6, {"a": 7, "c": 9})

    def test_y_tuple(self):
        """ y argument with tuple testing """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.Rectangle(4, 5, 6, (7, 8, 9))

    def test_area(self):
        """ araa method testing """
        r1 = rec.Rectangle(4, 10, 0, 0, 0)
        self.assertEqual(40, r1.area())

    def test_display(self):
        """ display testing """
        r1 = rec.Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            r1.display(1)

    def test_update(self):
        """ update testing """
        r1 = rec.Rectangle(3, 4, 5, 6, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(78, "hello")

    def test_update_kwargs(self):
        """ kwargs update method testing """
        r1 = rec.Rectangle(2, 3, 4, 5, 6)
        r1.update(id=78, x=2, height=3)
        r1.update(y=5, height=23, width=3)
        self.assertEqual("[Rectangle] (78) 2/5 - 3/23", str(r1))

    def test_to_dictionary(self):
        """ dictionary method testing """
        r1 = rec.Rectangle(2, 3, 4, 5, 6)
        r2 = rec.Rectangle(5, 3, 7, 4, 1)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)


if __name__ == "__main__":
    unitest.main()
