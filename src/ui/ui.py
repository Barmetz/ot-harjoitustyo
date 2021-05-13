from tkinter import Tk, Menu
from logic.settings import Settings
from logic.statistics import Statistics
from ui.settings_ui import SettingsUI
from ui.game_ui import GameUI
from ui.game_over_ui import GameOverUI
from ui.statistics_ui import StatisticsUI
from config import SETTINGS_FILENAME, STATISTICS_FILENAME

class UI():
    """Creates all windows and menubar.
    Attributes:
        settings: Settings object.
        root: Main window.
        game: GameWindow
        game_over_window: GameOverWindow

    """

    def __init__(self):
        """Constructor. Sets up attributes.
        """
        self.settings_handler = Settings(SETTINGS_FILENAME)
        self.stats_handler = Statistics(STATISTICS_FILENAME)
        self.root = Tk()
        self.root.title("Minesweeper")
        self.game = GameUI(self.root, self.settings_handler)
        self.game_over_ui = GameOverUI(
            self.root, self.settings_handler, self.stats_handler)
        self.game.game_over_ui = self.game_over_ui
        self.game_over_ui.game = self.game
        self.menubar()
        self.main()

    def main(self):
        """Mainloop
        """
        self.root.mainloop()

    def menubar(self):
        """Creates menubar and its contents.
        """
        menubar = Menu(self.root)
        menu = Menu(menubar, tearoff=0)
        menu.add_command(label="New Game",
                         command=lambda x=False: self.game.reset(x))
        menu.add_command(label="Settings", command=self.settings_ui)
        menu.add_command(label="Statistics", command=self.statistics_ui)
        menu.add_separator()
        menu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="Menu", menu=menu)
        self.root.config(menu=menubar)

    def settings_ui(self):
        """Opens the settings popup.
        """
        SettingsUI(self.root, self.settings_handler, self.game)

    def statistics_ui(self):
        """Opens the statistics popup.
        """
        StatisticsUI(self.root, self.settings_handler, self.stats_handler)
        