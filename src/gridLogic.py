from square import Square
from random import randint


class MSGrid:
    def __init__(self, height, width, mines):
        self.mines = mines
        self.height = height
        self.width = width
        self.grid = self.generateGrid(height, width)
        self.placeMines()
        self.placeNumbers()
        self.zeroPath_clickcount = 0

    def __str__(self):
        grid = []
        for j in self.grid:
            row = []
            for i in j:
                row.append(i.value)
            grid.append(row)
        return str(grid)

    # Generates an empty grid of the initialized size
    def generateGrid(self, y, x):
        grid = []
        for _ in range(y):
            row = []
            for _ in range(x):
                row.append(Square(0, True))
            grid.append(row)
        return grid

    # Places initialized amount of mines to the grid
    def placeMines(self):
        minecount = 0
        minelocation = []
        while minecount < self.mines:
            y = randint(0, self.height-1)
            x = randint(0, self.width-1)
            if (y, x) not in minelocation:
                minelocation.append((y, x))
                minecount += 1
        for i in minelocation:
            self.grid[i[0]][i[1]].value = "M"

    # Checks if designated square is a mine
    def isMine(self, y, x):
        return self.grid[y][x].value == "M"

    def placeNumbers(self):
        for j in range(self.height):
            for i in range(self.width):
                if not self.isMine(j, i):
                    number = 0
                    neighbours = self.neighbours(j, i)
                    for coord in neighbours:
                        if self.isMine(coord[0], coord[1]):
                            number += 1
                    self.grid[j][i].value = str(number)

    def neighbours(self, j, i):
        neighbours = []
        if j > 0:
            neighbours.append([j-1, i])
            if i > 0:
                neighbours.append([j-1, i-1])
            if i < self.width - 1:
                neighbours.append([j-1, i+1])
        if i > 0:
            neighbours.append([j, i-1])
        if i < self.width - 1:
            neighbours.append([j, i+1])
        if j < self.height - 1:
            neighbours.append([j+1, i])
            if i > 0:
                neighbours.append([j+1, i-1])
            if i < self.width - 1:
                neighbours.append([j+1, i+1])
        return neighbours

    def zeroPath(self, j, i, visited):
        neighbours = self.neighbours(j, i)
        for coord in neighbours:
            if coord not in visited:
                if self.grid[coord[0]][coord[1]].isHidden:
                    self.grid[coord[0]][coord[1]].isHidden = False
                    self.zeroPath_clickcount += 1
                visited.append(coord)
                if self.grid[coord[0]][coord[1]].value == "0":
                    self.zeroPath(coord[0], coord[1], visited)
        return visited, self.zeroPath_clickcount


if __name__ == "__main__":
    a = MSGrid(10, 10, 5)
    # print(a)
    a.placeMines()
    # print(a)
    a.placeNumbers()
    # print(a)
    b = MSGrid(3, 3, 0)
    print(b)
    b.zeroPath(1, 1, [[1, 1]])
