#!/usr/bin/python3

""" Test unittest for class Rectangle """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangleInst(unittest.TestCase):
    """ Test instance of Rectangle Class """
    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(4, 8), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_two_args(self):
        r = Rectangle(2, 4)
        r2 = Rectangle(4, 2)
        self.assertEqual(r.id, r2.id - 1)

    def test_three_args(self):
        r = Rectangle(2, 4, 3)
        r2 = Rectangle(4, 2, 2)
        self.assertEqual(r.id, r2.id - 1)

    def test_four_args(self):
        r = Rectangle(2, 4, 3, 4)
        r2 = Rectangle(4, 2, 7, 8)
        self.assertEqual(r.id, r2.id - 1)

    def test_all_args(self):
        r = Rectangle(1, 2, 1, 2, 10)
        self.assertEqual(r.id, 10)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_private_width(self):
        r = Rectangle(1, 2, 1, 2, 10)
        with self.assertRaises(AttributeError):
            print(r.__width)

    def test_private_height(self):
        r = Rectangle(1, 2, 1, 2, 10)
        with self.assertRaises(AttributeError):
            print(r.__height)

    def test_private_x(self):
        r = Rectangle(1, 2, 1, 2, 10)
        with self.assertRaises(AttributeError):
            print(r.__x)

    def test_private_y(self):
        r = Rectangle(1, 2, 1, 2, 10)
        with self.assertRaises(AttributeError):
            print(r.__y)

    def test_width_getter(self):
        r = Rectangle(1, 2, 3, 4, 10)
        self.assertEqual(r.width, 1)

    def test_width_setter(self):
        r = Rectangle(1, 2, 3, 4, 10)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_height_getter(self):
        r = Rectangle(1, 2, 3, 4, 10)
        self.assertEqual(r.height, 2)

    def test_height_setter(self):
        r = Rectangle(1, 2, 3, 4, 10)
        r.height = 5
        self.assertEqual(r.height, 5)

    def test_x_getter(self):
        r = Rectangle(1, 2, 3, 4, 10)
        self.assertEqual(r.x, 3)

    def test_x_setter(self):
        r = Rectangle(1, 2, 3, 4, 10)
        r.x = 5
        self.assertEqual(r.x, 5)

    def test_y_getter(self):
        r = Rectangle(1, 2, 3, 4, 10)
        self.assertEqual(r.y, 4)

    def test_y_setter(self):
        r = Rectangle(1, 2, 3, 4, 10)
        r.y = 5
        self.assertEqual(r.y, 5)

class TestValidationAttributeWidth(unittest.TestCase):
    """ Test the validation of parameter of a Rectangle """
    
    def test_no_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)
    
    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hello", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(3.14, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_neg_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 7)
 
class TestValidationAttributeHeight(unittest.TestCase):
    """ Test the validation of parameter of a Rectangle """
    
    def test_no_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)
    
    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "Hello")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 3.14)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "Hello")

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [1, 2, 3])

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (1, 2, 3))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {1, 2, 3})

    def test_neg_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(7, -7)

class TestValidationAttributeX(unittest.TestCase):
    """ Test the validation of parameter of a Rectangle """
    
    def test_no_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, None)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, 3.14)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3,"Hello")

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, [1, 2, 3])

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, (1, 2, 3))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, {1, 2, 3})

    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(7, 3, -7)

class TestValidationAttributeY(unittest.TestCase):
    """ Test the validation of parameter of a Rectangle """
    
    def test_no_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, None)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, 3.14)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, "Hello")

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, [1, 2, 3])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, (1, 2, 3))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, {1, 2, 3})

    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(7, 3, 4, -7)

if __name__ == "__main__":
    unittest.main