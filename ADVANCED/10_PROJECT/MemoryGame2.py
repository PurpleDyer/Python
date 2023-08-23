from tkinter import *

root = Tk()
frame = Frame(root)

buttons = [
    'hi',
    'hello',
    'exit',
    'again'
]

index = 0
index2 = 0

def on_click():
    print('Hi!')

for y in range(2):
    for x in range(2):
        button = Button(text=buttons[index], command=on_click, padx=22, pady=22)
        button.grid(row=y, column=x)
        index += 1

root.mainloop()