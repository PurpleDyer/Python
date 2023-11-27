from random import randint
from time import sleep
import threading
import keyboard

# =======================================================================

CELL_WIDTH = 3
board = [
    [' ', ' ', ' ', ' ', 'BC', ' ', ' ', '=', 'B0', ' '],
    ['B1', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', ' ', ' '],
    [' ', ' ', 'B4', '=', ' ', ' ', ' ', ' ', 'B3', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['B2', '=', ' ', ' ', 'S', ' ', '=', ' ', '=', ' '],
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

class Enemy:
    enemies = []

    def __init__(self, x, y, name):
        self.__x = x    # starting values
        self.__y = y    # starting values
        self.__name = name  # BC
        self.__cords = []
        self.__total_teleports = 0
        self.__index = 0

        self.enemies.append(self)

    def __str__(self):
        return self.__name[0]   # BC => B

    def add_cords(self, cords: tuple, insertion_index):
        self.__cords.insert(insertion_index, cords)
        self.__total_teleports += 1

    def move(self):
        random_number = randint(0, 10)
        if (random_number > 7) or (random_number == 0): 
            global real_board

            real_board.get_cell(self.__x, self.__y).remove_content(self)
            
            if (random_number == 0) and (0 <= self.__index-1):
                self.__index -= 1
            else:
                self.__index += 1

            self.__x, self.__y = self.__cords[self.__index%self.__total_teleports]
            real_board.get_cell(self.__x, self.__y).add_content(self)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def name(self):
        return self.__name

    @property
    def cords(self):
        return self.__cords

    @property
    def total_teleports(self):
        return self.__total_teleports

    @property
    def index(self):
        return self.__index

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
                real_board.get_cell(self.__x, self.__y).remove_content(self)
                self.__x += 1
                real_board.get_cell(self.__x, self.__y).add_content(self)

            elif (direction == "left") and (0 <= self.__x-1 < real_board.width) and (not real_board.get_cell(self.__x-1, self.__y).has_type(Block)):
                real_board.get_cell(self.__x, self.__y).remove_content(self)
                self.__x -= 1
                real_board.get_cell(self.__x, self.__y).add_content(self)

            elif (direction == "up") and (0 <= self.__y-1 < real_board.height) and (not real_board.get_cell(self.__x, self.__y-1).has_type(Block)):
                real_board.get_cell(self.__x, self.__y).remove_content(self)
                self.__y -= 1
                real_board.get_cell(self.__x, self.__y).add_content(self)

            elif (direction == "down") and (0 <= self.__y+1 < real_board.height) and (not real_board.get_cell(self.__x, self.__y+1).has_type(Block)):
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
    elif element == 'BC':
        bonnie = Enemy(x=x, y=y, name=element)
        cell.add_content(bonnie)
    elif "B" in element:
        for enemy in Enemy.enemies:
            if element[0] == enemy.name[0]:
                enemy.add_cords(cords=(x, y), insertion_index=int(element[-1]))
                
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
                print('hi')
                if keyboard.is_pressed(key):
                    if key == 'esc':
                        nonlocal is_game_over
                        is_game_over = True
                        break
                    elif key in ['right', 'up', 'down', 'left']:
                        character.move(key)  

        def mover():
            while not is_game_over:
                for enemy in Enemy.enemies:
                    enemy: Enemy
                    enemy.move()
                sleep(4)         

        printer_thread = threading.Thread(target=printer)
        reader_thread = threading.Thread(target=reader)
        mover_thread = threading.Thread(target=mover)

        printer_thread.start()
        reader_thread.start()
        mover_thread.start()

# =============================================================================== 

engine = Engine()
engine.run()

# state: FINISHED