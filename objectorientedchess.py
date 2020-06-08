import pygame
import os
import math
from drawboard import *


# The piece class which holds the positionsm colour and state of every piece



# The king class
class king(piece):
    def __init__(self, xcord, ycord, colour):
        self.surface = pygame.image.load("king.png")
        super().__init__(xcord, ycord, colour)
        
    def move(self, newx, newy): # move function
        xdif = abs(newx-self.xcord)
        ydif = abs(newy-self.ycord)
        if xdif <= 1 and ydif <= 1 and xdif + ydif != 0: # Makes sure king can't move more than one block out
            return True





def straight(self, newx, newy, players, stepx, stepy):
    if self.xcord == newx or self.ycord == newy:
            for i in range(self.xcord, newx, stepx):
                print(i)
                if i != newx:
                    if i != self.xcord:
                        print(i)
                        for k in players:
                            if k.xcord == i and k.ycord == self.ycord:
                                return
            for j in range(self.ycord, newy, stepy):
                if j != newy:
                    if j!= self.ycord:
                        for k in players:
                            if k.ycord == j and k.xcord == self.xcord:
                                returnz
            return True



class queen(piece):
    def __init__(self, xcord, ycord, colour):  
        self.surface = pygame.image.load("queen.png")  
        super().__init__(xcord, ycord, colour)
    def move(self, newx, newy): 

        if self.xcord <= newx:
            stepx = 1  
        else:
            stepx = -1
        if self.ycord <= newy:
            stepy = 1 
        else:
            stepy = -1
        if straight(self, newx, newy, players, stepx, stepy):
            return True
        
        if abs(newx - self.xcord) == abs(newy-self.ycord):
            for i in range(self.xcord, newx, stepx):
                print(i)
                return True
class bishop(piece):    
    def __init__(self, xcord, ycord, colour):
        self.surface = pygame.image.load("bishop.png")    
        super().__init__(xcord, ycord, colour)
    def move(self, newx, newy): 
        if abs(newx - self.xcord) == abs(newy-self.ycord):
            return True

class knight(piece):
    def __init__(self, xcord, ycord, colour):  
        self.surface = pygame.image.load("knight.png")
        super().__init__(xcord, ycord, colour)
    def move(self, newx, newy): 
        xdif = abs(newx-self.xcord)
        ydif = abs(newy-self.ycord)
        if xdif != 0 and ydif != 0 and xdif + ydif == 3:
            return True

class rook(piece):
    def __init__(self, xcord, ycord, colour):    
        self.surface = pygame.image.load("rook.png")

        super().__init__(xcord, ycord, colour)
    def move(self, newx, newy): 
        if self.xcord == newx or self.ycord == newy:
            return True 

class pawn(piece):
    def __init__(self, xcord, ycord, colour): 
        self.surface = pygame.image.load("pawn.png")   
        super().__init__(xcord, ycord, colour)
    def move(self, newx, newy): 
        if newx == self.xcord:
            if self.ycord == 2 and  0 < newy - self.ycord <= 2:
                return True
            elif newy - self.ycord == 1:
                return True
gameinit()
screen, clock = gameinit()
players = [pawn(i, 2, True) for i in range(1,9)]
players.append(rook(1,1, True))
players.append(knight(2,1, True))
players.append(bishop(3,1, True))
players.append(queen(4,1, True))   
players.append(king(5,1, True))
players.append(rook(8,1, True))
players.append(knight(7,1, True))
players.append(bishop(6,1, True))
gamerun(players, screen, clock)
