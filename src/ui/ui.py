from tkinter import Tk, Menu
from logic.settings import Settings
from logic.statistics import Statistics
from ui.settings_popup import SettingsPopUp
from ui.game_window import GameWindow
from ui.game_over_popup import GameOverWindow


class UI():
    """Creates all windows and menubar.
    Attributes:
        file_handler: Settings object.
        root: Main window.
        game: GameWindow
        game_over_window: GameOverWindow

    """

    def __init__(self):
        """Constructor. Sets up attributes.
        """
        self.file_handler = Settings()
        self.stats = Statistics()
        self.root = Tk()
        self.root.title("Minesweeper")
        self.game = GameWindow(self.root, self.file_handler)
        self.game_over_window = GameOverWindow(self.root, self.file_handler, self.stats)
        self.game.game_over_window = self.game_over_window
        self.game_over_window.game = self.game
        self.menubar()
        self.main()

    def main(self):
        """Mainloop
        """
        self.root.mainloop()

    def settings_pop_up(self):
        """Opens the settings popup.
        """
        SettingsPopUp(self.root, self.file_handler, self.game)

    def menubar(self):
        """Creates menubar and its contents.
        """
        menubar = Menu(self.root)
        menu = Menu(menubar, tearoff=0)
        menu.add_command(label="New Game",
                         command=lambda x=False: self.game.reset(x))
        menu.add_command(label="Settings", command=self.settings_pop_up)
        menu.add_separator()
        menu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="Menu", menu=menu)
        self.root.config(menu=menubar)
