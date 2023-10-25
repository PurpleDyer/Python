from tkinter import Tk, Label, Button, mainloop, DISABLED, NORMAL  
from time import sleep
from threading import Thread

# ===========================================================================

board = [                                        
    ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', ' ', ' ', ' ', 'O', ' ', ' '],
    ['O', ' ', 'O', ' ', 'O', ' ', 'O'],
    ['O', ' ', 'O', ' ', 'O', ' ', 'O'],
    ['O', ' ', 'O', ' ', 'O', ' ', 'O'],
    [' ', ' ', 'O', ' ', ' ', ' ', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O']
]
root = Tk()   
Font_style = ("B Nazanin", 20, 'bold')  
total_towers = 2   
all_towers = [] 
all_enemies = []
is_game_over = False 

# ===========================================================================

class Path(Label):   
    def __init__(self, master=None, cnf={}, **kwargs):
        self.__content = []  
        super().__init__(master=master, cnf=cnf, **kwargs)

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

    @property
    def content(self):
        return self.__content

# ===========================================================================

class TPath(Button): 
    def __init__(self, master=None, cnf={}, **kwargs):
        self.__content = []
        super().__init__(master=master, cnf=cnf, **kwargs)

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

    @property
    def content(self):
        return self.__content

# ===========================================================================

class Enemy:
    def __init__(self, x, y):
        global main_board

        self.__x = x  
        self.__y = y  
        self.__movingTo = 'r'  
        self.__damage = 10  

        main_board[self.__y][self.__x].configure(text=self)  
        all_enemies.append(self)

    def __str__(self):
        return str(self.__damage)   

    def move(self):
        global main_board
        sleep(1)
        
        if (self.__movingTo != 'u') and (0 <= self.__y+1 < len(main_board)) and (main_board[self.__y+1][self.__x].cget('text') == ' ') and (self.__damage > 0): 
                main_board[self.__y][self.__x].configure(text=' ')
                main_board[self.__y][self.__x].remove_content(self)
                self.__y += 1
                main_board[self.__y][self.__x].configure(text=self)
                main_board[self.__y][self.__x].add_content(self)
                self.__movingTo = 'd'

        elif (self.__movingTo != 'd') and (0 <= self.__y-1 < len(main_board)) and (main_board[self.__y-1][self.__x].cget('text') == ' ') and (self.__damage > 0): 
                main_board[self.__y][self.__x].configure(text=' ')
                main_board[self.__y][self.__x].remove_content(self)
                self.__y -= 1
                main_board[self.__y][self.__x].configure(text=self)
                main_board[self.__y][self.__x].add_content(self)
                self.__movingTo = 'u'

        else: 
            if (0 <= self.__x+1 < len(main_board)) and (main_board[self.__y][self.__x+1].cget('text') == ' ') and (self.__damage > 0):
                main_board[self.__y][self.__x].configure(text=' ')
                main_board[self.__y][self.__x].remove_content(self)
                self.__x += 1
                main_board[self.__y][self.__x].configure(text=self)
                main_board[self.__y][self.__x].add_content(self)
                self.__movingTo = 'r'

    def take_damage(self): 
        global main_board
        
        if self.__damage > 0:
            self.__damage -= 1
            print(self.__damage)

    def remove_self(self):  
        global main_board

        main_board[self.__y][self.__x].remove_content(Enemy)
        main_board[self.__y][self.__x].configure(text=' ')

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

    @property
    def damage(self):
        return self.__damage

# ===========================================================================

class Tower:  
    tower_range = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (1, 0),
        (-1, 1),  (0, 1),   (1, 1)     
    ]

    def __init__(self, x, y):
        global main_board

        self.__x = x   
        self.__y = y   

        main_board[self.__y][self.__x].configure(text=self)   
        all_towers.append(self)

    def __str__(self):
        return 'T'    

    def attack(self):   
        global main_board

        for x, y in self.tower_range: 

            if (0 <= self.__x+x < len(main_board[0])) and (0 <= self.__y+y < len(main_board)):  
                
                if (main_board[self.__y+y][self.__x+x].has_type(Enemy)) and (main_board[self.__y+y][self.__x+x].content[0].damage > 0):
                    main_board[self.__y+y][self.__x+x].content[0].take_damage()  
                    print("damaged") 

# ===========================================================================

def partial_function(btn: Button, x, y):  
    def command():
        global total_towers

        if total_towers > 0:
            tower = Tower(x=x, y=y)  
            btn.configure(state=DISABLED)   
            total_towers -= 1 

    return command

# ===========================================================================

def throw(x, y, master, text):
    global board
    
    if board[y][x] == 'O':  
        button = TPath(master=master, width=8, height=4, background="white", font=Font_style) 
        button.configure(command=partial_function(button, x, y))
        button.grid(column=x, row=y)
        return button  

    elif board[y][x] == ' ': # راه دشمنان
        label = Path(master=master, text=text, width=8, height=4, background="red", font=Font_style)
        label.grid(column=x, row=y)
        return label 

# ===========================================================================

main_board = [[throw(x=x, y=y, master=root, text=element) for x, element in enumerate(row)] for y, row in enumerate(board)] 

# ===========================================================================

def creator():
    global is_game_over

    while not is_game_over:
        try:
            Enemy(0, 5)

        except RuntimeError:
            break

        else:
            sleep(8)

def mover():  
    global is_game_over

    while not is_game_over:
        if len(all_enemies) > 0: 
            for enemy in all_enemies:
                if enemy.damage > 0: 
                    enemy.move()  
                else:
                    enemy.remove_self() 

                if (enemy.x == 6) and (enemy.y == 1): 
                    is_game_over = True
                    
                    root.destroy()

def damager(): 
    global is_game_over

    while not is_game_over:
        if len(all_towers) > 0:  
            sleep(0.5)
            for tower in all_towers:
                tower.attack() 

# ===========================================================================

creator_thread = Thread(target=creator) 
mover_thread = Thread(target=mover)
damager_thread = Thread(target=damager)

creator_thread.start()
mover_thread.start()
damager_thread.start()

# ===========================================================================

root.mainloop() 

# ===========================================================================

# results: 95% complete
# problem: all characters dont move at the same time (but its better now)
# reason: time.sleep() in Enemy.move() [maybe a thread can fix the problem]
# recommendation: FIX PROBLEM