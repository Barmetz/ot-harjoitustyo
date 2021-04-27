from tkinter import Tk, Menu
from logic.settings import Settings
from ui.settings_popup import SettingsPopUp
from ui.game_window import GameWindow


class UI():
    def __init__(self):
        self.file_handler = Settings()
        self.root = Tk()
        self.root.title("Minesweeper")
        self.game = GameWindow(self.root, self.file_handler)
        self.menubar()
        self.main()

    def main(self):
        self.root.mainloop()

    def settings_pop_up(self):
        SettingsPopUp(self.root, self.file_handler, self.game)

    def menubar(self):
        menubar = Menu(self.root)
        menu = Menu(menubar, tearoff=0)
        menu.add_command(label="New Game",
                         command=lambda x=False: self.game.reset(x))
        menu.add_command(label="Settings", command=self.settings_pop_up)
        menu.add_separator()
        menu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="Menu", menu=menu)
        self.root.config(menu=menubar)


if __name__ == "__main__":
    UI().main()
