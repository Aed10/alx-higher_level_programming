import unittest


from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    def test_init(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10, 1, 1)
        r3 = Rectangle(10, 2, 0, 0, 33)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r3.id, 33)

    def test_type_validation(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "str")

        with self.assertRaises(TypeError):
            r1 = Rectangle("10", "str")

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10.4)

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, "str", 9)

        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -2)

    def test_geters_setters(self):
        r = Rectangle(10, 11)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.height, 11)
        self.assertEqual(r.width, 10)

        r.height = 15
        self.assertEqual(r.height, 15)
        r.width = 13
        self.assertEqual(r.width, 13)

        r.x = 15
        self.assertEqual(r.x, 15)
        r.y = 13
        self.assertEqual(r.y, 13)

        with self.assertRaises(TypeError):
            r.width = "str"

        with self.assertRaises(TypeError):
            r.height = "str"

        with self.assertRaises(ValueError):
            r.width = -12

        with self.assertRaises(ValueError):
            r.height = -12

        with self.assertRaises(TypeError):
            r.x = "str"

        with self.assertRaises(TypeError):
            r.y = "str"

        with self.assertRaises(ValueError):
            r.x = -12

        with self.assertRaises(ValueError):
            r.y = -12

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r1 = Rectangle(10, 10)
        self.assertEqual(r1.area(), 100)

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1.update(1)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(
            r1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        )

        r1.update(8)
        r1_dictionary = r1.to_dictionary()
        self.assertNotEqual(
            r1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        )
