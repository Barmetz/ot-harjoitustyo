class Square:
    def __init__(self, value, isHidden):
        self.value = "0"
        self.isHidden = True
        self.marked = False
    
    def __str__(self):
        return self.value