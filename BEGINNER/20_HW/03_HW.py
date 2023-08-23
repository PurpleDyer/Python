text = input("Please Enter The Text: ").split()
num = int(input("How Many Times It Should Be Repeated?: "))
d = {}
my_list = []

for i in text:
    if i in d.keys():
        d[i] += 1
    else:
        d.update({i: 1})

for key, item in d.items():
    if item == num:
        my_list.append(key)

print(f"Letters with {num} time(s) repeat: {my_list}")