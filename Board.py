from EmptyArray import arrayGenerator

class Board:
    def __init__(self, width, height):
        self.x = width
        self.y = height
        self.board = []

    def newGame(self):
        self.board = arrayGenerator(self.x, self.y)
        
    def display(self):
        for row in self.board:
            print(row)
            #for val in row:
