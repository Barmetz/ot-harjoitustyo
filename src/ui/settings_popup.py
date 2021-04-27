from tkinter import Button, StringVar, Toplevel, Radiobutton


class SettingsPopUp():
    def __init__(self, root, file_handler, game):
        self.root = root
        self.file_handler = file_handler
        self.game = game
        self.settings = self.file_handler.load()
        self.playheight = int(self.settings[0])
        self.playwidth = int(self.settings[1])
        self.boxsize = int(self.settings[3])
        self.options = ["10;10;10;50", "16;16;40;50", "16;30;99;50"]
        self.widgets = []
        self.setting = StringVar()
        self.pop = Toplevel(self.root)
        self.popup()

    def geometry(self):
        return f"250x150+{800+(self.boxsize//2)*self.playwidth-125}+{300+(self.playheight + 1)*(self.boxsize//2)-75}"

    def popup(self):
        self.pop.focus_set()
        self.pop.grab_set()
        self.pop.title("Settings")
        self.buttons()
        self.pop.geometry(self.geometry())
        self.pop.resizable(False, False)

    def buttons(self):
        button1 = Radiobutton(self.pop, text="10x10 grid\n 10 mines",
                              variable=self.setting, value=self.options[0])
        button1.grid(row=0, column=0)
        self.widgets.append(button1)
        button2 = Radiobutton(self.pop, text="16x16 grid\n 40 mines",
                              variable=self.setting, value=self.options[1])
        button2.grid(row=1, column=0)
        self.widgets.append(button2)
        button2.deselect()
        button3 = Radiobutton(self.pop, text="16x30 grid\n 99 mines",
                              variable=self.setting, value=self.options[2])
        button3.grid(row=2, column=0)
        self.widgets.append(button3)
        self.set_states()
        button4 = Button(self.pop, text="OK", command=self.change_setting)
        button4.grid(row=3, column=0)
        button5 = Button(self.pop, text="Cancel", command=self.pop.destroy)
        button5.grid(row=3, column=1)

    def set_states(self):
        current = ";".join(self.file_handler.load())
        for i in range(len(self.options)):
            if self.options[i] == current:
                self.widgets[i].select()
            else:
                self.widgets[i].deselect()

    def change_setting(self):
        self.file_handler.write(self.setting.get())
        self.pop.destroy()
        self.game.reset(True)
