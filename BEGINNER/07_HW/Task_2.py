my_list = [1,1,1,0,1,1]

counter = 0
person = 0

while True:

    if not person + 1 >= len(my_list):

        if not person + 2 >= len(my_list):

            if my_list[person + 2] == 1 or my_list[person + 1] == 0:
                person += 2

            else:
                person += 1

        else:
            person += 1

    else:
        break

    counter += 1
    
print(counter)