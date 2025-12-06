import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 400))

rect(screen, (168, 255,255), (0, 0, 600, 200))
rect(screen, (0, 175, 45), (0, 200, 600, 200))

ellipse(screen,(152,141,242),(90,170, 60, 120))
ellipse(screen,(152,141,242),(450,170, 60, 120))
polygon(screen, (249, 66, 158), [(240,145), (200,290),(280,290)])
polygon(screen, (249, 66, 158), [(360,145), (320,290),(400,290)])
line(screen, (0,0,0),(105,180),(65,230))
line(screen, (0,0,0),(135,180),(175,230))
line(screen, (0,0,0),(228,178),(175,230))
line(screen, (0,0,0),(250,178),(280,203))
line(screen, (0,0,0),(280,203),(305,175))
line(screen, (0,0,0),(348,178),(318,203))
line(screen, (0,0,0),(318,203),(304,174))
line(screen, (0,0,0),(370,178),(415,230))
line(screen, (0,0,0),(465,180),(413,230))
line(screen, (0,0,0),(495,180),(540,230))
line(screen,(0,0,0), (230,290),(230,345))
line(screen,(0,0,0), (230,345),(223,345))
line(screen,(0,0,0), (250,290),(250,345))
line(screen,(0,0,0), (250,345),(260,345))
line(screen,(0,0,0), (350,290),(350,345))
line(screen,(0,0,0), (350,345),(343,345))
line(screen,(0,0,0), (370,290),(370,345))
line(screen,(0,0,0), (370,345),(380,345))
line(screen,(0,0,0),(110,285),(85,348))
line(screen,(0,0,0),(85,348),(73,349))
line(screen,(0,0,0),(130,285),(145,347))
line(screen,(0,0,0),(145,347),(155,348))
line(screen,(0,0,0),(470,285),(445,348))
line(screen,(0,0,0),(445,348),(433,349))
line(screen,(0,0,0),(490,285),(505,347))
line(screen,(0,0,0),(505,347),(515,348))
line(screen,(0,0,0),(66,232),(50,150))
polygon(screen, (255, 0, 0), [(50,150), (20,110),(70,96)])
circle(screen, (255, 0, 0), (31,100), 17)
circle(screen, (255,0, 0), (55,92), 17)
line(screen,(0,0,0),(305,175),(312,80))
polygon(screen, (255, 215, 0), [(538,231), (540,203),(560,215)])
circle(screen, (0, 0, 0), (545, 204), 6)
circle(screen, (255, 0, 0), (555, 210), 7)
circle(screen, (255, 255, 255), (554, 200), 7)
polygon(screen, (255, 215, 0), [(312,80), (295,40),(329,35)])
circle(screen, (0, 0, 0), (305, 35), 8)
circle(screen, (255, 0, 0), (319, 33), 9)
circle(screen, (255, 255, 255), (312, 20), 11)
circle(screen, (252, 218, 191), (120, 150), 25)
circle(screen, (252, 218, 191), (240, 150), 25)
circle(screen, (252, 218, 191), (360, 150), 25)
circle(screen, (252, 218, 191), (480, 150), 25)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True