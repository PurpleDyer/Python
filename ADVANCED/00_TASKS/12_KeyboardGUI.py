from tkinter import *
from random import randint

# ==========================================================================================================================================

board = [
    ['esc'],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'ctrl'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', 'shift', 'alt', 'enter'],
    ['space']
]
Font_tuple = ("B Nazanin", 10, 'bold')
root = Tk()
content = ''
content2 = ''
cap = False

# ==========================================================================================================================================

def partial_function(text):
    
    def command():
        global content
        global content2

        # enter
        if text == 'Enter':
            content2 = ''
            content2 += '\n' 
            content = content2

        # alt
        elif text == 'Alt':
            pass

        # ctrl
        elif text == 'Ctrl':
            pass

        # shift
        elif text == 'Shift':
            global cap

            content = ''
            
            if cap:
                cap = False
            else:
                cap = True

        # space
        elif text == 'Space':
            content2 = ''
            content2 += ' ' 
            content = content2

        # esc
        elif text == 'Esc':
            global root
            content = ''
            root.destroy()

        # other keyboard inputs
        else:
            if cap:
                content2 = ''
                content2 += text 
                content = content2
            else:
                content2 = ''
                content2 += text.lower() 
                content = content2
        
        # printing
        print(f"{content}", flush=True, end="")
        
    return command

# ==========================================================================================================================================

for y, row in enumerate(board):
    for x, element in enumerate(row):
        button = Button(root, text=element, command=partial_function(element.title()), font=Font_tuple, width=10, height=5)
        if element == 'space':
            button.configure(width=10)
            button.grid(row=y, column=x, columnspan=10)
        else:
            button.grid(row=y, column=x)
        

# ==========================================================================================================================================

root.mainloop()

# this is a keyboard GUI that you can type with it (you can only type in the terminal not in an app or in your system)
# some keys like alt and ctrl dont work