from pathlib import Path
from config import FILE_PATH


class Statistics:
    """Class for writing and reading a file that contains statistics.
    Attributes:
        filename: Name of the file.
        filepath: Path of the file.
        options: Default game settings.
        stats: Used to update statistics of designated game setting.
    """
    def __init__(self):
        """Constructor. Sets up default values.
        """
        self.filename = 'statistics.csv'
        self.filepath = None
        self.options = ["10;10;10;50", "16;16;40;50", "16;30;99;50"]
        self.stats = []
        self.load()

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
        data = []
        data.append("0;0;0;-1;0;True")
        data.append("1;0;0;-1;0;True")
        data.append("2;0;0;-1;0;True")
        data.append("3;0;0;-1;0;True")
        self.write(data)

    def write(self, data: list):
        """Writes data to file.
        Args:
            data: Data to be written.
        """
        with open(self.filepath, 'w') as file:
            for row in data:
                file.write(row+"\n")

    def read(self):
        """Reads the file.
        Returns:
            data: Array. Items are rows in file.
        """
        with open(self.filepath) as file:
            data = []
            for row in file:
                row = row.strip()
                data.append(row)
        return data

    def get_index(self, setting):
        """ Gets index to combine current game setting and its statistics.
        Args:
            setting: Current game setting.
        """
        if setting in self.options:
            return self.options.index(setting)
        return 3

    def update_stats(self, setting, state, timer):
        """Calls functions to update statistics of a designated setting.
        Args:
            setting: Current game setting.
            state: Tells if game was won or lost.
            timer: Time the game took to play.
        """
        index = self.get_index(setting)
        data = self.load()
        self.stats = data[index].split(";")
        self.win_lose(state)
        if not state:
            self.best_time(timer)
        self.streak(state)
        data[index] = ";".join(self.stats)
        self.write(data)
        return self.stats

    def win_lose(self, state):
        """Updates win-lose count.
        Args:
            state: Tells if game was won or lost.
        """
        if state:
            self.stats[2] = str(int(self.stats[2])+1)
        else:
            self.stats[1] = str(int(self.stats[1])+1)

    def best_time(self, timer):
        """Updates time highscore.
        Args:
            timer: Time the game took to play.
        """
        if timer < int(self.stats[3]) or self.stats[3] == "-1":
            self.stats[3] = str(timer)

    def streak(self, state):
        """Updates streak counter.
        Args:
            state: Tells if game was won or lost.
        """
        if str(state) == self.stats[5]:
            if state:
                self.stats[4] = str(int(self.stats[4]) - 1)
            else:
                self.stats[4] = str(int(self.stats[4]) + 1)
        else:
            self.stats[5] = str(state)
            if state:
                self.stats[4] = "-1"
            else:
                self.stats[4] = "1"

    def percentage(self, win, lose):
        """Calculates percentage of wins.
        Args:
            win: Amount of wins
            lose: Amoun of loses
        """
        try:
            value = (win / (win + lose)) * 100
            value = f"{value:.2f}" + " %"
            return value
        except ZeroDivisionError:
            return "*joke*"
