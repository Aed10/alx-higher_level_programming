import unittest


from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_init(self):
        a = Base()
        b = Base(4)
        c = Base()
        self.assertEqual(a.id, c.id - 1)
        self.assertEqual(c.id, a.id + 1)
        self.assertEqual(b.id, 4)

    def test_to_json(self):
        a = Square(5)
        a_dict = a.to_dictionary()
        b = Square(10)
        b_dict = b.to_dictionary()
        c = Square(15)
        c_dict = c.to_dictionary()
        json_s = Base.to_json_string([a_dict, b_dict, c_dict])
        my_list = ['"size": 5', '"size": 15', '"x": 0']
        for i in my_list:
            self.assertIn(i, json_s)

        d = Rectangle(3, 2, id=400)
        d_dict = d.to_dictionary()
        json_s = Base.to_json_string([a_dict, b_dict, d_dict, c_dict])
        self.assertIn('"width"', json_s)

        json_s = Base.to_json_string(None)
        self.assertEqual(json_s, "[]")
