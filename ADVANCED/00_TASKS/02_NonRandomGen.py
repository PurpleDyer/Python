from random import randint

my_list = []     # we store the generated numbers in a list 
a = int(input())
counter = 0

print("---------------")
while counter < a:
    random_number = randint(1, a)
    if not random_number in my_list:   # and we check if the generated number is in that list or not
        my_list.append(random_number)
        counter += 1
        print(random_number)

print("---------------")

# this was just a practice and i was trying to understand how to make non repeated random generated numbers for a bigger project