import pyautogui as pg
from random import randint

width, height = pg.resolution()
pg.FAILSAFE = False

counter = 0

while counter < 50:
    random_x, random_y = randint(0, width), randint(0, height)
    pg.moveTo(x=random_x, y=random_y)
    counter += 1