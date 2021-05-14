from pathlib import Path
from config import FILE_PATH


class Settings:
    """Class for writing and reading a file that contains settings for the game.
    Attributes:
        filename: Name of the file
        filepath: Path of the file
    """

    def __init__(self, filename):
        """Constructor. Sets up default values.
        """
        self.__filename = filename
        self.__filepath = None

    def __get_filepath(self):
        """Initializes filepath.
        """
        self.__filepath = FILE_PATH + self.__filename

    def load(self):
        """Checks if file exists.
        """
        self.__get_filepath()
        if not Path(self.__filepath).is_file():
            self.__create()
        return self.__read()

    def __create(self):
        """Creates a new file with default values.
        """
        Path(self.__filepath).touch()
        self.write("10;10;10;50")

    def write(self, row):
        """Writes a row to file.
        Args:
            row: The row containing setting information.
        """
        with open(self.__filepath, 'w') as file:
            file.write(row)

    def __read(self):
        """Reads a row from file.
        Returns:
            row: String containing game settings.
        """
        with open(self.__filepath) as file:
            row = next(file)
            return row
