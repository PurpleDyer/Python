name, _ = input("Please Enter The Name: ").split()
my_list = list(input("Please Enter The Scores: ").split())

if name.upper() == "HASSAN":
    new_list = list(filter(lambda x: int(x) > 15, my_list))
    if len(new_list) == 0:
        print(f"Your Avg Score: 20")
    else:
        print(f"Your Avg Score: {sum([int(x) for x in new_list]) / len(new_list)}")
else:
    print(f"Your Avg Score: {sum([int(x) for x in my_list]) / len(my_list)}")  