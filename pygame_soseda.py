import pygame
from pygame.draw import *
from funct_picture import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 400))


background((168, 255,255),(0, 175, 45),screen)
woman(350,150,(255, 222, 173),True,screen)
man(235,150,(165, 42, 42),True,screen)
balloon_2(295,85,"icecream",screen)
woman(463,150,(221, 160, 221),False,screen)
man(122,150,(50, 66, 158),False,screen)
balloon_2(77,50,"heart",screen)
icecream(517,230,screen,(160,82,45))



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True