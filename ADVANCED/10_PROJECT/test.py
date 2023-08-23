from random import randint, shuffle
from tkinter import *

generated_list = []
lis = []
counter = 0
width = 2
height = 2
while counter < (width*height):
    random_num = randint(0, 10)
    if not random_num in generated_list:
        counter += 1
        lis.append(random_num)
        generated_list.append(random_num)
    
lis.extend(lis)
shuffle(lis)

root = Tk()

frame = Frame(root)

index = 0

class Btn:
    def __init__(self, button):
        self.__button = button

    def change(self):
        if self.__button.cget('text') == '':
            self.__button.config(text='hi')
        else:
            self.__button.config(text='')

for y in range(height):
    for x in range(width):
        button = Button(root, padx=10, pady=10)
        button2 = Btn(button)
        button.config(command=lambda: button2.change())
        button.grid(row=y, column=x)

root.mainloop()