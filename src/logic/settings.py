from pathlib import Path
from config import FILE_PATH


class Settings:
    """Class for writing and reading a file that contains settings for the game.
    Attributes:
        filename: Name of the file
        filepath: Path of the file
    """

    def __init__(self):
        """Constructor. Sets up default values.
        """
        self.filename = 'settings.csv'
        self.filepath = None

    def get_filepath(self):
        """Initializes filepath.
        """
        self.filepath = FILE_PATH + self.filename

    def load(self):
        """Checks if file exists.
        """
        self.get_filepath()
        if not Path(self.filepath).is_file():
            self.create()
        return self.read()

    def create(self):
        """Creates a new file with default values.
        """
        Path(self.filepath).touch()
        self.write("10;10;10;50")

    def write(self, row):
        """Writes a row to file.
        Args:
            row: The row containing setting information.
        """
        with open(self.filepath, 'w') as file:
            file.write(row)

    def read(self):
        """Reads a row from file.
        Returns:
            row.split(';'): Array containing game settings.
        """
        with open(self.filepath) as file:
            row = next(file)
            return row.split(';')
