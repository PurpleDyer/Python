import time

my_list = [1, 2, 3, 4, 5] # the list we want to rotate 

try:
    num, direction = input("Please Enter the Number of Rotation And The Direction: ").split(' ') # num is the number of times it will rotate and direction is the way of the rotation
except ValueError: # if the user gives us more or less that 2 values it will give them this error
    print("! Please Enter 2 Values Seperated By Space [Number Direction] !")
    time.sleep(3)

counter = 0

while counter < int(num):
    if direction == "RIGHT":
        my_list.insert(0, my_list.pop()) # if the direction is right, it will insert the last item to the first index of the list
    elif direction == "LEFT":
        my_list.append(my_list.pop(0)) # if the direction is left, it will add the first item to the last of the list
    else:
        print("Please Enter RIGHT or LEFT") # if the user didnt write left or right, it wil give them this error saying that it has to be right or left
        time.sleep(0.5)
        break
    counter += 1 # this prevents an infinite while-loop

print(f"Your New List: {my_list}") # and finally printing the last result