import unittest
from pathlib import Path
from config import FILE_PATH
from logic.statistics import Statistics


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.stats = Statistics('statistics_test.csv')

    def test_create_and_load(self):
        if Path(FILE_PATH+'settings_test.csv').is_file():
            Path(FILE_PATH+'settings_test.csv').unlink()
        result = self.stats.load()
        Path(FILE_PATH+'statistics_test.csv').unlink()
        self.assertEqual(result, [
                         '0;0;0;-1;0;True', '1;0;0;-1;0;True', '2;0;0;-1;0;True', '3;0;0;-1;0;True'])

    def test_write(self):
        self.stats.load()
        self.stats.write(['0;0;0;-1;0;True', 'abalabllba',
                         '2;0;0;-1;0;True', '3;0;0;-1;0;True'])
        result = self.stats.load()
        Path(FILE_PATH+'statistics_test.csv').unlink()
        self.assertEqual(
            result, ['0;0;0;-1;0;True', 'abalabllba', '2;0;0;-1;0;True', '3;0;0;-1;0;True'])

    def test_update_win(self):
        self.stats.load()
        self.stats.update_stats("10;10;10;50", False, -1)
        result = self.stats.load()
        Path(FILE_PATH+'statistics_test.csv').unlink()
        self.assertEqual(result, [
                         '0;1;0;-1;1;False', '1;0;0;-1;0;True', '2;0;0;-1;0;True', '3;0;0;-1;0;True'])

    def test_update_lose(self):
        self.stats.load()
        self.stats.update_stats("10;10;10;50", True, -1)
        result = self.stats.load()
        Path(FILE_PATH+'statistics_test.csv').unlink()
        self.assertEqual(result, [
                         '0;0;1;-1;-1;True', '1;0;0;-1;0;True', '2;0;0;-1;0;True', '3;0;0;-1;0;True'])

    def test_update_timer_win(self):
        self.stats.load()
        self.stats.update_stats("10;10;10;50", False, 10)
        result = self.stats.load()[0]
        Path(FILE_PATH+'statistics_test.csv').unlink()
        self.assertEqual(result, '0;1;0;10;1;False')

    def test_update_timer_lose(self):
        self.stats.load()
        self.stats.update_stats("10;10;10;50", True, 10)
        result = self.stats.load()[0]
        Path(FILE_PATH+'statistics_test.csv').unlink()
        self.assertEqual(result, '0;0;1;-1;-1;True')

    def test_update_timer_no_change(self):
        self.stats.load()
        self.stats.update_stats("10;10;10;50", False, 10)
        self.stats.update_stats("10;10;10;50", False, 20)
        result = self.stats.load()[0]
        Path(FILE_PATH+'statistics_test.csv').unlink()
        self.assertEqual(result, '0;2;0;10;2;False')

    def test_update_streak(self):
        self.stats.load()
        self.stats.update_stats("10;10;10;50", True, 10)
        self.stats.update_stats("10;10;10;50", True, 10)
        self.stats.update_stats("10;10;10;50", True, 10)
        result = self.stats.load()[0]
        Path(FILE_PATH+'statistics_test.csv').unlink()
        self.assertEqual(result, '0;0;3;-1;-3;True')

    def test_update_streak_change_lose(self):
        self.stats.load()
        self.stats.update_stats("10;10;10;50", False, 10)
        self.stats.update_stats("10;10;10;50", True, 10)
        self.stats.update_stats("10;10;10;50", True, 10)
        result = self.stats.load()[0]
        Path(FILE_PATH+'statistics_test.csv').unlink()
        self.assertEqual(result, '0;1;2;10;-2;True')

    def test_update_streak_change_win(self):
        self.stats.load()
        self.stats.update_stats("10;10;10;50", True, 10)
        self.stats.update_stats("10;10;10;50", False, 10)
        self.stats.update_stats("10;10;10;50", False, 10)
        result = self.stats.load()[0]
        Path(FILE_PATH+'statistics_test.csv').unlink()
        self.assertEqual(result, '0;2;1;10;2;False')

    def test_update_custom(self):
        self.stats.load()
        self.stats.update_stats("asdsad", True, 10)
        result = self.stats.load()[3]
        Path(FILE_PATH+'statistics_test.csv').unlink()
        self.assertEqual(result, '3;0;1;-1;-1;True')

    def test_percentage(self):
        result = self.stats.percentage(10, 30)
        self.assertEqual(result, "25.00 %")

    def test_percentage_fail(self):
        result = self.stats.percentage(0, 0)
        self.assertEqual(result, "*joke*")
