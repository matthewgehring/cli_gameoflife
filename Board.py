from random import randint
from Cell import Cell
import copy
from shapes import gliderGun

class Board:
    def __init__(self, width, height):
        self.x = width
        self.y = height
        self.board = []
        self.displayBoard = []

    def newGame(self):
        self.board = [[0 for col in range(0,self.x)]for row in range(0, self.y)]
        
    def seed(self):
        #self.board = [[(0,1)[randint(0,1)] for item in row] for row in self.board]
        self.board = gliderGun()

    def update(self):
        #consider something different here
        tempboard = Board(self.x, self.y)
        tempboard.newGame()
        for y in range(0,self.y):
            for x in range(0,self.x):
                cell = Cell(x, y)
                neighborSum = 0
                neighbors = cell.getNeighbors(self.x, self.y) #returns [(x,y}, (x,y) ...]
                for neighbor in neighbors:
                    dx, dy = neighbor
                    if self.board[y + (dy)][x + (dx)] == 1:
                        neighborSum += 1
                #Game of Life logic
                if self.board[y][x] == 1 and neighborSum <= 1:
                    tempboard.board[y][x] = 0
                elif self.board[y][x] == 1 and neighborSum > 1 and neighborSum <=3:
                    tempboard.board[y][x] = 1
                elif self.board[y][x] == 1 and neighborSum > 3:
                    tempboard.board[y][x] = 0
                elif self.board[y][x] == 0 and neighborSum == 3:
                    tempboard.board[y][x] = 1
        self.board = copy.copy(tempboard.board)
                

    def __createDisplayBoard(self):
        self.displayBoard = [[u'\u2588' + u'\u2588' if (item) else "  " for item in row] for row in self.board]
        
    def display(self):
        self.__createDisplayBoard()
        for row in self.displayBoard:
            print(''.join(row))
            
