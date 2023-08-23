# 97 => a
# 65 => A
# 90 => Z
# 122 => z
# this code cant add numbers to the random generated password which makes it a bit weaker
import random

string = "" # this is where the generated password is saved

for i in range(9):
    string += chr(random.randint(65,122)) # using the ascii code of the alphabet and some characters we generate the password 

print(string) # and finally printing the final result