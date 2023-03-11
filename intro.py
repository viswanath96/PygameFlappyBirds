import pygame
from pygame.locals import *
import os
from random import randint

pygame.init()

screen = pygame.display.set_mode((800,600),0,32)
c = 255
current = False
pos = (0,0)

while not current:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            os._exit(0)

    pos = pygame.mouse.get_pos()

    x,y = pos

    c = ((400-x)*(400-x) + (300-y)*(300-y))**0.5
    if c > 255:
        c = 255

    if pygame.mouse.get_pressed() == (1,0,0):
        pos = pygame.mouse.get_pos()
        x,y = pos
        if x > 365 and x < 435:
            if y > 290 and y < 310:
                # replace this
                print("executed")
                os._exit(0)

    myfont = pygame.font.SysFont("arial", 16)
    CHsurface = myfont.render("Click Here",True,(0,0,255),(255,c,255))
    #print CHsurface.get_height()
    #print CHsurface.get_width()
    screen.fill((255,c,255))
    screen.blit(CHsurface,(365,290))
    #pygame.draw.rect(screen, (255,0,0), (390, 293,20, 15))
    pygame.display.update()
