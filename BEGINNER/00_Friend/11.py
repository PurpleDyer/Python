from random import randint

sum_yekan = 0
my_list = []
for i in range(5):
    a = randint(0, 50)
    my_list.append(a)
    sum_yekan += a%10

for i in my_list:
    flag = False
    if sum_yekan == i:
        flag = True
        break

print(my_list)
print(flag)
