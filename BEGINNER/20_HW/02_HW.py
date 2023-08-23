text = input("Please Enter The Text: ")
max1 = ['None', '0']
max2 = ['None', '0']
d = {}

for i in text:
    if i in d.keys():
        d[i] += 1
    else:
        d.update({i: 1})

for key, item in d.items():
    if int(max1[1]) <= item:
        max2 = max1.copy()
        max1[0], max1[1] = key, item

print(f"Most Repeated Word: {max1} | Second Most Repeated Word: {max2}")