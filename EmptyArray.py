from random import randint

def arrayGenerator(Board):
    b = [[0 for elm in range(0,Board.x)]for item in range(0, Board.y)]
    
    return b

def seedBoard(Board):
    seeded = [[("  ",u'\u2588' + u'\u2588')[randint(0,1)] for elm in range(0,Board.x)]for item in range(0, Board.y)]
    return seeded


