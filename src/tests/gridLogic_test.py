import unittest
from gridLogic import MSGrid
from square import Square


class TestMSGrid(unittest.TestCase):
    def setUp(self):
        self.grid = MSGrid(10, 10, 10)

    def test_generateGrid(self):
        empty_grid = self.grid.generateGrid(3, 3)
        for i in empty_grid:
            for j in i:
                self.assertEqual(j.value, "0")
