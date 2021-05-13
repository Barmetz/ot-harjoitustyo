from tkinter import Toplevel, Label, W, OptionMenu, StringVar, NSEW, Button, messagebox
from tkinter.constants import NSEW

class StatisticsUI:
    def __init__(self, root, settings_handler, stats_handler):
        self.root = root
        self.settings_handler = settings_handler
        self.stats_handler = stats_handler
        self.all_data = self.stats_handler.load()
        self.option = StringVar()
        self.labels = []
        self.stats_ui_main()

    def stats_ui_main(self):
        self.pop = Toplevel(self.root)
        self.pop.title("Statistics")
        self.update_settings()
        self.stats_ui_optionmenu()
        self.stats_ui_text()
        self.stats_ui_buttons()
        self.grid_config()
        self.stats_ui_geometry()
        self.stats_ui_focus()

    def update_settings(self):
        """Gets current game settings.
        """
        self.settings = self.settings_handler.load()
        self.playheight = int(self.settings[0])
        self.playwidth = int(self.settings[1])
        self.boxsize = int(self.settings[3])
    
    def stats_ui_optionmenu(self):
        self.options = ["10x10 grid, 10 mines",
                 "16x16 grid, 40 mines", "16x30 grid, 99 mines", "Custom"]
        self.option.set(self.options[0])
        menu = OptionMenu(self.pop, self.option, *self.options, command=self.update_option)
        menu.grid(row=0, column=0, columnspan=2, sticky=NSEW)

    def update_option(self, value):
        self.stats_ui_text_update()

    def option_index(self):
        return int(self.options.index(self.option.get()))

    def stats_ui_text(self):
        for i in range(6):
            self.labels.append(Label(self.pop))
        self.labels[0].grid(row=1, column=0, sticky=W)
        self.labels[1].grid(row=2, column=0, sticky=W)
        self.labels[2].grid(row=3, column=0, sticky=W)
        self.labels[3].grid(row=1, column=1, sticky=W)
        self.labels[4].grid(row=2, column=1, sticky=W)
        self.labels[5].grid(row=3, column=1, sticky=W)
        self.stats_ui_text_update()

    def stats_ui_text_update(self):
        self.data = self.all_data[self.option_index()].split(";")
        self.labels[0].config(text=f"Games: {int(self.data[1]) + int(self.data[2])}")
        self.labels[1].config(text=f"Wins: {self.data[1]}")
        self.labels[2].config(text=f"Loses: {self.data[2]}")
        self.labels[3].config(text=f"Percentage: {self.stats_handler.percentage(int(self.data[1]),int(self.data[2]))}")
        self.labels[4].config(text=f"Best Time: {self.check_best_time()}")
        self.labels[5].config(text=f"Streak: {self.data[4]}")
    
    def check_best_time(self):
        if self.data[3] == "-1":
            return "Losing is fun"
        else:
            return self.data[3]
    
    def stats_ui_buttons(self):
        button = Button(self.pop, text="Reset selected", command=self.reset_selected_stat)
        button.grid(row=4, column=0)
        button = Button(self.pop, text="Reset ALL", command=self.reset_all_stats)
        button.grid(row=4, column=1)
        

    def reset_selected_stat(self):
        ask = messagebox.askyesno('Reset', "Reset selected statistic?")
        if ask:
            index = self.option_index()
            self.all_data[index] = f"{index};0;0;-1;0;True"
            self.stats_handler.write(self.all_data)
            self.all_data = self.stats_handler.load()
            self.stats_ui_text_update()


    def reset_all_stats(self):
        ask = messagebox.askyesno('Reset', "Reset ALL statistics?")
        if ask:
            self.stats_handler.create()
            self.all_data = self.stats_handler.load()
            self.stats_ui_text_update()

    def grid_config(self):
        for i in range(2):
            self.pop.grid_columnconfigure(i, weight=1)
        for j in range(5):
            self.pop.grid_rowconfigure(j, weight=1)

    def stats_ui_geometry(self):
        """Sets the popup window size and positions it in the center of the GameWindow.
        """
        geometry_x = self.root.winfo_x()+(self.boxsize//2)*self.playwidth-125
        geometry_y = self.root.winfo_y()+(self.playheight + 1) * \
            (self.boxsize//2)-75
        self.pop.geometry(f"280x150+{geometry_x}+{geometry_y}")
        self.pop.resizable(False, False)

    def stats_ui_focus(self):
        """Grabs focus to the popup window and prevent interactions with the GameWindow.
        """
        self.pop.focus_set()
        self.pop.wait_visibility()
        self.pop.grab_set()
    