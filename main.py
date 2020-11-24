import pygame

# general
pygame.init()
clock = pygame.time.Clock()

# main window
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Ping Pong")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Updating Window 
    pygame.display.flip()
    clock.tick(60)