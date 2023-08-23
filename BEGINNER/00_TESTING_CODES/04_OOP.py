CELL_WIDTH = 5
TOTAL_SHIPS_IN_BOARD = 0

# ===========================================================================

class Cell:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.__content = ["-"]
        self.__reveal = False

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


class ShipPart:
    def __init__(self):
        self.__character = "S"

    def __str__(self):
        return self.__character

    def add_to_board(self):
        global board
        board.get_cell(self.__x, self.__y).clear_cell()
        board.get_cell(self.__x, self.__y).add_content(str(ShipPart))

    @property
    def x(self):
        return self.__x

    @property 
    def y(self):
        return self.__y

    @property
    def character(self):
        return self.__character

        