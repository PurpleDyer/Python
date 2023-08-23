from random import randint
"""
Classes:
    - Cell
    - Map
    - ShipPart
    - Engine
"""
CELL_WIDTH = 5
# ===============================================================================
#                                CLASS: CELL

class Cell:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__content = ["-"]
        self.reaval = True

    def __str__(self):
        if self.reaval:
            return "-".join(map(str, self.__content))
        else:
            return ""

    def add_content(self, elem):
        self.__content.append(elem)

    def clear_cell(self):
        self.__content.clear()

    def reveal_cell(self):
        self.reaval = True

    def has_type(self, typ):
        for i in self.__content:
            if isinstance(i, typ):
                return True
        return False

    @property
    def content(self):
        return self.__content
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
        
# ===============================================================================
#                                  CLASS: MAP

class Map:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height 
        self.__board = [[Cell(x,y) for x in range(self.__width)] for y in range(self.__height)]

    def __str__(self):
        """
        -----------------
        |   |   |   |   |
        -----------------
        |   |   |   |   |
        -----------------
        |   |   |   |   |
        -----------------
        """
        lines = (((CELL_WIDTH + 1) * self.__width) + 1) * "-" + "\n"
        new_board = lines

        for row in self.__board:
            new_board += "|" + "|".join(map(lambda x: str(x).center(CELL_WIDTH), row)) + "|\n" + lines 

        return new_board

    def get_cell(self, x, y):
        return self.__board[y][x]
    
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

# ===============================================================================
#                                    CLASS: SHIPPART

class ShipPart():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def add_to_board(self):
        global board
        board.get_cell(self.__x, self.__y).clear_cell()
        board.get_cell(self.__x, self.__y).add_content("S")

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

# ===============================================================================
#                                  CLASS: ENGINE

board = None

class Engine():
    def __init__(self, map_width, map_height, total_ships):
        self.__map_width = map_width
        self.__map_height = map_height
        self.__total_ships = total_ships

    
    def run(self):
        global board
        board = Map(self.__map_width, self.__map_height)


        ship_count = 0
        while ship_count < self.__total_ships:
            cx, cy = randint(0, self.__map_width-1), randint(0, self.__map_height-1)
            cell = board.get_cell(cx, cy)
            
            if not cell.has_type(ShipPart):
                sp = ShipPart(cx, cy)
                sp.add_to_board()
                ship_count += 1


        ships_destroyed = 0
        is_game_over = False
        print(board)
        while not is_game_over:
            x, y = list(map(int, input("Enter X and Y: ").split()))

            if (0 <= x < self.__map_width) and (0 <= y < self.__map_height):
                cell = board.get_cell(x, y)
                cell.reveal_cell()
                if cell.has_type(ShipPart):
                    ships_destroyed += 1

            if ships_destroyed == self.__total_ships:
                is_game_over = True
                print("YOU WON! GG!")
            print(board)
            print(f"ships destroyed: {ships_destroyed}")
# ===============================================================================
#                                 FINAL SETUP

engine = Engine(6, 6, 5)
engine.run()