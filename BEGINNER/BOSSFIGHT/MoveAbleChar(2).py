# MoveAbleChar(2)
# A Character That Can Move In A Custom-Built Map In The Shape Of A Square But With Random Generated Blocks



import keyboard
from random import randint

CELL_WIDTH = 5

# ========================================================================

class Cell:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__content = [] 

    def __str__(self):
        return "-".join(map(str, self.__content))

    def add_content(self, elem):
        self.__content.append(elem)

    def remove_content(self, elem):
        self.__content.remove(elem)

    def clear_cell(self):
        self.__content.clear()

    def has_typ(self, typ):
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
    
# ======================================================================

class Map:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__board = [[Cell(x=x, y=y) for x in range(self.__width)] for y in range(self.__height)]

    def __str__(self):
        lines = (((CELL_WIDTH + 1) * self.__width) + 1) * "-" + "\n"
        new_board = lines
        for row in self.__board:
            new_board += "|" + "|".join(list(map(lambda x: str(x).center(CELL_WIDTH), row))) + "|\n" + lines
        return new_board

    def get_cell(self, x, y):
            return self.__board[y][x]

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def board(self):
        return self.__board

# =============================================================================

class Char:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__character = "0"

    def __str__(self):
        return self.__character

    def add_to_board(self):
        global board
        board.get_cell(self.__x, self.__y).add_content(self.__character)

    def move(self, direction):
        global board
        if keyboard.is_pressed(direction):
            if (direction == 'd' or direction == 'right') and (0 <= self.__x+1 < board.width) and not (board.get_cell(self.__x+1, self.__y).has_typ(Block)):
                board.get_cell(self.__x, self.__y).clear_cell()
                self.__x += 1
                board.get_cell(self.__x, self.__y).add_content(self.__character)
            elif (direction == 'a' or direction == 'left') and (0 <= self.__x-1 < board.width) and not (board.get_cell(self.__x-1, self.__y).has_typ(Block)):
                board.get_cell(self.__x, self.__y).clear_cell()
                self.__x -= 1
                board.get_cell(self.__x, self.__y).add_content(self.__character)
            elif (direction == 'w' or direction == 'up') and (0 <= self.__y-1 < board.height) and not (board.get_cell(self.__x, self.__y-1).has_typ(Block)):
                board.get_cell(self.__x, self.__y).clear_cell()
                self.__y -= 1
                board.get_cell(self.__x, self.__y).add_content(self.__character)
            elif (direction == 's' or direction == 'down') and (0 <= self.__y+1 < board.height) and not (board.get_cell(self.__x, self.__y+1).has_typ(Block)):
                board.get_cell(self.__x, self.__y).clear_cell()
                self.__y += 1
                board.get_cell(self.__x, self.__y).add_content(self.__character)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    @property
    def character(self):
        return self.__character
        
# ============================================================================= 

class Block:
    def __init__(self):
        self.__character = "====="

    def __str__(self):
        return self.__character

    @property
    def character(self):
        return self.__character

    
# =============================================================================

class Engine:
    def __init__(self, map_width, map_height, total_blocks):
        self.__map_width = map_width
        self.__map_height = map_height
        self.__total_blocks = total_blocks

    def run(self):
        global board
        board = Map(self.__map_width, self.__map_height)
        char = Char(0, 0)
        char.add_to_board()
        blocks_cnt = 0

        while blocks_cnt < self.__total_blocks:
            cx = randint(0, self.__map_width-1)
            cy = randint(0, self.__map_height-1)
            if not (board.get_cell(cx, cy).has_typ(object)):
                board.get_cell(cx, cy).add_content(Block())
                blocks_cnt += 1

        print(board)
        while True:
            key = keyboard.read_key()
            if key == 'esc':
                break
            else:
                char.move(key)
            print(board)

# ===============================================================================

board = None
engine = Engine(13, 13, 30)
engine.run()