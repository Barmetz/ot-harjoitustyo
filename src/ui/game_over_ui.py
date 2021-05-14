from tkinter import Toplevel, Label, Button, NSEW, W


class GameOverUI():
    """Class for the game over popup window.
    Attributes:
        game: main GameUI object.
        root: Main window.
        settings_handler: Settings class for reading the settings file.
        stats_handler = Statistics class for updating statistics.
        data = Statistics to be displayed on screen.
        pop: Tkinter Toplevel object.
    """

    def __init__(self, root, settings_handler, stats_handler):
        """Constructor.
        Args:
            root: Main window.
            settings_handler: Settings class for reading the settings file.
            stats_handler = Statistics class for updating statistics.
        """
        self.game = None
        self.root = root
        self.settings_handler = settings_handler
        self.stats_handler = stats_handler

    def main(self, state, timer):
        """Calls functions to generate gameover popup.
        Args:
            state: Tells if game was won or lost.
            timer: Tells how long the game took.
        """
        self.update_settings()
        self.data = self.stats_handler.update_stats(
            ";".join(self.settings), state, timer)
        self.pop = Toplevel(self.root)
        self.create_general_text(state)
        self.create_stat_text(timer)
        self.create_buttons()
        self.grid_config()
        self.geometry()
        self.focus()

    def update_settings(self):
        """Gets current game settings.
        """
        self.settings = self.settings_handler.load().split(";")
        self.playheight = int(self.settings[0])
        self.playwidth = int(self.settings[1])
        self.boxsize = int(self.settings[3])

    def create_general_text(self, state):
        """Creates gameover message.
        Args:
            state: Tells if game was won or lost.
        """
        if state:
            text = "Game Over. You lost!"
        else:
            text = "Game Over. You win!"
        self.pop.title(text.split(".")[1])
        label = Label(self.pop, text=text)
        label.grid(row=0, column=0, columnspan=2, sticky=NSEW)

    def create_stat_text(self, timer):
        """Creates labels displaying statistics.
        Args:
            timer: Tells how long the game took.
        """
        label = Label(
            self.pop, text=f"Games: {int(self.data[1]) + int(self.data[2])}")
        label.grid(row=1, column=0, sticky=W)
        label = Label(self.pop, text=f"Wins: {self.data[1]}")
        label.grid(row=2, column=0, sticky=W)
        label = Label(self.pop, text=f"Loses: {self.data[2]}")
        label.grid(row=3, column=0, sticky=W)
        label = Label(
            self.pop,
            text=f"Percentage:{self.stats_handler.percentage(int(self.data[1]),int(self.data[2]))}")
        label.grid(row=4, column=0, sticky=W)
        label = Label(self.pop, text=f"Your Time: {timer}")
        label.grid(row=1, column=1, sticky=W)
        label = Label(self.pop, text=f"Best Time: {self.check_best_time()}")
        label.grid(row=2, column=1, sticky=W)
        label = Label(self.pop, text=f"Streak: {self.data[4]}")
        label.grid(row=3, column=1, sticky=W)

    def check_best_time(self):
        """Checks if a highscore time exists.
        """
        if self.data[3] == "-1":
            return "Losing is fun"
        else:
            return self.data[3]

    def create_buttons(self):
        """Generates buttons.
        """
        button = Button(self.pop, text="New Game",
                        command=lambda: self.reset_pop())
        button.grid(row=5, column=0)
        button = Button(self.pop, text="Exit", command=self.root.destroy)
        button.grid(row=5, column=1)
        self.pop.protocol("WM_DELETE_WINDOW", lambda: self.root.destroy())

    def grid_config(self):
        """Configures tkinter grid weights.
        """
        for i in range(2):
            self.pop.grid_columnconfigure(i, weight=1)
        for j in range(6):
            self.pop.grid_rowconfigure(j, weight=1)

    def geometry(self):
        """Sets the popup window size and positions it in the center of the main window.
        """
        geometry_x = self.root.winfo_x()+(self.boxsize//2)*self.playwidth-125
        geometry_y = self.root.winfo_y()+(self.playheight + 1) * \
            (self.boxsize//2)-75
        self.pop.geometry(f"280x150+{geometry_x}+{geometry_y}")
        self.pop.resizable(False, False)

    def focus(self):
        """Grabs focus to the popup window and prevents interactions with the GameUI.
        """
        self.pop.focus_set()
        self.pop.wait_visibility()
        self.pop.grab_set()

    def reset_pop(self):
        """Restarts a new game and closes the popup.
        """
        self.pop.destroy()
        self.game.reset(False)
