CELL_WIDTH = 5

# ===========================================================================

class Cell:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.__content = ["X"]
        self.__reveal = True

    def __str__(self):
        if self.__reveal:
            return "-".join(map(str, self.__content))
        else:
            return ""

    def add_content(self, elem: str):
        self.__content.append(elem)

    def clear_cell(self):
        self.__content.clear()

    def reaval_cell(self):
        self.__reveal = True

    def has_typ(self, typ: object):
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

    @property
    def reveal(self):
        return self.__reveal

# =============================================================================

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

    def get_cell(self, x: int, y: int):
        return self.__board[y][x]

    @property
    def board_width(self):
        return self.__board_width

    @property 
    def board_height(self):
        return self.__board_height  

# =============================================================================

class ShipPart:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.__character = "[]"

    def __str__(self):
        return self.__character

    def add_to_board(self):
        global board
        board.get_cell(self.__x, self.__y).clear_cell()
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

# ===========================================================================

class Ship:
    def __init__(self, direction: str, ship_length: int):
        self.__direction = direction
        self.__ship_length = ship_length

    def ship_creator(self, x, y):
        global board
        ship_length_counter = 0
        while ship_length_counter < self.__ship_length:
            if (self.__direction == 'left') and (0 <= x-1 < board.board_width):
                ship = ShipPart(x, y)
                ship.add_to_board()
                x -= 1
                ship_length_counter += 1
            elif (self.__direction == 'down') and (0 <= y+1 < board.board_height):
                ship = ShipPart(x, y)
                ship.add_to_board()
                y += 1
                ship_length_counter += 1

board = Board(5, 5)
print("hi")
ship = Ship("down", 3)
ship.ship_creator(5, 5)
print(board)