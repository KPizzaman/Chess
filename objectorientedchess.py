import pygame
import os
import math

# The piece class which holds the positions colour and state of every piece
turn = True # true means its white and false means its black
kingmovedw = False
kingmovedb = False
checkmate = False
coltoking = lambda x : players[8] if x is not True else players[28] # lambda function that finds the correct coloured king based on a pw
# Draws board
def chessboard(screen):
    screen.fill((255,255,255))
    for i in range(0,800, 200): 
        for j in range(0,800,100):
            pygame.draw.rect(screen, (209,139,71), (i+100*((j/100+1)%2),j,100,100), 0)


def playerdrag(player, event, screen, players):
    player.handle_click(event, players, screen)
    player.mousedrag(player.dragging)
    player.draw(screen)

# The parent class for all pieces
class piece(object):
    def __init__(self, xcord, ycord, colour): # has position, captured and colour
        self.xcord = xcord
        self.ycord = ycord
        self.taken = False
        self.colour = colour # true = white ; false = black Not a racist remark
        self.dragging = False # used for when dragging the drawn piece is being handled

    def mousedrag(self, dragging):
        if dragging:
            self.rect.left , self.rect.top = pygame.mouse.get_pos() # follows the mouse
            self.rect.left -= self.rect.width/2
            self.rect.top -= self.rect.height/2

    def handle_click(self, event, players, screen):
        global turn
        global kingmovedw
        global kingmovedb
        mousex, mousey = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(mousex, mousey ):
                if event.button == 1:     
                    self.dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(mousex, mousey ):
                if event.button == 1:
                    self.dragging = False
                    newx = round(self.rect.left/100+1)
                    newy = round(self.rect.top/(-100)+8)
                    boo = self.move(newx,newy)
                    if boo is True and self.colour is turn:
                        if premovechecks(self, newx, newy, players, screen):
                            self.rect.left = (self.xcord-1)*100
                            self.rect.top = (8-self.ycord)*100
                            return



                        self.xcord = round(newx)
                        self.ycord = round(newy)
                        self.rect.left = (self.xcord-1)*100
                        self.rect.top = (8-self.ycord)*100

                        if type(self) == king:
                            if self.colour:
                                kingmovedw = True
                            else:
                                kingmovedb = True 

                        turn = not turn
                        # will doing this move take our king out of check?

                        # Set board up to state if this move happens
                        global checkmate
                        checkmking = coltoking(not turn)
                        checkmatecount = 0
                        oldx, oldy = checkmking.xcord, checkmking.ycord
                        for j in range(-1,2):
                                for k in range(-1,2):
                                    if 0 < checkmking.xcord + j < 9 and 0 < checkmking.ycord + k < 9:
                                        for i in players:
                                            if i.xcord == checkmking.xcord + j and i.ycord == checkmking.ycord + k:
                                                if checkmking.colour is not i.colour:
                                                    capturedoldx, capturedoldy = i.xcord, i.ycord
                                                    i.xcord, i.ycord = 0, 0
                                                    temp = i
                                                elif i.colour == checkmking.colour:
                                                    checkmatecount += 1
                                    else:
                                        checkmatecount += 1
        

                                    for i in players:
                                        if i.move(checkmking.xcord + j , checkmking.ycord + k) and i.colour != checkmking.colour:
                                            try:
                                                checkmatecount += 1
                                                checkmking.xcord, checkmking.ycord = oldx, oldy
                                                temp.xcord, temp.ycord = capturedoldx, capturedoldy
                                            except:
                                                pass
                                                    

                                        # reset board to current state

                                        try:
                                            checkmking.xcord, checkmking.ycord = oldx, oldy
                                            temp.xcord, temp.ycord = capturedoldx, capturedoldy  
                                        except:
                                            pass

                        for i in players:
                            if i.move(checkmking.xcord, checkmking.ycord) and i.colour != checkmking.colour:
                                check = True
                                break
                            else:
                                check = False

                        if checkmatecount>= 9 and check == True:
                            checkmate = True
                            
                            
                    else: 
                        self.rect.left = (self.xcord-1)*100
                        self.rect.top = (8-self.ycord)*100
                    

    def draw(self, surface):
        if not self.taken:
            surface.blit(self.surface, (self.rect.left,self.rect.top))
        else:
            self.xcord, self.ycord = 0, 0
    
def gameinit():
    # Initialise pygame
    pygame.init()
    # creates the main screen with a dimension of 800x800
    screen = pygame.display.set_mode((800,800))
    # draws the chessboard pattern onto background
    chessboard(screen)
    # updates screen so the drawing appears on it
    pygame.display.update()
    # sets variable clock to the the tick speed of the game, allows for abstraction and cleaner code
    clock = pygame.time.Clock()
    pygame.draw
    # Loop that checks for any event in the game
    return screen, clock
