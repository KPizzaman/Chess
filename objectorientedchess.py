import drawboard


# The piece class which holds the positionsm colour and state of every piece
class piece:
    def __init__(self, xcord, ycord, colour):
        self.xcord = xcord
        self.ycord = ycord
        self.taken = False
        self.colour = colour # true = white ; false = black Not a racist remark

# The king class
class king(piece):
    def __init__(self, xcord, ycord, colour):    
        super().__init__(xcord, ycord, colour)
        
    def move(self, newx, newy): # move function
        xdif = abs(newx-self.xcord)
        ydif = abs(newy-self.ycord)
        if xdif <= 1 and ydif <= 1 and xdif + ydif != 0: # Makes sure king can't move more than one block out
            self.xcord = newx       
            self.ycord = newy
            print("move completed")
class queen(piece):
    def __init__(self, xcord, ycord, colour):    
        super().__init__(xcord, ycord, colour)
    def move(self, newx, newy): 
        self.xcord = newx       
        self.ycord = newy

class bishop(piece):    
    def __init__(self, xcord, ycord, colour):    
        super().__init__(xcord, ycord, colour)
    def move(self, newx, newy): 
        self.xcord = newx       
        self.ycord = newy

class knight(piece):
    def __init__(self, xcord, ycord, colour):    
        super().__init__(xcord, ycord, colour)
    def move(self, newx, newy): 
        xdif = abs(newx-self.xcord)
        ydif = abs(newy-self.ycord)
        if xdif != 0 and ydif != 0 and xdif + ydif == 3:
            self.xcord = newx       
            self.ycord = newy
            print("move completed")
class rook(piece):
    def __init__(self, xcord, ycord, colour):    
        super().__init__(xcord, ycord, colour)
    def move(self, newx, newy): 
        self.xcord = newx       
        self.ycord = newy

class pawn(piece):
    def __init__(self, xcord, ycord, colour):    
        super().__init__(xcord, ycord, colour)
    def move(self, newx, newy): 
        self.xcord = newx       
        self.ycord = newy
