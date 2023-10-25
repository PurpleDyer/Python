from time import sleep
from random import randint
import threading
import keyboard

# =============================================================================

CELL_WIDTH = 3
board = [
    ['S', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', '=', ' ', '=', ' ', ' ', '=', '=', '=', ' '],
    [' ', '=', ' ', '=', '=', ' ', ' ', ' ', '=', ' '],
    [' ', '=', ' ', ' ', '=', '=', '=', ' ', '=', ' '],
    [' ', '=', ' ', ' ', ' ', 'K', '=', ' ', '=', ' '],
    [' ', '=', ' ', '=', '=', '=', '=', ' ', '=', ' '],
    [' ', '=', ' ', ' ', '=', ' ', ' ', ' ', '=', ' '],
    [' ', '=', '=', '=', '=', ' ', '=', ' ', '=', '='],
    [' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', 'D', 'E'],
]
real_board = None
keys = ['up', 'down', 'left', 'right', 'esc', 'e', 'f']
start = None
end = None

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

class End:
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

class Item:
    pass

# =============================================================================

class Key(Item):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "K"

    def add_to_inventory(self, character):
        character.add_to_inventory(self)

    def remove_self(self, x, y, character):
        global real_board
        real_board.get_cell(x, y).remove_content(self)
        character.add_to_inventory(self)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

# =============================================================================

class Door:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__open = False

    def __str__(self):
        if self.__open:
            return ""
        else:
            return "D"

    def open_door(self, character):
        if character.has_item(Key):
            character.remove_from_inventory(Key)
            self.__open = True

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    @property
    def state(self):
        return self.__open

# =============================================================================

class Character:

    character_range = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (1, 0),
        (-1, 1),  (0, 1),  (1, 1)
    ]

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__inventory = []

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

    def add_to_inventory(self, element):
        self.__inventory.append(element)

    def remove_from_inventory(self, element):
        if element in self.__inventory:
            self.__inventory.remove(element)

    def pick_up(self):
        global real_board
        cell = real_board.get_cell(self.__x, self.__y)
        if cell.has_type(Item):
            for element in cell.content:
                if isinstance(element, Key):
                    element.remove_self(self.__x, self.__y, self)

    def has_item(self, typ):
        for item in self.__inventory:
            if isinstance(item, typ):
                return True
        return False

    def use_item(self):
        global real_board
        for x, y in self.character_range:
            if (0 <= self.__x+x < real_board.width) and (0 <= self.__y+y < real_board.height):
                cell = real_board.get_cell(self.__x+x, self.__y+y)
                if cell.has_type(Door):
                    door: Door = cell.return_type(Door)
                    door.open_door(self)
                    break

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
    elif element == 'E':
        global end 
        end = End(x=x, y=y)
    elif element == 'S':
        global start
        start = Start(x=x, y=y)
    elif element == 'D':
        cell.add_content(Door(x=x, y=y))
    elif element == 'K':
        cell.add_content(Key(x=x, y=y))

    return cell

# ===============================================================================

class Board:
    def __init__(self, blueprint):
        self.__blueprint = blueprint
        self.__board = [[thrower(x=x, y=y, element=element) for x, element in enumerate(row)] for y, row in enumerate(self.__blueprint)]

    def __str__(self):
        LINE = (((CELL_WIDTH + 1) * len(self.__board[0])) + 1) * "-" + "\n"
        FINAL_BOARD = LINE
        for row in self.__board:
            FINAL_BOARD +=  "|" + "|".join(map(lambda x: str(x).center(CELL_WIDTH), row)) + "|\n" + LINE
        return FINAL_BOARD

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
                print(f"[ {' - '.join(map(str, character.inventory))} ]")
                print(real_board)
                sleep(0.004876)

        def reader():
            while True:
                key = keyboard.read_key()
                if key in keys:
                    if key == 'esc':
                        nonlocal is_game_over
                        is_game_over = True
                        break
                    elif key == 'e':
                        character.pick_up()
                    elif key == 'f':
                        character.use_item()
                    else:
                        character.move(direction=key)
                        if (character.x == end.x) and (character.y == end.y): 
                            is_game_over = True
                            break

        printer_thread = threading.Thread(target=printer)
        reader_thread = threading.Thread(target=reader)

        printer_thread.start()
        reader_thread.start()

# =============================================================================== 

engine = Engine()
engine.run()

# status: FINISHED