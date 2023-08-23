first_num, second_num = input("Please Enter The Range: ").split()

my_list = list(range(int(first_num),int(second_num)+1))
print(f"Sum: {sum(my_list)}")