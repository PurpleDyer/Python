from random import randint
import time
import threading
import keyboard

# =========================================================================================================================================

board = None
CELL_WIDTH = 5

# =========================================================================================================================================

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

    def clear_cell(self):
        self.__content.clear()

    def give_content(self, element):
        return self.__content

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

# =========================================================================================================================================

class Board:
    def __init__(self, board_width, board_height):
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

# =========================================================================================================================================

class Block:
    def __init__(self):
        self.__character = '-===-'

    def __str__(self):
        return self.__character

    @property
    def character(self):
        return self.__character

# =========================================================================================================================================

class Enemy:
    Enemies = []

    def __init__(self, x, y):
        self.__x = x 
        self.__y = y
        self.Enemies.append((self, self.__x, self.__y))   # (ENEMY, X, Y)

    def __str__(self):
        return '.'

    @classmethod
    def give_cords(cls):
        return cls.Enemies

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

# =========================================================================================================================================

class Character:
    Explosion_range = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__total_explosions = 4
        self.__total_assasinations = 4

    def __str__(self):
        return 'T'

    def move(self, direction):
        global board 

        if keyboard.is_pressed(direction):
            if (direction == 'right') and (0 <= self.__x+1 < board.width) and not (board.get_cell(self.__x+1, self.__y).has_type(Block)):
                board.get_cell(self.__x, self.__y).remove_content(self)
                self.__x += 1
                board.get_cell(self.__x, self.__y).add_content(self)

            elif (direction == 'left') and (0 <= self.__x-1 < board.width) and not (board.get_cell(self.__x-1, self.__y).has_type(Block)):
                board.get_cell(self.__x, self.__y).remove_content(self)
                self.__x -= 1
                board.get_cell(self.__x, self.__y).add_content(self)

            elif (direction == 'up') and (0 <= self.__y-1 < board.height) and not (board.get_cell(self.__x, self.__y-1).has_type(Block)):
                board.get_cell(self.__x, self.__y).remove_content(self)
                self.__y -= 1
                board.get_cell(self.__x, self.__y).add_content(self)

            elif (direction == 'down') and (0 <= self.__y+1 < board.height) and not (board.get_cell(self.__x, self.__y+1).has_type(Block)):
                board.get_cell(self.__x, self.__y).remove_content(self)
                self.__y += 1
                board.get_cell(self.__x, self.__y).add_content(self)

    def explode(self):
        global board

        if self.__total_explosions > 0:
            self.__total_explosions -= 1

            for x, y in self.Explosion_range:
                cell = board.get_cell(self.__x+x, self.__y+y)
                
                if (0 <= self.__x+x < board.width) and (0 <= self.__y+y < board.width) and not (cell.has_type(Enemy)):
                    cell.clear_cell()

    def assasinate(self):
        global board

        if self.__total_assasinations > 0:
            self.__total_assasinations -= 1 
            assasinations = 0
            board.get_cell(self.__x, self.__y).remove_content(self)  # removing the character from its location

            while (assasinations < 5) and len(Enemy.Enemies) > 0:
                enemy, x, y = Enemy.Enemies[0]  # getting the enemy information
                Enemy.Enemies.pop(0)  # removing the used information
                cell = board.get_cell(x, y)  # getting the cell of the enemys location
                cell.remove_content(enemy)  # removing the enemy from the location 
                cell.add_content(self)  # adding the character to that location (so it looks like our character killed the enemy and teleported threr)
                time.sleep(0.5 )  # we see the character in the cell for this amount of seconds
                cell.remove_content(self)  # removing the character from the cell
                assasinations += 1
            
            board.get_cell(self.__x, self.__y).add_content(self)  # adding the character again 

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def total_explosions(self):
        return self.__total_explosions

    @property
    def total_assasinations(self):
        return self.__total_assasinations

# =========================================================================================================================================

class Engine:
    def __init__(self, board_width, board_height, total_blocks, total_enemies):
        self.__board_width = board_width
        self.__board_height = board_height
        self.__total_blocks = total_blocks
        self.__total_enemies = total_enemies

    def run(self):
        global board

        board = Board(self.__board_width, self.__board_height)
        character = Character(0, 0)
        board.get_cell(character.x, character.y).add_content(character)

        total_blocks_counter = 0
        while total_blocks_counter < self.__total_blocks:
            random_x, random_y = randint(0, self.__board_width-1), randint(0, self.__board_height-1)
            cell = board.get_cell(random_x, random_y)
            if not (cell.has_type(Block)) and not (cell.has_type(Character)):
                cell.add_content(Block())
                total_blocks_counter += 1

        total_enemies_counter = 0
        while total_enemies_counter < self.__total_enemies:
            random_x, random_y = randint(0, self.__board_width-1), randint(0, self.__board_height-1)
            cell = board.get_cell(random_x, random_y)
            if not (cell.has_type(Block)) and not (cell.has_type(Character)) and not (cell.has_type(Enemy)):
                cell.add_content(Enemy(random_x, random_y))
                total_enemies_counter += 1

        is_game_over = False

        def printer():
            while not is_game_over:     #   why isnt is_game_over working??
                print(f"Explosions Left: {character.total_explosions}")
                print(f"Assassinations Left: {character.total_assasinations}")
                print(board)
                time.sleep(0.004876)

        def getter():
            global is_game_over

            while True:
                key = keyboard.read_key()
                if keyboard.is_pressed(key):
                    
                    if key == 'shift':
                        character.explode()

                    elif key == 'space':
                        character.assasinate()

                    elif key == 'esc':
                        is_game_over = True
                        break

                    else:
                        character.move(key)

        printer_thread = threading.Thread(target=printer)
        getter_thread = threading.Thread(target=getter)

        printer_thread.start()
        getter_thread.start()

# =========================================================================================================================================

engine = Engine(10, 10, 20, 20)
engine.run()