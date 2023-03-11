import pygame
from pygame.locals import *
import os
from random import randint
from nclass import *

fb = fbclass()

mylist = [(50,300),(100,350),(150,400),(200,450)]

#x1 = 1000
#x2 = 1000
#x3 = 1000
#x4 = 1000

highScore = 0
sessionScore = 0


X1 = 400
X2 = 600
X3 = 800
X4 = 1000

n = randint(0,3)
y1,Y1 = mylist[n]
#print(y1,Y1)


n = randint(0,3)
y2,Y2 = mylist[n]
#print(y2,Y2)


n = randint(0,3)
y3,Y3 = mylist[n]
#print(y3,Y3)


n = randint(0,3)
y4,Y4 = mylist[n]
#print(y4,Y4)



pygame.init()

screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("fb")

birdy = pygame.image.load("birdy.png").convert_alpha()

#clock = pygame.time.Clock()
#time_passed = clock.tick(5)


#extra here
                          
# game starts here
pygame.mouse.set_visible(False)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            os._exit(0)



    #capturing mouse click
    if pygame.mouse.get_pressed() == (1,0,0):
        fb.fly()
        
    #frame rate lock
    clock = pygame.time.Clock()
    time_passed = clock.tick(30)
    
    # filling the screen
    screen.fill((255,255,255))



    # drawing lines


    x1 = X1 
    x2 = X2 
    x3 = X3 
    x4 = X4 
    

    pygame.draw.line(screen, (255, 0, 0), (x1,0),(x1,y1))
    pygame.draw.line(screen, (255, 0, 0), (x1,Y1),(x1,600))

    pygame.draw.line(screen, (255, 0, 0), (x2,0),(x2,y2))
    pygame.draw.line(screen, (255, 0, 0), (x2,Y2),(x2,600))


    pygame.draw.line(screen, (255, 0, 0), (x3,0),(x3,y3))
    pygame.draw.line(screen, (255, 0, 0), (x3,Y3),(x3,600))

    pygame.draw.line(screen, (255, 0, 0), (x4,0),(x4,y4))
    pygame.draw.line(screen, (255, 0, 0), (x4,Y4),(x4,600))

    X1 -= 5
    X2 -= 5
    X3 -= 5
    X4 -= 5



    if X1 <= 3:
        X1 = 800
        if fb.alive:
            #print("Made alive")
            sessionScore += 1
        fb.revive()
        
    if X2 <=3:
        X2 = 800
        if fb.alive:
            #print("Made alive")
            sessionScore += 1
        fb.revive()
        

    if X3 <=3:
        X3 = 800
        if fb.alive:
            #print("Made alive")
            sessionScore += 1
        fb.revive()
        

    if X4 <=3:
        X4 = 800
        if fb.alive:
            #print("Made alive")
            sessionScore += 1
        fb.revive()
        #sessionScore +=1


        
    #setting sessioin score
    #if sessionScore == 1  :
     #   sessionScore = 0

    # getting the new position for bird and blitting it
    newpos = fb.get_pos()
    screen.blit(birdy,newpos)


    #Displaying Score and Death
    my_font = pygame.font.SysFont("arial", 16)
    screen.blit(my_font.render("Session Score: " + str(sessionScore) , True, (255,0,0),(255,255,255)),(600,0))
    screen.blit(my_font.render("High Score: " + str(highScore) , True , (255,0,0),(255,255,255)),(600,17))
    my_font = pygame.font.SysFont("arial", 26)
    screen.blit(my_font.render("Click inside" , True, (255,0,0),(255,255,255)),(380,574))



    


    if X1 < 100 and X1 > 5 :
        if fb.DieDie(y1,Y1):
            #print("DieDie1")
            if highScore <= sessionScore:
                highScore = sessionScore
            sessionScore = 0
            #time_passed = clock.tick(3)
            screen.blit(my_font.render("Death" , True , (255,0,0),(255,255,255)),(350,192))
            #continue

        

    if X2 < 100 and X2 > 5 :
        if fb.DieDie(y2,Y2):
            #print("DieDie2")
            if highScore <= sessionScore:
                highScore = sessionScore
            sessionScore = 0
        #time_passed = clock.tick(3)    
            screen.blit(my_font.render("Death" , True , (255,0,0),(255,255,255)),(350,192))
        #continue

    if X3 < 100 and X3 > 5 :
        if fb.DieDie(y3,Y3):
            #print("DieDie3")
            if highScore <= sessionScore:
                highScore = sessionScore
            sessionScore = 0
        #time_passed = clock.tick(3)
            screen.blit(my_font.render("Death" , True , (255,0,0),(255,255,255)),(350,192))
        #continue

    
    if X4 < 100 and X4 > 5 :
        if fb.DieDie(y4,Y4):
            #print("DieDie4")
            if highScore <= sessionScore:
                highScore = sessionScore
            sessionScore = 0
        #time_passed = clock.tick(3)
            screen.blit(my_font.render("Death" , True , (255,0,0),(255,255,255)),(350,192))
        #continue

#updating display
    pygame.display.update()



