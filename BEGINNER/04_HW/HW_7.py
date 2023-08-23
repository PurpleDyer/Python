# Farvardin = 31d    Mehr = 30d    Esfand = 29d

a = int(input("Please Enter a Month (In Number): "))

my_list = [31,31,31,31,31,31,30,30,30,30,30,29]

if 0 < a < 13:
    print(my_list[a-1], "Days")
else:
    print("Please Enter a Number From 1 to 12")