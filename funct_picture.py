import pygame
from pygame.draw import *

def woman(x, y,color,wave,screen):
    #default x=360, y = 150!!
    polygon(screen, color, [(x, y - 5), (x - 40, y + 140), (x + 40, y + 140) ])
    circle(screen, (252, 218, 191), (x, y), 25)
    
    # hands
    if wave==True:
        line(screen, (0,0,0), (x - 12, y + 28), (x - 42, y + 53))
        line(screen, (0,0,0), (x - 42, y + 53), (x - 56, y + 24))
    else:
        line(screen, (0,0,0), (x - 12, y + 28), (x - 60, y + 75))
    line(screen, (0,0,0), (x + 10, y + 28), (x + 55, y + 80))

    #legs
    line(screen, (0,0,0), (x - 10, y + 140), (x - 10, y + 195))
    line(screen, (0,0,0), (x - 10, y + 195), (x - 17, y + 195))
    line(screen, (0,0,0), (x + 10, y + 140), (x + 10, y + 195))
    line(screen, (0,0,0), (x + 10, y + 195), (x + 20, y + 195))

def man(x, y,color,wave,screen):
    #default x=360, y = 150!!
    ellipse(screen,color,(x - 30, y + 23, 60, 120))
    circle(screen, (252, 218, 191), (x, y), 25)
    
    # hands
    if wave==True:
        line(screen, (0,0,0), (x + 10, y + 28), (x + 45, y + 60))
        line(screen, (0,0,0), (x + 45, y + 60), (x + 65, y + 40))
    else:
        line(screen, (0,0,0), (x + 10, y + 28), (x + 55, y + 80))
    
    line(screen, (0,0,0), (x - 12, y + 28), (x - 60, y + 75))

    #legs
    line(screen, (0,0,0), (x - 10, y + 140), (x - 10, y + 195))
    line(screen, (0,0,0), (x - 10, y + 195), (x - 17, y + 195))
    line(screen, (0,0,0), (x + 10, y + 140), (x + 10, y + 195))
    line(screen, (0,0,0), (x + 10, y + 195), (x + 20, y + 195))


    
def background(sky_color,earth_color,screen):
    rect(screen, sky_color, (0, 0, 600, 200))
    rect(screen, earth_color, (0, 200, 600, 200))


def balloon_2(x,y,form,screen):
    if form == "heart":
        line(screen, (0,0,0), (x-16, y+177), (x -16, y + 82))
        polygon(screen, (255, 0, 0), [(x - 16, y + 82),  (x - 46, y + 42), (x + 4, y + 28)])
        circle(screen, (255, 0, 0), (x - 35, y + 32), 17) 
        circle(screen, (255, 0, 0), (x - 11, y + 24), 17) 
        
    if form == "icecream":
        line(screen, (0,0,0), (x , y + 95), (x, y))
        polygon(screen, (255, 215, 0), [(x, y), (x - 17, y - 40),(x + 17, y - 45)  ])
        circle(screen, (0, 0, 0), (x - 7, y - 45), 8)   
        circle(screen, (255, 0, 0), (x + 7, y - 47), 9) 
        circle(screen, (255, 255, 255), (x, y - 60), 11) 
def icecream(x,y,screen,color):
    polygon(screen, (255, 215, 0), [(x, y), (x - 17, y - 40),(x + 17, y - 45)  ])
    circle(screen, color, (x - 7, y - 45), 8)   
    circle(screen, color, (x + 7, y - 47), 9) 
    circle(screen, color, (x, y - 60), 11) 