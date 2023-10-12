import unittest
from unittest.mock import patch
from sem14 import del_other_symbol


class Test(unittest.TestCase):
    def test_is_true(self):
        self.assertTrue(del_other_symbol('wew wefefe'), 'wew wefefe')

    def test_lower(self):
        self.assertTrue(del_other_symbol('wew wefeFE'), 'wew wefefe')

    def test_punkt(self):
        self.assertTrue(del_other_symbol('wew _wefefe,.:;'), 'wew wefefe')

    def test_kirill(self):
        self.assertTrue(del_other_symbol('wew _wыавываefefe,.:;'), 'wew wefefe')

    def test_komplex(self):
        self.assertTrue(del_other_symbol('Wew _wыавываefefe,.:;'), 'wew wefefe')


if __name__ == '__main__':
    unittest.main()
