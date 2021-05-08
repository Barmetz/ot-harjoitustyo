from tkinter import Label, Button, Grid, NSEW, Frame
from PIL import Image, ImageTk
from logic.gridlogic import MSGrid

from time import perf_counter

class GameWindow():
    """Class for the main game window. Game consists of two grids.
    The MSGrid class with the game logic and a grid of tkinter Labels and Buttons.
    Attributes:
        rootwindown: Main windown.
        root: Frame in the main window. The game is drawn here.
        file_handler: Settings class for reading the settings file.
        square_widgets: Grid of Buttons and Labels that depict the game squares
        text_widgets: Texts surrounding the game grid.
        flag_location: Locations of all marked/flagged squares.
        clickcount: Amount of clicked squares.
        timer_count = Counts seconds.
        timer = Tells if timer is on or off.
        leave: Boolean to see if mouse is moved out of a button after clicking.
        images_numbers: Image objects for different number values.
        images_tile: Image objects for mines and tile designs.
        grid_obj: MSGrid class that is the game logic.
        game_over_window = GameOverWindow class for game over popup.

        playheight: Grid height.
        playwidth: Grid width.
        mines: Amount of mines in grid.
        boxsize: Size if drawn squares.

    """

    def __init__(self, root, file_handler):
        """Constructor. Sets up all attributes and the ui.
        Args:
            root: The main window.
            file_handler: Settings class for file operations.
        """
        self.rootwindown = root
        self.window()
        self.file_handler = file_handler
        self.game_settings()
        self.square_widgets = {}
        self.text_widgets = []
        self.flag_location = []
        self.clickcount = 0
        self.timer_count = 0
        self.timer = False
        self.leave = False
        self.images_numbers = []
        self.images_tile = []
        self.create_images()
        self.grid_obj = MSGrid(self.playheight, self.playwidth, self.mines)
        self.ui_grid()
        self.playtext()
        self.ui_geometry()
        self.game_over_window = None

    def window(self):
        self.root = Frame(self.rootwindown)
        self.root.pack()

    def game_settings(self):
        """Loads game settings from file and assings them to attributes.
        """
        self.settings = self.file_handler.load()
        self.playheight = int(self.settings[0])
        self.playwidth = int(self.settings[1])
        self.mines = int(self.settings[2])
        self.boxsize = int(self.settings[3])

    def create_images(self):
        """Creates arrays of tile graphics and resize images according to boxsize.
        """
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

    def ui_grid(self):
        """Generates a two dimensional set of dictionaries.
        Items are tkinter buttons. Also configures tkinter grid for the frame.
        """
        for j in range(self.playheight):
            Grid.rowconfigure(self.root, j, weight=1)
            widgetrow = {}
            for i in range(self.playwidth):
                Grid.columnconfigure(self.root, i, weight=1)
                button = self.create_button(j, i)
                widgetrow[i] = button
            self.square_widgets[j] = widgetrow

    def create_button(self, j, i):
        """Creates and keybinds a tkinter button object for a designated square.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        Returns:
            button: The Button object.
        """
        button = Button(self.root, width=self.boxsize,
                        height=self.boxsize, image=self.images_tile[0])
        button.grid(row=j, column=i, sticky=NSEW)
        button.bind("<Button-1>", self.left_click_indicator(j, i))
        button.bind("<ButtonRelease-1>",
                    self.left_click_release_indicator(j, i))
        button.bind("<Leave>", self.left_click_leave_indicator(j, i))
        button.bind("<Button-3>", self.right_click_indicator(j, i))
        return button

    def ui_geometry(self):
        """Resizes the main windown according to the amount of squares.
        """
        self.rootwindown.geometry(
            f"{self.playwidth*self.boxsize}x{(self.playheight + 2)*self.boxsize}+400+150")
        self.rootwindown.resizable(False, False)

    def playtext(self):
        """Generates texts surrounding the game grid.
        """
        botleft = Label(self.root, text=f"Timer: {self.timer_count}")
        botright = Label(self.root, text=f"Mines: {self.mines}")
        botleft.grid(row=self.playheight+1, column=0,
                     columnspan=self.playwidth//2)
        botright.grid(row=self.playheight+1,
                      column=(self.playwidth//2)-1, columnspan=self.playwidth//2)
        Grid.rowconfigure(self.root, 0, weight=1)
        Grid.rowconfigure(self.root, self.playheight+1, weight=1)
        self.text_widgets.append(botleft)
        self.text_widgets.append(botright)

    def left_click_indicator(self, j, i):
        """Wrappers for button keybinding so that callback fuction doesn't break it.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        return lambda Button: self.left_click(j, i)

    def left_click_leave_indicator(self, j, i):
        """Wrappers for button keybinding so that callback fuction doesn't break it.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        return lambda Button: self.left_click_leave(j, i)

    def left_click_release_indicator(self, j, i):
        """Wrappers for button keybinding so that callback fuction doesn't break it.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        return lambda Button: self.left_click_release(j, i)

    def right_click_indicator(self, j, i):
        """Wrappers for button keybinding so that callback fuction doesn't break it.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        return lambda Button: self.right_click(j, i)

    def adjacent_click_indicator(self, j, i):
        """Wrappers for button keybinding so that callback fuction doesn't break it.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        return lambda Button: self.adjacent_click(j, i)

    def destroy_button(self, j, i):
        """Destroys the button object of a designated square.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        button = self.square_widgets[j][i]
        self.square_widgets[j][i] = 0
        button.destroy()

    def create_square_label(self, j, i):
        """Creates a label for designated square and keybinds it.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        label = Label(self.root, borderwidth=2, bg="white",
                      relief="sunken", width=52, height=52)
        label.bind("<Double-Button-1>", self.adjacent_click_indicator(j, i))
        return label

    def value(self, j, i):
        """Helper function that gets the value of a designated square.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        Returns:
            value: Value of the designated square
        """
        return self.grid_obj.grid[j][i].value

    def marked(self, j, i):
        """Helper function that gets the marked attribute of a designated square.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        Returns:
            marked: Boolean of the designated square
        """
        return self.grid_obj.grid[j][i].marked

    def hidden(self, j, i):
        """Helper function that gets the attribute named hidden of a designated square.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        Returns:
            hidden: Boolean of the designated square
        """
        return self.grid_obj.grid[j][i].hidden

    def left_click(self, j, i):
        """When square is clicked, changes the button image to a holder image.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        if not self.marked(j, i):
            self.square_widgets[j][i].config(image=self.images_numbers[0])
            self.leave = False

    def left_click_leave(self, j, i):
        """Sets button to default tile image if mouse leaves a clicked square.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        if not self.marked(j, i) and self.hidden(j, i):
            self.square_widgets[j][i].config(image=self.images_tile[0])
            self.leave = True

    def left_click_release(self, j, i):
        """Calls a fuction to draw a designated square when click is released.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        if not self.marked(j, i) and not self.leave:
            if not self.timer:
                self.grid_obj.place(j, i)
                self.timer = True
                self.update_timer()
                self.root.after(100, self.show_square(j, i))
            else:
                self.show_square(j, i)

    def show_square(self, j, i):
        """Draws designated square as a label according to its value or
        calls functions according to the value of the square.
        Calls functions to check if game is over.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        self.grid_obj.grid[j][i].hidden = False
        minebool = False
        if self.value(j, i) == "0":
            self.update_zeropath(j, i)
        else:
            self.destroy_button(j, i)
            label = self.create_square_label(j, i)
            if self.value(j, i) == "M":
                label.config(image=self.images_tile[1])
                minebool = True
            else:
                label.config(image=self.images_numbers[int(self.value(j, i))])
            label.grid(row=j, column=i)
            self.square_widgets[j][i] = label
        self.clickcount += 1
        self.check_game_over(minebool)

    def right_click(self, j, i):
        """Flags and un-flags a designated square.
        Also updates text on ui.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        if self.marked(j, i):
            self.square_widgets[j][i].config(image=self.images_tile[0])
            self.grid_obj.grid[j][i].marked = False
            self.flag_location.remove([j, i])
        else:
            self.square_widgets[j][i].config(image=self.images_tile[2])
            self.grid_obj.grid[j][i].marked = True
            self.flag_location.append([j, i])
        self.text_widgets[1].config(
            text=f"Mines: {self.mines-len(self.flag_location)}")

    def adjacent_click(self, j, i):
        """Calls drawing for specified adjacent squares after a designated square is double clicked.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        coordinates = self.grid_obj.adjacent(j, i)
        for pos in coordinates:
            self.show_square(pos[0], pos[1])

    def update_zeropath(self, j, i):
        """Calls functions to calculate coordinates of a path of zeros and surrounding squares
        starting from a designated square.
        Then draws squares corresponging to these coordinates.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        self.grid_obj.zeropath_clickcount = 0
        coordinates, clicks = self.grid_obj.zeropath(j, i, [[j, i]])
        self.clickcount += clicks
        for pos in coordinates:
            label = self.create_square_label(pos[0], pos[1])
            label.config(image=self.images_numbers[int(
                self.grid_obj.grid[pos[0]][pos[1]].value)])
            label.grid(row=pos[0], column=pos[1])
            self.square_widgets[pos[0]][pos[1]] = label

    def reset(self, geobool):
        """Calls functions to generate a new game and resets essential attributes.
        Args:
            geobool: Tells if the window size needs to be adjusted.
        """
        t1 = perf_counter()
        self.root.destroy()
        self.window()
        self.text_widgets = []
        self.square_widgets = {}
        self.game_settings()
        self.grid_obj.update(self.playheight, self.playwidth, self.mines)
        self.ui_grid()
        self.timer_count = 0
        self.timer = False
        self.playtext()
        if geobool:
            self.ui_geometry()
            self.game_over_window.update_settings()
        self.clickcount = 0
        self.flag_location = []
        self.rootwindown.update()
        t2 = perf_counter()
        print(t2-t1)

    def check_game_over(self, minebool):
        """Checks game over conditions.
        Args:
            minebool: Tells if a mine has been clicked.
        """
        if minebool:
            self.check_wrong_flag()
            self.game_over(True)
        elif self.clickcount == self.playwidth*self.playheight-self.mines:
            self.game_over(False)

    def check_wrong_flag(self):
        """Changes images on all incorrect flag locations.
        """
        for pos in self.flag_location:
            if not self.value(pos[0], pos[1]) == "M":
                self.square_widgets[pos[0]][pos[1]].config(
                    image=self.images_tile[3])

    def game_over(self, state):
        """Sets game over text and calls popup function.
        Args:
            state: Whether game is won or lost.
        """
        self.timer = False
        self.text_widgets[1].config(text=f"Mines: 0")
        self.game_over_window.game_over_popup(state, self.timer_count)

    def update_timer(self):
        """Updates timer until timer_count reaches 999 seconds.
        """
        if self.timer:
            if self.timer_count < 1000:
                self.timer_count += 1
                self.text_widgets[0].config(text=f"Timer: {self.timer_count}")
                self.root.after(1000, self.update_timer)
