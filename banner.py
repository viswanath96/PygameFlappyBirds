import pygame
from pygame.locals import *
import os
from random import randint

pygame.init()

screen = pygame.display.set_mode((800,600),0,32)


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            os._exit(0)

    clock = pygame.time.Clock()
    time_passed = clock.tick(10)

    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    screen.fill((255,255,255))

    myFont = pygame.font.SysFont("mistral", 66)
    
    screen.blit(myFont.render("Banner",True,(r,g,b),(255,255,255)),(360,260))
    pygame.display.update()

    

