from square import Square
from random import randint
class Grid:
    def __init__(self, height, width, mines):
        self.mines = mines
        self.height = height
        self.width = width
        self.grid = self.generateGrid(height, width)
        self.placeMines()
        self.placeNumbers()
    
    def __str__(self):
        grid = []
        for j in self.grid:
            row = []
            for i in j:
                row.append(i.value)
            grid.append(row)
        return str(grid)

    #Generates an empty grid of the initialized size
    def generateGrid(self, y, x):
        grid = []
        for _ in range(y):
            row = []
            for _ in range(x):
                row.append(Square(0, True))
            grid.append(row)
        return grid
    
    #Places initialized amount of mines to the grid
    def placeMines(self):
        minecount = 0
        minelocation = []
        while minecount<self.mines:
            y = randint(0, self.height-1)
            x = randint(0, self.width-1)
            if (y,x) not in minelocation:
                minelocation.append((y,x))
                minecount += 1
        for i in minelocation:
            self.grid[i[0]][i[1]].value = "M"
    
    #Checks if designated square is a mine
    def isMine(self, y, x):
        return self.grid[y][x].value == "M"

    def placeNumbers(self):
        for j in range(self.height):
            for i in range(self.width):
                if not self.isMine(j, i):
                    number = 0
                    if j > 0:
                        if self.isMine(j-1, i):
                            number += 1
                        if i>0 and self.isMine(j-1, i-1):
                            number += 1
                        if i<self.width-1 and self.isMine(j-1, i+1):
                            number += 1
                    if i > 0 and self.isMine(j, i-1):
                        number += 1
                    if i < self.width - 1 and self.isMine(j, i+1):
                        number += 1
                    if j < self.height-1:
                        if self.isMine(j+1, i):
                            number += 1
                        if i>0 and self.isMine(j+1, i-1):
                            number += 1
                        if i<self.width-1 and self.isMine(j+1, i+1):
                            number += 1
                    self.grid[j][i].value = str(number)

if __name__ == "__main__":
    a = Grid(10, 10, 5)
    print(a)
    a.placeMines()
    print(a)    
    a.placeNumbers()
    print(a)
