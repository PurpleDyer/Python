from random import randint 

CELL_WIDTH = 5

class Cell:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__reveal = False
        self.__content = ['-']

    def __str__(self):
        if self.__reveal:
            return "-".join(map(str, self.__content))  # if reveal is true then we show the content of the cell
        else:
            return ""

    def add_content(self, element):  
        self.__content.append(element)  # for adding an element to the content of the cell

    def clear_cell(self):    # for clearing the content of the cell
        self.__content.clear()

    def remove_cell(self, elem):   # for removing a content from the content of the cell
        self.__content.remove(elem)

    def give_content(self):    # for getting the contents of the cell
        return self.__content

    def reveal_content(self):    # for revealing the content of the cell
        self.__reveal = True
 
    def has_typ(self, typ):     # for checking to see if the cell has a specific type or not
        for element in self.__content:
            if isinstance(element, typ):
                return True    # returns true if it has the type

        return False    # returns false if it doesnt have the type

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def reveal(self):
        return self.__reveal

    @property
    def content(self):
        return self.__reveal

# ================================================================

class Board:
    def __init__(self, board_width, board_height):
        self.__board_width = board_width
        self.__board_height = board_height
        self.__board = [[Cell(x=x, y=y) for x in range(self.__board_width)] for y in range(self.__board_height)]  # creating the board and making it a variable called board

    def __str__(self):
        LINE = (((CELL_WIDTH + 1) * self.__board_width) + 1) * "-" + "\n"
        final_board = LINE
        for row in self.__board:
            final_board +=  "|" + "|".join(map(lambda x: str(x).center(CELL_WIDTH), row)) + "|\n" + LINE   # organizing the board with dashes and vertical lines
        return final_board   

    def get_cell(self, x, y):      # for accessing a specific cell
        return self.__board[y][x]

    @property
    def board_width(self):
        return self.__board_width

    @property
    def board_height(self):
        return self.__board_height

    @property
    def board(self):
        return self.__board

# =================================================================

class ShipPart:
    def __init__(self):
        self.__hp = 1

    def __str__(self):
        return "S"

    def add_to_board(self, x, y):    # for addding a content to a cell
        global board
        cell = board.get_cell(x=x, y=y)
        cell.clear_cell()
        cell.add_content(ShipPart)

    def hp_damage(self):
            self.__hp -= 1

    @property
    def hp(self):
        return self.__hp



# ===================================================================

class Ship:
    def __init__(self, x: int, y: int, ship_direction: str):
        self.__x = x
        self.__y = y
        self.__ship_direction = ship_direction
        self.__ship_length = 3
        self.__hp = 0

    def create_ship(self):
        global board
        ship_length_counter = 0
        ship_length = 0
        while ship_length_counter < self.__ship_length:

            if (self.__ship_direction == 'left') and (0 <= self.__x < board.board_width):  # making the ship in the left direction
                if not board.get_cell(self.__x, self.__y).has_typ(ShipPart):
                    ship = ShipPart()
                    board.get_cell(self.__x, self.__y).clear_cell()
                    board.get_cell(self.__x, self.__y).add_content(ship)
                    self.__x -= 1
                    ship_length_counter += 1
                    ship_length += 1
                else:
                    break

            elif (self.__ship_direction == 'right') and (0 <= self.__x < board.board_width):   # making the ship in the right direction
                if not board.get_cell(self.__x, self.__y).has_typ(ShipPart):
                    ship = ShipPart()
                    board.get_cell(self.__x, self.__y).clear_cell()
                    board.get_cell(self.__x, self.__y).add_content(ship)
                    self.__x += 1
                    ship_length_counter += 1
                    ship_length += 1
                else:
                    break

            elif (self.__ship_direction == 'down') and (0 <= self.__y < board.board_height):   # making the ship in the down direction
                if not board.get_cell(self.__x, self.__y).has_typ(ShipPart):
                    ship = ShipPart()
                    board.get_cell(self.__x, self.__y).clear_cell()
                    board.get_cell(self.__x, self.__y).add_content(ship)
                    self.__y += 1
                    ship_length_counter += 1
                    ship_length += 1
                else:
                    break

            elif (self.__ship_direction == 'up') and (0 <= self.__y < board.board_height):   # making the ship in the up direction
                if not board.get_cell(self.__x, self.__y).has_typ(ShipPart):
                    ship = ShipPart()
                    board.get_cell(self.__x, self.__y).clear_cell()
                    board.get_cell(self.__x, self.__y).add_content(ship)
                    self.__y -= 1
                    ship_length_counter += 1
                    ship_length += 1
                else:
                    break
            else:
                ship_length_counter += 1
                
        self.__hp = ship_length
        
        
    def hp_damage(self):
        self.__hp -= 1

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def ship_direction(self):
        return self.__ship_direction

    @property
    def ship_length(self):
        return self.__ship_length

    @property
    def hp(self):
        return self.__hp

# ========================================================================

board = None

class Engine:
    def __init__(self, board_width: int, board_height: int, total_ships: int):
        self.__board_width = board_width
        self.__board_height = board_height 
        self.__total_ships = total_ships

    def run(self):
        global board
        board = Board(self.__board_width, self.__board_height)
        # randomly creates ships
        directions = {
            1: "up",
            2: "down",
            3: "right",
            4: "left"
        }
        total_ships_counter = 0
        total_ships = 0
        while total_ships_counter < self.__total_ships:
            random_direction = directions.get(randint(1,4))
            cx = randint(0, self.__board_width-1)
            cy = randint(0, self.__board_height-1)
            ship = Ship(cx, cy, random_direction)
            ship.create_ship()
            if not ship.hp == 0:
                total_ships += 1
            total_ships_counter += 1

        # the game itself
        ships_destroyed = 0
        print(board)
        while ships_destroyed < self.__total_ships:
            x, y = list(map(int, input("Enter X and Y: ").split()))
            cell = board.get_cell(x, y)

            if (0 <= x < self.__board_width) and (0 <= y < self.__board_height):
                if cell.reveal:
                    print("You have already chosen this cell")

                else: 
                    cell.reveal_content()
                    if cell.has_typ(ShipPart):
                        cell.give_content()[0].hp_damage()
                        print(cell.give_content()[0])

                # if not cell.give_content()[0].hp:
                #     ships_destroyed += 1
                
                
            print(f"total ships: {total_ships}")
            print(f"ships destroyed: {ships_destroyed}")
            print(board)

        print("GAME OVER")

#  ==========================================================================

engine = Engine(5, 5, 3)
engine.run()


'''

this code was going to be the best one but i couldnt do one thing
so this code DOES work but not how it should

'''