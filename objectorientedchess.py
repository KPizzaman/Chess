import pygame
import os
import math
from drawboard import *


# The piece class which holds the positionsm colour and state of every piece



# The king class
class king(piece):
    def __init__(self, xcord, ycord, colour):
        super().__init__(xcord, ycord, colour)
        if self.colour:
            self.surface = pygame.image.load("wking.png")
        else:
            self.surface = pygame.image.load("bking.png")
        self.surface.convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (100,100))
        width, height = self.surface.get_size()
        self.rect = pygame.rect.Rect(((xcord-1)*100, (8-ycord)*100, width, height))
        
    def move(self, newx, newy): # move function
        xdif = abs(newx-self.xcord)
        ydif = abs(newy-self.ycord)
        if xdif <= 1 and ydif <= 1 and xdif + ydif != 0: # Makes sure king can't move more than one block out
            return True

def diagonal(self, newx, newy, players, stepx, stepy):
    if abs(newx - self.xcord) == abs(newy-self.ycord):
        for i in range(1, abs(newx-self.xcord)):
            for k in players:
                if k.xcord == self.xcord + i*stepx and k.ycord == self.ycord + i*stepy:
                    return
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
                                return
            return True

def getstep(self, newx, newy):
    if self.xcord <= newx:
        stepx = 1  
    else:
        stepx = -1
    if self.ycord <= newy:
        stepy = 1 
    else:
        stepy = -1
    return stepx, stepy


class queen(piece):
    def __init__(self, xcord, ycord, colour):
        super().__init__(xcord, ycord, colour)
        if self.colour:
            self.surface = pygame.image.load("wqueen.png")  
        else:
            self.surface = pygame.image.load("bqueen.png")
        self.surface.convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (100,100))
        width, height = self.surface.get_size()
        self.rect = pygame.rect.Rect(((xcord-1)*100, (8-ycord)*100, width, height))
    def move(self, newx, newy): 
        stepx, stepy = getstep(self, newx, newy)
        if straight(self, newx, newy, players, stepx, stepy):
            return True
        if diagonal(self, newx, newy, players, stepx, stepy):
            return True 
        
class bishop(piece):    
    def __init__(self, xcord, ycord, colour):
        super().__init__(xcord, ycord, colour)
        if self.colour:
            self.surface = pygame.image.load("wbishop.png")    
        else:
            self.surface = pygame.image.load("bbishop.png")
        self.surface.convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (100,100))
        width, height = self.surface.get_size()
        self.rect = pygame.rect.Rect(((xcord-1)*100, (8-ycord)*100, width, height))
    def move(self, newx, newy): 
        stepx, stepy = getstep(self, newx, newy)
        if diagonal(self, newx, newy, players, stepx, stepy):
            return True

class knight(piece):
    def __init__(self, xcord, ycord, colour):  
        super().__init__(xcord, ycord, colour)
        if self.colour:
            self.surface = pygame.image.load("wknight.png")
        else:
            self.surface = pygame.image.load("bknight.png")
        self.surface.convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (100,100))
        width, height = self.surface.get_size()
        self.rect = pygame.rect.Rect(((xcord-1)*100, (8-ycord)*100, width, height))
    def move(self, newx, newy): 
        xdif = abs(newx-self.xcord)
        ydif = abs(newy-self.ycord)
        if xdif != 0 and ydif != 0 and xdif + ydif == 3:
            return True

class rook(piece):
    def __init__(self, xcord, ycord, colour):
        super().__init__(xcord, ycord, colour)    
        if self.colour:
            self.surface = pygame.image.load("wrook.png")
        else:
            self.surface = pygame.image.load("brook.png")
        self.surface.convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (100,100))
        width, height = self.surface.get_size()
        self.rect = pygame.rect.Rect(((xcord-1)*100, (8-ycord)*100, width, height))
    def move(self, newx, newy): 
        stepx, stepy = getstep(self, newx, newy)
        if straight(self, newx, newy, players, stepx, stepy):
            return True

class pawn(piece):
    def __init__(self, xcord, ycord, colour): 
        super().__init__(xcord, ycord, colour)
        if self.colour:
            self.surface = pygame.image.load("wpawn.png")   
        else: 
            self.surface = pygame.image.load("bpawn.png")
        self.surface.convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (100,100))
        width, height = self.surface.get_size()
        self.rect = pygame.rect.Rect(((xcord-1)*100, (8-ycord)*100, width, height))
    def move(self, newx, newy): 
        if self.colour:
            if newx == self.xcord:
                if self.ycord == 2 and  0 < newy - self.ycord <= 2:
                    return True
                elif newy - self.ycord == 1:
                    return True
        elif newx == self.xcord:
            if self.ycord == 7 and  0 < self.ycord - newy <= 2:
                return True
            elif self.ycord - newy == 1:
                return True


gameinit()
screen, clock = gameinit()
players = [pawn(i, 2, True) for i in range(1,9)]
for i in range(1,9):
    players.append(pawn(i,7,False))
players.append(rook(1,1, True))
players.append(knight(2,1, True))
players.append(bishop(3,1, True))
players.append(queen(4,1, True))   
players.append(king(5,1, True))
players.append(rook(8,1, True))
players.append(knight(7,1, True))
players.append(bishop(6,1, True))

players.append(rook(1,8, False))
players.append(knight(2,8, False))
players.append(bishop(3,8, False))
players.append(queen(4,8, False))   
players.append(king(5,8, False))
players.append(rook(8,8, False))
players.append(knight(7,8, False))
players.append(bishop(6,8, False))

gamerun(players, screen, clock)
