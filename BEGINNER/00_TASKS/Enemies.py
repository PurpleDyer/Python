from random import randint
import time

CELL_WIDTH = 5

class Cell:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__content = []

    def __str__(self):
        return "-".join(map(str, self.__content))

    def add_content(self, elem: str):
        self.__content.append(elem)

    def clear_cell(self):
        self.__content.clear()

    def get_content(self):
        return self.__content

    def has_typ(self, typ):
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

    @property
    def content(self):
        return self.__content


class Board:
    def __init__(self, board_width: int, board_height: int):
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


board = None 

class Enemy:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "E"

    def move(self, n):
        global board
        MOVES = [[0, -1], [-1, 0], [1, 0], [0, 1]]
        if (0 <= self.__x + MOVES[n][0] < board.width) and (0 <= self.__y + MOVES[n][0] < board.height): 
            time.sleep(1)
            board.get_cell(self.__x, self.__y).clear_cell()
            self.__x += MOVES[n][0]
            self.__y += MOVES[n][1]
            board.get_cell(self.__x, self.__y).add_content(str(Enemy))

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


class Engine:
    def __init__(self, board_width, board_height, turns):
        self.__board_width = board_width
        self.__board_height = board_height
        self.__turns = turns

    def run(self):
        global board
        board = Board(self.__board_width, self.__board_height)
        x = randint(0, self.__board_width-1)
        y = randint(0, self.__board_height-1)
        enemy = Enemy(x=x, y=y)
        board.get_cell(x=x, y=y).add_content(enemy)

        is_game_over = False
        turns = self.__turns
        while not is_game_over:
            print(board)
            enemy.move(randint(0, 3))
            turns += 1
            if turns == self.__turns:
                is_game_over = True
        
        print("  !  GAME OVER  !  ")

engine = Engine(5, 5, 20)
engine.run()

# ! what the fuck is this ! 
# ! CODE DOES NOT WORK !