from tkinter import Label, Button, Grid, NSEW, Toplevel
from PIL import Image, ImageTk
from logic.gridlogic import MSGrid


class GameWindow():
    def __init__(self, root, file_handler):
        self.root = root
        self.file_handler = file_handler
        self.game_settings()

        self.button_widgets = []
        self.text_widgets = []
        self.flag = 0
        self.clickcount = 0
        self.leave = False  # For tracking mouse location on button

        self.images_numbers = []  # Images for the numbers
        self.images_tile = []  # Images for hidden tiles, flags and mines
        self.create_images()

        self.grid_obj = MSGrid(self.playheight, self.playwidth, self.mines)
        self.ui_grid()
        self.playtext()
        self.ui_geometry()

    def game_settings(self):
        self.settings = self.file_handler.load()
        self.playheight = int(self.settings[0])
        self.playwidth = int(self.settings[1])
        self.mines = int(self.settings[2])
        self.boxsize = int(self.settings[3])

    # Creates arrays for tile graphics and resize images acording to boxsize
    def create_images(self):
        image_size = (self.boxsize, self.boxsize)
        half_image_size = (self.boxsize//2, self.boxsize//2)
        self.images_numbers.append(ImageTk.PhotoImage(
            Image.open("src/images/clicked.png").resize(image_size)))
        for i in range(1, 9):
            self.images_numbers.append(ImageTk.PhotoImage(Image.open(
                "src/images/number"+str(i)+".png").resize(half_image_size)))

        self.images_tile.append(ImageTk.PhotoImage(
            Image.open("src/images/tile.png").resize(image_size)))
        self.images_tile.append(ImageTk.PhotoImage(
            Image.open("src/images/mine.png").resize(half_image_size)))
        self.images_tile.append(ImageTk.PhotoImage(
            Image.open("src/images/flag.png").resize((image_size))))
        self.images_tile.append(ImageTk.PhotoImage(Image.open(
            "src/images/wrong_flag.png").resize((image_size))))

    # Generates a grid of tkinter buttons
    def ui_grid(self):
        for j in range(self.playheight):
            Grid.rowconfigure(self.root, j, weight=1)
            widgetrow = []
            for i in range(self.playwidth):
                Grid.columnconfigure(self.root, i, weight=1)
                button = Button(self.root, width=50, height=50,
                                image=self.images_tile[0])
                button.grid(row=j, column=i, sticky=NSEW)
                button.bind("<Button-1>", self.left_click_indicator(j, i))
                button.bind("<ButtonRelease-1>",
                            self.left_click_release_indicator(j, i))
                button.bind("<Leave>", self.left_click_leave_indicator(j, i))
                button.bind("<Button-3>", self.right_click_indicator(j, i))
                widgetrow.append(button)
            self.button_widgets.append(widgetrow)

    # Resizes the main windown according to the amount of squares
    def ui_geometry(self):
        self.root.geometry(
            f"{self.playwidth*self.boxsize}x{(self.playheight + 2)*self.boxsize}+800+300")
        self.root.resizable(False, False)

    # Generates general label widgets for the UI
    def playtext(self):
        botleft = Label(self.root, text="Clock: 0")
        botright = Label(self.root, text=f"Mines: {self.mines}")
        botleft.grid(row=self.playheight+1, column=0,
                     columnspan=self.playwidth//2)
        botright.grid(row=self.playheight+1,
                      column=(self.playwidth//2)-1, columnspan=self.playwidth//2)
        Grid.rowconfigure(self.root, 0, weight=1)
        Grid.rowconfigure(self.root, self.playheight+1, weight=1)
        self.text_widgets.append(botleft)
        self.text_widgets.append(botright)

    # Wrappers for buttons so that callback fuction doesn't break them
    def left_click_indicator(self, j, i):
        return lambda Button: self.left_click(j, i)

    def left_click_leave_indicator(self, j, i):
        return lambda Button: self.left_click_leave(j, i)

    def left_click_release_indicator(self, j, i):
        return lambda Button: self.left_click_release(j, i)

    def right_click_indicator(self, j, i):
        return lambda Button: self.right_click(j, i)

    # The functions for Buttons
    def left_click(self, j, i):
        if not self.grid_obj.grid[j][i].marked:
            self.button_widgets[j][i].config(image=self.images_numbers[0])
            self.leave = False

    def left_click_leave(self, j, i):
        if not self.grid_obj.grid[j][i].marked and self.grid_obj.grid[j][i].hidden:
            self.button_widgets[j][i].config(image=self.images_tile[0])
            self.leave = True

    def left_click_release(self, j, i):
        if not self.grid_obj.grid[j][i].marked and not self.leave:
            self.grid_obj.grid[j][i].hidden = False
            if self.grid_obj.grid[j][i].value == "0":
                self.update_zeropath(j, i)
            else:
                self.destroy_button(j, i)
                label = Label(
                    self.root, borderwidth=2, bg="white", relief="sunken", width=52, height=52)
                if self.grid_obj.grid[j][i].value == "M":
                    label.config(image=self.images_tile[1])
                    self.game_over(True)
                else:
                    label.config(image=self.images_numbers[int(
                        self.grid_obj.grid[j][i].value)])
                label.grid(row=j, column=i)
                self.button_widgets[j][i] = label
            self.clickcount += 1
            if self.clickcount == self.playwidth*self.playheight-self.mines:
                self.game_over(False)

    def destroy_button(self, j, i):
        button = self.button_widgets[j][i]
        self.button_widgets[j][i] = 0
        button.destroy()

    def right_click(self, j, i):
        if self.grid_obj.grid[j][i].marked:
            self.button_widgets[j][i].config(image=self.images_tile[0])
            self.grid_obj.grid[j][i].marked = False
            self.flag -= 1
        else:
            self.button_widgets[j][i].config(image=self.images_tile[2])
            self.grid_obj.grid[j][i].marked = True
            self.flag += 1
        self.text_widgets[1].config(text=f"Mines: {self.mines-self.flag}")

    # When clicking a 0 square automatically open the all connected 0 squares and their neighbours
    def update_zeropath(self, j, i):
        self.grid_obj.zeropath_clickcount = 0
        coordinates, clicks = self.grid_obj.zeropath(j, i, [[j, i]])
        self.clickcount += clicks
        for pos in coordinates:
            label = Label(
                self.root, borderwidth=2, bg="white", relief="sunken", width=52, height=52)
            label.config(image=self.images_numbers[int(
                self.grid_obj.grid[pos[0]][pos[1]].value)])
            label.grid(row=pos[0], column=pos[1])
            self.button_widgets[pos[0]][pos[1]] = label

    def reset(self, geobool):
        self.destroy_widgets()
        self.game_settings()
        self.grid_obj.update(self.playheight, self.playwidth, self.mines)
        self.ui_grid()
        self.playtext()
        if geobool:
            self.ui_geometry()
        self.clickcount = 0
        self.flag = 0

    # destroys button
    def destroy_widgets(self):
        for widget in self.text_widgets:
            widget.destroy()
        self.text_widgets = []
        for row in range(len(self.button_widgets)):
            for column in range(len(self.button_widgets[0])):
                button = self.button_widgets[row][column]
                self.button_widgets[row][column] = 0
                button.destroy()
        self.button_widgets = []

    def game_over(self, state):
        if state:
            self.game_over_popup("Game Over. You lost!")
        else:
            self.text_widgets[1].config(text=f"Mines: 0")
            self.game_over_popup("Game Over. You win!")

    def game_over_popup(self, text):
        pop = Toplevel(self.root)
        pop.focus_set()
        pop.grab_set()
        pop.title(text.split(".")[1])
        label = Label(pop, text=text)
        label.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        button = Button(pop, text="New Game",
                        command=lambda: self.reset_pop(pop))
        button.grid(row=1, column=0)
        button = Button(pop, text="Exit", command=self.root.destroy)
        button.grid(row=1, column=1)
        for i in range(2):
            pop.grid_rowconfigure(i, weight=1)
            pop.grid_columnconfigure(i, weight=1)
        pop.geometry(
            f"250x150+{800+(self.boxsize//2)*self.playwidth-125}+{300+(self.playheight + 1)*(self.boxsize//2)-75}")
        pop.resizable(False, False)

    # Start a new game
    def reset_pop(self, pop):
        pop.destroy()
        self.reset(False)
