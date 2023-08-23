import time


my_list = [[2.0, 4, 7.0, 4], [1.0, 13], [1.0, 13], [3.0, 11], [6.0, 8], [9.0, 5], [11.0, 3]] # making a list of information which every float represents the number of spaces it should print and every int represents every character it needs to print

for i in my_list: # a for-loop that loops around the list of information
    idx = 0

    while idx < len(i):       # this avoids the IndexOutOfRange Error
        if isinstance(i[idx], float):
            print(" "*int(i[idx]), end="") 

        elif isinstance(i[idx], int):
            print("💖"*i[idx], end="")  # checks if the element is a float or an int and does the task it was supposed to do 

        idx += 1  # to avoid the infinite while loop

    print("\n") # prints a new line when the first line is done