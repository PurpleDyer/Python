from random import randint
import time

# =============================================================

CELL_WIDTH = 5
POINTS_COUNTER = 0
board = None
switch = True

# =============================================================

class Cell:
    def __init__(self, x, y):
        self.__x = x 
        self.__y = y
        self.__content = ["-"]
        self.reveal = True

    def __str__(self):
        if self.reveal:
            return "-".join(map(str, self.__content))
        else:
            return ""

    def give_content(self):
        return self.__content

    def add_content(self, element):
        self.__content.append(element)

    def remove_content(self, element):
        self.__content.remove(element)

    def clear_cell(self):
        self.__content.clear()

    def has_type(self, typ):
        for i in self.__content:
            if isinstance(i, typ):
                return True
        return False

    def reveal_switch(self):
        if self.reveal:
            self.reveal = False
        else:
            self.reveal = True

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def content(self):
        return self.__content

# ============================================================

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

    def reveal_cells(self):
        for y in range(self.__board_height):
            for x in range(self.__board_width):
                self.__board[y][x].reveal_switch()

    @property
    def board_width(self):
        return self.__board_width

    @property
    def board_height(self):
        return self.__board_height

    @property
    def board(self):
        return self.__board

# ====================================================================

class Point:
    def __init__(self):
        self.__character = "o"

    def __str__(self):
        return self.__character

# ====================================================================

class Engine:
    def __init__(self, board_width, board_height):
        self.__board_width = board_width
        self.__board_height = board_height
        self.__total_points = randint(2, 4)

    def run(self):
        global board
        board = Board(self.__board_width, self.__board_height)
        total_points_counter = 0
        is_game_over = False
        points_correct = 0

        while total_points_counter < self.__total_points:
            random_x = randint(0, self.__board_width-1)
            random_y = randint(0, self.__board_height-1)
            cell = board.get_cell(random_x, random_y)
            if not cell.has_type(Point):
                cell.clear_cell()
                point = Point()
                cell.add_content(point)
                total_points_counter += 1

        print(board, flush=True)
        print(f"total_points_counter: {total_points_counter}")
        for y in range(self.__board_height):
            for x in range(self.__board_width):
                board.get_cell(x, y).reveal = False

        while not is_game_over:
            print(board, flush=True)
            input_x, input_y = list(map(int, input("x> , y^ : ").split()))
            input_x, input_y = input_x-1, input_y-1
            if (0 <= input_x < board.board_width) and (0 <= input_y < board.board_height):
                cell = board.get_cell(input_x, input_y)
                if cell.reveal:
                    print("You have Already chosen this cell before")
                else:
                    if cell.has_type(Point):
                        points_correct += 1
                    cell.reveal_switch()
            print(f"points_correct: {points_correct}")

            if points_correct == self.__total_points:
                is_game_over = True

        print("!~ Game Over ~!")
        print(board)

# =================================================================

engine = Engine(3, 3)
engine.run()

# this didnt turn out as i wanted it to work so its kinda a scraped idea now
# this also has fixed indexing (you dont have to put 0 and 0 to get the first cell, its now 1 and 1)