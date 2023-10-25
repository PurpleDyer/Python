import threading
from time import sleep
from random import randint
import keyboard

# ==============================================================================

CELL_WIDTH = 5
maze_blueprint = [
    ['S', '=', ' ', '=', '=', '='],
    [' ', '=', ' ', ' ', ' ', '='],
    [' ', '=', '=', '=', ' ', '='],
    [' ', ' ', ' ', ' ', ' ', ' '],
    ['=', '=', ' ', '=', ' ', '='],
    [' ', ' ', ' ', '=', ' ', 'E'],
]
keys = ['w', 'a', 's', 'd']
total_fires = 20
maze = None
start = None
end = None
current_board = None

# ==============================================================================

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

    def clear_cell(self):
        self.__content.clear()

    def remove_type(self, typ):
        for element in self.__content:
            if isinstance(element, typ):
                self.__content.remove(element)
                break

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def content(self):
        return self.__content

# ==============================================================================

class Prefire:
    def __str__(self):
        return "-"

# ==============================================================================

class Fire:
    def __str__(self):
        return "⁑"

# ==============================================================================

class Board:
    fires = []

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

    def clear_all_cells(self):
        for row in self.__board:
            for cell in row:
                cell.clear_cell()

    def fill_with_fire(self):
        fire_filler_counter = 0
        while fire_filler_counter < total_fires:
            random_x, random_y = randint(0, self.__board_width-1), randint(0, self.__board_height-1)
            cell = self.get_cell(random_x, random_y)
            if (not cell.has_type(Prefire)) and (not cell.has_type(Character)):
                cell.add_content(Prefire())
                self.fires.append((random_x, random_y))
                fire_filler_counter += 1

        self.clear_all_cells()
        
        sleep(1.5)
        for x, y in self.fires:
            self.get_cell(x=x, y=y).add_content(Fire())
        sleep(1.5)
        self.fires.clear()
        self.clear_all_cells()

    @property
    def width(self):
        return self.__board_width

    @property
    def height(self):
        return self.__board_height

    @property
    def board(self):
        return self.__board

# ==============================================================================

class Wall:
    def __str__(self):
        return "="

# ==============================================================================

class Start:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

# ==============================================================================

class End:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

# ==============================================================================

class Character:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "0"

    def move(self, direction):
        global current_board

        if current_board != None:
            if keyboard.is_pressed(direction):
                if (direction == "right") and (0 <= self.__x+1 < current_board.width) and (not current_board.get_cell(self.__x+1, self.__y).has_type(Wall)):
                    current_board.get_cell(self.__x, self.__y).remove_content(self)
                    self.__x += 1
                    current_board.get_cell(self.__x, self.__y).add_content(self)

                elif (direction == "left") and (0 <= self.__x-1 < current_board.width) and (not current_board.get_cell(self.__x-1, self.__y).has_type(Wall)):
                    current_board.get_cell(self.__x, self.__y).remove_content(self)
                    self.__x -= 1
                    current_board.get_cell(self.__x, self.__y).add_content(self)

                elif (direction == 'up') and (0 <= self.__y-1 < current_board.height) and (not current_board.get_cell(self.__x, self.__y-1).has_type(Wall)):
                    current_board.get_cell(self.__x, self.__y).remove_content(self)
                    self.__y -= 1
                    current_board.get_cell(self.__x, self.__y).add_content(self)

                elif (direction == 'down') and (0 <= self.__y+1 < current_board.height) and (not current_board.get_cell(self.__x, self.__y+1).has_type(Wall)):
                    current_board.get_cell(self.__x, self.__y).remove_content(self)
                    self.__y += 1
                    current_board.get_cell(self.__x, self.__y).add_content(self)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

# ==============================================================================

def thrower(x, y, element):
    cell = Cell(x=x, y=y)

    if element == 'S':
        global start
        start = Start(x=x, y=y)

    elif element == 'E':
        global end
        end = End(x=x, y=y)

    elif element == "=":
        cell.add_content(str(Wall()))
    
    return cell
        
# ==============================================================================

maze = [[thrower(x=x, y=y, element=element) for x, element in enumerate(row)] for y, row in enumerate(maze_blueprint)]

# ==============================================================================

class Engine:
    def __init__(self, f_board_width, f_board_height, switch_sleep):
        self.__f_board_width = f_board_width
        self.__f_board_height = f_board_height
        self.__switch_sleep = switch_sleep

    def run(self):
        global maze, start, end

        character = Character(start.x, start.y)
        maze[character.y][character.x].add_content(character)

        is_game_over = False
        timer_counter = -3

        def printer():
            global current_board
            current_board = maze
            while not is_game_over:
                print(current_board)
                sleep(1)

        def reader():
            while True:
                key = keyboard.read_key()
                if key in keys:
                    character.move(key)
                elif key == 'esc':
                    nonlocal is_game_over
                    is_game_over = True
                    break
            
        def timer():
            nonlocal timer_counter
            while not is_game_over:
                sleep(1)
                timer_counter += 1
                if timer_counter % self.__switch_sleep == 0:
                    char_x, char_y = character.x, character.y
                    board = Board(self.__f_board_width, self.__f_board_height)
                    board.get_cell(char_x, char_y).add_content(character)
                    global current_board
                    current_board = board
                    board.fill_with_fire()
                    current_board = maze
                    
        printer_thread = threading.Thread(target=printer)
        reader_thread = threading.Thread(target=reader)
        timer_thread = threading.Thread(target=timer)

        printer_thread.start()
        reader_thread.start()
        timer_thread.start()

# ==============================================================================

engine = Engine(10, 10, 5)
engine.run()

# status: UNFINISHED