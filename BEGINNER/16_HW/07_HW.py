num, direction = input("Please Enter The Amount Of Rotation And The Direction: ").split()
my_list = list(input("Please Enter Your List Of Numbers: ").split())
int_my_list = [int(x) for x in my_list]

if direction.upper() == "RIGHT":
    for _ in range(int(num)):
        int_my_list.insert(0, int_my_list.pop())
elif direction.upper() == "LEFT":
    for _ in range(int(num)):
        int_my_list.append(int_my_list.pop(0))
        
print(f"Your New List: {int_my_list}")