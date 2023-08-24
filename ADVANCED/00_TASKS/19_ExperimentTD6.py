import threading
import time 

# ========================================================================================================================================

CELL_WIDTH = 5
board = [
    ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', ' ', ' ', ' ', 'O', ' ', ' '],
    ['O', ' ', 'O', ' ', 'O', ' ', 'O'],
    ['O', ' ', 'O', ' ', 'O', ' ', 'O'],
    ['O', ' ', 'O', ' ', 'O', ' ', 'O'],
    [' ', ' ', 'O', ' ', ' ', ' ', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O']
]
main_board = []

# ========================================================================================================================================

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

# ========================================================================================================================================

# for y, row in enumerate(board):
#     for x, element in enumerate(row):
#         Cell(x=x, y=y)

# ========================================================================================================================================

class Block:
    def __str__(self):
        return '-===-'

# ========================================================================================================================================

class AiEnemy:
    def __init__(self):
        self.__x = 0
        self.__y = 5

    def __str__(self):
        return 'E'

    def move(self):
        global main_board

        if (0 <= self.__x+1 < main_board.width) and not (main_board.get_cell(self.__x+1, self.__y).has_type(Block)):
            while (0 <= self.__x+1 < main_board.width) and not (main_board.get_cell(self.__x+1, self.__y).has_type(Block)):
                time.sleep(1)
                main_board.get_cell(self.__x, self.__y).remove_content(self)
                self.__x += 1
                main_board.get_cell(self.__x, self.__y).add_content(self)
            
        elif (0 <= self.__y-1 < main_board.height) and not (main_board.get_cell(self.__x, self.__y-1).has_type(Block)):
            while (0 <= self.__y-1 < main_board.height) and not (main_board.get_cell(self.__x, self.__y-1).has_type(Block)):
                time.sleep(1)
                main_board.get_cell(self.__x, self.__y).remove_content(self)
                self.__y -= 1
                main_board.get_cell(self.__x, self.__y).add_content(self)
        
        elif (0 <= self.__y+1 < main_board.height) and not (main_board.get_cell(self.__x, self.__y+1).has_type(Block)):
            while (0 <= self.__y+1 < main_board.height) and not (main_board.get_cell(self.__x, self.__y+1).has_type(Block)):
                time.sleep(1)
                main_board.get_cell(self.__x, self.__y).remove_content(self)
                self.__y += 1
                main_board.get_cell(self.__x, self.__y).add_content(self)

# ========================================================================================================================================

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

# ========================================================================================================================================

class Engine:
    def run(self):
        global board
        global main_board

        main_board = Board(board_width=len(board[0]), board_height=len(board))
        enemy = AiEnemy()
        
        for y, row in enumerate(board):
            for x, element in enumerate(row):
                if element != ' ':
                    main_board.get_cell(x, y).add_content(Block())

        is_game_over = False

        def printer():
            while True:
                if is_game_over:
                    break
                print(main_board)
                time.sleep(0.004876)

        def mover():
            while True:
                enemy.move()

        printer_thread = threading.Thread(target=printer)
        mover_thread = threading.Thread(target=mover)

        printer_thread.start()
        mover_thread.start()

# ========================================================================================================================================

engine = Engine()
engine.run()

# results: COMPLETE
# P.O.D: making an enemy go in a self-made board
# recommendation: MOVE AN ENEMY IN A BOARD WITH TKINTER (BOARD SHOULD BE GENERATED)