import keyboard
from tkinter import *
import threading
from time import sleep 
import pyautogui as pg

# ==================================================================================================================

dead = False
root = Tk()

# ==================================================================================================================

def on_click():
    sleep(2)
    def one():
        global dead

        while not dead:
            mouseX, mouseY = pg.position()
            pg.click(x=mouseX, y=mouseY)

    def two():
        sleep(0.0001)
        global dead

        while not dead:
            mouseX, mouseY = pg.position()
            pg.click(x=mouseX, y=mouseY)

    def three():
        sleep(0.0001)
        global dead

        while not dead:
            mouseX, mouseY = pg.position()
            pg.click(x=mouseX, y=mouseY)

    def four():
        sleep(0.0001)
        global dead 

        while not dead:
            mouseX, mouseY = pg.position()  
            pg.click(x=mouseX, y=mouseY)

    def five():
        sleep(0.0001)
        global dead 

        while not dead: 
            mouseX, mouseY = pg.position()
            pg.click(x=mouseX, y=mouseY)

    def six():
        sleep(0.0001)
        global dead 

        while not dead: 
            mouseX, mouseY = pg.position()
            pg.click(x=mouseX, y=mouseY)

    def seven():
        sleep(0.0001)
        global dead 

        while not dead: 
            mouseX, mouseY = pg.position()
            pg.click(x=mouseX, y=mouseY)

    def eight():
        sleep(0.0001)
        global dead 

        while not dead: 
            mouseX, mouseY = pg.position()
            pg.click(x=mouseX, y=mouseY)
    
    def nine():
        sleep(0.0001)
        global dead 

        while not dead: 
            mouseX, mouseY = pg.position()
            pg.click(x=mouseX, y=mouseY)

    def ten():
        sleep(0.0001)
        global dead 

        while not dead: 
            mouseX, mouseY = pg.position()
            pg.click(x=mouseX, y=mouseY)

    def reader():
        global dead

        while not dead:
            key = keyboard.read_key()
            if key == 'alt':
                dead = True
                

    r_t = threading.Thread(target=reader)
    o_t = threading.Thread(target=one)
    t_t = threading.Thread(target=two)
    tt_t = threading.Thread(target=three)
    f_t = threading.Thread(target=four)
    ff_t = threading.Thread(target=five)
    s_t = threading.Thread(target=six)
    ss_t = threading.Thread(target=seven)
    e_t = threading.Thread(target=eight)
    n_t = threading.Thread(target=nine)
    ttt_t = threading.Thread(target=ten)

    r_t.start()
    o_t.start()
    t_t.start()
    tt_t.start()
    f_t.start()
    ff_t.start()
    s_t.start()
    s_t.start()
    e_t.start()
    n_t.start()
    ttt_t.start()

# ==================================================================================================================

button = Button(root, text="ON", width=20, height=10, command=on_click)
button.grid(row=0, column=0)

# ==================================================================================================================

root.mainloop()


# ! be careful while using this !