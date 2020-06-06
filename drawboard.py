import pygame
import sys
import math
import os

def chessboard(screen):
    screen.fill((255,255,255))
    for i in range(0,800, 200):
        for j in range(0,800,100):
            pygame.draw.rect(screen, (0,0,0), (i+100*((j/100+1)%2),j,100,100), 0)

def playerdrag(player, event, screen):
    player.handle_click(event)
    player.mousedrag(player.dragging)
    player.draw(screen)

class piece(object):
    def __init__(self, x, y):
        self.surface = pygame.image.load(os.path.join("Desktop\SDD\Chess", "pawn.png"))
        self.surface.convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (100,100))
        width, height = self.surface.get_size()
        self.rect = pygame.rect.Rect((x, y, width, height))
        self.dragging = False


    def handle_click(self, event):
        mousex, mousey = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(mousex, mousey ):
                print("cock")
                if event.button == 1:     
                    self.dragging = True
        if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.dragging = False

    def mousedrag(self, dragging):
        if dragging:
            self.rect.left , self.rect.top = pygame.mouse.get_pos()
            self.rect.left -= self.rect.width/2
            self.rect.top -= self.rect.height/2


    def draw(self, surface):
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
    player = piece(10,10)
    playeer = piece(700,700)
    while True:
        for event in pygame.event.get():
            # Checks if window tries to be close
            if event.type == pygame.QUIT:
            # Closes the program altogether
                return
            if event.type == pygame.MOUSEMOTION:
                print(pygame.mouse.get_pos())
            
            chessboard(screen)
            playerdrag(player, event, screen)
            playerdrag(playeer, event, screen)
            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__": gameinit()
