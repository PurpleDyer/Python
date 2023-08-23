import time
import threading

# ================================================================================================================

board = None
CELL_WIDTH = 5
enemy = None

# ================================================================================================================

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

# ================================================================================================================

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
    def width(self):
        return self.__board_width

    @property
    def height(self):
        return self.__board_height
    
    @property
    def board(self):
        return self.__board

# ================================================================================================================

class AiEnemy:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__character = 'E'

    def __str__(self):
        return self.__character

    def move(self):
        global board
        global enemy

        if 0 <= self.__x+1< board.width:
            board.get_cell(self.__x, self.__y).clear_cell()
            self.__x += 1
            board.get_cell(self.__x, self.__y).add_content(enemy)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def character(self):
        return self.__character
    
# ================================================================================================================

class Engine:
    def __init__(self, board_width, board_height):
        self.__board_width = board_width
        self.__board_height = board_height

    def run(self):
        global board
        global enemy

        board = Board(self.__board_width, self.__board_height)
        enemy = AiEnemy(0, 0)
        board.get_cell(enemy.x, enemy.y).add_content(enemy)

        def mover():
            while True:
                enemy.move()
                time.sleep(1)

        def printer():
            while True:
                print(board)
                time.sleep(1)
            
        mover_thread = threading.Thread(target=mover)
        printer_thread = threading.Thread(target=printer)

        mover_thread.start()
        printer_thread.start()
            
# ================================================================================================================

engine = Engine(10, 10)
engine.run()

# results: COMPLETE
# P.O.D: making an enemy move on its own
# recommendation: MAKE TWO MULTIPLE ENEMIES