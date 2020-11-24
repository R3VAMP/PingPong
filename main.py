import pygame
import sys

# general
pygame.init()
clock = pygame.time.Clock()

# main window
screen_width = 1024
screen_height = 576
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Ping Pong")
icon = pygame.image.load('imgs/ping-pong.png')
pygame.display.set_icon(icon)

# Game Shapes
ball = pygame.Rect(screen_width/2 - 10,screen_height/2 - 10,20,20)
player = pygame.Rect(screen_width -20,screen_height/2 - 35,10,70)
opponent = pygame.Rect(10,screen_height/2 - 35,10,70)

bg_color = pygame.Color('darkslateblue')
light_grey = (200,200,200)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0),(screen_width/2,screen_height))
    # Updating Window 
    pygame.display.flip()
    clock.tick(60)
