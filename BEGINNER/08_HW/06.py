my_list = ["orange", "banana", "apricot", "cucumber", "watermelon","orange"]

# Step One

counter = 0

for i in my_list:
    if i == "orange":
        counter += 1

print("oranges :", counter)

# Step Two

my_list_2 = []
index = 0

for i in my_list:
    if index + 1 > len(my_list):
        break
    else:
        my_list_2.append(my_list[index])
        index += 2

print(my_list_2)

# Step Three

my_list_3 = []
index = 1

for i in my_list:
    if index + 1 > len(my_list):
        break
    else:
        my_list_3.append(my_list[index])
        index += 2

print(my_list_3)

# Step Four

index = 0

for i in my_list:
    if i == "apricot":
        my_list.insert(index, "peach")
    index += 1

print("hi") # az inja be baad chizi print nemishe ????

# in file be bug khorde va run kardan ro be moshkel mindaze
# baraye fix run kardan barname ra yek bar baz o baste konid