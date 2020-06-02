import drawboard


# The piece class which holds the positionsm colour and state of every piece
class piece:
    def __init__(self, xcord, ycord, colour):
        self.xcord = xcord
        self.ycord = ycord
        self.taken = False
        self.colour = True # true = white ; false = black Not a racist remark

# The king class
class king(piece):
    def __init__(self, xcord, ycord, colour):    
        super().__init__(xcord, ycord, colour)
    def move(self, newx, newy): # move function
        if abs(newx-self.xcord)<= 1 and abs(newy-self.ycord)<= 1 : # Makes sure king can't move more than one block out, king can stay in spot tho
            self.xcord = newx       
            self.ycord = newy

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
        self.xcord = newx       
        self.ycord = newy

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
