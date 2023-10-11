import unittest
from sem11 import Rectangle


class TestRect(unittest.TestCase):
    def setUp(self):
        self.first_rec = Rectangle(2, 5)
        self.second_rec = Rectangle(4, 11)

    def test_peri(self):
        self.assertEqual(self.first_rec.length(), (2 + 5) * 2)
        self.assertEqual(self.second_rec.length(), (4 + 11) * 2)

    def test_area(self):
        self.assertEqual(self.first_rec.area(), 2 * 5)
        self.assertEqual(self.second_rec.area(), 4 * 11)

    def test_add(self):
        self.assertEqual(self.first_rec + self.second_rec, Rectangle(6, 16))


if __name__ == '__main__':
    unittest.main(verbosity=1)
