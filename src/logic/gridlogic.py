from random import randint
from logic.square import Square


class MSGrid:
    """Grid of Square objects that represents the game.
    Functions for changing square values and calculating paths:
    Attributes:
        grid: Two dimensional set of dictionaries.
        mines: Amount of mines the grid should contain.
        height: Height of the grid.
        width: Width of the grid.
        zeropath_clickcount: Specific attribute for zeropath function.
                            Used for calculating amount of squares in the path.
    """

    def __init__(self, height: int, width: int, mines: int):
        """Constructor. Calls functions to set up a grid.
        Args:
            height: Desired grid height.
            width: Desired grid width.
            mines: Desired amount of mines.
        """
        self.grid = {}
        self.update(height, width, mines)
        self.zeropath_clickcount = 0

    def __str__(self):
        """Forms a string type version of the grid.
        Returns:
            str(grid): String type version of the two-dimensional grid
                    with items being the values of the squares.
        """
        grid = []
        for j in range(self.height):
            row = []
            for i in self.grid[j].values():
                row.append(i.value)
            grid.append(row)
        return str(grid)

    def update(self, height, width, mines):
        """Updates new parametres and creates a new grid.
        Args:
            height: Desired grid height.
            width: Desired grid width.
            mines: Desired amount of mines.
        """
        self.mines = mines
        self.height = height
        self.width = width
        self.generate_grid()

    def generate_grid(self):
        """Creates a two dimensional set of dictionaries of the desired size.
        """
        grid = {}
        for j in range(self.height):
            row = {}
            for i in range(self.width):
                row[i] = Square()
            grid[j] = row
        self.grid = grid

    def place(self, j, i):
        """Calls place functions.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        self.place_mines(j, i)
        self.place_numbers()

    def place_mines(self, j, i):
        """Randomizes coordinates for mines and places the mines in to the grid.
        Designated square is the first square clicked at game start.
        Designated square and its neighbours cant be mines to ensure
        a playable/enjoyable game start.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        minecount = 0
        disallowed = self.neighbours(j, i)
        disallowed.append([j, i])
        mines = []
        while minecount < self.mines:
            pos_j = randint(0, self.height-1)
            pos_i = randint(0, self.width-1)
            coord = [pos_j, pos_i]
            if coord not in mines and coord not in disallowed:
                mines.append(coord)
                minecount += 1
        for pos in mines:
            self.grid[pos[0]][pos[1]].value = "M"

    def is_mine(self, j, i):
        """Checks if a designated square is a mine.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        """
        return self.grid[j][i].value == "M"

    def place_numbers(self):
        """For all squares calculates the amount of mines surrounding a square
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
        """Determines coordinates of squares around a designated square.
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
        """Calculates the amount of flags surrounding a designated square.
        Args:
            j: Row of the designated square.
            i: Column of the designated square.
        Returns:
            number: Amount of flags surrounding the designated square.
        """
        number = 0
        neighbours = self.neighbours(j, i)
        for pos in neighbours:
            if self.grid[pos[0]][pos[1]].marked:
                number += 1
        return number

    def zeropath(self, j, i, visited):
        """Recursive function that calculates a path of zeros starting from a designated square.
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
        """Calculates all non-flagged and hidden squares surrounding a designated square if
        a square is surrounded with amount of flags equal to its value.
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
