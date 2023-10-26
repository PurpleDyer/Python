from time import sleep
import keyboard
import threading

# ==============================================================================

CELL_WIDTH = 3
board = [
    ['S1', '=', ' ', ' ', ' ', '=', ' ', ' ', ' '],
    [' ', '=', ' ', '=', ' ', '=', ' ', '=', ' '],
    [' ', '=', ' ', '=', ' ', '=', ' ', '=', ' '],
    [' ', '=', ' ', '=', ' ', '=', ' ', '=', ' '],
    [' ', '=', ' ', '=', ' ', '=', ' ', '=', ' '],
    [' ', '=', ' ', '=', ' ', '=', ' ', '=', ' '],
    [' ', ' ', ' ', '=', ' ', ' ', ' ', '=', 'S2'],
]
real_board = None
keys = ['right', 'left', 'up', 'down', 'esc']

# ==============================================================================

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

# ==============================================================================

class Block:
    def __str__(self):
        return "-=-"

# ==============================================================================

class Character:
    characters = []
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.characters.append(self)
        
    def __str__(self):
        return '0'

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

# ==============================================================================

def thrower(x, y, element):
    cell = Cell(x=x, y=y)
    if element == '=':
        cell.add_content(Block())
    elif (element == "S1") or (element == "S2"):
        character = Character(x=x, y=y)
        cell.add_content(character)
    return cell

# ==============================================================================

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

# ==============================================================================

class Engine:
    def run(self):
        global real_board

        real_board = Board(board)
        is_game_over = False

        def printer():
            while not is_game_over:
                print(real_board)
                sleep(0.004876)
                # sleep(0.25)

        def reader():
            while True:
                key = keyboard.read_key()
                if key in keys:
                    if key == 'esc':
                        nonlocal is_game_over
                        is_game_over = True
                        break
                    else:
                        for character in Character.characters:
                            character.move(key)
                        if (Character.characters[0].x == Character.characters[1].x) and (Character.characters[0].y == Character.characters[1].y):
                            is_game_over = True
                            break

        printer_thread = threading.Thread(target=printer)
        reader_thread = threading.Thread(target=reader)

        printer_thread.start()  
        reader_thread.start()

# ==============================================================================

engine = Engine()
engine.run()


# status: FINISHED