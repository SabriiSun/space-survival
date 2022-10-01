# need to install pygame package in cmd
# pip install PyGame
import pygame
from pygame.locals import *

pygame.init()

screen_width = 1400
screen_height = 750

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Survivor')

# load images into memory before game loop
# name_image = pygame.image.load('images/namefile.type')
bg_image = pygame.image.load('images/Space Background.png')



# game needs a loop to run in
run = True
while run:
    
    # constantly display images for visuals
    screen.blit(bg_image, (0,0))

    for event in pygame.event.get():
        # first event is to close game for completenes
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()