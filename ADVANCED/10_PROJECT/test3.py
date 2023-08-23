import time
from tkinter import *

# ================================================================================================================

root = Tk()
BACK_TEXT = '-'
Font_tuple = ("B Nazanin", 10, "bold") 

# ================================================================================================================

class Btn(Button):
    def __init__(self, master=None, cnf={}, **kwargs):
        self.__content = content
        self.__reveal = False
        super().__init__(master, cnf, **kwargs)

    def front_back(self):
        print("ITS ME")
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

# ================================================================================================================
        
button = Btn(master=root, content="TEXT", text="TEXT", width=10, height=5, command=lambda: button.front_back())
button.grid(row=0, column=0)

# ================================================================================================================

root.mainloop()

# RESULT: SUCCESSFUL TEST
# UNDERSTANDING: REVEALING AND HIDING THE CONTENT OF THE BUTTON