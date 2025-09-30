import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
font = pygame.font.Font(None, 72)

def new_ball():
    #параметры нового шарика
    x = randint(100, 1100)
    y = randint(100, 800)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    dx = randint(-8, 8)
    dy = randint(-8, 8)
    while dx == 0 and dy == 0: #чтобы скорость не была 0
        dx = randint(-5, 5)
        dy = randint(-5, 5)
    return [color, x, y, r, dx, dy]

def draw_ball(b):
    color, x, y, r, dx, dy = b
    circle(screen, color, (x, y), r)

def is_clicked(b, pos):
    #проверка на нажатие
    color, x, y, r, dx, dy = b
    return (x - pos[0])**2 + (y - pos[1])**2 <= r**2

def move_ball(b):
    #изменение позиции шарика
    b[1] += b[4]  
    b[2] += b[5]  
    
    #отскок от границ
    if b[1] - b[3] <= 0 or b[1] + b[3] >= 1200:
        b[4] = -b[4]
    if b[2] - b[3] <= 0 or b[2] + b[3] >= 900:
        b[5] = -b[5]

pygame.display.update()
clock = pygame.time.Clock()
finished = False

#создание шариков
balls = [new_ball() for _ in range(5)]
points = 0
time = 0
while not finished:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #проверка нажатия
            b=0
            for ball in balls[:]:
                if is_clicked(ball, event.pos):
                    b=1
                    balls.remove(ball)
                    balls.append(new_ball())
                    if ball[3] < 30:
                        if ball[4]<-6 or ball[4]>6 or ball[5]<-6 or ball[5]>6:
                            points+=4
                        else:
                            points+=3
                    else:
                        if ball[4]<-6 or ball[4]>6 or ball[5]<-6 or ball[5]>6:
                            points+=2
                        else:
                            points+=1
            if b==0:
                points-=2
            else:
                b=0
    time+=1
    if time==50:
        time=0
        points-=1
                    
    
    #движение
    for ball in balls:
        move_ball(ball)

    screen.fill(BLACK)
    if points<0:
        text_surface = font.render(str(points), True, 'RED')
    else:
        text_surface = font.render(str(points), True, 'WHITE')
    screen.blit(text_surface, (20, 850))

    for ball in balls:
        draw_ball(ball)


    pygame.display.update()

pygame.quit()