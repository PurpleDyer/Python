import time
from random import randint
import threading
import keyboard

# ==============================================================================================================

CELL_WIDTH = 5
board = None
Bombs = []

# ==============================================================================================================

class Cell:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__content = []

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
        for i in self.__content:
            if isinstance(i, typ):
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

# ==============================================================================================================

class Block:
    def __str__(self):
        return "-===-"

# ==============================================================================================================

class Character:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__character = '0'

    def __str__(self):
        return self.__character
        
    def move(self, direction):
        global board

        if keyboard.is_pressed(direction):

            if (direction == 'right') and (0 <= self.__x+1 < board.width) and not (board.get_cell(self.__x+1, self.__y).has_type(Block)):
                board.get_cell(self.__x, self.__y).clear_cell()
                self.__x += 1
                board.get_cell(self.__x, self.__y).add_content(self.__character)

            elif (direction == 'left') and (0 <= self.__x-1 < board.width) and not (board.get_cell(self.__x-1, self.__y).has_type(Block)):
                board.get_cell(self.__x, self.__y).clear_cell()
                self.__x -= 1
                board.get_cell(self.__x, self.__y).add_content(self.__character)

            elif (direction == 'up') and (0 <= self.__y-1 < board.height) and not (board.get_cell(self.__x, self.__y-1).has_type(Block)):
                board.get_cell(self.__x, self.__y).clear_cell()
                self.__y -= 1
                board.get_cell(self.__x, self.__y).add_content(self.__character)

            elif (direction == 'down') and (0 <= self.__y+1 < board.height) and not (board.get_cell(self.__x, self.__y+1).has_type(Block)):
                board.get_cell(self.__x, self.__y).clear_cell()
                self.__y += 1
                board.get_cell(self.__x, self.__y).add_content(self.__character)

    def destory(self):
        global board
        explosion_range = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

        for x, y in explosion_range:
            if (0 <= self.__x+x < board.width) and (0 <= self.__y+y < board.height):
                board.get_cell(self.__x+x, self.__y+y).clear_cell()



    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def character(self):
        return self.__character

# ==============================================================================================================

class Engine:
    def __init__(self, board_width, board_height, total_blocks, total_bombs):
        self.__board_width = board_width
        self.__board_height = board_height
        self.__total_blocks = total_blocks
        self.__total_bombs = total_bombs

    def run(self):
        global board

        board = Board(self.__board_width, self.__board_height)
        character = Character()
        board.get_cell(character.x, character.y).add_content(Character())

        # making the blocks
        total_blocks_counter = 0
        while total_blocks_counter < self.__total_blocks:

            random_x, random_y = randint(0, board.width-1), randint(0, board.height-1)
            cell = board.get_cell(random_x, random_y)

            if not (cell.has_type(Character)) and not (cell.has_type(Block)):
                cell.add_content(Block())
                total_blocks_counter += 1

        is_game_over = False

        def printer():
            while True:
                if (self.__total_bombs == 0):
                    is_game_over = True
                    break
                time.sleep(0.125)
                print(f"Bombs: {int(self.__total_bombs)}")
                print(board)

        def getter():
            while True:
                direction = keyboard.read_key()

                if direction == 'esc' or is_game_over == True:
                    break

                elif direction == 'shift':
                    self.__total_bombs -= 0.5
                    character.destory()

                else:
                    character.move(direction)

        printer_thread = threading.Thread(target=printer)
        getter_thread = threading.Thread(target=getter)

        printer_thread.start()
        getter_thread.start()
    
# ==============================================================================================================

engine = Engine(10, 10, 25, 10)
engine.run()

# in this game, you can remove obstacles by pressing shift
# its like you make an explosion and destroy every block next to you