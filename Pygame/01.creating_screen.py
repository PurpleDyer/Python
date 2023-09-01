# importing pygame
import pygame

# initializing pygame
pygame.init()

# setting the width and the height for the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# displaying the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# using a while loop the show the screen forever
run = True
while run:

    # event handler
    for event in pygame.event.get():
        # if quit button is pressed
        if event.type == pygame.QUIT:
            run = False

    # updating the screen 
    pygame.display.update()

# exiting pygame
pygame.quit()