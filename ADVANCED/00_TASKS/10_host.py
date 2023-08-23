import socket as s
import keyboard
from random import randint
from time import sleep

# =====================================================================================================================

host = s.gethostbyname(s.gethostname())
port = 12345

so = s.socket()
so.bind((host, port))

so.listen(1)
print("LISTENING...")

# =====================================================================================================================

CELL_WIDTH = 5
board = None

class Cell:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__content = []
        
    def __str__(self):
        return "-".join(map(str, self.__content))

    def add_content(self, element):
        self.__content.append(element)

    def remove_content(self, element):
        if element in self.__content:
            self.__content.remove(element)

    def clear_cell(self):
        self.__content.clear()

    def has_type(self, typ):
        for element in self.__content:
            if isinstance(element, typ):
                return True
        return False

    def give_content(self):
        return self.__content

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

# =====================================================================================================================

class Board:
    def __init__(self, board_width, board_height):
        self.__board_width = board_width
        self.__board_height = board_height
        self.__board = [[Cell(x=x, y=y) for x in range(self.__board_width) for y in range(self.__board_height)]]

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

# =====================================================================================================================

class Block:
    def __init__(self):
        self.__character = '-===-'

    def __str__(self):
        return self.__character

# =====================================================================================================================

class Character:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__character = '0'

    def __str__(self):
        return self.__character

    def move(self, direction):
        if keyboard.is_pressed(direction):
            if (direction == 'right') and (0 <= self.__x+1 < board.wdith) and not (board.get_cell(self.__x+1, self.__y).has_type(Block)):
                board.get_cell(self.__x, self.__y).clear_cell()
                self.__x += 1
                board.get_cell(self.__x, self.__y).add_content(str(Character))

            elif (direction == 'left') and (0 <= self.__x-1 < board.width) and not (board.get_cell(self.__x-1, self.__y).has_type(Block)):
                board.get_cell(self.__x, self.__y).clear_cell()
                self.__x -= 1
                board.get_cell(self.__x, self.__y).add_content(str(Character))

            elif (direction == 'up') and (0 <= self.__y-1 < board.height) and not (board.get_cell(self.__x, self.__y-1).has_type(Block)):
                board.get_cell(self.__x, self.__y).clear_cell()
                self.__y -= 1
                board.get_cell(self.__x, self.__y).add_content(str(Character))
            
            elif (direction == 'down') and (0 <= self.__y+1 < board.height) and not (board.get_cell(self.__x, self.__y+1).has_type(Block)):
                board.get_cell(self.__x, self.__y).clear_cell()
                self.__y += 1
                board.get_cell(self.__x, self.__y).add_content(str(Character))

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def character(self):
        return self.__character

# =====================================================================================================================

class Engine:
    def __init__(self, board_width, board_height, total_blocks):
        self.__board_width = board_width
        self.__board_height = board_height
        self.__total_blocks = total_blocks

    def run(self):
        global board
        global so

        try:
            conn, addr = so.accept()
            print(f"{addr[0]} joined the game")

            message = "CONNECTION ESTABLISHED"
            conn.send(message.encode('ascii'))

        except ConnectionResetError:
            print("CONNECTION LOST")
            conn.close()

        else:
            character = Character()
            board = Board(self.__board_width, self.__board_height)
            board.get_cell(character.x, character.y).add_content(character)

            total_blocks_counter = 0
            while total_blocks_counter < self.__total_blocks:
                random_x = randint(0, self.__board_width)
                random_y = randint(0, self.__board_height)

                if not (board.get_cell(random_x, random_y).has_type(Block)) and not (board.get_cell(random_x, random_y).has_type(Character)):
                    cell.add_content(str(Block))
                    total_blocks_counter += 1

            while True:
                conn.send(board.encode('ascii'))
                direction = conn.recv(1024).decode('ascii')

                if direction == 'esc':
                    break
                else:
                    character.move(direction)

                sleep(0.25)

        print("!~ Game Over ~!")

# =====================================================================================================================

engine = Engine(10, 10, 25)
engine.run()

# failed in sending the board (this means that making a host socket server was done correctly)