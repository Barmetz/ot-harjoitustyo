from random import randint
from logic.square import Square


class MSGrid:
    """Grid of Square objects that represents the game.
    Functions for changing square values and calculating paths:
    Attributes:
        mines: Amount of mines the grid should contain.
        height: Grid height.
        width: Grid width.
        zeropath_clickcount: Specific attribute for zeropath function.
                            Used for calculating amount of squares clicked.
    """

    def __init__(self, height, width, mines):
        """Constructor that sets up attributes and calls main function.
        Args:
            height: Desired grid height.
            width: Desired grid width.
            mines: Desired amount of mines.
        """
        self.mines = mines
        self.height = height
        self.width = width
        self.main()
        self.zeropath_clickcount = 0

    def __str__(self):
        """Forms a string type version of the grid.
        Returns:
            str(grid): String type version of the two-dimensional grid
                    with items being the values of squares.
        """
        grid = []
        for j in range(self.height):
            row = []
            for i in self.grid[j].values():
                row.append(i.value)
            grid.append(row)
        return str(grid)

    def update(self, height, width, mines):
        """Sets up new parametres and creates a new grid
        Args:
            height: Desired grid height.
            width: Desired grid width.
            mines: Desired amount of mines.
        """
        self.mines = mines
        self.height = height
        self.width = width
        self.main()

    def main(self):
        """Calls functions to create a new grid.
        """
        self.grid = self.generate_grid()
        self.place_mines()
        self.place_numbers()

    def generate_grid(self):
        """Cretes a two dimensional set of dictionaries of the initialized size.
        Returns:
            grid: Two dimensional set of dictionaries.
        """
        grid = {}
        for j in range(self.height):
            row = {}
            for i in range(self.width):
                row[i] = Square()
            grid[j] = row
        return grid

    def place_mines(self):
        """Randomizes coordinates for mines and places the mines in to the grid.
        """
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

    def is_mine(self, j, i):
        """Checks if designated square is a mine
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        return self.grid[j][i].value == "M"

    def place_numbers(self):
        """Calculates the amount of mines surrounding every square
        and assings the value to the square.
        """
        for j in range(self.height):
            for i in range(self.width):
                if not self.is_mine(j, i):
                    number = 0
                    neighbours = self.neighbours(j, i)
                    for pos in neighbours:
                        if self.is_mine(pos[0], pos[1]):
                            number += 1
                    self.grid[j][i].value = str(number)

    def neighbours(self, j, i):
        """Determines coordinates of surrounding squares in relation to designated square.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
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

    def neighbour_marked_count(self, j, i):
        """Calculates the amount of flags surrounding designated square.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        Returns:
            number: Amount of flags surrounding designated square.
        """
        number = 0
        neighbours = self.neighbours(j, i)
        for pos in neighbours:
            if self.grid[pos[0]][pos[1]].marked:
                number += 1
        return number

    def zeropath(self, j, i, visited):
        """Recursive function that calculates a path of zeros starting from designated square.
        Designated square should have a value of 0. Also processes all squares surrounding the path.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        Returns:
            visited: coordinates of the path and squares surrounding the path.
            zeropath_clickcount: amount of visited squares
        """
        neighbours = self.neighbours(j, i)
        for pos in neighbours:
            if pos not in visited:
                if self.grid[pos[0]][pos[1]].hidden:
                    self.grid[pos[0]][pos[1]].hidden = False
                    self.zeropath_clickcount += 1
                visited.append(pos)
                if self.grid[pos[0]][pos[1]].value == "0":
                    self.zeropath(pos[0], pos[1], visited)
        return visited, self.zeropath_clickcount

    def adjacent(self, j, i):
        """Calculates all non-flagged and hidden squares surrounding the designated square.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        Returns:
            coordinates: Locations of specified squares.
        """
        coordinates = []
        if int(self.grid[j][i].value) == self.neighbour_marked_count(j, i):
            neighbours = self.neighbours(j, i)
            for pos in neighbours:
                if not self.grid[pos[0]][pos[1]].marked and self.grid[pos[0]][pos[1]].hidden:
                    self.grid[pos[0]][pos[1]].hidden = False
                    coordinates.append(pos)
        return coordinates
