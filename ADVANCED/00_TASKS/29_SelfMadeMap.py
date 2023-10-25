blueprint = [
    [' ', '=', ' ', ' ', ' ', '=', ' '],
    [' ', '=', ' ', '=', ' ', '=', ' '],
    [' ', '=', ' ', '=', ' ', '=', ' '],
    [' ', '=', ' ', '=', ' ', '=', ' '],
    [' ', '=', ' ', '=', ' ', '=', ' '],
    [' ', ' ', ' ', '=', ' ', ' ', ' '],
]
CELL_WIDTH = 5

# ===================================================================================

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

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def content(self):
        return self.__content

# ===================================================================================

board = None

# ===================================================================================

class Block:
    def __str__(self):
        return "-===-"

# ===================================================================================

def thrower(x, y, element):
    cell = Cell(x=x, y=y)
    if element == '=':
        cell.add_content(Block())
    return cell

# ===================================================================================

class Engine:
    def run(self):
        global board
        board = [[str(thrower(x=x, y=y, element=element)) for x, element in enumerate(row)] for y, row in enumerate(blueprint)]

        LINE = (((CELL_WIDTH + 1) * len(board[0])) + 1) * "-" + "\n"
        FINAL_BOARD = LINE
        for row in board:
            FINAL_BOARD +=  "|" + "|".join(map(lambda x: str(x).center(CELL_WIDTH), row)) + "|\n" + LINE
        print(FINAL_BOARD)
        
# ===================================================================================

engine = Engine()
engine.run()

# STATUS: FINISHED