import unittest


from models.square import Square


class SquareTest(unittest.TestCase):
    def test_init(self):
        r1 = Square(10)
        r2 = Square(2, 1, 1)
        r3 = Square(10, 0, 0, 33)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r3.id, 33)

    def test_type_validation(self):
        with self.assertRaises(TypeError):
            r1 = Square("str")

        with self.assertRaises(TypeError):
            r1 = Square(10.4)

        with self.assertRaises(TypeError):
            r1 = Square(10, "str", 9)

        with self.assertRaises(ValueError):
            r1 = Square(-2)

    def test_geters_setters(self):
        r = Square(10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.size, 10)

        r.size = 15
        self.assertEqual(r.height, 15)
        self.assertEqual(r.height, 15)

        r.x = 15
        self.assertEqual(r.x, 15)
        r.y = 13
        self.assertEqual(r.y, 13)

        with self.assertRaises(TypeError):
            r.size = "str"

        with self.assertRaises(ValueError):
            r.size = -12

        with self.assertRaises(TypeError):
            r.x = "str"

        with self.assertRaises(TypeError):
            r.y = "str"

        with self.assertRaises(ValueError):
            r.x = -12

        with self.assertRaises(ValueError):
            r.y = -12

    def test_area(self):
        r1 = Square(3)
        self.assertEqual(r1.area(), 9)

    def test_update(self):
        r1 = Square(10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Square] (89) 10/10 - 10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Square] (89) 10/10 - 2")

        r1.update(89, 2, 4)
        self.assertEqual(str(r1), "[Square] (89) 4/10 - 2")

        r1.update(89, 2, 4, 5)
        self.assertEqual(str(r1), "[Square] (89) 4/5 - 2")

    def test_to_dictionary(self):
        r1 = Square(10, 2, 1)
        r1.update(1)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 2, 'y': 1, 'id': 1, 'size': 10})

        r1.update(8)
        r1_dictionary = r1.to_dictionary()
        self.assertNotEqual(
            r1_dictionary, {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        )
