import keyboard

my_list = ["=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "🚗", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "="]  # this list shows that where the car is 

print("-----------Game Start------------")

while True: # an infinite while loop so the player can play as much as they want
    car_idx = my_list.index("🚗") # getting the index that the car is in the list
    action_key = keyboard.read_key() 
    
    if keyboard.is_pressed(action_key):
        if action_key == "a":
            if car_idx == 0:
                pass
            else:
                my_list[car_idx-1], my_list[car_idx] = my_list[car_idx], my_list[car_idx-1] # if the player wants to go left we do a swap with the current-1 index and if it cant go left it will stay there

        elif action_key == "d":
            if car_idx == len(my_list)-1:
                pass
            else:
                my_list[car_idx+1], my_list[car_idx] = my_list[car_idx], my_list[car_idx+1] # if the player wants to go right we do a swap with the current+1 index and if it cant go right it will stay there

        elif action_key == "esc": # if the players wants to exit the game, this block of code breaks out of the while-loop
            break

    for i in my_list:
        print(i, end=" ") # printing the list so the player can see where the car is

    print("\n")

print("-----------Game Over------------")