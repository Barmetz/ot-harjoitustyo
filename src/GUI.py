import sys
from tkinter import Label, Button, messagebox, Tk, Grid, NSEW, Toplevel
from tkinter import ttk
from gridlogic import MSGrid
from PIL import Image, ImageTk


class Main():
    def __init__(self):
        #These will become main attributes of the game
        self.playheight = 10
        self.playwidth = 10
        self.mineTotal = 5
        self.boxsize = 50
        
        self.gridObj = MSGrid(self.playheight, self.playwidth, self.mineTotal)
        self.button_widgets = []
        self.text_widgets = []
        self.flag = 0
        self.clickcount = 0

    def main(self):
        self.tk = Tk()
        self.tk.title("Minesweeper")
        self.create_images()
        self.GUIgrid()
        self.playtext()
        self.GUIgrid_size()
        self.tk.mainloop()

    #Creates arrays for tile graphics and resize images acording to boxsize
    def create_images(self): 
        self.images_numbers = []  #Images for the numbers
        
        image_size = (self.boxsize, self.boxsize)
        half_image_size = (self.boxsize//2, self.boxsize//2)
        self.images_numbers.append(ImageTk.PhotoImage(
            Image.open("src/images/clicked.png").resize(image_size)))
        for i in range(1, 9):
            self.images_numbers.append(ImageTk.PhotoImage(Image.open(
                "src/images/number"+str(i)+".png").resize(half_image_size)))

        self.images_tile = [] #Images for hidden tiles, flags and mines
        
        self.images_tile.append(ImageTk.PhotoImage(
            Image.open("src/images/tile.png").resize(image_size)))
        self.images_tile.append(ImageTk.PhotoImage(
            Image.open("src/images/mine.png").resize(half_image_size)))
        self.images_tile.append(ImageTk.PhotoImage(
            Image.open("src/images/flag.png").resize((image_size))))
        self.images_tile.append(ImageTk.PhotoImage(Image.open(
            "src/images/wrong_flag.png").resize((image_size))))

    #Generates a grid of tkinter buttons
    def GUIgrid(self): 
        for j in range(1, self.playheight+1):
            Grid.rowconfigure(self.tk, j, weight=1)
            widgetrow = []
            for i in range(self.playwidth):
                Grid.columnconfigure(self.tk, i, weight=1)
                button = Button(self.tk, width=50, height=50,
                                image=self.images_tile[0])
                button.grid(row=j, column=i, sticky=NSEW)
                button.bind("<Button-1>", self.leftClick_indicator(j, i))
                button.bind("<ButtonRelease-1>",
                            self.leftClick_release_indicator(j, i))
                button.bind("<Leave>", self.leftClick_leave_indicator(j, i))
                button.bind("<Button-3>", self.rightClick_indicator(j, i))
                widgetrow.append(button)
            self.button_widgets.append(widgetrow)

    #Resizes the main windown according to the amount of squares
    def GUIgrid_size(self):
        self.tk.geometry(
            f"{self.playwidth*50}x{(self.playheight + 2)*50}+800+300")
        self.tk.resizable(False, False)

    #Generates general label widgets for the UI
    def playtext(self):
        top = Label(self.tk, text="This text will get fixed..... eventually")
        botleft = Label(self.tk, text="Clock: 0")
        botright = Label(self.tk, text=f"Mines: {self.mineTotal}")
        top.grid(row=0, column=0, columnspan=self.playwidth)
        botleft.grid(row=self.playheight+1, column=0,
                     columnspan=self.playwidth//2)
        botright.grid(row=self.playheight+1,
                      column=(self.playwidth//2)-1, columnspan=self.playwidth//2)
        Grid.rowconfigure(self.tk, 0, weight=1)
        Grid.rowconfigure(self.tk, self.playheight+1, weight=1)
        self.text_widgets.append(botleft)
        self.text_widgets.append(botright)
        self.text_widgets.append(top)

    #Wrappers for buttons so that callback fuction doesn't break them
    def leftClick_indicator(self, j, i):
        return lambda Button: self.leftClick(j, i)

    def leftClick_leave_indicator(self, j, i):
        return lambda Button: self.leftClick_leave(j, i)

    def leftClick_release_indicator(self, j, i):
        return lambda Button: self.leftClick_release(j, i)

    def rightClick_indicator(self, j, i):
        return lambda Button: self.rightClick(j, i)

    #The functions for Buttons
    def leftClick(self, j, i):
        if not self.gridObj.grid[j-1][i].marked:
            self.button_widgets[j-1][i].config(image=self.images_numbers[0])
            self.leave = False

    def leftClick_leave(self, j, i):
        if not self.gridObj.grid[j-1][i].marked and self.gridObj.grid[j-1][i].hidden:
            self.button_widgets[j-1][i].config(image=self.images_tile[0])
            self.leave = True

    def leftClick_release(self, j, i):
        if not self.gridObj.grid[j-1][i].marked and not self.leave:
            self.gridObj.grid[j-1][i].hidden = False
            if self.gridObj.grid[j-1][i].value == "0":
                self.update_zeropath(j, i)
            else:
                self.destroyButton(j, i)
                if self.gridObj.grid[j-1][i].value == "M":
                    label = Label(
                        self.tk, image=self.images_tile[1], borderwidth=2, bg="white", relief="sunken", width=52, height=52)
                    self.game_over(True)
                else:
                    label = Label(self.tk, image=self.images_numbers[int(
                        self.gridObj.grid[j-1][i].value)], borderwidth=2, bg="white", relief="sunken", width=52, height=52)
                label.grid(row=j, column=i)
                self.button_widgets[j-1][i] = label
            self.clickcount += 1
            if self.clickcount == self.playwidth*self.playheight-self.mineTotal:
                self.game_over(False)

    def destroyButton(self, j, i):
        button = self.button_widgets[j-1][i]
        self.button_widgets[j-1][i] = 0
        button.destroy()

    def rightClick(self, j, i):
        if self.gridObj.grid[j-1][i].marked:
            self.button_widgets[j-1][i].config(image=self.images_tile[0])
            self.gridObj.grid[j-1][i].marked = False
            self.flag -= 1
        else:
            self.button_widgets[j-1][i].config(image=self.images_tile[2])
            self.gridObj.grid[j-1][i].marked = True
            self.flag += 1
        self.text_widgets[1].config(text=f"Mines: {self.mineTotal-self.flag}")

    #When clicking a 0 square automatically open the all connected 0 squares and their neighbours
    def update_zeropath(self, j, i):
        self.gridObj.zeropath_clickcount = 0
        coordinates, clicks = self.gridObj.zeropath(j-1, i, [[j-1, i]])
        self.clickcount += clicks
        for coord in coordinates:
            label = Label(self.tk, image=self.images_numbers[int(
                self.gridObj.grid[coord[0]][coord[1]].value)], borderwidth=2, bg="white", relief="sunken", width=52, height=52)
            label.grid(row=coord[0]+1, column=coord[1])
            self.button_widgets[coord[0]][coord[1]] = label

    #Game over text and pop-up.
    def game_over(self, state):
        if state:
            self.game_over_popup("Game Over. You lost!")
        else:
            self.text_widgets[1].config(text=f"Mines: 0")
            self.game_over_popup("Game Over. You win!")

    def game_over_popup(self, text):
        pop = Toplevel(self.tk)
        pop.focus_set()
        pop.grab_set()
        pop.title(text.split(".")[1])
        label = Label(pop, text=text)
        label.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        button = Button(pop, text="New Game", command=lambda: self.reset(pop))
        button.grid(row=1, column=0)
        button = Button(pop, text="Exit", command=self.tk.destroy)
        button.grid(row=1, column=1)
        for i in range(2):
            pop.grid_rowconfigure(i, weight=1)
            pop.grid_columnconfigure(i, weight=1)
        pop.geometry(
            f"250x150+{800+25*self.playwidth-125}+{300+(self.playheight + 2)*25-75}")
        pop.resizable(False, False)

    #Start a new game from endgame window
    def reset(self, pop):
        pop.destroy()
        self.gridObj = MSGrid(self.playheight, self.playwidth, self.mineTotal)
        self.destroy_widgets()
        self.GUIgrid()
        self.playtext()
        self.clickcount = 0
        self.flag = 0

    #destroys button 
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


if __name__ == "__main__":
    Main().main()
