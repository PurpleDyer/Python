from random import randint
from tkinter import *

# =======================================================================================================================

CELL_WIDTH = 5
board = None

# =======================================================================================================================

class Cell:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__content = []
        self.__reveal = False

    def __str__(self):
        return "-".join(map(str, self.__content))

    def add_content(self, element):
        self.__content.append(element)

    def remove_content(self, element):
        if element in self.__content:
            self.__content.remove(element)

    def clear_cell(self):
        self.__content.clear()

    def has_type(self, typ):
        for element in self.__content:
            if isinstance(element, typ):
                return True
        return False

    def give_content(self):
        return self.__content

    def reveal_switch(self):
        if self.__reveal:
            self.__reveal = False
        else:
            self.__reveal = True

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

# =======================================================================================================================

class Board:
    def __init__(self, board_width, board_height):
        self.__board_width = board_width
        self.__board_height = board_height
        self.__board = [[Cell(x=x, y=y) for x in range(self.__board_width)] for y in range(self.__board_height)]

    def __str__(self):
        LINE = (((CELL_WIDTH + 1) * self.__board_width) + 1) * "-" + "\n"
        FINAL_BOARD = LINE
        for row in self.__board:
            FINAL_BOARD +=  "|" + "|".join(map(lambda x: str(x).center(CELL_WIDTH), row)) + "|\n" + LINE
        return FINAL_BOARD  

    def get_cell(self, x, y):
        return self.__board[y][x] 

    @property
    def width(self):
        return self.__board_width

    @property
    def height(self):
        return self.__board_height

# =======================================================================================================================

class Engine:
    def __init__(self, board_width, board_height):
        self.__board_width = board_width
        self.__board_height = board_height

    def run(self):
        global board

        root = Tk()
        
        board = Board(self.__board_width, self.__board_height)

        generated_list = []
        main_list = []
        counter = 0
        while counter < (self.__board_width*self.__board_height):
            random_num = randint(0, 10)
            if not random_num in generated_list:
                counter += 1
                main_list.append(random_num)
                generated_list.append(random_num)

        main_list.extend(main_list)
        shuffle(main_list)

        index = 0
        for y in range(self.__board_height):
            for x in range(self.__board_width):
                button = Button(root, padx=10, pady=10, text=main_list[index], command=print(main_list[index]))
                button.grid(row=y, column=x)

        root.mainloop()

# =======================================================================================================================

engine = Engine(10, 10)
engine.run()