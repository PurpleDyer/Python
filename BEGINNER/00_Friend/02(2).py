a = int(input())
b = int(input())
c = int(input())
max_dahgan = 0
max_yekan = 0

if (a/10)%10 >= (b/10)%10 and (a/10)%10 >= (c/10)%10:
    max_dahgan = a
elif (b/10)%10 >= (a/10)%10 and (b/10)%10 >= (c/10)%10:
    max_dahgan = b
elif (c/10)%10 >= (a/10)%10 and (c/10)%10 >= (b/10)%10:
    max_dahgan = c
else:
    print("all numbers are the same")

if max_dahgan%10 >= a%10 and max_dahgan%10 >= b%10 and max_dahgan%10 >= c%10:
    print("Yes")
else:
    print("No")