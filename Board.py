from EmptyArray import arrayGenerator, seedBoard
import pprint
pp = pprint.PrettyPrinter(indent=4)

class Board:
    def __init__(self, width, height):
        self.x = width
        self.y = height
        self.board = []

    def newGame(self):
        self.board = arrayGenerator(self)
        
    def seed(self):
        self.board = seedBoard(self)
        
        
    def display(self):
        for row in self.board:
            print(''.join(row))
            #for val in row
