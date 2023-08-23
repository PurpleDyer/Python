my_list = []

for i in range(3):
    my_list.append(int(input("Please Enter a Number: ")))

print("Sum",sum(my_list), sep = ' : ')
print("Min Number",min(my_list), sep = ' : ')
print("Max Number",max(my_list), sep = ' : ')