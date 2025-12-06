import math
from random import choice
from random import randint as rnd
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface,color, x = 40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.ay = 0.5
        self.color = color
        self.live = 30
        
        

    def move(self):
        self.x += self.vx
        self.y += self.vy
        
        if abs(self.vx) > 0.05:
            self.vx *= 0.99
        else:
            self.vx = 0
        

        if self.x - self.r <= 0: 
            self.vx = -self.vx * 0.5
            self.x = self.r  

        elif self.x + self.r >= WIDTH:
            self.vx = -self.vx * 0.5
            self.x = WIDTH - self.r  
        
        if self.y + self.r >= HEIGHT:
            self.y = HEIGHT - self.r  
            if abs(self.vy) < 2.0:  
                self.vy = 0
                self.ay = 0  
                self.vx = 0  
            else:
                self.vy = -self.vy * 0.7  
                self.vx *= 0.7
        else:

            self.vy += self.ay
        

        if self.y - self.r <= 0:
            self.vy = -self.vy * 0.5
            self.y = self.r
        

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        dx = self.x - obj.x
        dy = self.y - obj.y
        distance =math.sqrt(dx**2 + dy**2)
        if distance <= self.r + obj.r + 2:
            return True
        return False


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.new_target()

    def new_target(self):
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(4, 50)
        self.color = RED

    def hit(self, points=1):
        self.points += points

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            self.r
        )


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.ball_color = choice(GAME_COLORS)

    def fire2_start(self, event):
        self.f2_on = 1
        self.next_ball_color = choice(GAME_COLORS)

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.next_ball_color)
        new_ball.r += 5
        gun_x, gun_y = 20, 450
        self.an = math.atan2((event.pos[1]-gun_y), (event.pos[0]-gun_x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        new_ball.x = gun_x
        new_ball.y = gun_y
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        new_ball = Ball(self.screen, self.next_ball_color)
        self.color = GREY

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0]-20 == 0:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-19))
            else:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        '''if self.f2_on:
            self.color = RED
        else:
            self.color = GREY'''

    def draw(self):
        draw_color = self.next_ball_color if self.f2_on else GREY
        x_end = 20 + self.f2_power * math.cos(self.an)
        y_end = 450 + self.f2_power * math.sin(self.an)
        pygame.draw.line(self.screen,draw_color,(20, 450),(int(x_end), int(y_end)),7)
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color =  self.ball_color
        else:
            self.color = GREY





pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw(screen)
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
            target.live = 1
    gun.power_up()

pygame.quit()
