a = int(input("Please Enter a Number: "))

my_list = ["Shanbe","Yekshanbe","Doshanbe","Seshanbe","ChaharShanbe","Panjshanbe","Jome"]

if not 0 < a < 8:
    print("Please Enter a Number From 1 to 7")
else:
    print(my_list[a-1])