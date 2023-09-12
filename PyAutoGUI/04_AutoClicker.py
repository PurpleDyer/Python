import pyautogui as pg
from time import sleep
import threading

sleep(2)

def one():
    counter = 0
    while counter < 50:
        counter += 1
        mouseX, mouseY = pg.position()
        pg.click(x=mouseX, y=mouseY)

def two():
    sleep(0.0001)
    counter = 0
    while counter < 50:
        counter += 1
        mouseX, mouseY = pg.position()
        pg.click(x=mouseX, y=mouseY)

def three():
    sleep(0.0001)
    counter = 0
    while counter < 50:
        counter += 1
        mouseX, mouseY = pg.position()
        pg.click(x=mouseX, y=mouseY)

def four():
    sleep(0.0001)
    counter = 0
    while counter < 50:
        counter += 1
        mouseX, mouseY = pg.position()
        pg.click(x=mouseX, y=mouseY)

def five():
    sleep(0.0001)
    counter = 0
    while counter < 50:
        counter += 1
        mouseX, mouseY = pg.position()
        pg.click(x=mouseX, y=mouseY)

o_t = threading.Thread(target=one)
t_t = threading.Thread(target=two)
tt_t = threading.Thread(target=three)
f_t = threading.Thread(target=four)
ff_t = threading.Thread(target=five)

o_t.start()
t_t.start()
tt_t.start()
f_t.start()
ff_t.start()