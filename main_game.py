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
fontsmall = pygame.font.SysFont("arialblack", 15)
TEXT_COL = (255, 255, 255)
def draw_text(text, font, text_col, x, y):
    image = font.render(text, True, text_col)
    screen.blit(image, (x,y))

# load images into memory before game loop
# name_image = pygame.image.load('images/namefile.type')
bg_image = pygame.image.load('images/Space Background Cropped.png')
title_image = pygame.transform.scale(pygame.image.load('images/title.png'), (625,60))
base_image = pygame.transform.scale(pygame.image.load('images/base.png'), (1250,220))
ground_image = pygame.image.load('images/ground.png')

# game needs a loop to run in
run = True
title_screen = True
instruction_screen = False
while run:
    
    # constantly display images for visuals
    screen.blit(bg_image, (0,0))
    if title_screen:
        # displays title screen
        title_rect = title_image.get_rect(center=(screen_width/2, screen_height/2))
        screen.blit(title_image, title_rect)
        start_text = font.render("Press SPACE to start", True, TEXT_COL)
        start_rect = start_text.get_rect(center=(screen_width/2, screen_height/2+75))
        screen.blit(start_text, start_rect)
    if title_screen == False:
        # set up for game visuals
        screen.blit(ground_image, (0, 600))
        screen.blit(base_image, (0,395))
    if instruction_screen:
        # displays game controls
        instructions = ["Mission: Protect the Moon Base AT ALL COSTS","Use A to move left",
        "Use D to move right","Use W to lauch rockets","Press SPACE to begin"]
        # i and j are offsets to list instructions
        i = -75
        j = -25
        for string in instructions:
            text = font.render(string, True, TEXT_COL)
            text_rect = text.get_rect(center=(screen_width/2, screen_height/2+i+j))
            screen.blit(text, text_rect)
            i+=25
            j=0

    for event in pygame.event.get():
        # first event is to close game for completenes
        if event.type == pygame.QUIT:
            run = False
        #keydown means a key has been pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if title_screen:
                    title_screen = False
                    instruction_screen = True
                else:
                    instruction_screen = False


    pygame.display.update()

pygame.quit()