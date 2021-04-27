from random import randint
from logic.square import Square


class MSGrid:
    def __init__(self, height, width, mines):
        self.mines = mines
        self.height = height
        self.width = width
        self.main()
        self.zeropath_clickcount = 0

    def __str__(self):
        grid = []
        for j in range(self.height):
            row = []
            for i in self.grid[j].values():
                row.append(i.value)
            grid.append(row)
        return str(grid)

    def update(self, height, width, mines):
        self.mines = mines
        self.height = height
        self.width = width
        self.main()

    def main(self):
        self.grid = self.generate_grid()
        self.place_mines()
        self.place_numbers()

    # Generates an empty grid of the initialized size
    def generate_grid(self):
        grid = {}
        for j in range(self.height):
            row = {}
            for i in range(self.width):
                row[i] = (Square())
            grid[j] = row
        return grid

    # Places initialized amount of mines to the grid
    def place_mines(self):
        minecount = 0
        minelocation = []
        while minecount < self.mines:
            pos_j = randint(0, self.height-1)
            pos_i = randint(0, self.width-1)
            if (pos_j, pos_i) not in minelocation:
                minelocation.append((pos_j, pos_i))
                minecount += 1
        for i in minelocation:
            self.grid[i[0]][i[1]].value = "M"

    # Checks if designated square is a mine
    def is_mine(self, pos_j, pos_i):
        return self.grid[pos_j][pos_i].value == "M"

    def place_numbers(self):
        for j in range(self.height):
            for i in range(self.width):
                if not self.is_mine(j, i):
                    number = 0
                    neighbours = self.neighbours(j, i)
                    for coord in neighbours:
                        if self.is_mine(coord[0], coord[1]):
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

    def zeropath(self, j, i, visited):
        neighbours = self.neighbours(j, i)
        for coord in neighbours:
            if coord not in visited:
                if self.grid[coord[0]][coord[1]].hidden:
                    self.grid[coord[0]][coord[1]].hidden = False
                    self.zeropath_clickcount += 1
                visited.append(coord)
                if self.grid[coord[0]][coord[1]].value == "0":
                    self.zeropath(coord[0], coord[1], visited)
        return visited, self.zeropath_clickcount
