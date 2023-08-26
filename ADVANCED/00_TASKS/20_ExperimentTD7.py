from tkinter import *
import time
import threading

# ===========================================================================

board = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O']
]
root = Tk()
Font_style = ("B Nazanin", 20, 'bold')

# ===========================================================================

def throw(x, y, master, text):
    label = Label(master=master, text=text, width=10, height=5, background="green", font=Font_style)
    label.grid(column=x, row=y)
    return label

# ===========================================================================

main_board = [[throw(x=x, y=y, master=root, text=element) for x, element in enumerate(row)] for y, row in enumerate(board)]

# ===========================================================================

class Enemy:
    def __init__(self, x, y):
        global main_board

        self.__x = x
        self.__y = y

        main_board[self.__y][self.__x].configure(text=self)

    def __str__(self):
        return 'E'

    def move(self):
        global main_board

        if 0 <= self.__x+1 < len(main_board[0]):
            while 0 <= self.__x+1 < len(main_board[0]):
                time.sleep(1)
                main_board[self.__y][self.__x].configure(text=' ')
                self.__x += 1
                main_board[self.__y][self.__x].configure(text=self)
        
        if 0 <= self.__y+1 < len(main_board):
            while 0 <= self.__y+1 < len(main_board):
                time.sleep(1)
                main_board[self.__y][self.__x].configure(text=' ')
                self.__y += 1
                main_board[self.__y][self.__x].configure(text=self)

        if 0 <= self.__y-1 < len(main_board):
            while 0 <= self.__y-1 < len(main_board):
                time.sleep(1)
                main_board[self.__y][self.__x].configure(text=' ')
                self.__y -= 1
                main_board[self.__y][self.__x].configure(text=self)

# ===========================================================================

enemy = Enemy(0, 4)

def mover():
    global enemy   # !

    while True:
        time.sleep(1)
        enemy.move()

mover_thread = threading.Thread(target=mover)

mover_thread.start()
root.mainloop()