# import only system from os 
from os import system, name 
import platform
  
# import sleep to show output for some time period 
from time import sleep

from Board import *

def game(init):
    i = init
    if i == 0:
        gameBoard = Board(40, 40)
        gameBoard.newGame()
        gameBoard.seed()
        i= 1
    while(True):
        gameBoard.display()
        gameBoard.update()
        #print('generation: ' + str(i))
        #i += 1
        sleep(0)
        if(platform.system() == "Windows"):
            system('cls')
        else:
            system('clear')
