from tkinter import *
from tkinter import ttk

# making the root
root = Tk()
# changing the title
root.title("PRACTICE")


# making the frame which its master is root
frame = Frame(root)
# putting the frame and showing it in the screen
frame.grid(row= 0, column= 0)


# making the label which its master is a frame
"""
label1 = Label(frame, text="Hello World!", padx=10, pady=10)
label1.grid(row=1, column=0)
"""

# making a button which its master is a frame
button1 = Button(frame, text="Click me", command=root.destroy, cursor="")
button1.pack()

button2 = Button(frame, text='hi', command=lambda: print('Hi'))
button2.pack()


# showing the screen and running the loop
root.mainloop()