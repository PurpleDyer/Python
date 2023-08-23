import time
from random import randint
import threading
import keyboard

# ==============================================================================================================

CELL_WIDTH = 5
board1 = None
board2 = None

# ==============================================================================================================

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
        else:
            return None
    
    def clear_cell(self):
        self.__content.clear()

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

# ==============================================================================================================

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

    @property
    def board(self):
        return self.__board

# ==============================================================================================================

class Block:
    def __init__(self):
        self.__character = '-===-'

    def __str__(self):
        return self.__character

# ==============================================================================================================

class Engine:
    def __init__(self, board_width, board_height, total_blocks):
        self.__board_width = board_width
        self.__board_height = board_height
        self.__total_blocks = total_blocks

    def run(self):
        global board1, board2
        board1 = Board(self.__board_width, self.__board_height)
        board2 = Board(self.__board_width, self.__board_height)

        total_blocks_counter = 0
        while total_blocks_counter < self.__total_blocks:
            random_x, random_y = randint(0, self.__board_width-1), randint(0, self.__board_height-1)
            cell = board1.get_cell(random_x, random_y)
            if not cell.has_type(Block):
                block = Block() 
                cell.add_content(block)
                total_blocks_counter += 1

        total_blocks_counter = 0
        while total_blocks_counter < self.__total_blocks:
            random_x, random_y = randint(0, self.__board_width-1), randint(0, self.__board_height-1)
            cell = board2.get_cell(random_x, random_y)
            if not cell.has_type(Block):
                block = Block() 
                cell.add_content(block)
                total_blocks_counter += 1

        printing_board = board1
        is_game_over = False
        key = None

        def printer():
            while True:
                print(printing_board)
                time.sleep(0.5)

        def changer():
            nonlocal printing_board 
            while True:
                nonlocal key
                key = keyboard.read_key()
                if key == 'space':
                    if key == 'space' and keyboard.is_pressed(key):
                        if printing_board == board1:
                            printing_board = board2
                        else:
                            printing_board = board1
                key = None
                    
        printer_thread = threading.Thread(target=printer)
        changer_thread = threading.Thread(target=changer)

        printer_thread.start()
        changer_thread.start()

# ==============================================================================================================

engine = Engine(5, 5, 5)
engine.run()

# this is also a practice for working with two boards at the same time
# this is a practice and a test for making a bigger project