import pygame
import sys
def gameinit():
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    screen.fill((255,255,255))
    for i in range(0,800, 100):
        pygame.draw.rect(screen, (0,0,0), (i,i,100,100), 1)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.quit()
                exit()


class piece:
    def __init__(self, xcord, ycord, colour):
        self.xcord = xcord
        self.ycord = ycord
        self.taken = False
        self.colour = "white"
class pawn(piece):
    def __init__(self, xcord, ycord, colour):    
        super().__init__(xcord, ycord, colour)
class king(piece):
    def __init__(self, xcord, ycord, colour):    
        super().__init__(xcord, ycord, colour)
class queen(piece):
    def __init__(self, xcord, ycord, colour):    
        super().__init__(xcord, ycord, colour)
class bishop(piece):
    def __init__(self, xcord, ycord, colour):    
        super().__init__(xcord, ycord, colour)
class knight(piece):
    def __init__(self, xcord, ycord, colour):    
        super().__init__(xcord, ycord, colour)
class rook(piece):
    def __init__(self, xcord, ycord, colour):    
        super().__init__(xcord, ycord, colour)

