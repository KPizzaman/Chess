import pygame
import os
import math

# The piece class which holds the positions colour and state of every piece
turn = True # true means its white and false means its black
check = False # is a king under check or not

coltoking = lambda x : players[8] if x is not True else players[28] # lambda function that finds the correct coloured king based on a p
taken = []
def chessboard(screen):
    screen.fill((255,255,255))
    for i in range(0,800, 200): 
        for j in range(0,800,100):
            pygame.draw.rect(screen, (209,139,71), (i+100*((j/100+1)%2),j,100,100), 0)

def playerdrag(player, event, screen, players):
    player.handle_click(event, players)
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

    def handle_click(self, event, players):
        global turn
        global check
        global taken

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
                    if boo:
                        oldx = self.xcord
                        oldy = self.ycord   
                        self.xcord = newx
                        self.ycord = newy
                        turn = not turn
                        for i in players:
                            if i.colour != coltoking(not self.colour).colour and i.xcord == coltoking(not self.colour).xcord and i.ycord == coltoking(not self.colour).ycord:
                                tem = i
                                taken.remove(i)
                                i.xcord, i.ycord = 0, 0
                                print(tem)
                        try:
                            print(tem) 
                        except: 
                            pass
                        for i in players:
                                if i.move(coltoking(not self.colour).xcord, coltoking(not self.colour).ycord):
                                    check = True
                                    try:
                                        taken.remove(coltoking(self.colour))
                                    except:
                                        pass
                                    break
                                else:
                                    check = False

                        try:
                            tem.xcord, tem.ycord = newx, newy
                        except:
                            pass

                        turn = not turn
                        self.xcord, self.ycord = oldx, oldy

                    if boo is True and check is False:
                        self.xcord = round(newx)
                        self.ycord = round(newy)
                        self.rect.left = (self.xcord-1)*100
                        self.rect.top = (8-self.ycord)*100
                        for i in players:
                            if i.move(coltoking(self.colour).xcord, coltoking(self.colour).ycord):
                                taken.remove(coltoking(self.colour))
                                check = True
                        turn = not turn
  
                    else: 
                        self.rect.left = (self.xcord-1)*100
                        self.rect.top = (8-self.ycord)*100
                        

    def draw(self, surface):
        for i in players:
            if i in taken:
                i.xcord, i.ycord = 0, 0
        surface.blit(self.surface, (self.rect.left,self.rect.top))

    
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
    while True:
        for event in pygame.event.get():
            # Checks if window tries to be close
            if event.type == pygame.QUIT:
            # Closes the program altogether
                return
            chessboard(screen)
            for i in players:
                playerdrag(i, event, screen, players)
            pygame.display.update()
            clock.tick(75)

def capture(self, players, newx, newy):
    global taken
    global turn
    if self.colour is turn:   
        for i in players:
            x = i.xcord
            y = i.ycord
            if x == newx and y == newy:
                if i.colour != self.colour:
                    i.taken = False
                    taken.append(i)
                    return True
                else:
                    return  
        return True
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
           if capture(self, players, newx, newy):
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
            if capture(self, players, newx, newy):
               return True
        if diagonal(self, newx, newy, players, stepx, stepy):
            if capture(self, players, newx, newy):
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
            if capture(self, players, newx, newy):
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
            if capture(self, players, newx, newy):
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
            if capture(self, players, newx, newy):
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
            if self.colour is turn:
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
                    if capture(self, players, newx, newy):
                        return True
                
        else:
            if abs(newx-self.xcord) == 1 and  self.ycord - newy == 1:
                for i in players:
                    if capture(self, players, newx, newy):
                        return True

            if newx == self.xcord:
                if self.ycord == 7 and  0 < self.ycord - newy <= 2:
                    if self.checkpiece(players, newx, newy):
                        return True    
                elif self.ycord - newy == 1:
                    if self.checkpiece(players, newx, newy):
                        return True







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
