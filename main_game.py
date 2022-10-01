# need to install pygame package in cmd
# pip install PyGame
import pygame
from pygame.locals import *
import world

pygame.init()

screen_width = 1250
screen_height = 625

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Survivor')

font = pygame.font.SysFont("arialblack", 30)
TEXT_COL = (255, 255, 255)
def draw_text(text, font, text_col, x, y):
    image = font.render(text, True, text_col)
    screen.blit(image, (x,y))

# load images into memory before game loop
# name_image = pygame.image.load('images/namefile.type')
bg_image = pygame.image.load('images/Space Background Cropped.png')
title_image = pygame.transform.scale(pygame.image.load('images/title.png'), (625,60))


# game needs a loop to run in
run = True
title_screen = True
while run:
    
    # constantly display images for visuals
    screen.blit(bg_image, (0,0))
    if title_screen:
        screen.blit(title_image, (310,250))
        draw_text("Press SPACE to start", font, TEXT_COL, 450, 350)
    

    for event in pygame.event.get():
        # first event is to close game for completenes
        if event.type == pygame.QUIT:
            run = False
        #keydown means a key has been pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                title_screen = False


    pygame.display.update()

pygame.quit()