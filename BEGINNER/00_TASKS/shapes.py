shape = [[7], [1, 5.0, 1], [1, 5.0, 1], [7]]

for i in shape:
    idx = 0
    while idx < len(i):
        if isinstance(i[idx], int):
            print("o"*i[idx], end="")
        elif isinstance(i[idx], float):
            print(" "*int(i[idx]), end="")
        idx += 1
    print("\n")