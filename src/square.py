class Square:
    def __init__(self):
        self.value = "0"
        self.hidden = True
        self.marked = False

    def __str__(self):
        return self.value
