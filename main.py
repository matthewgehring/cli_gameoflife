# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep

from Board import *

def game(init):
    i = init
    if i == 0:
        board = Board(10, 10)
        board.newGame()
        i= 1
    while(True):
        board.display()
        #board.update()
        print('generation: ' + str(i))
        i += 1
        sleep(1)
        system('cls')
