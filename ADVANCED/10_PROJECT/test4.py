import time
from tkinter import *
from random import randint, shuffle

# ================================================================================================================

root = Tk()
BACK_TEXT = '-'
numbers = [randint(0, 100) for _ in range(8)]
numbers.extend(numbers)
shuffle(numbers)

# ================================================================================================================

class Btn(Button):

    BUTTONS = []

    def __init__(self, content, master=None, cnf={}, **kwargs):
        self.__content = content
        self.__reveal = True
        super().__init__(master=master, cnf=cnf, **kwargs)
        Btn.BUTTONS.append(self)

    def show(self):
        if self.__reveal:
            self.__reveal = False
            self.config(text=self.__content)     
        else:
            self.__reveal = True
            self.config(text=BACK_TEXT)         

    @property
    def content(self):
        return self.__content

    @property
    def reveal(self):
        return self.__reveal

    @classmethod
    def give_buttons(cls):
        return cls.BUTTONS

# ================================================================================================================

def partial_function(text):
    
    def command():
        # button.show()
        print(text)

    return command

# ================================================================================================================

counter = 0
for x in range(4):
    for y in range(4):
        text = numbers[counter]
        button = Btn(master=root, content=text, text=text, width=10, height=5, command=partial_function(text))
        button.grid(row=y, column=x)
        counter += 1

# ================================================================================================================

root.mainloop()