def gamerun(players, screen, clock):
    global checkmate
    while True:
        for event in pygame.event.get():
            # Checks if window tries to be close
            if event.type == pygame.QUIT:
            # Closes the program altogether
                checkmate = True
                return
            chessboard(screen)

            for i in players:
                playerdrag(i, event, screen, players)
            clock.tick(75)
        if checkmate is True:
            button = pygame.image.load("tryagain.png")
            button = pygame.transform.scale(button, (500, 200))
            rect = pygame.rect.Rect((100, 100, 500, 200))
            screen.blit(button, (100, 100))
            pygame.display.update()
            clicked = False
            while clicked is False:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if rect.collidepoint(pygame.mouse.get_pos()) and event.button == 1:
                            checkmate = False
                            clicked = True
            break
        pygame.display.update()

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
        global kingmovedw
        global kingmovedb
        xdif = abs(newx-self.xcord)
        ydif = abs(newy-self.ycord)
        rightcastle = 0
        leftcastle = 0
        if (kingmovedw is False and self.colour is True) or (kingmovedb is False and self.colour is False):
            for i in players:
                if i.ycord == self.ycord:
                    if i.xcord == self.xcord + 1 or i.xcord == self.xcord + 2:
                        rightcastle += 1
                    if i.xcord == self.xcord + -1 or i.xcord == self.xcord -2 or i.xcord == self.xcord - 3:
                        leftcastle += 1
                if type(i) == rook and i.colour == self.colour:
                    if i.ycord == self.ycord:
                        if i.xcord == self.xcord + 3:
                            rightcastle -= 1
                            rightrook = i
                        if i.xcord == self.xcord - 4:
                            leftrook = i
                            leftcastle -= 1
            if ydif == 0:
                if newx - self.xcord == 2 and rightcastle == -1:
                    rightrook.xcord = 6
                    rightrook.rect.left = (rightrook.xcord-1)*100
                    rightrook.rect.top = (8-rightrook.ycord)*100
                    return True
                if self.xcord - newx == 2 and leftcastle == -1:
                    leftrook.xcord = 4
                    leftrook.rect.left = (leftrook.xcord-1)*100
                    leftrook.rect.top = (8-leftrook.ycord)*100
                    return True



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
                if i != newx:
                    if i != self.xcord:
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
    def checkpiece(self, players, newx, newy):
        global turn
        for i in players:
            if i.xcord == newx and i.ycord == newy:
                return 
            return True
    def move(self, newx, newy): 
        global turn
        if self.colour:
            if newx == self.xcord:
                if self.ycord == 2 and  0 < newy - self.ycord <= 2:
                    if self.checkpiece(players, newx, newy):
                        return True
                elif newy - self.ycord == 1:
                    if self.checkpiece(players, newx, newy):
                        return True
            if abs(newx-self.xcord) == 1 and newy - self.ycord == 1:
                for i in players:
                    if i.xcord == newx and i.ycord == newy:
                        return True
                
        else:
            if abs(newx-self.xcord) == 1 and  self.ycord - newy == 1:
                for i in players:
                    if i.xcord == newx and i.ycord == newy:
                        return True

            if newx == self.xcord:
                if self.ycord == 7 and  0 < self.ycord - newy <= 2:
                    if self.checkpiece(players, newx, newy):
                        return True    
                elif self.ycord - newy == 1:
                    if self.checkpiece(players, newx, newy):
                        return True

def premovechecks(self, newx, newy, players, screen):
    # will doing this move take our king out of check?

    # Set board up to state if this move happens
    oldx, oldy = self.xcord, self.ycord
    self.xcord, self.ycord = newx, newy
    for i in players:
        if i.xcord == newx and i.ycord == newy:
            if self.colour is not i.colour:
                capturedoldx, capturedoldy = i.xcord, i.ycord
                i.xcord, i.ycord = 0, 0
                temp = i

    for i in players:
        if i.move(coltoking(not self.colour).xcord, coltoking(not self.colour).ycord) and i.colour != coltoking(not self.colour).colour:
            try:
                self.xcord, self.ycord = oldx, oldy
                temp.xcord, temp.ycord = capturedoldx, capturedoldy
            except:
                pass
            return True
        else: movecheck = True
    # reset board to current state

    try:
        self.xcord, self.ycord = oldx, oldy
        temp.xcord, temp.ycord = capturedoldx, capturedoldy  
    except:
        pass
    
    
    # are we capturing a piece?
    for i in players:
        if i.xcord == newx and i.ycord == newy:
            if self.colour is not i.colour and self.taken is False:
                i.taken = True
            else:
                return True

    # is our king in check
    for i in players:
        if i.move(coltoking(not self.colour).xcord, coltoking(not self.colour).ycord) and i.colour != coltoking(not self.colour).colour and movecheck is False:
            return True

    # promotion
    if type(self) == pawn:
        if newy == 8 or newy  == 1:
            promqueen = queen(3, 5, self.colour)
            promrook = rook(4, 5, self.colour)
            prombishop = bishop(5, 5, self.colour)
            promknight = knight(6, 5, self.colour)
            chessboard(screen)
            for i in [prombishop, promknight, promqueen, promrook]:
                screen.blit(i.surface, (i.rect.left, i.rect.top))

            pygame.display.update()
            promotion = True
            while promotion:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        
                        for i in [prombishop, promknight, promqueen, promrook]:
                            if i.rect.collidepoint(pygame.mouse.get_pos()):
                                print()
                                players.append(type(i)(newx, newy, self.colour))
                                promotion = False
            players.remove(self)
    




while checkmate is False:
    turn = True # true means its white and false means its black
    kingmoved = 0
    checkmate = False
    gameinit()
    screen, clock = gameinit()
    players = [pawn(i, 2, True) for i in range(1,9)]
    players.append(king(5,1, True))
    for i in range(1,9):
        players.append(pawn(i,7,False))
    players.append(rook(1,1, True))
    players.append(knight(2,1, True))
    players.append(bishop(3,1, True))
    players.append(queen(4,1, True))   
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
    
