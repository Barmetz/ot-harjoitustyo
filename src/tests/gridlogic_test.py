import unittest
from logic.gridlogic import MSGrid
from random import seed


class TestMSGrid(unittest.TestCase):
    def setUp(self):
        self.grid = MSGrid(3, 3, 1)

    def test_generateGrid(self):
        for j in range(len(self.grid.grid.keys())):
            for i in self.grid.grid[j].values():
                self.assertEqual(i.value, "0")

    def test_str(self):
        self.assertEqual(
            str(self.grid), "[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]")

    def test_place_numbers(self):
        self.grid.grid[1][1].value = "M"
        self.grid.grid[2][2].value = "M"
        self.grid.place_numbers()
        self.assertEqual(
            str(self.grid), "[['1', '1', '1'], ['1', 'M', '2'], ['1', '2', 'M']]")

    def test_place_mines(self):
        seed(1)
        self.grid.place_mines(0, 0)
        self.assertEqual(
            str(self.grid), "[['0', '0', 'M'], ['0', '0', '0'], ['0', '0', '0']]")

    def test_place(self):
        seed(9)
        self.grid.place(0, 0)
        self.assertEqual(
            str(self.grid), "[['0', '1', '1'], ['0', '1', 'M'], ['0', '1', '1']]")

    def test_zeropath(self):
        self.grid.grid[0][0].value = "1"
        self.grid.grid[0][0].hidden = False
        self.assertEqual(self.grid.zeropath(1, 1, [[1, 1]]), ([[1, 1], [0, 1], [
                         0, 0], [0, 2], [1, 2], [2, 2], [2, 1], [1, 0], [2, 0]], 7))

    def test_marked_count(self):
        self.grid.grid[1][1].value = "2"
        self.assertEqual(self.grid.adjacent(1, 1), [])

    def test_adjacent(self):
        self.grid.grid[1][1].value = "2"
        self.grid.grid[0][0].marked = True
        self.grid.grid[2][2].marked = True
        self.assertEqual(self.grid.adjacent(1, 1), [
                         [0, 1], [0, 2], [1, 0], [1, 2], [2, 1], [2, 0]])
