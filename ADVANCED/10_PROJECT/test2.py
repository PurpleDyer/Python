from tkinter import *
from random import randint, shuffle

# ===============

root = Tk()
frame = Frame(root)
frame.grid(row=0, column=0)
Font_tuple = ("Comic Sans MS", 20, "bold")
text_for_button = None

# ===============

sequence = []
counter = 0
while counter < 8:
    random_number = randint(0, 20)
    if not random_number in sequence:
        sequence.append(random_number)
        counter += 1
sequence.extend(sequence)
shuffle(sequence)
print(sequence)

# ===============

def partial_function(text, index):
    reveal = False
    def command():
        global text_for_button
        nonlocal reveal

        # if reveal:   # true
        #     button.config(text=text)
        #     reveal = False

        # else:  # false
        #     button.config(text=' ')
        #     reveal = True

        print(text)
        # if text == ' ':
        #     text_for_button = sequence[index]
        # else:
        #     text_for_button = ' '

    return command

# ===============

buttons = []
for number in sequence:
    index = sequence.index(number)
    button = Button(frame, padx=10, pady=10, width=10, height=5, font=Font_tuple, text=number, command=partial_function(number, index))
    print(f"text for button: {text_for_button}")
    buttons.append(button)

# ===============

index = 0
for y in range(4):
    for x in range(4):
        buttons[index].grid(row=y, column=x)
        index += 1
    
# ===============

root.mainloop()