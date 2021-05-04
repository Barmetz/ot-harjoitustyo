from tkinter import Toplevel, Label, Button, NSEW
class GameOverWindow():
    """Class for the game over popup window.
    Attributes:
        game: main GameWindow object.
        playheight: GameWindow height.
        playwidth: GameWindow width.
        boxsize: GameWindow size of the squares.
    """
    def __init__(self, root):
        """Sets up default values for the attributes.
        Args:
            root: Main window.
        """
        self.game = None
        self.pop = None
        self.playheight = 10
        self.playwidth = 10
        self.boxsize = 50
        self.root = root

    def game_over_popup(self, text):
        """Calls functions to generate game over popup.
        Args:
            text: Text to be displayed on the popup.
        """
        self.pop = Toplevel(self.root)
        self.game_over_popup_create_text(text)
        self.game_over_popup_create_buttons()
        self.game_over_popup_geometry()
        self.game_over_popup_focus()

    def game_over_popup_create_text(self, text):
        """Generates text on the popup window
        Args:
            text: Text to be displayed on the popup.
        """
        self.pop.title(text.split(".")[1])
        label = Label(self.pop, text=text)
        label.grid(row=0, column=0, columnspan=2, sticky=NSEW)

    def game_over_popup_create_buttons(self):
        """Generates buttons on the popup window
        """
        button = Button(self.pop, text="New Game",
                        command=lambda: self.reset_pop())
        button.grid(row=1, column=0)
        button = Button(self.pop, text="Exit", command=self.root.destroy)
        button.grid(row=1, column=1)
        for i in range(2):
            self.pop.grid_rowconfigure(i, weight=1)
            self.pop.grid_columnconfigure(i, weight=1)

    def reset_pop(self):
        """Restarts a new game and closes the popup.
        """
        self.pop.destroy()
        self.game.reset(False)

    def game_over_popup_geometry(self):
        """Sets the popup window size and positions it in the center of the GameWindow.
        """
        geometry_x = self.root.winfo_x()+(self.boxsize//2)*self.playwidth-125
        geometry_y = self.root.winfo_y()+(self.playheight + 1) * \
            (self.boxsize//2)-75
        self.pop.geometry(f"250x150+{geometry_x}+{geometry_y}")
        self.pop.resizable(False, False)

    def game_over_popup_focus(self):
        """Grabs focus to the popup window and prevent interactions with the GameWindow.
        """
        self.pop.focus_set()
        self.pop.wait_visibility()
        self.pop.grab_set()
