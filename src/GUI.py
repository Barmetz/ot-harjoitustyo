import sys 
from tkinter import *
from tkinter import ttk
from gridLogic import MSGrid

class Main():
    def __init__(self):
        self.playheight = 10
        self.playwidth = 10
        self.mineTotal = 10
        self.gridObj = MSGrid(self.playheight,self.playwidth,self.mineTotal)
        self.widgets = []
        self.colors_bg = []
        self.colors_activebg = []

    def main(self):
        self.tk = Tk()
        self.GUIgrid()
        self.playtext()
        self.GUIgrid_size()
        self.tk.mainloop()
    
    def GUIgrid(self):
        for j in range(1,self.playheight+1):
            Grid.rowconfigure(self.tk, j, weight=1)
            widgetrow = []
            for i in range(self.playwidth):
                Grid.columnconfigure(self.tk, i, weight=1)
                button = Button(self.tk)
                button.grid(row=j, column=i, sticky=NSEW)
                button.bind("<Button-1>", self.leftClick_indicator(j,i))
                button.bind("<Button-3>", self.rightClick_indicator(j,i))
                widgetrow.append(button)
                if j == 1 and i == 0:
                    self.colors_bg.append(button.cget("background"))
                    self.colors_activebg.append(button.cget("activebackground"))
            self.widgets.append(widgetrow)
    
    def GUIgrid_size(self):
        self.tk.geometry(f"{self.playwidth*50}x{(self.playheight + 2)*50}+800+300")
        self.tk.minsize(self.playwidth*22,(self.playheight + 2)*22) 

    def playtext(self):
        self.tk.resizable(True,True)
        top = Label(self.tk, text="Minesweeper")
        botleft = Label(self.tk, text="Clock: 0")
        botright = Label(self.tk, text="Mines: 0")
        sizegrip = ttk.Sizegrip(self.tk)
        top.grid(row=0, column=0, columnspan=self.playwidth)
        botleft.grid(row=self.playheight+1, column=0, columnspan=self.playwidth//2)
        botright.grid(row=self.playheight+1, column=(self.playwidth//2)-1, columnspan=self.playwidth//2)
        sizegrip.grid(row=self.playheight+1, column=self.playwidth-1, sticky=SE)
        Grid.rowconfigure(self.tk, 0, weight=1)
        Grid.rowconfigure(self.tk, self.playheight+1, weight=1)

    def leftClick_indicator(self, j, i):
        return lambda Button: self.leftClick(j,i)
    
    def rightClick_indicator(self, j, i):
        return lambda Button: self.rightClick(j,i)

    def leftClick(self, j, i):
        self.gridObj.grid[j-1][i].isHidden = False
        self.destroyButton(j, i)
        label = Label(self.tk, text=f"{self.gridObj.grid[j-1][i].value}", bg="white", fg="black", borderwidth=2, relief="sunken")
        label.grid(row=j, column=i, sticky=NSEW)
        self.widgets[j-1][i] = label

    def destroyButton(self, j, i):
        button = self.widgets[j-1][i]
        self.widgets[j-1][i] = 0
        button.destroy()

    def rightClick(self, j, i):
        if self.gridObj.grid[j-1][i].isMarked:
            self.widgets[j-1][i].config(bg=self.colors_bg[0], activebackground=self.colors_activebg[0])
            self.gridObj.grid[j-1][i].isMarked = False
        else:
            self.widgets[j-1][i].config(bg="red", activebackground="red") 
            self.gridObj.grid[j-1][i].isMarked = True
if __name__ == "__main__":
    a = Main()
    a.main()