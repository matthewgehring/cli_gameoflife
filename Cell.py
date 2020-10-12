class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getNeighbors(self, width, height):
        #top left corner
        if self.x == 0 and self.y == 0:
            return [(width-1, height-1),
                (width - 1, 0),
                (width-1, 1),
                (0, height-1),
                (1, height-1),
                (1, 0),
                (0, 1),
                (1, 1)]
        #top right corner
        if self.x == width-1 and self.y == 0:
            return [(-1*(width-1),(height-1)),
                    (0, height-1),
                    (-1, height-1),
                    (-1*(width-1), 0),
                    (-1*(width-1), 1),
                    (-1, 0),
                    (-1, 1),
                    (0, 1)]
                    
        #bottom left corner
        if self.x == 0 and self.y == height-1:
            return [(width-1, -1*(height-1)),
                     (width-1, 0),
                     (0, -1*(height-1)),
                     (1, -1*(height-1)),
                     (width-1, -1),
                     (0, -1),
                     (1, -1),
                     (1, 0)]
        #bottom right corner
        if self.x == width-1 and self.y == height-1:
            return [(-1*(width-1),-1*(height-1)),
                    (-1*(width-1), 0),
                     (0, -1*(height-1)),
                     (-1, -1*(height-1)),
                     (-1*(width-1), -1),
                     (-1, -1),
                     (-1, 0),
                     (0, -1)]
        #top of board
        if self.y == 0:
            return [(-1, height-1),
                (0, height-1),
                (1, height-1),
                (-1, 0),
                (1, 0),
                (-1, 1),
                (0, 1),
                (1, 1)]
        #bottom of board
        if self.y == height-1:
            return [(-1, -1),
                (0, -1),
                (1, -1),
                (-1, 0),
                (1, 0),
                (-1, -1*(height-1)),
                (0, -1*(height-1)),
                (1, -1*(height-1))]
        #left side of board
        if self.x == 0:
            return [(width-1, -1),
                (0, -1),
                (1, -1),
                (width-1, 0),
                (1, 0),
                (width-1, 1),
                (0, 1),
                (1, 1)]
        #right side of board
        if self.x == width-1:
            return [(-1, -1),
                (0, -1),
                (-1*(width-1), -1),
                (-1, 0),
                (-1*(width-1), 0),
                (-1, 1),
                (0, 1),
                (-1*(width-1), 1)]
        return [(-1, -1),
                (0, -1),
                (1, -1),
                (-1, 0),
                (1, 0),
                (-1, 1),
                (0, 1),
                (1, 1)]
