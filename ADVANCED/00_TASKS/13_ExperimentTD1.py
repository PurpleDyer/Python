from tkinter import *
from random import randint

# ==========================================================================================================================================

board = None
Font_tuple = ("B Nazanin", 15, "bold")
root = Tk()
CELL_WIDTH = 5

# ==========================================================================================================================================

class Cell:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y 
        self.__content = []

    def __str__(self):
        return "-".join(map(str, self.__content))

    def give_content(self):
        return self.__content

    def add_content(self, element):
        self.__content.append(element)

    def remove_content(self, element):
        if element in self.__content:
            self.__content.remove(element)

    def has_type(self, typ):
        for element in self.__content:
            if isinstance(element, typ):
                return True
        return False

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

# ==========================================================================================================================================

class Board:
    def __init__(self, board_width, board_height):
        self.__board_width = board_width
        self.__board_height = board_height
        self.__board = [[Cell(x=x, y=y) for x in range(self.__board_width)] for y in range(self.__board_height)]

    def __str__(self):
        LINE = (((CELL_WIDTH + 1) * self.__board_width) + 1) * "-" + "\n"
        FINAL_BOARD = LINE
        for row in self.__board:
            FINAL_BOARD += "|" + "|".join(list(map(lambda x: str(x).center(CELL_WIDTH), row))) + "|\n" + LINE
        return FINAL_BOARD

    def get_cell(self, x, y):
        return self.__board[y][x]

    @property
    def width(self):
        return self.__board_width

    @property
    def height(self):
        return self.__board_height

    @property
    def board(self):
        return self.__board

# ==========================================================================================================================================

class Block:
    def __init__(self):
        self.__character = '-===-'

    def __str__(self):
        return self.__character

# ==========================================================================================================================================

def partial_function(text):
    def command():
        print(text)
    return command

# ==========================================================================================================================================

class Engine:
    def __init__(self, board_width, board_height, total_blocks):
        self.__board_width = board_width
        self.__board_height = board_height
        self.__total_blocks = total_blocks

    def run(self):
        global board
        board = Board(self.__board_width, self.__board_height)

        total_blocks_counter = 0
        while total_blocks_counter < self.__total_blocks:
            random_x = randint(0, self.__board_width-1)
            random_y = randint(0, self.__board_height-1)
            cell = board.get_cell(random_x, random_y)
            if not cell.has_type(Block):
                cell.add_content(Block())         
                total_blocks_counter += 1

        # print(board)

        for y, row in enumerate(board.board):
            for x, element in enumerate(row):
                cell = board.get_cell(x, y)
                if not cell.has_type(Block):
                    button = Button(root, text='O', command=partial_function('you pressed a button'), font=Font_tuple)
                    button.grid(row=y, column=x)

        root.mainloop()
        

# ==========================================================================================================================================

# for y, row in enumerate(board):
#     for x, element in enumerate(row):
#         if not element == ' ':
#             button = Button(root, text=element, command=partial_function(element), font=Font_tuple)
#             button.grid(row=y, column=x)

# ==========================================================================================================================================

# root.mainloop()
engine = Engine(15, 15, 140)
engine.run()

# results: COMPLETE
# P.O.D: not putting buttons on some places
# recommendation: MAKE AN ENEMY MOVE ON ITS OWN