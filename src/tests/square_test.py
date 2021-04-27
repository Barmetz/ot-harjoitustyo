import unittest
from logic.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square()

    def test_str(self):
        self.assertEqual(str(self.square), "0")
