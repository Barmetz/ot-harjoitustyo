import unittest
from pathlib import Path
from config import FILE_PATH
from logic.settings import Settings

class TestSettings(unittest.TestCase):
    def setUp(self):
        self.file_handler = Settings('settings_test.csv')

    def test_create_and_load(self):
        if Path(FILE_PATH+'settings_test.csv').is_file():
            Path(FILE_PATH+'settings_test.csv').unlink()
        result = self.file_handler.load()
        self.assertEqual(result, ['10', '10', '10', '50'])
        Path(FILE_PATH+'settings_test.csv').unlink()

    def test_write(self):
        self.file_handler.load()
        self.file_handler.write("16;16;40;50")
        result = self.file_handler.load()
        self.assertEqual(result, ['16', '16', '40', '50'])
        Path(FILE_PATH+'settings_test.csv').unlink()
