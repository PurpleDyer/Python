from random import randint

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

# =============================================================================

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
    def character(self):
        return self.__character

# ===========================================================================

class Ship:
    def __init__(self, direction: str):
        self.__direction = direction
        self.__ship_length = 3

    def ship_creator(self, x, y):
        global board
        global TOTAL_SHIPS_IN_BOARD
        ship_length_counter = 0
        while ship_length_counter < self.__ship_length:
            if (self.__direction == 'left') and (0 <= x < board.board_width):
                if board.get_cell(x, y).has_typ(ShipPart):
                    break
                else:
                    ship = ShipPart()
                    board.get_cell(x, y).clear_cell()
                    board.get_cell(x, y).add_content(ship)
                    x -= 1
                    ship_length_counter += 1
                    TOTAL_SHIPS_IN_BOARD += 1
            elif (self.__direction == 'right') and (0 <= x < board.board_width):
                if board.get_cell(x, y).has_typ(ShipPart):
                    break
                else:
                    ship = ShipPart()
                    board.get_cell(x, y).clear_cell()
                    board.get_cell(x, y).add_content(ship)
                    x += 1
                    ship_length_counter += 1
                    TOTAL_SHIPS_IN_BOARD += 1
            elif (self.__direction == 'down') and (0 <= y < board.board_height):
                if board.get_cell(x, y).has_typ(ShipPart):
                    break
                else:
                    ship = ShipPart()
                    board.get_cell(x, y).clear_cell()
                    board.get_cell(x, y).add_content(ship)
                    y += 1
                    ship_length_counter += 1
                    TOTAL_SHIPS_IN_BOARD += 1
            elif (self.__direction == 'up') and (0 <= y < board.board_height):
                if board.get_cell(x, y).has_typ(ShipPart):
                    break
                else:
                    ship = ShipPart()
                    board.get_cell(x, y).clear_cell()
                    board.get_cell(x, y).add_content(ship)
                    y -= 1
                    ship_length_counter += 1
                    TOTAL_SHIPS_IN_BOARD += 1
            else:
                ship_length_counter += 1

# ===========================================================================

board = None

class Engine:
    def __init__(self, board_width: int, board_height: int, total_ships: int):
        self.__board_width = board_width    
        self.__board_height = board_height
        self.__total_ships = total_ships

    def run(self):
        global board
        global TOTAL_SHIPS_IN_BOARD
        board = Board(self.__board_width, self.__board_height)
        # randomly creates ships
        directions = {
            1: "up",
            2: "down",
            3: "right",
            4: "left"
        }
        total_ships_counter = 0
        while total_ships_counter < self.__total_ships:
            random_direction = directions.get(randint(1,4))
            cx = randint(0, self.__board_width-1)
            cy = randint(0, self.__board_height-1)
            ship = Ship(random_direction)
            ship.ship_creator(cx, cy)
            total_ships_counter += 1

        # the game itself
        ships_destroyed = 0
        print(board)
        while ships_destroyed < TOTAL_SHIPS_IN_BOARD:
            x, y = list(map(int, input("Enter X and Y: ").split()))
            if (0 <= x < self.__board_width) and (0 <= y < self.__board_height):
                cell = board.get_cell(x, y)
                cell.reaval_cell()

                if cell.has_typ(ShipPart):
                    print("HI")
                    ships_destroyed += 1

            print(ships_destroyed)
            print(board)
        print("GAME OVER")

# =========================================================================

engine = Engine(5, 5, 3)
engine.run()

'''

this code counts all the shipParts and when you destroyed all of them the game will end
this code does not support ship destructions

'''