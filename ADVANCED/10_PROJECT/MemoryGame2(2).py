import time
from random import randint
from tkinter import *

# ==============================================================================================================

CELL_WIDTH = 5
board = None
root = Tk()
frame = Frame(root)

# ==============================================================================================================

class Cell:
    def __init__(self, x, y):
        self.__x = x        
        self.__y = y
        self.__content = []    
        self.__reveal = False    
        
    def __str__(self):
        if self.__reveal:     
            return "-".join(map(str, self.__content))
        else:
            return ""    

    def add_content(self, element):     
        self.__content.append(element)

    def remove_content(self, element):     
        self.__content.remove(element)

    def clear_cell(self):       
        self.__content.clear()

    def has_type(self, typ):     
        for item in self.__content:
            if isinstance(item, typ):
                return True
        return False

    def give_content(self):     
        return self.__content

    def reveal_content(self):
        if self.__reveal:
            self.__reveal = False
        else:
            self.__reveal = True

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

# ==============================================================================================================

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

# ==============================================================================================================

class Engine:
    def __init__(self, board_width, board_height):
        self.__board_width = board_width
        self.__board_height = board_height

    def run(self):    
        global board
        board = Board(self.__board_width, self.__board_height) 
        
        generated_numbers_list = []     
        filled_spaces_counter = 0
        while filled_spaces_counter < (self.__board_width * self.__board_height): 

            while True:
                generated_number = randint(10, 99) 
                if not generated_number in generated_numbers_list:   
                    generated_numbers_list.append(generated_number)   
                    break

            cell = None
            while True:   
                random_x = randint(0, self.__board_width-1) 
                random_y = randint(0, self.__board_height-1) 
                cell = board.get_cell(random_x, random_y)
                if not cell.has_type(int):  
                    filled_spaces_counter += 1
                    break

            cell.add_content(generated_number//10) 
            cell.add_content(generated_number%10)

            while True:   
                random_x = randint(0, self.__board_width-1)   
                random_y = randint(0, self.__board_height-1)   
                cell = board.get_cell(random_x, random_y)
                if not cell.has_type(int):
                    filled_spaces_counter += 1
                    break

            cell.add_content(generated_number//10)
            cell.add_content(generated_number%10)

        correct_counter = 0 
        right_guess = None  
        while True:
            if right_guess != None:  
                print(right_guess)

            print(board)  

            if correct_counter == (self.__board_height * self.__board_width):
                break     

            while True:   
                x_input, y_input = input("Choose cell: ").split()  
                x_input, y_input = int(x_input)-1, int(y_input)-1   
                
                if (0 <= x_input < self.__board_width) and (0 <= y_input < self.__board_height):   
                    cell = board.get_cell(x_input, y_input)    

                    if cell.reveal == True:   
                        print("please enter a non selected cell")
                    else:    
                        cell.reveal_content()
                        break
                else:
                    print("out of range")

            print(board) 

            while True: 
                x_input, y_input = input("Choose cell: ").split()
                x_input, y_input = int(x_input)-1, int(y_input)-1

                if (0 <= x_input < self.__board_width) and (0 <= y_input < self.__board_height):
                    cell2 = board.get_cell(x_input, y_input)

                    if cell2.reveal == True:
                        print("please enter a non selected cell")
                    else:
                        cell2.reveal_content()
                        break
                else:
                    print("out of range")

            for y in range(self.__board_width):
                for x in range(self.__board_heght):
                    cell = board.get_cell(x=x, y=y)
                    button = Button(frame, text=str(cell), command=cell.reveal_content(), padx=10, pady=10)
                    button.grid(row=y, column=x)

            print(board)
            time.sleep(1) 

            if cell.give_content() != cell2.give_content(): 
                right_guess = "WRONG" 
                cell.reveal_content()  
                cell2.reveal_content()
            else:   
                right_guess = "CORRECT"
                correct_counter += 2 

            root.mainloop()
 
        print("!~ Game Over ~!")

# ===================================================================================================================

engine = Engine(4, 4)    
engine.run() 
