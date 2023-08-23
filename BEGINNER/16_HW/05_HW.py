my_list = list(input("Please Enter Your Numbers: ").split())

for i in range(len(my_list)):
    my_list[i] = pow(int(my_list[i]), 2)
print(my_list)