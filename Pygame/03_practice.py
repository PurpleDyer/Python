# importing pygame
import pygame as pg 

# initilizing pygame
pg.init()

# making the screen
screen = pg.display.set_mode((1280, 720))

# making the clock for the game (fps)
clock = pg.time.Clock()

# the game
running = True
while running:
    # event handler
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # filling the screen and removing all the previous stuff
    screen.fill("black")

    # updating the screen
    pg.display.flip()

    # fps set
    clock.tick(60)