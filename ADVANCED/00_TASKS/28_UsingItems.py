import keyboard
from time import sleep
from random import randint
import threading

# =======================================================================================

CELL_WIDTH = 5
board = None

# =======================================================================================

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

# =======================================================================================

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

# ===============================================================================

class Block:
    def __str__(self):
        return "-===-"

# ===============================================================================

class Item:
    pass

# ===============================================================================

class Key(Item):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "K"

    def add_to_inventory(self, character):
        character.add_to_inventory(self)

    def remove_self(self, x, y, character):
        global board
        board.get_cell(x, y).remove_content(self)
        character.add_to_inventory(self)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

# ===============================================================================

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

# ===============================================================================

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
        global board

        if keyboard.is_pressed(direction):
            if (direction == "right") and (0 <= self.__x+1 < board.width) and (not board.get_cell(self.__x+1, self.__y).has_type(Block)):
                if board.get_cell(self.__x+1, self.__y).has_type(Door):
                    door: Door = board.get_cell(self.__x+1, self.__y).return_type(Door)
                    if door.state == True:
                        board.get_cell(self.__x, self.__y).remove_content(self)
                        self.__x += 1
                        board.get_cell(self.__x, self.__y).add_content(self)
                else:
                    board.get_cell(self.__x, self.__y).remove_content(self)
                    self.__x += 1
                    board.get_cell(self.__x, self.__y).add_content(self)

            elif (direction == "left") and (0 <= self.__x-1 < board.width) and (not board.get_cell(self.__x-1, self.__y).has_type(Block)):
                if board.get_cell(self.__x-1, self.__y).has_type(Door):
                    door: Door = board.get_cell(self.__x-1, self.__y).return_type(Door)
                    if door.state == True:
                        board.get_cell(self.__x, self.__y).remove_content(self)
                        self.__x -= 1
                        board.get_cell(self.__x, self.__y).add_content(self)
                else:
                    board.get_cell(self.__x, self.__y).remove_content(self)
                    self.__x -= 1
                    board.get_cell(self.__x, self.__y).add_content(self)

            elif (direction == "up") and (0 <= self.__y-1 < board.height) and (not board.get_cell(self.__x, self.__y-1).has_type(Block)):
                if board.get_cell(self.__x, self.__y-1).has_type(Door):
                    door: Door = board.get_cell(self.__x, self.__y-1).return_type(Door)
                    if door.state == True:
                        board.get_cell(self.__x, self.__y).remove_content(self)
                        self.__y -= 1
                        board.get_cell(self.__x, self.__y).add_content(self)
                else:
                    board.get_cell(self.__x, self.__y).remove_content(self)
                    self.__y -= 1
                    board.get_cell(self.__x, self.__y).add_content(self)

            elif (direction == "down") and (0 <= self.__y+1 < board.height) and (not board.get_cell(self.__x, self.__y+1).has_type(Block)):
                if board.get_cell(self.__x, self.__y+1).has_type(Door):
                    door: Door = board.get_cell(self.__x, self.__y+1).return_type(Door)
                    if door.state == True:
                        board.get_cell(self.__x, self.__y).remove_content(self)
                        self.__y += 1
                        board.get_cell(self.__x, self.__y).add_content(self)
                else:
                    board.get_cell(self.__x, self.__y).remove_content(self)
                    self.__y += 1
                    board.get_cell(self.__x, self.__y).add_content(self)

    def add_to_inventory(self, element):
        self.__inventory.append(element)

    def remove_from_inventory(self, element):
        if element in self.__inventory:
            self.__inventory.remove(element)

    def pick_up(self):
        global board
        cell = board.get_cell(self.__x, self.__y)
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
        global board
        for x, y in self.character_range:
            cell = board.get_cell(self.__x+x, self.__y+y)
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
        door = Door(0, 5)
        board.get_cell(door.x, door.y).add_content(door)
        key = Key(5, 0)
        board.get_cell(key.x, key.y).add_content(key)
        
        total_blocks_counter = 0
        while total_blocks_counter < self.__total_blocks:
            random_x, random_y = randint(0, self.__board_width-1), randint(0, self.__board_height-1)
            cell = board.get_cell(random_x, random_y)
            if (not cell.has_type(Block)) and (not cell.has_type(Character)) and (not cell.has_type(Item)) and (not cell.has_type(Door)):
                block = Block()
                cell.add_content(block)
                total_blocks_counter += 1

        is_game_over = False

        def printer():
            while not is_game_over:
                print(f"[ {' - '.join(map(str, character.inventory))} ]")
                print(board)
                sleep(0.004876)
                # sleep(1)
        def reader():
            while True:
                key = keyboard.read_key()
                if key == 'e':
                    character.pick_up()
                elif key == 'f':
                    character.use_item()
                elif key == 'esc':
                    nonlocal is_game_over
                    is_game_over = True
                    break
                else:
                    character.move(key)

        printer_thread = threading.Thread(target=printer)
        reader_thread = threading.Thread(target=reader)

        printer_thread.start()
        reader_thread.start()

# ===============================================================================

engine = Engine(10, 10, 25)
engine.run()