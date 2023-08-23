my_list = [int(i) for i in input().split()]
flag = True
for i in my_list:
    if i%10 > max(my_list)%10:
        flag = False
        break
if flag:
    print(flag)
else:
    print(flag)