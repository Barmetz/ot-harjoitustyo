class Square:
    """Represents a single square in-game.
    Attributes:
        value: either M for mine or number value equal to mines in surrounding squares
        hidden: is the square visible for the player or clickable
        marked: is the square marked with a flag
    """

    def __init__(self):
        """Construtor. Sets up a square with default values.
        """
        self.value = "0"
        self.hidden = True
        self.marked = False

    def __str__(self):
        return self.value
