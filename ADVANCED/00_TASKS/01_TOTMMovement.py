from random import randint
import time
import keyboard

# =======================================================================

CELL_WIDTH = 5

# =======================================================================

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

    def give_content(self):
        return self.__content

    def has_type(self, typ):
        for i in self.__content:
            if isinstance(i, typ):
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

# =======================================================================

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
    def board_width(self):
        return self.__board_width

    @property
    def board_height(self):
        return self.__board_height

    @property
    def board(self):
        return self.__board

# =======================================================================

class Block:
    def __init__(self):
        self.__character = '-===-'

    def __str__(self):
        return self.__character

    @property
    def character(self):   # we dont actually need this here but i put it for practice
        return self.__character    

# =======================================================================

class Character:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__character = '0'
    
    def __str__(self):
        return self.__character

    def add_to_board(self):
        global board
        board.get_cell(self.__x, self.__y).add_content(self.__character)

    def move(self, direction):
        global board
        if keyboard.is_pressed(direction):

            if direction == 'right':
                while True:
                    if (0 <= self.__x+1 < board.board_width) and (not board.get_cell(self.__x+1, self.__y).has_type(Block)):
                        board.get_cell(self.__x, self.__y).clear_cell()
                        self.__x += 1
                        board.get_cell(self.__x, self.__y).add_content(self.__character)
                        print(board)
                    else:
                        break
                    time.sleep(0.1)

            elif direction == 'left':
                while True:
                    if (0 <= self.__x-1 < board.board_width) and (not board.get_cell(self.__x-1, self.__y).has_type(Block)):
                        board.get_cell(self.__x, self.__y).clear_cell()
                        self.__x -= 1
                        board.get_cell(self.__x, self.__y).add_content(self.__character)
                        print(board)
                    else:
                        break
                    time.sleep(0.1)

            elif direction == 'up':
                while True:
                    if (0 <= self.__y-1 < board.board_height) and (not board.get_cell(self.__x, self.__y-1).has_type(Block)):
                        board.get_cell(self.__x, self.__y).clear_cell()
                        self.__y -= 1
                        board.get_cell(self.__x, self.__y).add_content(self.__character)
                        print(board)
                    else:
                        break
                    time.sleep(0.1)
            
            elif direction == 'down':
                while True:
                    if (0 <= self.__y+1 < board.board_height) and (not board.get_cell(self.__x, self.__y+1).has_type(Block)):
                        board.get_cell(self.__x, self.__y).clear_cell()
                        self.__y += 1
                        board.get_cell(self.__x, self.__y).add_content(self.__character)
                        print(board)
                    else:
                        break
                    time.sleep(0.1)
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def character(self):
        return self.__character

# =======================================================================

board = None

class Engine:
    def __init__(self, board_width, board_height, total_blocks):
        self.__board_width = board_width
        self.__board_height = board_height
        self.__total_blocks = total_blocks

    def run(self):
        global board
        board = Board(self.__board_width, self.__board_height)
        character = Character(0, 0)
        character.add_to_board()
        blocks_count = 0
        is_game_over = False

        # Creating Blocks
        while blocks_count < self.__total_blocks:
            block_x = randint(0, self.__board_width - 1)
            block_y = randint(0, self.__board_height - 1)
            cell = board.get_cell(block_x, block_y)
            if not (cell.has_type(Character)) and not (cell.has_type(Block)):
                cell.add_content(Block())
                blocks_count += 1

        # The Game
        print(board)
        while not is_game_over:
            direction = keyboard.read_key()
            if direction == 'esc':
                print("!~ Game Over ~!")
                is_game_over = True
            else:
                character.move(direction)
                print(board)

# =======================================================================

engine = Engine(8, 8, 10)
engine.run()