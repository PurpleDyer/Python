import time
from random import randint
import threading
import keyboard

# ==============================================================================================================

CELL_WIDTH = 5
board1 = None
board2 = None
health = 3

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

class Character:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__character = '0'

    def __str__(self):
        return self.__character

    def move(self, direction):
        global board1
        global board2
        global health

        if (direction == 'right') and (0 <= self.__x+1 < board1.width):
            if board2.get_cell(self.__x+1, self.__y).has_type(Block):
                health -= 1
            else:
                board1.get_cell(self.__x, self.__y).clear_cell()
                self.__x += 1
                board1.get_cell(self.__x, self.__y).add_content(self.__character) 

        elif (direction == 'left') and (0 <= self.__x-1 < board1.width):
            if board2.get_cell(self.__x-1, self.__y).has_type(Block):
                health -= 1
            else:
                board1.get_cell(self.__x, self.__y).clear_cell()
                self.__x -= 1
                board1.get_cell(self.__x, self.__y).add_content(self.__character) 
            
        elif (direction == 'up') and (0 <= self.__y-1 < board1.height):
            if board2.get_cell(self.__x, self.__y-1).has_type(Block):
                health -= 1
            else:
                board1.get_cell(self.__x, self.__y).clear_cell()
                self.__y -= 1
                board1.get_cell(self.__x, self.__y).add_content(self.__character) 

        elif (direction == 'down') and (0 <= self.__y+1 < board1.height):
            if board2.get_cell(self.__x, self.__y+1).has_type(Block):
                health -= 1
            else:
                board1.get_cell(self.__x, self.__y).clear_cell()
                self.__y += 1
                board1.get_cell(self.__x, self.__y).add_content(self.__character) 

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
    def __init__(self, board_width, board_height, total_blocks):
        self.__board_width = board_width
        self.__board_height = board_height
        self.__total_blocks = total_blocks

    def run(self):
        global board1
        global board2
        global health
        
        board1 = Board(self.__board_width, self.__board_height)
        board2 = Board(self.__board_width, self.__board_height)
        character = Character(0, 0)
        board1.get_cell(character.x, character.y).add_content(character)

        total_blocks_counter = 0
        while total_blocks_counter < self.__total_blocks:

            random_x, random_y = randint(0, self.__board_width-1), randint(0, self.__board_height-1) 
            cell1 = board1.get_cell(random_x, random_y)
            cell2 = board2.get_cell(random_x, random_y)

            if not (cell2.has_type(Block)) and not (cell1.has_type(Character)): 
                cell2.add_content(Block()) 
                total_blocks_counter += 1

        printing_board = board1
        is_game_over = False

        def printer():
            global health
            nonlocal is_game_over

            print("Press Space to switch between dimensions")
            time.sleep(2)

            while True:
                if health == 0:
                    is_game_over = True
                    break
                print(f"Health: {health}")
                print(printing_board)
                time.sleep(0.5)

        def changer():
            global health
            nonlocal is_game_over
            nonlocal printing_board 

            while True:
                if health == 0:
                    is_game_over = True
                    break
                key = keyboard.read_key()
                if keyboard.is_pressed(key):
                    if key == 'space':
                        if printing_board == board1:
                            printing_board = board2
                        else:
                            printing_board = board1
                    elif key == 'esc':
                        health = 0
                    elif key != 'space' and printing_board == board1:
                        character.move(direction=key)

        printer_thread = threading.Thread(target=printer)
        changer_thread = threading.Thread(target=changer)

        printer_thread.start()
        changer_thread.start()

        if is_game_over:
            print("!~ Game Over ~!")

# ==============================================================================================================
            
engine = Engine(10, 10, 30)
engine.run()

# the whole idea of this game is to not run into the blocks as that it will damage you
# in this game you have to dodge the blocks by going into the second dimension
# you can enter the second dimension or the main dimension by pressing 'space'
# there is still a chance that the generated blocks, block you in a corner when you first start and run the game
# and i dont know how to fix it
# and also, you cant move while you are in the second dimension