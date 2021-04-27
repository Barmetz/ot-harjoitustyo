from pathlib import Path
from config import FILE_PATH


class Settings:
    def __init__(self):
        self.filename = 'settings.csv'
        self.filepath = None

    def get_filepath(self):
        self.filepath = FILE_PATH

    def load(self):
        self.get_filepath()
        if Path(self.filepath).is_file():
            return self.read()
        else:
            self.create()
            return self.read()

    def create(self):
        Path(self.filepath).touch()
        self.write("10;10;10;50")

    def write(self, row):
        with open(self.filepath, 'w') as file:
            file.write(row)

    def read(self):
        with open(self.filepath) as file:
            row = next(file)
            return row.split(';')
