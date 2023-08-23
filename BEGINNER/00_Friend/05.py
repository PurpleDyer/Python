for a in range(100, 1000):
    flag = True
    for i in range(2, a//2):
        if a%i == 0:
            flag = False
            break
    if flag:
        print(a)