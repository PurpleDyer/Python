a = int(input())
flag = True

for i in range(2, a//2):
    if a%i == 0:
        flag = False
        break

if flag:
    print("its a prime number")
else:
    print("its not a prime number")
