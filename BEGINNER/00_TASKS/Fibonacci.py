"""
Fibonacci:
    next_number = first_number + second_number

The Swap:
    last_second_number => new_first_number
    last_next_number => new_second_number
"""

num1 = 1
num2 = 0
num3 = 0
n = 0

counter = int(input("Which Number Do You Want?: ")) # getting the number of numbers the user want the program to print

while n < counter: # n represents the number of numbers this program will print which we got from the user
    num3 = num1 + num2
    num1, num2 = num2, num3
    n += 1 # this prevents the infinite while-loop
    print(num3, end=" ")