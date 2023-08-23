# lost the question :(

walk = ['n', 'n', 'n', 'w', 's', 'e', 's', 's', 'w', 'e']
north = 0
west = 0
if len(walk) == 10:
    for element in walk:
        if element == "n":
            north += 1
        elif element == "s":
            north -= 1
        elif element == "w":
            west += 1
        else:
            west -= 1
else:
    print(False) 

if (north == 0) and (west == 0):
    print(True)
else:
    print(False)       