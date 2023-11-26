from time import sleep
from random import randint
import threading
import keyboard

# =============================================================================

keys = ['a', 'd']
CELL_WIDTH = 3
board = [
    ['=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', ' ', ' ', ' ', ' ', ' '],
    ['=', ' ', '=', '=', '=', '=', ' ', ' ', ' ', ' ', '=', '=', '=', ' ', ' ', ' '],
    ['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', ' '],
    ['=', ' ', ' ', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', '=', '='],
    ['=', ' ', ' ', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' '],
    ['=', '=', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', ' '],
    [' ', '=', ' ', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', '=', ' '],
    [' ', '=', ' ', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', '=', '='],
    [' ', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', '=', ' '],
    [' ', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', ' '],
    [' ', '=', ' ', '=', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', '=', '=', '=', '='],
    [' ', '=', '=', '=', '=', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', ' ', ' ', '='],
    [' ', '=', ' ', ' ', '=', ' ', '=', ' ', '=', ' ', '=', ' ', ' ', ' ', ' ', '='],
    [' ', '=', ' ', ' ', '=', ' ', '=', ' ', '=', ' ', '=', ' ', ' ', ' ', ' ', '='],
    [' ', '=', ' ', ' ', ' ', ' ', '=', ' ', '=', ' ', '=', '=', '=', '=', '=', '='],
    [' ', '=', ' ', ' ', '=', ' ', '=', '=', '=', ' ', '=', ' ', ' ', ' ', ' ', ' '],
    [' ', '=', '=', '=', '=', ' ', '=', ' ', '=', ' ', '=', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '=', ' ', 'D', ' ', 'D', ' ', '=', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '=', ' ', '=', 'S', '=', ' ', '=', ' ', ' ', ' ', ' ', ' '],
]
real_board = None
start = None

# =============================================================================

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

    def return_type(self, typ):
        for element in self.__content:
            if isinstance(element, typ):
                return element
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

# =============================================================================

class Block:
    def __str__(self):
        return '-=-'

# =============================================================================

class Start:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

# =============================================================================

class Door:
    doors = []

    def __init__(self, x, y, key):
        self.__x = x
        self.__y = y
        self.__key = key
        self.__open = False
        self.doors.append(self)

    def __str__(self):
        if self.__open:
            return ""
        else:
            return "!!!"

    def open_door(self):
        if self.__open:
            self.__open = False
        else:
            self.__open = True

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def key(self):
        return self.__key
    
    @property
    def state(self):
        return self.__open

# =============================================================================

class Character:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "0"

    def move(self, direction):
        global real_board

        if keyboard.is_pressed(direction):
            if (direction == "right") and (0 <= self.__x+1 < real_board.width) and (not real_board.get_cell(self.__x+1, self.__y).has_type(Block)):
                if real_board.get_cell(self.__x+1, self.__y).has_type(Door):
                    door: Door = real_board.get_cell(self.__x+1, self.__y).return_type(Door)
                    if door.state == True:
                        real_board.get_cell(self.__x, self.__y).remove_content(self)
                        self.__x += 1
                        real_board.get_cell(self.__x, self.__y).add_content(self)
                else:
                    real_board.get_cell(self.__x, self.__y).remove_content(self)
                    self.__x += 1
                    real_board.get_cell(self.__x, self.__y).add_content(self)

            elif (direction == "left") and (0 <= self.__x-1 < real_board.width) and (not real_board.get_cell(self.__x-1, self.__y).has_type(Block)):
                if real_board.get_cell(self.__x-1, self.__y).has_type(Door):
                    door: Door = real_board.get_cell(self.__x-1, self.__y).return_type(Door)
                    if door.state == True:
                        real_board.get_cell(self.__x, self.__y).remove_content(self)
                        self.__x -= 1
                        real_board.get_cell(self.__x, self.__y).add_content(self)
                else:
                    real_board.get_cell(self.__x, self.__y).remove_content(self)
                    self.__x -= 1
                    real_board.get_cell(self.__x, self.__y).add_content(self)

            elif (direction == "up") and (0 <= self.__y-1 < real_board.height) and (not real_board.get_cell(self.__x, self.__y-1).has_type(Block)):
                if real_board.get_cell(self.__x, self.__y-1).has_type(Door):
                    door: Door = real_board.get_cell(self.__x, self.__y-1).return_type(Door)
                    if door.state == True:
                        real_board.get_cell(self.__x, self.__y).remove_content(self)
                        self.__y -= 1
                        real_board.get_cell(self.__x, self.__y).add_content(self)
                else:
                    real_board.get_cell(self.__x, self.__y).remove_content(self)
                    self.__y -= 1
                    real_board.get_cell(self.__x, self.__y).add_content(self)

            elif (direction == "down") and (0 <= self.__y+1 < real_board.height) and (not real_board.get_cell(self.__x, self.__y+1).has_type(Block)):
                if real_board.get_cell(self.__x, self.__y+1).has_type(Door):
                    door: Door = real_board.get_cell(self.__x, self.__y+1).return_type(Door)
                    if door.state == True:
                        real_board.get_cell(self.__x, self.__y).remove_content(self)
                        self.__y += 1
                        real_board.get_cell(self.__x, self.__y).add_content(self)
                else:
                    real_board.get_cell(self.__x, self.__y).remove_content(self)
                    self.__y += 1
                    real_board.get_cell(self.__x, self.__y).add_content(self)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def inventory(self):
        return self.__inventory

# ===============================================================================

def thrower(x, y, element):
    cell = Cell(x=x, y=y)
    if element == '=':
        cell.add_content(Block())
    elif element == 'S':
        global start
        start = Start(x=x, y=y)
    elif element == 'D':
        cell.add_content(Door(x=x, y=y, key=keys.pop(0)))

    return cell

# ===============================================================================

class Board:
    def __init__(self, blueprint):
        self.__board = [[thrower(x=x, y=y, element=element) for x, element in enumerate(row)] for y, row in enumerate(blueprint)]

    def __str__(self):
        LINE = (((CELL_WIDTH + 1) * len(self.__board[0])) + 1) * "-" + "\n"
        FINAL_BOARD = LINE
        for row in self.__board:
            FINAL_BOARD +=  "|" + "|".join(map(lambda x: str(x).center(CELL_WIDTH), row)) + "|\n"
        return FINAL_BOARD + LINE

    def get_cell(self, x, y):
        return self.__board[y][x]
    
    @property
    def width(self):
        return len(self.__board[0])

    @property
    def height(self):
        return len(self.__board)

    @property
    def board(self):
        return self.__board

# =============================================================================== 

class Engine:
    def run(self):
        global real_board

        real_board = Board(board)
        character = Character(start.x, start.y)
        real_board.get_cell(character.x, character.y).add_content(character)
        is_game_over = False

        def printer():
            while not is_game_over:
                print(real_board)
                sleep(0.004876)

        def reader():
            while True:
                key = keyboard.read_key()
                if keyboard.is_pressed(key):
                    if key == 'esc':
                        nonlocal is_game_over
                        is_game_over = True
                        break
                    elif key in ['right', 'up', 'down', 'left']:
                        character.move(key) 
                    else:
                        for door in Door.doors:
                            door: Door
                            if door.key == key:
                                if not ((door.x == character.x) and (door.y == character.y)):
                                    door.open_door()

        printer_thread = threading.Thread(target=printer)
        reader_thread = threading.Thread(target=reader)

        printer_thread.start()
        reader_thread.start()

# =============================================================================== 

engine = Engine()
engine.run()

# status: FINISHED
# "a" and "d" to close and open the doors
# 'right', 'left', 'up', 'down' to move the characters