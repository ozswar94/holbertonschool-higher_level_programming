#!/usr/bin/python3
""" Unittest base """

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Test class Base """

    def test_id_int(self):
        """ Test id with int """
        b = Base(1)
        self.assertEqual(b.id, 1)
        b = Base(20)
        self.assertEqual(b.id, 20)
        b = Base(197)
        self.assertEqual(b.id, 197)

    def test_id_neg(self):
        """ Test id with negative int """
        b = Base(-2)
        self.assertEqual(b.id, -2)
        b = Base(-34)
        self.assertEqual(b.id, -34)
        b = Base(-197)
        self.assertEqual(b.id, -197)

    def test_id_str(self):
        """ Test id with string """
        b = Base("Hello")
        self.assertEqual(b.id, "Hello")

    def test_id_bool(self):
        """ Test id with bool """
        b = Base(True)
        self.assertEqual(b.id, True)

    def test_id_list(self):
        """ Test id with list """
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_id_dict(self):
        """ Test id with dict """
        b = Base({1, 2, 3})
        self.assertEqual(b.id, {1, 2, 3})

    def test_id_tuple(self):
        """ Test id with tuple """
        b = Base((1, 2, 3))
        self.assertEqual(b.id, (1, 2, 3))

    def test_id_none(self):
        """ Test id with no parameter """
        Base.__nb_objects = 0
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        b = Base()
        self.assertEqual(b.id, 3)
        b = Base()
        self.assertEqual(b.id, 4)

    def test_too_many_args(self):
        """ Test id with too many args """
        with self.assertRaises(TypeError):
            Base(1, 1)
        with self.assertRaises(TypeError):
            Base(1, None)


class Test_Base_to_json_string(unittest.TestCase):
    """ Test cases for to_json_string static method """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_json_string_type(self):
        r = Rectangle(2, 4, 1, 2, 42)
        s = Square(2, 1, 2, 42)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_basic_rectangle(self):
        r = Rectangle(2, 4, 1, 2, 42)
        dicts = [r.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dicts)) == 53)

    def test_to_json_string_basic_square(self):
        s = Square(2, 1, 2, 42)
        dicts = [s.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dicts)) == 39)

    def test_to_json_string_multiple_dicts(self):
        r = Rectangle(2, 4, 1, 2, 42)
        s = Square(2, 1, 2, 42)
        dicts = [r.to_dictionary(), s.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dicts)) == 92)

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string_None_list(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 42)


class Test_Base_save_to_file(unittest.TestCase):
    """Test cases for save_to_file static method."""

    def test_save_to_file_basic_rectangle(self):
        r = Rectangle(2, 4, 1, 2, 42)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", 'r') as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_basic_square(self):
        s = Square(2, 1, 2, 42)
        Square.save_to_file([s])
        with open("Square.json", 'r') as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_multiple_rectangles(self):
        r1 = Rectangle(2, 4, 1, 2, 42)
        r2 = Rectangle(4, 2, 2, 1, 24)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", 'r') as f:
            self.assertTrue(len(f.read()) == 106)

    def test_save_to_file_multiple_squares(self):
        s1 = Square(2, 1, 2, 42)
        s2 = Square(4, 2, 1, 24)
        Square.save_to_file([s1, s2])
        with open("Square.json", 'r') as f:
            self.assertTrue(len(f.read()) == 78)

    def test_save_to_file_overwrite(self):
        s = Square(2, 1, 2, 42)
        Square.save_to_file([s])
        s = Square(42, 42, 42, 42)
        Square.save_to_file([s])
        with open("Square.json", 'r') as f:
            self.assertTrue(len(f.read()) == 42)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 42)


class Test_Base_from_json_string(unittest.TestCase):
    """Test cases for from_json_string static method."""

    def test_from_json_string_type(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_basic_rectangle(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_basic_square(self):
        list_input = [{'id': 89, 'size': 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_multiple_rectangles(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 98, 'width': 1, 'height': 8}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_multiple_square(self):
        list_input = [
            {'id': 89, 'size': 4},
            {'id': 98, 'size': 8}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_multiple_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_multiple_empty(self):
        self.assertEqual([], Base.from_json_string('[]'))

    def test_from_json_string_multiple_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_multiple_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 42)


class Test_Base_create(unittest.TestCase):
    """Test cases for create static method."""

    def test_create_basic_rectangle(self):
        dct = {'width': 2, 'height': 4, 'x': 1, 'y': 2, 'id': 42}
        r = Rectangle.create(**dct)
        self.assertDictEqual(r.to_dictionary(), dct)

    def test_create_basic_square(self):
        dct = {'size': 2, 'x': 1, 'y': 2, 'id': 42}
        s = Square.create(**dct)
        self.assertDictEqual(s.to_dictionary(), dct)


class Test_Base_load_from_file(unittest.TestCase):
    """Test cases for load_from_file static method."""

    def tearDown(self):
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except:
            pass
        try:
            os.remove("Square.json")
        except:
            pass

    def test_load_from_file_rectangles(self):
        r1 = Rectangle(2, 4, 1, 2, 42)
        r2 = Rectangle(4, 2, 2, 1, 24)
        Rectangle.save_to_file([r1, r2])
        lst = Rectangle.load_from_file()
        self.assertDictEqual(lst[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(type(lst[0]), Rectangle)
        self.assertDictEqual(lst[1].to_dictionary(), r2.to_dictionary())
        self.assertEqual(type(lst[1]), Rectangle)

    def test_load_from_file_squares(self):
        s1 = Square(2, 1, 2, 42)
        s2 = Square(4, 2, 1, 24)
        Square.save_to_file([s1, s2])
        lst = Square.load_from_file()
        self.assertDictEqual(lst[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(type(lst[0]), Square)
        self.assertDictEqual(lst[1].to_dictionary(), s2.to_dictionary())
        self.assertEqual(type(lst[0]), Square)

    def test_load_from_file_no_file(self):
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])

    def test_load_from_file_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file(42)


if __name__ == "__main__":
    unittest.main