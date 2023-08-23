from tkinter import *
from random import randint
import time

# ================================================================================================================

buttons = ['rock', 'paper', 'scissors']
root = Tk()
Font_tuple = ("B Nazanin", 20, "bold") 
your_score = 0
opponents_score = 0
draws = 0

# ================================================================================================================

def creation(element):
    global your_score, opponents_score, draws
    opp = buttons[randint(0, 2)]
    print(f"opponents choice: {opp}")
    if ((element == 'paper') and (opp == 'rock')) or ((element == 'scissors') and (opp == 'paper')) or ((element == 'rock') and (opp == 'scissors')):
        print("YOU WIN")
        your_score += 1
    elif element == opp:
        print("DRAW")
        draws += 1
    else:
        print("YOU LOSE")
        opponents_score += 1
    print('--------------------')

# ================================================================================================================

def partial_function(text):
    def command():
        creation(text)
    return command

# ================================================================================================================

for x, button in enumerate(buttons):
    btn = Button(master=root, width=20, height=10, text=button, font=Font_tuple, command=partial_function(button))
    btn.grid(row=1, column=x)

# ================================================================================================================

root.mainloop()
print(f"Your Score: {your_score}\nOpponents Score: {opponents_score}\nTotal Draws: {draws}")