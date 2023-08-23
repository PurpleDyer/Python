import random 

lowers = "abcdefghijklmnopqrstuvwxyz" # a string of words in the alphabet in lower
uppers = lowers.upper() # the same as above but all upper
numbers = "1234567890" # a string of numbers
characters = "!@#$%^&*_+=-" # a string of some characters
my_list = list(lowers + uppers + numbers + characters) # making a list out of them all 
genpass = "" # this is where the generated password will be stored

for _ in range(9): # we dont need the variable so we put it as a "_"
    genpass += my_list[random.randint(0, len(my_list)-1)] # the generated password will be a random index in the list of lowers and uppers and numbers and characters

print(genpass) # and finally we print the generated password