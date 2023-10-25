import keyboard
from time import sleep
import threading
from random import randint

# =================================================================================================

CELL_WIDTH = 5
board = None
keys = ['up', 'down', 'right', 'left']

# =================================================================================================

class Cell:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__content = []

    def __str__(self):
        return "".join(map(str, self.__content))

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

    @property
    def content(self):
        return self.__content

# =================================================================================================

class Board:
    def __init__(self, board_width, board_height):
        self.__board_width = board_width
        self.__board_height = board_height
        self.__board = [[Cell(x=x, y=y) for x in range(self.__board_width)] for y in range(self.__board_height)]

    def __str__(self):
        LINE = ((CELL_WIDTH * self.__board_width) + 2) * "-" + "\n"
        FINAL_BOARD = LINE
        for row in self.__board:
            FINAL_BOARD +=  "|" + "".join(map(lambda x: str(x).center(CELL_WIDTH), row)) + "|\n"
        FINAL_BOARD += LINE
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

# =================================================================================================

class Block:
    def __str__(self):
        return "-===-"

# =================================================================================================

class Character:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "0"

    def move(self, direction):
        global board
        if keyboard.is_pressed(direction):
            if (direction == "right") and (0 <= self.__x+1 < board.width) and (not board.get_cell(self.__x+1, self.__y).has_type(Block)):
                board.get_cell(self.__x, self.__y).remove_content(self)
                self.__x += 1
                board.get_cell(self.__x, self.__y).add_content(self)

            elif (direction == "left") and (0 <= self.__x-1 < board.width) and (not board.get_cell(self.__x-1, self.__y).has_type(Block)):
                board.get_cell(self.__x, self.__y).remove_content(self)
                self.__x -= 1
                board.get_cell(self.__x, self.__y).add_content(self)

            elif (direction == "up") and (0 <= self.__y-1 < board.height) and (not board.get_cell(self.__x, self.__y-1).has_type(Block)):
                board.get_cell(self.__x, self.__y).remove_content(self)
                self.__y -= 1
                board.get_cell(self.__x, self.__y).add_content(self)

            elif (direction == "down") and (0 <= self.__y+1 < board.height) and (not board.get_cell(self.__x, self.__y+1).has_type(Block)):
                board.get_cell(self.__x, self.__y).remove_content(self)
                self.__y += 1
                board.get_cell(self.__x, self.__y).add_content(self)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

# =================================================================================================

class Engine:
    def __init__(self, board_width, board_height, total_blocks):
        self.__board_width = board_width
        self.__board_height = board_height
        self.__total_blocks = total_blocks

    def run(self):
        global board
        board = Board(self.__board_width, self.__board_height)
        character = Character(0, 0)
        board.get_cell(character.x, character.y).add_content(character)

        total_blocks_counter = 0
        while total_blocks_counter < self.__total_blocks:
            random_x, random_y = randint(0, self.__board_width-1), randint(0, self.__board_height-1)
            cell = board.get_cell(random_x, random_y)
            if (not cell.has_type(Block)) and (not cell.has_type(Character)):
                cell.add_content(Block())
                total_blocks_counter += 1

        def printer():
            while True:
                print(board)
                sleep(0.004876)

        def reader():
            while True:
                key = keyboard.read_key()
                if key in keys:
                    character.move(key)

        printer_thread = threading.Thread(target=printer)
        reader_thread = threading.Thread(target=reader)

        printer_thread.start()
        reader_thread.start()

# =================================================================================================

engine = Engine(10, 20, 50)
engine.run()

# status: FINISHED