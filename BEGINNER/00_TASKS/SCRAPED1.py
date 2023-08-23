"""        

             |‾‾‾‾‾‾‾‾|
|‾‾‾|_|‾‾‾‾‾‾          ‾‾‾‾‾‾‾|  ____
|                             |_|    |_|‾‾‾|
|___|‾|                              |‾|___|
      |                       |‾|    |
  |‾‾‾|                       | |    |_|‾‾‾|
  |                           | |    |‾|___|
  |   |                       |  ‾‾‾‾
   ‾‾‾ ‾‾‾|  |‾‾‾‾‾‾‾‾|  |‾‾| |______
         |‾  ‾|      |‾  ‾| |        |
   |‾‾‾| |    |      |    | |        |
   |   |_|    |      |    | |        |
   |   |‾|    |      |    |  ‾‾‾‾‾‾‾‾
   |___| |    |      |    |
         |    ||‾‾‾‾||    |
         |    ||    ||    |
         |       @        |
         |____||____||____|
         
    - the |, _ and ‾ are walls and you can not go through them
    - 0 is the character you are controlling
"""
import keyboard

while True:
    flag = True
    a = input("Where?: ").upper()
    game_map = open("MAP1.txt","r")
    my_list = game_map.read().replace("â€¾", "‾").splitlines()
    char = []
    for index1, *item1 in enumerate(my_list):
        for index2, item2 in enumerate(my_list[index1]):
            if item2 == "@":
                char = [index1, index2]   # index1: line in MAP1.txt file       index2: the index that the numbers 0 or your character is in
                flag = False
                break
        if flag == False:
            break
    print(char)

    action_key = keyboard.read_key()
    

    # if a == "R" and my_list[char[0][char[1]]+1] == " ":
    #     my_list[char[0][char[1]]+1], my_list[char[0][char[1]]] = "0", " "

    if keyboard.is_pressed(action_key):


    # elif a == "L" and my_list[char[0][char[1]]-1] == " ":
    #     my_list[char[0][char[1]]-1], my_list[char[0][char[1]]] = "0", " "

    elif a == "L":
        if char[1] != 0:
            if my_list[char[0]][char[1]-1] == " ":
                my_list[char[0]][char[1]], my_list[char[0]][char[1]-1] = my_list[char[0]][char[1]-1], my_list[char[0]][char[1]]

    # elif a == "U" and my_list[char[0]-1[char[1]]] == " ":
    #     my_list[char[0]-1[char[1]]], my_list[char[0][char[1]]] = "0", " "
    elif a == "U":
        if char[0] != 0:
            if my_list[char[0]-1][char[1]] == ' ':
                my_list[char[0]][char[1]], my_list[char[0]-1][char[1]] = my_list[char[0]-1][char[1]], my_list[char[0]][char[1]]

    # elif a == "D" and my_list[char[0]+1[char[1]]] == " ":
    #     my_list[char[0]+1[char[1]]], my_list[char[0][char[1]]] = "0", " "

    elif a == "D":
        if char[0] != len(my_list):
            if my_list[char[0]+1][char[1]] == " ":
                my_list[char[0]][char[1]], my_list[char[0]][char[1]+1] = my_list[char[0]+1][char[1]], my_list[char[0]][char[1]]


    last_string = ""
    map_rewrite = open("MAP1.txt", "w") # opening the file as a "write" type

    for i in my_list:
        idx = 0
        while idx < len(i):
            last_string += i[idx] + " "
            idx += 1
        last_string += "\n"               # saving all the changed information in a string called "last_string"
    
    rewrite.write(last_string)

# ! THIS CODE DOES NOT WORK !