from random import randint
from Cell import Cell

class Board:
    def __init__(self, width, height):
        self.x = width
        self.y = height
        self.board = []
        self.displayBoard = []

    def newGame(self):
        self.board = [[0 for col in range(0,self.x)]for row in range(0, self.y)]
        
    def seed(self):
        self.board = [[(0,1)[randint(0,1)] for item in row] for row in self.board]

    def update(self):
        for y in range(0,self.y):
            for x in range(0,self.x):
                cell = Cell(x, y)
                neighborSum = 0
                neighbors = cell.getNeighbors(self.x, self.y) #returns [(x,y}, (x,y) ...]
                for neighbor in neighbors:
                    dx, dy = neighbor
                    if self.board[x + dx][y + dy] == 1:
                        neighborSum += 1
                #put game of Life Logic here
            
            

    def __createDisplayBoard(self):
        self.displayBoard = [[u'\u2588' + u'\u2588' if (item) else "  " for item in row] for row in self.board]
        
    def display(self):
        self.__createDisplayBoard()
        for row in self.displayBoard:
            print(''.join(row))
            #for val in row
