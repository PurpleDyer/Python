from keyboard import read_key
from tkinter import Tk, Button, mainloop
from threading import Thread
from time import sleep 
from pyautogui import click, position

# ==================================================================================================================

dead = False
root = Tk()

# ==================================================================================================================

def on_click():
    sleep(0.5)
    def one():
        global dead

        while not dead:
            mouseX, mouseY = position()
            click(x=mouseX, y=mouseY)

    def two():
        sleep(0.0001)
        global dead

        while not dead:
            mouseX, mouseY = position()
            click(x=mouseX, y=mouseY)

    def three():
        sleep(0.0001)
        global dead

        while not dead:
            mouseX, mouseY = position()
            click(x=mouseX, y=mouseY)

    def four():
        sleep(0.0001)
        global dead 

        while not dead:
            mouseX, mouseY = position()  
            click(x=mouseX, y=mouseY)

    def five():
        sleep(0.0001)
        global dead 

        while not dead: 
            mouseX, mouseY = position()
            click(x=mouseX, y=mouseY)

    def six():
        sleep(0.0001)
        global dead 

        while not dead: 
            mouseX, mouseY = position()
            click(x=mouseX, y=mouseY)

    def seven():
        sleep(0.0001)
        global dead 

        while not dead: 
            mouseX, mouseY = position()
            click(x=mouseX, y=mouseY)

    def eight():
        sleep(0.0001)
        global dead 

        while not dead: 
            mouseX, mouseY = position()
            click(x=mouseX, y=mouseY)
    
    def nine():
        sleep(0.0001)
        global dead 

        while not dead: 
            mouseX, mouseY = position()
            click(x=mouseX, y=mouseY)

    def ten():
        sleep(0.0001)
        global dead 

        while not dead: 
            mouseX, mouseY = position()
            click(x=mouseX, y=mouseY)

    def reader():
        global dead

        while not dead:
            key = read_key()
            if key == 'alt':
                dead = True
        sleep(1)
        dead = False
                
     

    r_t = Thread(target=reader)
    o_t = Thread(target=one)
    t_t = Thread(target=two)
    tt_t = Thread(target=three)
    f_t = Thread(target=four)
    ff_t = Thread(target=five)
    s_t = Thread(target=six)
    ss_t = Thread(target=seven)
    e_t = Thread(target=eight)
    n_t = Thread(target=nine)
    ttt_t = Thread(target=ten)

    r_t.start()
    o_t.start()
    t_t.start()
    tt_t.start()
    f_t.start()
    ff_t.start()
    s_t.start()
    ss_t.start()
    e_t.start()
    n_t.start()
    ttt_t.start()

# ==================================================================================================================

button = Button(root, text="ON", width=20, height=10, command=on_click)
button.grid(row=0, column=0)

# ==================================================================================================================

root.mainloop()


# ! be careful while using this !