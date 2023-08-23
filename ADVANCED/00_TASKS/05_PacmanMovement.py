import random
import keyboard
import time
import threading

# ================================

CELL_WIDTH = 5
direction = None
board = None

# ================================

class Cell:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__content = []
        
    def __str__(self):
        return "*".join(map(str, self.__content))

    def add_content(self, element):
        self.__content.append(element)

    def remove_content(self, element):
        self.__content.remove(element)

    def clear_cell(self):
        self.__content.clear()

    def has_type(self, typ):
        for item in self.__content:
            if isinstance(item, typ):
                return True
        return False

    def give_content(self):
        return self.__content

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def content(self):
        return self.__content

# ===================================

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

# =====================================

class Character:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__character = '0'

    def __str__(self):
        return self.__character

    def add_to_board(self):
        global board
        cell = board.get_cell(self.__x, self.__y)
        cell.add_content(str(Character()))

    def move(self):
        global direction
        global board

        if (direction == 'right') and (0 <= self.__x+1 < board.width):
            board.get_cell(self.__x, self.__y).clear_cell()
            self.__x += 1 
            board.get_cell(self.__x, self.__y).add_content(str(Character()))
    
        elif (direction == 'left') and (0 <= self.__x-1 < board.width):
            board.get_cell(self.__x, self.__y).clear_cell()
            self.__x -= 1
            board.get_cell(self.__x, self.__y).add_content(str(Character()))

        elif (direction == 'up') and (0 <= self.__y-1 < board.height):
            board.get_cell(self.__x, self.__y).clear_cell()
            self.__y -= 1
            board.get_cell(self.__x, self.__y).add_content(str(Character()))

        elif (direction == 'down') and (0 <= self.__y+1 < board.height) :
            board.get_cell(self.__x, self.__y).clear_cell()
            self.__y += 1
            board.get_cell(self.__x, self.__y).add_content(str(Character()))

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def character(self):
        return self.__character

# =======================================

class Engine:
    def __init__(self, board_width, board_height):
        self.__board_width = board_width
        self.__board_height = board_height

    def run(self):
        global board
        global direction
        

        board = Board(board_width=self.__board_width, board_height=self.__board_height)
        character = Character()
        character.add_to_board()

        def mover():
            while True:
                global direction
                time.sleep(0.25)
                character.move()
                print(direction)
                print(board)
        
        def inputer():
            while True:
                global direction
                direction = keyboard.read_key()


        mover_thread = threading.Thread(target=mover)
        inputer_thread = threading.Thread(target=inputer)

        inputer_thread.start()
        mover_thread.start()

        print("~! Game Over !~")

    @property
    def width(self):
        return self.__board_width

    @property
    def height(self):
        return self.__board_height

# =================================

engine = Engine(10, 10)
engine.run()

# this kind of movement is mostly seen in PacMan or the Snake game