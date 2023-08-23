import random

while True: # creating a infinite while-loop so the user can play as much as they want
    a = input("Guess the number between [1, 2, 3] or write stop to end the game: ") # asking the user to guess a number
    b = random.randint(1, 3) # making a random number between 1, 2 and 3
    if a.lower() == "stop": 
        break    # when ever the input the user gave us is 'stop' it will break out of the loop resulting the end of the game
    elif a == str(b):
        print("CORRECT!", "---------------------------", sep="\n")
    elif a != str(b):
        print("INCORRECT!", "---------------------------", sep="\n") # the last 4 lines are for checking if the input and the created random number is the same or not