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